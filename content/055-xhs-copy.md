# 055 — Marvel Stadium 无障碍观演攻略（场馆攻略）

**选题类型**：场馆攻略（周六轮换位，2026-10-17 生成）
**场馆选择**：Marvel Stadium（墨尔本 Docklands）——它是 `data/events.json` 中 `verified=true`
条目「周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会」的 `venue`。按本栏目"最久没被写过"的
取法，8 座 verified 场馆上次被写的时间依次为：**Marvel Stadium(027, 09-16, 31 天前)**、
Palais Theatre(030, 09-19)、Sydney Event Centre(034, 09-23)、ENGIE Stadium(037, 09-26)、
TikTok Entertainment Centre(040, 09-30)、Margaret Court Arena(043, 10-03)、
Chippo Hotel(047, 10-07)、Club Voltaire(050, 10-10)——Marvel 最久，故取它。
这是 Marvel 的**第三讲**，也是本栏目**第七次"回头换角度重讲"**。

**不锚定任何具体演出（沿用 030 的处理）**：Marvel 唯一的 verified 演出就是周杰伦墨尔本站，
而该场的演出日**正是今天 2026-10-17（19:30）**。本内容需经用户手机审核后手动发布，发布
时点可能已在开演之后——若按 004/027 的写法把"10 月 17 日周杰伦墨尔本站就在这里"写进正文
和封面，这篇会**发布即过期**。故本篇不绑定任何场次，只写场馆自身的 evergreen 无障碍信息
（030 写 Palais 时已确立此先例：提示词对场馆攻略只要求场馆"出现在 verified=true 演出里"，
未要求该演出必须是未来场次）。同理，官方 Special Events 页今天列出的其余场次
（Robbie Williams / Foo Fighters / Harry Styles / Guns 'n' Roses / BTS / Bruno Mars 等）
在 `events.json` 中**均非 `verified=true`，按红线一律不点名、不暗示**。

**角度**：「带着需要照顾的人去」——004 写"怎么到 / 怎么进"（进场前的交通与禁带清单），
027 写"散场之后这一小时"（结束时间 / 封路 / 接送点 / 打车点 / 回家换乘）。两篇读者都是
**自己一个人能走能跑的那种观众**。本篇把读者换成**推着轮椅、扶着长辈、带着怕吵的人**的
那一个，主线是**一半的事必须在到场之前就安排好**（无障碍票的买法、Companion Card 的
add-on、停车反着订、提前联系场馆）。这是本号 55 篇里**第一次以无障碍为整篇主线**——
030（Palais）曾在"怎么进 & 座位"那张卡里放过 4 行无障碍信息，但那是混合卡里的一块、
且是另一座场馆；016 只写过"无障碍停车预订改走 AXS"一行；028/035 把"无障碍订票热线"
明确列为剔除项。Marvel 这边 004/027 两篇**一个字都没碰过**无障碍。

**信源纪律**：全篇场馆事实逐条取自 marvelstadium.com.au 官网 7 个页面（无障碍专题 5 页
＋ A-Z 指南 ＋ Conditions of Entry ＋ Special Events），均为 2026-10-17 当日 curl 原文
抽取；**凡官网查不到、或官网两页口径冲突的说法一律不写**（详见事实核查表末尾"主动排除项"，
其中"中途出场再入场的扫码机制"是本次新发现的冲突项，已整块剔除）。

**红线自查**：全篇**零引用**任何单场演出的字段（不写日期/票价/购票平台/限购/主办方/
开演时间）；唯一与 `events.json` 的接点是"Marvel Stadium 是某 `verified=true` 条目的
场馆"这一事实本身。不自行添加任何 JSON 没有的演出信息；不点名任何个人/账号；
无障碍咨询邮箱**不落字面地址**（见剔除项）。

## 标题（17字）

坐轮椅、带长辈去Marvel看演出

## 正文（发帖文案，无外链）

Marvel Stadium 的无障碍服务比大多数人以为的多——但**一大半要在到场之前就安排好**，当天到现场才问就晚了。这篇不讲怎么坐车、也不讲散场怎么走，只讲一件事：带着需要照顾的人去 Marvel 看演出，哪几步必须提前走 👇

🎫 **无障碍票在官方票务的"互动座位图"里买**：官网写明，无障碍票经 Ticketmaster 的互动座位图或筛选器购买（也可能是该场次的其它官方授权售票方）。**Companion Card 的陪同人可以免费入场**，但要在买无障碍票的时候作为 add-on 一起勾上，不是到场再补。

