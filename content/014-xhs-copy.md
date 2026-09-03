# 014 — 你在哪座城？这 4 场对号入座（本周开票汇总）

**选题类型**：本周开票汇总（周四轮换位，2026-09-03 生成）

**信源条目**（全部 `data/events.json` → `verified=true`，共选 4 场）：
1. 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会（2026-11-21）
2. Rolling Donkey 中文喜剧开放麦（悉尼，每周二）
3. 周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会（2026-10-17）
4. 候场喜剧 Loadingzone Comedy 开放麦（墨尔本，常驻）

**本篇口径决定（先说清楚）**：

- **沿用 005/009 的"不说'本周开票'"口径。** 4 条 `status` 都是 `on_sale`（已在售），
  `events.json` 里没有任何字段支持"这些票是本周开售的"。栏目定位保留（仍记为
  "本周开票汇总"），标题/卡面一律用"在售""现在能买"这类可核实的表述。
- **角度与 005、009 刻意错开。** 005（08-20）是"8 到 11 月 5 场演唱会时间线"，按时间排；
  009（08-27）是"要提前锁的大场 vs 不用等的常驻"，按提前量排。本篇**按城市排**——
  可用池 4 条刚好是悉尼 2 条 + 墨尔本 2 条，每座城各"一大一小"。读者的动作是先看自己
  住哪，再看这座城今年剩下什么，而不是先看日期或先看场馆规模。这是 005/009 都没有过的
  切分方式，不是换皮重排同一张清单。
- **顺带回应老粉的实际处境。** 本账号是复用的"玩转布里斯班"（粉丝以布里斯班本地华人为主，
  见账号档案）。可用池里两场大的都不在布里斯班，本篇明写这一点并给出"要跨城就早点定"的
  动作提示——这是从 `city` 字段直接读出来的事实，不是新的演出断言。
- **Loadingzone 改写为"华语喜剧厂牌"，不再沿用 JSON 的"双语"。** JSON `notes` 写的是
  "双语喜剧厂牌"，但今日两处一手信源（Eventbrite 主办方页、Club Voltaire 场次页）口径
  都是"华语/Mandarin"而非"双语"——009 引用过的那句"专业双语喜剧厂牌"在 Eventbrite 页
  今日已改版。本篇只写两处信源共同支持的表述。详见事实核查表第 19 行。
- **Loadingzone 不写开场时间。** JSON `time=19:00`，但场馆侧公开信息写的是 7:30pm，
  两个数字冲突且无法判定哪个适用于当前场次。沿用 008/009 的既定做法（"没有官方原文就
  不写"）整条剔除，只写场馆与平台。详见事实核查表第 21 行。

**排除项摘要**：袁娅维墨尔本站（08-20）/ 悉尼站（08-22）演出日期均早于本篇生成日
2026-09-03，已开演，不进"接下来能买"的清单；AKMU 两场仍在 `EXCEPTIONS.md` OPEN 状态
（墨尔本站 `ticket_platform` 已失真，悉尼站场馆名为旧名且 `price`/`time` 仍为 null，
截至今日 `data/events.json` 未修改），本篇一并不收。

**红线自查**：4 条全部 `verified=true`；日期/场馆/票价/平台逐字取自 JSON 字段；`price`
为 null 的两条不编造票价；`time` 存疑的一条不写时间；正文无外链；未点名任何个人/账号。

**本篇额外做了外部复核**：AKMU 那次事故（`ticket_platform` 随场馆换票务商而失真）说明
verified 条目也会过期。本篇 4 条全部另做了一次外部核对，逐条留 URL，见事实核查表。
特别复核了**周杰伦两场是否仍由 Ticketmaster 承接**（AKMU 就是栽在这个字段上）——
Ticketmaster 官方巡演页今日仍列这两场，墨尔本场标 "On Sale Now!"，未发现换票务商迹象。

**一条主动排除的"信源"**：外部检索时出现一个 Threads 账号在兜售"周杰伦澳洲站 VIP 门票
预定 / CAT 1 黄金位置"。这正是本账号防诈内容里讲的官方渠道以外的转票模式，**不作为信源
引用，也不在文案里点名**（红线：只讲模式，不点名具体个人/账号）。

