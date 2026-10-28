# 064 — ENGIE Stadium 无障碍观演攻略（场馆攻略）

**选题类型**：场馆攻略（周三轮换位，2026-10-28 生成）
**场馆选择**：ENGIE Stadium（悉尼 Sydney Olympic Park）——它是 `data/events.json` 中
`verified=true` 条目「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」的 `venue`
（`"ENGIE Stadium (Sydney Olympic Park)"`，`date=2026-11-21`）。按本栏目 055 写定的
"最久没被写过"取法，8 座 verified 场馆上次被写的时间依次为：**ENGIE Stadium(037,
2026-09-26, 32 天前)**、TikTok Entertainment Centre(040, 09-30)、
Margaret Court Arena(043, 10-03)、Chippo Hotel(047, 10-07)、Club Voltaire(050, 10-10)、
Marvel Stadium(055, 10-17)、Palais Theatre(058, 10-21)、
Sydney Event Centre(061, 10-24)——**ENGIE 最久，故取它**。这是该馆的**第三讲**，
也是本栏目**第十次"回头换角度重讲"**。

**角度（与 008／037 零重叠）**：008（08-26）写"**怎么到 / 怎么进**"（4 条交通 + 包限 A4、
cashless、旗帜尺寸、电子烟、外带食物）；037（09-26）写"**散场之后怎么回**"（火车加开、
出租点、渡轮别赌、封路改道）。两篇的读者都是**自己能走能跑、一个人来的那种观众**。
本篇把读者换成**推轮椅、推婴儿车、带怕吵的小孩或长辈**的那一个，主线是
**一半的事必须在买票那一刻就定下来，另一半在门口就决定了能不能回场**。
这是 ENGIE 三讲里**第一次碰无障碍**——008／037 两篇一个字都没写过。
与 055（Marvel 无障碍）同类但不同馆、且几乎零重复项：Marvel 那篇的主线是
无障碍票买法／Companion Card add-on／UbiPark 反着订／外部电梯与门号；
ENGIE 这边官网给的是完全另一套东西——**pass out 机制、感官包、安静室、
按 aisle 号点名的"避开楼梯"订座建议、无酒精区、Metrasens 安检门对医疗植入物的说明**，
Marvel 官网一条都没有。

**本篇的信源升级（008／037 当时没用到的一手页）**：008 用的是 `getting-here` 与
`conditions-of-entry`，037 用的是 Transport NSW 的大型活动页。本次新接入三处同站一手源：
①`/engie-stadium/engie-stadium-faqs/` 的 **Accessibility 整段**（008 当时只取了这页的
cashless 与接水站两行，无障碍段未碰）；②`/visitors/?tab=Accessibility`；
③场馆自己的 **Accessibility PDF**（`/globalassets/document-library/sydney-showground/
accessibility/sydney-showground-accessiblity.pdf`，5 页）。三处均为 2026-10-28 当日
curl 原文抽取。

**🔴 本次核查发现一处官网自相矛盾（已整块剔除，并影响 008／037 两篇旧稿）**：
停车价格在**同一个官网页面内**给出两套数字——`/visitors/` 的 Getting here 段写
"$8 per hour, up to a maximum fee of $40 per day"（008 据此写过 $8／$40，037 写过 $40），
而同页 FAQ 段写 "Parking costs between $7 per hour, up to a maximum fee of $35 per day"
并把统一费率写成 $35。按本栏目"两处官方口径打架一律不写"的纪律，**本篇不写任何停车
金额**，只写无障碍车位的数量与限高。此事已追加进 `EXCEPTIONS.md`（旧稿里的 $8／$40
需要用户裁决是否更正）。

**红线自查**：
- 全篇唯一涉及单场演出的断言是**日期＋场馆**两个字段，逐字取自 `events.json` 的
  `verified=true` 条目；**不写票价／购票平台／限购／主办方／开演时间**（不是本篇主题，
  且避免与安利篇 002/018/029/038/049/060 重复）。
- 场馆官网 What's On 当日列出的其余在售场次在 `data/events.json` 中**均非 `verified=true`**，
  按"未核实的不发"一律**不点名、不暗示、不计数**。
