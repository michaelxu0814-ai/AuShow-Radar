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
