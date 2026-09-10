# 021 — 先看预算，这 4 场分两档（本周开票汇总）

**选题类型**：本周开票汇总（周四轮换位，2026-09-10 生成）

**信源条目**（全部 `data/events.json` → `verified=true`，共选 4 场）：
1. 周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会（2026-10-17）
2. 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会（2026-11-21）
3. Rolling Donkey 中文喜剧开放麦（悉尼，每周二）
4. 候场喜剧 Loadingzone Comedy 开放麦（墨尔本，常驻）

**本篇口径决定（先说清楚）**：

- **沿用 005/009/014 的"不说'本周开票'"口径。** 4 条 `status` 都是 `on_sale`（已在售），
  `events.json` 里没有任何字段支持"这些票是本周开售的"。栏目定位保留（仍记为
  "本周开票汇总"），标题/卡面一律用"在售""官方票面"这类可核实的表述。

- **角度与 005/009/014 刻意错开，且这是第 4 种切分。** `EXCEPTIONS.md` 2026-09-03 那条
  预警说得很直白：同一批底料已连出 3 篇（005 按时间线排、009 按"大场 vs 常驻"的提前量排、
  014 按城市排），"第四种切分很难再找到"。本篇找到的第四种是**按票价档位排**——
  `price` 是这批条目里**唯一一个从未被当作组织原则**的字段：前三篇都只把 "$208–$748"
  当作行末括注顺手列一下，没有一篇拿它当主线，更没有一篇拆开过它内部的结构。
  本篇把 4 场按"官方票价现在能不能查到"分成两档，落点是账号的核心差异化——
  **官方票面是你唯一的防骗标尺**。

- **本篇的新增事实（前三篇都没有过）：两站各 7 档票价，天花板相同、地板不同。**
  `events.json` 只存了区间端点（墨 `$208–$748`、悉 `$188–$748`）。今日外部核实拿到了
  两站完整的档位表，均为 7 档：墨尔本 `AUD$748 / AUD$648 / AUD$548 / AUD$448 / AUD$348 /
  AUD$248 / AUD$208`，悉尼 `AUD 748 / 648 / 548 / 448 / 348 / 248 / 188`。即两站
  **最高档同为 $748，最低档差 $20**。这是 005/009/014 从未写过的内容，也是本篇"分两档"
  这个结构成立的事实基础。详见事实核查表第 5、11 行。

- **不写任何座位区域名称。** 有二手来源把最低档描述为"山顶票"、最高档描述为"VIP区"，
  但该来源同时把墨尔本站起价写成 $248（与 `events.json` 及档位表的 $208 冲突），
  口径不可靠；`events.json` 也没有座位区域字段。只写价格数字，不写座位描述。
  详见事实核查表第 6 行。

- **不写"某一档还有没有票"。** 检索中见到"$348 以上有余票"这类说法，属于**瞬时余票状态**，
  沿用 018 对 Ticketmaster "Low Availability" 标签的既定处理（瞬时标签不做长期物料）：
  正文与卡片一律不写余票档位，只写"余票落在哪一档随时会变，以官方页面为准"。

**排除项摘要**：袁娅维墨尔本站（08-20）/ 悉尼站（08-22）演出日期均早于本篇生成日
2026-09-10，已开演，不进"接下来能买"的清单；AKMU 两场仍在 `EXCEPTIONS.md` OPEN 状态
（墨尔本站 `ticket_platform` 已确证失真应改 AXS，悉尼站 `venue` 为旧名且 `price`/`time`
仍为 null，截至今日 `data/events.json` 未修改），本篇一并不收——**票价正是本篇的主线字段，
而这两条的 `price` 恰好都是 null，收进来只会在主线上开一个洞。**

**红线自查**：4 条全部 `verified=true`；日期/场馆/票价/平台逐字取自 JSON 字段；`price`
为 null 的两条不编造票价；`time` 存疑的一条不写时间；正文无外链；未点名任何个人/账号。

