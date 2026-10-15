# 053 — 3个场子，墨尔本那个只剩2天（本周开票汇总）

**选题类型**：本周开票汇总（周四轮换位，2026-10-15 生成）

**信源条目**（全部 `data/events.json` → `verified=true`，共选 3 场）：
1. 周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会（2026-10-17 周六，Marvel Stadium，Ticketmaster）
2. 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会（2026-11-21 周六，ENGIE Stadium，Ticketmaster）
3. Rolling Donkey 中文喜剧开放麦（悉尼，每周二，Chippo Hotel，Eventbrite）

**本篇口径决定（先说清楚）**：

- **沿用 005/009/014/021/028/035/041/048 的"不说'本周开票'"口径。** 3 条 `status` 都是
  `on_sale`（已在售），`events.json` 里没有任何字段支持"这些票是本周开售的"。栏目定位保留
  （仍记为"本周开票汇总"），标题/卡面一律用"在售""官方票面"这类可核实的表述。

- **角度与前八篇刻意错开，这是第 9 种切分：按 `venue`（场馆）分。**
  005=时间线、009=提前量（大场 vs 常驻）、014=城市、021=票价档位、028=倒计时、035=官方购票
  平台、041=档期月份、048=`time`+星期几——八篇都没有用过 **`venue`** 这个字段当组织原则。
  注意与 014（按城市）的区别：014 是**按城市分组**（悉尼 2 场 / 墨尔本 2 场），本篇是**按场馆
  性质分组**（两个大体育场 / 一个酒吧小场），落点完全不同。

- **本篇的新事实有三条**：
  1. **3 场落在 3 个完全不同的场馆，一个都没重复**（`venue` 三值互不相同）。
  2. **3 个场馆里有 2 个在悉尼**——ENGIE Stadium（Sydney Olympic Park）与 Chippo Hotel
     （Chippendale），同一座城市里体量两个极端；墨尔本只占 1 个场馆。这是 014 按城市分组时
     没有拆出来的层次（014 只数到"悉尼 2 场"，没说这 2 场的场子根本不是一类）。
  3. **场馆体量和"官方票价查不查得到"刚好对应**：两个体育场明码标价（$208–$748 / $188–$748，
     最高档同为 $748），酒吧那场 `price` 为 null、官方页至今不标价。

- **最硬的时效事实：墨尔本站只剩 2 天（10-17 周六），这是它最后一次能进这份清单。**
  下一次周四轮换是 10-22，已在演出日之后。10-17 之后清单上的体育场只剩 ENGIE 一个，
  两场周六之间隔 35 天。倒计时与星期几均由本地 `date` 计算（10-15 周四 / 10-17 周六 /
  10-20 周二 / 11-21 周六）。

- **今日外部复核**（三场逐条过了一手源，全部与 `events.json` 一致）：
  Ticketmaster AU 官方巡演页原文 Melbourne "October 17, 2026" / "Marvel Stadium, Melbourne VIC" /
  "On Sale Now!"、Sydney "November 21, 2026" / "ENGIE Stadium, Sydney NSW"、
  "You may purchase a maximum of **6** tickets per person."，且该页"no ticket prices or booking
  fees"、指向各场馆页（与 009/021/048 记录一致）；Eventbrite 售票页原文 "Every Tuesday, 7:30 PM"
  / "87-91 Abercrombie St (Chippo Hotel)" / Chippendale NSW 2008 / 未标价。

**排除项摘要**：

- **袁娅维 TIA RAY 墨尔本站（08-20）/ 悉尼站（08-22）**——`verified=true` 但演出日早于生成日，
  已开演，不进"接下来能买"的清单。
- **AKMU 乐童音乐家 墨尔本站（09-18）/ 悉尼站（09-20）**——演出日均已过，且仍挂
  `EXCEPTIONS.md` OPEN（墨站 `ticket_platform` 失真、悉站 `venue` 旧名 + `price`/`time` null）。
  悉站的 `venue` 待改这一点在本篇尤其致命——`venue` 正是本篇主线，收进来会在主线上开洞
  （同 021 对 `price=null`、048 对 `time=null` 的处理）。
- **候场喜剧 Loadingzone Comedy（墨尔本，常驻）**——"常驻开放麦 · on_sale"自 09-14 起无法在
  Eventbrite 主办方页核实到当前场次（OPEN，已满一个月未修），本轮整条不列、**不点名**。

