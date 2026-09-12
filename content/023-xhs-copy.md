# 023 — Club Voltaire 看中文开放麦攻略（场馆攻略）

**选题类型**：场馆攻略（周六轮换位，2026-09-12 生成）
**场馆选择**：Club Voltaire（墨尔本 North Melbourne）——它是 `data/events.json` 中
`verified=true` 条目「候场喜剧 Loadingzone Comedy 开放麦(墨尔本,常驻)」的场馆。

**为什么选它、以及和前五篇场馆攻略的边界**：
- 这是 verified 池里**最后一座还没写过的场馆**：004＝Marvel Stadium、008＝ENGIE Stadium、
  011＝Chippo Hotel、016＝Margaret Court Arena、020＝TikTok Entertainment Centre。袁娅维两条
  的 Palais Theatre／Sydney Event Centre 因演出日（08-20／08-22）已过、池内再无演出挂在那两座
  场馆，本轮不写。
- 品类与 011 同为"小场"，但读者动作完全不同：011 的坑是"演出在**地下室**、别以为走错"，
  本篇的坑是"场馆在**巷子里的楼上**、门脸不在大街上、只能走楼梯"。这是一座 50 席的小剧场，
  不是酒吧。
- 该条目 `recurrence="常驻(场次见Eventbrite)"`，是常驻场次，攻略保鲜期长；且 010 只把它当
  "有这么个开放麦"安利过一次，场馆本身（怎么找、怎么去、多大）从未展开。

**信源纪律**：场馆客观信息全部取自 clubvoltaire.com.au（场馆官网 `/your-visit`、`/about`
两页）；楼梯这一条取自 Only Melbourne 的场馆条目；57 路电车走向用维基百科线路条目交叉核对。
逐条留 URL。**凡官网查不到、或与 events.json 字段可能打架的说法一律不写**（详见事实核查表
末尾的"主动排除项"，本篇最大的一处是**开场时间**）。

**红线自查**：
- 文中涉及该演出的断言只有：主办方名／城市／场馆与地址／售票平台／常驻性质，逐字取自
  events.json 的 `verified=true` 条目，并用 Eventbrite 主办方页与一场 2026 年场次页独立复核。
- **本篇不写票价、不写开场时间、不写下一场日期**。`price=null` 故不写价格；`time=19:00`
  与 Eventbrite 上该主办方历史场次时间（14:00／14:30／17:00／19:30 均出现过）不一致，且
  `recurrence` 字段本身写的就是"场次见 Eventbrite"，故全文一律引导读者"场次和时间看
  Eventbrite"，不给任何时间数字（已在 RUNBOOK 提请用户复核 `time` 字段）。
- 未点名任何个人／账号；不涉及防诈内容。

## 标题（14字）

墨尔本中文开放麦，藏在巷子楼上

## 正文（发帖文案，无外链）

在墨尔本想看中文开放麦，候场喜剧 Loadingzone Comedy 的常驻场地是 North Melbourne 的 Club Voltaire。

这家场馆第一次去的人十有八九会在巷口来回走两遍，所以先说最要紧的一件事 👇

🏚️ **它不在大街上，在 Raglan St 的巷子里，而且在楼上**。官网地址写的是 Level 1 / 14 Raglan Street——进了巷子要找的是一扇通往二层的门，不是临街店面。Only Melbourne 的场馆条目写得更具体：**上一段带扶手的木楼梯**才到。腿脚不方便、推婴儿车的朋友，出发前先在官网找电话问一句，官网和第三方条目都没提电梯。

🪑 **它只有 50 个座位**。官网自己的说法是"intimate bar and 50 seat theatre space"，从 2003 年开到现在，平时演的是 cabaret、burlesque、喜剧这类小剧场东西。50 席是什么概念——一个班的人坐满就没了。**晚到不是坐后排，是没位置。**

再记 3 条再出门（都是官网 Your Visit 页的原话）：

① **坐 57 路电车最省事**：到 Stop 11（Errol St 和 Victoria St 路口）下车，沿 Errol St 走 2 分钟到 Raglan St 巷口。57 路是 West Maribyrnong 到 Flinders St 那条，走 Elizabeth St → Victoria St → Errol St，从 CBD 上车就行。