**本篇额外做了外部复核**：因为整篇的主线是票价，而 `price` 字段此前**从未被独立核实过**
（009 的核查表第 5 行明确记过"Ticketmaster 汇总页不列价，指向各场次页"，即前三篇的票价
数字一直只有 `events.json` 单一来源），本篇专门为两站的票价各找到了一个列出完整档位表的
外部来源，逐条留 URL，见事实核查表。

**一条主动排除的"信源"**：外部检索时再次出现同一个 Threads 账号在兜售"周杰伦澳洲站
VIP 门票预定 / CAT 1 黄金位置"（014 也遇到过）。这正是本账号防诈内容里讲的官方渠道以外的
转票模式，**不作为信源引用，也不在文案里点名**（红线：只讲模式，不点名具体个人/账号）。
本篇"官方票面最高一档就是 $748"这句话，正是给读者用来判断这类报价的标尺。

## 标题（11字）

先看预算，这4场分两档

## 正文（发帖文案，无外链）

这份清单按日期排过、按城市排过，今天换个最实际的排法——**按钱包** 👇 手里这 4 场，2 场官方票价明码到每一档，2 场官方还没公布。先知道要花多少，再决定抢哪场。

**💰 第一档 · 明码标价的两场**

两场周杰伦，官方票面都是 **7 档**，天花板一样、地板不一样：

🌸 **周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会**
10 月 17 日（周六）晚 7:30 · 墨尔本 Marvel Stadium
官方票面 **$208 – $748**（7 档，另加 $9.90 手续费），Ticketmaster。**距今 37 天**，是这份清单里最先开唱的一场。

🌊 **周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会**
11 月 21 日（周六）晚 7:30 · 悉尼 ENGIE Stadium (Sydney Olympic Park)
官方票面 **$188 – $748**（7 档，另加 $9.90 手续费），Ticketmaster。距今 72 天。

⚠️ 同一个巡演，**悉尼的起步价比墨尔本低 $20**，最高档倒是一样的 $748。两站不是同一张价目表，别拿其中一站的价去推另一站。

**🎙️ 第二档 · 官方还没公布票价的两场**

🐴 **Rolling Donkey 中文喜剧开放麦（悉尼）**
每周二 晚 7:30 · Chippo Hotel，87-91 Abercrombie St, Chippendale
Eventbrite 报名，常驻周场——这周二没赶上，下周二还在。

🎭 **候场喜剧 Loadingzone Comedy 开放麦（墨尔本）**
Club Voltaire，1st Floor/14 Raglan St, North Melbourne
AUNZ Comedy Media 旗下的华语喜剧厂牌，墨尔本常驻，Eventbrite 报名。

这两场我们收录时官方都没公布票价，所以这里**不给数字**，也不写具体开场时间——以 Eventbrite 页面为准。

**📌 记住 $748，这是你的防骗标尺**

官方票面最高的一档就是 **$748**。任何私下报给你的"内场 VIP""黄金位置""前排锁位"，只要价格超过官方票面，多出来的那部分**不会变成更好的座位**——它只是加价。

两站都是 Ticketmaster 官方规则 **每人最多 6 张**，超量订单官方写明可能被直接取消，别为了凑人头拿一个号狂买。

余票落在哪一档随时会变，出手前以官方页面为准；购票只认上面写的官方平台，别从站外二维码或私信"内部渠道"走。

评论区扣 1，私信发你这份清单和官方票价档位，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #悉尼演唱会 #墨尔本演唱会 #周杰伦 #脱口秀 #开放麦 #演唱会情报 #留学生活

## 卡片文案结构（4张，票根美学）

> 张数说明：本篇是"两档对照"结构，P2 装"明码标价的两场"、P3 装"官方未公布的两场 +
> 防骗标尺"，两组的字段密度完全不同（一组有完整档位区间+手续费+限购规则，一组票价未公布
> 只有场馆地址），合成一张 ledger 会让单行注释超过 3 行不可读。封面与 CTA 是账号固定品牌
> 结构。张数与 005/009/014 一致，无空卡、无凑数卡。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 本周在售 · 演出清单
- 大字标题: 先看预算 / 这 4 场分两档
- 副标题: 2 场明码标价 · 2 场官方未公布
- 说明: 悉尼 & 墨尔本 4 场。先知道要花多少，再决定抢哪场。
- 底部条: 现在都能买 — 4 场 · 2 座城
- 配图: 无（汇总篇涉及多组演出方，挂任一张海报都有"张冠李戴"风险，整篇不挂图；沿用 004/005/008/009/014）

