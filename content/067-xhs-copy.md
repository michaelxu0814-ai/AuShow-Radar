# 067 — TikTok Entertainment Centre 带娃观演攻略（场馆攻略）

**选题类型**：场馆攻略（周六轮换位，2026-10-31 生成）
**场馆选择**：TikTok Entertainment Centre（悉尼 Darling Harbour，ICC Sydney 剧院馆）——
它是 `data/events.json` 中 `verified=true` 条目「AKMU 乐童音乐家 澳洲演唱会 悉尼站」的场馆
（JSON 里记的是旧名 `ICC Sydney Theatre`，同一座馆）。该条目 2026-09-20 演出日已过，
**本篇不锚定任何一场具体演出**，只写场馆本身的 evergreen 规则。

**为什么选它 + 与 020／040 的边界**：verified 池里 8 座场馆已全部写过两轮以上，本篇是
第三次触碰这座馆，也是**它距上次被写最久**的一座（020 在 2026-09-09、040 在 2026-10-01，
距今 30 天；其余七座最近一次都在 10-03 之后）。前两篇的主角与本篇零重叠：
- 020 的主角是**场馆改名 + 随身物品禁带清单**（背包／专业相机／自拍杆／平板、寄存免费）。
- 040 的主角是**怎么去 + 找对门**（轻轨 Exhibition 站、正门 Tumbalong Blvd、打车 Zollner
  Circuit、停车 Car Park 2）。
- 本篇的主角是**带小孩来这座馆**：2 岁就要票、2 岁以下官网不建议带、婴儿车不进座位区、
  育婴室在 Level 2，外加三条家长最容易踩的场内规则（全场无现金且不收支付宝／微信、
  水瓶不让带、急救室与遗失物品在哪）。这是 18 篇场馆攻略里**第一次写"带娃观演"这个角度**
  （055／064 写的是无障碍观演，面向轮椅与低行动能力观众，规则条目与本篇不重合）。

**红线自查**：
- 全篇**不写任何演出的日期／票价／开演时间／购票平台**。该馆在 verified 池里唯一的演出
  （AKMU 悉尼站 2026-09-20）已过期，且其 `price` 与 `time` 在 JSON 里均为 `null`。
- 场馆客观信息逐条取自 `iccsydney.com.au`（场馆运营方官方站）与 `tiktokentcent.com`
  （场馆官方站），留 URL；**凡官网查不到的说法一律不写**（见文末主动排除项）。
- 官方 FAQ 里"Earplugs"一条仍使用旧名 `ICC Sydney Theatre`，文案中如实标注"同一座馆"，
  不替官网改写口径。

## 标题（11字）

带娃看演出，2岁就要票

## 正文（发帖文案，无外链）

悉尼 **TikTok Entertainment Centre**（ICC Sydney 的剧院馆，达令港，14 Darling Drive）带小孩来看演出，有几条规则官网写得很硬，到了门口才发现就晚了 👇

👶 **2 岁就要买票**。官网 FAQ 原话：**"Children 2 years of age and older require a ticket to enter TikTok Entertainment Centre and must occupy their ticketed seat."**（2 岁及以上进场要票，而且要坐在自己票上的那个座位。）面向儿童的场次年龄规则可能不一样，以该场次页面和票面条款为准。

🔇 **2 岁以下，官网不建议带**。原话写得很直白：现场音量很大（strong noise levels），小孩需要适当的护耳。耳塞不一定要自己带——官网写明可以在 **Level 2 的客服台（Customer Service Desk）**买到（这一条 FAQ 用的还是旧名 ICC Sydney Theatre，指的就是这座馆）。

🚼 **婴儿车不能推进座位区**。为保持通道畅通，演出期间婴儿车必须寄存在该场次指定的位置；**寄存点每场可能不同**，提前看场馆发的活动邮件，或到场问引导员。娱乐类场次的寄存处在场馆外侧的 **Tumbalong Boulevard 或 Moriarty Walk**——过安检之前就能把东西放掉，不用拎到闸口再折返。

🍼 **育婴室在 Level 2**。官网给的配置：喂奶区、换台、备餐区。

