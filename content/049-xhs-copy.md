# 049 — 周杰伦悉尼站：两站之间隔了 35 天（单场演出安利 · 五讲）

**选题类型**：单场演出安利（周五轮换位，2026-10-09 生成）
**信源条目**：`data/events.json` → 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会（verified=true，11-21 / ENGIE Stadium）

**选场说明（池子仍为空，属"换角度重讲"）**：8 条 verified 中未被单场安利过的条目早已清空。
袁娅维两场（08-20 / 08-22）、AKMU 两场（09-18 / 09-20）演出日均已过，AKMU 两条自 08-24 起
仍挂 `EXCEPTIONS.md` OPEN；Loadingzone 由 010 安利过、自 09-14 挂 OPEN，**今日 WebFetch 复核
Eventbrite 主办方页仍显示无任何 Upcoming 场次、无 Club Voltaire 表述**，维持不可发。故按提示词
第 2 步取**已用条目里最久没被安利过的一条**：跳过 Loadingzone（首选 RED）后，三条干净条目中
周杰伦悉尼站上次为 038（2026-09-28，11 天前）、Rolling Donkey 为 042（10-02，7 天前）、
周杰伦墨尔本站为 045（10-05，4 天前）——取 **周杰伦悉尼站**。

**与既有篇目的差异化**：
- **002**（08-17）播报式安利，平铺 JSON 字段。
- **018**（09-07）角度是「名字」——悉尼站为何叫「海洋」、一城一主题。
- **029**（09-18）角度是「地理距离」——布里斯班飞悉尼比飞墨尔本近。
- **038**（09-28）角度是「收官站」——悉尼是澳洲最后一场。
- **本篇（049）角度是「两站之间的 35 天时间差」**：墨尔本 10-17 已在眼前（今天起 8 天），
  悉尼 11-21 还有 43 天，两站整整隔了 5 周。落点是**准备期**而非抢票动作——现在才开始排
  请假 / 机票 / 住宿 / 凑人的人，赶不上墨尔本，但完全排得开悉尼。`date` 字段的"差值"在本号
  是第一次被当作组织原则（028/041 的倒计时是单场距今天数，不是两站之间的间隔）。

**主动排除项**：
- **不写"6:00pm 开门"**——Sydney Showground 官方页确有此说法，但 `events.json` 无该字段，
  且属提示词点名的"入场须知/检票时间"类，按红线不往卡片和正文放。
- **不写"余票不多 / Low Availability"**——该瞬时标签与本篇"你还有时间"的落点自相矛盾，
  且会过期，本篇一处不用（038 已用过该角度）。
- **不写"收官站 / 最后一场"做主叙事**——038 的范畴，本篇 ledger 仅以"两站里后开的那场"
  作中性事实表述。
- **不写场馆交通 / 入场规则**——008 场馆攻略的范畴。
- **精确倒计时只进正文且带日期锚**（"从 10-09 算还有 43 天"）；卡片一律用**不会过期的
  35 天间隔和绝对日期**，不放会随发布日漂移的天数。

## 标题（16字）

墨尔本赶不上？杰伦悉尼还有一个月

## 正文（发帖文案，无外链）

周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会——这轮澳洲只有墨尔本（10-17）和悉尼（11-21）两站，中间整整隔了 35 天，五周。

墨尔本那场马上就要开唱，现在才开始排请假、订机票、找住宿的基本赶不上了；但悉尼这场是 11 月 21 日（周六），从今天（10-09）算还有 43 天——请假、机票、住宿、凑够同行的人，都还排得开。

📍ENGIE Stadium（Sydney Olympic Park），晚 7:30 开唱，Ticketmaster 官方开票中。票价 $188–$748（另加 $9.90 手续费），每账户限购 6 张，主办方 Sky Music & Horizon Production。

想跨城看杰伦的姐妹评论区扣1，私信告诉你行程怎么排，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出，不再错过任何一场。

#周杰伦 #悉尼演唱会 #澳洲华人 #跨城看演出 #演唱会情报

## 卡片文案结构（4张，票根美学）

**P1 封面**
- kicker: 演出情报 · 单场安利
- 大字标题: 墨尔本赶不上？/ 悉尼还来得及
- 副标题: 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会
- 配图: 官方艺人页头图（Ticketmaster 提供），alt 写"澳洲巡演官方宣传图"（非"悉尼站海报"，规避张冠李戴红线）
- 说明: 澳洲两站隔了 35 天——11 月 21 日的悉尼场，是还够你从头安排的那一站。
- 底部条: 11.21 SAT · SYD — Ticketmaster 开票中

**P2 两站时间差 ledger（4条）**
1. 10.17 墨尔本 — Marvel Stadium，两站里先开的那场
2. 11.21 悉尼 — ENGIE Stadium（Sydney Olympic Park）
3. 相隔 35 天 — 整整五周——请假 / 机票 / 住宿，都还排得开
4. $188–$748 — Ticketmaster 官方售票，另加 $9.90 手续费，限购 6 张
- 收尾: 官方票价是唯一标准——加价转票、来源不明的二手票，风险自己扛。
- 底部条: 信息来自主办方公告 — 发售前建议官网复核
- 说明: 购票四要素（票价/平台/手续费/限购）放在本卡第 04 行，而非另开一张"购票须知"卡，
  也不塞进 P3 票根——票根卡沿用 001 已验证过的字段密度（演出/日期+徽章/场馆+时间），
  001 的渲染记录里那张卡曾因多塞内容出现底部溢出，本篇不重复该风险。