**P2 明码标价的两场（ledger 3条）**
1. 墨尔本 — 周杰伦「粉色 嘉年华Ⅱ」·10.17 周六 19:30 · Marvel Stadium · 官方票面 $208–$748（7 档，另加 $9.90 手续费）· Ticketmaster
2. 悉尼 — 周杰伦「海洋 嘉年华Ⅱ」·11.21 周六 19:30 · ENGIE Stadium (Sydney Olympic Park) · 官方票面 $188–$748（7 档，另加 $9.90 手续费）· Ticketmaster
3. 差 $20 — 同一个巡演，悉尼起步价比墨尔本低 $20，最高档同为 $748。两站不是同一张价目表
- 收尾: Ticketmaster 官方写明每人最多 6 张，超量订单可能被取消。
- 底部条: 两站均在售 — 余票档位以官方页面为准
- 版式说明: ledger-row 网格为 `96px 1fr auto`，note 占 460px 后 title 列只剩约 300px，
  故 title 一律压到 2–4 字，完整演出名/场馆/票价放进 note，避免 42px 标题折行

**P3 官方未公布票价的两场 + 防骗标尺（ledger 3条）**
1. 悉尼 — Rolling Donkey 中文喜剧开放麦 · 每周二 19:30 · Chippo Hotel，87-91 Abercrombie St, Chippendale · Eventbrite
2. 墨尔本 — 候场喜剧 Loadingzone Comedy · 墨尔本常驻 · Club Voltaire，1st Floor/14 Raglan St, North Melbourne · Eventbrite
3. 不给数字 — 这两场我们收录时官方均未公布票价，也不写开场时间；以 Eventbrite 页面为准
- 收尾: 官方票面最高一档就是 $748。超过官方票面的报价，多出来的钱不会变成更好的座位。
- 底部条: 官方票价是唯一标准 — 别从站外二维码走
- 版式说明: 同 P2

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 先看预算 / 再抢票
- 正文: 评论区扣 1，私信发你这份 4 场清单和官方票价档位，还有后续开票提醒。
- 底部条: VOL. 021 — 简介里有完整演出日历