- 不点名任何个人／账号。**不落任何外部联系方式字符串**——无障碍订票专线、场馆客服电话、
  票务方邮箱、轮椅租赁公司电话，官网都给了，但沿用 055／047／054 的惯例改写成
  "官网上列了对应的专线"（见剔除项，这是排版/风控选择，不是事实问题）。
- 文中出现的所有数字都是**车位数／限高／aisle 号／限时分钟**，没有一个是票价。

## 标题（15字）

ENGIE无障碍，安静室在场外

## 正文（发帖文案，无外链）

11 月 21 日周杰伦悉尼站在 ENGIE Stadium（Sydney Olympic Park）。这篇不讲怎么到、也不讲散场，讲**推轮椅、推婴儿车、带怕吵的小孩或长辈**的那一个 👇

🚪 **安静室在球场范围之外，出去之前要先拿 pass out**。官网原话：安静室和成人协助更衣室都在 **Grand Parade**，这些设施位于球场范围之外，看球场场次的观众**必须先向闸口工作人员领一张 pass out**。孩子中途受不了想躲一下，这张条子就决定了你还能不能再进来。

🎧 **感官包是真有的**。官网写明 ENGIE 场次提供：**成人和儿童两种尺寸的耳机或耳罩**，加几个 fidget 玩具。押一份 ID、把名字电话留给安静室工作人员就能领，还的时候 ID 拿回来。

⚠️ **但只在部分场次开放**。官网两处反复写同一句：这些设施只在**部分场次**开放，去之前上**该场次的 What's On 页面**确认当天开不开；高峰时段还有 **20 分钟限时**。

🪑 **不想爬楼梯的，官网直接点了排号**。原话是：低行动能力的观众建议订 **201-202、206-208、212-214、218、230、232、235-236、238-239、244、246-249、251、253 这些 aisle 的最后一排**，可以完全避开楼梯。无障碍席和轮椅位不在场馆这边订——官网写明由**该场次的票务方**直接受理。

🍺 **顺手勾一个无酒精区**。买票时就能选 alcohol-free 座位；已经买完的，当天找客服说也行。带孩子或带长辈的，这一勾比什么都值。

🅿️ **停车是反着订的**。离球场最近是 P1、P5、P6，无障碍车位官网给的是 **P1 179 个、P5 77 个、P6 18 个**。订法是**先买一个普通车位**，当天再停无障碍车位，车上**必须出示无障碍停车许可**，不然要罚。开高顶改装车的注意：**P1 限高 2 米**。

进场之后还有 3 条：**上 4 层认对 foyer**（Members Stand foyer 通 420-430，Cumberland Stand 的 4 层官网明写不是无障碍的）；**场馆自己不出租轮椅**，但需要人推你到座位的，闸口工作人员可以用轮椅协助；**带心脏起搏器的可以放心过安检**，官网写明安检门对人体和任何医疗植入物都没有影响。

官网在"演唱会和特别活动"那几处反复写的是同一句：**请联系场馆**。有需求的提前填官网那份无障碍协助表，别等到当天。

评论区扣 1，私信发你这份 ENGIE Stadium 无障碍清单，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #悉尼 #演唱会 #周杰伦 #ENGIEStadium #悉尼演出 #无障碍出行 #看演出攻略

## 卡片文案结构（6张，票根美学）

> 张数说明：prompt 建议场馆攻略类 2–3 张，本篇用 6 张，理由是**四块内容分别对应四个
> 不同的时间点、互不可换位**，压并任何两块都会让读者在错误的时间点拿到信息：
> P2＝**买票那一刻**（席位/排号/无酒精区/协助表，买完就改不了）、
> P3＝**出门之前**（车位反着订/限高/街边车位/火车协助，到了场馆就来不及订）、
> P4＝**在闸口**（pass out 必须出去之前拿，这是全篇唯一"错一步就回不去"的动作）、
> P5＝**已经在场内**（电梯 foyer/轮椅/助行器/安检门）。封面与 CTA 是账号档案里写死的
> 品牌结构（P4… 即末张固定 kicker 作品牌锚）。每张 4 条实条目，无空卡、无凑数卡。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 场馆攻略 · ENGIE Stadium
- 大字标题: 安静室 / 在球场外面
- 副标题: 出去之前先拿 pass out
- 说明: 推轮椅、推婴儿车、带怕吵的小孩或长辈去 ENGIE——有一半的事在买票那一刻就定了。全部取自场馆官网。
- 底部条: 悉尼 Sydney Olympic Park — 官网原话 outside the stadium footprint
- 配图: 无（场馆攻略不挂任何演出海报，避免"海报张冠李戴"复发）

