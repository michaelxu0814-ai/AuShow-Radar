# 058 — Palais Theatre 进场规则攻略（场馆攻略）

**选题类型**：场馆攻略（周三轮换位，2026-10-21 生成）
**场馆选择**：Palais Theatre（墨尔本 St Kilda）——它是 `data/events.json` 中 `verified=true`
条目「袁娅维 TIA RAY「月亮撒野」世界巡演 墨尔本站」的 `venue`。按本栏目 055 明确写下的
"最久没被写过"取法，8 座 verified 场馆上次被写的时间依次为：**Palais Theatre(030, 09-19,
32 天前)**、Sydney Event Centre(034, 09-23)、ENGIE Stadium(037, 09-26)、
TikTok Entertainment Centre(040, 09-30)、Margaret Court Arena(043, 10-03)、
Chippo Hotel(047, 10-07)、Club Voltaire(050, 10-10)、Marvel Stadium(055, 10-17)——
**Palais 最久，故取它**。这是 Palais 的**第二讲**，也是本栏目**第八次"回头换角度重讲"**。

**角度（与 030 零重叠）**：030 写的是「**怎么到、怎么进**」——电车/火车/巴士/停车四条交通
线，加一张无障碍与座位结构卡，读者动作全部发生在**到场馆门口之前**。本篇把镜头推到
**门口那一关之后**：包多大能带、什么东西会被拦下、票怎么取、钱怎么付、坐下之后能不能站
起来跳。这是本号 57 篇前作里**第一次以"进场规则/场内规矩"为整篇主线**的场馆攻略——
004（Marvel）曾在一张卡里放过禁带清单，但那是混合卡里的一块、且是另一座场馆；030 整篇
一个字都没碰过包尺寸、取票、无现金、站立规则。

**信源纪律**：本篇所有场馆事实逐条取自 `palaistheatre.com.au` 官网**两个页面**——
`/faqs`（Conditions of Entry、Prohibited Items、取票、Box Office、座位与站立、酒水licensing、
寄存、儿童、失物、周边等全部 FAQ 条目）与 `/food-and-drink`，均为 **2026-10-21 当日
`curl` 原文抽取**（`/faqs` 页 500KB HTML 已本地剥标签取正文，非搜索摘要）。
**凡官网查不到、或官网两处口径冲突的说法一律不写或只写可直接引证的那一侧**
（详见事实核查表末尾"主动排除项"——其中"背包是否一律禁带"与"水瓶规则"两处是本次发现的
官网内部口径差异，均已按保守侧处理）。

**红线自查**：全篇**零引用**任何单场演出的字段（不写任何演出名/日期/票价/开演时间/主办方/
限购）。该场馆在 verified 池里唯一的演出（袁娅维墨尔本站 2026-08-20）**已过期**，而
`data/events.json` 里出现在 Palais 的其余条目均为 `verified=false`，按红线"未核实的不发"
一律不点名、不暗示。唯一与 `events.json` 的接点是"Palais Theatre 是某 `verified=true`
条目的场馆"这一事实本身（沿用 030/034/055 已确立的 evergreen 处理）。全篇不点名任何
个人/账号/卖家/转售平台；第 18 条提到 Ticketmaster 仅为照抄场馆官网"唯一授权售票方"
这一自述事实，不作推荐、不绑定任何场次。封面不挂任何演出海报。

## 标题（17字）

Palais看演出，包别超30公分

## 正文（发帖文案，无外链）

上次写 Palais 讲的是怎么到（电车、火车、停车那个坑）。这次讲**门口那一关**——在这座 1927 年的老剧院被拦下来的，多半不是票有问题，是包和带的东西 👇

📦 **包别超 30cm×30cm**：背包、冰箱袋（Eskies）、任何大于 30cm×30cm 的包都在官方禁带清单上。进门还可能被开包检查。

🧳 **没有寄存处**：场馆没有 cloakroom，官方直接建议别带比 A4 还大的东西，点名了摩托头盔和大伞。易腐食物也没地方存，只能留在车里或别的安全地方。