## 事实核查表

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | 演出名「周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` 该条目 `title_zh`，`verified=true`，逐字复制 |
| 2 | 墨尔本站 2026-10-17，且为周六 | GREEN | 同条目 `date="2026-10-17"`；星期由日期计算得出（2026-10-17 = Saturday）；外部复核 https://www.marvelstadium.com.au/king-of-mandopop-jay-chou-announces-melbourne-show 原文 "17 October 2026 (Saturday)" |
| 3 | 墨尔本站开演 19:30（文案写"晚 7:30"） | GREEN | 同条目 `time="19:30"`；外部复核同上 Marvel Stadium 官网页原文 "7:30 PM" |
| 4 | 墨尔本站场馆 Marvel Stadium，城市墨尔本 | GREEN | 同条目 `venue` / `city`；外部复核 https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 原文 "October 17, 2026, – Marvel Stadium, Melbourne VIC" |
| 5 | 墨尔本站官方票面 $208–$748，共 7 档，另加 $9.90 手续费 | GREEN | 同条目 `price="$208–$748 (+$9.90手续费)"`（区间端点）；**档位数与完整档位表**外部复核 https://www.wesydney.com.au/03271740/ 原文 "AUD$748 / AUD$648 / AUD$548 / AUD$448 / AUD$348/ AUD$248/ AUD$208"（数得 7 档，最低 $208、最高 $748，与 JSON 区间端点一致）及同页 "$9.90 手续费" |
| 6 | **不写**最低/最高档的座位区域名称（"山顶票"/"VIP区"） | AMBER | https://ent.sina.cn/2026-04-03/detail-inhtfrev3660234.d.html 原文把墨尔本站写成 "248澳元（山顶票）至748澳元（VIP区）"，其 **$248 起价与 `events.json` 的 `$208` 及第 5 行的档位表冲突**（该表同时含 $248 与 $208 两档，即 sina 很可能漏记了最低档）。座位区域名称仅此一处来源且该来源在相邻数字上已被证伪，`events.json` 亦无座位字段。**处理=整条剔除，只写价格数字不写座位描述**。未升级 RED：本篇未依赖该说法做出任何断言 |
| 7 | 墨尔本站购票平台 Ticketmaster、当前在售 | GREEN | 同条目 `ticket_platform="Ticketmaster"` / `status="on_sale"`；外部复核 https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 墨尔本场标注 "On Sale Now!" |
| 8 | 演出名「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` 该条目 `title_zh`，`verified=true`，逐字复制 |
| 9 | 悉尼站 2026-11-21，且为周六 | GREEN | 同条目 `date="2026-11-21"`；星期由日期计算得出（2026-11-21 = Saturday）；外部复核 https://hk.trip.com/events/澳大利亞悉尼++海洋+悉尼+嘉年華Ⅱ+周杰倫世界巡迴演唱會-20260425/ 原文 "2026 年 11 月 21 日（星期六）" |
| 10 | 悉尼站开演 19:30（文案写"晚 7:30"），场馆 ENGIE Stadium (Sydney Olympic Park) | GREEN | 同条目 `time="19:30"` / `venue` / `city`；外部复核同上 Trip.com 页原文 "19 時 30 分"、"ENGIE 體育場"；另 https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 原文 "November 21, 2026, – ENGIE Stadium, Sydney NSW" |
| 11 | 悉尼站官方票面 $188–$748，共 7 档，另加 $9.90 手续费 | GREEN | 同条目 `price="$188–$748 (+$9.90手续费)"`（区间端点）；**档位数与完整档位表**外部复核 https://hk.trip.com/events/澳大利亞悉尼++海洋+悉尼+嘉年華Ⅱ+周杰倫世界巡迴演唱會-20260425/ 原文 "AUD 748 / 648 / 548 / 448 / 348 / 248 / 188"（数得 7 档，最低 $188、最高 $748，与 JSON 区间端点一致）。手续费数字取自 JSON 字段（与墨尔本站同为 $9.90，第 5 行有该站外部原文佐证） |
| 12 | 悉尼站购票平台 Ticketmaster、当前在售 | GREEN | 同条目 `ticket_platform` / `status="on_sale"`；外部复核 Ticketmaster 巡演页悉尼场 "General Public Sale: 12pm on Tuesday 28th April"（早于本篇生成日 2026-09-10，即已开售） |
| 13 | 两站最高档同为 $748，悉尼起步价比墨尔本低 $20 | GREEN | 由第 5 行与第 11 行两张档位表直接比对得出：两表最高档均为 748；最低档 208（墨）− 188（悉）= $20。纯算术，未引入新断言 |
| 14 | 两站每人限购 6 张，超量订单可能被取消 | GREEN | 两条目 `notes="主办方 Sky Music & Horizon Production;每账户限购6张"`；外部复核 https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 原文 "You may purchase a maximum of 6 tickets per person." 及 "any or all of their orders and tickets cancelled without notice by Ticketmaster at its discretion"；另 https://www.wesydney.com.au/03271740/ 原文 "每个 Ticketmaster 账户可购买（6）张门票" |
| 15 | 墨尔本站距本篇生成日 37 天、悉尼站 72 天；墨尔本站是清单里最先开唱的一场 | GREEN | 由两条目 `date` 与生成日 2026-09-10 计算得出（2026-10-17 − 2026-09-10 = 37 天；2026-11-21 − 2026-09-10 = 72 天）；"最先开唱"由本篇 4 条中仅有的两个 `date` 值比较得出（另两条 `date=null` 为常驻场） |
| 16 | 演出名「Rolling Donkey 中文喜剧开放麦(悉尼,每周二)」，每周二举行，开场 19:30 | GREEN | `data/events.json` 该条目 `title_zh` / `time="19:30"`，`verified=true`；外部复核 https://www.eventbrite.com/e/copy-of-rolling-donkey-tickets-1983189907399 页面标题 "Rolling Donkey 驴打滚每周二中文喜剧开放麦"，原文 "Weekly on Tuesdays at 7:30 PM" |
| 17 | Rolling Donkey 场馆 Chippo Hotel，87-91 Abercrombie St, Chippendale（悉尼） | GREEN | 同条目 `venue` / `city="悉尼"`；外部复核同上 Eventbrite 页原文 "Chippo Hotel, 87-91 Abercrombie Street, Chippendale, NSW 2008" |
| 18 | Rolling Donkey 报名平台 Eventbrite，页面在售 | GREEN | 同条目 `ticket_platform="Eventbrite"` / `status="on_sale"` / `ticket_url` 为 eventbrite.com 域名；外部复核同上页面今日仍为 live 的 recurring 场次页 |
| 19 | 演出名「候场喜剧 Loadingzone Comedy 开放麦(墨尔本,常驻)」，墨尔本常驻 | GREEN | `data/events.json` 该条目 `title_zh` / `city="墨尔本"`，`verified=true`，"常驻"取自 `title_zh` 括注 |
| 20 | Loadingzone 场馆 Club Voltaire，1st Floor/14 Raglan St, North Melbourne | GREEN | 同条目 `venue="Club Voltaire, 1st Floor/14 Raglan St, North Melbourne"`（逐字复制）；场馆地址此前已由 https://www.clubvoltaire.com.au/events/loading-zone-comedy-29 原文核实（009 核查表第 19 行） |
| 21 | Loadingzone 为 AUNZ Comedy Media 旗下**华语**喜剧厂牌（不写"双语"） | GREEN | 外部复核 https://www.eventbrite.com/o/loadingzone-comedy-75417874333 主办方简介今日原文 "候场喜剧是澳大利亚AUNZ COMEDY MEDIA旗下运营的一家以喜剧内容为核心的澳洲**华语**文化厂牌"。**不采用** `events.json` `notes` 里的"双语喜剧厂牌"——该字段已于 014 认定与官方口径不符并写入 EXCEPTIONS OPEN，截至今日仍未修正；本篇沿用 014 的表述 |
| 22 | Loadingzone 报名平台 Eventbrite | GREEN | 同条目 `ticket_platform="Eventbrite"` / `status="on_sale"` / `ticket_url` 为 eventbrite.com 主办方页；外部复核该主办方页今日仍 live。**本篇不复述场次数量**（009 曾写过"4 场待售"，今日抓取该页未显示场次计数，不沿用旧数字） |
| 23 | 两场开放麦均不给票价数字、不写开场时间 | GREEN | 两条目 `price=null`；外部复核两个 Eventbrite 页今日均未列出票价。Loadingzone 的 `time="19:00"` 与场馆侧公开信息 "7:30 pm" 冲突（009 核查表第 22 行已定性），沿用既定处理整条剔除不写 |
| 24 | "官方票面最高一档就是 $748；超过官方票面的报价，多出来的钱不会变成更好的座位" | GREEN | 前半句由第 5、11 两行的档位表得出（两站最高档均为 $748）；后半句是由此得出的直接推论——超出官方票面的部分不对应任何官方售出的更高座位档，属加价。表述只讲模式，未点名任何个人/账号/转售平台，符合账号档案红线 |
| 25 | "官方票价是唯一标准，加价转票/来源不明二手票风险自负；只认官方平台" | GREEN | 账号档案 `~/.claude/skills/xhs-content/accounts/aushow.md` 红线段 + 已发布的 `content/001-xhs-copy.md` P3、`005` P3、`009`、`014` 同款表述；口径与历史帖一致 |
| 26 | 本篇共 4 场，覆盖悉尼与墨尔本，当前均可购买/报名 | GREEN | 上述 4 条 `verified=true` 条目的 `city` ∈ {悉尼, 墨尔本}、`status` 均为 `on_sale`，计数由该 4 条汇总得出；封面"4 场 · 2 座城"由此得出 |

