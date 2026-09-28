# 038 — 周杰伦悉尼站：全澳收官站（单场演出安利 · 四讲）

**选题类型**：单场演出安利（周一轮换位）
**信源条目**：`data/events.json` → 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会（verified=true，11-21 / ENGIE Stadium）

**选场说明（池子仍为空，属"换角度重讲"）**：8 条 verified 中，未被单场安利过的条目早已清空。
袁娅维两场（08-20/08-22）演出日已过；AKMU 两场（09-18/09-20）演出日已过且自 08-24 挂
`EXCEPTIONS.md` OPEN 至今字段未修；Loadingzone 由 010 安利过、自 09-14 挂 EXCEPTIONS OPEN
（Eventbrite 主办方页已无开放麦场次），今日 WebFetch 复核仍无任何 Upcoming 场次、无 Club
Voltaire 表述，维持不可发。故按提示词第 2 步取**已用条目里最久没被安利过的一条**：跳过
Loadingzone（首选 RED）后，取 **周杰伦悉尼站**（上次 029，2026-09-18，10 天前）。

**与既有篇目的差异化**：
- **002**（08-17）是"开票了"的播报式安利，平铺 JSON 字段。
- **018**（09-07）角度是「名字」——悉尼站为何叫「海洋」、一城一主题。
- **029**（09-18）角度是「布里斯班人最近的一站」（地理距离 + 跨城），"最后一场"只在其中一条
  ledger 顺带一提。
- **本篇（038）把"收官站"单独拎出来做成一整篇**：澳洲仅墨尔本（10-17）/ 悉尼（11-21）两站，
  悉尼 11-21 是最后一场——看完这场，这轮澳洲巡演就结束了。与 036（墨尔本"全澳首站"）正好
  一头一尾互为镜像，各自成篇、零重叠。

## 标题（14字）

悉尼收官站！杰伦澳洲最后一场

## 正文（发帖文案，无外链）

周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会，是这轮澳洲巡演的收官站——全澳只有墨尔本（10-17）和悉尼（11-21）两站，悉尼就是最后一场。

📍ENGIE Stadium（Sydney Olympic Park），11月21日（周六）晚7:30，Ticketmaster 官方开票中，官方页现标余票不多。

想在澳洲最后一场看到杰伦的姐妹评论区扣1，私信告诉你抢票窍门和后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出，不再错过任何一场。

#周杰伦 #悉尼演唱会 #澳洲华人 #收官站 #演唱会情报

## 卡片文案结构（4张，票根美学）

**P1 封面**
- kicker: 演出情报 · 单场安利
- 大字标题: 周杰伦 / 悉尼收官站！
- 副标题: 「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会
- 配图: 官方艺人页头图（Ticketmaster 提供），alt 写"澳洲巡演官方宣传图"（非"悉尼站海报"，规避张冠李戴红线）
- 说明: 全澳只有墨尔本（10-17）和悉尼（11-21）两站，悉尼是最后一场。
- 底部条: 11.21 · SYD — 全澳收官站 · 开票中

**P2 票根组件**
- 演出: 周杰伦「海洋 悉尼嘉年华Ⅱ」世界巡回演唱会
- 日期: 21 NOV 2026 ｜ 状态徽章: ON SALE 开票中
- 场馆: ENGIE Stadium（悉尼 Sydney Olympic Park）
- 时间: 19:30

**P3 收官站 ledger（4条）**
1. 全澳收官站 — 澳洲仅两站：墨尔本 10-17 先开，悉尼 11-21 最后一场
2. Ticketmaster — 唯一官方购票平台
3. $188–$748 — 票价区间（另加 $9.90 手续费）
4. 限购 6 张 — 每账户购买上限
- 收尾: 官方票价是唯一标准——加价转票、来源不明的二手票，风险自己扛。
- 底部条: 主办 Sky Music & Horizon Production — 发售前建议官网复核

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 全澳最后一场 / 你锁票了吗？
- 正文: 评论区扣 1，私信告诉你怎么锁票，还有后续开票提醒。
- 底部条: VOL. 038 — 简介里有完整演出日历

## 事实核查表

