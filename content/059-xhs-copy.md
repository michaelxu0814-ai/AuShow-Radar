# 059 — 清单只剩2场：一场倒计时，一场每周有（本周开票汇总）

**选题类型**：本周开票汇总（周四轮换位，2026-10-22 生成）

**信源条目**（全部 `data/events.json` → `verified=true`，共选 2 场）：
1. 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会（2026-11-21 周六，ENGIE Stadium (Sydney Olympic Park)，Ticketmaster）
2. Rolling Donkey 中文喜剧开放麦（悉尼，每周二，Chippo Hotel，Eventbrite）

**本篇口径决定（先说清楚）**：

- **沿用 005/009/014/021/028/035/041/048/053 的"不说'本周开票'"口径。** 2 条 `status` 都是
  `on_sale`（已在售），`events.json` 里没有任何字段支持"这些票是本周开售的"。栏目定位保留
  （仍记为"本周开票汇总"），标题/卡面一律用"在售""官方票面"这类可核实的表述。

- **角度与前九篇刻意错开，这是第 10 种切分：按 `date` / `recurrence` 这对字段分**——
  "有唯一日期、过了就结束" vs "没有日期字段、每周重复"。
  005=时间线、009=提前量（大场 vs 常驻）、014=城市、021=票价档位、028=倒计时、
  035=官方购票平台、041=档期月份、048=`time`+星期几、053=`venue`。
  **与 009 的区别要说清楚**：009 的落点是劝你"别干等大场，常驻的这周就能去"；本篇的落点是
  清单瘦到 2 条之后，这 2 条在**数据形态上刚好相反**——一条 `date=2026-11-21` 且
  `recurrence=null`（只有那一天），一条 `date=null` 且 `recurrence=每周二`（没有那一天，
  只有每一周）。所以它们各自**只能用一种方式管理**：前者只能倒计时，后者只能"这周有空就去"。

- **本篇的新事实有四条（都是今天才成立的）**：
  1. **清单第一次只剩 2 条。** 本栏目前九篇逐篇写明"共选 N 场"：5 / 4 / 4 / 4 / 3 / 3 / 3 / 3 / 3，
     本篇是 2——10 篇里最薄的一期。原因很直接：周杰伦墨尔本站（10-17 周六）已于 5 天前演完。
     053 当时写"这是它最后一次出现在这份清单里"，今天这句话兑现了。
  2. **整份清单两条都在悉尼，这是本栏目第一次只有一座城市。** 前九篇每一期都至少横跨悉尼和
     墨尔本（每期都含 Marvel Stadium 或墨尔本的 Loadingzone 条目）。
  3. **11-21 是 `verified` 池子里最后一个有日期的场次。** 枚举 `verified=true` 且 `date` 非空的
     6 条（08-20 / 08-22 / 09-18 / 09-20 / 10-17 / 11-21），最大值就是它。它一演完，清单上
     就只剩"每周二"那一条，不再有任何带具体日期的在售场次。
  4. **接下来的 30 天里，清单上没有第二场带日期的演出。** 这 30 天唯一能稳定去的，就是每周二。

- **今日外部复核**（两场逐条过了一手源，全部与 `events.json` 一致）：
  Sydney Showground 官方场次页原文 "Saturday 21 November" / "7:30pm – Event starts" /
  "ENGIE Stadium"，页面 "Tickets" 链接指向 Ticketmaster Australia；Sydney Olympic Park
  Aquatic Centre 官方页原文 "Saturday 21 November 2026" / "ENGIE Stadium, Sydney Showground"；
  Ticketmaster AU 官方巡演页原文 "Sydney: November 21, 2026" / "ENGIE Stadium, Sydney NSW" /
  "You may purchase a maximum of **6** tickets per person."，该页不列票价、指向场馆页
  （与 009/021/048/053 一致）；Eventbrite 售票页原文 "每周二 晚7:30"（"Every Tuesday, 7:30 PM"）/
  "87-91 Abercrombie St （Chippo Hotel）" / "87-91 Abercrombie Street, Chippendale, NSW 2008"，
  日期行显示 "Multiple dates"、全页无任何票价字样。