💧 **水瓶有两种带法**：自己带的可重复用塑料瓶，必须是**空的**且容量 **600mL 以下**；或者带**一瓶未开封**的瓶装水/软饮（每人一瓶）。开过的进门前要倒空。进去之后楼上楼下 foyer 都有免费接水点。

🍔 **热食和外带快餐别带**：禁带清单里有"热食/餐食"，也有"商业食品（快餐店或全服务餐厅买的食物）"。

📷 **相机只能带小的**：DSLR、摄像机、录音设备、三脚架、自拍杆全不行；手机和小型手持相机可以，但**禁止闪光灯**。

带小孩的额外注意：**婴儿车不能进场、场馆也没地方寄存**，得留在车里；2 岁以上要买票，2 岁以下坐大人腿上不占座可以不用票；18 个月以下的宝宝去成人演出，**戴耳罩是入场条件**（自己带）；场馆建议 14 岁以下由成年人陪同。

票和钱这边还有三件事容易踩：

💳 **全场不收现金**。完全无现金场馆，Box Office、吧台、周边柜台都只能刷卡或手机支付。

🎫 **预付票只有本人能取**。只有信用卡持卡人本人可以取票，要带购票那张卡 **＋ 带照片的身份证件**。Box Office 只在演出夜开门，比票面/官网写的 doors open 时间**早 30 分钟**；非演出日取票得去 Ticketmaster 门店。

🪑 **坐下之后能不能站，看多数人**。全场有座、按票上的区域和座位坐（Orchestra / Stalls / Lounge / Dress Circle）。**Lounge A–D 排不许站也不许跳**，这是票面写明的安全规定；其他区域按"多数人规则"——多数人坐着就请坐着，多数人站起来了就可以站。通道要全程留空。迟到的只能等演出合适的间隙才放进去。应援牌可以带，但不能大于 **A2**、要软卡纸、能折起来收到座位底下（横幅旗子标语大于 A3 的一律不能带）。

还有一条跟买票有关、值得记一下：**场馆官网自己写明，Ticketmaster 是 Palais 演出的唯一授权售票方**，并提醒从非授权渠道买的票，场馆和 Ticketmaster **都无法替你验证真伪**。官方渠道的票价和出票方式，永远是唯一的标准。

小贴士：场内有六个吧台，还供应热的小食；吧台开到中场休息，或演出结束前 30 分钟为止。周边柜台在地面层，热门场次会再开第二个。全场禁烟，含电子烟和 vape。场馆不发 pass out（除经场馆管理方批准），别打算中途出去再回来。进酒水区要出示政府签发的带照片身份证件。东西丢了场馆会留 4 周。

评论区扣 1，私信发你这份 Palais Theatre 进场清单，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #墨尔本 #看演出 #StKilda #PalaisTheatre #墨尔本演出 #演唱会攻略

## 卡片文案结构（5张，票根美学）

> 张数说明：沿用 055/056/057 已验证的 5 张结构（封面 + 3 张内容 + CTA）。本篇的三张内容卡
> 对应**三个互不重叠、各自饱满**的主题：「带什么进去」（4 条禁带/寄存/水瓶/食物）、
> 「票和钱」（4 条无现金/取票/Box Office/授权售票方）、「场内规矩」（4 条对号入座/站立
> 规则/迟到/相机与应援牌）。压成 2 张会让任一 ledger 挤到 8 行不可读；封面与 CTA 是账号
> 档案里写死的品牌结构（P5 固定 kicker 作品牌锚）。无空卡、无凑数卡。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 场馆攻略 · Palais Theatre
- 大字标题: Palais 进场 / 包别超 30 公分
- 副标题: 没有寄存处 · 全场不收现金
- 说明: 在这座 1927 年的老剧院被门口拦下来的，多半不是票的问题，是包和带的东西。全部取自场馆官网。
- 底部条: 墨尔本 St Kilda — 1927 年的老剧院
- 配图: 无（场馆攻略不挂任何演出海报，避免"海报张冠李戴"复发）

