# 071 — 周六 ENGIE，8:30 后进不去（场馆攻略）

**选题类型**：场馆攻略（周三轮换位，2026-11-18 生成）
**场馆选择**：ENGIE Stadium（悉尼 Sydney Olympic Park）——`data/events.json` 中
`verified=true` 条目「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」的 `venue`
（`"ENGIE Stadium (Sydney Olympic Park)"`，`date=2026-11-21`）。

**⚠️ 本篇是对 055 确立的「最久没被写过」取法的一次有意偏离，理由与补偿如下**：
按该取法，8 座 verified 场馆上次被写时间为 **Margaret Court Arena(043, 10-03, 46 天前)**
／Chippo(047, 10-07)／Club Voltaire(050, 10-10)／Marvel(055, 10-17)／Palais(058, 10-21)
／Sydney Event Centre(061, 10-24)／ENGIE(064, 10-28, 21 天前)／TikTok Ent Centre(067, 10-31)
——**轮到的是 Margaret Court，本篇取的是排序倒数第二的 ENGIE**。偏离理由：
**周杰伦悉尼站就在 3 天后（11-21 周六），它是 8 条 verified 里唯一演出日仍在未来的一场**；
11-21 一过，整个池子将全部变成"演出日已过"的 evergreen 素材，**这是本号最后一次能发
"三天后那场"的场馆攻略**。Margaret Court 的锚点演出（AKMU 09-18）已过去两个月，写它
只能是 evergreen，不存在时效损失。**轮换欠账记录：Margaret Court Arena 仍是最久未写
（下一次场馆攻略应优先取它，除非届时又有新的近期 verified 演出）。**

**⚠️ 本篇还遇上一次 10-16 日的停更空窗**：`automation/logs` 显示 11-05 → 11-16 连续 12 天
`Failed to authenticate: OAuth session expired`，11-17 那次写出了 070 文案但卡在建卡片 HTML
（session limit）。本号上一次成功推送是 069（11-03）。详见文末「值班发现」。

**角度（与 008／037／064 三篇 ENGIE 前作零重叠）**：
- 008（08-26）＝**怎么到／怎么进**（交通四条 + 包限 A4、cashless、旗帜 1m×1m、电子烟、外带食物），
  依据是场馆通用 `conditions-of-entry` 与 `getting-here`；
- 037（09-26）＝**散场之后怎么回**（火车加开、出租点、渡轮别赌、封路改道），依据 Transport NSW；
- 064（10-28）＝**无障碍观演**（安静室、感官包、pass out、避开楼梯的排号、Metrasens），
  依据场馆 FAQ 的 Accessibility 段 + 无障碍 PDF。

本篇的主线是前三篇都没问过的一个问题：**你查到的那页规矩，到底是不是写给你这场的。**

ENGIE 的官方 FAQ 页上，**8 个答案逐字写着 "For concerts and special events, please contact
the venue."**（热饮保温杯／外带食物／保温箱／周边售卖／祈祷室／急救点／育婴室／寄存处），
**pass out 那条另写 "Pass outs vary per event. Please contact the venue to confirm."**
——合计 **9 个问题，官网对"演唱会"一概不作答**。那页能查到的答案，几乎都是**按球赛模式
（24,000 座）写的**；周杰伦这场是**演唱会模式（46,500 座）**，是另一套规矩。

而答案其实是有的：场馆给这一场**单开了一页官方活动页**，上面那 9 个问题里最要命的几个
（pass out／年龄／时间／随身物品）全部有明确答案，**并且有两条与 FAQ 页给的球赛版答案
正好相反**。本篇就是把那一页讲清楚。

**🔴 本次核查发现：064 的两条建议对这一场已失效（需用户裁决是否追注）**
064 写的是"安静室在 **Grand Parade**、在球场范围之外，**出去之前先拿 pass out**"（依据
FAQ 页，属球赛模式）。周杰伦这一场的官方活动页写的是：安静空间设在 **Members Stand 后方
的外围 concourse**，且 **"Pass outs are not permitted"**。
→ 若 064 已发布，按 064 的说法去领 pass out 的读者**这场会被卡在门外**。已追加
`EXCEPTIONS.md`，由用户裁决是否给 064 追一条评论／改图。**这正是本篇主线的最好例证。**

