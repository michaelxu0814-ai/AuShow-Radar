#!/usr/bin/env python3
"""给缺图的演出条目补海报: 从 ticket_url / source_url 页面抓 og:image。

用法: python3 pipeline/enrich.py [--retry]  (--retry 会重试之前失败过的条目)
best-effort: 抓不到就记 null,前端自动用占位图,不影响展示。
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVENTS_FILE = ROOT / "data" / "events.json"
OG_RE = re.compile(
    r'<meta[^>]+(?:property|name)=["\']og:image(?::secure_url)?["\'][^>]+content=["\']([^"\']+)["\']'
    r'|<meta[^>]+content=["\']([^"\']+)["\'][^>]+(?:property|name)=["\']og:image["\']',
    re.I,
)


def is_homepage(url: str) -> bool:
    # 裸域名首页的og:image是站点通图,不是活动海报,跳过
    from urllib.parse import urlparse
    return urlparse(url).path.strip("/") == ""


def og_image(url: str) -> str | None:
    if is_homepage(url):
        return None
    try:
        p = subprocess.run(
            ["curl", "-sL", "--max-time", "25", "--compressed",
             "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
             url],
            capture_output=True, text=True, timeout=35, errors="replace",
        )
        m = OG_RE.search(p.stdout or "")
        if m:
            img = (m.group(1) or m.group(2)).strip()
            if img.startswith("http"):
                return img
    except Exception:
        pass
    return None


def main():
    retry = "--retry" in sys.argv
    db = json.loads(EVENTS_FILE.read_text())
    changed = 0
    for e in db["events"]:
        if e.get("image"):
            continue
        if "image" in e and not retry:  # 已尝试过且失败
            continue
        img = None
        for url in filter(None, [e.get("ticket_url"), e.get("source_url")]):
            img = og_image(url)
            if img:
                break
        e["image"] = img
        changed += 1
        print(f"{'✓' if img else '✗'} {e.get('title_zh') or e.get('title_en')}")
    EVENTS_FILE.write_text(json.dumps(db, ensure_ascii=False, indent=2))
    print(f"\nprocessed {changed} events -> {EVENTS_FILE}")


if __name__ == "__main__":
    main()
