# 048 — 都是 7 点半开演，差在星期几（本周开票汇总）

**选题类型**：本周开票汇总（周四轮换位，2026-10-08 生成）

**信源条目**（全部 `data/events.json` → `verified=true`，共选 3 场）：
1. 周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会（2026-10-17 周六，Ticketmaster）
2. 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会（2026-11-21 周六，Ticketmaster）
3. Rolling Donkey 中文喜剧开放麦（悉尼，每周二，Eventbrite）

**本篇口径决定（先说清楚）**：

- **沿用 005/009/014/021/028/035/041 的"不说'本周开票'"口径。** 3 条 `status` 都是 `on_sale`
  （已在售），`events.json` 里没有任何字段支持"这些票是本周开售的"。栏目定位保留（仍记为
  "本周开票汇总"），标题/卡面一律用"在售""官方票面"这类可核实的表述。

- **角度与前七篇刻意错开，这是第 8 种切分：按 `time` 字段 + 星期几分。**
  005=时间线、009=提前量（大场 vs 常驻）、014=城市、021=票价档位、028=倒计时、035=官方购票
  平台、041=档期月份——七篇都没有用过 **`time`（开演时间）**这个字段当组织原则，也没有一篇
  按**星期几**切过。本篇的新事实是：**3 场的 `time` 全部是 19:30，一分不差**，差别全在落到
  星期几上——**两场周六（10-17 / 11-21）＋ 一场每周二**。落点是"同一个 7 点半，占掉的是你
  哪一天"：周六那两场不用动工作日，代价是提前量（9 天 / 44 天）和可能的跨城住宿；周二那场
  动的是工作日晚上，但零提前量、散场就在市区。

- **星期几是 `date`/`recurrence` 字段的纯推导，非新编造**（本地 `date` 计算）。倒计时随生成日
  更新：5 天（下周二 10-13）/ 9 天（10-17）/ 44 天（11-21）。

- **本篇首次拿到"两站官方场馆页同时确认 19:30"。** 035/041 记录过一个悬着的分歧：Marvel
  Stadium 官方页曾标 7:00 pm，与 `events.json` 的 19:30 打架（当时判为开门时间，采信 19:30）。
  今日复核，Marvel Stadium 官方公告页写的是 **"Time: 7:30 PM"**，Sydney Showground 官方场次页
  写的是 **"7:30pm – Event starts"**——两站官方口径都站到 19:30 这一边，该分歧消解。这一条对
  本篇特别重要，因为 `time` 正是本篇的组织主线。

**排除项摘要**：

- **袁娅维 TIA RAY 墨尔本站（08-20）/ 悉尼站（08-22）**——`verified=true` 但演出日期早于生成日，
  已开演，不进"接下来能买"的清单。
- **AKMU 乐童音乐家 墨尔本站（09-18）/ 悉尼站（09-20）**——演出日均已早于生成日（已开演），且
  仍挂 `EXCEPTIONS.md` OPEN（墨站 `ticket_platform` 失真、悉站 `venue` 旧名 + `price`/`time`
  null）。双重原因不收。`time` 为 null 这一点在本篇尤其致命——`time` 是本篇主线，收进来会在
  主线上开洞（同 021 对 `price=null` 的处理）。
- **候场喜剧 Loadingzone Comedy（墨尔本，常驻）**——"常驻开放麦 · on_sale"自 09-14 起无法在
  Eventbrite 主办方页核实到当前场次（OPEN），本轮整条不列。**不点名**，正文只写通用原则。

**红线自查**：3 条全部 `verified=true`；日期/时间/场馆/票价/平台逐字取自 JSON 字段；`price` 为
null 的 Rolling Donkey 不编造票价；**开门/检票/散场时间一律不写**（账号红线明确点名"检票时间"
属不可自行添加项，即使官方页今日列出了也不写进来）；正文无外链；未点名任何个人/账号/转售平台。

## 标题（13字）

都是7点半开演，差在星期几

## 正文（发帖文案，无外链）

这周的华人演出在售清单还是 3 场。今天换个切法：**不按日期排，按星期几排**。