**P2 买票那一刻就定了（ledger 4条）**
1. 想完全避开楼梯 — 官网点名：低行动能力观众建议订 201-202、206-208、212-214、218、230、232、235-236、238-239、244、246-249、251、253 这些 aisle 的最后一排
2. 无障碍席／轮椅位 — 不在场馆这边订；官网写明由该场次的票务方直接受理，官网上列了对应的无障碍订票专线；到场客服也能协助
3. 无酒精区 — 买票时勾 alcohol-free 座位；已经买了的，当天找客服说
4. 无障碍协助表 — 官网有一份 ENGIE Stadium 专用的无障碍协助申请表；官网在"演唱会与特别活动"多处反复写"请联系场馆"
- 底部条: 来源 sydneyshowground.com.au — ENGIE Stadium FAQ

**P3 出门之前（ledger 4条 + body 一段）**
1. 最近三个车场的无障碍车位 — 离球场最近是 P1、P5、P6；无障碍车位数 P1 179 个、P5 77 个、P6 18 个
2. 反着订 — 官网写法：先买一个普通车位，当天再停无障碍车位；车上必须出示无障碍停车许可，否则会被罚
3. 开高顶改装车看限高 — P1 限高 2 米；P2、P4、P5、P6 官网列为露天车场
4. 坐火车的 — Trip Planner 里有无障碍选项可勾；官网写明遇 accessible event，Showground 会与 Sydney Trains 协调，在 Lidcombe 站安排斜坡操作员协助
- body: 街边也有无障碍车位（Showground Road 8 个、Dawn Fraser Ave 西侧 5 个），但官网提醒大型活动封路时可能用不了。本篇不写任何停车金额——官网同一页给了两套数字，口径未统一。
- 底部条: 车位数与限高取自官网 Visitors · Accessibility

**P4 在闸口：先拿 pass out（ledger 4条）**
1. 设施在球场范围之外 — 安静室与成人协助更衣室都在 Grand Parade，官网明写位于球场范围之外；看球场场次须先向闸口工作人员领一张 pass out
2. 安静室里面是什么 — 柔和灯光、可触摸与视觉元素帮助重新聚焦、声学吸音板、豆袋椅和可以放松的空间
3. 感官包怎么领 — ENGIE 场次提供，内含成人与儿童两种尺寸的耳机／耳罩加 fidget 玩具；押一份 ID、留名字电话给安静室工作人员，归还时取回 ID
4. 两个硬限制 — 只在部分场次开放，去之前查该场次 What's On 页；高峰时段 20 分钟限时
- 收尾: 成人协助更衣室需 NSW 发的 MLAK 钥匙与认可的吊具，且须有受过训练的照护者全程在场；室内有全电动吊机和可升降的成人更衣台。
- 底部条: 感官包与安静室 — 以该场次 What's On 页为准

**P5 已经在场内（ledger 4条）**
1. 上 4 层认对 foyer — Martin & Angus Stand foyer 通 402-412，Council Stand foyer 通 414-418，Members Stand foyer 通 420-430，Sydney Royal Stand foyer 通 Skydeck；Cumberland Stand 的 4 层官网明写不是无障碍的
2. 场馆不出租轮椅 — 官网 FAQ 原话；但需要有人推你到座位的，闸口工作人员可以用轮椅协助
3. 助行器与婴儿车 — 拐杖、膝代步车等助行器可带入、须过安检，活动中收在座位下或指定婴儿车位；婴儿车折起放座位下，或停 201、221、402、431 附近的指定车位
4. 安检门对医疗植入物无影响 — 官网写明安检门是 Metrasens FMDS，对人体和任何医疗植入物或设备都没有影响
- 收尾: 育婴室两处：球场 concourse 上 Members Stand 入口对面，以及 Grand Parade（后者在球场范围外，同样要先拿 pass out）。
- 底部条: 以官网 ENGIE Stadium FAQ 为准 — 出发前再看一眼

