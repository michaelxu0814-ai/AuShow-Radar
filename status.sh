#!/bin/zsh
# 项目进展一览: ./status.sh
cd "$(dirname "$0")"

echo "━━━ 澳华演出雷达 项目状态 $(date '+%F %T') ━━━"

echo "\n【线上站点】"
curl -s -o /dev/null -w "  https://michaelxu0814-ai.github.io/AuShow-Radar/ -> HTTP %{http_code}\n" \
  "https://michaelxu0814-ai.github.io/AuShow-Radar/"

echo "\n【数据库】"
python3 -c "
import json
db = json.load(open('data/events.json'))
ev = db['events']
v = sum(1 for e in ev if e.get('verified'))
print(f'  {len(ev)} 条演出 | 已核实 {v} | 待核实 {len(ev)-v} | 数据日期 {db[\"updated\"]}')"

echo "\n【自动任务】(每天09:00)"
launchctl print gui/$(id -u)/com.aushow.daily 2>/dev/null | grep -E "runs =|last exit" | sed 's/^/  /'
LATEST=$(ls -t logs/2*.log 2>/dev/null | head -1)
if [ -n "$LATEST" ]; then
  echo "  最近日志 $LATEST:"
  grep -E "=====|FAILED|pushed|sources fetched|new events" "$LATEST" | tail -6 | sed 's/^/    /'
else
  echo "  (还没有运行日志)"
fi

echo "\n【git】"
git log --oneline -3 | sed 's/^/  /'
AHEAD=$(git rev-list origin/main..main --count 2>/dev/null)
[ "$AHEAD" = "0" ] && echo "  ✓ 已全部推送" || echo "  ⚠ 有 $AHEAD 个提交未推送"

echo "\n【待人工核实】(每周花20分钟核对,改 verified:true)"
python3 -c "
import json
for e in json.load(open('data/events.json'))['events']:
    if not e.get('verified'):
        print(f'  - {e.get(\"title_zh\") or e.get(\"title_en\")} | {e.get(\"source_url\")}')"
