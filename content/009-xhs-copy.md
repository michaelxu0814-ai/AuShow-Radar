# 009 — 要提前锁的 2 场 + 不用等的 2 场（本周开票汇总）

**选题类型**：本周开票汇总（周四轮换位，2026-08-27 生成）

**信源条目**（全部 `data/events.json` → `verified=true`，共选 4 场）：
1. 周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会（2026-10-17）
2. 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会（2026-11-21）
3. Rolling Donkey 中文喜剧开放麦（悉尼，每周二）
4. 候场喜剧 Loadingzone Comedy 开放麦（墨尔本，常驻）

**本篇口径决定（先说清楚）**：

- **沿用 005 的"不说'本周开票'"口径。** 4 条 `status` 都是 `on_sale`（已在售），
  `events.json` 里没有任何字段支持"这些票是本周开售的"。栏目定位保留（仍记为
  "本周开票汇总"），但标题/卡面一律用"在售""现在能买"这类可核实的表述。
- **角度与 005 刻意错开。** 005（08-20）是"8 到 11 月 5 场演唱会时间线"，一条纯大场
  清单。本篇的可用池子已经变了（袁娅维两场均已过演出日、AKMU 两场仍卡在 EXCEPTIONS），
  剩下的 4 条天然分成两类：**要提前几个月锁的体育场大场** vs **常驻的中文开放麦**。
  本篇就按这个对比来写——"周杰伦要等到 10 月，这两场不用等"，是本篇独立于 005 的价值点，
  不是换皮重排同一张时间线。
- **Loadingzone 不写开场时间。** JSON `time=19:00`，但场馆官网该厂牌场次页写的是
  "7:30 pm – 9:30 pm"，两个数字冲突且无法判定哪个适用于当前场次。按 008 的既定做法
  （"没有官方原文就不写"）整条剔除，只写场馆与平台。详见事实核查表。

**排除项摘要**：袁娅维墨尔本站（08-20）/ 悉尼站（08-22）演出日期均早于本篇生成日
2026-08-27，已开演，不进"接下来能买"的清单；AKMU 两场仍在 `EXCEPTIONS.md` OPEN 状态
（墨尔本站 `ticket_platform` 已失真，悉尼站字段冲突 + 场馆名歧义），本篇一并不收。

**红线自查**：4 条全部 `verified=true`；日期/场馆/票价/平台逐字取自 JSON 字段；`price`
为 null 的两条不编造票价；`time` 存疑的一条不写时间；正文无外链；未点名任何个人/账号。

**本篇额外做了外部复核**：AKMU 那次事故（JSON 里 `ticket_platform` 随场馆换票务商而失真）
说明 verified 条目也会过期。本篇 4 条全部另做了一次外部核对，逐条留 URL，见事实核查表。

## 标题（14字）

周杰伦要等10月，这两场不用等

## 正文（发帖文案，无外链）

想看华语演出，不是只有"等大场"这一个选项 👇 手里这 4 场，2 场要提前几个月锁，2 场常驻——这周想去就能去。日期、场馆、票价、官方平台都逐条核过。

**先说要提前锁的两场 🌟**

🎤 **周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会**
10 月 17 日（周六）晚 7:30 · 墨尔本 Marvel Stadium
$208–$748（另加 $9.90 手续费），Ticketmaster。

🌊 **周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会**
11 月 21 日（周六）晚 7:30 · 悉尼 ENGIE Stadium (Sydney Olympic Park)
$188–$748（另加 $9.90 手续费），Ticketmaster。

两站都是 Ticketmaster 官方规则**每人最多 6 张**，超量的订单官方写明可能被直接取消——别为了凑人头用一个号狂买。

**再说不用等的两场 🎙️**

🐴 **Rolling Donkey 中文喜剧开放麦（悉尼）**
每周二 晚 7:30 · Chippo Hotel，87-91 Abercrombie St, Chippendale
Eventbrite 报名，常驻周场——这周二没赶上，下周二还在。

🎭 **候场喜剧 Loadingzone Comedy 开放麦（墨尔本）**
Club Voltaire，1st Floor/14 Raglan St, North Melbourne
AUNZ Comedy Media 旗下的双语喜剧厂牌，墨尔本常驻，Eventbrite 报名。

⚠️ 这两场我们收录时官方都没公布票价，所以这里不给数字，也不写具体开场时间——**以 Eventbrite 页面为准**。

最后还是那句：**官方票价是唯一标准**。加价转票、来源不明的二手票，风险自己扛；购票只认上面写的官方平台，别从站外二维码走。

