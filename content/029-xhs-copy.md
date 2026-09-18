# 029 — 周杰伦悉尼站：布里斯班人最近的一站（单场演出安利 · 三讲）

**选题类型**：单场演出安利
**信源条目**：`data/events.json` → 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会（verified=true）

## 标题（14字）

杰伦澳洲只两站，悉尼离你更近

## 正文（发帖文案，无外链）

周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会，这轮澳洲只来墨尔本（10-17）和悉尼（11-21）两站——布里斯班没有场。📍离你更近的是悉尼：11 月 21 日（周六）晚 7:30，ENGIE Stadium（Sydney Olympic Park），官方开票中。

想跨城看杰伦的姐妹评论区扣 1，私信告诉你跨城安排和后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出，不再错过任何一场。

#周杰伦 #悉尼演唱会 #澳洲华人 #布里斯班 #跨城看演出

## 卡片文案结构（4张，票根美学）

**P1 封面**
- kicker: 演出情报 · 单场安利
- 大字标题: 杰伦这轮 / 澳洲只两站
- 副标题: 「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会
- 配图: 官方艺人页头图（Ticketmaster 提供，澳洲巡演通用宣传图）
- 说明: 墨尔本 10-17、悉尼 11-21，布里斯班没有场。离你更近的那站，是悉尼。
- 底部条: 11.21 SAT · SYD — Ticketmaster 开票中

**P2 为什么是悉尼（ledger 4条）**
1. 澳洲仅两站 — 墨尔本 10-17、悉尼 11-21，布里斯班没有场
2. 悉尼更近 — 布里斯班飞悉尼约 750km / 1.5 小时；飞墨尔本约 1381km / 2 小时起
3. 最低档更省 — 悉尼 $188 起（$188–$748），比墨尔本 $208 起便宜 $20
4. 澳洲站最后一场 — 11-21 之后，这轮澳洲没有下一场
- 收尾: 官方票价是唯一标准——跨城加价转票、来源不明的二手票，风险自己扛。
- 底部条: 信息来自主办方公告 — 发售前建议官网复核

**P3 票根组件**
- 演出: 周杰伦「海洋 悉尼嘉年华Ⅱ」世界巡回演唱会
- 日期: 21 NOV 2026 (SAT) ｜ 状态徽章: ON SALE 开票中
- 场馆: ENGIE Stadium (Sydney Olympic Park)
- 城市: 悉尼 Sydney
- 时间: 19:30

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 跨城看杰伦 / 我们帮你盯
- 正文: 评论区扣 1，私信告诉你怎么安排跨城，还有后续开票提醒。
- 底部条: Vol. 029 — 简介里有完整演出日历

## 事实核查表

| 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|
| 演出名「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` events[].title_zh，该条目 verified=true | 逐字复制 |
| 澳洲仅两站：墨尔本 10-17、悉尼 11-21，布里斯班没有场次 | GREEN | WebSearch 维基百科「嘉年華II世界巡迴演唱會」词条 + ausmusicscene 澳洲巡演页，澳洲仅墨尔本/悉尼两城、无布里斯班日期；`data/events.json` 两条目 date 字段 | 核心新角度 |
| 悉尼场日期 2026-11-21，周六 | GREEN | `data/events.json` events[].date=2026-11-21 + Sydney Showground 官方活动页 "Saturday, 21 November 2026" | 逐字+独立复核 |
| 悉尼场时间 19:30 | GREEN | `data/events.json` events[].time=19:30 + Sydney Showground 官方活动页 "7:30 pm" | 一致 |
| 场馆 ENGIE Stadium (Sydney Olympic Park) | GREEN | `data/events.json` events[].venue + Sydney Showground/SOPA 官方活动页 "ENGIE Stadium, Sydney Olympic Park" | 逐字+独立复核 |
| 票价 $188–$748（+$9.90手续费） | GREEN | `data/events.json` events[].price | 逐字复制 |
| 悉尼最低档 $188 vs 墨尔本 $208（便宜 $20） | GREEN | `data/events.json` 悉尼条目 price=$188–$748、墨尔本条目 price=$208–$748 | 两字段比较 |
| 购票平台 Ticketmaster | GREEN | `data/events.json` events[].ticket_platform + Ticketmaster AU 艺人页 | 逐字+独立复核 |
| 状态 on_sale（官方开票中） | GREEN | `data/events.json` events[].status + Sydney Showground 官方 "Tickets are officially on sale" | 一致 |
| 悉尼更近：布里斯班飞悉尼约 750km/1.5 小时，飞墨尔本约 1381km/2 小时起 | GREEN | WebSearch distance.to（BNE-SYD 750.81km）+ flightera/AirNav Radar（BNE-MEL 1381km）+ Tripadvisor（BNE-SYD 约 1h32m）/flightq（BNE-MEL 约 2h21m） | 均为"约"，未写精确值 |
| 悉尼为澳洲站最后一场（11-21 晚于 10-17） | GREEN | `data/events.json` 两条目 date 比较 + WebSearch（澳洲为 2 场 Oceania shows，悉尼 11-21 在后） | 表述限定在"澳洲站"内，未称"整轮巡演收官" |

FACT-AUDIT-STATUS: RED=0 CHECKED=11 SOURCES-CITED=11

## 渲染状态

- 模板: `cards/029/index.html`（由 `cards/001/index.html` 复制，保留 `data-theme="aushow"` 主题 token、整体 CSS、`.ticket`/`.ledger`/`.issue-strip` 等组件样式，未改任何颜色）
- 输出: `cards/029/output/xhs-01-cover.png` ~ `xhs-04-cta.png`，均 1080×1440
- 卡片顺序相对 001 做了内容级调整：P2 与 P3 互换（P2=「为什么是悉尼」ledger、P3=票根），因本篇核心论点"为什么选悉尼"应紧跟封面钩子，两组件均为无 canvas 的全局样式块，互换不影响渲染
- 封面配图沿用 `events.json` 悉尼条目的 image（Ticketmaster 澳洲巡演通用艺人头图，与 018 悉尼站封面同一张，alt 写"澳洲巡演官方宣传图"不写"墨尔本站"，规避海报张冠李戴红线）
- 渲染方式：不调用任何截图工具，由 `run_daily_xhs.sh` → `automation/render_card.py` 完成
