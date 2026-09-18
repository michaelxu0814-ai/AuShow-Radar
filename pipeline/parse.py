#!/usr/bin/env python3
"""用 claude CLI 从 data/raw/<日期>/ 的原始文本中抽取条目,合并进 data/events.json

两条线,按 sources.json 里每个源的 scope 选提示词:
  scope=shows(默认) -> 悉尼/墨尔本华语演出
  scope=local       -> 布里斯班本地吃喝玩乐 / 亲子周末活动
抽到的条目会被打上 scope 字段(由源决定,不由 LLM 决定),build_site.py 据此分区展示。

用法: python3 pipeline/parse.py [日期,默认今天]
去重: ①prompt里带同 scope 的已收录清单让LLM跳过 ②艺人模糊匹配+城市+日期兜底 ③标题前12字精确键。
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
SOURCES_FILE = ROOT / "sources.json"

COMMON_RULES = """规则:
- 只抽取文本中明确写出的信息,不要推断或编造。缺失字段用 null。
- 没有明确名称(title)的条目不要输出;没有任何可跳转链接(ticket_url或source_url)的条目不要输出。
- 已结束的活动(日期早于{today})跳过。
- 每场活动输出一个对象,城市不同算不同场次。
- 下面「已收录清单」里的条目不要再输出——即使标题写法不同,只要是同一主体同一城市的同一场就算已收录。

已收录清单:
{known}
"""

PROMPT_SHOWS = """你是演出信息抽取器。从下面的原始网页/搜索结果文本中,抽取澳大利亚的华语/华人受众演出信息(演唱会、脱口秀、开放麦、话剧、音乐会、粉丝见面会)。

""" + COMMON_RULES + """- status: on_sale=明确已开票 / announced=已官宣未开票 / tbc=信息不完整待核实

只输出 JSON 数组,不要任何其他文字。字段:
title_zh, title_en, artist, category(演唱会|脱口秀|开放麦|话剧|音乐会|见面会|其他), city(悉尼|墨尔本|其他), venue, date(YYYY-MM-DD或null), time, recurrence(如"每周二",否则null), price, ticket_platform, ticket_url, status, source_url

原始文本:
"""

PROMPT_LOCAL = """你是本地活动信息抽取器。从下面的原始网页/搜索结果文本中,抽取**布里斯班及周边(黄金海岸/阳光海岸)**面向华人家庭与年轻人的线下活动:周末市集、夜市与美食活动、亲子遛娃(儿童工作坊、图书馆故事会、动物园/农场活动)、节庆与烟火、展览与博物馆特展、免费户外活动、华人社群节庆。

""" + COMMON_RULES + """- **只收录有具体时间的活动**:要么有明确日期,要么有明确的固定场次(如"每周六 6am-12pm")。常年开放的景点、餐厅、商场本身不是活动,不要输出。
- 纯广告、团购、代购、房产/移民/招聘推广一律不输出。
- 免费活动把 price 写成"免费"、status 写成 free;要买票的照常写价格与平台。
- 亲子类活动优先写清适龄信息(放进 notes,如"3-8岁"),没写就 null。
- artist 一律 null(本地活动没有艺人),主办方写进 notes。
- status: free=免费入场无需买票 / on_sale=已开票在售 / announced=已官宣未开票 / tbc=信息不完整待核实

只输出 JSON 数组,不要任何其他文字。字段:
title_zh, title_en, artist, category(市集|美食|亲子|展览|节庆|户外|工作坊|演出|其他), city(布里斯班|黄金海岸|阳光海岸|其他), venue, date(YYYY-MM-DD或null), time, recurrence(如"每周六",否则null), price, ticket_platform, ticket_url, status, source_url, notes

原始文本:
"""

PROMPTS = {"shows": PROMPT_SHOWS, "local": PROMPT_LOCAL}


def source_scopes() -> dict:
    """source_id -> scope(缺省 shows)"""
    try:
        srcs = json.loads(SOURCES_FILE.read_text())["sources"]
    except Exception:
        return {}
    return {s["id"]: s.get("scope", "shows") for s in srcs}


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


def extract(raw_text: str, known: str, scope: str) -> list:
    prompt = (PROMPTS[scope].replace("{today}", date.today().isoformat())
                            .replace("{known}", known) + raw_text[:12000])
    p = subprocess.run(
        ["claude", "-p", prompt, "--model", "claude-opus-5", "--output-format", "text"],
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


def known_list(events: list, scope: str, today: str) -> str:
    """同 scope 的未过期条目(有日期的取未来,加上常驻/待定),最多 80 条"""
    same = [e for e in events if e.get("scope", "shows") == scope]
    live = [e for e in same if not e.get("date") or e["date"] >= today]
    return "\n".join(
        f"- {e.get('title_zh') or e.get('title_en')} | {e.get('city')} | "
        f"{e.get('date') or e.get('recurrence') or '日期未定'}"
        for e in live[-80:]
    ) or "(暂无)"


def main():
    day = sys.argv[1] if len(sys.argv) > 1 else date.today().isoformat()
    raw_dir = ROOT / "data" / "raw" / day
    if not raw_dir.exists():
        sys.exit(f"no raw data at {raw_dir}, run fetch.py first")

    db = json.loads(EVENTS_FILE.read_text()) if EVENTS_FILE.exists() else {"events": []}
    existing = {dedupe_key(e) for e in db["events"]}
    scopes = source_scopes()
    known_cache = {s: known_list(db["events"], s, day) for s in PROMPTS}

    added = {s: 0 for s in PROMPTS}
    for f in sorted(raw_dir.glob("*.txt")):
        scope = scopes.get(f.stem, "shows")
        if scope not in PROMPTS:
            print(f"skip {f.name}: unknown scope {scope}")
            continue
        print(f"parsing {f.name} (scope={scope}) ...")
        try:
            items = extract(f.read_text(), known_cache[scope], scope)
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
            e["scope"] = scope       # 由源决定,不采信 LLM 自称
            e["verified"] = False    # 新抓取条目默认未人工核实
            e["added"] = day
            db["events"].append(e)
            existing.add(dedupe_key(e))
            added[scope] += 1
            print(f"  + [{scope}] {e.get('title_zh')} @ {e.get('city')} {e.get('date') or e.get('recurrence')}")

    db["updated"] = day
    EVENTS_FILE.write_text(json.dumps(db, ensure_ascii=False, indent=2))
    total = sum(added.values())
    detail = " / ".join(f"{s} {n}" for s, n in added.items())
    print(f"\n{total} new events ({detail}) -> {EVENTS_FILE}(verified=false 的条目请人工核对后改 true)")


if __name__ == "__main__":
    main()