**P3 票根组件**（字段密度与 001 已验证版本一致，未加行）
- 演出: 周杰伦「海洋 悉尼嘉年华Ⅱ」世界巡回演唱会
- 日期: 21 NOV 2026 (SAT) ｜ 状态徽章: ON SALE 开票中
- 场馆: ENGIE Stadium（悉尼 Sydney Olympic Park）
- 时间: 19:30

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 这一场 / 别再说来不及
- 正文: 评论区扣 1，私信告诉你跨城行程怎么排，还有后续开票提醒。
- 底部条: VOL. 049 — 简介里有完整演出日历

## 事实核查表

| 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|
| 演出名「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` events[].title_zh，该条目 verified=true | 逐字复制 |
| 城市 悉尼 | GREEN | 同上 events[].city | 逐字复制 |
| 日期 2026-11-21 | GREEN | 同上 events[].date；Ticketmaster AU 巡演页 "November 21, 2026 / ENGIE Stadium, Sydney NSW"（https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 ） | 逐字复制 |
| 11-21 是周六 | GREEN | Sydney Showground 官方活动页原文 "Saturday 21 November"（https://www.sydneyshowground.com.au/whats-on/jay-chou-carnival--world-tour/ ）+ Python weekday 复核 | 029/038 亦曾核实 |
| 时间 19:30（晚 7:30 开唱） | GREEN | 同上 events[].time；Sydney Showground 官方页 "7:30pm" 开演 | 逐字复制 |
| 场馆 ENGIE Stadium（Sydney Olympic Park） | GREEN | 同上 events[].venue；Sydney Showground 官方页 "ENGIE Stadium, Sydney Showground" | 逐字复制 |
| 票价 $188–$748（+$9.90 手续费） | GREEN | 同上 events[].price | 逐字复制；Ticketmaster 巡演页将悉尼票价指向场馆分页，分页未列价目，故以 JSON 字段为准 |
| 购票平台 Ticketmaster | GREEN | 同上 events[].ticket_platform；Sydney Showground 官方页 Tickets 按钮指向 Ticketmaster Australia | 逐字复制 |
| 状态 on_sale（开票中） | GREEN | 同上 events[].status；Sydney Showground 官方页 "Tickets are officially on sale now!"；Ticketmaster 巡演页悉尼 General Public Sale "12pm on Tuesday 28th April" 已过 | 逐字复制 |
| 每账户限购 6 张 | GREEN | 同上 events[].notes；Ticketmaster 巡演页 "You may purchase a maximum of 6 tickets per person" | 逐字复制 |
| 主办方 Sky Music & Horizon Production | GREEN | 同上 events[].notes；Ticketmaster 巡演页 "proudly organised by Sky Music and Horizon Production" | 逐字复制 |
| 墨尔本站 2026-10-17 / Marvel Stadium | GREEN | `data/events.json` 墨尔本站条目 date / venue（verified=true）；Ticketmaster 巡演页 "October 17, 2026 / Marvel Stadium, Melbourne VIC" | 本篇对照项 |
| 澳洲仅墨尔本 / 悉尼两站 | GREEN | `data/events.json` 该巡演仅两条条目；Ticketmaster AU 官方巡演页仅列墨、悉两场 | 018/029/036/038 亦核实 |
| 两站相隔 35 天（10-17 → 11-21，五周） | GREEN | 两条 events[].date 字段相减 + Python `date` 复核（35 天 = 5.0 周） | **核心新角度**，首次以两站 date 差值为组织原则 |
| 悉尼场距今 43 天（2026-10-09 计） | GREEN | events[].date 与生成日相减 + Python 复核 | 仅进正文且带日期锚，不进卡片（会随发布日漂移） |
| 墨尔本场距今 8 天（2026-10-09 计） | GREEN | 同上，Python 复核 | 正文以"马上就要开唱"表述，不写具体天数入卡片 |
| Loadingzone 今日仍无可发场次（未取为本篇选题的依据） | GREEN | WebFetch Eventbrite 主办方页（https://www.eventbrite.com/o/loadingzone-comedy-75417874333 ）今日仍显示无 Upcoming 场次、无 Club Voltaire | 维持 09-14 起的 EXCEPTIONS OPEN 判定 |
| 封面图为澳洲巡演官方宣传图（非悉尼站专属海报） | GREEN | 同上 events[].image（Ticketmaster 官方站资源，与 002/018/029/038 同一 URL） | alt 写"澳洲巡演官方宣传图" |
| 购票链接可访问（link_ok=true） | GREEN | 同上 events[].link_ok | 未在正文/卡片放外链，仅用于内部核实 |

FACT-AUDIT-STATUS: RED=0 CHECKED=19 SOURCES-CITED=19

## 渲染状态

- 模板: `cards/049/index.html`（复制自 `cards/001/index.html`，保留 `data-theme="aushow"` 主题色 token 与 `.ticket`/`.ledger`/`issue-strip` 组件样式，仅替换四个 `<section class="poster xhs">` 内文案）
- 卡片数: 4 张（xhs-01 封面 / xhs-02 两站时间差 ledger / xhs-03 票根 / xhs-04 CTA）
- 渲染: 由 `automation/render_card.py` 在本会话结束后执行（headless Chrome 逐张单独截图，1080×1440）；按提示词第 0 步，本会话不调用任何截图工具