**与 060／065 两次"主动挂起"的接续（必须说明的一条口径）**：
060（10-23，单场安利）与 065（10-29，开票汇总）都查到了同样这几行时间，但**都主动剔除
未写**，理由记录为"入场须知类，`events.json` 无字段"。那两篇的判断在**它们自己的选题下
是对的**——安利／汇总篇的纪律是"只用 JSON 里实际有的字段"。但提示词对**场馆攻略**的要求
是另一条："场馆本身的客观信息……只写你能通过 WebSearch 核实到官方信息的内容"，008 当年
正是据此写了包限 A4／cashless／旗帜尺寸等整套入场须知并通过核查。**入场须知属于场馆攻略
的本职范围，红线禁的是"编"（`不要自己编一句放上去`），不是禁"官方页上逐字查到的"。**
本篇全部时间与规则均来自场馆官方活动页逐字引用、附 URL，且保留官方自注的
"Times are subject to change"。→ 060／065 挂起的那条线，在它该出现的选题里补上了。

**信源纪律**：全篇只用 `sydneyshowground.com.au`（场馆官方站）四个页面，**均为 2026-11-18
当日 Firecrawl `maxAge:0` 实时抓取、HTTP 200**；演出日期／场馆／开演时间同时与 `events.json`
的 `verified=true` 条目逐字比对一致。凡两处官方口径打架的一律不写（见末尾"主动剔除项"）。

**红线自查**：涉及单场演出的断言（日期／场馆／开演时间）逐字取自 `events.json` 的
`verified=true` 条目并经官方页二次确认；**不写票价／购票平台／限购／主办方**（非本篇主题）；
未引用任何未核实演出；不点名任何个人／账号。

## 标题（16字）

周六ENGIE，8:30后进不去

## 正文（发帖文案，无外链）

11 月 21 日周六，周杰伦悉尼站在 ENGIE Stadium（Sydney Olympic Park）。

先说一件很多人不知道的事：**你在场馆官网 FAQ 上查到的规矩，多半不是写给这场的。** 那页上有 8 个答案原文写着"演唱会与特别活动请联系场馆"，pass out 那条写的是"每场不同，请联系场馆确认"——**9 个问题，对演唱会一概没答**。那页能查到的，基本都是按球赛模式写的；周杰伦这场是演唱会模式，另一套规矩。

真正管你这一场的，是场馆给这场**单开的那一页官方活动页**。下面全部从那页来 👇

⏰ **最后入场 8:30pm**。6:00pm 开闸、7:30pm 开演、10:30pm 结束。迟到不是"少听几首"的问题——**8:30 之后是进不去的**。（官方自注：时间可能调整）

🚫 **这场不许中途出去再进来**。官方原话 "Pass outs are not permitted"。出去买杯奶茶、回车上拿件外套再进来，这场不行——**FAQ 页上那条"每场不同"，到这一场的答案是"不行"。**

👶 **6 岁以下不得入场**。6 岁及以上每人都要一张有效票，**没有儿童优惠票**；14 岁及以下必须全程有家长或法定监护人陪同，同样要票。

🪧 **应援物有三条尺寸线**。包不能大于 A4、**所有背包一律不行**；标语和海报大于 A3 不行；**非官方灯牌、自拍杆也不行**。出门前拿张 A4 纸比一比最稳。

🌻 **需要安静空间的，位置和平时不一样**。这场的安静空间设在 **Members Stand 后方的外围 concourse**（认向日葵旗子）；**Gate A 和 Gate D 里面的咨询台**可以免费领 Hidden Disabilities 向日葵挂绳，另有**少量含耳机的感官包**可以借（需登记）。