**P6 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 出闸之前 / 先要那张条
- 正文: pass out、感官包、避开楼梯的那几排、P1 限高 2 米——出门前先存好这份清单。
- 底部条: VOL. 064 — 简介里有完整演出日历

## 事实核查表

信源代号：
**A** = `https://www.sydneyshowground.com.au/engie-stadium/engie-stadium-faqs/`（2026-10-28 curl 原文）
**B** = `https://www.sydneyshowground.com.au/visitors/?tab=Accessibility`（2026-10-28 curl 原文）
**C** = `https://www.sydneyshowground.com.au/globalassets/document-library/sydney-showground/accessibility/sydney-showground-accessiblity.pdf`（场馆自有 Accessibility PDF，5 页，2026-10-28 curl 原文）
**D** = `https://www.sydneyshowground.com.au/accessibility/` 与 `https://www.sydneyshowground.com.au/accessibility/accessibility-assistance/`（2026-10-28 curl 原文）
**E** = 本仓库 `data/events.json`

| # | 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|---|
| 1 | 周杰伦悉尼站于 2026-11-21 在 ENGIE Stadium（Sydney Olympic Park）举行 | GREEN | **E** 条目「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」：`date="2026-11-21"`、`venue="ENGIE Stadium (Sydney Olympic Park)"`、`city="悉尼"`、`verified=true` | 正文只用日期＋场馆两个字段，未复述 `price`／`ticket_platform`／`notes` 的限购 |
| 2 | 安静室与成人协助更衣室都位于 Grand Parade | GREEN | **A** 原文 "Quiet Room & Adult Assisted Change Room: The quiet room and adult assisted change room are both located on Grand Parade."；**B** 同句互证（另 "Located: Grand Parade"） | 只照抄官网给的位置串，未推断它离球场多远（见剔除项） |
| 3 | 这些无障碍设施位于球场范围之外；看球场场次的观众须先向闸口工作人员领取 pass out 才能前往 | GREEN | **A** 原文 "Pass Out Required: Please note, these accessible amenities are located outside the stadium footprint. Patrons attending stadium events must collect a pass out from the gate staff before accessing these facilities." | **本篇的核心事实**。008 曾把"中途出场再入场（pass out）政策"列为剔除项（当时官网只有《Inclosed Lands Protection Act 1901》的非法再入场条款，与普通观众无关）；本次在 ENGIE FAQ 的 Accessibility 段找到**官网明文**，故本篇可写。文案未推断"没有 pass out 就一定进不来"，只写官网的"must collect … before accessing" |
| 4 | ENGIE Stadium 场次提供感官包，内含成人与儿童两种尺寸的耳机／耳罩及 fidget 玩具 | GREEN | **A**／**B** 同文 "Sensory bags are available at ENGIE Stadium events … Each bag includes headphones/earmuffs, available in both adult and child sizes, and fidget toys to help manage sensory overload." | 两页同一表述；未写数量、不承诺一定领得到 |
| 5 | 领取感官包须提供一份 ID 并把姓名与电话留给安静室工作人员，归还时取回 ID | GREEN | **A**／**B** 同文 "you will need to provide a form of ID and leave your name and phone number with the quiet room staff. Your ID will be returned to you once the sensory bag is returned." | 逐条照搬，未补写接受哪种 ID |
| 6 | 这些无障碍设施只在部分场次开放，须查该场次 What's On 页确认 | GREEN | **A** 原文 "the facilities are open for use during select ENGIE Stadium events. Check the event's \"What's On\" page to confirm availability"；感官包另有 "available at select events when the Grand Parade facilities are open"；**B** 互证 | 正文"官网两处反复写同一句"即据此；**本篇不承诺 11-21 当天这些设施会开**（官网未按场次公布） |
| 7 | 高峰时段对无障碍设施适用 20 分钟限时 | GREEN | **A**／**B** 同文 "To ensure all patrons who require use can access the space, a 20-minute time limit is applied during peak times." | 官网未定义"peak times"，文案也不定义 |
| 8 | 安静室配置柔和灯光、可触摸与视觉元素、声学吸音板、豆袋椅与放松空间 | GREEN | **A**／**B** 同文 "Featuring calm lighting, tactile and visual elements to help patrons refocus and desensitise, acoustic panelling for even quieter sound, soft bean bag chairs and space to relax." | 逐项对应，未增补官网没写的设施 |
| 9 | 成人协助更衣室须 NSW 发出的 MLAK 钥匙与认可的吊具，须有受过训练的照护者全程在场；内有全电动吊机与可升降成人更衣台 | GREEN | **A**／**B** 同文 "Use of the room requires a NSW issued MLAK key and approved harness. A trained carer/helper must be present at all times. Includes a fully electric hoist and height-adjustable adult change table." | 未写 MLAK 钥匙怎么申请（官网未涉及，见剔除项） |
| 10 | 低行动能力观众若要完全避开楼梯，官网建议订 201-202、206-208、212-214、218、230、232、235-236、238-239、244、246-249、251 或 253 这些 aisle 的最后一排 | GREEN | **A** 原文 "To avoid stairs altogether, patrons with low mobility requirements are encouraged to book seats in the back row of aisles 201-202, 206-208, 212-214, 218, 230, 232, 235-236, 238-239, 244, 246-249, 251 or 253." | 号码逐字照抄、未增删。008／037 把"座位区推荐"整块列为剔除项（理由是官网无说明、属凭印象编）；本条**是官网自己给的订座建议**，不是视野推荐，故可写——文案也只讲"避开楼梯"，不讲视线好不好 |
| 11 | 无障碍席与轮椅位由该场次的票务方直接受理；场馆官网列出对应的无障碍订票专线；到场客服也可协助 | GREEN | **A** 原文 "Accessible seating requests are managed directly by the event's ticketing provider … please contact the appropriate ticketing provider for the event you are attending."＋同页 "Customer service staff can also assist on the day if required."；**B** 互证；**C** 第 4 页同口径 | 官网列的两家专线号码与邮箱**不落字面字符串**（见剔除项）；也未断言 11-21 那场归哪一家票务方（`events.json` 虽写 Ticketmaster，但这是演出字段、不是场馆无障碍流程的依据，本篇不混用） |
| 12 | 无酒精区可在购票时选择 alcohol-free 座位；已购票者可于当天向客服提出 | GREEN | **A** 原文 "Alcohol-free seating is available … choose the 'alcohol-free' seating option when purchasing tickets. If you have already purchased your ticket, but wish to sit in the alcohol-free area, please speak with customer service staff on the day." | 未断言每场都有该选项（官网用 "is available" 的泛述），文案写"买票时就能选"与之对齐 |
| 13 | 离 ENGIE Stadium 最近的车场是 P1、P6、P5 | GREEN | **A** 原文 "The closest to ENGIE Stadium are P1, P6 & P5."；**B** 同句互证 | 008 已核过同一条，本次复核仍一致 |
| 14 | 无障碍车位数：P1 179 个、P5 77 个、P6 18 个 | GREEN | **B** 原文 "P1 car park - 179 spaces / P5 car park - 77 spaces / P6 car parks - 18 spaces"（同段另列 P2 10、P3 46、P4 32、P8 6） | 只写离 ENGIE 最近那三个（与第 13 条对齐）；**不写总数**（见剔除项：官网两处总数打架） |
| 15 | 预订无障碍车位的方式是先买一个普通车位，当天再使用无障碍车位 | GREEN | **B** 原文 "To pre-book your parking, buy a standard space in your preferred car park and use an accessible space on the day of your visit." | 与 055 写 Marvel／UbiPark 的"反着订"是同一类机制但**不同场馆、不同平台**，文案未跨馆套用 |
| 16 | 使用无障碍车位须出示无障碍停车许可，否则会被罚 | GREEN | **B** 原文 "When using an accessible parking space, please display your Accessible Parking Permit to avoid fines."；**C** 第 2 页互证 "please display your Mobility Parking Permit to avoid fines" | 两处用词不同（Accessible／Mobility Parking Permit）、所指同一件事；文案取中性表述"无障碍停车许可"，不写英文名以免落定某一种叫法 |
| 17 | P1 车场限高 2 米；P2、P4、P5、P6 为露天车场 | GREEN | **B** 原文 "P1 - 2 metres / P3 - 2.1 metres / P8 - 2.3 metres / All other carparks (P2, P4, P5 and P6) are open air car parks." | 文案**未写"露天车场没有限高"**——官网只说是露天、未给数字，不替它补结论 |
| 18 | 街边无障碍车位：Showground Road 8 个、Dawn Fraser Avenue 西侧 5 个；大型活动封路期间可能不可用 | GREEN | **B** 原文 "There are on-street accessible spaces along Showground Road (8 spaces) and Dawn Fraser Avenue west (5 spaces). Please plan ahead as these may not be available during major events due to road closures."；**C** 第 2 页互证 Showground Road 8 个 | — |
| 19 | Transport NSW 的 Trip Planner 有无障碍选项；遇 accessible event，Sydney Showground 会与 Sydney Trains 协调在 Lidcombe 站安排斜坡操作员协助 | GREEN | **C** 第 2 页原文 "Plan an accessible trip on public transport … Just choose your options and select the accessibility check box … If there is an accessible event, Sydney Showground will liaise with Sydney Trains to ensure there are ramp operators available at Lidcombe station to assist with access." | Lidcombe 正是 008 核过的 Sprint 摆渡线起点，两篇口径衔接；文案未承诺 11-21 那场属于 "accessible event"（官网未按场次公布），只写机制 |
| 20 | 上 4 层的电梯：Martin & Angus Stand foyer 通 aisles 402-412、Council Stand foyer 通 414-418、Members Stand foyer 通 420-430、Sydney Royal Stand foyer 通 Skydeck；Cumberland Stand 的 4 层不具无障碍通行 | GREEN | **A** 原文 "Lift access to level 4 is available in: Martin & Angus Stand foyer – For access to aisles 402-412 / Council Stand foyer – For access to aisles 414-418 / Members Stand foyer – For access to aisles 420-430 / Sydney Royal Stand foyer – For access to Skydeck. Please note Cumberland Stand level 4 is not accessible." | 四条对应关系与否定项逐字照抄；正文为控制长度只举 Members Stand 与 Cumberland 两例，**卡片 P5 给全**，两处都未改写对应关系 |
| 21 | 场馆不出租轮椅；需协助前往座位时，闸口工作人员可用轮椅提供协助 | GREEN | **A** 原文 "We do not have wheelchairs for hire, but if you require assistance to your seat, gate staff are able to assist with a wheelchair."；**C** 第 3／4 页互证 "Assistance to your Seat. If you require assistance to your seat, gate staff are able to assist with a wheelchair." | **C** 另提到可向一家外部康复器材公司租轮椅并给了电话——与"场馆不出租"不矛盾（主体不同），但属第三方商业联系方式，按惯例不写（见剔除项） |
| 22 | 拐杖、膝代步车等助行器可带入场馆，须过安检；活动期间须置于座位下或指定婴儿车位 | GREEN | **A**／**B** 同文 "Crutches, knee scooters and other mobility aids are permitted into the stadium, subject to security screening. During the event, they must be stored under your seat or in a designated pram storage bay." | — |
| 23 | 婴儿车须折叠后置于座位下，或停放在 aisles 201、221、402、431 附近的指定婴儿车位 | GREEN | **A** 原文 "Prams must be folded and placed under your seat or parked in one of the designated pram bays located near aisles 201, 221, 402 and 431."；**C** 第 4 页互证同一组号码 | 两处号码一致 |
| 24 | 育婴室两处：球场 concourse 上 Members Stand 入口对面，以及 Grand Parade | GREEN | **A** 原文 "There are two conveniently located parents' room facilities: one on the stadium concourse across from the Members Stand entrance, and one on Grand Parade." | **B** 另列出第三处 "Dome Foyer, inside the Dome"，但 Dome 是 Showground 园区内**另一栋建筑、不是球场**，而 **A** 的 ENGIE 专页明确写"两处"；本篇按 ENGIE 口径只写两处（见剔除项） |
| 25 | 安检门为 Metrasens FMDS，官网写明对人体及任何医疗植入物或设备均无影响 | GREEN | **A** 原文 "the security detection system patrons pass through is a Metrasens FMDS and has no effect either on the human body or on any medical implant or device." | 照搬官网口径，**不自行扩展成"起搏器一定安全"的医学结论**——文案写的是"官网写明…没有影响"，主语是官网 |
| 26 | 官网在"演唱会与特别活动"多处要求联系场馆；并设有 ENGIE Stadium 专用的无障碍协助申请表 | GREEN | **A** 页三处出现 "For concerts and special events, please contact the venue."（急救点位置／育婴室／寄存）；**D** 原文 "If you require additional accessibility support for your visit, let our team know by completing the Accessibility Assistance form." 及该表页标题 "Accessibility Support for ENGIE Stadium Events" | 表单本身是 JS 渲染、未抓到字段内容，故文案只写"有这份表、提前填"，不描述它问什么 |