评论区扣 1，私信发你这份清单，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #悉尼演唱会 #墨尔本演唱会 #周杰伦 #脱口秀 #开放麦 #演唱会情报 #留学生活

## 卡片文案结构（4张，票根美学）

> 张数说明：本篇天然是"两组对照"结构，P2 装"要提前锁的"、P3 装"不用等的"，两组的
> 字段密度完全不同（一组有完整票价区间+限购规则，一组票价未公布+只有场馆地址），
> 合成一张 ledger 会让单行注释超过 3 行不可读。封面与 CTA 是账号固定品牌结构。
> 无空卡、无凑数卡。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 本周在售 · 演出清单
- 大字标题: 周杰伦要等 10 月 / 这两场不用等
- 副标题: 2 场大场 · 2 场常驻
- 说明: 悉尼 & 墨尔本，4 场华语演出。日期、场馆、票价、官方平台，一张图排明白。
- 底部条: 现在都能买 — 悉尼 & 墨尔本 4 场
- 配图: 无（涉及多组演出方，挂任一张海报都有"张冠李戴"风险，整篇不挂图；沿用 004/005/008）

**P2 要提前锁的（ledger 3条）**
1. 墨尔本 — 周杰伦「粉色 嘉年华Ⅱ」·10.17 周六 19:30 · Marvel Stadium · $208–$748（另加 $9.90 手续费）· Ticketmaster
2. 悉尼 — 周杰伦「海洋 嘉年华Ⅱ」·11.21 周六 19:30 · ENGIE Stadium (Sydney Olympic Park) · $188–$748（另加 $9.90 手续费）· Ticketmaster
3. 限购 6 张 — 两站同属「嘉年华Ⅱ」世界巡回演唱会；Ticketmaster 官方写明每人最多 6 张，超量订单可能被取消
- 底部条: 两站均在售 — 出手前再复核官方页面
- 版式说明: ledger-row 网格为 `96px 1fr auto`，note 占 460px 后 title 列只剩约 300px，
  故 title 一律压到 2–4 字，完整演出名/场馆/票价放进 note，避免 42px 标题折行

**P3 不用等的（ledger 3条）**
1. 悉尼 — Rolling Donkey 中文喜剧开放麦 · 每周二 19:30 · Chippo Hotel，87-91 Abercrombie St, Chippendale · Eventbrite
2. 墨尔本 — 候场喜剧 Loadingzone Comedy · 墨尔本常驻 · Club Voltaire，1st Floor/14 Raglan St, North Melbourne · Eventbrite
3. 票价未公布 — 这两场我们收录时官方均未公布票价，这里不给数字；具体场次与票价以 Eventbrite 页面为准
- 收尾: 官方票价是唯一标准——加价转票、来源不明的二手票，风险自己扛。
- 底部条: 常驻场 — 这周没赶上，下周还在

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 大场要等 / 小场随时
- 正文: 评论区扣 1，私信发你这份 4 场清单，还有后续开票提醒。
- 底部条: VOL. 009 — 简介里有完整演出日历