💳 **全场不收现金，也不收支付宝和微信支付**。官网原话：**"ICC Sydney is a cashless venue."**，餐饮亭、咖啡、停车、周边全部只收 eftpos；主流信用卡、借记卡和 Apple Pay／Google Pay／Samsung Pay 可以用。带现金来的，连一瓶水都买不了。

🚰 **水瓶不能带进场**，但每个吧台都有**免费的水和可降解杯子**，场内零售点也有瓶装水卖。

🏥 **急救室两处**：Level 2（Door 1 旁边）和一楼。东西丢了：活动期间在 Level 2 客服台，散场之后转到安保办公室。

还有一条带小孩特别容易踩：可以在自己票位前站着跳，但官网明写**不许站在座椅上**。

评论区扣 1，私信发你这份带娃看演出清单，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #悉尼 #带娃看演出 #演唱会攻略 #悉尼遛娃 #看演出 #澳洲生活

## 卡片文案结构（4张，票根美学）

> 张数说明：prompt 允许场馆攻略 2–3 张、不为凑数硬填。本篇用 4 张的理由与 043／061 相同：
> 「带娃进场」（2岁要票／护耳／婴儿车／育婴室）与「场内这四条」（付钱／水／急救室／失物）
> 各自饱满且互不重叠，压成一张会变成 8 行 ledger 不可读；封面与 CTA 是账号档案写死的品牌
> 结构（P4 固定 kicker 作品牌锚）。无空卡、无凑数卡。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 场馆攻略 · TikTok Entertainment Centre
- 大字标题: 带娃看演出 / 2 岁就要票
- 副标题: 悉尼达令港 · ICC Sydney 剧院馆
- 说明: 婴儿车不能推进座位区、水瓶不让带、全场不收现金——这几条官网都写死了。全部取自场馆官网。
- 底部条: 悉尼 Darling Harbour — 14 Darling Drive
- 配图: 无（场馆攻略不挂任何演出海报，避免"海报张冠李戴"复发）

**P2 带娃进场（ledger 4条）**
1. 2 岁就要票 — 官网 FAQ：2 岁及以上进场要票，且必须坐在自己票上的座位；面向儿童的场次年龄规则可能不同，以场次页与票面条款为准
2. 2 岁以下不建议带 — 官网原话：不建议 2 岁以下儿童来看现场，音量很大、需要适当护耳；耳塞可在 Level 2 客服台购买（该条 FAQ 仍用旧名 ICC Sydney Theatre，指同一座馆）
3. 婴儿车不进座位区 — 为保持通道畅通，演出期间婴儿车须寄存在该场次指定位置；寄存点每场可能不同，先看场馆活动邮件或到场问引导员
4. 育婴室在 Level 2 — 官网给的配置：喂奶区、换台、备餐区
- 收尾: 娱乐类场次的寄存处在场馆外侧 Tumbalong Boulevard 或 Moriarty Walk，过安检之前就能把违禁物品放掉。
- 底部条: 来源 iccsydney.com.au — Event FAQs

**P3 场内这四条（ledger 4条）**
1. 全场不收现金 — 官网原话 ICC Sydney is a cashless venue：餐饮亭、咖啡、停车、周边只收 eftpos，且明确写明不收支付宝和微信支付
2. 能用什么付 — 主流信用卡、借记卡，以及 Apple Pay／Google Pay／Samsung Pay（手机与手表）
3. 水瓶不能带进场 — 这是 TikTok Entertainment Centre 与 Darling Harbour Theatre 娱乐场次的入场条件；每个吧台有免费水和可降解杯，零售点有瓶装水卖
4. 急救室两处 — Level 2（Door 1 旁）与一楼；遗失物品活动期间在 Level 2 客服台，散场后转到安保办公室
- 收尾: 可以在自己票位前站着跳，但官网明写不许站在座椅上——带小孩的尤其注意这条。
- 底部条: 场内规则 — 以该场次条款为准

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 2 岁那张票 / 别漏了
- 正文: 2 岁要票、婴儿车要寄存、现金用不了、水瓶带不进——出门前先存好这份清单。
- CTA: 评论区扣 1，私信发你这份带娃看演出清单，还有后续开票提醒。
- 底部条: VOL. 067 — 简介里有完整演出日历