**主动排除项（官网口径打架／查不到依据／与本篇角度无关，一律不写）**：

- 🔴 **停车金额（全部）**——`/visitors/` **同一页之内**给出两套数字：Getting here 段
  "$8 per hour, up to a maximum fee of $40 per day"（预订 "$40 per car for the day"），
  FAQ 段 "between $7 per hour, up to a maximum fee of $35 per day"（统一费率 "$35"）。
  按"两处官方口径打架一律不写"整块剔除。**注意这同时影响旧稿**：008 写过 $8／小时与
  $40／天，037 写过 $40 统一价——已写入 `EXCEPTIONS.md` 交用户裁决，本次未改动旧稿。
- **无障碍车位总数**——**C** 第 2 页写 "376 accessible and mobility car parking spaces"，
  **B** 写 "almost 400" 且逐场相加（179+10+46+32+77+18+6＝368，加街边 13＝381）与 376
  不符。总数不写，只写离 ENGIE 最近三个车场的逐场数字（三处来源一致）。
- **听力感应环（hearing loop）**——**C** 第 3 页只把 hearing loop 列在 The Dome 与
  Halls 2–4 名下，**ENGIE Stadium 的清单里没有这一项**。不写"ENGIE 有听力辅助"，
  也不写"没有"（官网未作否定陈述）。