② **坐火车的话是 North Melbourne 站**，官网写的是步行 17 分钟、930 米。不算近，天冷天黑的晚上想想清楚。

③ **开车的话 Raglan St 周边是路边停车**。官网只写了这一句，没写收费和时段，自己看牌子。

⚠️ 最后：候场喜剧的**具体场次和开场时间以 Eventbrite 为准**，这个开放麦不是固定每周同一天同一时间，我不敢写死一个数字给你。票也在 Eventbrite 上。

评论区扣 1，私信发你候场喜剧的 Eventbrite 主办方页和后续场次提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #墨尔本 #脱口秀 #中文脱口秀 #开放麦 #墨尔本生活 #看演出攻略 #NorthMelbourne

## 卡片文案结构（3张，票根美学）

> 张数说明：prompt 对场馆攻略类建议 2–3 张，本篇取 **3 张**，与 011（同为小场）一致。
> 理由：可核实事实密度低于体育场（无入场条款页、无停车费率、开场时间被主动砍掉），
> 硬拆成 4 张必然出现凑数卡。现结构为 封面／场馆 4 条／收尾 CTA，三张都满，无空卡。
> P3 保留账号档案里写死的固定 kicker 作品牌锚。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 场馆攻略 · Club Voltaire
- 大字标题: 中文开放麦 / 在巷子楼上
- 副标题: 候场喜剧 Loadingzone Comedy · 常驻
- 说明: 墨尔本 North Melbourne。门脸不在大街上，进巷子、上楼梯。
- 底部条: North Melbourne · MEL — Eventbrite 售票
- 配图: 无（场馆攻略不挂任何演出海报，沿用 004／008／011 做法）

**P2 这家场馆的 4 件事（ledger 4条）**
1. 在巷子里的楼上 — 官网地址 Level 1 / 14 Raglan St；Only Melbourne：上一段带扶手的木楼梯。没提电梯
2. 只有 50 个座位 — 官网原话 "50 seat theatre space"，2003 年开到现在。晚到不是坐后排，是没位置
3. 57 路电车最省事 — Stop 11（Errol St & Victoria St）下车，沿 Errol St 走 2 分钟到巷口
4. 火车 17 分钟 — North Melbourne 站，官网写步行 930 米。开车的话 Raglan St 周边路边停车
- 收尾: 具体场次和开场时间以 Eventbrite 为准——这个开放麦不是每周固定时间，别照旧攻略卡点。
- 底部条: Level 1 / 14 Raglan St — North Melbourne VIC 3051

**P3 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 巷口来回走两遍 / 是正常的
- 正文: 找的是通往二层的一扇门，不是临街店面。50 席小剧场，坐满就是坐满。
- 补充: 场次、时间、票都在 Eventbrite 上。评论区扣 1，私信发你候场喜剧的主办方页和后续场次提醒。
- 底部条: VOL. 023 — 简介里有完整演出日历

## 事实核查表

