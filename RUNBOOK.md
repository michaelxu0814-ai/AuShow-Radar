# AuShow Radar — 值班日志

小红书内容自动化(`run_daily_xhs.sh`)每次运行后在此追加一条记录：日期、编号、
选题类型、fact-audit 是否发现问题。

## 值班日志

- **2026-08-16** | 001号 | 单场演出安利(周杰伦墨尔本站) | fact-audit 7条全GREEN，
  RED=0。渲染阶段发现1处：票根卡(P2)底部曾有内容溢出+编造文案"Gate details TBC on
  ticket"(events.json无此字段)，人工发现并删除后重渲染，四张图逐一核对通过。
  已推送Telegram(sendMediaGroup确认`"ok":true`)，等用户手动发布。
  当天同时确定：chrome-devtools-mcp 截图工具反复超时/卡死，不适合无人值守自动化，
  改用 `automation/render_card.py`(headless Chrome CLI + PIL裁切)做确定性渲染，
  daily-xhs-prompt.md 已相应调整为"只写内容不管渲染"。

- **2026-08-17** | 002号 | 单场演出安利(周杰伦悉尼站) | fact-audit 9条全GREEN，RED=0，
  未发现事实错误。选题按周一轮换位=单场演出安利；001已用掉周杰伦墨尔本站，本篇取同巡演
  悉尼站(verified 池未用过、热度最高)。**未选日期最近的袁娅维墨尔本8/20/悉尼8/22**：按
  "001计划08-24起手动发布"的节奏，这两场在发布时已演完，写了等于浪费——已在
  `content/002-xhs-copy.md` 末尾留备注等用户裁决(若8/20前就发，可加急改产袁娅维)。
  本次会话按 daily-xhs-prompt.md 第0节未调用任何浏览器截图工具，渲染留给 render_card.py。
  另注：`content/cards/00N/index.html` 引用的 `assets/magazine-bg-webgl.js` 在 001/002
  下均不存在(404)，WebGL 墨流背景实际未挂载——001 出图已人工验收通过，故本次沿用未改。