📧 **有无障碍需求的，演出日之前先联系场馆**：官网在两个页面上反复强调同一件事——提前联系场馆的无障碍团队，他们才有时间了解你的具体情况、给出可用的支持方案。联系邮箱就在官网 Accessibility & Inclusion 页上。

🅿️ **停车是反着来的**：先在 UbiPark 订一个普通车位——官网明说**订的时候不用勾"无障碍车位"**，但车上必须出示有效的无障碍停车许可；到场直接告诉停车场工作人员你需要无障碍车位，他们会指引你过去。

🛗 **不开车的就认电梯，别认大门**：Bourke Street 和 Harbour Esplanade 两处都有外部电梯，从地面层直接上外部 concourse，落客走这两处最省力；La Trobe Street 那一侧是一段小斜坡。进了场，**Gate 4、5、6、8、9 都有电梯通到场馆内所有层**。另外提醒一句：**散场接人统一去 Harbour Esplanade**——Bourke Street 和 La Trobe Street 演出结束后会封。

♿️ **无障碍进场口在这三处**：La Trobe Street 的 Gate 6–8、Harbour Esplanade 的 Gate 8–9、Bourke Street 的 Gate 1–4 和 Gate 9。买了内场 GA 的，从票上写的那个门进去之后，无障碍通道是 **Gate 6 的电梯下到 B2**。

🦽 **轮椅这条最容易误会**：轮椅、代步车、拐杖、助行架、手杖都能带进场，但必须能安全收在座位底下、不挡通道；收不下的到 Guest Services 免费寄存。场馆也有**推轮椅把你送到座位**的服务——但官网写得很清楚，**演出期间轮椅不能一直留在你身边**；散场还需要轮椅的，可以提前让工作人员到时候来接你出场。要用这个服务，到场找客服人员，或者去 Gate 1 / Gate 5 的 Guest Services。

🤫 **怕吵、需要缓一缓**：Marvel 是经认证的感官包容场馆（和 KultureCity 合作，员工受过训练）。**Chill Hub** 在 Level 2 – Aisle 25（Danvers Room），撑不住了可以去那儿自我调节，缓好再回座位；另有两个 **Sensory Room**，在 Level 1 – Aisle 3 和 Level 3 – Aisle 31，**不用预约**（人多的时候可能同时有别人在用）。装了降噪耳机、fidget 玩具、视觉提示卡的 **sensory bag 免费借**，在各个无障碍空间和 Gate 5 Guest Services 都能领；加重膝垫和 strobe glasses 也能借。进 Sensory Room 或领东西之前要签一份免责声明，借物品还要留照片 ID 和联系电话，归还前由工作人员保管。全部免费，但弄坏了要赔。

还有几条顺手记一下：

- **两个 Guest Services 分工不一样**：Gate 1 管接待和无障碍咨询，Gate 5 管 sensory bag 租借。问对地方少跑一趟。
- **Changing Places** 无障碍卫浴在 Gate 1 Guest Services（Level 1 – Aisle 3），**全程需要 MLAK 钥匙**；没钥匙的在演出期间去 Gate 1 Guest Services 找工作人员帮忙（要有有效门票）。它的外部入口在开门前 1 小时到演出结束后 2 小时之间不开放，这段时间持票观众从场馆内部进去。
- **婴儿车**可以带进场，同样要收在座位底下；坐 Level 3 的可以把空车停在 Aisles 6、19、30、43 无障碍座位后面（有位置的话），也能在 Gate 1 / Gate 5 免费寄存。
- **协助犬**可以进场，记得带上相关文件、给它戴好识别背带。
- **12 岁以下**必须由家长或监护人全程陪同。
- **别打算中途出去透气再回来**——官网明确写了场馆不发 pass out。想缓一下，用场内的 Chill Hub 或 Sensory Room。
- 场馆支持 Hidden Disabilities Sunflower（2025 年起成为认证场馆），但**挂绳场馆不卖**，需要的要自己提前准备。
- 以上是场馆为演唱会/大型活动季列出的服务，官网也提醒**可能与场馆日常运营不同**，出发前再看一眼官网最稳。

评论区扣 1，私信发你这份 Marvel Stadium 无障碍清单，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #墨尔本 #演唱会 #MarvelStadium #墨尔本演唱会 #看演出攻略 #无障碍出行

## 卡片文案结构（5张，票根美学）