- **"在售"这一条今天的处理方式（与 053 有变化，记录在案）**：053 可以引用 Ticketmaster 巡演页
  原文 "On Sale Now!"，但该字样只印在**墨尔本站**那一栏——墨站已经演完，这句话今天不能挪用到
  悉尼站。今日没有任何官方页面印出指向悉尼站的"现在在售"字样。因此本篇"在售"的依据回到
  `status="on_sale"` 字段本身，辅以 Sydney Showground 官方页的 Tickets 入口直指 Ticketmaster
  Australia；文案只写"Ticketmaster 官方售票"，**不声称有新的开票动作**。

**排除项摘要**：

- **周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会（10-17 周六，Marvel Stadium）**——演出日
  早于生成日 5 天，已散场，退出"接下来能买"的清单。它的离场就是本篇的主线事实。
- **袁娅维 TIA RAY 墨尔本站（08-20）/ 悉尼站（08-22）**——`verified=true` 但演出日已过。
- **AKMU 乐童音乐家 墨尔本站（09-18）/ 悉尼站（09-20）**——演出日均已过，且仍挂
  `EXCEPTIONS.md` OPEN（墨站 `ticket_platform` 失真、悉站 `venue` 旧名 + `price`/`time` null）。
- **候场喜剧 Loadingzone Comedy（墨尔本，常驻）**——自 09-14 起无法在 Eventbrite 主办方页
  核实到当前场次（OPEN，已逾一个月未修），本轮整条不列、**不点名**。注意这一条对本篇主线
  尤其关键：它是 `date=null` + `recurrence` 形态的**另一条**，若它可用，本篇"每周重复"那一侧
  就不是独一份、"两条都在悉尼"也不成立。它不可用是本篇四条新事实成立的前提，已在核查表
  第 24/25 条写明。

**主动剔除的 7 项**：

1. **"本周开票"的字面说法**——沿 005 起的既定口径，`status` 字段只说明"在售"，无任何字段
   支持"本周开售"。
2. **悉尼站的 "On Sale Now!" 字样**——该字样只对已结束的墨尔本站成立，不挪用（见上）。
3. **二级市场价**——Eventworld "from $178"、Hellotickets "AU$353"、Stereoboard 的英镑价，
   均为转售聚合站自述 resale、非票面价，与"官方票价是唯一标准"口径直接冲突，不写。
4. **开门/检票/散场时间**——沿 027/045/048/053 处理；账号红线明确点名"检票时间/入场须知"
   属不可自行添加项，`events.json` 亦无此字段。
5. **场馆容量 / 顶棚是否露天**——053 已记录来源之间打架（ENGIE 23,500 vs 24,000；官网无
   roof 表述），本篇同样一字不写。
6. **Eventbrite 页面上的活动名「Rolling Donkey 驴打滚每周二中文喜剧开放麦」**——与 JSON
   `title_zh` 不同名，文案一律只用 `title_zh` 的「Rolling Donkey 中文喜剧开放麦」。
7. **Ticketmaster 巡演页的 "general public sale ... 12pm on Tuesday 28th April"**——无年份，
   且该页自身标注日期为 2026-03-26，属已过去的开票窗口，不写进任何倒计时。

**红线自查**：2 条全部 `verified=true`；日期/时间/场馆/城市/票价/平台/限购逐字取自 JSON 字段；
`price` 为 null 的 Rolling Donkey 不编造票价；开门/散场时间、场馆容量、顶棚状况一律不写；
正文无外链；未点名任何个人/账号/转售平台。

## 标题（18字）

清单只剩2场：一场倒计时，一场每周有

## 正文（发帖文案，无外链）

先说个有点冷清的事实：这份在售清单今天**只剩 2 场**了 👀

原因很简单——周杰伦墨尔本那场（10.17 周六）五天前已经散场。上一期我写"这是它最后一次出现在
这份清单里"，今天这句话兑现了。

剩下的 2 场，我发现它们在"怎么买"这件事上**刚好是相反的两种票** 👇