因为我核对字段的时候发现一件挺巧的事——**这 3 场的开演时间一分不差，全是晚 7:30**。真正不一样的，是它落在你哪一天 👇

**【周六 ×2】不用动工作日，但要提前锁**

🌸 **10-17 周六 晚7:30** · 墨尔本
周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会
Marvel Stadium，官方票面 $208–$748（另加 $9.90 手续费）。**只剩 9 天**，跨城看的，机票住宿现在不订就是在赌。

🌊 **11-21 周六 晚7:30** · 悉尼
周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会
ENGIE Stadium (Sydney Olympic Park)，官方票面 $188–$748（另加 $9.90 手续费）。还有 44 天，时间宽裕，但别等到最后两周才看住宿。

📌 两场周六中间隔了整整 5 周，**这期间没有第二场周六的大场**。也就是说，周六这个"不用请假"的名额，近期就这两次。

**【周二 ×每周】动的是工作日晚上，但零提前量**

🐴 **每周二 晚7:30** · 悉尼
Rolling Donkey 中文喜剧开放麦
Chippo Hotel（87-91 Abercrombie St, Chippendale），官方未标价。同样是 7:30 开场，这个不用提前 9 天也不用提前 44 天——**下周二就是 10-13**，下班过去就行，散场还在市区里。

📌 老规矩：只列逐字核实过的。两站周杰伦都是 Ticketmaster 官方规则每人最多 6 张；官方票面最高一档就是 $748——超过这个数的"内部渠道""前排锁位"，多出来的钱不会变成更好的座位。

评论区扣 1，私信发你这份按星期几排好的清单和官方票价档位，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #悉尼 #墨尔本 #周杰伦 #开放麦 #演唱会情报 #留学生活

## 卡片文案结构（3张，票根美学）

> 张数说明：本篇是"按星期几切分的清单"结构，3 场各一行、字段密度接近（都有开演时间+日期/
> 周期+城市+场馆，两场有票价、一场未标价），合进一张 ledger 即可，星期几放进 ledger 的 title
> 列作为切分主线。封面与 CTA 是账号固定品牌结构。与 028/035/041（同为 3 场清单）同为 3 张，
> 不硬凑空卡。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 在售清单 · 按星期几排
- 大字标题: 都是 7:30 开演 / 差在星期几
- 副标题: 周六 ×2 · 每周二 ×1
- 说明: 3 场在售演出的开演时间一分不差，全是晚 7:30。差别在于它占掉你哪一天。
- 底部条: 现在都在售 — 3 场 · 悉尼 & 墨尔本
- 配图: 无（汇总篇涉及多组演出方，挂任一张海报都有"张冠李戴"风险，整篇不挂图；沿用 004/005/008/009/014/021/028/035/041）

**P2 在售清单（ledger 3条）**
- kicker: 同一个 7:30 · 不同的那一天
- 大字标题: 周六两场 / 周二每周
1. 周六 — 10.17 · 19:30 · 周杰伦「粉色 墨尔本 嘉年华Ⅱ」· Marvel Stadium · $208–$748（另加 $9.90 手续费）· 还剩 9 天
2. 周六 — 11.21 · 19:30 · 周杰伦「海洋 悉尼 嘉年华Ⅱ」· ENGIE Stadium (Sydney Olympic Park) · $188–$748（另加 $9.90 手续费）· 还有 44 天
3. 周二 — 每周 · 19:30 · 悉尼 · Rolling Donkey 中文喜剧开放麦 · Chippo Hotel，87-91 Abercrombie St, Chippendale · 官方未标价 · 下周二 10.13
- 收尾: 两场周六中间隔 5 周，没有第二场周六大场。两站周杰伦都是 Ticketmaster 官方每人最多 6 张，票面最高一档就是 $748。
- 底部条: 官方票面是唯一标准 — 别的入口先问一句
- 版式说明: ledger-row 网格沿用 021/028/035/041（`96px 1fr auto`，note 占 460px 后 title 列剩约
  300px）。title 列放星期几标签（周六/周六/周二，均为 2 个汉字，是历次汇总篇里最短的 title 值，
  确定不折行），完整演出名/场馆/票价/倒计时放进 note，避免 42px 标题折行。

