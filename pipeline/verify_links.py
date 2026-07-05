#!/usr/bin/env python3
"""校验未核实条目的链接:抓取目标页标题,和演出艺人/标题做匹配。

不匹配 => link_ok=false,build_site 会把这些卡片排除出站点(宁可不上线,不可错链接)。
用法: python3 pipeline/verify_links.py [--all 重查全部,默认只查 link_ok 缺失的]
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVENTS_FILE = ROOT / "data" / "events.json"
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)


def page_title(url: str) -> str | None:
    # 先直连,拿不到再走 Jina
    try:
        p = subprocess.run(
            ["curl", "-sL", "--max-time", "20", "--compressed",
             "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36", url],
            capture_output=True, text=True, timeout=30, errors="replace")
        m = TITLE_RE.search(p.stdout or "")
        if m:
            return m.group(1).strip()[:200]
    except Exception:
        pass
    try:
        p = subprocess.run(["curl", "-s", "--max-time", "40", f"https://r.jina.ai/{url}"],
                           capture_output=True, text=True, timeout=50, errors="replace")
        for line in (p.stdout or "").splitlines()[:5]:
            if line.startswith("Title:"):
                return line[6:].strip()[:200]
    except Exception:
        pass
    return None


def page_content(url: str) -> str:
    """Jina渲染全文(处理JS单页应用),失败返回空串"""
    try:
        p = subprocess.run(["curl", "-s", "--max-time", "50", f"https://r.jina.ai/{url}"],
                           capture_output=True, text=True, timeout=60, errors="replace")
        return (p.stdout or "")[:20000]
    except Exception:
        return ""


def tokens(e: dict) -> list[str]:
    """取艺人/标题里的显著词: 连续CJK段(>=2字)和拉丁词(>=3字符)"""
    blob = f"{e.get('artist') or ''} {e.get('title_zh') or ''} {e.get('title_en') or ''}"
    toks = re.findall(r"[一-鿿]{2,}|[A-Za-z]{3,}", blob)
    stop = {"演唱会", "巡回", "巡演", "世界", "澳洲", "澳大利亚", "悉尼", "墨尔本", "珀斯",
            "布里斯班", "音乐会", "脱口秀", "开放麦", "见面会", "粉丝", "专场", "Tour",
            "World", "Live", "Concert", "站"}
    return [t for t in toks if t not in stop][:6]


def main():
    recheck_all = "--all" in sys.argv
    db = json.loads(EVENTS_FILE.read_text())
    checked = ok = bad = 0
    for e in db["events"]:
        # verified 条目同样校验(种子数据也出过首页链接的雷),结果缓存,不重复抓
        if not recheck_all and "link_ok" in e:
            continue
        # 首页级 ticket_url 不指向具体演出,剥掉让标题回退到信源链接
        from urllib.parse import urlparse
        if e.get("ticket_url") and urlparse(e["ticket_url"]).path.strip("/") in ("", "search"):
            print(f"⚠ 剥离首页级购票链接: {(e.get('title_zh') or '')[:24]} | {e['ticket_url']}")
            e["ticket_url"] = None
        url = e.get("ticket_url") or e.get("source_url")
        name = (e.get("title_zh") or e.get("title_en") or "")[:24]
        if not url:
            e["link_ok"] = False
            e["link_note"] = "无链接"
            bad += 1
            print(f"✗ {name} | 无链接")
            continue
        title = page_title(url)
        checked += 1
        if title is None:
            e["link_ok"] = None  # 抓取失败,暂不判死刑,下次重试
            e.pop("link_note", None)
            print(f"? {name} | 页面抓取失败,待重试")
            continue
        toks = tokens(e)
        hit = any(t.lower() in title.lower() for t in toks)
        stage = "标题"
        if not hit:
            # 二次校验: JS渲染全文找艺人(单页应用/标题无艺人名的场景)
            body = page_content(url)
            hit = bool(body) and any(t.lower() in body.lower() for t in toks)
            stage = "全文"
        e["link_ok"] = hit
        e["link_note"] = None if hit else f"页面不含艺人/演出名: {title[:60]}"
        ok += hit
        bad += not hit
        print(f"{'✓' if hit else '✗'} [{stage}] {name} | {title[:50]}")
    EVENTS_FILE.write_text(json.dumps(db, ensure_ascii=False, indent=2))
    print(f"\n校验{checked} | 通过{ok} | 不匹配{bad}(link_ok=false 的条目不会出现在站点)")


if __name__ == "__main__":
    main()