## 标题（12字）

你在哪座城？这4场对号入座

## 正文（发帖文案，无外链）

先看你住哪座城，再看要不要抢票 👇 手里这 4 场，悉尼 2 场、墨尔本 2 场，每座城都是"一场要提前锁的大的 + 一个不用等的常驻场"。日期、场馆、票价、官方平台，逐条核过。

**🌊 人在悉尼**

🎤 **周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会**
11 月 21 日（周六）晚 7:30 · ENGIE Stadium (Sydney Olympic Park)
$188–$748（另加 $9.90 手续费），Ticketmaster。距今还有 79 天。

🐴 **Rolling Donkey 中文喜剧开放麦**
每周二 晚 7:30 · Chippo Hotel，87-91 Abercrombie St, Chippendale
Eventbrite 报名，常驻周场——这周二没赶上，下周二还在。

**🌸 人在墨尔本**

🎤 **周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会**
10 月 17 日（周六）晚 7:30 · Marvel Stadium
$208–$748（另加 $9.90 手续费），Ticketmaster。**距今只剩 44 天**，是这份清单里最先开唱的一场。

🎭 **候场喜剧 Loadingzone Comedy 开放麦**
Club Voltaire，1st Floor/14 Raglan St, North Melbourne
AUNZ Comedy Media 旗下的华语喜剧厂牌，墨尔本常驻，Eventbrite 报名。

**📌 两条要先记住的**

两场周杰伦同属「嘉年华Ⅱ」世界巡回演唱会，Ticketmaster 官方规则**每人最多 6 张**，超量订单官方写明可能被直接取消——别为了凑人头拿一个号狂买。

两场开放麦我们收录时官方都没公布票价，所以这里不给数字，也不写具体开场时间——**以 Eventbrite 页面为准**。

**🛫 人在布里斯班（或其他城）的说一句**：这两场大的都不在你家门口，一场在墨尔本一场在悉尼。真要飞过去看，票和机酒是两笔账，越靠近日子越贵——想去就趁早把两边都定了，别只抢到票才发现周末飞不动。

最后还是那句：**官方票价是唯一标准**。加价转票、来源不明的二手票，风险自己扛；购票只认上面写的官方平台，别从站外二维码或私信"内部渠道"走。

评论区扣 1，私信发你这份清单，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #悉尼演唱会 #墨尔本演唱会 #周杰伦 #脱口秀 #开放麦 #演唱会情报 #留学生活

## 卡片文案结构（4张，票根美学）

> 张数说明：本篇是"两座城对照"结构，P2 装悉尼、P3 装墨尔本，两组各自是完整的一城清单，
> 合成一张 ledger 会有 6 行、单卡不可读。封面与 CTA 是账号固定品牌结构。无空卡、无凑数卡。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 本周在售 · 演出清单
- 大字标题: 你在哪座城 / 就看哪两场
- 副标题: 悉尼 2 场 · 墨尔本 2 场
- 说明: 每座城一场要提前锁的大的，一个不用等的常驻场。日期、场馆、票价、官方平台，一张图排明白。
- 底部条: 现在都能买 — 4 场 · 2 座城
- 配图: 无（涉及多组演出方，挂任一张海报都有"张冠李戴"风险，整篇不挂图；沿用 004/005/008/009）

**P2 人在悉尼（ledger 3条 + body）**
1. 大场 — 周杰伦「海洋 嘉年华Ⅱ」· 11.21 周六 19:30 · ENGIE Stadium (Sydney Olympic Park) · $188–$748（另加 $9.90 手续费）· Ticketmaster
2. 常驻 — Rolling Donkey 中文喜剧开放麦 · 每周二 19:30 · Chippo Hotel，87-91 Abercrombie St, Chippendale · Eventbrite
3. 还有 79 天 — 悉尼场是这份清单里最晚开唱的一场，但票已在售，不用等到临近才动手
- body: 两场周杰伦同属「嘉年华Ⅱ」世界巡回演唱会；Ticketmaster 官方写明每人最多 6 张，超量订单可能被取消。
- 底部条: 悉尼 — 一大一小，都在售
- 版式说明: ledger-row 网格为 `96px 1fr auto`，note 占 460px 后 title 列只剩约 300px，
  故 title 一律压到 2–5 字，完整演出名/场馆/票价放进 note，避免 42px 标题折行