- **轮椅租赁公司的名称与电话**——**C** 第 4 页给了一家外部公司与号码，但①属第三方商业
  联系方式②与 **A** 的"场馆不出租轮椅"合在一起容易被误读成场馆服务。按惯例不写。
- **无障碍订票专线号码／票务方邮箱／场馆客服电话**——官网确实给出（**A**／**B**／**C**
  三处），但沿用 055／047／054 的惯例：正文与卡片不放任何外部联系方式字符串，改写成
  "官网上列了对应的专线"。**这是排版／风控选择，不是事实问题**（第 11、26 条判 GREEN）。
- **MLAK 钥匙的申领方式／认可吊具的具体规格**——属 NSW 州级通用设施体系，场馆官网只写
  "须持 NSW 发出的 MLAK 钥匙与认可的吊具"，未涉及谁能办、怎么办、哪种吊具算认可。不写。
- **Dome Foyer 的第三处育婴室**——**B** 列为三处之一，但 Dome 是园区内另一栋建筑、
  **A** 的 ENGIE 专页明确写"两处"。本篇按 ENGIE 口径写两处，不把另一栋楼的设施算进来。
- **Olympic Park 站到场馆的具体步行分钟数**——**C** 第 2 页写 "just 2mins away"，
  **A**／`getting-here` 写 "on Sydney Showground's doorstep"，008 当年还剔除过一个
  "5 分钟"的三方说法。三个数字都出现过，口径不统一，本篇沿用 008 的处理：不给分钟数，
  且本篇角度在无障碍，连"就在门口"都不重复写。
