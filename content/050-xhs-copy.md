# 050 — Club Voltaire 散场之后怎么回家（场馆攻略）

**选题类型**：场馆攻略（周六轮换位，2026-10-10 生成）
**场馆选择**：Club Voltaire（墨尔本 North Melbourne）——它是 `data/events.json` 中
`verified=true` 条目「候场喜剧 Loadingzone Comedy 开放麦(墨尔本,常驻)」的场馆。

**为什么选它、以及和 023 的边界**：
- 按"最久没被写过"取场馆：verified 池 8 座场馆都已各写过一轮，二讲进度为
  Marvel(004→027)、ENGIE(008→037)、TikTok Ent Centre(020→040)、Margaret Court(016→043)、
  Chippo(011→047)。只剩三座还是一讲：**Club Voltaire(023, 2026-09-12, 28 天前)**、
  Palais(030, 09-19)、Sydney Event Centre(034, 09-23)。Club Voltaire 最久，取它。
- **第六次"回头换角度重讲"**（前五次：027 Marvel 散场、037 ENGIE 散场、040 TikTok Ent Centre
  怎么去+找对门、043 Margaret Court 怎么去+认对门、047 Chippo 买票那一步）。
- 角度与 023 严格错开：**023＝怎么找到／怎么去（进场前），本篇＝散场之后怎么回家**。
  023 写的是巷子楼上／50 席／57 路 Stop 11／火车站 17 分钟／路边停车，一句都没碰"回去"。
- 切入点是 2026-10-10 复核时发现的一处真空：**场馆官网 Your Visit 页教读者"从 Elizabeth
  Street 坐 57 路"过来，而 57 路并不在墨尔本通宵电车名单里**——官网给的路线深夜不成立，
  而官网本身不会提醒这件事。这是 023 当时没写、也不可能从场馆官网单页看出来的。
- 该条目 `recurrence="常驻(场次见Eventbrite)"`、场次不固定在某一天，而墨尔本通宵班次只在
  周五/周六晚运行——"先看你那场是周几"这个动作因此成为本篇的落点，且不依赖任何
  JSON 里口径有问题的字段（time/date/price 全部不碰）。

**信源纪律**：场馆信息取自 clubvoltaire.com.au `/your-visit`（2026-10-10 WebFetch 当日复核，
与 023 记录一致）；57 路线路与"是否通宵线"取自 Yarra Trams 官网线路页
`yarratrams.com.au/routes/route-57`（2026-10-10 WebFetch）；Night Network 的夜别/频次/车站
取自 PTV 官方 Night Network 页（`ptv.vic.gov.au/nightnetwork`，今日 WebFetch 被
transport.vic.gov.au 的 Cloudflare 挑战拦下返回 403，改由 WebSearch 两次独立读取该页、
结论一致），通宵电车六条线另以维基百科 Night Network 条目交叉核对。逐条留 URL。

**红线自查**：
- 文中涉及该演出的断言只有：主办方名／城市／场馆与地址／售票平台／场次不固定，逐字取自
  `events.json` 的 `verified=true` 条目。
- **本篇不写票价、不写开场时间、不写散场时间、不写下一场日期**（`price`/`date=null`，
  `time=19:00` 与 Eventbrite 历史场次打架，沿用 023 处理）。全篇引导看 Eventbrite。
- **不写任何末班车时间数字**——Yarra Trams 线路页不列首末班，官方时刻表页今日抓不到。
- **不暗示"现在有票可买"**——今日复核 Eventbrite 主办方页仍无任何 Upcoming 场次（09-14 起
  挂 EXCEPTIONS OPEN，至今未解除），正文与 P3 卡均直接写明"今天查没有下一场"。
- 未点名任何个人／账号；不涉及防诈内容。

## 标题（14字）

看完开放麦，57 路可能已收车

## 正文（发帖文案，无外链）

上个月写过怎么找到 Club Voltaire——墨尔本 North Melbourne 那家藏在巷子楼上的 50 席小剧场，候场喜剧 Loadingzone Comedy 的常驻场地。今天写反过来那一半：**散场之后，你怎么回去。**

先说一件很多人没想过的事——**场馆官网给你的那条路线，深夜是不成立的。**

官网 Your Visit 页的原话是："从 City 坐火车过来，可以在 Melbourne Central 或 Flinders Street 下车，再从 Elizabeth Street 坐 57 路。" 来的时候没问题。问题在回去 👇

🚋 **57 路不是通宵线。** Yarra Trams 官网的线路页上，19、67、75、86、96、109 这六条的标题前面都挂着 "(Night route)"，57 路没有；PTV 的 Night Network 页也只列了这六条通宵电车，每 30 分钟一班。换句话说，**通宵名单里没有你来时坐的那条。**（57 路本身是 West Maribyrnong ↔ Flinders Street Station，经 Flemington、North Melbourne 进城。）