**P3 人在墨尔本（ledger 3条 + body）**
1. 大场 — 周杰伦「粉色 嘉年华Ⅱ」· 10.17 周六 19:30 · Marvel Stadium · $208–$748（另加 $9.90 手续费）· Ticketmaster
2. 常驻 — 候场喜剧 Loadingzone Comedy · 墨尔本常驻 · Club Voltaire，1st Floor/14 Raglan St, North Melbourne · Eventbrite
3. 只剩 44 天 — 墨尔本场是这份清单里最先开唱的一场，四场里时间最紧的就是它
- body: 两场开放麦收录时官方均未公布票价，这里不给数字、也不写开场时间；以 Eventbrite 页面为准。官方票价是唯一标准——加价转票、来源不明的二手票，风险自己扛。
- 底部条: 墨尔本 — 最先开唱的一场在这

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 先认城 / 再抢票
- 正文: 两场大的都不在布里斯班——要跨城就把票和机酒一起定。评论区扣 1，私信发你这份 4 场清单，还有后续开票提醒。
- 底部条: VOL. 014 — 简介里有完整演出日历

## 事实核查表

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | 演出名「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` 该条目 `title_zh`，`verified=true`，逐字复制 |
| 2 | 悉尼站 2026-11-21，且为周六 | GREEN | 同条目 `date="2026-11-21"`；星期由日期计算得出（2026-11-21 = Saturday）；外部复核 https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 今日原文 "November 21, 2026 at ENGIE Stadium, Sydney NSW" |
| 3 | 悉尼站开演 19:30（文案写"晚 7:30"） | GREEN | 同条目 `time="19:30"`；外部复核 https://hk.trip.com/events/%E6%BE%B3%E5%A4%A7%E5%88%A9%E4%BA%9E%E6%82%89%E5%B0%BC++%E6%B5%B7%E6%B4%8B+%E6%82%89%E5%B0%BC+%E5%98%89%E5%B9%B4%E8%8F%AF%E2%85%A1+%E5%91%A8%E6%9D%B0%E5%80%AB%E4%B8%96%E7%95%8C%E5%B7%A1%E8%BF%B4%E6%BC%94%E5%94%B1%E6%9C%83-20260425/ 原文 "2026年11月21日（星期六）晚上7时30分" |
| 4 | 悉尼站场馆 ENGIE Stadium (Sydney Olympic Park)，城市悉尼 | GREEN | 同条目 `venue` / `city="悉尼"`；外部复核同上 Ticketmaster 巡演页 "ENGIE Stadium, Sydney NSW" 及 Trip.com 页 "悉尼奥林匹克公园的 ENGIE Stadium" |
| 5 | 悉尼站票价 $188–$748，另加 $9.90 手续费 | GREEN | 同条目 `price="$188–$748 (+$9.90手续费)"`，逐字复制；外部复核 https://hk.trip.com/events/%E6%BE%B3%E5%A4%A7%E5%88%A9%E4%BA%9E%E6%82%89%E5%B0%BC++%E6%B5%B7%E6%B4%8B+%E6%82%89%E5%B0%BC+%E5%98%89%E5%B9%B4%E8%8F%AF%E2%85%A1+%E5%91%A8%E6%9D%B0%E5%80%AB%E4%B8%96%E7%95%8C%E5%B7%A1%E8%BF%B4%E6%BC%94%E5%94%B1%E6%9C%83-20260425/ 列出票档 "AUD 748 / 648 / 548 / 448 / 348 / 248 / 188"，最低 188、最高 748 与 JSON 区间一致 |
| 6 | 悉尼站购票平台 Ticketmaster、当前在售 | GREEN | 同条目 `ticket_platform="Ticketmaster"` / `status="on_sale"`；外部复核 https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 今日仍由 Ticketmaster AU 承接该巡演，悉尼场公售 "12pm on Tuesday 28th April"（早于本篇生成日 2026-09-03，即已开售）。**本行为本篇重点复核项**：AKMU 事故正是 `ticket_platform` 随场馆换票务商失真，今日未发现该巡演换票务商迹象 |
| 7 | 演出名「Rolling Donkey 中文喜剧开放麦(悉尼,每周二)」，每周二举行 | GREEN | `data/events.json` 该条目 `title_zh` / `recurrence="每周二"`，`verified=true`；外部复核 https://www.eventbrite.com/e/copy-of-rolling-donkey-tickets-1983189907399 今日页面名 "Rolling Donkey 驴打滚每周二中文喜剧开放麦"，原文 "Every Tuesday, 7:30 PM" |
| 8 | Rolling Donkey 场馆 Chippo Hotel，87-91 Abercrombie St, Chippendale（悉尼） | GREEN | 同条目 `venue="Chippo Hotel, 87-91 Abercrombie St, Chippendale"` / `city="悉尼"`；外部复核同上 Eventbrite 页原文 "87-91 Abercrombie Street, Chippendale, NSW 2008" |
| 9 | Rolling Donkey 开场 19:30（文案写"晚 7:30"） | GREEN | 同条目 `time="19:30"`；外部复核同上 Eventbrite 页原文 "Every Tuesday, 7:30 PM" |
| 10 | Rolling Donkey 报名平台 Eventbrite，页面在售且有未来场次（"常驻周场"成立） | GREEN | 同条目 `ticket_platform="Eventbrite"` / `status="on_sale"` / `ticket_url` 为 eventbrite.com 域名；外部复核 https://www.eventbrite.com/e/copy-of-rolling-donkey-tickets-1983189907399 今日页面 live，标注 "Multiple dates" 的周二循环场次 |
| 11 | 演出名「周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` 该条目 `title_zh`，`verified=true`，逐字复制 |
| 12 | 墨尔本站 2026-10-17，且为周六 | GREEN | 同条目 `date="2026-10-17"`；星期由日期计算得出（2026-10-17 = Saturday）；外部复核 https://www.austadiums.com/concerts/event/678 原文 "Saturday 17th October 2026" |
| 13 | 墨尔本站开演 19:30（文案写"晚 7:30"） | GREEN | 同条目 `time="19:30"`；外部复核同上 Austadiums 页原文 "7:30 PM" |
| 14 | 墨尔本站场馆 Marvel Stadium，城市墨尔本 | GREEN | 同条目 `venue="Marvel Stadium"` / `city="墨尔本"`；外部复核 https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 今日原文 "October 17, 2026 at Marvel Stadium, Melbourne VIC" |
| 15 | 墨尔本站票价 $208–$748，另加 $9.90 手续费 | GREEN | 同条目 `price="$208–$748 (+$9.90手续费)"`，逐字复制；外部复核 https://m.163.com/dy/article/KOUQEVKV0534I43Y.html 原文票档 "AUD$748 / 648 / 548 / 448 / 348 / 248 / 208"，并明写"不含 $9.90 服务费"，与 JSON 区间及手续费一致 |
| 16 | 墨尔本站购票平台 Ticketmaster、当前在售 | GREEN | 同条目 `ticket_platform="Ticketmaster"` / `status="on_sale"`；外部复核 https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 今日墨尔本场标注 "On Sale Now!"。**本行同为重点复核项**（见第 6 行说明），今日未发现该场换票务商迹象 |
| 17 | 演出名「候场喜剧 Loadingzone Comedy 开放麦(墨尔本,常驻)」，墨尔本常驻 | GREEN | `data/events.json` 该条目 `title_zh` / `city="墨尔本"` / `recurrence="常驻(场次见Eventbrite)"`，`verified=true` |
| 18 | Loadingzone 场馆 Club Voltaire，1st Floor/14 Raglan St, North Melbourne | GREEN | 同条目 `venue="Club Voltaire, 1st Floor/14 Raglan St, North Melbourne"`；外部复核 https://www.clubvoltaire.com.au/events/loading-zone-comedy-29 （Club Voltaire 官网自有页面）原文地址 "Club Voltaire, 1st Floor/14 Raglan St, North Melbourne VIC 3051, Australia"，与 JSON 字段逐字一致 |
| 19 | Loadingzone 为 AUNZ Comedy Media 旗下**华语**喜剧厂牌（文案未写"双语"） | GREEN | 同条目 `notes="AUNZ Comedy Media旗下双语喜剧厂牌,也承接国内演员澳洲巡演"` 提供 "AUNZ Comedy Media 旗下" 这一半；**但"双语"一词今日两处一手信源均不支持**——https://www.eventbrite.com/o/loadingzone-comedy-75417874333 主办方简介今日原文为 "澳大利亚AUNZ COMEDY MEDIA旗下运营的一家以喜剧内容为核心的澳洲华语文化厂牌"，https://www.clubvoltaire.com.au/events/loading-zone-comedy-29 原文为 "the only Mandarin Speaking Comedy club in Melbourne"。两者口径都是"华语/中文"而非"双语"。**处理=文案改写为"华语喜剧厂牌"**，只保留两处信源共同支持的表述，不沿用 JSON `notes` 里的"双语"。（009 当时引的是 Eventbrite 页更早一版的"专业双语喜剧厂牌"文案，该页今日已改版；本篇以今日页面为准） |
| 20 | Loadingzone 报名平台 Eventbrite，当前有未来场次（"常驻"成立） | GREEN | 同条目 `ticket_platform="Eventbrite"` / `status="on_sale"` / `ticket_url` 为 eventbrite.com 主办方页；外部复核该主办方页今日标题仍为 "候场喜剧Loadingzone Comedy Events - 4 Upcoming Activities and Tickets"（https://www.eventbrite.com/o/loadingzone-comedy-75417874333 ），即有 4 场待售场次 |
| 21 | Loadingzone 的开场时间**不写** | AMBER | 条目 `time="19:00"`，但 https://www.clubvoltaire.com.au/events/loading-zone-comedy-29 该场次页写的是 "7:30 pm – 9:30 pm"，两数字冲突；且该页对应的是 **2025 年 5 月 20 日的过往场次**，更无法据以判定当前场次的开场时间。**处理=整条剔除不写**，文案改为"以 Eventbrite 页面为准"。未升级 RED：本篇没有依赖该字段做出任何断言（沿用 008/009 的同一处理） |
| 22 | 两场开放麦均不给票价数字 | GREEN | 两条目 `price=null`；外部复核 https://www.eventbrite.com/e/copy-of-rolling-donkey-tickets-1983189907399 今日页面未显示票价，与"官方未公布"一致 |
| 23 | 两站每人限购 6 张，超量订单可能被取消 | GREEN | 两条目 `notes="主办方 Sky Music & Horizon Production;每账户限购6张"`；外部复核 https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 今日原文 "You may purchase a maximum of 6 tickets per person"，及 https://m.163.com/dy/article/KOUQEVKV0534I43Y.html "每个 Ticketmaster 账户最多可购买 6 张门票"；"超量可能被取消"取自同一 Ticketmaster 页购票条款 |
| 24 | 距墨尔本站 44 天、距悉尼站 79 天；墨尔本场是本篇 4 场里最先开唱的一场 | GREEN | 纯算术，由两条目 `date` 字段与本篇生成日 2026-09-03 相减得出（`python3 datetime`：2026-10-17 − 2026-09-03 = 44 天；2026-11-21 − 2026-09-03 = 79 天）；"最先开唱"由 4 条中仅这两条有 `date` 字段、且 10-17 < 11-21 得出，另两条 `date=null` 为常驻场不参与排序 |
| 25 | 本篇共 4 场，悉尼 2 场 + 墨尔本 2 场，当前均可购买/报名 | GREEN | 上述 4 条 `verified=true` 条目的 `city` 分别为 悉尼×2、墨尔本×2，`status` 均为 `on_sale`，计数由该 4 条汇总得出；封面"悉尼 2 场 · 墨尔本 2 场""现在都能买"均由此得出 |
| 26 | "两场大的都不在布里斯班"，以及"官方票价是唯一标准，加价转票/来源不明二手票风险自负" | GREEN | 前半句由两条周杰伦条目 `city` ∈ {墨尔本, 悉尼}、无任何 verified 条目 `city="布里斯班"` 得出；后半句依据账号档案 `~/.claude/skills/xhs-content/accounts/aushow.md` 红线段 + 已发布的 `content/001-xhs-copy.md` P3、`content/005-xhs-copy.md` P3、`content/009-xhs-copy.md` P3 同款表述，口径与历史帖一致，只讲模式未点名任何个人/账号 |

