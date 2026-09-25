# 036 — 周杰伦墨尔本站「全澳首站」（单场演出安利）

**选题类型**：单场演出安利
**信源条目**：`data/events.json` → 周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会（verified=true，10-17 / Marvel Stadium）

## 标题（13字）

周杰伦澳洲首站！只剩22天

## 正文（发帖文案，无外链）

周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会，全澳首站就在墨尔本！

📍Marvel Stadium，10月17日（周六）晚7:30，Ticketmaster 官方开票中。这轮澳洲只有两站——墨尔本 10-17 先开、悉尼 11-21 收官，官方页现标余票不多。

想在全澳第一批看到就锁这场，评论区扣1，私信告诉你抢票窍门和后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#周杰伦 #墨尔本演唱会 #澳洲华人 #演唱会情报

## 卡片文案结构（4张，票根美学）

**P1 封面**
- kicker: 演出情报 · 单场安利
- 大字标题: 周杰伦 / 全澳首站！
- 副标题: 「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会
- 配图: 官方艺人页头图（Ticketmaster 提供）
- 说明: 这轮澳洲只有两站——墨尔本 10-17 先开，悉尼 11-21 收官。
- 底部条: 10.17 · MELB — 全澳首站 · 开票中

**P2 票根组件**
- 演出: 周杰伦「粉色 墨尔本嘉年华Ⅱ」世界巡回演唱会
- 日期: 17 OCT 2026 ｜ 状态徽章: ON SALE 开票中
- 场馆: Marvel Stadium（墨尔本 Melbourne）
- 时间: 19:30

**P3 首站 ledger（4条）**
1. 全澳首站 — 墨尔本 10-17 先开，悉尼 11-21 收官
2. 只剩 22 天 — 今天 09-25 距开演三周出头
3. Ticketmaster — 唯一官方购票平台
4. $208–$748 — 票价区间（另加 $9.90 手续费）
- 收尾: 官方票价是唯一标准——加价转票、来源不明的二手票，风险自己扛。
- 底部条: 主办 Sky Music & Horizon Production — 每账户限购 6 张

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 首站只剩 22 天 / 你锁票了吗？
- 正文: 评论区扣 1，私信告诉你怎么锁票，还有后续开票提醒。
- 底部条: VOL. 036 — 简介里有完整演出日历

## 事实核查表

| 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|
| 演出名「周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` events[].title_zh，该条目 verified=true | 逐字复制 |
| 日期 2026-10-17 | GREEN | 同上 events[].date | 逐字复制 |
| 10-17 是周六 | GREEN | WebSearch：Marvel Stadium 官方活动页 "Saturday, 17 October 2026"（https://www.marvelstadium.mediaservices.com.au/events/916/jay-chou-carnival-world-tour） | 025 亦曾核实 |
| 时间 19:30 | GREEN | `data/events.json` events[].time；WebSearch 均标 7:30 PM | 逐字复制 |
| 场馆 Marvel Stadium（墨尔本 Melbourne） | GREEN | 同上 events[].venue / events[].city | 逐字复制 |
| 票价 $208–$748（+$9.90手续费） | GREEN | 同上 events[].price | 逐字复制 |
| 购票平台 Ticketmaster | GREEN | 同上 events[].ticket_platform；Ticketmaster AU 艺人页（https://www.ticketmaster.com.au/artist/1260229） | 逐字复制 |
| 状态 on_sale（开票中） | GREEN | 同上 events[].status | 逐字复制 |
| 主办方 Sky Music & Horizon Production | GREEN | 同上 events[].notes；WebSearch 确认 | 逐字复制 |
| 每账户限购6张 | GREEN | 同上 events[].notes；WebSearch "每人限购6张票" | 逐字复制 |
| 悉尼场 2026-11-21（收官站） | GREEN | `data/events.json` 悉尼条目 events[].date | 逐字复制 |
| 11-21 是周六 | GREEN | WebSearch 各源均标 "Saturday, 21 November 2026"（https://www.ausmusicscene.com.au/news/jay-chou-carnival-ii-australian-tour-2026） | 仅用于"悉尼收官"上下文，未单独入卡 |
| 澳洲仅墨尔本/悉尼两站，墨尔本为全澳首站（10-17 先于 11-21 开演） | GREEN | events.json 两站 date（10-17 < 11-21）+ WebSearch：ausmusicscene "Jay Chou – Carnival II Australian Tour 2026" 仅列墨/悉两场、Ticketmaster AU 艺人页仅两澳洲场次、搜索无其他澳洲城市场次 | 029 亦曾核实"澳洲仅墨/悉两城" |
| 只剩 22 天（今天 09-25 距 10-17） | GREEN | 算术：2026-09-25 → 2026-10-17 = 22 天（Python datetime 复核） | 卡内以"今天 09-25"锚定生成日 |
| 官方页现标余票不多（Low Availability） | GREEN | WebSearch：Ticketmaster AU 艺人页现标 Low Availability（https://www.ticketmaster.com.au/artist/1260229） | 仅在正文引用一次，不进卡片（瞬时标签，018 同口径） |

FACT-AUDIT-STATUS: RED=0 CHECKED=15 SOURCES-CITED=15

## 渲染状态

- 模板: `cards/036/index.html`（复制自 001，Editorial Magazine × E-ink，`data-theme="aushow"` 主题 token 不变：--paper:#F6F1E6 --ink:#1C1712 --red:#D6402B --tan:#8C7B62 --line:#D8CDB8 --card:#FFFDF7，Noto Serif SC 展示字体）
- 输出: `cards/036/output/xhs-036-01.png` ~ `xhs-036-04.png`，均 1080×1440（由 `automation/render_card.py` 确定性渲染，本任务不碰截图工具）
- 张数: 4 张（封面 / 票根 / 首站 ledger / CTA），沿用 001 的四卡结构
- 备注: 本条目为"换角度重讲"（非新条目）——未安利池已空，按提示词第2步取四条可安利条目里最久没被安利过的周杰伦墨尔本站（上次 025，09-14）。Loadingzone（08-28 更久）自 09-14 挂 EXCEPTIONS OPEN 仍未解（Eventbrite 无 2026 开放麦场次，WebSearch 今日复核无明确 2026 事件），沿用 025/029/032 "首选 RED → 换下一条" 处理。角度为「全澳首站」，与 001（官宣）/004（Marvel Stadium 场馆攻略）/015（倒计时+限购/价位）/018（名字来历）/025（上次 vs 这次）零重叠