**P2 带什么进去（ledger 4条 + body）**
- kicker: 带什么进去
- 大字: 包超过 30 公分 / 门口就被拦
1. 包别超 30×30 — 背包、冰箱袋（Eskies）、任何大于 30cm×30cm 的包都在官方禁带清单上；进门还可能被开包检查
2. 没有寄存处 — 场馆没有 cloakroom，官方建议别带比 A4 大的东西（点名摩托头盔、大伞）；易腐食物也不能存，留车里
3. 水瓶两种带法 — 自带可重复用塑料瓶须空的且 600mL 以下；或每人一瓶未开封的水/软饮；开过的进门前倒空；场内楼上楼下 foyer 有免费接水点
4. 热食快餐别带 — 禁带清单含"热食/餐食"，也含"商业食品（快餐店或全服务餐厅买的食物）"
- body: 带小孩的额外注意：婴儿车不能进场、场馆也没地方寄存，得留在车里或别的安全地方；2 岁以上要买票，2 岁以下坐大人腿上不占座可以不用票；18 个月以下的宝宝参加成人演出，戴耳罩是入场条件（建议自己带）；场馆建议 14 岁以下由负责的成年人陪同。
- 底部条: 来源 palaistheatre.com.au — 出门前先把包换小的

**P3 票和钱（ledger 4条）**
- kicker: 票和钱
- 大字: 全场不收现金 / 取票只认本人
1. 全场不收现金 — 完全无现金场馆；Box Office、餐饮、周边柜台都只收刷卡或手机支付
2. 取票只认本人 — 预付票只有信用卡持卡人本人能取，须出示购票那张卡 ＋ 带照片的身份证件
3. Box Office 早 30 分钟 — 只在演出夜开门，比官网写的 doors open 时间早 30 分钟；非演出日取票去 Ticketmaster 门店
4. 只有一个授权售票方 — 场馆官网写明 Ticketmaster 是其演出唯一授权售票方，并提醒非授权渠道买的票，场馆与 Ticketmaster 都无法验证真伪
- 底部条: 官方渠道的票价与出票方式 — 永远是唯一标准

**P4 场内规矩（ledger 4条 + body）**
- kicker: 场内规矩
- 大字: 能不能站起来 / 看多数人
1. 对号入座 — 全场有座，按票上写的区域和座位坐（Orchestra / Stalls / Lounge / Dress Circle）；个别 General Admission 场次先到先坐
2. Lounge A–D 禁站 — 这四排不许站也不许跳，票面写明、安全原因；通道须全程保持畅通
3. 其他区看多数 — 官方"多数人规则"：多数人坐着就请坐着，多数人站起来跳则放行，由工作人员视情况把控
4. 迟到与应援牌 — 迟到只能在演出合适的间隙入场；应援牌不得大于 A2、须软卡纸且能折起来收座位下，挡到他人视线会被要求放下
- body: 场内有六个吧台，另供应热的小食；吧台开到中场休息，或演出结束前 30 分钟为止。周边柜台在地面层，繁忙场次会再开一个。全场禁烟，含电子烟与 vaping。场馆不发 pass out（除经场馆管理方批准），别打算中途出去再回来。进持照酒水区须出示政府签发的带照片身份证件。失物场馆会留存最多四周。
- 底部条: 禁止闪光灯 — 手机和小型手持相机可以带

**P5 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 带得进去 / 才叫看得上
- 正文: 评论区扣 1，私信发你这份 Palais Theatre 进场清单，还有后续开票提醒。
- 底部条: VOL. 058 — 简介里有完整演出日历

## 事实核查表

> 下表 `/faqs` 指 https://www.palaistheatre.com.au/faqs ，`/food-and-drink` 指
> https://www.palaistheatre.com.au/food-and-drink ，均为 2026-10-21 当日 `curl`
> （浏览器 UA）取得 HTML 后本地剥标签抽出的页面正文原文，非搜索摘要。