**主动剔除的 4 项**：

1. **场馆顶棚/是否露天**——本篇主线是场馆，"有没有顶、会不会淋雨"本来是最有用的落点，
   但今日核不实：Marvel Stadium 官网首页**没有任何 roof 表述**，ENGIE Stadium 的露天状况在
   二手源之间口径不一（Austadiums 的场馆表无 arena roof、2012 年扩建加的是 open-air Skydeck，
   但找不到官方"整个碗体露天"的表述）。按账号红线"核实不了的具体细节宁可不写"整条不写。
2. **场馆容量数字**——ENGIE Stadium 的座位数在来源之间打架（Austadiums/维基 23,500、
   Populous 项目页 24,000），Marvel Stadium 官网首页不给容量。不写任何容量数字。
3. **开门/检票/散场时间**——沿 027/045/048 处理。今日搜索结果里 Musick 标 gates 6:00pm、
   维州交通页标 gates 5:00pm，两者冲突，且维州交通页把 10-17 写成 "Friday"（该日实为周六）
   已自证不可靠；账号红线亦明确点名"检票时间/入场须知"属不可自行添加项，JSON 无此字段。
4. **二级市场价**——Eventworld 列 "from $126"（自述 resale、非票面价），与"官方票价是唯一
   标准"口径直接冲突，不写。

**红线自查**：3 条全部 `verified=true`；场馆/日期/时间/票价/平台逐字取自 JSON 字段；`price`
为 null 的 Rolling Donkey 不编造票价；开门/散场时间、场馆容量、顶棚状况一律不写；正文无
外链；未点名任何个人/账号/转售平台。

## 标题（14字）

3个场子，墨尔本那个只剩2天

## 正文（发帖文案，无外链）

这周在售清单还是 3 场。今天换个切法——**按场馆排**。因为我核字段的时候发现，这 3 场落在
**3 个完全不同的场子，一个都没重复** 👇

**【大体育场 ×2】得专门腾出一整天**

🌸 **10.17 周六 晚7:30 · 墨尔本 Marvel Stadium**
周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会
$208–$748（另加 $9.90 手续费）· Ticketmaster 官方在售
**⚠️ 只剩 2 天**——这也是它最后一次出现在这份清单里。

🌊 **11.21 周六 晚7:30 · 悉尼 ENGIE Stadium（Sydney Olympic Park）**
周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会
$188–$748（另加 $9.90 手续费）· Ticketmaster 官方在售
还有 37 天，是清单上唯一还留着提前量的大场。

**【酒吧小场 ×1】下班直接走进去**

🎤 **每周二 晚7:30 · 悉尼 Chippo Hotel（87-91 Abercrombie St, Chippendale）**
Rolling Donkey 中文喜剧开放麦 · Eventbrite
官方不标价。最近一场就是下周二 **10.20**。

**场馆其实已经替你把票分好类了**：两个体育场明码标价、最高一档都是 $748，代价是你得提前锁；
酒吧那场官方连价都不用公布，因为它每周都在。

还有个挺巧的——**3 个场馆里有 2 个在悉尼**：一个是奥林匹克公园的大体育场，一个是 Chippendale
的街角酒吧，同城两个极端。墨尔本只占 1 个，而那 1 个这周六就散场了。它一走，清单上的体育场
只剩 ENGIE，两场周六之间隔整整 35 天。

官方票面是唯一标准。两场周杰伦都是 Ticketmaster 官方、每人最多 6 张，别的入口先问一句。

评论区扣 1，私信发你这份按场馆排好的清单 🎫

#周杰伦 #墨尔本演唱会 #悉尼演唱会 #澳洲华人 #演出情报 #中文脱口秀

## 卡片文案结构（3张，票根美学）

**P1 封面**（无配图：汇总篇涉及多组演出方，不挂任何海报）
- issue-row: AuShow · 澳华演出雷达
- kicker: 在售清单 · 按场馆排
- 大字标题: 3 个场子 / 墨尔本那个只剩 2 天
- 分隔线
- 副标题: 大体育场 ×2 · 酒吧小场 ×1
- lead: 3 场在售演出落在 3 个完全不同的场馆，一个都没重复。场馆决定了这张票的性质。
- 底部条: 现在都在售 — 3 场 · 悉尼 & 墨尔本

