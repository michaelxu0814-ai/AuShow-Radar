# 047 — Chippo Hotel 买票认对那一页（场馆攻略）

**选题类型**：场馆攻略（周三轮换位，2026-10-07 生成）
**场馆选择**：The Chippo Hotel（悉尼 Chippendale）——`data/events.json` 中 `verified=true`
条目「Rolling Donkey 中文喜剧开放麦(悉尼,每周二)」的场馆。

**为什么又是这座场馆**：verified 池里 8 座场馆（004=Marvel、008=ENGIE、011=Chippo、
016=Margaret Court、020=TikTok Entertainment Centre、023=Club Voltaire、030=Palais、
034=Sydney Event Centre）均已写过一轮；第二轮换角度重讲已完成 027(Marvel 散场)、
037(ENGIE 散场)、040(TikTok Ent Centre 怎么去+找对门)、043(Margaret Court 怎么去+认对门)。
按"最久没被写过"取 **Chippo Hotel（011，2026-08-29，39 天前）**——下一个才是 023 的
Club Voltaire（09-12）。本篇是 **第五次"回头换角度重讲"**。

**角度（与 011／022 零重叠）**：011 写"这家店是什么"（全素 pub／演出在地下室／4 点开门／
退款／年龄），022 写"台上会发生什么"（开放麦≠专场）。本篇写**买票那一步**——
2026-10-07 实测发现：**场馆官网 WEEKLY EVENTS 栏目里 Rolling Donkey 的「Tickets」按钮，
落地页是一个显示 "Event ended / Sales ended" 的旧 Eventbrite 场次页**，而 `events.json`
里记的那一页（"Every Tuesday, 7:30 PM" / "Multiple dates"）仍在售。这是个只有点下去才会
撞到的坑，也正好是本账号"认对页面"的口径。第二块是**周二这栋楼同时挂着两场活动**
（官网周二同列 Rolling Donkey 与 Pub Trivia，一个按钮写 Tickets、一个写 Book Now），
第三块是周二的餐饮特价。011／022 三块全部没写过。

**信源纪律**：场馆事实全部取自场馆官网（首页 WEEKLY EVENTS／WEEKLY SPECIALS、菜单页，
2026-10-07 curl 原文 + href 逐一核对）与两个 Eventbrite 场次页；地下室一句沿用 011 已核
的 Broadsheet／Time Out。官方没写、或第三方口径打架的一律不写（Pub Trivia 的开始时间
就是被整块砍掉的，详见"主动排除项"）。

**红线自查**：演出相关断言（星期／开场时间／场馆／售票平台／在售状态）逐字取自
`events.json` 的 `verified=true` 条目并经在售 Eventbrite 页复核；`price=null` 故全文不给
任何票价数字（出现的 `$5 / $14 / $22.50` 是场馆官网的**餐饮**价格，已在文案里明确标注
来源与"以当天店里为准"）；未点名任何个人／账号（主办方的微信联系 ID 已剔除）；
官网同栏目里其它非 verified 场次（周一 Comedy Cagefight、周三／周四 Stand Out Comedy）
一律不写。

## 标题（16字）

悉尼中文开放麦，官网票链接是旧页

## 正文（发帖文案，无外链）

在悉尼看中文开放麦的，这条建议先存一下。

Rolling Donkey 的中文喜剧开放麦，**每周二 19:30**，场地在 Chippendale 的 The Chippo Hotel——这个没变。会出问题的是**买票那一步**。

🔗 **场馆官网上那个「Tickets」按钮，点进去是一个已经结束的旧场次页。**

我今天（10/7）从场馆官网的 WEEKLY EVENTS 栏目点 Rolling Donkey 的购票按钮，落地的 Eventbrite 页面上明明白白写着 **"Event ended"**、**"Sales ended"**。

**但这不是场次取消了。** 同一个主办方在 Eventbrite 上有新旧两个页面，官网那个按钮还挂在旧的那一个上。真正在售的那页，写的是 **"Every Tuesday, 7:30 PM"**，日期处显示 **"Multiple dates"**（多场次），能正常往下走。

所以买票只认两件事 👇
① 页面上写着 **Every Tuesday, 7:30 PM**
② 还能点进下一步，而不是停在 "Sales ended"

两条对不上的那一页，直接退出去重搜，别在上面纠结"为什么买不了"。

🧠 **第二个容易走错的地方：周二这栋楼里不止一场活动。**

官网的 WEEKLY EVENTS 里，周二同时挂着两个——**Rolling Donkey**（按钮写 Tickets）和 **Pub Trivia**（按钮写 Book Now）。这俩入口根本不是一个东西，别拿 trivia 的订位当开放麦的票。

