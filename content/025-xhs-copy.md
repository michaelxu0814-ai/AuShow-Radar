# 025 — 周杰伦回墨尔本了，这次换成球场（单场演出安利）

**选题类型**：单场演出安利（周一轮换位，2026-09-14 生成）
**信源条目**：`data/events.json` → 周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会（verified=true）

**选题决策**：未安利池仍为空——8 条 verified 中周杰伦墨/悉已由 001/002 用过（并分别于
015/018 换角度重讲），Rolling Donkey 由 006 用过（022 重讲），Loadingzone 由 010 用过，
袁娅维两场（08-20/08-22）演出日已过，AKMU 两场自 08-24 挂 EXCEPTIONS OPEN 至今
`data/events.json` 相关字段仍未改动（墨站 09-18 只剩 4 天、悉站 09-20 只剩 6 天），按红线不可发。
按提示词第 2 步应取**四条已用条目里最久没被安利过的一条**，即 **Loadingzone（010，08-28）**。
**但今日核实后判定它不能发**：Eventbrite 主办方页今日标题为 "2 Upcoming Activities"，两场
分别是 09-20 Library at The Dock（Docklands）的品牌合作活动与 09-26 9 Prospect St 的"抓马大会"，
**没有任何一场是开放麦、也没有任何一场在 Club Voltaire**；能找到的最近一场 Club Voltaire 开放麦
是 2026-03-21。即 JSON 的 `status="on_sale"` + `venue="Club Voltaire"` 对"开放麦"这件事今天
无法证实，写"常驻开放麦 · Eventbrite 售票中"会是一条无法验证的断言（RED）。沿用 006 的处理
（首选 RED → 换下一条），已写入 EXCEPTIONS OPEN 请用户复核该条目。
故本篇取**下一条最久没被安利过的**：周杰伦墨尔本站（015，09-04，10 天前）。这是该条目
**第二次换角度重讲**。

**角度**：「上次 vs 这次」。周杰伦上一次在墨尔本开唱是 **2024 年 3 月 16、17 日，Rod Laver Arena
连开两晚**（上一轮「嘉年华」巡演）；这次是 **2026 年 10 月 17 日，Marvel Stadium**（新一轮
「嘉年华Ⅱ」）。从演唱会最多约 1.42 万人的室内馆换到 5.3 万余座的球场——这个对比 001（官宣播报）、
004（Marvel Stadium 场馆攻略）、015（倒计时+限购/价位）、021（票价档位）四篇都没碰过，
018 只解释了「粉色/海洋」的名字来历。**与前作零重叠**：本篇不展开 Marvel Stadium 的交通/入场
（004 已写透），不重复 7 档票价结构（021 已写透），限购/票价/平台只在票根卡和正文各出现一次
作购票落点。

**红线自查**：演出信息（名称/日期/时间/场馆/票价/平台/状态/限购/主办方）逐字取自 events.json
的 `verified=true` 条目，并于今日对 Marvel Stadium 官方公告页与 Ticketmaster 巡演页逐条独立复核；
2024 年两场的日期/场馆取自维基百科「Carnival World Tour」词条并用 setlist.fm 交叉核对；
两座场馆容量数字均取自维基百科对应词条并在文案里标明"按维基百科的数字"；不点名任何个人/账号；
未放外链。

## 标题（15字）

周杰伦回墨尔本了，这次换成球场

## 正文（发帖文案，无外链）

周杰伦上一次在墨尔本开唱，是 2024 年 3 月 16、17 日，Rod Laver Arena 连开两晚——那是上一轮「嘉年华」巡演。

两年半之后他又来了：**周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会，10 月 17 日（周六）19:30，Marvel Stadium**，Ticketmaster 官方开票中。

这次和上次最大的不同，是场地换了一个量级 👇

🏟️ **从室内馆到球场。** Rod Laver Arena 办演唱会最多约 1.42 万人；Marvel Stadium 的座位数是 5.3 万余（都按维基百科的数字）。上次两晚加起来的人，这次一晚就装得下还有富余。

🎪 **从「嘉年华」到「嘉年华Ⅱ」。** 上一轮 2019 年从上海开跑、2025 年收官；这一轮 2026 年 4 月从杭州开始，主办方说的是出道 25 周年，一城一个主题——墨尔本这站叫「粉色」。

☔ **顶棚这件事不用担心。** 两座场馆都有可开合顶棚，10 月墨尔本的天气不影响看演出。

要买票的记三件事：官方票价 **$208–$748**（另加 $9.90 手续费）、**每账户限购 6 张**、**Ticketmaster 是唯一官方平台**。官方票价是唯一标准，"内部票""加价转让"一律别信。

距离 10 月 17 日还有 33 天（按 9 月 14 日算）。评论区扣 1，私信告诉你怎么抢票，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出，不再错过任何一场。