## 事实核查表

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | 演出名「周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` 该条目 `title_zh`，`verified=true`，逐字复制 |
| 2 | 墨尔本站 2026-10-17，且为周六 | GREEN | 同条目 `date="2026-10-17"`；星期由日期计算得出（2026-10-17 = Saturday）；外部复核 https://www.marvelstadium.com.au/king-of-mandopop-jay-chou-announces-melbourne-show 原文 "Saturday, 17 October 2026" |
| 3 | 墨尔本站开演 19:30（文案写"晚 7:30"） | GREEN | 同条目 `time="19:30"`；外部复核同上 Marvel Stadium 官网页 "7:30 PM" |
| 4 | 墨尔本站场馆 Marvel Stadium，城市墨尔本 | GREEN | 同条目 `venue` / `city`；外部复核 https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 原文 "October 17, 2026 – Marvel Stadium, Melbourne VIC" |
| 5 | 墨尔本站票价 $208–$748，另加 $9.90 手续费 | GREEN | 同条目 `price="$208–$748 (+$9.90手续费)"`，逐字复制（Ticketmaster 汇总页不列价，指向各场次页；本篇以 verified 条目字段为准并提示复核官方页面） |
| 6 | 墨尔本站购票平台 Ticketmaster、当前在售 | GREEN | 同条目 `ticket_platform="Ticketmaster"` / `status="on_sale"`；外部复核 https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 墨尔本场标注 "On Sale Now!" |
| 7 | 演出名「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` 该条目 `title_zh`，`verified=true`，逐字复制 |
| 8 | 悉尼站 2026-11-21，且为周六 | GREEN | 同条目 `date="2026-11-21"`；星期由日期计算得出（2026-11-21 = Saturday）；外部复核 https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 原文 "November 21, 2026 – ENGIE Stadium, Sydney NSW" |
| 9 | 悉尼站开演 19:30（文案写"晚 7:30"） | GREEN | 同条目 `time="19:30"` |
| 10 | 悉尼站场馆 ENGIE Stadium (Sydney Olympic Park)，城市悉尼 | GREEN | 同条目 `venue` / `city`；外部复核同上 Ticketmaster 汇总页 "ENGIE Stadium, Sydney NSW" |
| 11 | 悉尼站票价 $188–$748，另加 $9.90 手续费 | GREEN | 同条目 `price="$188–$748 (+$9.90手续费)"`，逐字复制；与墨尔本站起价不同，两站分开写未合并区间 |
| 12 | 悉尼站购票平台 Ticketmaster、当前在售 | GREEN | 同条目 `ticket_platform` / `status="on_sale"`；外部复核 Ticketmaster 汇总页悉尼场 General Public Sale "12pm on Tuesday 28th April"（早于本篇生成日 2026-08-27，即已开售） |
| 13 | 两站每账户/每人限购 6 张，超量订单可能被取消 | GREEN | 两条目 `notes="主办方 Sky Music & Horizon Production;每账户限购6张"`；外部复核 https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 原文 "You may purchase a maximum of 6 tickets per person" 及 "Persons who exceed the ticket limit may have any or all of their orders and tickets cancelled without notice by Ticketmaster" |
| 14 | 演出名「Rolling Donkey 中文喜剧开放麦(悉尼,每周二)」，每周二举行 | GREEN | `data/events.json` 该条目 `title_zh`，`verified=true`；外部复核 https://www.eventbrite.com/e/copy-of-rolling-donkey-tickets-1983189907399 页面为 "Rolling Donkey 驴打滚每周二中文喜剧开放麦"，标注 Tuesday、多场次 recurring weekly |
| 15 | Rolling Donkey 场馆 Chippo Hotel，87-91 Abercrombie St, Chippendale（悉尼） | GREEN | 同条目 `venue="Chippo Hotel, 87-91 Abercrombie St, Chippendale"` / `city="悉尼"`；外部复核同上 Eventbrite 页原文 "87-91 Abercrombie Street, Chippendale, NSW 2008" |
| 16 | Rolling Donkey 开场 19:30（文案写"晚 7:30"） | GREEN | 同条目 `time="19:30"`；外部复核同上 Eventbrite 页原文 "7:30 PM" |
| 17 | Rolling Donkey 购票/报名平台 Eventbrite，页面在售 | GREEN | 同条目 `ticket_platform="Eventbrite"` / `status="on_sale"` / `ticket_url` 为 eventbrite.com 域名；外部复核同上页面当前 live 且列出多个未来场次 |
| 18 | 演出名「候场喜剧 Loadingzone Comedy 开放麦(墨尔本,常驻)」，墨尔本常驻 | GREEN | `data/events.json` 该条目 `title_zh` / `city="墨尔本"`，`verified=true`，"常驻"取自 `title_zh` 括注 |
| 19 | Loadingzone 场馆 Club Voltaire，1st Floor/14 Raglan St, North Melbourne | GREEN | 同条目 `venue="Club Voltaire, 1st Floor/14 Raglan St, North Melbourne"`；外部复核 https://www.clubvoltaire.com.au/events/loading-zone-comedy-29 原文地址 "Club Voltaire, 1st Floor/14 Raglan St, North Melbourne VIC 3051, Australia" |
| 20 | Loadingzone 为 AUNZ Comedy Media 旗下双语喜剧厂牌 | GREEN | 同条目 `notes="AUNZ Comedy Media旗下双语喜剧厂牌,也承接国内演员澳洲巡演"`；外部复核 https://www.eventbrite.com/o/loadingzone-comedy-75417874333 主办方简介原文 "澳大利亚AUNZ COMEDY MEDIA旗下运营的专业双语喜剧厂牌" |
| 21 | Loadingzone 报名平台 Eventbrite，当前有未来场次（文案称"常驻"成立） | GREEN | 同条目 `ticket_platform="Eventbrite"` / `status="on_sale"` / `ticket_url` 为 eventbrite.com 主办方页；外部复核该主办方页当前标题为 "候场喜剧Loadingzone Comedy Events - 4 Upcoming Activities and Tickets"，即有 4 场待售场次 |
| 22 | Loadingzone 的开场时间**不写** | AMBER | 条目 `time="19:00"`，但 https://www.clubvoltaire.com.au/events/loading-zone-comedy-29 该厂牌场次页写的是 "7:30 pm – 9:30 pm"，两数字冲突且无法判定哪个适用于当前场次。**处理=整条剔除不写**，文案改为"以 Eventbrite 页面为准"。未升级 RED：本篇没有依赖该字段做出任何断言 |
| 23 | 两场开放麦均不给票价数字 | GREEN | 两条目 `price=null`；外部复核两个 Eventbrite 页面均未列出票价（Rolling Donkey 页 "Ticket Price: Not specified"），与"官方未公布"一致 |
| 24 | "官方票价是唯一标准，加价转票/来源不明二手票风险自负" | GREEN | 账号档案 `~/.claude/skills/xhs-content/accounts/aushow.md` 红线段 + 已发布的 `content/001-xhs-copy.md` P3、`content/005-xhs-copy.md` P3 同款表述；口径与历史帖一致，只讲模式未点名任何个人/账号 |
| 25 | 本篇共 4 场，覆盖悉尼与墨尔本，且当前均可购买/报名 | GREEN | 上述 4 条 `verified=true` 条目的 `city` ∈ {悉尼, 墨尔本}、`status` 均为 `on_sale`，计数由该 4 条汇总得出；封面"4 场""现在都能买"均由此得出 |

