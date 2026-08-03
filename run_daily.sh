#!/bin/zsh
# 澳华演出雷达 每日更新: 抓取 -> LLM解析 -> 补海报 -> 生成站点 -> (有远程仓库则自动发布)
# 由 launchd 每天 09:00 调用(com.aushow.daily),也可手动跑: ./run_daily.sh
cd "$(dirname "$0")"
mkdir -p logs
LOG="logs/$(date +%F).log"

# 2026-08-03: 主账号Claude月度用量106%超限,临时切DeepSeek(Anthropic兼容接口)
# 跑pipeline/parse.py里的claude调用,不影响其他会话。凭证来自CC-Switch本地配置
# (~/.cc-switch/cc-switch.db)。额度恢复后删掉下面三行export即可回退。
export ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
export ANTHROPIC_AUTH_TOKEN="sk-2df46abe788c4d29aef75f21ede23581"
export ANTHROPIC_MODEL="DeepSeek-V4-pro"

{
  echo "===== run_daily $(date '+%F %T') ====="

  echo "--- [1/4] fetch"
  python3 pipeline/fetch.py || echo "fetch FAILED(继续)"

  echo "--- [2/4] parse (claude CLI)"
  python3 pipeline/parse.py || echo "parse FAILED(继续)"

  echo "--- [3/5] verify links (质量闸门)"
  python3 pipeline/verify_links.py || echo "verify FAILED(继续)"

  echo "--- [4/5] enrich images"
  python3 pipeline/enrich.py || echo "enrich FAILED(继续)"

  echo "--- [5/5] build site"
  python3 pipeline/build_site.py

  # 已配置 git 远程仓库时自动提交发布(GitHub Pages 即自动更新)
  if git rev-parse --git-dir >/dev/null 2>&1 && git remote get-url origin >/dev/null 2>&1; then
    git add -A
    git commit -m "daily update $(date +%F)" >/dev/null 2>&1
    # 显式用 michaelxu0814-ai 账号推送(gh 全局 active account 常被 AUComplianceAI 那边切成 UEXU,
    # 导致 push 被拒),token 现取现用不落盘
    if git push "https://michaelxu0814-ai:$(gh auth token -u michaelxu0814-ai)@github.com/michaelxu0814-ai/AuShow-Radar.git" HEAD:main; then
      echo "pushed to origin"
    fi
  else
    echo "no git remote, site updated locally only"
  fi

  echo "===== done $(date '+%F %T') ====="
} >> "$LOG" 2>&1

# 失败告警: 任一环节FAILED或push未发生 -> 写入组合例外队列 + 系统通知
if grep -q "FAILED" "$LOG" || ! grep -q "pushed to origin\|no git remote" "$LOG"; then
  ISSUE=$(grep -m1 "FAILED" "$LOG" || echo "push未完成")
  echo "- $(date +%F) | AuShow | run_daily 异常: $ISSUE | 查 logs/$(date +%F).log" >> /Users/reanne/Projects/EXCEPTIONS.md
  osascript -e "display notification \"run_daily 异常,已写入例外队列\" with title \"AuShow Radar\"" 2>/dev/null
fi
