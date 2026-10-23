# 060 — 周杰伦悉尼站：墨尔本演完，澳洲只剩这一场（单场演出安利 · 六讲）

**选题类型**：单场演出安利（周五轮换位，2026-10-23 生成）
**信源条目**：`data/events.json` → 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会（verified=true，11-21 / ENGIE Stadium）

**选场说明（池子仍为空，属"换角度重讲"）**：8 条 verified 中未被单场安利过的条目早已清空。
袁娅维两场（08-20 / 08-22）、AKMU 两场（09-18 / 09-20）演出日均已过（AKMU 两条自 08-24 起
仍挂 `EXCEPTIONS.md` OPEN）；**周杰伦墨尔本站（10-17）已于 6 天前开演，自本篇起退出可安利范围**；
Loadingzone 由 010 安利过、自 09-14 挂 OPEN，**今日 WebFetch 复核 Eventbrite 主办方页仍无任何
Upcoming 场次**，维持不可发。故按提示词第 2 步取**已用条目里最久没被安利过的一条**：跳过
Loadingzone（首选 RED，沿用 025/029/032/036/038/042/045/049/054 的处理）后，可用条目只剩两条——
周杰伦悉尼站上次为 049（2026-10-09，14 天前）、Rolling Donkey 为 054（10-16，7 天前）——
取 **周杰伦悉尼站**。它同时是 verified 池里**唯一一场日期还在今天之后**的演出。

**与既有五篇的差异化**（悉尼站此前：002 / 018 / 029 / 038 / 049）：
- **002**（08-17）播报式安利，平铺 JSON 字段。
- **018**（09-07）角度是「名字」——悉尼站为何叫「海洋」、一城一主题。
- **029**（09-18）角度是「地理距离」——布里斯班飞悉尼比飞墨尔本近。
- **038**（09-28）角度是「收官站」——悉尼是澳洲两站里排在后面的那场。
- **049**（10-09）角度是「两站之间的 35 天时间差」——落点在"你还有时间准备"。
- **本篇（060）角度是「对照组消失」**：前五篇无一例外都把悉尼站放在**和墨尔本站的对照里**
  写（先开的那场 / 后开的那场 / 哪站更近 / 中间隔多久），因为写的时候**两站都还没演**，
  读者手上始终有两个选项。10-17 已在 6 天前开演，**从今天起悉尼站第一次没有对照组**——
  "这次赶不上就去另一站"这句话不再成立。这是今天才成立的事实，前五篇都写不出来。
  038 的"收官站"是**排期上的先后**（当时两场都在未来、仍是二选一）；本篇是**选项数量
  由 2 变成 1**，读者位置也换成"错过墨尔本的人 / 一直在等下次的人"。

**与 059（10-22 本周开票汇总）的边界**：059 也用到"11-21 是最后一个有日期的场次"这条事实，
但 059 是**汇总栏目**、组织原则是 `date`/`recurrence` 两种数据形态的对照（有唯一日期 vs 每周重复），
清单里还有 Rolling Donkey 占一半篇幅；本篇是**单场安利栏目**，全篇只讲这一场，
落点是"没有备选场次"这个决策处境，不提 Rolling Donkey、不做清单。

**主动排除项**：
- **不写 gates 6:00pm / 最后入场 8:30pm / 散场 10:30pm**——Sydney Showground 官方页确有此四项
  时间，但 `events.json` 无对应字段，且属提示词点名的"入场须知 / 检票时间"类，按红线不写；
  该页自注 "Times are subject to change"。（沿用 027/045/048/049/053 的处理）
- **不引用 Ticketmaster 巡演页上的 "Melbourne: On Sale Now!"**——该页今日仍挂此字样，但墨尔本
  站已于 10-17 演完，这句话已失真，整条不用（本篇主线恰恰是"墨站已经演完"，引用它会自相矛盾）。
- **不写二级市场价**——EventWorld "from A$178" / HelloTickets "A$353" / Stereoboard 英镑价
  均为 resale 自述，与"官方票价是唯一标准"冲突。
- **不写"下一轮巡演还会不会来澳洲"**——无任何官方信息，属编造，一字不提；正文只说
  "这轮澳洲只排了两站"，不外推未来。
- **不写场馆无现金 / 儿童入场规则 / 交通**——入场须知与场馆攻略栏目的范畴（037 已写 ENGIE）。
- **精确倒计时只进正文且带日期锚**（"从 10-23 算还有 29 天"）；卡片一律用**不会随发布日
  漂移的绝对日期**，不放天数。