**P3 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 周六的名额 / 近期只有两次
- 正文: 评论区扣 1，私信发你这份按星期几排好的清单和官方票价档位，还有后续开票提醒。
- 底部条: Vol. 048 — 简介里有完整演出日历

## 事实核查表

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | 3 场的开演时间全部为 19:30（本篇主线） | GREEN | `data/events.json` 三条目 `time` 字段逐一比对：墨站 `"19:30"`、悉站 `"19:30"`、Rolling Donkey `"19:30"`，三者相同 |
| 2 | 演出名「周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | 同条目 `title_zh`，`verified=true`，逐字复制 |
| 3 | 墨尔本站 2026-10-17 是周六 | GREEN | 同条目 `date="2026-10-17"`；本地 `date` 计算 = Saturday；Marvel Stadium 官方公告页原文 "Date: 17 October 2026 (Saturday)" <https://www.marvelstadium.com.au/king-of-mandopop-jay-chou-announces-melbourne-show> |
| 4 | 墨尔本站 19:30 开演 | GREEN | 同条目 `time="19:30"`；同上官方公告页原文 "Time: 7:30 PM" |
| 5 | 墨尔本站场馆 Marvel Stadium、城市墨尔本 | GREEN | 同条目 `venue="Marvel Stadium"` / `city="墨尔本"`；同上官方公告页 "Venue: Marvel Stadium (Melbourne)" |
| 6 | 墨尔本站票价 $208–$748（另加 $9.90 手续费） | GREEN | 同条目 `price` 逐字复制（Ticketmaster 官方巡演页不列价，原文指向 "For Melbourne pricing refer to the venue event page"，与 009/021 的既有记录一致） |
| 7 | 墨尔本站平台 Ticketmaster、状态在售 | GREEN | 同条目 `ticket_platform="Ticketmaster"` / `status="on_sale"`；Ticketmaster AU 官方巡演页 "Melbourne … On Sale Now!" <https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666> |
| 8 | 墨尔本站距生成日 9 天 | GREEN | 生成日 2026-10-08 与同条目 `date` 计算：2026-10-17 − 2026-10-08 = 9 天 |
| 9 | 演出名「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` 该条目 `title_zh`，`verified=true`，逐字复制 |
| 10 | 悉尼站 2026-11-21 是周六 | GREEN | 同条目 `date="2026-11-21"`；本地 `date` 计算 = Saturday；Sydney Showground 官方场次页原文 "Saturday 21 November" <https://www.sydneyshowground.com.au/whats-on/jay-chou-carnival--world-tour/> |
| 11 | 悉尼站 19:30 开演 | GREEN | 同条目 `time="19:30"`；同上官方场次页原文 "7:30pm – Event starts" |
| 12 | 悉尼站场馆 ENGIE Stadium (Sydney Olympic Park)、城市悉尼 | GREEN | 同条目 `venue` / `city="悉尼"` 逐字复制；同上官方场次页场馆名 "ENGIE Stadium" |
| 13 | 悉尼站票价 $188–$748（另加 $9.90 手续费） | GREEN | 同条目 `price` 逐字复制（Ticketmaster 官方巡演页同样不列价，原文 "For Sydney pricing refer to the venue event page"） |
| 14 | 悉尼站平台 Ticketmaster、状态在售 | GREEN | 同条目 `ticket_platform="Ticketmaster"` / `status="on_sale"`；Ticketmaster AU 官方巡演页列 "Sydney … ENGIE Stadium, Sydney NSW"，`November 21, 2026` |
| 15 | 悉尼站距生成日 44 天 | GREEN | 生成日 2026-10-08 与同条目 `date` 计算：2026-11-21 − 2026-10-08 = 44 天 |
| 16 | 演出名「Rolling Donkey 中文喜剧开放麦(悉尼,每周二)」 | GREEN | `data/events.json` 该条目 `title_zh`，`verified=true`，逐字复制 |
| 17 | Rolling Donkey 每周二举行 | GREEN | 同条目 `recurrence="每周二"`；Eventbrite 售票页原文 "每周二 晚7:30" / "Time: Every Tuesday, 7:30 PM" <https://www.eventbrite.com/e/copy-of-rolling-donkey-tickets-1983189907399> |
| 18 | Rolling Donkey 19:30 开演 | GREEN | 同条目 `time="19:30"`；同上售票页 "晚7:30" / "7:30 PM" |
| 19 | Rolling Donkey 城市悉尼、场馆 Chippo Hotel，87-91 Abercrombie St, Chippendale | GREEN | 同条目 `city="悉尼"` / `venue` 逐字复制；同上售票页 "87-91 Abercrombie St (Chippo Hotel)"、"87-91 Abercrombie Street, Chippendale, NSW 2008"（沿用 011/047 对门牌 87-91 的采信口径） |
| 20 | Rolling Donkey 报名平台 Eventbrite、当前仍可购票 | GREEN | 同条目 `ticket_platform="Eventbrite"` / `status="on_sale"`；同上售票页今日仍为 "Multiple dates" + "Get tickets"（与 047 昨日 10-07 的实测结论一致） |
| 21 | Rolling Donkey 官方未标价 | GREEN | 同条目 `price=null`；同上售票页今日未显示任何票价，不编造票价 |
| 22 | "下周二就是 10-13"（距生成日 5 天） | GREEN | 生成日 2026-10-08 为周四 + 同条目 `recurrence="每周二"` 推算：下一个周二 = 2026-10-13；10-13 − 10-08 = 5 天 |
| 23 | 两站周杰伦都是 Ticketmaster 官方规则每人最多 6 张 | GREEN | 两条目 `notes="主办方 Sky Music & Horizon Production;每账户限购6张"`；Ticketmaster AU 官方巡演页原文 "You may purchase a maximum of 6 tickets per person."（两站同一规则） |
| 24 | 官方票面最高一档就是 $748 | GREEN | 两站 `price` 区间上端均为 $748 |
| 25 | "两场周六相隔 5 周，这期间没有第二场周六的大场" | GREEN | `verified=true` 且 `category="演唱会"` 的条目按 `date` 枚举：10-17 与 11-21 之间（含端点外）无其它演唱会条目——袁娅维×2（08-20/08-22）与 AKMU×2（09-18/09-20）演出日均早于生成日。两日期相差 35 天 = 整 5 周（本地 `date` 计算，两天同为周六） |
| 26 | "这周的在售清单还是 3 场"表述成立 | GREEN | `data/events.json` 中 `verified=true` 共 8 条，逐条排除后剩 3：袁娅维×2 演出日（08-20/08-22）已早于生成日；AKMU×2 演出日（09-18/09-20）已早于生成日且字段失真（`EXCEPTIONS.md` OPEN）；Loadingzone 常驻开放麦当前无法核实（OPEN）。剩 3 条 `status="on_sale"` 且字段可逐字核实 |
| 27 | 正文 CTA"评论区扣1私信"与"官方票价是唯一标准"防骗口径 | GREEN | 账号档案 `~/.claude/skills/xhs-content/accounts/aushow.md` CTA 模板 + 红线段，与已发布 001/005/009/014/021/028/035/041 同款表述一致 |
| 28 | 035/041 记录的"墨站官方页 7:00 pm vs 19:30"分歧，今日已消解 | GREEN | Marvel Stadium 官方公告页今日原文为 "Time: 7:30 PM"（见第 4 行同一 URL），与 `events.json` 的 `time="19:30"` 一致；Sydney Showground 官方页同样为 "7:30pm – Event starts"。两站官方口径均站 19:30，本篇主线 `time` 字段无失真 |

**主动排除项（无依据、依据冲突、瞬时状态、已过期或属账号红线点名的不可添加项，本篇一律不写）**：

- **开门时间 / 散场时间（gates 6:00pm、event finishes 10:30pm）**——两站官方页今日都列了这组
  时间（Sydney Showground "6:00pm – Gates open" / "10:30pm – Event finishes"，并自带
  "*Times are subject to change"；Marvel Stadium 社区信息页列 gates 6:00PM）。**但账号红线明确
  点名"检票时间""入场须知"属不可自行添加项，`events.json` 也无对应字段，故即使官方列出也不写
  进文案**，沿用 027/045 的既定处理。本篇主线只用 `time`（开演时间）这一个有 JSON 字段支撑的
  时间点。
- **二级市场价格（$178 / AU$353 / £219.81 等）**——来自 eventworld / hellotickets / stereoboard
  等转售或聚合站，均非官方票面，且与本账号"官方票价是唯一标准"的核心口径直接冲突。整组剔除，
  正文只写 `events.json` 的官方票面区间。
- **"Carnival" vs "Carnival II" 巡演名分歧**——Marvel Stadium 社区信息页把巡演写成 "Jay Chou
  'Carnival' World Tour"，官方公告页写 "Carnival II"。文案一律用 `events.json` 的 `title_zh`
  逐字复制，不引用任何英文巡演名，分歧不进文案。
- **袁娅维 TIA RAY 墨尔本站（08-20）/ 悉尼站（08-22）**——`verified=true` 但演出日期早于生成日
  2026-10-08，已开演，整组剔除。
- **AKMU 乐童音乐家 墨尔本站（09-18）/ 悉尼站（09-20）**——演出日均已早于生成日（已开演），且
  仍挂 `EXCEPTIONS.md` OPEN（墨站 `ticket_platform` 已确证失真应改 AXS、悉站 `venue` 为旧名且
  `price`/`time` 为 null），`data/events.json` 截至今日未修。整组不收。**额外理由**：`time=null`
  正好落在本篇主线上，收进来会在主线上开洞（同 021 对 `price=null` 的处理）。
- **候场喜剧 Loadingzone Comedy（墨尔本，常驻）**——"常驻开放麦 · on_sale"自 09-14 起无法在
  Eventbrite 主办方页核实到当前场次（OPEN），整条不列；正文不点名，只写通用原则。
- **"Low Availability / 余票紧张"**——属瞬时余票状态，沿用 018/028/035/041 的既定处理，不进
  正文/卡片。
- **座位区域名称、赞助商、主办方全称、退改签政策、余票量、座位视野、寄存、停车、公共交通**
  ——`events.json` 无对应字段，或与"星期几/开演时间"主线无关，不写（省略不等于错误）。悉尼站
  官方页今日虽列了停车预订截止与年龄限制，属"入场须知"类，同第 1 条排除理由处理。
- **`verified=false` 的其余条目**——`events.json` 未核实条目一条不进本篇（账号红线）。

FACT-AUDIT-STATUS: RED=0 CHECKED=28 SOURCES-CITED=28

## 渲染状态

- 模板: `cards/048/index.html`，复制自 `cards/041/index.html`。选 041 为基底的原因：041 是
  "无外链配图 + 3 场清单单 ledger"这一纯文字版式的最新验证后代（041 自记复制自 035、035 复制自
  028、028 与 001 的 `<head>`+CSS 段 diff 比对除 `<title>` 外完全一致），与本篇同为"3 场清单 +
  3 张卡"的汇总结构，结构匹配度最高。`<html data-theme="aushow">`、主题色 token、字体、
  `.ticket`/`.ledger`/`issue-strip` 组件样式全部原样保留，仅替换 `<title>` + 3 个 poster 区块
  内文案。
- 卡片数: 3 张 `<section class="poster xhs" id="xhs-01…03">`（与 028/035/041 同为 3 场清单，不凑空卡）。
- `render_card.py` 在计数前会剥掉 HTML 注释（`html_no_comments`），模板顶部示例注释里的
  `id="xhs-01"` 不会被算成 poster，脚本会正确识别为 3 张。
- 渲染: 交由 `automation/render_card.py`（headless Chrome 逐张截图 + PIL 校验 1080×1440）。
  本次会话按提示词第 0 节要求，**未调用任何浏览器/截图工具**。