末班几点？Yarra Trams 的 route 57 页面**没有列首末班时间**，我不编一个数字给你——出门前在官方 App 查你那一晚的。

📅 **通宵班次只有周五、周六晚。** PTV 写的是"每周五、周六晚，以及部分公共假日"。而候场喜剧的场次在我们的数据里就写着"场次见 Eventbrite"、**不固定在某一天**——所以第一件事不是查车，是**先看你那场是周几**。落在周三、周四、周日的场次，没有"通宵车"这回事。

🚆 **真要走通宵，走去 North Melbourne 火车站。** 这里有个运气不错的地方：Night Train 全线每 60 分钟一班（只有 Stony Point 和 Flemington Racecourse 两条线除外），而 **North Melbourne 正好是官方点名"班次更密"的那几个站之一**——同名单上还有 Richmond、South Yarra、Footscray、Caulfield、Clifton Hill、Burnley。场馆官网写去这个站是步行 17 分钟、930 米。

还有一条记住：官方写明**凌晨 1 点之后，所有列车直达 Flinders Street 往返**。深夜的集合点是 Flinders Street，别按白天的习惯挑站。

⚠️ 所以出门前就两个动作：**① 看清你那场是周几 ② 不是周五周六，先把回去的方案想好。** 别等散场了站在 Raglan St 巷口才开始查。

⚠️ 还有一句得说清楚：**今天（10-10）我去翻候场喜剧的 Eventbrite 主办方页，上面暂时没有挂出下一场。**所以这篇是攻略，不是约你今晚去——等场次重新挂出来，再按上面这套走。

评论区扣 1，私信发你候场喜剧的 Eventbrite 主办方页，有新场次我提醒你～澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #墨尔本 #脱口秀 #中文脱口秀 #开放麦 #墨尔本生活 #看演出攻略 #墨尔本交通 #NorthMelbourne

## 卡片文案结构（3张，票根美学）

> 张数说明：prompt 对场馆攻略类建议 2–3 张，本篇取 **3 张**，与 023（同场馆一讲）一致。
> 结构为 封面／散场 4 条 ledger／收尾 CTA，三张都满，无空卡。本篇可核实事实密度与 023
> 相当（4 条硬事实 + 1 条"官方没写所以不给数字"），硬拆成 4 张必然凑数。
> P3 保留账号档案里写死的固定 kicker 作品牌锚。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 场馆攻略 · Club Voltaire
- 大字标题: 看完开放麦 / 57 路可能已收车
- 副标题: 墨尔本 North Melbourne · 散场篇
- 说明: 场馆官网教你坐 57 路来。深夜，这条路线不成立。
- 底部条: North Melbourne · MEL — 散场怎么回去
- 配图: 无（场馆攻略不挂任何演出海报，沿用 004／008／011／023 做法）

**P2 散场之后的 4 件事（ledger 4条）**
1. 57 路不是通宵线 — Yarra Trams 官网只给 19/67/75/86/96/109 标 "(Night route)"；PTV 也只列这六条，每 30 分钟一班
2. 通宵只在周五、周六晚 — PTV 原话"每周五、周六晚及部分公共假日"。候场喜剧场次不固定，先看你那场是周几
3. 走去 North Melbourne 站 — Night Train 全线每 60 分钟（Stony Point、Flemington Racecourse 除外），该站是官方点名"班次更密"的之一
4. 凌晨 1 点之后 — 官方写明所有列车直达 Flinders Street 往返。深夜的集合点是 Flinders Street
- 收尾: 57 路末班几点，Yarra Trams 线路页没列——出门前查官方 App 当晚的，别信任何二手数字（包括这张卡）。
- 底部条: 场馆官网：火车站步行 17 分钟 930 米 — Level 1 / 14 Raglan St

**P3 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 来的那条路 / 不一定送你回去
- 正文: 官网教你从 Elizabeth Street 坐 57 路过来。57 路不在通宵名单里。
- 补充: 先看场次是周几，再决定怎么回去。注：10-10 查主办方页暂未挂出下一场。评论区扣 1，私信发你候场喜剧的主办方页，有新场次我提醒你。
- 底部条: VOL. 050 — 简介里有完整演出日历

## 事实核查表