## 事实核查表

信源代号：
**A** = https://iccsydney.com.au/about/venue-information/faqs/event-faqs （ICC Sydney 官方 Event FAQs，2026-10-31 抓取，页面 `article:modified_time` 2026-06-01）
**B** = https://iccsydney.com.au/visit/getting-here （ICC Sydney 官方 Getting Here & Parking，2026-10-31 抓取）
**C** = https://www.tiktokentcent.com/ （场馆官方站，2026-10-31 抓取）

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | 场馆现用名为 TikTok Entertainment Centre | GREEN | C（官方站站名与页面标题即此名）；A 全页多处以该名指称该馆 |
| 2 | 该馆是 ICC Sydney 三座建筑之一（与 Convention Centre、Exhibition Centre 并列） | GREEN | A 原文 "ICC Sydney offers complimentary cloaking to all guests to the Convention Centre, Exhibition Centre and TikTok Entertainment Centre."；A 急救室条目亦三馆并列 |
| 3 | ICC Sydney 位于达令港，地址 14 Darling Drive, Sydney NSW 2000 | GREEN | B 原文 "ICC Sydney is located at 14 Darling Drive, Sydney NSW 2000, in the heart of the Darling Harbour precinct." |
| 4 | 2 岁及以上进场需要票，且必须坐在自己票上的座位 | GREEN | A 原文 "Children 2 years of age and older require a ticket to enter TikTok Entertainment Centre and must occupy their ticketed seat." |
| 5 | 部分场次（尤其面向儿童的）年龄规则不同，以场次页与票面条款为准 | GREEN | A 原文 "Some shows (especially those intended for children) will have a different age policy. Please see the specific event page and ticket conditions for further information." |
| 6 | 官网不建议 2 岁以下儿童参加现场活动，原因是音量强、需要适当护耳 | GREEN | A 原文 "We do not recommend children under the age of 2 attend live events at ICC Sydney as there are strong noise levels and they will require appropriate protection." |
| 7 | 耳塞可在 Level 2 的客服台购买（该条 FAQ 仍写旧名 ICC Sydney Theatre） | GREEN | A 原文 "Should you wish to purchase earplugs for an event at ICC Sydney Theatre, they are available for purchase at the Customer Service Desk on Level 2."（旧名出现在官网原文，文案已如实标注） |
| 8 | 演出期间婴儿车不得进入座位区，须寄存在该场次指定位置 | GREEN | A 原文 "In order to keep aisles clear, prams are not permitted in the seating area during live events, and must be cloaked in the allocated location for the event." |
| 9 | 婴儿车寄存位置每场可能不同，应提前看场馆活动邮件或到场问引导员 | GREEN | A 原文 "Pram cloaking locations may change per event, so please ensure to read the event communications (email) from the venue prior to arrival, or check with our friendly ushers upon arrival." |
| 10 | 娱乐类场次的寄存处在场馆外侧 Tumbalong Boulevard 或 Moriarty Walk，以便在过安检前寄存违禁物品 | GREEN | A 原文 "TikTok Entertainment Centre cloak room is located externally on Tumbalong Boulevard or Moriarty Walk to enable prohibited items to be cloaked prior to passing through security." |
| 11 | 该馆育婴室在 level two；育婴室配置为喂奶区、换台、备餐区 | GREEN | A 原文 "ICC Sydney has accessible parenting rooms equipped with a feeding area, change table and food preparation area." + 位置列表 "TikTok Entertainment Centre: level two" |
| 12 | 全场无现金，餐饮亭／咖啡／停车／周边均只收 eftpos | GREEN | A 原文 "ICC Sydney is a cashless venue. We accept payment via eftpos only for all services including food and beverage kiosks and cafes, parking and merchandise outlets." |
| 13 | 不收支付宝与微信支付 | GREEN | A 原文 "The venue does not accept alipay or wechat pay."（EFTPOS 条目亦重复一次："The venue does not accept Alipay or WeChat Pay."） |
| 14 | 可用主流信用卡、借记卡与 Apple Pay／Google Pay／Samsung Pay（手机／手表） | GREEN | A 原文 "Major credit cards, debit cards and mobile/watch pay (apple pay, google pay and samsung pay) are accepted." |
| 15 | 水瓶不得带入场馆（TikTok Entertainment Centre 与 Darling Harbour Theatre 娱乐场次的入场条件） | GREEN | A 原文 "As a condition of entry to TikTok Entertainment Centre and Darling Harbour Theatre for live events, water bottles are not permitted into the venue." |
| 16 | 每个吧台提供免费水与可降解杯；场内零售点有瓶装水出售 | GREEN | A 原文 "Free water and biodegradable cups are available at every bar, and bottled water is available for purchase at all retail kiosks in the Entertainment Centre."（Responsible Service of Alcohol 条亦写 "Free drinking water is available at every bar."） |
| 17 | 该馆急救室两处：level two（Door 1 旁）与 ground floor | GREEN | A 原文 "TikTok Entertainment Centre: level two (next to Door 1) and ground floor." |
| 18 | 遗失物品活动期间在 Level 2 客服台，活动结束后转到安保办公室 | GREEN | A 原文 "All lost property is held at the Customer Service Desk, level 2 during an event. After an event all lost property will be located in our security office." |
| 19 | 允许在自己票位前站立／跳舞，但不允许站在座椅上 | GREEN | A 原文 "patrons are allowed to stand/dance in front of their ticketed seat only… Standing on seats is not permitted at TikTok Entertainment Centre." |