| 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|
| 候场喜剧 Loadingzone Comedy 在墨尔本有常驻中文开放麦 | GREEN | `data/events.json` 条目「候场喜剧 Loadingzone Comedy 开放麦(墨尔本,常驻)」：`category=开放麦`、`city=墨尔本`、`recurrence=常驻(场次见Eventbrite)`、`verified=true` | 该条目 `date=null`，故全文不给任何具体日期 |
| 该开放麦的场地为 Club Voltaire，地址 1st Floor/14 Raglan St, North Melbourne | GREEN | 同上条目 `venue="Club Voltaire, 1st Floor/14 Raglan St, North Melbourne"` | JSON 的 venue 字段本身即含店名与地址 |
| 场馆官网自述地址为 Level 1 / 14 Raglan Street, North Melbourne 3051 | GREEN | https://www.clubvoltaire.com.au/your-visit （2026-09-12 WebFetch，原文 "Level 1 / 14 Raglan Street, North Melbourne 3051, VIC AUSTRALIA"） | 与 JSON 的 "1st Floor/14 Raglan St" 同义、门牌街道逐字一致；What's On Melbourne 条目 https://whatson.melbourne.vic.gov.au/things-to-do/club-voltaire 亦写 "1st Floor/14 Raglan St, North Melbourne 3051" |
| 该场次由 Eventbrite 售票且当前在售 | GREEN | 同上 JSON 条目 `ticket_platform=Eventbrite`、`status=on_sale`；另经 https://www.eventbrite.com/o/loadingzone-comedy-75417874333 （2026-09-12 WebFetch）复核该主办方页当前 live，搜索结果标题显示 "4 Upcoming Activities" | 主办方页场次列表为 JS 渲染，本次抓取未能读到具体场次，故文案只写"票在 Eventbrite 上"，不写下一场日期 |
| 候场喜剧 2026 年确有开放麦场次在 Club Voltaire 举办 | GREEN | Eventbrite 场次页 https://www.eventbrite.com.au/e/321-city-tickets-1985227108723 （2026-09-12 WebFetch）：标题「候场喜剧3月21号星期六- 墨尔本City开放麦」，Venue "Club Voltaire, Raglan Street, North Melbourne, VIC, Australia"，状态 Event ended | 用来佐证"常驻场地是 Club Voltaire"在 2026 年仍成立，不作为"下一场"信息发布 |
| 候场喜剧隶属 AUNZ Comedy Media，为华语喜剧厂牌 | GREEN | JSON `notes="AUNZ Comedy Media旗下…喜剧厂牌"`；Eventbrite 主办方页自述原文「澳大利亚AUNZ COMEDY MEDIA旗下运营的一家以喜剧内容为核心的澳洲华语文化厂牌」 | 文案仅称"候场喜剧 Loadingzone Comedy"与"中文开放麦"，未写"双语"（JSON notes 与官方"华语"口径不一致，沿用 022 值班日志已记录的处理：不采用"双语"） |
| 场馆位于 Raglan St 的巷子（laneway）里 | GREEN | https://www.clubvoltaire.com.au/about （2026-09-12 WebFetch，原文 "located down the Raglan St laneway in the heart of North Melbourne's bustling arts precinct"） | 文案"不在大街上，在巷子里"由此直接推得 |
| 场馆在一楼（Level 1），需上一段带扶手的木楼梯 | GREEN | 官网 your-visit 页 "Level 1"（同上）；Only Melbourne 场馆条目 https://www.onlymelbourne.com.au/club-voltaire （2026-09-12 WebFetch，原文 "Club Voltaire is on the 1st floor of the building up a flight of wooden stairs with a handrail."、"First floor above Gallery Voltaire."） | ⚠️ 楼梯细节来自第三方条目，文案已明确归属"Only Melbourne 的场馆条目写得更具体"；**不写"没有无障碍通道／无障碍厕所"**——搜索摘要有此说法但无法定位到具体来源页，只写"官网和第三方条目都没提电梯"这一可核的事实 |
| 场馆为 50 席小剧场兼酒吧 | GREEN | 官网 about 页（同上，原文 "Our intimate bar and 50 seat theatre space"）；Creative Spaces 条目 https://www.creativespaces.net.au/space/club-voltaire （"An intimate 50 seat theatre"，Capacity 50） | 两个来源互证；文案"晚到不是坐后排，是没位置"是由 50 席直接推得的定性提醒，不给"几点前到"这类未核实建议 |
| 场馆自 2003 年起营业，常演 cabaret／burlesque／喜剧 | GREEN | 官网 about 页（同上，原文 "providing alternative, eccentric & unique live performances for audiences since 2003"）；What's On Melbourne 条目（同上，列出 "cabaret, burlesque, comedy, live music, circus, drag, magic"） | 文案只举 cabaret、burlesque、喜剧三例，均在官方列表内 |
| 57 路电车到 Stop 11（Errol St & Victoria St 路口），沿 Errol St 步行 2 分钟到 Raglan St 巷口 | GREEN | 官网 your-visit 页（同上，原文 "Take the 57 Tram to Stop 11 on the corner of Errol Street & Victoria Street then take a 2 minute stroll up Errol St to the Raglan St laneway."） | 逐字照抄官网，"2 分钟"归属官网口径 |
| 57 路电车为 West Maribyrnong – Flinders St 线，经 Elizabeth St、Victoria St、Errol St | GREEN | 维基百科 Melbourne tram route 57 https://en.wikipedia.org/wiki/Melbourne_tram_route_57 （"from West Maribyrnong to Flinders Street station… travels along Elizabeth Street before turning onto Victoria Street towards North Melbourne, then travels along Errol, Queensberry and Abbotsford Streets"）；PTV 线路页 https://www.ptv.vic.gov.au/route/887 （"57 West Maribyrnong - Flinders Street Station"） | 用来交叉核对官网"57 路"这一说法在 2026-09 仍成立，文案据此写"从 CBD 上车就行" |
| North Melbourne 火车站步行 17 分钟、930 米 | GREEN | 官网 your-visit 页（同上，原文 "North Melbourne Railway Station is a 17min (930m) walk away."） | 与 011 不同，本篇步行数字有**场馆官网**单一口径，故可写，且文案已明确"官网写的是" |
| Raglan St 周边为路边停车 | GREEN | 官网 your-visit 页（同上，原文 "On-street parking is available surrounding Raglan St."） | 官网未写收费／时段，文案已明确"官网只写了这一句…自己看牌子" |

