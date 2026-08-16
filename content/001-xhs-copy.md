# 001 — 周杰伦墨尔本站官宣（单场演出安利）

**选题类型**：单场演出安利
**信源条目**：`data/events.json` → 周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会（verified=true）

## 标题（12字）

周杰伦墨尔本站官宣！别错过

## 正文（发帖文案，无外链）

周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会官宣啦！📍Marvel Stadium，10月17日晚7:30，官方正式开票中。

想去的姐妹评论区扣1，私信告诉你抢票窍门和后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出，不再错过任何一场。

#周杰伦 #墨尔本演唱会 #澳洲华人 #演唱会情报

## 卡片文案结构（4张，票根美学）

**P1 封面**
- kicker: 演出情报 · 单场安利
- 大字标题: 周杰伦 / 要来墨尔本了！
- 副标题: 「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会
- 配图: 官方艺人页头图（Ticketmaster 提供）
- 说明: 10月17日 Marvel Stadium，官方正式开票中。
- 底部条: 10.17 · MELB — Ticketmaster 开票中

**P2 票根组件**
- 演出: 周杰伦「粉色 墨尔本嘉年华Ⅱ」世界巡回演唱会
- 日期: 17 OCT 2026 ｜ 状态徽章: ON SALE 开票中
- 场馆: Marvel Stadium（墨尔本 Melbourne）
- 时间: 19:30

**P3 购票须知（ledger 4条）**
1. $208–$748 — 票价区间（另加 $9.90 手续费）
2. Ticketmaster — 唯一官方购票平台
3. 限购 6 张 — 每账户购买上限
4. 官方主办 — Sky Music & Horizon Production
- 收尾: 官方票价是唯一标准——加价转票、来源不明的二手票，风险自己扛。
- 底部条: 信息来自主办方公告 — 发售前建议官网复核

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 还有多少场 / 你不知道？
- 正文: 评论区扣 1，私信告诉你怎么抢票，还有后续开票提醒。
- 底部条: VOL. 001 — 简介里有完整演出日历

## 事实核查表

| 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|
| 演出名「周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` events[].title_zh，该条目 verified=true | 逐字复制 |
| 日期 2026-10-17 / 时间 19:30 | GREEN | 同上 events[].date / events[].time | 逐字复制 |
| 场馆 Marvel Stadium（墨尔本） | GREEN | 同上 events[].venue / events[].city | 逐字复制 |
| 票价 $208–$748（+$9.90手续费） | GREEN | 同上 events[].price | 逐字复制 |
| 购票平台 Ticketmaster | GREEN | 同上 events[].ticket_platform | 逐字复制 |
| 状态 on_sale（开票中） | GREEN | 同上 events[].status | 逐字复制 |
| 每账户限购6张 / 主办 Sky Music & Horizon Production | GREEN | 同上 events[].notes | 逐字复制 |
| link_ok=true（购票链接可访问） | GREEN | 同上 events[].link_ok | 未在正文/卡片放外链，仅用于内部核实 |

FACT-AUDIT-STATUS: RED=0 CHECKED=7 SOURCES-CITED=7

## 渲染状态

- 模板: `cards/001/index.html`（Editorial Magazine × E-ink，自定义 `data-theme="aushow"` 主题，色值对齐 aushow.com.au 站点：--paper:#F6F1E6 --ink:#1C1712 --red:#D6402B --red-dk:#A82C1C --tan:#8C7B62 --line:#D8CDB8 --card:#FFFDF7，Noto Serif SC 展示字体）
- 输出: `cards/001/output/xhs-01-cover.png` ~ `xhs-04-cta.png`，均 1080×1440
- 修正记录：P2 票根卡底部曾有溢出+编造文案「Gate details TBC on ticket」（events.json 无此字段），已删除该行并重渲染，四张图逐一人工核对无溢出、无编造内容
- 渲染方式：headless Chrome CLI（`--headless --screenshot`）整页渲染后用 PIL 按 1440px 等分裁切——chrome-devtools-mcp 当次会话截图工具反复超时（Page.captureScreenshot timeout），改用此更可靠的路径，后续每日自动化沿用同一方式（见 automation/render_card.py）
