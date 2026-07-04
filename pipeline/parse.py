#!/usr/bin/env python3
"""用 claude CLI 从 data/raw/<日期>/ 的原始文本中抽取演出条目,合并进 data/events.json

用法: python3 pipeline/parse.py [日期,默认今天]
去重: ①prompt里带已收录清单让LLM跳过 ②艺人模糊匹配+城市+日期兜底 ③标题前12字精确键。
已有条目不覆盖,只新增,人工审核后再改。
"""
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVENTS_FILE = ROOT / "data" / "events.json"

PROMPT = """你是演出信息抽取器。从下面的原始网页/搜索结果文本中,抽取澳大利亚的华语/华人受众演出信息(演唱会、脱口秀、开放麦、话剧、音乐会、粉丝见面会)。

规则:
- 只抽取文本中明确写出的信息,不要推断或编造。缺失字段用 null。
- 没有明确演出名称(title)的条目不要输出;没有任何可跳转链接(ticket_url或source_url)的条目不要输出。
- 已结束的活动(日期早于{today})跳过。
- 每场演出输出一个对象,城市不同算不同场次。
- status: on_sale=明确已开票 / announced=已官宣未开票 / tbc=信息不完整待核实
- 下面「已收录清单」里的演出不要再输出——即使标题写法不同,只要是同一艺人同一城市的同一场/同一巡演就算已收录。

已收录清单:
{known}

只输出 JSON 数组,不要任何其他文字。字段:
title_zh, title_en, artist, category(演唱会|脱口秀|开放麦|话剧|音乐会|见面会|其他), city(悉尼|墨尔本|其他), venue, date(YYYY-MM-DD或null), time, recurrence(如"每周二",否则null), price, ticket_platform, ticket_url, status, source_url

原始文本:
"""


def norm(s: str) -> str:
    return re.sub(r"[^\w一-鿿]+", "", (s or "").lower())


def fuzzy_dup(e: dict, events: list) -> bool:
    """艺人(或标题)互相包含 + 同城 + 同日期(或新条目无日期) => 视为同一场"""
    a = norm(e.get("artist") or e.get("title_zh"))
    if not a:
        return False
    for x in events:
        if e.get("city") != x.get("city"):
            continue
        if e.get("date") and x.get("date") and e["date"] != x["date"]:
            continue
        b = norm(x.get("artist") or x.get("title_zh"))
        if b and (a in b or b in a):
            return True
    return False


def extract(raw_text: str, known: str) -> list:
    prompt = (PROMPT.replace("{today}", date.today().isoformat())
                    .replace("{known}", known) + raw_text[:12000])
    p = subprocess.run(
        ["claude", "-p", prompt, "--output-format", "text"],
        capture_output=True, text=True, timeout=300,
    )
    out = p.stdout.strip()
    # 容错: 剥掉可能的 ```json 包裹
    if out.startswith("```"):
        out = out.split("```")[1].removeprefix("json").strip()
    start, end = out.find("["), out.rfind("]")
    if start == -1 or end == -1:
        raise ValueError(f"no JSON array in output: {out[:200]}")
    return json.loads(out[start : end + 1])


def dedupe_key(e: dict) -> tuple:
    return ((e.get("title_zh") or "")[:12], e.get("date"), e.get("city"))


def main():
    day = sys.argv[1] if len(sys.argv) > 1 else date.today().isoformat()
    raw_dir = ROOT / "data" / "raw" / day
    if not raw_dir.exists():
        sys.exit(f"no raw data at {raw_dir}, run fetch.py first")

    db = json.loads(EVENTS_FILE.read_text()) if EVENTS_FILE.exists() else {"events": []}
    existing = {dedupe_key(e) for e in db["events"]}
    known = "\n".join(
        f"- {e.get('title_zh') or e.get('title_en')} | {e.get('city')} | {e.get('date') or '日期未定'}"
        for e in db["events"][-80:]
    ) or "(暂无)"

    added = 0
    for f in sorted(raw_dir.glob("*.txt")):
        print(f"parsing {f.name} ...")
        try:
            items = extract(f.read_text(), known)
        except Exception as err:
            print(f"  FAILED: {err}")
            continue
        for e in items:
            # 硬门槛: 无标题或无任何链接的条目直接丢弃(LLM偶尔不守规则)
            if not (e.get("title_zh") or e.get("title_en")):
                continue
            if not (e.get("ticket_url") or e.get("source_url")):
                continue
            if dedupe_key(e) in existing or fuzzy_dup(e, db["events"]):
                continue
            e["verified"] = False  # 新抓取条目默认未人工核实
            e["added"] = day
            db["events"].append(e)
            existing.add(dedupe_key(e))
            added += 1
            print(f"  + {e.get('title_zh')} @ {e.get('city')} {e.get('date')}")

    db["updated"] = day
    EVENTS_FILE.write_text(json.dumps(db, ensure_ascii=False, indent=2))
    print(f"\n{added} new events -> {EVENTS_FILE}(verified=false 的条目请人工核对后改 true)")


if __name__ == "__main__":
    main()