> 张数说明：提示词对场馆攻略建议精简（2–3 张内容卡）。本篇用 **5 张**（封面＋3 张内容＋CTA），
> 理由是三块内容各自饱满且读者动作完全不同：「到场之前」是**买票/订车位阶段的决定**（错过
> 就补不回来：Companion Card 的 add-on、停车许可、提前联系场馆）、「怎么进场」是**当天的
> 空间路径**（三处无障碍口 / 两处外部电梯 / 五个带电梯的门 / 内场 GA 的 B2）、「场内这些事」
> 是**进去之后的规则与资源**（轮椅不能留身边 / Chill Hub / Sensory Room / sensory bag）。
> 压成两张会让任一张的 ledger 挤到 6 行以上不可读。封面与 CTA 是账号固定品牌结构。
> 无空卡、无凑数卡；剩余细节（Changing Places / 婴儿车 / 协助犬 / pass out / 12 岁以下）
> 压进 P4 ledger 后的 `body` 段落，沿用 020 的处理。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 场馆攻略 · Marvel Stadium
- 大字标题: 坐轮椅、带长辈 / 去 Marvel
- 副标题: 一半的事 · 得提前安排
- 说明: 无障碍票怎么买 / 停车怎么订 / 电梯在哪 / 怕吵了去哪缓一缓。全部取自场馆官网。
- 底部条: 墨尔本 Docklands — 演唱会与大型活动季
- 配图: 无（场馆攻略不挂任何演出海报，避免"海报张冠李戴"复发）

**P2 到场之前（ledger 4条）**
1. 票在互动图里买 — 官网：无障碍票经 Ticketmaster 的互动座位图或筛选器购买，或该场次的其它官方授权售票方
2. 陪同人免费入场 — Companion Card 的陪同人免费入场，但须在买无障碍票时作为 add-on 一起勾选
3. 先联系场馆 — 官网建议有无障碍需求的观众在演出日之前联系场馆无障碍团队，他们才有时间安排支持方案
4. 停车反着订 — 先在 UbiPark 订普通车位，订时不必勾无障碍；车上须出示有效无障碍许可，到场告知停车场工作人员
- 底部条: 来源 marvelstadium.com.au — 当天现场才问就晚了

**P3 怎么进场（ledger 4条）**
1. 无障碍口三处 — La Trobe St 的 Gate 6–8、Harbour Esplanade 的 Gate 8–9、Bourke St 的 Gate 1–4 与 Gate 9
2. 落客认电梯 — Bourke St 与 Harbour Esplanade 都有外部电梯从地面层上 concourse；La Trobe St 那侧是小斜坡
3. 场内五个门有电梯 — Gate 4、5、6、8、9 都有电梯通到场馆内所有层
4. 内场 GA 走 B2 — 从票上写的那个门入场后，无障碍通道是 Gate 6 的电梯下到 B2
- 底部条: 散场接人走 Harbour Esplanade — Bourke St 与 La Trobe St 散场后封

**P4 场内这些事（ledger 4条）**
1. 轮椅能带进场 — 轮椅、代步车、拐杖、助行架、手杖都可带入，须安全收在座位底下、不挡通道
2. 放不下就寄存 — 收不进座位底下的，Gate 1 与 Gate 5 的 Guest Services 免费寄存
3. 轮椅不能留身边 — 有人推你到座位的服务，但官网写明演出期间轮椅不能一直留在你身边；散场要用可提前让工作人员来接
4. 怕吵有地方缓 — Chill Hub 在 Level 2–Aisle 25；两个 Sensory Room 在 Level 1–Aisle 3、Level 3–Aisle 31，不用预约
- 收尾段落: Changing Places 无障碍卫浴在 Gate 1 Guest Services（Level 1 – Aisle 3），全程需 MLAK 钥匙；没钥匙的演出期间去 Gate 1 求助（要有有效门票）。sensory bag 免费借，在各无障碍空间和 Gate 5 Guest Services，要签免责声明、留照片 ID 和电话。婴儿车可带入但要收在座位下，Level 3 可把空车停在 Aisles 6、19、30、43 无障碍座位后面（有位置的话）。协助犬可入场，带好文件、戴识别背带。场馆不发 pass out，别打算出去再回来。12 岁以下须家长或监护人全程陪同。
- 底部条: Gate 1 管无障碍咨询 — Gate 5 管 sensory bag 租借