| # | 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|---|
| 1 | Palais Theatre 位于墨尔本 St Kilda（Lower Esplanade 与 Cavell Street 路口） | GREEN | https://www.palaistheatre.com.au/getting-here（030 已逐字核实："Palais Theatre is located next to Luna Park, on Lower Esplanade and Cavell Street, St Kilda VIC 3182"） | 沿用 030 的处理：官方页未给门牌号，故不写门牌号 |
| 2 | 场馆于 1927 年建成 | GREEN | https://en.wikipedia.org/wiki/Palais_Theatre（"officially opened by the Mayor of St Kilda on 12 November 1927"），030 已核实并交叉维州文化遗产名录条目 https://vhd.heritagecouncil.vic.gov.au/places/1115 | 只写"1927 年"，不写开幕日、不写建筑风格 |
| 3 | 背包、冰箱袋（Eskies）、任何大于 30cm×30cm 的包禁止带入 | GREEN | `/faqs` Prohibited Items 逐字："Eskies, backpacks or any bag larger than 30cm x 30cm." | 文案写 30cm×30cm，与原文同 |
| 4 | 入场时可能被要求开包检查 | GREEN | `/faqs` 酒水licensing 条逐字："As a condition of entry to events at Palais Theatre, please be aware that bag checks or searches may be required upon arrival." | 文案写"可能被开包检查"，保留 "may" 的强度 |
| 5 | 场馆没有 cloakroom（寄存处），官方建议避免大件或笨重物品，并点名摩托头盔、大伞、大于 A4 的物品 | GREEN | `/faqs` 寄存条逐字："Palais Theatre does not have a cloakroom, so we recommend avoiding large or bulky items when attending a show — for example, motorbike helmets, large umbrellas, or items bigger than A4." | 逐字照搬三个举例 |
| 6 | 易腐食物无法在场馆存放，须留在车里或其他安全地点 | GREEN | `/faqs` 寄存条逐字："We're also unable to store perishable food items… please leave it in your car or another secure location before entering." | — |
| 7 | 自带可重复使用塑料水瓶必须是空的、容量 600mL 以下 | GREEN | `/faqs` Conditions of Entry（General Conditions）逐字："Personal reusable plastic drink bottles must be empty and under 600mL capacity. (There are free water stations in the Venue.)" | 两个条件（空 + <600mL）均照抄，未放宽 |
| 8 | 每人可带一瓶未开封的塑料瓶装水或软饮（非酒精）；已开封的须在入场前倒空 | GREEN | `/faqs` 酒水licensing 条逐字："You're welcome to bring one unopened plastic bottle of soft drink or water (non-alcoholic) per person. If you have an opened bottle, it'll need to be emptied before entering." | 与第 7 条并列呈现而非互相覆盖，见剔除项说明 |
| 9 | 场内楼上楼下 foyer 均有免费接水点 | GREEN | `/faqs` 酒水licensing 条逐字："Once inside, you'll find free water refill stations in both the downstairs and upstairs foyers." | — |
| 10 | 禁带"热食/餐食" | GREEN | `/faqs` Prohibited Items 逐字："Hot food/meals." | — |
| 11 | 禁带商业食品（快餐店或全服务餐厅购买的食物） | GREEN | `/faqs` 第二份禁带清单逐字："Commercial food (fast food items or food purchased from a full service restaurant)." | 逐字转述括号内的两类举例 |
| 12 | 婴儿车/推车不得带入场馆，场馆亦无寄存设施，须事先留在车内或其他地方 | GREEN | `/faqs` Prohibited Items："Prams or strollers."＋寄存条："prams aren't permitted inside the venue, and we don't have facilities to store them. Please arrange to store prams in your car or elsewhere prior to arrival." | 两处同向，无冲突 |
| 13 | 2 岁以上观众需购票；2 岁以下婴儿坐在成人腿上、不占座位可无需购票 | GREEN | `/faqs` 儿童条逐字："All guests over 2 years old will need a ticket… Babies under 2 years are welcome without a ticket, as long as they're seated on an adult's lap and not occupying their own seat." | 保留"不占座位"这个前提 |
| 14 | 18 个月以下婴儿参加成人演出须佩戴耳部防护，为入场条件（儿童演出不适用） | GREEN | `/faqs` 儿童条逐字："it's a condition of entry that babies under 18 months wear ear protection when attending adult concerts or events (this doesn't apply to children's shows). We recommend bringing your own ear protection" | 文案保留"自己带"为建议语气（原文 "We recommend"） |
| 15 | 场馆完全无现金，Box Office、餐饮、周边柜台均只接受卡或数字支付 | GREEN | `/faqs` 支付条逐字："Palais Theatre is a completely cashless venue, so card payments only are accepted… including the Box Office, Food & Beverage stands, and Merchandise counters." | 三个点位逐字照抄 |
| 16 | 预付票只有信用卡持卡人本人可领取，须出示购票所用信用卡及带照片的身份证件 | GREEN | `/faqs` 取票条逐字："The person whose name is on the credit card is the only person who can collect a prepaid ticket. The credit card used to purchase the ticket(s) and photo I.D. must be presented at time of pick up." | — |
| 17 | Box Office 仅在演出夜开门，于 doors open 时间前 30 分钟开始；非演出日可去 Ticketmaster 门店取票 | GREEN | `/faqs` Box Office 条逐字："Our Box Office is open on event nights, starting 30 minutes before the doors open (as listed on the event page)."＋"If you need to collect your tickets on a non-event day, you can visit any Ticketmaster outlet." | 不写任何具体钟点（官网要求看 event page／票面） |
| 18 | 场馆官网写明 Ticketmaster 是 Palais Theatre 演出的唯一授权售票方；非经其系统购买的票，Ticketmaster 与场馆均无法核验真伪 | GREEN | `/faqs` IMPORTANT NOTICE 逐字："Ticketmaster is the only authorised seller of tickets to Palais Theatre events."＋"Ticketmaster or the Palais Theatre are not able to verify if your tickets are legitimate as they have not been purchased on our system." | 仅照抄场馆自述，不作推荐；不点名任何转售平台（官网原文点了名，本篇按红线不转述那串名字） |
| 19 | 场馆全场有座，每张票对应指定座位；入场须前往票上所列区域（Orchestra / Stalls / Lounge / Dress Circle）；个别场次为 General Admission，先到先坐 | GREEN | `/faqs` 座位条逐字："Palais Theatre is a fully seated venue, and each ticket holder is assigned a specific seat."＋"whether it's the Orchestra, Stalls, Lounge, or Dress Circle."＋"Palais Theatre may host a General Admission event. For these, seating is on a first come, first served basis." | 只照抄四个区域名，**不解释楼层结构**，见剔除项 |
| 20 | Lounge A–D 排禁止站立与跳舞（票面写明，安全原因）；通道须全程保持畅通 | GREEN | `/faqs` 座位条逐字："For Lounge Rows A-D, no standing or dancing is allowed, as per your ticket and at the time of purchase. This is for safety reasons."＋"The aisles must remain clear throughout the performance for safety." | 排号与范围逐字照抄 |
| 21 | 其他区域按"多数人规则"决定能否站立/跳舞：多数人就座则请保持就座；多数人站立则允许，由工作人员视情况把控 | GREEN | `/faqs` 座位条逐字："We operate on a majority rules basis regarding standing and dancing. If the majority are seated, we kindly ask that you remain seated… If the majority of the crowd begins standing or dancing, this is permitted and staff will monitor accordingly." | — |
| 22 | 迟到者只能在演出的合适间隙入场 | GREEN | `/faqs` Latecomers 条逐字："Latecomers will be admitted only during a suitable break in the performance."（Show times 条同向："some shows may have a lock-out once the performance starts"） | 文案不写"一定会被锁在外面"，只写"等合适间隙" |
| 23 | 禁带 DSLR、摄像机、录音设备、三脚架、自拍杆；手机与小型手持个人相机可带；严禁闪光摄影 | GREEN | `/faqs` Prohibited Items 逐字："Cameras and equipment (e.g. DSLR, video cameras, audio recorders, tripods or selfie sticks)."＋允许项"Small, hand-held personal cameras and mobile phones."＋"Flash photography is strictly prohibited." | — |
| 24 | 应援牌（fan signs）可带，但不得大于 A2，须软卡纸材质且能折叠收于座位下；若挡到他人视线会被要求放下 | GREEN | `/faqs` Fan Signs 条逐字："please keep them no larger than A2 size. They must be made of soft card and should be able to be folded and stored under your seat if needed. If your sign is obstructing someone's view, we may ask you to put it down." | — |
| 25 | 大于 A3 的横幅、海报、旗子或标语禁止带入 | GREEN | `/faqs` Prohibited Items 逐字："Banners, posters, flags or signs larger than an A3 sheet of paper." | 与第 24 条的 A2（应援牌）并存，均照抄原文，未合并 |
| 26 | 场内设有六个吧台，并供应热的小食（bar snacks） | GREEN | `/food-and-drink` 逐字："Palais Theatre has six conveniently located bars…"＋"We have introduced hot bar snacks" | 不写任何菜品价格；菜品举例不入文案 |
| 27 | 吧台营业至中场休息，或至演出预定结束前 30 分钟 | GREEN | `/faqs` 酒水licensing 条逐字："Our bars are open until the interval, or up to 30 minutes before the scheduled end of the event." | — |
| 28 | 周边柜台位于地面层（Ground Level），繁忙场次会增开第二个柜台 | GREEN | `/faqs` 周边条逐字："You can find the merchandise counter on the Ground Level, and for busy shows, we may open a second counter" | 保留 "may" 的强度 |
| 29 | 场馆严格禁烟，含电子烟与 vaping | GREEN | `/faqs` Conditions of Entry 逐字："The Venue is strictly a smoke-free venue, including e-cigarettes and vaping." | — |
| 30 | 场馆不发 pass out（中途外出再入场凭证），除经场馆管理方批准 | GREEN | `/faqs` Conditions of Entry 逐字："No pass-outs will be issued, unless approved by Venue management." | 例外情形（经批准）已在文案括号内保留 |
| 31 | 进入持照酒水区域须出示政府签发的带照片身份证件 | GREEN | `/faqs` Conditions of Entry 逐字："Patrons must provide government issued photo identification to enter licensed area(s)." | — |
| 32 | 失物由场馆留存最多四周 | GREEN | `/faqs` 失物条逐字："All lost items are stored safely and will remain at the venue for up to four weeks" | 不写场馆邮箱/电话（见剔除项） |
| 33 | 场馆建议 14 岁以下儿童由负责的成年人陪同 | GREEN | `/faqs` 年龄条逐字："For safety and comfort, we prefer that children under 14 are accompanied by a responsible adult." | 原文是 "we prefer"，文案写"场馆建议"，未写成硬性规定 |