还有两条顺手的：**不许提前排队过夜**，官方明说会请人离开；开车的话官方建议 **Olympic Blvd 上下客**，停车要**提前在线订**，**活动前一晚 11:59pm 截止或订完即止**。

评论区扣 1，私信发你这份 ENGIE 周六入场清单，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#周杰伦 #悉尼演唱会 #澳洲华人 #演唱会情报

## 卡片文案结构（4张，票根美学）

**P1 封面**
- kicker: 场馆攻略 · ENGIE Stadium
- 大字标题: 8:30 之后 / 你就进不去了
- 副标题: 官网那页 FAQ，不是写给这场的
- 说明: 周六周杰伦悉尼站。场馆 FAQ 有 9 个问题对演唱会不作答——答案在这场单开的官方活动页上。
- 底部条: 悉尼 Sydney Olympic Park — 11.21 周六

**P2 票根组件**
- 演出: 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会
- 日期: 21 NOV 2026 ｜ 状态徽章: ON SALE 开票中
- 场馆: ENGIE Stadium（悉尼 Sydney）
- 时间: 19:30
- 时间轴条: 18:00 开闸 · 19:30 开演 · 20:30 最后入场 · 22:30 结束

**P3 入场须知（ledger 4条）**
1. 8:30pm — 最后入场，之后进不去（时间可能调整）
2. 不给 pass out — 中途出场不能再进
3. 6 岁以下 — 不得入场；6 岁以上每人一票，无儿童票
4. A4 / A3 — 包不过 A4、背包全不行；标语海报不过 A3；非官方灯牌、自拍杆不行
- 收尾: 官网 FAQ 上那 9 个"请联系场馆"的问题，答案都在这场自己的活动页上。
- 底部条: 全部取自场馆官方活动页 — 出发前再核一眼

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 你查的那页 / 是写给这场的吗？
- 正文: 评论区扣 1，私信发你这份 ENGIE 周六入场清单，还有后续开票提醒。
- 底部条: VOL. 071 — 简介里有完整演出日历

## 事实核查表