**P5 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 带得进去 / 才叫看得上
- 正文: 评论区扣 1，私信发你这份 Marvel Stadium 无障碍清单，还有后续开票提醒。
- 底部条: VOL. 055 — 简介里有完整演出日历

## 事实核查表

信源编号（全部为 2026-10-17 当日抓取）：
- **S1** = `~/Projects/AuShow-Radar/data/events.json`
- **A** = https://www.marvelstadium.com.au/accessibility-information-major-events-concerts
- **B** = https://www.marvelstadium.com.au/event-day-assistance-and-ticketing
- **C** = https://www.marvelstadium.com.au/sensory-room-accessibility
- **D** = https://www.marvelstadium.com.au/changing-places
- **E** = https://www.marvelstadium.com.au/a-z-guide-to-marvel-stadium/
- **F** = https://www.marvelstadium.com.au/conditions-of-entry
- **G** = https://www.marvelstadium.com.au/hidden-disabilities-sunflower
- **H** = https://www.marvelstadium.com.au/local-community-information-special-events

| # | 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|---|
| 1 | Marvel Stadium 是 `verified=true` 条目的场馆 | GREEN | **S1** 条目「周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会」：`venue=Marvel Stadium`、`city=墨尔本`、`verified=true` | 全篇**只用到"该场馆出现在 verified 条目里"这一点**，正文/卡片一个演出字段都不引（含日期），理由见文件头"不锚定任何具体演出" |
| 2 | 无障碍票经 Ticketmaster 的互动座位图或筛选器购买，或该场次的其它官方授权售票方 | GREEN | **B** 原文 "Accessible tickets are purchased via Ticketmaster using the interactive map or filters (or another authorised ticketing agent for that event)." | 括号里的限定句（可能是别的官方授权售票方）**照搬保留**，未简化成"只能在 Ticketmaster 买"——那会变成官网没说的排他断言 |
| 3 | Companion Card 的陪同人免费入场；须在购买无障碍票时作为 add-on 一并选取 | GREEN | **B** 原文 "Companion cards entitles a companion to free entry to the venue and are available at the time of purchase via Ticketmaster when purchasing accessible tickets as an 'add-on'." | 未写 Companion Card 的申领条件/资格（属州政府计划，官网该页未涉及，见剔除项） |
| 4 | 官网建议有无障碍需求者在演出日之前联系场馆无障碍团队，以便提前了解需求、讨论可用支持 | GREEN | **A** 与 **B** 同句原文 "we encourage anyone with accessibility enquiries relating to a Major Events & Concerts to contact … prior to event day. Getting in touch in advance gives our team the best opportunity to understand your needs and discuss available support options." | 两页同一表述，正文写"官网在两个页面上反复强调同一件事"即据此 |
| 5 | 无障碍咨询的联系邮箱列在官网无障碍页上 | GREEN | **A** 页正文给出 `accessibility@…` 形式的邮箱并在页尾重复一次；**A** 同页链向 "Accessibility & Inclusion Information Hub" | 文案**只写"邮箱在官网 Accessibility & Inclusion 页上"，不落字面地址**（见剔除项） |
| 6 | 无障碍车位先经 UbiPark 订车位，下单时不必指明需要无障碍车位 | GREEN | **C** 原文 "To use an accessible parking space, first book parking through UbiPark HERE. Patrons do not need to request an accessible space when booking"；**E** 互证 "patrons do not have to indicate via Ubi Park if they need an accessible car-park" | 两页口径一致 |
| 7 | 停用无障碍车位须出示有效的无障碍停车许可 | GREEN | **C** 原文 "a valid accessible parking permit must be displayed to park in these spaces"；**E** 作 "will require a disabled sticker to park in these spaces" | 两页措辞不同、所指同一件事；文案采用 **C** 的正式表述"有效的无障碍停车许可" |
| 8 | 到场须告知停车场工作人员需要无障碍车位，由其指引空位 | GREEN | **C** 原文 "On event day, please advise a car park attendant that you require an accessible parking space. They will help direct you to an available spot."；**A** 与 **E** 互证 | — |
| 9 | 可在 Bourke Street 或 Harbour Esplanade 落客，两处有外部电梯从地面层到 concourse | GREEN | **C** 原文 "patrons with accessible needs can be dropped off at Bourke Street or Harbour Esplanade, where external lifts provide access from ground level to the concourse" ＋同页 "Public lift access is available from Harbour Esplanade and Bourke Street from Ground Level to External Concourse."；**E** 互证 | 027 写过 Harbour Esplanade 是官方接送点，但**"这两处有外部电梯"从未写过**，是本行的新内容 |
| 10 | La Trobe Street 一侧有从街面到外部 concourse 的小斜坡 | GREEN | **C** 原文 "A small ramp from street-level to the external concourse is located from La Trobe Street." | — |
| 11 | Gates 4、5、6、8、9 均有电梯通往场馆内所有层 | GREEN | **C** 原文 "Gates 4, 5, 6, 8 & 9 all have lift access to all levels within the stadium." | 逐字照抄门号，未自行增补其它门 |
| 12 | 无障碍进入外部 concourse 的通道为：La Trobe Street（Gates 6–8）、Harbour Esplanade（Gates 8–9）、Bourke Street（Gates 1–4 及 9） | GREEN | **A** 原文 "Accessible access to the external concourse is available via La Trobe Street (Gates 6-8), Harbour Esplanade (Gates 8-9) & Bourke Street (Gates 1-4 & 9)."；**E** 逐字互证 | 门号区间逐字照抄 |
| 13 | 内场 GA 的无障碍通道：从票上注明的门入场后，走 Gate 6 的电梯到 B2 | GREEN | **A** 与 **B** 同句原文 "Once entering the venue via the gate noted on your ticket, Accessible GA Arena access is available via Gate 6 lifts to B2." | 保留"从票上写的那个门入场"这个前置条件，未写成"直接去 Gate 6" |
| 14 | 散场后 Bourke Street 与 La Trobe Street 关闭，Harbour Esplanade 是官方指定接送点 | GREEN | **H** 原文 "Bourke Street (managed throughout the event and closed post event), Harbour Esplanade (dedicated drop of and pick up location) and La Trobe Street (closed post event)"（"drop of" 系官网拼写） | ⚠️ **有意重叠**：这三条 027 已写过。本篇仅作**一句收口**放在 P3 底部条，不单独成行、不展开——因为对推轮椅的读者来说，新信息是第 9 条"哪个落客点有电梯"与这一条"哪个落客点散场后还在"的**组合**（去程两处都行、回程只剩 Harbour Esplanade）。已在卡片结构里标注 |
| 15 | 轮椅、代步车、拐杖、助行架、手杖可带入场馆，但须安全收于座位下、不阻挡通道 | GREEN | **A**/**B**/**C**/**E** 四页同句 "Mobility Aids such as wheelchairs, mobility scooters, crutches, walking frames, and walking canes are permitted inside the Stadium, but they must be stowed safely under your seat to avoid blocking access paths." | 器械清单逐字照抄；004 写过"包不超过 A3"，与本行**不是同一件事**（包 vs 助行器），未混用 |
| 16 | 助行器收不进座位下时，可在 Gate 1 与 Gate 5 的 Guest Services 免费寄存 | GREEN | **A**/**B**/**C**/**E** 同句 "If a Mobility Aid does not fit under a seat, cloaking services are free of charge and available at Guest Services, located Gate 1 (Aisle 3) and Gate 5 (Aisle 36)." | ⚠️ 004 已写过"寄存免费，在 Gate 1 与 Gate 5 的 Guest Services"。本行新的是**适用对象**（助行器也走寄存）。**本篇一律不写 Aisle 号**：一是 004 已写过，二是 **B** 页同页内把 Gate 5 写成 "Aisle 37" 而 **A**/**C**/**E** 三页均写 "Aisle 36"，存在口径冲突（见剔除项） |
| 17 | 轮椅接送/陪同服务可把观众送到座位并接出，但演出期间轮椅不能一直留在观众身边 | GREEN | **B** 与 **C** 同句 "Wheelchair services / escorts are available to take patrons to and from their seat, but please note that wheelchairs cannot remain with patrons during an event." | 这是本篇最可能被误会的一条，正文与 P4 大字都用了官网的转折语气，未写成"场馆提供全程轮椅" |
| 18 | 散场仍需轮椅的，可安排工作人员前来协助离场 | GREEN | **B** 与 **C** 同句 "If a wheelchair is needed post event, patrons can organise for a staff member to meet them to assist with exiting the Stadium." | 文案写"可以提前让工作人员到时候来接"，对应 organise（需安排），未写成"散场自动有人来" |
| 19 | 需要陪同或轮椅服务，可现场找客服人员，或前往 Gate 1 / Gate 5 的 Guest Services | GREEN | **B** 与 **C** 同句 "patrons are to ask a customer service team member upon arrival at the Stadium, or are to visit Guest Services located inside Gates 1 … and 5 …" | 同第 16 条，不写 Aisle 号 |
| 20 | 两个 Guest Services 分工不同：Gate 1 管接待与无障碍咨询，Gate 5 管 sensory bag 租借等 | GREEN | **E** 原文 "Gate 1 Guest Services (Aisle 3): Reception and accessibility enquiries." / "Gate 5 Guest Services (Aisle 36): Sensory bag hire, club membership assistance (subject to event availability), and VIP enquiries for special events." | 文案只取与本篇相关的两项分工，未复述会员/VIP 事项 |
| 21 | Marvel Stadium 是经认证的感官包容场馆，与 KultureCity 合作、员工受过相关训练 | GREEN | **A** 原文 "Marvel Stadium is proud to be an official accredited sensory inclusive venue"；**C** 原文 "Stadium staff have undergone Sensory Inclusive Training 101 with KultureCity, and Marvel Stadium is officially an accredited Sensory venue." | 未复述 KultureCity 的奖项/其它场馆数量（营销性内容，与读者动作无关） |
| 22 | Chill Hub（感官友好空间）位于 Danvers Room，Level 2 – Aisle 25 | GREEN | **A** 原文 "Chill Hub: A sensory-friendly space available for all patrons to utilise when requiring self-regulation before re-joining the event from their seats. Located at Danvers Room, Level 2 - Aisle 25." | 该设施**只在 A 页（大型活动与演唱会季专页）出现**，与本篇场景一致 |
| 23 | 两个 Sensory Room 位于 Level 1 – Aisle 3 与 Level 3 – Aisle 31 | GREEN | **A** 原文 "Sensory Rooms: Located at Level 1 - Aisle 3 & Level 3 - Aisle 31."；**C** 与 **E** 逐字互证 | 三页一致，故此处保留 Aisle 号（与第 16 条的冲突项不同） |
| 24 | Sensory Room 无须预约；高峰时段可能多人同时使用 | GREEN | **C** 原文 "Do I need a reservation before using the Sensory Room? No reservation is required. However, please be aware that at busy times there may be multiple users of the space." | 两句都写进正文，未只写"不用预约"这半句 |
| 25 | sensory bag 免费租借，可在所有无障碍空间与 Gate 5 Guest Services 领取，借用期为活动期间 | GREEN | **A** 原文 "Complimentary sensory bags are available for hire from all Accessibility Spaces and Gate 5 Guest Services (Level 1, Aisle 36)."；**C**/**E** 互证 "for the event duration" | — |
| 26 | 加重膝垫（weighted lap pads）与 strobe glasses 亦可租借 | GREEN | **C** 原文 "Weighted lap pads and strobe glasses are also available for patrons to hire in addition or separately to sensory bags." | — |
| 27 | 进入 Sensory Room 或领取 sensory bag / 加重膝垫前须签署免责声明；租借物品另须留存照片 ID 与联系电话，由工作人员保管至归还 | GREEN | **C** 原文 "Patrons will be required to sign a waiver prior to entering the Sensory Room or receiving a sensory bag/weighted lap pad. A photo ID and contact number is also required to be kept by staff when hiring a sensory bag or item until it has been returned." | 两项要求的**适用范围不同**（签声明=进房或领物；留 ID=借物），文案分开表述未合并 |
| 28 | 感官包容资源全部免费，但损坏需由观众赔偿 | GREEN | **C** 原文 "No - all resources are free of any charge for hire and use. However, any damage to sensory items will require reimbursement from the guest." | — |
| 29 | 场馆不发 pass out（中途外出凭证） | GREEN | **F** 原文 "Pass outs will not be issued to patrons…"；**E** 原文 "Please be advised that pass outs are not issued at Marvel Stadium." | 两页在"不发 pass out"这一点上**一致**，故本篇只写这一点；**两页对"之后能不能再进场"的机制互相冲突，整块剔除**（见剔除项） |
| 30 | 婴儿车可带入场馆，须收于座位下 | GREEN | **C** 原文 "Prams and strollers are permitted into the venue, provided they are stowed under your seat."；**E** 逐字互证 | — |
| 31 | Level 3 的观众可将空婴儿车停在 Aisles 6、19、30、43 无障碍座位后方（如有空间） | GREEN | **C** 原文 "Patrons with prams or strollers on Level 3 may park their empty pram or stroller behind the accessible seating at Aisles 6, 19, 30 & 43, if space permits."；**E** 逐字互证 | "empty"（空车）与 "if space permits"（有位置的话）两个限定都保留 |
| 32 | 婴儿车可在 Gate 1 / Gate 5 的 Guest Services 免费寄存 | GREEN | **C** 原文 "Prams and strollers may be cloaked free-of-charge at Guest Services"；**E** 逐字互证 | 同第 16 条，不写 Aisle 号 |
| 33 | 协助犬可入场，须携带相关文件并佩戴识别背带 | GREEN | **C** 原文 "Assistance dogs are permitted entry into the venue. Please ensure you bring any documentation with you, and that all assistance animals wear an identifying harness."；**E** 逐字互证；**F** 禁带清单作 "animals (other than guide/assistance dogs)" 反向互证 | 三页互证 |
| 34 | Changing Places 无障碍卫浴位于 Gate 1 Guest Services，Level 1 – Aisle 3 | GREEN | **D** 原文 "It is located at Gate 1 Guest Services, Level 1 - Aisle 3 and is accessible 24/7."；**E** 逐字互证 | 此处保留 Aisle 号（两页一致，且是定位该设施的唯一信息） |
| 35 | Changing Places 全时段需 MLAK 钥匙；演出期间无钥匙者可到 Gate 1 Guest Services 求助，并需持有效门票 | GREEN | **D** 原文 "Access to this facility requires an MLAK key at all times." ＋ "If you require assistance accessing this facility during an event, please speak with our team at Gate 1 Guest Services. A valid event ticket is required."；**E** 逐字互证 | "需有效门票"这个条件保留，未写成"直接去就行" |
| 36 | Changing Places 的外部入口自开门前 1 小时起至演出结束后 2 小时止不开放，该时段内持票观众由场馆内部进入 | GREEN | **D** 原文 "the external entrance to the Changing Places facility is unavailable from one hour prior to gate opening until two hours after the event concludes. During this period, access is available via the stadium interior for ticketed patrons." | 本条用的是**相对时间**（开门前 1 小时 / 结束后 2 小时），不含任何具体钟点，故不触碰"开门/开演时间"这个 004/027 一直剔除的禁区 |
| 37 | 12 岁以下观众须由家长或监护人全程陪同 | GREEN | **F** 原文 "Patrons under the age of 12 years must be accompanied by a parent or guardian at all times within the Stadium." | 这是 Conditions of Entry 里的硬条款，非场次规则 |
| 38 | Marvel Stadium 于 2025 年成为 Hidden Disabilities Sunflower 认证场馆；场馆支持该计划但不出售 Sunflower 挂绳 | GREEN | **G** 原文 "The Hidden Disabilities Sunflower was established in 2016, with Marvel Stadium officially becoming a Sunflower-accredited venue in 2025." ＋ "Sunflower lanyards are not available for purchase at the Stadium."；**A** 页重复后半句 | 只写了对读者有动作意义的那半句（挂绳得自己提前准备），未介绍该计划的历史 |
| 39 | 以上服务针对 Major Event & Concert 季列出，官网提醒可能与场馆日常运营不同 | GREEN | **A** 原文 "Please note: The below information relates specifically to services and facilities available Major Event & Concert season which may differ to the Stadium's regular operations." | 这句**官网自带的限定**写进了正文末尾，不让读者把本篇当作全场景通用口径 |

**主动排除项（查不到官方依据、或官网两页冲突，本篇一律不写）**：

- 🔴 **"中途可以扫码出场、再回原门重扫进来"的再入场机制**——**E**（A-Z 指南）写 "Should
  patrons wish to leave the venue, it is a requirement to scan out using the ticket used for
  entry. Upon re-entry, patrons are required to re-scan in at the gate listed on the ticket."，
  描述的是一套**常规可用**的出入流程；而 **F**（Conditions of Entry）写 "Pass outs will not
  be issued to patrons, **except in exceptional circumstances at the sole discretion of MSL**"，
  即再入场属**例外、由场馆单方裁量**。两页对"普通观众中途出去还能不能回来"口径冲突，
  按红线"不自行添加入场规则"整块剔除，只保留两页一致的"不发 pass out"，并把读者引向场内的
  Chill Hub / Sensory Room。（004 当时也剔除过这一项，今天复核后**冲突依然存在**，非笔误。）
- 🔴 **Gate 5 Guest Services 的 Aisle 号**——**B** 页同一页内先写 "Gates 1 (Level 1, Aisle 3)
  and 5 (Level 1, Aisle 37)"、后写 "Gate 1 (Aisle 3) and Gate 5 (Aisle 36)"，自相矛盾；
  **A**/**C**/**E** 三页均作 Aisle 36。虽然 36 占多数（且 004 当时写的也是 36），但既然官方
  页内自相矛盾，本篇**索性不写任何 Guest Services 的 Aisle 号**，只写 Gate 1 / Gate 5
  （Changing Places 的 Level 1 – Aisle 3 例外：**D**/**E** 两页一致且是定位该设施的唯一信息）。