**主动排除项（官网查不到／官网内部口径不一致／属其他篇边界，本篇一律不写）**：

- 🔎 **"背包一律不能带"这个说法**——官网两份禁带清单口径不同：Conditions of Entry 写的是
  **"Eskies, backpacks or any bag larger than 30cm x 30cm."**（带明确尺寸），另一份 FAQ 清单
  只写 **"Backpacks and large bags."**（无尺寸、读起来像一律禁带）。文案**只采用带明确尺寸
  的那一侧**并写明 30cm×30cm，不写"背包一律不能带"——后者会让读者把小号背包也留在家里，
  且与官网第一份清单冲突。
- 🔎 **水瓶规则不作合并简化**——第 7 条（可重复用塑料瓶须空且 <600mL）与第 8 条（每人一瓶
  未开封瓶装水/软饮）出自官网两个不同条目，**既非互相覆盖也非互相否定**。文案把两种带法
  **并列写出**，不自行归纳成"水瓶一律要空的"或"一律可以带一瓶满的"——任何一种归纳都会在
  门口被现场规则打脸。
- **场馆楼层结构的解释**——本次 `/faqs` 座位条列出四个区域（Orchestra / Stalls / Lounge /
  Dress Circle），而 030 依据 `/accessibility` 页写的是"地面层 Stalls、一楼 Lounge"两层。
  两者未必冲突（无障碍页只覆盖它关心的两层），但本次**未取得任何一页逐字说明四个区域各在
  哪一层**，故本篇只照抄区域名、**不写楼层归属**，也不重复 030 的两层说法。