**主动排除项（无依据、依据冲突或已过期，本篇一律不写）**：

- **袁娅维 TIA RAY 墨尔本站（2026-08-20）与悉尼站（2026-08-22）**——两条均 `verified=true`，
  但演出日期都早于本篇生成日 2026-09-03，已开演。列进"接下来能买"的清单属误导，整组剔除。
- **AKMU 乐童音乐家 墨尔本站（09-18）与悉尼站（09-20）**——两条仍在 `~/Projects/EXCEPTIONS.md`
  OPEN 状态且 `data/events.json` 截至今日未修改：墨尔本站 `ticket_platform="Ticketek"` 已失真
  （Melbourne Park 自 2026-08-22 起改由 AXS 承接票务），悉尼站 `venue="ICC Sydney Theatre"`
  为旧名（该剧院 2025-11 更名 TikTok Entertainment Centre）且 `price`/`time` 仍为 null。
  购票平台与场馆名是"开票汇总"这一栏目的核心字段，带着已知失真的字段发汇总篇风险高于价值，
  整组不收。**注意两场分别只剩 15 天和 17 天**，再不修就会像袁娅维两场一样直接过期作废。
- **Loadingzone 的开场时间**——见核查表第 21 行，字段冲突，剔除。
- **Rolling Donkey 与 Loadingzone 的票价、具体单场日期**——`price=null`、`date=null`，不给任何
  数字、不写"几月几号那场"。Rolling Donkey 只写 `recurrence` 字段已有的"每周二"。