**信源**（均为 2026-11-18 当日 Firecrawl `maxAge:0` 实时抓取，HTTP 200）
- **A** = 场馆官方本场活动页 `https://www.sydneyshowground.com.au/whats-on/jay-chou-carnival--world-tour/`
- **B** = 场馆官方 FAQ 页 `https://www.sydneyshowground.com.au/engie-stadium/engie-stadium-faqs/`
- **C** = 场馆官方入场条款 `https://www.sydneyshowground.com.au/conditions-of-entry---sydney-showground--engie-stadium/`
- **D** = 场馆官方 What's On 列表 `https://www.sydneyshowground.com.au/whats-on/?EventVenueId=22581`
- **E** = 本仓库 `data/events.json`，`verified=true` 条目「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | 演出日期 2026-11-21，为周六 | GREEN | **E** `date="2026-11-21"`；**A**／**D** 同页逐字 "Saturday 21 November" |
| 2 | 场馆为 ENGIE Stadium（悉尼 Sydney Olympic Park） | GREEN | **E** `venue="ENGIE Stadium (Sydney Olympic Park)"`；**A** "returns to ENGIE Stadium, Sydney Showground" |
| 3 | 开演 19:30 | GREEN | **E** `time="19:30"`；**A** 逐字 "7:30pm – Event starts"（两源一致） |
| 4 | 6:00pm 开闸 | GREEN | **A** 逐字 "6:00pm – Gates open" |
| 5 | 8:30pm 最后入场 | GREEN | **A** 逐字 "8:30pm - Final Entry" |
| 6 | 10:30pm 结束 | GREEN | **A** 逐字 "10:30pm – Event finishes" |
| 7 | 官方自注上述时间可能调整 | GREEN | **A** 逐字 "*Times are subject to change" |
| 8 | 本场不提供 pass out（中途出场不可再入） | GREEN | **A** 逐字 "Pass outs are not permitted" |
| 9 | FAQ 页对 pass out 的答案是"每场不同、请联系场馆确认" | GREEN | **B** 逐字 "Pass outs vary per event. Please contact the venue to confirm." |
| 10 | FAQ 页有 8 个答案逐字写"演唱会与特别活动请联系场馆" | GREEN | **B** 逐字 "For concerts and special events, please contact the venue." 共 8 处：热饮保温杯／外带食物／保温箱(esky)／周边售卖／祈祷室／急救点／育婴室／寄存处（本次会话逐条点数） |
| 11 | 连同第 9 条合计 9 个问题官网对演唱会不作答 | GREEN | **B** 8 处（#10）+ pass out 变体 1 处（#9）= 9 |
| 12 | FAQ 可查答案多为球赛模式；球赛 24,000 座、演唱会 46,500 座 | GREEN | **B** 逐字 "24,000 in sport mode or up to 46,500 in concert mode"；多条答案以 "For sporting events…" 起句 |
| 13 | 场馆为本场单开官方活动页 | GREEN | **A** 本身即该页；**D** 列表链接指向该页 |
| 14 | 6 岁以下不得入场 | GREEN | **A** 逐字 "Children under 6 years old are not permitted at this event." |
| 15 | 6 岁及以上须持有效票，且无儿童优惠票 | GREEN | **A** 逐字 "Children aged 6 and above must have a valid ticket for admission. No concession tickets will be available for children." |
| 16 | 14 岁及以下须家长或法定监护人全程陪同并持有效票 | GREEN | **A** 逐字 "Children 14 and under must be accompanied by a parent or legal guardian at all times and have a valid ticket" |
| 17 | 大于 A4 的包及所有背包不得入场 | GREEN | **A** 逐字 "bags over A4 size and all backpacks are not permitted"；**C** 第 2.16 条 "Backpacks & bags larger than A4 are not permitted for concerts, dance parties & festivals." |
| 18 | 大于 A3 的标语或海报不得入场 | GREEN | **A** 逐字 "Signs or posters larger than A3" 列于 not permitted |
| 19 | 非官方灯棒／灯牌不得入场 | GREEN | **A** 逐字 "Unofficial light sticks" 列于 not permitted |
| 20 | 自拍杆不得入场 | GREEN | **A** 逐字 "Selfie sticks" 列于 not permitted |
| 21 | 禁止为本场排队过夜／露营，会被要求离开 | GREEN | **A** 逐字 "camping for this show is strictly prohibited. Any patrons queuing / camping will be asked to move on." |
| 22 | 官方建议 Olympic Blvd 为上下客地点 | GREEN | **A** 逐字 "Olympic Blvd is the recommended drop off and pick up location for the event" |
| 23 | 停车须提前在线预订，活动前一晚 11:59pm 截止或售完即止 | GREEN | **A** 逐字 "pre-book your parking online – available until 11:59pm the night before the event, or until sold out." |
| 24 | 本场安静空间设于 Members Stand 后方外围 concourse，认向日葵旗 | GREEN | **A** 逐字 "The quiet space will be operational on the outer concourse behind Members Stand (Look out for the Sunflower flags!)" |
| 25 | Gate A 与 Gate D 内咨询台可免费领 Hidden Disabilities 向日葵挂绳 | GREEN | **A** 逐字 "collect a free Hidden Disabilities Sunflower Lanyard from our information desks located inside Gate A & D" |
| 26 | 另有少量含耳机的感官包可借出（需登记） | GREEN | **A** 逐字 "a limited number of sensory bags (including headphones) available to sign out"；**B** 领取须留 ID 与姓名电话 |

FACT-AUDIT-STATUS: RED=0 CHECKED=26 SOURCES-CITED=26

**主动剔除项（不计入核查表，仅记录）**
- **出租车排队点位置**——**B** 写 "closest taxi rank is located near the Novotel Hotel on
  Herb Elliot Ave"，而 037 当时据 Transport NSW 官方页写的是 "Pullman Hotel 旁边"。
  **两处官方口径不一致，按本栏目纪律一律不写。**（037 旧稿是否需更正，一并记入 EXCEPTIONS）