**主动排除项（无依据、依据冲突或已过期，本篇一律不写）**：

- **袁娅维 TIA RAY 墨尔本站（2026-08-20）与悉尼站（2026-08-22）**——两条均 `verified=true`，
  但演出日期都早于本篇生成日 2026-08-27，已开演。列进"接下来能买"的清单属误导，整组剔除。
  （005 当时只剔除了墨尔本站，悉尼站彼时尚未开演；本篇两条都到期。）
- **AKMU 乐童音乐家 墨尔本站（09-18）与悉尼站（09-20）**——两条仍在 `~/Projects/EXCEPTIONS.md`
  OPEN 状态：墨尔本站 `ticket_platform="Ticketek"` 已失真（Melbourne Park 自 2026-08-22 起
  改由 AXS 承接票务），悉尼站 `status` 与 `notes` 冲突且场馆名有歧义。购票平台是"开票汇总"
  这一栏目的核心字段，带着已知失真的平台名发汇总篇风险高于价值，整组不收，等用户修
  `events.json` 后再进池。
- **Loadingzone 的开场时间**——见核查表第 22 行，字段冲突，剔除。
- **Rolling Donkey 与 Loadingzone 的票价、具体日期**——`price=null`、`date=null`，不给任何
  数字、不写"几月几号那场"。Rolling Donkey 只写 `title_zh` 里已有的"每周二"。
- **"本周开票 / 本周开售"这一说法**——4 条中没有任何字段记录开售日期在本周，栏目名保留但
  措辞用"在售""现在能买"，详见文首口径决定。
- **周杰伦两场的主办方**——JSON `notes` 有 "Sky Music & Horizon Production"，但汇总篇信息
  密度已高，本篇只取限购条款，与 005 处理一致（省略不等于错误）。
- **`verified=false` 的另外 93 条演出**——events.json 共 101 条、verified 仅 8 条，未核实
  条目一条不进本篇（账号红线）。
- **座位视野、开门检票时间、寄存、退改签政策、余票量**——events.json 无对应字段，外部亦无
  可靠官方原文，不写。

FACT-AUDIT-STATUS: RED=0 CHECKED=25 SOURCES-CITED=25

## 渲染状态

- 模板: `cards/009/index.html`，复制自 `cards/008/index.html`（该文件的 `<head>`+CSS 段是
  004→005→…→008 一路沿用的同一份已验证版式，且已是"无 `frame-img` 外链配图 +
  `.ledger-note` 内联 `max-width:460px`"的纯文字版式后代，本篇同样不挂任何海报）。
  `<html data-theme="aushow">`、主题色 token、字体、`.ticket`/`.ledger`/`issue-strip`
  组件样式全部原样保留，仅替换 4 个 poster 区块内的文案 + `<title>`。
- 卡片数: 4 张 `<section class="poster xhs" id="xhs-01…04">`
- `render_card.py` 在计数前会剥掉 HTML 注释（`html_no_comments`），模板顶部示例注释里的
  `id="xhs-01"` 不会被算成 poster，脚本会正确识别为 4 张。
- 渲染: 交由 `automation/render_card.py`（headless Chrome 逐张截图 + PIL 校验 1080×1440）。
  本次会话按 `daily-xhs-prompt.md` 第 0 节要求，**未调用任何浏览器/截图工具**。