**主动排除项（查不到官方依据／与 JSON 字段可能打架，本篇一律不写）**：

- **开场时间**——JSON `time=19:00`，但 Eventbrite 上该主办方历史场次页显示的开场时间有
  14:00（2025-05-04／05-25／08-17）、14:30（2025-09-14，且该场在 139 Franklin St 另一场地）、
  17:00（2024-12-22）、19:30（2026-03-21）多种；`recurrence` 字段本身写"场次见 Eventbrite"。
  为避免读者按一个错误时间到场，本篇不写任何开场时间，全篇引导看 Eventbrite。**已在 RUNBOOK
  提请用户复核 `time` 字段是否应改为 null。**
- **下一场具体日期**——Eventbrite 主办方页为 JS 渲染，本次抓取读不到场次列表；`date=null`。不写。
- **票价**——`price=null`，Eventbrite 各场次页本次抓取亦未显示价格。全文不出现任何金额。
- **场馆营业时间**——官网写 "PERFORMANCES / Wednesday to Sunday / 7pm–11pm"，但候场喜剧历史场次有
  周日 14:00 开场的，与该时段不符（应属场馆 "Available for Hire" 时段）。写出来会与"看 Eventbrite"
  的引导互相打架，整块不写。
- **场馆自身的售票方式**（官网写 Trybooking 线上购票／电话预留／门口售票）——这是场馆自办演出的
  规则，候场喜剧的票在 Eventbrite（JSON 字段），两者并列会误导读者"到门口买就行"。不写。
- **无轮椅通道／无无障碍厕所／巷内鹅卵石路面**——搜索摘要有此类说法，但无法定位到具体来源页
  （Melbourne Fringe 场馆页返回 403），不予采信。只写"官网和第三方条目都没提电梯"。
- **"巷子里左手边"**（Only Melbourne："You'll find us on the left"）——单一第三方来源、无官网佐证，
  且方向描述依赖进巷方向，不写。
- **场馆电话**——官网 contact 页有列，但小红书文案不放外部联系方式（沿用 022 做法），只写
  "在官网找电话"。
- **"部分演出含裸露"**（What's On Melbourne 条目）——指该场馆其他类型演出，与开放麦无关，不写。
- **入场安检、包尺寸、能否带外食、拍照政策、饮品价格**——无公开条款页，不写。

FACT-AUDIT-STATUS: RED=0 CHECKED=14 SOURCES-CITED=14

## 渲染状态

- 模板: `cards/023/index.html`，复制自 `cards/011/index.html`（与 `cards/001/index.html` 的
  `<head>` 逐字一致、仅 `<title>` 不同，已 diff 确认；选 011 是因为它已是 3 张纯文字版式，
  且带 `.ledger-note` 的 `max-width:460px` 内联约束）。`<html data-theme="aushow">`、主题色
  token、字体、`.ticket`/`.ledger`/`issue-strip` 组件样式全部原样保留，仅替换 `<title>` 与
  `<section class="poster xhs">` 区块内文案。
- 卡片数: 3 张 `<section class="poster xhs" id="xhs-01…03">`
- 渲染: 交由 `automation/render_card.py`（headless Chrome 逐张截图 + PIL 校验 1080×1440）。
  本次会话按 `daily-xhs-prompt.md` 第 0 节要求，未调用任何浏览器/截图工具。
