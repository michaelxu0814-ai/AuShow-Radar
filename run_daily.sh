#!/bin/zsh
# 澳华演出雷达 每日更新: 抓取 -> LLM解析 -> 补海报 -> 生成站点 -> (有远程仓库则自动发布)
# 由 launchd 每天 09:00 调用(com.aushow.daily),也可手动跑: ./run_daily.sh
cd "$(dirname "$0")"
mkdir -p logs
LOG="logs/$(date +%F).log"
{
  echo "===== run_daily $(date '+%F %T') ====="

  echo "--- [1/4] fetch"
  python3 pipeline/fetch.py || echo "fetch FAILED(继续)"

  echo "--- [2/4] parse (claude CLI)"
  python3 pipeline/parse.py || echo "parse FAILED(继续)"

  echo "--- [3/4] enrich images"
  python3 pipeline/enrich.py || echo "enrich FAILED(继续)"

  echo "--- [4/4] build site"
  python3 pipeline/build_site.py

  # 已配置 git 远程仓库时自动提交发布(GitHub Pages 即自动更新)
  if git rev-parse --git-dir >/dev/null 2>&1 && git remote get-url origin >/dev/null 2>&1; then
    git add -A
    git commit -m "daily update $(date +%F)" >/dev/null 2>&1 && git push && echo "pushed to origin"
  else
    echo "no git remote, site updated locally only"
  fi

  echo "===== done $(date '+%F %T') ====="
} >> "$LOG" 2>&1
