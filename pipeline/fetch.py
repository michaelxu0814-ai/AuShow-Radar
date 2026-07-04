#!/usr/bin/env python3
"""抓取 sources.json 里的所有信息源,原始文本存到 data/raw/<日期>/<source_id>.txt

用法: python3 pipeline/fetch.py [--only source_id]
依赖: mcporter(Exa)、curl(Jina)、opencli(小红书,可选)。全部缺席时对应源跳过。
"""
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw" / date.today().isoformat()


def run(cmd: list[str], timeout: int = 90, cwd: str | None = None) -> tuple[bool, str]:
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=cwd)
        out = p.stdout.strip()
        if p.returncode != 0 or not out:
            return False, (out or p.stderr.strip())[:500]
        return True, out
    except FileNotFoundError:
        return False, f"command not found: {cmd[0]}"
    except subprocess.TimeoutExpired:
        return False, "timeout"


def fetch_exa(query: str) -> tuple[bool, str]:
    call = f'exa.web_search_exa(query: "{query}", numResults: 8)'
    # mcporter 的 exa 配置按 cwd 解析,必须在家目录下运行
    return run(["mcporter", "call", call], timeout=120, cwd=str(Path.home()))


def fetch_jina(url: str) -> tuple[bool, str]:
    return run(["curl", "-s", "--max-time", "60", f"https://r.jina.ai/{url}"])


def fetch_xhs(query: str) -> tuple[bool, str]:
    ok, out = run(["opencli", "xiaohongshu", "search", query, "-f", "yaml"])
    if ok and "AUTH_REQUIRED" in out:
        return False, "小红书未登录(在OpenCLI所连的Chrome里登录xiaohongshu.com后重跑)"
    return ok, out


def main():
    only = sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == "--only" else None
    sources = json.loads((ROOT / "sources.json").read_text())["sources"]
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    results = []
    for s in sources:
        if only and s["id"] != only:
            continue
        method = s["method"]
        if method == "exa":
            ok, out = fetch_exa(s["query"])
        elif method == "jina":
            ok, out = fetch_jina(s["url"])
        elif method == "xhs":
            ok, out = fetch_xhs(s["query"])
        else:
            ok, out = False, f"unknown method {method}"
        if ok:
            (RAW_DIR / f"{s['id']}.txt").write_text(out)
        results.append((s["id"], "ok" if ok else f"SKIP: {out[:120]}"))
        print(f"[{results[-1][1][:4]}] {s['id']}")

    failed = [r for r in results if r[1] != "ok"]
    print(f"\n{len(results) - len(failed)}/{len(results)} sources fetched -> {RAW_DIR}")
    for sid, msg in failed:
        print(f"  - {sid}: {msg}")


if __name__ == "__main__":
    main()