- **安静室／Grand Parade 距球场闸口多远、走多久**——官网只给位置名与"在球场范围之外"
  这两件事，没有任何距离或时间。属账号红线里"凭印象编"的高风险区，整块不写（这也正是
  pass out 这条值得写成封面的原因：官网自己只保证"你得先拿条子"）。
- **祈祷室**——**A** 写有，但明说"位置按场次变、当天由工作人员协助"，无可执行的定位信息，
  且与本篇"无障碍／带照护对象"的主线只是相邻而非同一件事，不写。
- **寄存（cloak room）**——**A** 只写 "no cloak room facilities for sporting events"，
  演唱会情形写的是"请联系场馆"。沿用 008 的剔除：无法对演唱会下断言。
- **演唱会模式容量 46,500**——本次在 **A** 里查到了官方数字（037 当时把"场馆容量"列为
  剔除项正是因为找不到官方口径，此处予以记录：**现在有一手源了**），但与本篇角度无关，
  不写进文案，留作日后"散场／选座"类选题的素材。
- **急救点位置**——**A**／**C** 都写"体育赛事在记分牌下方，演唱会与特别活动请联系场馆"。
  演唱会情形无定位，不写。
- **无障碍席具体在哪些区／哪一排**——**C** 第 4 页只写 "Accessible Seating is available on
  concourse level of the Stadium"，没有区位或排号；第 10 条那组 aisle 号是官网给**低行动
  能力观众**的订座建议，**不是轮椅位位置**，文案两者严格分开写，不合并、不互推。