- **无障碍咨询邮箱的字面地址**——官网确实给出该邮箱，但按本号惯例，正文/卡片不放任何
  外部联系方式字符串（沿用 047 剔除"售票页微信联系方式"、054 同款处理），改写成"邮箱在官网
  Accessibility & Inclusion 页上"。这是**排版/风控选择，不是事实问题**（第 5 条判定为 GREEN）。
- **Companion Card 的申领资格与办理方式**——属澳洲各州/领地政府的计划，Marvel 官网该页
  只说"持卡陪同人免费入场、买票时当 add-on 选"，未涉及谁能办、怎么办。不写。
- **无障碍座位具体在哪些区/排**——官网无任何座位区位说明（演唱会舞台布局还按场次变），
  属 004 已定性为"凭印象编"的高风险区，整块不写。030 能写 Palais 的 AA/WW/D 排是因为
  Palais 官网逐排列明了，Marvel 没有对应页面。
- **无障碍厕所的具体 Aisle 位置**——**E** 页该段落文字与相邻条目（Baby Change / Parent
  Rooms）在抓取后的纯文本里无法可靠切分，归属存疑，不写。
- **开门/检票/开演时间**——沿用 004/027/045/048 口径：官网 A-Z 明示 "See event pages for
  specific opening times"，因场次而异；**H** 页虽列出各场次 Gates Time，但那是**具体场次信息**，
  而本篇刻意不锚定任何场次，故一律不引。