**【一场只有那一天 · 只能倒计时】**

🌊 **11.21 周六 晚7:30 · 悉尼 ENGIE Stadium（Sydney Olympic Park）**
周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会
$188–$748（另加 $9.90 手续费）· Ticketmaster 官方售票 · 每人最多 6 张
**还有 30 天。** 它没有第二场、没有下一周，错过就是错过。

**【一场没有"那一天" · 只有每一周】**

🎤 **每周二 晚7:30 · 悉尼 Chippo Hotel（87-91 Abercrombie St, Chippendale）**
Rolling Donkey 中文喜剧开放麦 · Eventbrite
官方不标价。最近一场就是下周二 **10.27**，这周二没空就下周二，下周二没空就再下周。

**所以这 2 场根本不该用同一套方法管**：前面那场你要做的是**锁日期**，把 11.21 当天先空出来；
后面那场你要做的是**别把它当大事**，哪个周二有空就走进去。

今天还有两件事挺巧的：

① **这 2 场都在悉尼。** 这是这份清单第一次只有一座城市——以前每一期都至少是悉尼 + 墨尔本。
② **11.21 是清单上最后一个有具体日期的场次。** 它一演完，剩下的就只有"每周二"了。换句话说，
接下来这 30 天，清单上没有第二场带日期的演出。

官方票面是唯一标准。周杰伦那场是 Ticketmaster 官方、每人最多 6 张，别的入口先问一句。

评论区扣 1，私信发你这 2 场的官方票价区间和日期，还有后续开票提醒 🎫

#周杰伦 #悉尼演唱会 #澳洲华人 #演出情报 #中文脱口秀 #悉尼生活

## 卡片文案结构（3张，票根美学）

**P1 封面**（无配图：汇总篇涉及多组演出方，不挂任何海报）
- issue-row: AuShow · 澳华演出雷达
- kicker: 在售清单 · 只剩 2 场
- 大字标题: 清单只剩 2 场 / 一场倒计时 / 一场每周有
- 分隔线
- 副标题: 只有那一天 ×1 · 只有每一周 ×1
- lead: 墨尔本那场五天前散场了。剩下的 2 场，在"怎么买"这件事上刚好相反。
- 底部条: 两条都在售 — 2 场 · 都在悉尼

**P2 在售清单（按"有没有唯一日期"，ledger 2条）**
- kicker: 同一份清单 · 两种相反的票
- 大字: 一场错过就没 / 一场每周都有
1. **只有那一天** — 11.21 周六 · 19:30 · 悉尼 ENGIE Stadium (Sydney Olympic Park) · 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会 · $188–$748（另加 $9.90 手续费）· Ticketmaster · 每人最多 6 张 · **还有 30 天**
2. **只有每一周** — 每周二 · 19:30 · 悉尼 Chippo Hotel，87-91 Abercrombie St, Chippendale · Rolling Donkey 中文喜剧开放麦 · Eventbrite · 官方未标价 · 下一场 下周二 10.27
- 收尾: 前者要你锁死 11.21 这一天，后者要你别把它当大事。两条都在悉尼——这是本清单第一次只有一座城市。11.21 也是清单上最后一个有具体日期的场次。
- 底部条: 官方票面是唯一标准 — 别的入口先问一句

**P3 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 11.21 之后 / 清单上就只剩 / 每周二
- 正文: 评论区扣 1，私信发你这 2 场的官方票价区间和日期，还有后续开票提醒。
- 底部条: VOL. 059 — 简介里有完整演出日历