- **19 个场馆内无障碍厕所／67 个园区无障碍厕所**——**C** 第 4 页有数字，但对"要不要去、
  去哪一个"没有可执行价值（官网未给分布），属堆数字，不写。
- **任何具体演出的票价／购票平台／限购／主办方／开演时间**——不是本篇主题，且与安利篇
  重复，一律不写。
- **场馆官网 What's On 当日列出的其余在售场次**——在 `data/events.json` 中均非
  `verified=true`，按红线一律不点名、不暗示、不计数。

FACT-AUDIT-STATUS: RED=0 CHECKED=26 SOURCES-CITED=26

## 渲染状态

- 模板: `cards/064/index.html`，复制自 `cards/062/index.html`。选 062 而非 001 作为基底的
  原因：062 是同一模板链上最新的一份卡片，已带全部已验证修正（`.ledger-note` 的
  `max-width:460px` 内联约束、无 `frame-img` 外链配图的纯文字版式），而本篇同为无海报的
  纯文字选题；063 的渲染状态段记录了对 062 与 001 `<style>` 区块的逐字节比对结果为
  **完全一致**，故"保留 001 的 aushow 主题色 token 与全部已验证组件样式"这一要求自动满足。
  `<html lang="zh-CN" data-theme="aushow">`、文件顶部主题色 token、字体、
  `.ticket`／`.ledger`／`issue-strip` 组件样式、WebGL 背景脚本引用全部原样保留，
  仅替换 poster 区块内的文案与 `<title>`。
- 卡片数: **6 张** `<section class="poster xhs" id="xhs-01…06">`（062 为 4 张，本篇按上面
  "张数说明"的四个时间点各一张、加封面与 CTA，编号从 01 起连续无跳号）。
  `<main class="sheet">` 内无其它 `<section>` 元素——`automation/render_card.py` 用
  `nth-of-type` 逐张单独截图，依赖这一点。
- 输出: `cards/064/output/xhs-064-01.png` ~ `xhs-064-06.png`，预期均 1080×1440。
- 渲染: 交由 `automation/render_card.py`（headless Chrome 逐张截图 + PIL 校验 1080×1440）。
  本次会话按 daily-xhs-prompt 第 0／5 节要求，**未调用任何浏览器／截图工具**。