进门看到楼上一桌一桌在答题也别慌，你没走错：Broadsheet 和 Time Out 都提到这里有个专门的地下室演出厅，喜剧在楼下那间。

🌮 **最后一条是纯占便宜的。**

官网的 WEEKLY SPECIALS 写着周二 **"$5 Tacos & $14 Margaritas"**。同一个菜单页上，Soft Tacos 的正价是 **$22.50**（3 个，四种口味可选）。原文没写 $5 是几个、哪种口味，我也不替它编——**以当天店里为准**，但"周二来看开放麦顺手先吃个晚饭"这个时间点是对的。

（顺便，这家店是全素 pub，官网首页自己写着 "Australia's first 100% vegan pub"。所以 taco 的四种口味——crumbed chick'n、花菜、菇、墨西哥豆——全是植物基的。）

地址 87-91 Abercrombie Street, Chippendale NSW 2008，票在 Eventbrite。

评论区扣 1，私信发你这场开放麦**当前在售**的那一页，还有后续演出提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #悉尼 #中文脱口秀 #开放麦 #脱口秀 #悉尼生活 #看演出攻略

## 卡片文案结构（4张，票根美学）

> 张数说明：取 **4 张**（封面／买票认两条 ledger／周二这栋楼 ledger／收尾 CTA），
> 与 040／043 同结构。011 当时取 3 张是因为那篇可核实事实密度低；本篇有官网首页
> ＋菜单页＋两个 Eventbrite 页共 14 条已核事实，两张 ledger 都填满、无凑数卡。
> P4 保留账号档案里写死的固定 kicker 作品牌锚。场馆攻略不挂任何演出海报（沿用
> 004／008／011／023／030／034／040／043 做法）。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 场馆攻略 · The Chippo Hotel
- 大字标题: 官网那个购票按钮 / 点进去是旧页
- 副标题: Rolling Donkey · 每周二 19:30
- lead: 悉尼 Chippendale。场次没取消——是 Eventbrite 上新旧两个页面，官网的按钮还挂在旧的那个上。
- 底部条: 每周二 · SYD — Eventbrite 在售
- 配图: 无

**P2 买票认两条（ledger 4条）**
1. 官网按钮挂的是旧页 — 2026-10-07 实测：场馆官网 WEEKLY EVENTS 里 Rolling Donkey 的 Tickets 按钮，落地页显示 "Event ended"、"Sales ended"
2. 在售那页长这样 — 页面写 "Every Tuesday, 7:30 PM"，日期处显示 "Multiple dates"，能正常点下一步
3. 两页同一个主办方 — 新旧两页的 Eventbrite 主办方名称一致，旧页只是没下架，不是山寨页
4. 对不上就退出去重搜 — 既不写 Every Tuesday 7:30 PM、又停在 "Sales ended" 的，别在上面等它恢复
- 底部条: 来源 场馆官网 + Eventbrite — 2026-10-07 实测

**P3 周二这栋楼（ledger 4条）**
1. 周二挂着两场 — 官网 WEEKLY EVENTS 周二同时列 Rolling Donkey 和 Pub Trivia
2. 入口不是一个 — 开放麦按钮写 Tickets（Eventbrite 票），Pub Trivia 按钮写 Book Now；别拿订位当票
3. 喜剧在楼下那间 — Broadsheet / Time Out 都提到场馆有专门的地下室演出厅；楼上在答题不代表你走错
4. 周二餐饮特价 — 官网 WEEKLY SPECIALS 原文 "$5 Tacos & $14 Margaritas"；菜单 Soft Tacos 正价 $22.50（3 个）。没写 $5 是几个，以当天店里为准
- 底部条: 87-91 Abercrombie St, Chippendale — 全素 pub（官网自述）

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 认页面 / 不认按钮
- lead: "Every Tuesday, 7:30 PM"＋"Multiple dates"＋还能点下一步——三条都对上，才是在售的那一页。按钮会过期，场次不一定。
- body: 评论区扣 1，私信发你这场开放麦当前在售的那一页，还有后续开票提醒。
- 底部条: Vol. 047 — 简介里有完整演出日历

## 事实核查表