- **停车价格**——沿用 064 的处置：同一官网内 `$8/hr、$40/day` 与 `$7/hr、$35/day` 两套数字
  打架，**本篇只写"要提前订、前一晚 11:59 截止"，不写任何金额**。
- **cashless／接水站／Metrasens 安检门／旗帜 1m×1m／电子烟** —— 008 与 064 已写，本篇不复述。
- **无障碍订座排号、Companion Card、轮椅协助流程** —— 064 主线，本篇只写本场活动页上
  **与 064 不同**的那两条（安静空间位置、pass out），不展开无障碍全套。
- **禁带物品图与座位图** —— **A** 上以图片形式给出（`prohibited-items-_-engie.png`、
  `engie_stadiummap_jaychou.png`），**图片内容无法以文本逐字核实，一律不转述**。
- **同日同园区另有 Source Disability Expo（11/20–11/21）** —— **D** 可见，但该展与本场
  是否共用停车／是否影响交通，官网无任何说明，**不作任何推断**。
- **票价／购票平台／限购／主办方** —— 非本篇主题，且属安利篇范围。

## 值班发现（非内容问题，需用户处理，已同步 EXCEPTIONS.md）

1. **11-05 → 11-16 连续 12 天自动化失败**：`automation/logs/` 每天都是
   `Failed to authenticate: OAuth session expired and could not be refreshed`。
   这 12 天**一篇未产出**，直接冲击宪法里"每周至少实际发布 3 篇"的硬前提。
2. **070 是个孤儿**：11-17 那次写出了 `content/070-xhs-copy.md`（防骗指南，
   `FACT-AUDIT-STATUS: RED=0 CHECKED=20 SOURCES-CITED=20`，内容完整），但在建卡片 HTML
   前撞上 session limit，**`content/cards/070/` 不存在，从未渲染、从未推送、
   posted-log 与 RUNBOOK 都没有它的行**。因 `run_daily_xhs.sh` 只渲染"本次运行新增的文件"，
   **070 不会被今天这次运行捡起来，需要人工补建 HTML 后手动渲染**。
3. **posted-log 缺 063／069／070 三行**（063、069 内容与卡片均存在且已推送，只是漏登记）。
4. **064 的 pass out 建议对 11-21 这场失效**（见上文 🔴），需裁决是否追注。
5. **时钟已到期**：AuShow 杀死标准 **2026-11-08 到期，今日 11-18 已逾期 10 天**，尚未裁决。
6. **`PORTFOLIO.md` 最后评审 2026-09-06，已 73 天**，远超 14 天节律。

## 渲染状态

- 模板: `cards/071/index.html`（复制 `cards/001/index.html`——保留 `<html data-theme="aushow">`、
  文件顶部全部 aushow 主题色 token、整体 CSS 结构与字体，以及 `.ticket`／`.ledger`／
  `issue-strip` 等已验证组件样式，仅替换 4 个 `<section class="poster xhs">` 区块内的文案；
  `<title>` 已改为 071）
- 4 张卡，`id` 为 `xhs-01`…`xhs-04` 连续编号；本篇为场馆攻略，**P1 不放演出海报配图**
  （沿用 004／008／064 等全部场馆攻略前作的处理，避免用艺人宣传图给场馆攻略做封面）
- P2 在既有 `.ticket` 组件下方新增一行时间轴，**复用既有 `.tk-field-lbl`／`.tk-field-val`
  类，未新增任何 CSS 规则**
- 输出: 由 `automation/render_card.py` 在本次会话结束后渲染为
  `cards/071/output/xhs-071-01.png` ~ `xhs-071-04.png`，均 1080×1440
- 渲染不在本次对话内进行（2026-08-16 起的既定分工：chrome-devtools-mcp 截图不可靠，
  渲染交由确定性脚本 `render_card.py` 完成）