| 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|
| 演出名「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` events[].title_zh，该条目 verified=true | 逐字复制 |
| 城市 悉尼 | GREEN | 同上 events[].city | 逐字复制 |
| 日期 2026-11-21 | GREEN | 同上 events[].date | 逐字复制 |
| 11-21 是周六 | GREEN | Sydney Showground 官方活动页原文 "Saturday 21 November"（https://www.sydneyshowground.com.au/whats-on/jay-chou-carnival--world-tour/ ）+ Python weekday 复核 | 029 亦曾核实 |
| 时间 19:30 | GREEN | 同上 events[].time；官方活动页 "7:30pm event starts" | 逐字复制 |
| 场馆 ENGIE Stadium（Sydney Olympic Park） | GREEN | 同上 events[].venue；官方活动页 "ENGIE Stadium, Sydney Showground" | 逐字复制 |
| 票价 $188–$748（+$9.90手续费） | GREEN | 同上 events[].price | 逐字复制 |
| 购票平台 Ticketmaster | GREEN | 同上 events[].ticket_platform；官方活动页票务链接指向 Ticketmaster | 逐字复制 |
| 状态 on_sale（开票中） | GREEN | 同上 events[].status；官方活动页 "Tickets are officially on sale now" | 逐字复制 |
| 主办方 Sky Music & Horizon Production | GREEN | 同上 events[].notes | 逐字复制 |
| 每账户限购6张 | GREEN | 同上 events[].notes；sopa.nsw.gov.au 官方页 "A maximum of 6 tickets per customer applies"（WebSearch） | 逐字复制 |
| 澳洲仅墨尔本(10-17)/悉尼(11-21)两站 | GREEN | `data/events.json` 两站 date 字段；ausmusicscene "Carnival II Australian Tour 2026" 仅列墨/悉两场（https://www.ausmusicscene.com.au/news/jay-chou-carnival-ii-australian-tour-2026 ）；Ticketmaster AU 艺人页仅两澳洲场次（https://www.ticketmaster.com.au/artist/1260229 ） | 018/029/036 亦核实 |
| 悉尼是全澳收官站（11-21 晚于 10-17，且澳洲仅两站） | GREEN | `data/events.json` 两站 date 比较（11-21 > 10-17）+ 上述两站佐证 | 核心新角度 |
| 官方页现标余票不多（Low Availability） | GREEN | Ticketmaster AU 艺人页悉尼场现标 "Low Availability"（https://www.ticketmaster.com.au/artist/1260229 ） | 仅正文引用一次，不进卡片（瞬时标签，同 018/036 口径） |
| 封面图为澳洲巡演官方宣传图（非悉尼站专属海报） | GREEN | 同上 events[].image（Ticketmaster 官方站资源，与 002/018/029 同一 URL） | alt 写"澳洲巡演官方宣传图" |
| 购票链接可访问（link_ok=true） | GREEN | 同上 events[].link_ok | 未在正文/卡片放外链，仅用于内部核实 |

FACT-AUDIT-STATUS: RED=0 CHECKED=16 SOURCES-CITED=16

## 渲染状态

- 模板: `cards/038/index.html`（复制自 `cards/001/index.html`；已 diff 确认 001/003/006/009
  的第 1–845 行即全部 CSS / `data-theme="aushow"` 主题色 token / 字体逐字相同，仅 `<title>`
  与 4 个 poster 区块文案不同）
- 主题: Editorial Magazine × E-ink，`data-theme="aushow"`，色值对齐 aushow.com.au：
  --paper:#F6F1E6 --ink:#1C1712 --red:#D6402B --red-dk:#A82C1C --tan:#8C7B62 --line:#D8CDB8
  --card:#FFFDF7，Noto Serif SC 展示字体
- 输出: `cards/038/output/xhs-038-01.png` ~ `xhs-038-04.png`，均 1080×1440（由
  `automation/render_card.py` 确定性渲染，本任务不碰截图工具）
- 张数: 4 张（封面 / 票根 / 收官站 ledger / CTA），沿用 001 的四卡结构
- P2 票根场馆位沿用 029 悉尼票根口径：`ENGIE Stadium` + 第二行 `悉尼 Sydney Olympic Park`
- 本次会话按提示词第 0 节**未调用任何浏览器截图工具**，渲染交给 `run_daily_xhs.sh` →
  `automation/render_card.py`