**主动排除项（无依据、依据冲突、瞬时状态或已过期，本篇一律不写）**：

- **袁娅维 TIA RAY 墨尔本站（2026-08-20）与悉尼站（2026-08-22）**——两条均 `verified=true`，
  但演出日期都早于本篇生成日 2026-09-10，已开演，整组剔除。
- **AKMU 乐童音乐家 墨尔本站（09-18）与悉尼站（09-20）**——仍在 `~/Projects/EXCEPTIONS.md`
  OPEN：墨尔本站 `ticket_platform="Ticketek"` 已确证失真（Melbourne Park 自 2026-08-22 起
  改由 AXS 承接），悉尼站 `venue="ICC Sydney Theatre"` 为旧名且 `price`/`time` 仍为 null。
  **本篇主线就是票价，这两条 `price` 恰好都是 null**，收进来会在主线上开洞，整组不收。
- **"$348 以上有余票"这类余票档位说法**——瞬时状态，沿用 018 对 "Low Availability" 的处理，
  不进正文也不进卡片；只写"余票落在哪一档随时会变，以官方页面为准"。
- **座位区域名称（"山顶票""VIP区"）**——见核查表第 6 行，唯一来源已在相邻数字上被证伪，剔除。
- **"门票绑定观演人证件，不支持转赠或转售"**——仅见于 https://ent.sina.cn/2026-04-03/detail-inhtfrev3660234.d.html
  一处二手来源，Ticketmaster 官方巡演页与两处档位表来源均无此说法。这是一条**很强的规则断言**
  （会直接影响读者能不能走官方转售），单一二手来源不足以支撑，整条剔除。