- **停车费、车位数量、限高、车场入口字母**——004/027 已写过且本篇不是交通篇，不重复。
- **官方 Special Events 页今天列出的其余演出场次**（Robbie Williams / Foo Fighters /
  Harry Styles / Guns 'n' Roses / RMIT 毕业礼 / Faith No More・System Of A Down / BTS /
  Bruno Mars / 2027 橄榄球世界杯）——这些在 `data/events.json` 中**均非 `verified=true`**，
  按账号红线"未核实的不发"，一个都不点名、也不写"本季还有很多场"这类暗示。
- **Telstra Touch and Track**——官网标明为 AFL 赛季服务，与演唱会场景不符，不写。
- **可开合屋顶 / 场馆容量**——004 写过屋顶；容量在 053 已定性为各来源打架的剔除项。

FACT-AUDIT-STATUS: RED=0 CHECKED=39 SOURCES-CITED=39

## 渲染状态

- 模板: `cards/055/index.html`，复制自 `cards/020/index.html`。选 020 而非 001 作为基底的
  原因：① 本次会话已 `diff` 确认 `cards/020/index.html` 从第 1 行到 `<body>` 之前与
  `cards/001/index.html` **逐字相同，唯一差异是 `<title>`**，故等价于按提示词要求复制自 001；
  ② 020 同为**5 张卡、无配图的场馆攻略**，poster 骨架（封面 ledger×3 CTA）与本篇完全对应，
  且已带 `.ledger-note` 的 `max-width:460px` 内联约束与"ledger 后接 `body` 长段落"这两处
  已验证过的版式处理。`<html data-theme="aushow">`、主题色 token、字体、`.ticket`/`.ledger`/
  `issue-strip` 组件样式全部原样保留，仅替换 5 个 poster 区块内的文案。
- 卡片数: 5 张 `<section class="poster xhs" id="xhs-01…05">`，无配图（`frame-img` 外链一律不加）
- 版式预防: `.ledger-title` 控制在 7 字以内；`.ledger-note` 全部沿用 `max-width:460px`；
  P4 ledger 后的 `body` 长段落沿用 020 的 `style="margin-top:8px;"` 处理
- 渲染方式: 本次会话按 `daily-xhs-prompt.md` 第 0 节**未调用任何浏览器/截图工具**，
  渲染交由 `automation/render_card.py`（headless Chrome 逐张单独截图 + PIL 校验 1080×1440），
  由 `run_daily_xhs.sh` 在本任务结束后执行