**P2 在售清单（按场馆，ledger 3条）**
- kicker: 同一份清单 · 三种场子
- 大字: 两个体育场 / 一个酒吧
1. **体育场** — 10.17 周六 · 19:30 · 墨尔本 Marvel Stadium · 周杰伦「粉色 墨尔本 嘉年华Ⅱ」· $208–$748（另加 $9.90 手续费）· Ticketmaster · **只剩 2 天**
2. **体育场** — 11.21 周六 · 19:30 · 悉尼 ENGIE Stadium (Sydney Olympic Park) · 周杰伦「海洋 悉尼 嘉年华Ⅱ」· $188–$748（另加 $9.90 手续费）· Ticketmaster · 还有 37 天
3. **酒吧小场** — 每周二 · 19:30 · 悉尼 Chippo Hotel，87-91 Abercrombie St, Chippendale · Rolling Donkey 中文喜剧开放麦 · Eventbrite · 官方未标价 · 下周二 10.20
- 收尾: 3 个场馆里 2 个在悉尼——大体育场和街角酒吧，同城两个极端。两场周杰伦都是 Ticketmaster 官方、每人最多 6 张，票面最高一档同为 $748。
- 底部条: 官方票面是唯一标准 — 别的入口先问一句

**P3 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 这周六一过 / 清单就少一个场子
- 正文: 评论区扣 1，私信发你这份按场馆排好的清单和官方票价区间，还有后续开票提醒。
- 底部条: VOL. 053 — 简介里有完整演出日历