| 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|
| Rolling Donkey 中文喜剧开放麦为悉尼常驻场次，每周二 19:30 | GREEN | `data/events.json` 条目「Rolling Donkey 中文喜剧开放麦(悉尼,每周二)」：`recurrence=每周二`、`time=19:30`、`city=悉尼`、`category=开放麦`、`verified=true` | 该条目 `date=null`，故全文只写"每周二"，不给任何具体日期 |
| 场馆为 The Chippo Hotel，地址 87-91 Abercrombie Street, Chippendale NSW 2008 | GREEN | 同上条目 `venue="Chippo Hotel, 87-91 Abercrombie St, Chippendale"`；在售 Eventbrite 页 https://www.eventbrite.com/e/copy-of-rolling-donkey-tickets-1983189907399 （2026-10-07 WebFetch，原文 "87-91 Abercrombie Street, Chippendale, NSW 2008"） | ⚠️ 口径冲突延续 011：场馆官网页脚写 "87-93 abercrombie St."（2026-10-07 复现）。采信读者实际会点进去的售票页＋JSON 的 87-91，差异仅门牌尾号、指向同一栋 |
| 该场次由 Eventbrite 售票，当前在售 | GREEN | 同上条目 `ticket_platform=Eventbrite`、`status=on_sale`；在售 Eventbrite 页 2026-10-07 WebFetch 返回 "Multiple dates"，页面无 "Event ended"／"Sales ended" 字样 | 本次为该条目第四次独立复核（前三次见 006／011／022） |
| 在售页写明 "Every Tuesday, 7:30 PM" 且日期处显示 "Multiple dates" | GREEN | 同上在售 Eventbrite 页（2026-10-07 WebFetch，原文 "Every Tuesday, 7:30 PM"、"Multiple dates"） | 与 JSON 的 `recurrence`／`time` 两字段吻合，构成外部互证；这两句原文被直接写进文案当作读者的辨别依据 |
| 场馆官网 WEEKLY EVENTS 栏目把 Rolling Donkey 列为每周二 | GREEN | 场馆官网首页 https://www.thechippohotel.com.au/ （2026-10-07 curl 全文抽取，原文 "WEEKLY EVENTS" / "Rolling  Donkey" / "Every" / "TueSDAY"） | 第三个独立来源（场馆方）印证"每周二"这一断言 |
| 官网该栏目里 Rolling Donkey 的购票按钮指向 https://www.eventbrite.com/e/rolling-donkey-tickets-1783418686299 | GREEN | 同上官网首页 HTML（2026-10-07 curl）：自 "WEEKLY EVENTS" 起按文档顺序解析，该 href 紧随 "Rolling Donkey" 区块、位于 "Pub Trivia" 区块之前 | 用 href 位置（而不是肉眼看页面）确认按钮归属，避免把 Comedy Cagefight 的链接错配给 Rolling Donkey |
| 上述旧页面当前显示 "Event ended" / "Sales ended" | GREEN | https://www.eventbrite.com/e/rolling-donkey-tickets-1783418686299 （2026-10-07 WebFetch，原文 "Event ended"、"Sales ended"，状态判定 Past/Unavailable） | 本篇最核心的一条，也是整篇的选题由来 |
| 新旧两个 Eventbrite 页属于同一主办方 | GREEN | 两页的 organiser 字段在 2026-10-07 WebFetch 中为同一名称（旧页 "@Rolling Donkey喜剧…"、在售页 "Rolling Donkey喜剧…"）；JSON `notes` 亦记"小红书/公众号/抖音同名账号" | 文案据此写"不是山寨页，旧页只是没下架"；**主办方名称里的平台账号串与微信 ID 一律不进文案**（沿用 022 的剔除做法） |
| 官网 WEEKLY EVENTS 里周二同时列有 Pub Trivia | GREEN | 同上官网首页（2026-10-07 curl，原文 "Pub Trivia" / "Every" / "TUESDAY"） | 以"同一晚同一栋楼的另一场活动、避免走错入口"的场馆运营信息出现，不作为演出推荐，不写其时间／票务细节 |
| 官网上开放麦的按钮文案为 "Tickets"、Pub Trivia 的按钮文案为 "Book Now" | GREEN | 同上官网首页（2026-10-07 curl，Rolling Donkey 区块末为 "Tickets"，Pub Trivia 区块末为 "Book Now"） | 只写按钮**文案差异**；Pub Trivia 的 "Book Now" 在静态 HTML 中无 href（疑为 JS 组件），故不写它指向哪里 |
| 场馆设有专门的地下室演出厅，喜剧在地下室 | GREEN | Broadsheet https://www.broadsheet.com.au/sydney/chippendale/bars/chippo-hotel （"an intimate stage in the basement of the venue … as well as comedy"）＋ Time Out https://www.timeout.com/sydney/bars/the-chippo-hotel （"a basement gig room for live music and comedy"） | **本篇与 011 唯一的一处有意重叠**：讲"楼上在答题你没走错"必须有这句才成立，沿用 040 的"一句衔接"做法，不展开 |
| 官网 WEEKLY SPECIALS 写明周二 "$5 Tacos & $14 Margaritas" | GREEN | 场馆官网首页＋菜单页 https://www.thechippohotel.com.au/menu （2026-10-07 curl，两页 WEEKLY SPECIALS 区块原文一致："Tuesday $5 Tacos & $14 Margaritas"） | 这是**餐饮**价格不是票价；文案明确标注出处并加"以当天店里为准"，不写份数／口味（原文未写） |
| 菜单上 Soft Tacos 正价 $22.50，3 个，四种口味可选 | GREEN | 同上菜单页（原文 "Soft Tacos / 3 tacos with fresh slaw, pico de gallo, chipotle mayo, guacamole and pickled jalapeños. Choose from: Crumbed Chick'n, Battered Cauliflower, Grilled Mushroom, or Mexican Beans." / "$ 22.5"） | 给出正价是为了让 $5 这个特价有参照，不构成"周二能 $5 吃到 3 个"的承诺 |
| 该店为 100% 全素 pub，故 taco 四种口味均为植物基 | GREEN | 场馆官网首页（2026-10-07 curl，`<title>` "The Chippo Hotel \| Australia's First 100% Vegan Pub"、首屏大字 "AUSTRALIA'S FIRST 100% VEGAN PUB"）＋菜单页全菜单命名体系（chick'n／cheeze／fysh／prawnz／konjac "kalamari"／beef-style mince） | ⚠️ 核查过程记录：WebFetch 的摘要模型一度把菜单读成"含肉类／海鲜／乳制品"，拉原文逐项核对后确认是**植物基仿荤命名**，011 的全素结论仍成立。文案把"全澳第一"明确归属为官网自述，不由本账号背书 |