#周杰伦 #墨尔本演唱会 #澳洲华人 #演唱会情报 #MarvelStadium #嘉年华Ⅱ

## 卡片文案结构（4张，票根美学）

> 张数说明：4 张（封面 / 上次 vs 这次 ledger / 票根 / CTA）。与 015 相比把"购票须知"那张换成
> "上次 vs 这次"——限购/票价/平台三条 015 与 021 已各写过一次，本篇压进票根卡第三栏与 issue-strip，
> 不再单独占一张。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 演出情报 · 单场安利
- 大字标题: 周杰伦回墨尔本 / 这次换成球场
- 副标题: 「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会
- 配图: 官方艺人页头图（Ticketmaster 提供，与 001/015 同一张，`image` 字段）
- 说明: 10月17日（周六）19:30，Marvel Stadium，官方开票中。上次是 Rod Laver Arena，两年半前。
- 底部条: 10.17 · MELB — Ticketmaster 开票中

**P2 上次 vs 这次（ledger 3条）**
1. 上次 2024.03 — Rod Laver Arena，3 月 16、17 日连开两晚，「嘉年华」巡演
2. 这次 2026.10 — Marvel Stadium，10 月 17 日一晚，「嘉年华Ⅱ」墨尔本站叫「粉色」
3. 将近 4 倍 — 前者演唱会最多约 1.42 万人，后者座位 5.3 万余；两座都有可开合顶棚
- 收尾: 上次两晚加起来的人，这次一晚就装得下。
- 底部条: 2024 场次见维基百科「Carnival World Tour」 — 容量按维基百科数字

**P3 票根组件**
- 演出: 周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会
- 大字: 17 OCT 2026 ｜ 状态徽章: ON SALE 开票中
- 场馆: Marvel Stadium（墨尔本 Melbourne）
- 时间: 19:30
- 票价: $208–$748（+$9.90 手续费）
- 底部条: 限购 6 张 / 账户 — Ticketmaster 唯一官方平台

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 两年半了 / 这次别再错过
- 正文: 官方票价是唯一标准，"内部票"一律别信。评论区扣 1，私信告诉你怎么抢票，还有后续开票提醒。
- 底部条: VOL. 025 — 简介里有完整演出日历

## 事实核查表