## 标题（15字）

杰伦墨尔本演完了，只剩悉尼一场

## 正文（发帖文案，无外链）

周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会——这轮澳洲只排了墨尔本、悉尼两站，Ticketmaster 官方巡演页上也只有这两场。

墨尔本那场（10-17）已经在 6 天前唱完了。也就是说从今天起，这轮巡演在澳洲就只剩 11 月 21 日（周六）悉尼这一场——以前还能说"这次赶不上就去另一站"，现在没有另一站了。

从今天（10-23）算还有 29 天，请假、机票、住宿、凑人，时间还够，但这回没有 Plan B。

📍ENGIE Stadium（Sydney Olympic Park），晚 7:30 开唱，Ticketmaster 官方售票。票价 $188–$748（另加 $9.90 手续费），每账户限购 6 张，主办方 Sky Music & Horizon Production。

想去的姐妹评论区扣1，私信告诉你行程怎么排，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出，不再错过任何一场。

#周杰伦 #悉尼演唱会 #澳洲华人 #跨城看演出 #演唱会情报

## 卡片文案结构（4张，票根美学）

**P1 封面**
- kicker: 演出情报 · 单场安利
- 大字标题: 墨尔本演完了 / 只剩悉尼这一场
- 副标题: 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会
- 配图: 官方艺人页头图（Ticketmaster 提供），alt 写"澳洲巡演官方宣传图"（非"悉尼站海报"，规避张冠李戴红线）
- 说明: 这轮澳洲只排了两站，10 月 17 日的墨尔本已经唱完——11 月 21 日的悉尼，是剩下的那一场。
- 底部条: 11.21 SAT · SYD — Ticketmaster 官方售票

**P2 两站现状 ledger（4条）**
1. 墨尔本 10.17 — Marvel Stadium，已经演完
2. 悉尼 11.21 — ENGIE Stadium（Sydney Olympic Park），周六 19:30 开唱
3. 官方只排两站 — 巡演页只列墨、悉两场，没有第三站
4. $188–$748 — Ticketmaster 官方售票，另加 $9.90 手续费，限购 6 张
- 收尾: 官方票价是唯一标准——加价转票、来源不明的二手票，风险自己扛。
- 底部条: 信息来自主办方公告 — 发售前建议官网复核
- 说明: 购票四要素（票价/平台/手续费/限购）压在本卡第 04 行，不另开"购票须知"卡、也不塞进
  P3 票根——票根卡沿用 001 已验证过的字段密度（演出/日期+徽章/场馆+时间），001 渲染记录里
  那张卡曾因多塞内容底部溢出，本篇不重复该风险。

**P3 票根组件**（字段密度与 001 已验证版本一致，未加行）
- 演出: 周杰伦「海洋 悉尼嘉年华Ⅱ」世界巡回演唱会
- 日期: 21 NOV 2026 (SAT) ｜ 状态徽章: ON SALE 开票中
- 场馆: ENGIE Stadium（悉尼 Sydney Olympic Park）
- 时间: 19:30

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 没有下一站 / 就这一场
- 正文: 评论区扣 1，私信告诉你行程怎么排，还有后续开票提醒。
- 底部条: VOL. 060 — 简介里有完整演出日历