**主动排除项（查不到官方依据／来源口径打架／触红线，本篇一律不写）**：

- **Pub Trivia 的开始时间和所在房间**——官网该区块只写 "Every TUESDAY" 不写时间；第三方
  聚合站口径打架（一处称 "free trivia from 7:30pm"，另一处把 trivia 写成周一、把周二特价
  写成 "$20 植物基 pasta＋酒＋garlic bread"，与官网的 "$5 Tacos & $14 Margaritas" 直接冲突）。
  整块剔除，文案只写"周二同时有这场活动、入口不一样"。
- **其它非 verified 场次**——官网同一栏目里的周一 Comedy Cagefight、周三／周四
  Stand Out Comedy、周三 Pool Comp 以及 10–12 月的 live 场次（Media Puzzle、Gabe Levin 等），
  均不在 `data/events.json` 的 `verified=true` 池内，按账号红线不写，也不作"周二来不了可以去
  这些"的替代推荐。
- **票价**——JSON `price=null`，在售 Eventbrite 页 2026-10-07 仍未显示价格。全文无任何票价
  数字，也不写"便宜／几十块"这类模糊暗示。文中 `$5 / $14 / $22.50` 已逐个标注为场馆餐饮价。
- **两个 Eventbrite 页的 URL**——正文不放外链（账号红线）；旧页 URL 只写进本文件的核查表，
  不进发帖文案，避免读者反而被引到已结束的那一页。
- **退款条款（演出前 7 天）与 14 岁以下需家长陪同**——事实仍成立（在售页 2026-10-07 复现），
  但 011 已写过，为保持与 011 零重叠本篇不再写。
- **营业时间**——官网 "MONDAY - TUESDAY: 4PM-12PM" 自相矛盾（011 已记录，今日复现），不写。
- **交通／步行时间／最近车站距离**——仍无官方口径，011 记录过的第三方 10／11／23 分钟与
  335 米四种互斥说法未解决，继续整块剔除。
- **地下室容量／座位数／能否站／演出时长／演员阵容**——无官方数字，不写（022 已说明阵容为
  轮换制）。
- **入场安检／包尺寸／能否带外食／拍照政策／停车**——该场馆无公开 Conditions of Entry 页，
  不套用体育场条款，不写。
- **主办方微信联系 ID**——在售 Eventbrite 页有，不写（沿用 022）。

FACT-AUDIT-STATUS: RED=0 CHECKED=14 SOURCES-CITED=14

## 渲染状态

- 模板: `cards/047/index.html`，复制自 `cards/043/index.html`。选 043 作基底的原因：它是
  模板链上最近的一篇**场馆攻略**（4 张、两张 ledger、无配图），且其 `<head>`／CSS 与链上
  最新的 046 逐行一致（已 diff 确认，差异仅 `<title>` 与 poster 区块内文案），没有 043 之后
  新增的样式修正会被漏掉。`<html data-theme="aushow">`、主题色 token、字体、
  `.ticket`/`.ledger`/`issue-strip` 组件样式全部原样保留，仅替换 4 个 poster 区块内的文案
  与 `<title>`。
- 卡片数: 4 张 `<section class="poster xhs" id="xhs-01…04">`
- 渲染: 交由 `automation/render_card.py`（headless Chrome 逐张截图 + 1080×1440 校验）。
  本次会话按 `daily-xhs-prompt.md` 第 0 节要求，未调用任何浏览器／截图工具。