| # | 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|---|
| 1 | 演出名「周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` events[].title_zh，该条目 verified=true | 逐字复制 |
| 2 | 日期 2026-10-17（周六）/ 时间 19:30 | GREEN | 同上 events[].date="2026-10-17" / events[].time="19:30"；今日 WebFetch Marvel Stadium 官方公告页 https://www.marvelstadium.com.au/king-of-mandopop-jay-chou-announces-melbourne-show 原文 "17 October 2026 (Saturday)" / "7:30 PM" | JSON 与官方页一致；"周六"取自官方页 |
| 3 | 场馆 Marvel Stadium（墨尔本） | GREEN | 同上 events[].venue="Marvel Stadium" / events[].city="墨尔本"；上述 Marvel Stadium 官方页 "Marvel Stadium (Melbourne)" | 逐字复制 |
| 4 | 票价 $208–$748（+$9.90 手续费） | GREEN | 同上 events[].price="$208–$748 (+$9.90手续费)"（021 已对档位表做过外部核实，两端点一致） | 逐字复制；本篇不重复 7 档结构 |
| 5 | 购票平台 Ticketmaster、状态 on_sale（开票中） | GREEN | 同上 events[].ticket_platform="Ticketmaster" / events[].status="on_sale"；今日 WebFetch https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 原文 "On Sale Now!" | JSON 与官方页一致 |
| 6 | 每账户限购 6 张 | GREEN | 同上 events[].notes="…每账户限购6张"；上述 Ticketmaster 页原文 "You may purchase a maximum of 6 tickets per person." | JSON 与官方页一致 |
| 7 | 主办 Sky Music & Horizon Production | GREEN | 同上 events[].notes="主办方 Sky Music & Horizon Production…"；上述 Ticketmaster 页原文 "Sky Music and Horizon Production" | 仅出现在文档内部与 issue-strip 备选，正文未写主办方 |
| 8 | 上一次墨尔本开唱：2024-03-16、03-17，Rod Laver Arena，连开两晚 | GREEN | WebFetch https://en.wikipedia.org/wiki/Carnival_World_Tour 表格行 "March 16, 2024 / Melbourne / Australia / Rod Laver Arena" 与 "March 17, 2024 / Melbourne / Australia / Rod Laver Arena"；交叉核对 https://www.setlist.fm/setlist/jay-chou/2024/rod-laver-arena-melbourne-australia-3aac5a3.html （2024-03-17 Rod Laver Arena 演出记录） | 两处一致；文案写"连开两晚"对应两行连续日期 |
| 9 | 上一轮巡演名「嘉年华」，2019 年从上海开跑、2025 年收官；本轮「嘉年华Ⅱ」2026 年 4 月从杭州开始 | GREEN | 同上 Carnival World Tour 词条原文 "began in Shanghai at the Mercedes-Benz Arena on October 17, 2019"、词条标注 "The Carnival World Tour (2019–25)"；WebFetch https://en.wikipedia.org/wiki/Carnival_II_World_Tour 原文 "The tour began in Hangzhou at the Hangzhou Olympic Sports Centre Stadium on April 3, 2026." | 文案只写到"年/月"粒度，不写具体日 |
| 10 | 一城一主题，墨尔本站叫「粉色」 | GREEN | 同上 Carnival II 词条 "Each city will have its own exclusive concert title and thematic design named after Chou's songs." 及表格行 "October 17, 2026 / Melbourne / Marvel Stadium / Pink (粉色)"；Marvel Stadium 官方页 "One City, One Theme" / "Pink Melbourne" | 与 JSON title_zh 中的「粉色」一致；名字来历 018 已写，本篇只提一句 |
| 11 | 主办方说的是出道 25 周年 | GREEN | Marvel Stadium 官方页原文 "25th anniversary" since his debut in 2000 | 文案口径为"主办方说的是"，转述官方公告 |
| 12 | Rod Laver Arena 办演唱会最多约 1.42 万人 | GREEN | WebFetch https://en.wikipedia.org/wiki/Rod_Laver_Arena 信息框 "up to 14,200 for concerts with floor seating" | 文案写"最多约"并标明"按维基百科的数字" |
| 13 | Marvel Stadium 座位数 5.3 万余 | GREEN | WebFetch https://en.wikipedia.org/wiki/Marvel_Stadium 信息框 "53,343 (seating capacity)" | 用座位数而非 56,347 的 venue capacity，取较保守值；标明"按维基百科的数字" |
| 14 | 两座场馆都有可开合顶棚 | GREEN | 同上 Marvel Stadium 词条信息框 roof "Retractable"；同上 Rod Laver Arena 词条 "the first arena of any kind in Australia to have a retractable roof installed" | 只写"有可开合顶棚"，不写当晚是否开合（无来源） |
| 15 | 距 10 月 17 日还有 33 天（按 9 月 14 日算） | GREEN | 由 events[].date="2026-10-17" 与生成日 2026-09-14 计算：9 月余 16 天 + 10 月 17 天 = 33 | 文案与卡片均标明起算日，避免发布日延后造成错误 |
| 16 | link_ok=true（购票链接可访问） | GREEN | 同上 events[].link_ok=true；今日 WebFetch 该 ticket_url 页面 live 且返回巡演正文 | 未在正文/卡片放外链，仅用于内部核实 |

FACT-AUDIT-STATUS: RED=0 CHECKED=16 SOURCES-CITED=16

## 主动排除项

- 不写"这次只开一场/不会加场"——维基百科与官方页目前只列 10-17 一场，但"不会加场"是预测，
  文案只写"这次一晚"（指已官宣的这场）
- 不写 2024 年两场的票价（搜索摘要提到 $158–$728，未逐字核到一手页面）与上座/售罄情况
- 不写 Marvel Stadium 演唱会模式容量（词条只给 venue/seating/cricket 三个数字，无 concert 数字），
  用座位数 53,343 并注明口径
- 不写"上次两晚共 X 人"这类相加数字（14,200 是上限不是实际入场数），只写"装得下还有富余"的
  定性比较
- 不展开 Marvel Stadium 交通/入场/包袋规则（004 已写透）、不列 7 档票价（021 已写透）
- 不写 "Low Availability" 等瞬时标签（沿用 018 处理）
- 不写"内场/看台哪边视野好"等无来源说法
- 不点名任何转票个人/账号（只讲"内部票/加价转让"这一模式）

## 渲染状态

- 模板: `cards/025/index.html`（复制自 `cards/001/index.html`；已 diff 确认 001/015 的第 1–840 行
  即全部 CSS / `data-theme="aushow"` 主题色 token / 字体逐字相同，仅 `<title>` 不同）
- 卡片: 4 张（封面 / 上次 vs 这次 ledger / 票根 / CTA），封面配图沿用 `image` 字段的官方艺人页头图
- 版式预防：ledger 标题控制在 6 字以内（"上次 2024.03""这次 2026.10""将近 4 倍"），note ≤ 40 字；
  P3 票根第三栏"票价 $208–$748"与"场馆/时间"同行 flex 排列（沿用 022 的三栏结构），
  "(+$9.90 手续费)" 放在 tk-field-lbl 小字行避免撑宽
- 渲染方式：本次会话按 `daily-xhs-prompt.md` 第 0 节**未调用任何浏览器截图工具**，
  渲染交给 `automation/render_card.py`（headless Chrome 逐张单独截图）由
  `run_daily_xhs.sh` 在本任务结束后执行
