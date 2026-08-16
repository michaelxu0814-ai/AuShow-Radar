#!/bin/zsh
# AuShow Radar 小红书内容每日自动生产 + 推送 Telegram
# 由 launchd 每天调用(com.aushow.xhs-daily),也可手动跑: ./run_daily_xhs.sh
#
# 架构说明(2026-08-16):内容/文案由 claude -p 生成,渲染出图交给确定性脚本
# automation/render_card.py(headless Chrome CLI + PIL裁切),不依赖
# chrome-devtools-mcp——当天实测那条路径的截图工具反复超时/卡死,不适合无人值守自动化。
cd "$(dirname "$0")"

LOGDIR="automation/logs"
mkdir -p "$LOGDIR"
LOG="$LOGDIR/$(date +%F).log"
PROMPT_FILE="automation/daily-xhs-prompt.md"
CONTENT_DIR="content"
TG_TOKEN="8652002284:AAHUQM-Ljf9WJ0Qxk2bM8aQRYmkgX0BbUJM"
TG_CHAT="6591241918"
TG_PREFIX="🎫 AuShow:"

BEFORE_FILES=$(ls "$CONTENT_DIR"/*-xhs-copy.md 2>/dev/null | sort)

{
  echo "===== run_daily_xhs $(date '+%F %T') ====="
  caffeinate -s -i claude -p "$(cat "$PROMPT_FILE")" \
    --model claude-opus-5 \
    --dangerously-skip-permissions \
    --output-format text \
    --add-dir "$HOME/Projects" \
    || echo "FAILED: claude 非零退出"
  echo "===== claude done $(date '+%F %T') ====="
} >> "$LOG" 2>&1

AFTER_FILES=$(ls "$CONTENT_DIR"/*-xhs-copy.md 2>/dev/null | sort)
NEW_FILE=$(comm -13 <(echo "$BEFORE_FILES") <(echo "$AFTER_FILES"))

send_tg_text() {
  curl -s -X POST "https://api.telegram.org/bot${TG_TOKEN}/sendMessage" \
    -d chat_id="${TG_CHAT}" \
    -d text="$1" >/dev/null 2>&1
}

fail_and_log() {
  local reason="$1"
  echo "FAILED: $reason" >> "$LOG"
  echo "- $(date +%F) | AuShow | run_daily_xhs 异常: $reason | 查 $LOG" >> "$HOME/Projects/EXCEPTIONS.md"
  osascript -e "display notification \"run_daily_xhs 异常,已写入例外队列\" with title \"AuShow Radar\"" 2>/dev/null
  send_tg_text "${TG_PREFIX} ⚠️ 今天的内容生成失败：${reason}。详情见 ${LOG}"
}

if [ -z "$NEW_FILE" ]; then
  fail_and_log "没有产出新的 NNN-xhs-copy.md 文件(claude 可能在中途放弃或卡在某一步)"
  exit 1
fi

# 事实核查硬性关卡(不依赖模型自我报告)
STATUS_LINE=$(grep -m1 "^FACT-AUDIT-STATUS:" "$NEW_FILE" 2>/dev/null)
RED_VAL=$(echo "$STATUS_LINE" | grep -oE "RED=[0-9]+" | cut -d= -f2)
CHECKED_VAL=$(echo "$STATUS_LINE" | grep -oE "CHECKED=[0-9]+" | cut -d= -f2)
SOURCES_VAL=$(echo "$STATUS_LINE" | grep -oE "SOURCES-CITED=[0-9]+" | cut -d= -f2)

if [ -z "$STATUS_LINE" ] || [ "$RED_VAL" != "0" ] || [ -z "$CHECKED_VAL" ] || \
   [ "$CHECKED_VAL" = "0" ] || [ "$CHECKED_VAL" != "$SOURCES_VAL" ]; then
  fail_and_log "$(basename "$NEW_FILE") 缺少有效的 FACT-AUDIT-STATUS 确认行(RED=0且核查数=来源数),今天内容不可信"
  exit 1
fi

# 找到对应的编号和 HTML
POST_NUM=$(basename "$NEW_FILE" | grep -oE "^[0-9]+")
CARD_HTML="content/cards/${POST_NUM}/index.html"
CARD_OUT="content/cards/${POST_NUM}/output"

if [ ! -f "$CARD_HTML" ]; then
  fail_and_log "找不到 $CARD_HTML,claude 写完文案但没建卡片 HTML"
  exit 1
fi

# 确定性渲染(headless Chrome + PIL,不依赖交互式浏览器会话)
RENDER_LOG=$(python3 automation/render_card.py "$CARD_HTML" "$CARD_OUT" "xhs-${POST_NUM}" 2>&1)
echo "$RENDER_LOG" >> "$LOG"
if [ $? -ne 0 ] || ! echo "$RENDER_LOG" | grep -q "^wrote"; then
  fail_and_log "渲染失败: $(echo "$RENDER_LOG" | tail -1)"
  exit 1
fi

# 推送 Telegram: 标题+正文作为第一张图的 caption,sendMediaGroup 一次发全部图
TITLE=$(grep -m1 "^## 标题" -A2 "$NEW_FILE" | tail -1)
CAPTION="${TG_PREFIX} ${TITLE}"

IMAGES=("$CARD_OUT"/xhs-${POST_NUM}-*.png)
if [ ${#IMAGES[@]} -eq 0 ]; then
  fail_and_log "渲染声称成功但输出目录没有图片: $CARD_OUT"
  exit 1
fi

ESC_CAPTION=$(echo "$CAPTION" | sed 's/"/\\"/g')
MEDIA_JSON="["
CURL_ARGS=()
i=0
for img in "${IMAGES[@]}"; do
  if [ "$i" -eq 0 ]; then
    MEDIA_JSON="${MEDIA_JSON}{\"type\":\"photo\",\"media\":\"attach://p${i}\",\"caption\":\"${ESC_CAPTION}\"}"
  else
    MEDIA_JSON="${MEDIA_JSON},{\"type\":\"photo\",\"media\":\"attach://p${i}\"}"
  fi
  CURL_ARGS+=(-F "p${i}=@${img}")
  i=$((i+1))
done
MEDIA_JSON="${MEDIA_JSON}]"

TG_RESPONSE=$(curl -s -X POST "https://api.telegram.org/bot${TG_TOKEN}/sendMediaGroup" \
  -F "chat_id=${TG_CHAT}" -F "media=${MEDIA_JSON}" "${CURL_ARGS[@]}")
echo "telegram response: $TG_RESPONSE" >> "$LOG"

if ! echo "$TG_RESPONSE" | grep -q '"ok":true'; then
  fail_and_log "Telegram sendMediaGroup 失败: $TG_RESPONSE"
  exit 1
fi

echo "===== done $(date '+%F %T'), post ${POST_NUM} sent to Telegram =====" >> "$LOG"