**主动排除项（查得到但按红线／信源纪律不写）**：

- **改名日期**（020 当时引用的官方 FAQ 原句 "ICC Sydney Theatre officially became TikTok
  Entertainment Centre on 25 November 2025." 已不在现版 FAQ 页上）：本篇只写"现用名"与
  "官网个别条目仍用旧名"，不再复述一个今天在官网上复核不到的日期。二手媒体有这个日期，
  但不作为账号口径。
- **座位容量数字**（8,000／9,000 两说）：只见于二手聚合站且互相打架，官方页未给，不写。
- **任何具体演出的日期／票价／开演时间／购票平台**：该馆在 verified 池里唯一条目
  （AKMU 悉尼站 2026-09-20）已过期，`price`／`time` 为 `null`，按红线一律不写。
- **儿童票价、是否有儿童／家庭折扣**：官网未给，不写。
- **婴儿车寄存的具体位置**：官网明写"每场可能不同"，不给固定答案。
- **ATM 位置／场内能不能取现**：官方 FAQ 无此条，不补。
- **场内餐饮菜单与价格、信用卡休息室权益**：非场馆官方口径或与观演规则无关，不写。
- **各交通方式到馆的步行分钟数细节**：属 040 已覆盖的范围，本篇不重复、也不新增官网未给的数字。

FACT-AUDIT-STATUS: RED=0 CHECKED=19 SOURCES-CITED=19

## 渲染状态

- 模板: `cards/067/index.html`，复制自 `cards/061/index.html`。选 061 作为基底的原因：它是
  最近一份**正好 4 张、纯文字无演出海报**的场馆攻略，已带全部已验证修正（`.ledger-note`
  内联 `max-width:460px` 约束、无 `frame-img` 配图版式），本篇同为无海报纯文字选题、同样
  4 张卡，只需替换 4 个 poster 区块内文案与 `<title>`。`<html data-theme="aushow">`、主题色
  token、字体、`.ticket`/`.ledger`/`issue-strip` 组件样式、WebGL 背景脚本全部原样保留。
- 卡片数: 4 张 `<section class="poster xhs" id="xhs-01…04">`
- 渲染: 交由 `automation/render_card.py`（headless Chrome 逐张截图 + PIL 校验 1080×1440）。
  本次会话按 daily-xhs-prompt 第 0 节要求，未调用任何浏览器/截图工具。