- **doors open / 开演的具体钟点**——官网明确要求看票面或 event page（"You'll find either the
  doors open time or the show start time listed on your ticket."），"通常 doors open 后约一
  小时开演"仅为 as a guide 的参考值，**不写成具体时刻**。
- **具体门牌号**——官方页只给路口，第三方有 12/14 号歧义，沿用 030 不写。
- **"澳洲最大有座剧院"／容量数字（2896 近 3000 座）／建筑风格（Art Deco 等）**——沿用 030
  的判定：维基百科该表述带 citation-needed、容量数字各源不一、风格口径冲突，一律不写。
- **具体座位视野推荐（哪个区/哪排视线好、声音好）**——官网未给；`/faqs` 退款条里虽提到
  "renowned for its incredible acoustics"，但那是场馆自我宣传语且紧接着在谈音响问题免责，
  **不作为"音响好"的客观断言引用**。
- **交通、停车、无障碍设施（电车站号/线路、火车换乘、周边车场、无障碍座位排号、电梯、
  Kulture City 感官友好认证）**——**属 030 边界，本篇整块不重复**（本篇是同一场馆的第二讲，
  刻意零重叠）。
- **场馆失物邮箱/电话、具体退款与换票流程、Verified Fan 机制、Fan-to-Fan 转售操作步骤**——
  均在 `/faqs` 可查到，但：失物联系方式属"落字面联系方式"（沿用 055 的处理不写）；退款/
  换票/转售流程属**转票防骗指南**栏目（013/046/051/057）的边界，不在场馆攻略里开第二条线。