- **"本周开票 / 本周开售"这一说法**——4 条中没有任何字段记录开售日期在本周，栏目名保留但
  措辞用"在售""现在能买"，详见文首口径决定。
- **跨城看演出的机票/酒店价格、航线、任何具体数字**——`events.json` 无对应字段，本篇只写
  "越靠近日子越贵、想去就趁早定"这类不含数字的通用建议，不给任何可被证伪的报价。
- **周杰伦两场的主办方**——JSON `notes` 有 "Sky Music & Horizon Production"，但汇总篇信息
  密度已高，本篇只取限购条款，与 005/009 处理一致（省略不等于错误）。
- **外部检索中出现的 Threads 转售帖（兜售"VIP CAT 1 黄金位置"）**——非官方渠道，不作为信源，
  也不在文案中点名（账号红线：防诈只讲模式，不点名具体个人/账号）。
- **`verified=false` 的另外 95 条演出**——events.json 共 103 条、verified 仅 8 条，未核实
  条目一条不进本篇（账号红线）。
- **座位视野、开门检票时间、寄存、退改签政策、余票量**——events.json 无对应字段，外部亦无
  可靠官方原文，不写。

FACT-AUDIT-STATUS: RED=0 CHECKED=26 SOURCES-CITED=26

## 渲染状态

- 模板: `cards/014/index.html`，复制自 `cards/009/index.html`（同为"本周开票汇总"栏目、
  同为 4 张 ledger 版式，是结构最贴近的一份已验证模板；其 `<head>`+CSS 段是 004→…→013
  一路沿用的同一份版式，且已是"无 `frame-img` 外链配图 + `.ledger-note` 内联
  `max-width:460px`"的纯文字版式后代，本篇同样不挂任何海报）。
  `<html data-theme="aushow">`、主题色 token、字体、`.ticket`/`.ledger`/`issue-strip`
  组件样式全部原样保留，仅替换 4 个 poster 区块内的文案 + `<title>`。
- 卡片数: 4 张 `<section class="poster xhs" id="xhs-01…04">`
- `render_card.py` 在计数前会剥掉 HTML 注释（`html_no_comments`），模板顶部示例注释里的
  `id="xhs-01"` 不会被算成 poster，脚本会正确识别为 4 张。
- 渲染: 交由 `automation/render_card.py`（headless Chrome 逐张截图 + PIL 校验 1080×1440）。
  本次会话按 `daily-xhs-prompt.md` 第 0 节要求，**未调用任何浏览器/截图工具**。