## 事实核查表

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | 演出名「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` → `title_zh`（该条 `verified=true`），逐字复制 |
| 2 | 悉尼站日期 2026-11-21 | GREEN | 同条目 `date`；今日复核 Sydney Showground 官方场次页原文 "Saturday 21 November" https://www.sydneyshowground.com.au/whats-on/jay-chou-carnival--world-tour/ ；Ticketmaster AU 官方巡演页原文 "Sydney: November 21, 2026" https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 |
| 3 | 2026-11-21 是周六 | GREEN | 本地 `date` 推导（`python3 datetime`，11-21 weekday=5）；Sydney Olympic Park Aquatic Centre 官方页原文 "Saturday 21 November 2026" https://www.aquaticcentre.com.au/things-to-see-and-do/jay-chou-carnival-ii-world-tour |
| 4 | 悉尼站开演 19:30 | GREEN | 同条目 `time`；Sydney Showground 官方场次页原文 "7:30pm – Event starts"（同 #2 第一个 URL） |
| 5 | 悉尼站场馆 ENGIE Stadium (Sydney Olympic Park) | GREEN | 同条目 `venue`；Sydney Showground 官方页原文 "ENGIE Stadium"（同 #2 第一个 URL）；Ticketmaster 巡演页原文 "ENGIE Stadium, Sydney NSW"（同 #2 第二个 URL） |
| 6 | 悉尼站城市 = 悉尼 | GREEN | 同条目 `city`；Ticketmaster 巡演页原文 "ENGIE Stadium, Sydney NSW"（同 #2 第二个 URL） |
| 7 | 悉尼站票价 $188–$748（另加 $9.90 手续费） | GREEN | 同条目 `price`，逐字复制（档位结构已于 021 外部核实，本篇只用区间端点；官方巡演页今日仍不列价、指向场馆页，同 #2 第二个 URL） |
| 8 | 悉尼站官方购票平台 Ticketmaster | GREEN | 同条目 `ticket_platform`；Sydney Showground 官方场次页 "Tickets" 入口指向 Ticketmaster Australia（同 #2 第一个 URL） |
| 9 | 悉尼站状态 = 在售 | GREEN | 同条目 `status="on_sale"`；辅证同 #8（官方场馆页购票入口今日仍直指 Ticketmaster AU）。口径说明：今日无任何官方页印出指向悉尼站的"现在在售"字样，巡演页的 "On Sale Now!" 只对已结束的墨尔本站，故文案只写"官方售票"不声称新开票 |
| 10 | 悉尼站每账户限购 6 张 | GREEN | 同条目 `notes`；Ticketmaster AU 官方巡演页原文 "You may purchase a maximum of 6 tickets per person."（同 #2 第二个 URL） |
| 11 | 悉尼站距今还有 30 天 | GREEN | 本地 `date` 计算（2026-11-21 − 2026-10-22 = 30） |
| 12 | 演出名「Rolling Donkey 中文喜剧开放麦」 | GREEN | `data/events.json` → `title_zh`（`verified=true`），逐字复制 |
| 13 | Rolling Donkey 每周二 | GREEN | 同条目 `recurrence="每周二"`；今日复核 Eventbrite 售票页原文 "每周二 晚7:30"（"Every Tuesday, 7:30 PM"） https://www.eventbrite.com/e/copy-of-rolling-donkey-tickets-1983189907399 |
| 14 | Rolling Donkey 开演 19:30 | GREEN | 同条目 `time`；同 #13 Eventbrite 页原文 "晚7:30" / "7:30 PM" |
| 15 | Rolling Donkey 没有单一演出日期（`date` 为 null） | GREEN | 同条目 `date=null`；Eventbrite 售票页日期行今日显示 "Multiple dates"，不列任何具体单场日期（同 #13 URL） |
| 16 | Rolling Donkey 场馆 Chippo Hotel，87-91 Abercrombie St, Chippendale | GREEN | 同条目 `venue`，逐字复制；Eventbrite 页原文 "87-91 Abercrombie St （Chippo Hotel）" + "87-91 Abercrombie Street, Chippendale, NSW 2008"（同 #13 URL） |
| 17 | Rolling Donkey 城市 = 悉尼 | GREEN | 同条目 `city`；Eventbrite 页地址栏 "Chippendale, NSW 2008"（同 #13 URL） |
| 18 | Rolling Donkey 官方不标价 | GREEN | 同条目 `price=null`；Eventbrite 售票页今日全页无任何票价或"免费"字样（同 #13 URL） |
| 19 | Rolling Donkey 购票平台 Eventbrite | GREEN | 同条目 `ticket_platform`，逐字复制；#13 的 URL 本身即该条目 `ticket_url` 指向的 Eventbrite 售票页 |
| 20 | 下一场 Rolling Donkey 是下周二 2026-10-27 | GREEN | 本地 `date` 计算（2026-10-22 为周四，其后首个周二 = 2026-10-27） |
| 21 | 周杰伦墨尔本站（10-17）已散场、退出本清单 | GREEN | `events.json` 该条目 `date="2026-10-17"`，早于生成日 2026-10-22；本地 `date` 计算相差 5 天 |
| 22 | 本栏目第一次只剩 2 条 | GREEN | 枚举 `content/` 内本栏目前九篇各自写明的"共选 N 场"：005=5 / 009=4 / 014=4 / 021=4 / 028=3 / 035=3 / 041=3 / 048=3 / 053=3，本篇=2，为 10 篇最低 |
| 23 | 11-21 是 `verified` 池子里最后一个有日期的场次 | GREEN | 枚举 `events.json` 中 `verified=true` 且 `date` 非空的全部 6 条（2026-08-20 / 08-22 / 09-18 / 09-20 / 10-17 / 11-21），最大值为 2026-11-21 |
| 24 | 11-21 之后清单上只剩"每周二"那一条 | GREEN | 推导自 #23 + Rolling Donkey `date=null`/`recurrence="每周二"`；`events.json` 中另一条同形态条目（Loadingzone，墨尔本常驻）自 09-14 起挂 `EXCEPTIONS.md` OPEN、无法核实当前场次，不计入 |
| 25 | 整份清单两条都在悉尼，为本栏目首次单城 | GREEN | 两条目 `city` 字段均为"悉尼"；并枚举本栏目前九篇信源清单，每一篇都含墨尔本条目（005/009/014/021/028/035/041/048/053 均列有 Marvel Stadium 或墨尔本 Loadingzone / 袁娅维墨站） |
| 26 | 接下来 30 天内清单上没有第二场带日期的演出 | GREEN | 推导自 #23：`verified=true` 且 `date` 晚于今日的条目仅 11-21 一条 |
| 27 | 两条的官方购票平台不同（Ticketmaster / Eventbrite） | GREEN | 两条目 `ticket_platform` 字段（并分别经 #8 / #19 外部复核） |
| 28 | 一条明码标价、一条官方未标价 | GREEN | 两条目 `price` 字段：一条为区间字符串 "$188–$748 (+$9.90手续费)"、一条为 null（并经 #18 外部复核） |
| 29 | 两条 `status` 均为在售 | GREEN | 两条目 `status="on_sale"`；悉尼站辅证见 #9，Rolling Donkey 的 Eventbrite 售票页今日仍在线可访问（同 #13 URL） |

**剔除项未进文案**（不计入核查表，仅记录）：悉尼站 "On Sale Now!" 字样（只对已结束的墨站成立）、二级市场价（Eventworld "from $178" / Hellotickets "AU$353" / Stereoboard 英镑价，均为 resale 非票面）、开门/检票/散场时间（账号红线禁止自行添加入场须知，JSON 无字段）、场馆容量与顶棚状况（053 已记录来源打架）、Eventbrite 页上的活动名「驴打滚…」（与 `title_zh` 不同名）、Ticketmaster 巡演页旧开票窗口 "12pm on Tuesday 28th April"（无年份、页面自身日期为 2026-03-26）。

FACT-AUDIT-STATUS: RED=0 CHECKED=29 SOURCES-CITED=29

## 渲染状态

- 模板: `cards/059/index.html`（复制自 `cards/053/index.html`，保留 `data-theme="aushow"` 主题色 token 与 `.ticket`/`.ledger`/`issue-strip` 组件样式，仅替换 3 个 `<section class="poster xhs">` 区块内的文案）
- 张数: 3 张（封面 / 按"有没有唯一日期" 2 行 ledger / CTA）——本期只有 2 场，ledger 两行，不凑空卡
- 渲染: 交由 `automation/render_card.py`（headless Chrome 逐张单独截图），本次会话不调用任何截图工具