## 事实核查表

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | 演出名「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` events[].title_zh（verified=true），逐字复制 |
| 2 | 城市 悉尼 | GREEN | 同条目 events[].city |
| 3 | 日期 2026-11-21 | GREEN | 同条目 events[].date；今日 WebFetch Ticketmaster AU 官方巡演页原文 "November 21, 2026"（https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 ） |
| 4 | 11-21 是周六 | GREEN | 今日 WebFetch Sydney Showground 官方活动页原文 "Saturday 21 November"（https://www.sydneyshowground.com.au/whats-on/jay-chou-carnival--world-tour/ ）+ Python `date(2026,11,21).strftime('%A')` = Saturday |
| 5 | 时间 19:30（晚 7:30 开唱） | GREEN | 同条目 events[].time；Sydney Showground 官方页今日原文 "the event starts at 7:30pm" |
| 6 | 场馆 ENGIE Stadium（Sydney Olympic Park） | GREEN | 同条目 events[].venue；Sydney Showground 官方页 "ENGIE Stadium, Sydney Showground"；Ticketmaster 巡演页 "ENGIE Stadium, Sydney NSW" |
| 7 | 票价 $188–$748（另加 $9.90 手续费） | GREEN | 同条目 events[].price，逐字复制。**今日两个官方页均不列票价**（Ticketmaster 巡演页原文 "For Sydney pricing refer to the venue event page"，而场馆页亦未列价目），故该数字仅以 verified 记录为准，正文/卡片均标为"票价"不写"官网现价" |
| 8 | 购票平台 Ticketmaster | GREEN | 同条目 events[].ticket_platform；Sydney Showground 官方页 Tickets 链接指向 ticketmaster.com.au |
| 9 | 状态 on_sale（在售） | GREEN | 同条目 events[].status；Ticketmaster 巡演页悉尼 "General Public Sale: 12pm on Tuesday 28th April"（该时点已过），场馆页今日仍挂售票链接 |
| 10 | 每账户限购 6 张 | GREEN | 同条目 events[].notes；Ticketmaster 巡演页今日原文 "You may purchase a maximum of 6 tickets per person." |
| 11 | 主办方 Sky Music & Horizon Production | GREEN | 同条目 events[].notes；Ticketmaster 巡演页今日原文 "proudly organised by Sky Music and Horizon Production" |
| 12 | 墨尔本站 2026-10-17 / Marvel Stadium | GREEN | `data/events.json` 墨尔本站条目 date / venue（verified=true）；Ticketmaster 巡演页今日原文 "October 17, 2026" / "Marvel Stadium, Melbourne VIC" |
| 13 | 这轮澳洲只排了墨尔本、悉尼两站 | GREEN | `data/events.json` 该巡演仅此两条；今日 WebFetch Ticketmaster AU 官方巡演页只列墨、悉两场，无第三站 |
| 14 | 墨尔本站已于 6 天前（10-17）演完 | GREEN | 墨站 events[].date = 2026-10-17 早于生成日 2026-10-23；Python 日期相减 = 6 天 |
| 15 | 悉尼场距今 29 天（2026-10-23 计） | GREEN | events[].date 与生成日相减 + Python 复核（29 天）；仅进正文且带日期锚，不进卡片 |
| 16 | 悉尼站是 verified 池里唯一一场日期晚于今日的演出 | GREEN | 枚举 `data/events.json` 中 verified=true 且 date 非空的全部 6 条（08-20 / 08-22 / 09-18 / 09-20 / 10-17 / 11-21），仅 11-21 晚于 2026-10-23 |
| 17 | Loadingzone 今日仍无可发场次（本篇不取它的依据） | GREEN | 今日 WebFetch Eventbrite 主办方页（https://www.eventbrite.com/o/loadingzone-comedy-75417874333 ）仍无任何 Upcoming 场次；维持 09-14 起的 `EXCEPTIONS.md` OPEN 判定 |
| 18 | 封面图为澳洲巡演官方宣传图（非悉尼站专属海报） | GREEN | 同条目 events[].image（Ticketmaster 官方站资源，与 002/018/029/038/049 同一 URL）；alt 写"澳洲巡演官方宣传图" |
| 19 | 购票链接可访问（link_ok=true） | GREEN | 同条目 events[].link_ok；未在正文/卡片放外链，仅用于内部核实 |

**剔除项未进文案**（不计入核查表，仅记录）：gates 6:00pm / 最后入场 8:30pm / 散场 10:30pm（入场须知类，JSON 无字段，且官方页自注 "Times are subject to change"）、Ticketmaster 巡演页 "Melbourne: On Sale Now!"（墨站已演完，该字样已失真）、二级市场价（EventWorld "from A$178" / HelloTickets "A$353" / Stereoboard 英镑价，均为 resale 非票面）、场馆无现金与儿童入场规则（入场须知类）、"下一轮巡演是否还来澳洲"（无任何官方信息）。

FACT-AUDIT-STATUS: RED=0 CHECKED=19 SOURCES-CITED=19

## 渲染状态

- 模板: `cards/060/index.html`（复制自 `cards/049/index.html`——同为单场安利 4 卡结构、同一封面图；已用 Python 逐字节比对确认其 `<style>` 区块与 `cards/001/index.html` **完全一致（均 26896 字节，identical: True）**，故"保留 001 的 aushow 主题色 token 与已验证组件样式"要求已满足。`data-theme="aushow"` 未改动，只替换四个 `<section class="poster xhs">` 区块内的文案）
- 卡片数: 4 张（xhs-01 封面 / xhs-02 两站现状 ledger / xhs-03 票根 / xhs-04 CTA）
- 渲染: 由 `automation/render_card.py` 在本会话结束后执行（headless Chrome 逐张单独截图）；按提示词第 0 步，本会话不调用任何截图工具