| 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|
| 候场喜剧 Loadingzone Comedy 的墨尔本常驻场地为 Club Voltaire，地址 1st Floor/14 Raglan St, North Melbourne | GREEN | `data/events.json` 条目「候场喜剧 Loadingzone Comedy 开放麦(墨尔本,常驻)」：`venue="Club Voltaire, 1st Floor/14 Raglan St, North Melbourne"`、`city=墨尔本`、`verified=true` | JSON 的 venue 字段本身即含店名与地址；文案"50 席小剧场""巷子楼上"为 023 已核实事实的一句回指，不是本篇新增断言 |
| 该开放麦场次由 Eventbrite 售票，且场次不固定在某一天 | GREEN | 同上条目 `ticket_platform=Eventbrite`、`status=on_sale`、`recurrence="常驻(场次见Eventbrite)"` | `date=null`、`time` 与 Eventbrite 历史场次打架（见 023），故全文不给任何日期/时间数字，只给"先看你那场是周几"这个动作 |
| 场馆官网自述地址为 Level 1 / 14 Raglan Street, North Melbourne 3051 | GREEN | https://www.clubvoltaire.com.au/your-visit （2026-10-10 WebFetch，原文 "Level 1 / 14 Raglan Street, North Melbourne 3051, VIC AUSTRALIA"） | 今日复核与 023（2026-09-12）记录逐字一致，页面仍在线 |
| 场馆官网给出的"从 City 过来"的路线是：火车到 Melbourne Central 或 Flinders Street，再从 Elizabeth Street 坐 57 路 | GREEN | 同上页面（原文 "If you're coming by train from the City you can get off at Melbourne Central or Flinders Street station and catch the 57 tram from Elizabeth Street."） | 本篇核心钩子。023 未引用过这一句；文案为该原文的中译，未加任何官网没写的内容 |
| 场馆官网写 North Melbourne 火车站步行 17 分钟、930 米 | GREEN | 同上页面（原文 "North Melbourne Railway Station is a 17min (930m) walk away."） | 与 023 同一数字、同一单一官网口径；本篇用途不同（023＝怎么来，本篇＝通宵回家的落脚点），文案已明确"场馆官网写" |
| 57 路电车为 West Maribyrnong ↔ Flinders Street Station，经 Flemington、North Melbourne 进城 | GREEN | https://yarratrams.com.au/routes/route-57 （2026-10-10 WebFetch，标题 "57 West Maribyrnong to Flinders Street Station"，并写 "via Flemington > North Melbourne > City"） | 官方运营方线路页，取代 023 当时用的维基百科交叉核对 |
| 57 路不是通宵电车线；Yarra Trams 官网只给 19、67、75、86、96、109 六条标 "(Night route)" | GREEN | 同上 Yarra Trams route-57 页（该页标题无 "(Night route)" 前缀，而同一站点 19/67/75/86/96/109 带该前缀）；PTV 官方 Night Network 页亦只列这六条通宵电车 https://ptv.vic.gov.au/nightnetwork | 正向枚举（官方只列六条且不含 57）＋同站点标签缺失，两条独立官方依据互证，非单纯"查不到即否定" |
| Yarra Trams route 57 页面不列首末班时间 | GREEN | 同上 Yarra Trams route-57 页（2026-10-10 WebFetch：页面只给站点表与目的地，首末班时间需跳转 transport.vic.gov.au 的线路时刻表；页面上唯一出现的时段 "6am - midnight (all night Friday & Saturday)" 是客服电话时间，不是行车时间） | 这是文案"我不编一个末班数字给你"的依据。transport.vic.gov.au 今日被 Cloudflare 挑战拦下（HTTP 403），时刻表无法核实，故整篇不出现任何末班数字 |
| 通宵电车每 30 分钟一班（19/67/75/86/96/109 六条） | GREEN | PTV 官方 Night Network 页 https://ptv.vic.gov.au/nightnetwork （2026-10-10 两次独立 WebSearch 读取该页，结论一致："Night Trams run every 30 minutes on routes 19, 67, 75, 86, 96 and 109"）；维基百科 Night Network (Melbourne) https://en.wikipedia.org/wiki/Night_Network_(Melbourne) （2026-10-10 WebFetch，原文 "The following routes operate overnight to half-hour frequencies"，列 19、67、75、86、96、109） | 官方页今日 WebFetch 被 Cloudflare 挑战拦下，按 prompt 第4步允许的"WebSearch 核实到的 URL"采信，并以维基条目独立交叉核对，六条线号与频次完全一致 |
| 墨尔本 Night Network 只在每周五、周六晚及部分公共假日运行 | GREEN | 同上 PTV Night Network 页（"Night Network operates every Friday and Saturday night, as well as on selected public holidays"）；维基条目同句（"operates every Friday and Saturday night, as well as on selected public holidays"）；Yarra Trams route-57 页客服时间亦写 "all night Friday & Saturday" 佐证周五/周六为通宵夜 | 三处口径一致。这是本篇最关键的一条"别想当然"事实 |
| Night Train 全线每 60 分钟一班，Stony Point 与 Flemington Racecourse 两条线除外 | GREEN | 同上 PTV Night Network 页（"Night Trains run every 60 minutes on all lines, except Stony Point and Flemington Racecourse"，两次独立 WebSearch 读取一致）；维基条目（"Trains operate hourly on all lines"，并写 Flemington Racecourse 与 Stony Point 线不运行） | 两源一致 |
| North Melbourne 是官方点名"班次更密"的通宵车站之一（同名单：Richmond、South Yarra、Footscray、Caulfield、Clifton Hill、Burnley） | GREEN | 同上 PTV Night Network 页（"Some stations have more frequent trains, including Richmond, South Yarra, North Melbourne, Footscray, Caulfield, Clifton Hill and Burnley"，2026-10-10 两次独立 WebSearch 读取、七个站名完全一致） | 文案未写"更密"到底是多少分钟一班——官方页未给该数字，不补 |
| 凌晨 1 点之后所有列车直达 Flinders Street 往返 | GREEN | 同上 PTV Night Network 页（"After 1am, all trains run direct to and from Flinders Street Station"，两次独立 WebSearch 读取一致） | 文案按官方原文表述并标明"官方写明"，**不自行推出"City Loop 停运"**——官方原句没这么写，详见主动排除项 |
| 2026-10-10 候场喜剧 Eventbrite 主办方页未挂出任何即将到来的场次 | GREEN | https://www.eventbrite.com/o/loadingzone-comedy-75417874333 （2026-10-10 WebFetch：Upcoming 标签下无任何场次标题/日期/场馆） | 维持 09-14 起的 EXCEPTIONS OPEN 判定。因此本篇**不写"票在 Eventbrite 上"这类暗示当前有票可买的话**，改为在正文与 P3 卡上直说"今天查没有下一场"——这也是本篇定位为 evergreen 场馆攻略、不绑定任何场次的原因 |