- **赞助商 CovaU / Petmima**——Ticketmaster 官方页确有其文（"sponsored by CovaU and Petmima"），
  但与读者购票动作无关，汇总篇信息密度已高，不写（省略不等于错误）。
- **Trip.com 作为购票渠道**——本篇仅把该页当作**悉尼站档位表的文字信源**引用；
  `events.json` 的 `ticket_platform` 是 Ticketmaster，文案里给读者的官方平台只写 Ticketmaster，
  不把该站呈现为购票入口。
- **周杰伦两场的主办方**——JSON `notes` 有 "Sky Music & Horizon Production"（Ticketmaster 官方页
  原文亦确认），但汇总篇只取限购条款，与 005/009/014 处理一致。
- **`verified=false` 的其余条目**——events.json 共 105 条、verified 仅 8 条，未核实条目一条不进
  本篇（账号红线）。
- **座位视野、开门检票时间、寄存、退改签政策、余票量**——events.json 无对应字段，不写。

FACT-AUDIT-STATUS: RED=0 CHECKED=26 SOURCES-CITED=26

## 渲染状态

- 模板: `cards/021/index.html`，复制自 `cards/014/index.html`。选 014 为基底的原因：
  ① 其 `<head>`+CSS 段（第 1–840 行）经 `diff` 比对与 `cards/001/index.html` **除 `<title>`
  外完全一致**；② 014 已是同模板中"无 `frame-img` 外链配图 + `.ledger-note` 内联
  `max-width:460px`"这一纯文字版式的验证后代，且与本篇同为 4 卡"两组对照"的汇总结构，
  结构匹配度最高。`<html data-theme="aushow">`、主题色 token、字体、
  `.ticket`/`.ledger`/`issue-strip` 组件样式全部原样保留，仅替换 4 个 poster 区块内的文案
  + `<title>`。
- 卡片数: 4 张 `<section class="poster xhs" id="xhs-01…04">`
- `render_card.py` 在计数前会剥掉 HTML 注释（`html_no_comments`），模板顶部示例注释里的
  `id="xhs-01"` 不会被算成 poster，脚本会正确识别为 4 张。
- 渲染: 交由 `automation/render_card.py`（headless Chrome 逐张截图 + PIL 校验 1080×1440）。
  本次会话按 `daily-xhs-prompt.md` 第 0 节要求，**未调用任何浏览器/截图工具**。