- **官网点名的那几个非授权转售平台名字**——`/faqs` 原文确实列了名，但按账号红线"防诈内容
  不点名具体个人/账号/平台"，本篇**只转述"唯一授权售票方"这个正面事实**，不转述被点名的
  平台名单。
- **任何具体演出的名称/日期/票价/购票平台/主办方**——该场馆在 verified 池里唯一的演出已
  过期，其余同馆条目均为 `verified=false`，按红线一律不写。
- **任何统计数字**（被拦下人数、场馆年观演人次等）——一律不写。

FACT-AUDIT-STATUS: RED=0 CHECKED=33 SOURCES-CITED=33

## 渲染状态

- 模板: `cards/058/index.html`，复制自 `cards/055/index.html`。选 055 而非 001 作为基底的
  原因：055 是同一模板链上最新的一份**场馆攻略**（纯文字、无 `frame-img` 演出海报、5 张卡、
  P2/P4 带 `body` 长段落），与本篇结构完全同构，只需替换 poster 区块内的文案。已用 Python
  逐字节比对确认 `cards/055/index.html` 的 `<style>` 区块与 `cards/001/index.html`
  **完全一致（均 26896 字节，identical: True）**，故"保留 001 的 aushow 主题色 token 与
  已验证组件样式"这一要求已满足。`<html lang="zh-CN" data-theme="aushow">`、全部主题色
  token、字体、`.ticket`/`.ledger`/`issue-strip` 组件样式、WebGL 背景脚本全部原样保留，
  仅替换 5 个 poster 区块内的文案与 `<title>`。
- 卡片数: 5 张 `<section class="poster xhs" id="xhs-01…05">`，编号连续。
- 渲染: 交由 `automation/render_card.py`（headless Chrome 逐张截图 + PIL 校验 1080×1440）。
  本次会话按 `daily-xhs-prompt.md` 第 0 节要求，**未调用任何浏览器/截图工具**。