## 事实核查表

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | 演出名「周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` → `title_zh`（该条 `verified=true`），逐字复制 |
| 2 | 墨尔本站日期 2026-10-17 | GREEN | 同上 `date`；今日复核 Ticketmaster AU 官方巡演页原文 "Melbourne: October 17, 2026" https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 |
| 3 | 2026-10-17 是周六 | GREEN | 本地 `date` 推导（`python3 datetime`，10-17 weekday=5）；外部检索口径亦为 "Saturday 17 October 2026" https://www.austadiums.com/concerts/event/678 |
| 4 | 墨尔本站开演 19:30 | GREEN | 同条目 `time`；048 已用 Marvel Stadium 官方公告页 "Time: 7:30 PM" 坐实，本篇未再引用开门时间 |
| 5 | 墨尔本站场馆 Marvel Stadium | GREEN | 同条目 `venue`；Ticketmaster 官方巡演页原文 "Marvel Stadium, Melbourne VIC"（同 #2 URL） |
| 6 | 墨尔本站票价 $208–$748（另加 $9.90 手续费） | GREEN | 同条目 `price`，逐字复制（档位结构已于 021 外部核实，本篇只用区间端点） |
| 7 | 墨尔本站状态 = 在售 | GREEN | 同条目 `status="on_sale"`；Ticketmaster 官方巡演页原文 "Melbourne: On Sale Now!"（同 #2 URL） |
| 8 | 墨尔本站距今只剩 2 天 | GREEN | 本地 `date` 计算（2026-10-17 − 2026-10-15 = 2） |
| 9 | 墨尔本站是最后一次进本栏目 | GREEN | 本地 `date` 推导：本栏目为周四轮换，下一次周四为 2026-10-22，晚于演出日 10-17 |
| 10 | 演出名「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` → `title_zh`（`verified=true`），逐字复制 |
| 11 | 悉尼站日期 2026-11-21 | GREEN | 同条目 `date`；Ticketmaster 官方巡演页原文 "Sydney: November 21, 2026"（同 #2 URL） |
| 12 | 2026-11-21 是周六 | GREEN | 本地 `date` 推导（11-21 weekday=5） |
| 13 | 悉尼站开演 19:30 | GREEN | 同条目 `time`；048 已用 Sydney Showground 官方场次页 "7:30pm – Event starts" 坐实 |
| 14 | 悉尼站场馆 ENGIE Stadium (Sydney Olympic Park) | GREEN | 同条目 `venue`；Ticketmaster 官方巡演页原文 "ENGIE Stadium, Sydney NSW"（同 #2 URL） |
| 15 | 悉尼站票价 $188–$748（另加 $9.90 手续费） | GREEN | 同条目 `price`，逐字复制 |
| 16 | 悉尼站距今 37 天 | GREEN | 本地 `date` 计算（2026-11-21 − 2026-10-15 = 37） |
| 17 | 两站官方购票平台均为 Ticketmaster | GREEN | 两条目 `ticket_platform`；Ticketmaster AU 为该巡演官方售票页（同 #2 URL） |
| 18 | 两站每账户限购 6 张 | GREEN | 两条目 `notes`；Ticketmaster 官方页原文 "You may purchase a maximum of 6 tickets per person."（同 #2 URL） |
| 19 | 两站票面最高一档同为 $748 | GREEN | 推导自两条目 `price` 字符串端点（$208–$748 / $188–$748） |
| 20 | 两站最低档相差 $20（墨 $208 / 悉 $188） | GREEN | 同 #19，两 `price` 端点相减 |
| 21 | 两场周六之间隔 35 天 | GREEN | 本地 `date` 计算（2026-11-21 − 2026-10-17 = 35） |
| 22 | 10-17 后清单上的体育场只剩 ENGIE | GREEN | 枚举 `events.json` 中 `verified=true` 且演出日晚于 10-17 的条目：仅悉尼站（11-21）一条为体育场 |
| 23 | 演出名「Rolling Donkey 中文喜剧开放麦」 | GREEN | `data/events.json` → `title_zh`（`verified=true`），逐字复制 |
| 24 | Rolling Donkey 每周二 19:30 | GREEN | 同条目 `recurrence="每周二"` / `time="19:30"`；今日复核 Eventbrite 售票页原文 "Every Tuesday, 7:30 PM" https://www.eventbrite.com/e/copy-of-rolling-donkey-tickets-1983189907399 |
| 25 | Rolling Donkey 场馆 Chippo Hotel，87-91 Abercrombie St, Chippendale | GREEN | 同条目 `venue`，逐字复制；Eventbrite 页原文 "87-91 Abercrombie St (Chippo Hotel)" + Chippendale NSW 2008（同 #24 URL） |
| 26 | Chippo Hotel 是酒吧场地、常办现场演出/喜剧 | GREEN | Time Out Sydney 场地页：该场地地下 gig room "hosts live music and comedy almost every other night of the week" https://www.timeout.com/sydney/bars/the-chippo-hotel |
| 27 | Rolling Donkey 官方不标价 | GREEN | 同条目 `price=null`；Eventbrite 售票页今日无任何票价信息（同 #24 URL） |
| 28 | Rolling Donkey 购票平台 Eventbrite | GREEN | 同条目 `ticket_platform`，逐字复制 |
| 29 | 下一场 Rolling Donkey 是下周二 10-20 | GREEN | 本地 `date` 计算（2026-10-15 周四后的首个周二 = 2026-10-20） |
| 30 | 3 场落在 3 个互不相同的场馆 | GREEN | 推导自三条目 `venue`：Marvel Stadium / ENGIE Stadium (Sydney Olympic Park) / Chippo Hotel，三值互不相同 |
| 31 | 3 个场馆里 2 个在悉尼、墨尔本占 1 个 | GREEN | 推导自三条目 `city` + `venue`：悉尼 = ENGIE Stadium + Chippo Hotel，墨尔本 = Marvel Stadium |
| 32 | 两个体育场明码标价、酒吧那场官方未公布票价 | GREEN | 推导自三条目 `price`：两条为区间字符串、一条为 null（并经 #27 外部复核） |

**剔除项未进文案**（不计入核查表，仅记录）：场馆顶棚/露天状况（Marvel 官网无 roof 表述、ENGIE 露天口径二手源冲突）、场馆容量（23,500 vs 24,000 打架）、开门/散场时间（gates 6:00pm vs 5:00pm 冲突，且维州交通页把 10-17 误写为 Friday；账号红线亦禁止自行添加检票/入场信息）、二级市场价（Eventworld "from $126" 为 resale 非票面）。

FACT-AUDIT-STATUS: RED=0 CHECKED=32 SOURCES-CITED=32

## 渲染状态

- 模板: `cards/053/index.html`（复制自 `cards/048/index.html`，保留 `data-theme="aushow"` 主题色 token 与 `.ticket`/`.ledger`/`issue-strip` 组件样式，仅替换 3 个 `<section class="poster xhs">` 区块内的文案）
- 张数: 3 张（封面 / 按场馆 3 行 ledger / CTA）——与 028/035/041/048 同为 3 场清单，不凑空卡
- 渲染: 交由 `automation/render_card.py`（headless Chrome 逐张单独截图），本次会话不调用任何截图工具