**主动排除项（查不到官方依据／口径打架，本篇一律不写）**：

- **57 路（或任何线路）的具体末班时间**——Yarra Trams 线路页不列，官方时刻表所在的
  transport.vic.gov.au 今日 WebFetch 与 curl 均被 Cloudflare 挑战拦下（HTTP 403）。
  全篇不出现任何末班数字，改为明确告诉读者"出门前查官方 App 当晚的"。
- **"凌晨 1 点后不走 City Loop"**——官方原文只写"所有列车直达 Flinders Street 往返"，
  未提环线停运。文案只复述原文＋"深夜的集合点是 Flinders Street"这一句不越界的读法。
- **myki／tap-and-go 刷卡与充值规则**——2026-06 起信用卡 tap and go 已上线墨尔本火车线，
  但电车/巴士的时间表官方称"未来几周公布"，各来源互相打架（一份 FAQ 称 2026-07 起电车巴士
  已可用，与主流报道不符）。涉及读者真金白银，整块不写。
- **夜间巴士具体线路**——维基条目称有 11 条自郊区火车站发出，但无法定位到服务
  North Melbourne／Errol St 的具体线路与站点，不写。
- **"更密"到底多少分钟一班**（North Melbourne 等七站）——官方页只说 more frequent，无数字，不补。
- **场馆演出时段 "Wednesday to Sunday 7pm–11pm"**——沿用 023 处理：该时段与候场喜剧
  Eventbrite 历史场次（含周日 14:00 开场）打架。因此本篇也**不写"演出几点散"**，
  全篇不绑定任何散场时刻。
- **开场时间／下一场日期／票价**——`time` 口径有问题、`date=null`、`price=null`，沿用 023。
- **深夜步行安全建议、哪条路更亮、巷口照明**——无任何官方依据，不写。
- **打车／网约车落客点**——场馆官网未提，不写。
- **无障碍通道／电梯**——沿用 023，官网未提；本篇不触及。
- **场馆电话**——官网 contact 页有列，但小红书文案不放外部联系方式（沿用 022／023 做法）。

FACT-AUDIT-STATUS: RED=0 CHECKED=14 SOURCES-CITED=14

## 渲染状态

- 模板: `cards/050/index.html`，复制自 `cards/023/index.html`（同场馆、同为 3 张纯文字版式，
  且 `<head>` 与 `cards/001/index.html` 逐字一致、仅 `<title>` 不同，本次已 diff 确认）。
  `<html data-theme="aushow">`、主题色 token、字体、`.ticket`/`.ledger`/`issue-strip`
  组件样式全部原样保留，仅替换 `<title>` 与 `<section class="poster xhs">` 区块内文案。
- 卡片数: 3 张 `<section class="poster xhs" id="xhs-01…03">`
- 渲染: 交由 `automation/render_card.py`（headless Chrome 逐张截图 + PIL 校验 1080×1440）。
  本次会话按 `daily-xhs-prompt.md` 第 0 节要求，未调用任何浏览器/截图工具。
