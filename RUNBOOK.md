# AuShow Radar — 值班日志

小红书内容自动化(`run_daily_xhs.sh`)每次运行后在此追加一条记录：日期、编号、
选题类型、fact-audit 是否发现问题。

## 值班日志

- **2026-08-16** | 001号 | 单场演出安利(周杰伦墨尔本站) | fact-audit 7条全GREEN，
  RED=0。渲染阶段发现1处：票根卡(P2)底部曾有内容溢出+编造文案"Gate details TBC on
  ticket"(events.json无此字段)，人工发现并删除后重渲染，四张图逐一核对通过。
  已推送Telegram(sendMediaGroup确认`"ok":true`)，等用户手动发布。
  当天同时确定：chrome-devtools-mcp 截图工具反复超时/卡死，不适合无人值守自动化，
  改用 `automation/render_card.py`(headless Chrome CLI + PIL裁切)做确定性渲染，
  daily-xhs-prompt.md 已相应调整为"只写内容不管渲染"。

- **2026-08-17** | 002号 | 单场演出安利(周杰伦悉尼站) | fact-audit 9条全GREEN，RED=0，
  未发现事实错误。选题按周一轮换位=单场演出安利；001已用掉周杰伦墨尔本站，本篇取同巡演
  悉尼站(verified 池未用过、热度最高)。**未选日期最近的袁娅维墨尔本8/20/悉尼8/22**：按
  "001计划08-24起手动发布"的节奏，这两场在发布时已演完，写了等于浪费——已在
  `content/002-xhs-copy.md` 末尾留备注等用户裁决(若8/20前就发，可加急改产袁娅维)。
  本次会话按 daily-xhs-prompt.md 第0节未调用任何浏览器截图工具，渲染留给 render_card.py。
  另注：`content/cards/00N/index.html` 引用的 `assets/magazine-bg-webgl.js` 在 001/002
  下均不存在(404)，WebGL 墨流背景实际未挂载——001 出图已人工验收通过，故本次沿用未改。

- **2026-08-18** | 003号 | 转票防骗指南(周二轮换位) | fact-audit 10条全GREEN，RED=0。
  本篇不依赖 `data/events.json`，verified 池(8条)未被消耗——这正是轮换表把周二/周日
  安排给防骗选题的目的。10 条断言全部来自站外权威源：Scamwatch 官方警示(盗号冒充熟人
  "原价急转"、270+人报案、追加"改名费"、只从 authorised seller 买、用 PayPal/Apple Pay
  而非银行转账)、Ticketek 帮助中心(Marketplace 官方自营、转售价上限=原票面、转售后重新
  配发条码原票作废)、Ticketmaster AU 官方 Resale 页、NSW 政府转售规则(10% 上限含各类
  手续费 + 广告必须列原价/要价/座位)、维州 Major Events Act 2009(declared 活动 10% 上限)。
  **抓取备注**：djsir.vic.gov.au、help.ticketek.com.au、help.ticketmaster.com.au、
  fairtrading.nsw.gov.au 四个站点对 WebFetch 返回 403 或 301 到重定向服务，改用 WebSearch
  抽取 + nsw.gov.au 镜像页(WebFetch 成功)交叉核实，已在核查表逐条注明抓取方式。
  措辞上刻意保留了两处法律限定(NSW 仅适用带转售限制条款的票、维州仅适用 declared 活动)，
  未泛化成"澳洲加价10%就违法"。
  卡片 4 张(封面/套路识别/自保清单/CTA)，无配图——防骗选题不挂任何演出海报，规避
  "海报张冠李戴"红线；全篇不点名任何个人/账号/二手平台，只讲模式。
  本次会话按 daily-xhs-prompt.md 第0节未调用任何浏览器截图工具，渲染留给 render_card.py。

- **2026-08-19** | 004号 | 场馆攻略(周三轮换位) | fact-audit 15条全GREEN，RED=0。
  场馆选 Marvel Stadium(墨尔本 Docklands)——它是 verified 池里日期最近的体育场级演出
  (周杰伦墨尔本站 2026-10-17)的场馆。本篇同样不消耗单场安利池：只引用了该条目的
  日期+场馆两个字段作时间锚点，不复述票价/平台/限购。
  15 条断言全部来自 marvelstadium.com.au 官网(WebFetch 全部抓取成功，无 403)：
  getting-to-marvel-stadium(地址 740 Bourke St Docklands VIC 3008、Southern Cross 紧邻 +
  Bourke St 人行天桥、电车 30/35/70/75/86 直达 vs 96/11/48 需步行、巴士总站、
  Port Phillip Ferries 对街停靠、停车入口 A&B/D&E + 限高 2.1m)、conditions-of-entry
  (包不得大于 A3 + 须放得进座位底下)、a-z-guide(cashless 无 ATM、禁专业相机/录音录像/
  三脚架、禁罐装玻璃、旗杆 1.6m 上限、Gate 1/Gate 5 免费寄存位置)、faq(可自带食物与
  非酒精饮料无玻璃、电子票提醒充电+调亮度)、about-the-stadium(可开合屋顶 8 分钟)。
  **本次 fact-audit 拦下的问题(未进入文案)**：
  ① 搜索摘要给的"步行 4 分钟"在官网正文核实不到 → 删掉，只写"就在隔壁/走天桥"；
  ② 重入(pass out)政策官网两处自相矛盾(A-Z 页称可扫票离场再入场，Conditions of Entry
     页称 "Pass outs will not be issued") → 无法判定，整条不写；
  ③ 免费电车区是否覆盖球场：PTV 官方边界图 PDF 抓取失败(SSL 握手错误) → 不写；
  ④ 视野/座位区推荐官网无依据、且演唱会舞台布局因场次而异 → 整块砍掉，
     这是账号红线"凭印象编"的高风险区，宁可让攻略少一个卖点。
  以上四项已在 `content/004-xhs-copy.md` 的"主动排除项"里写明，便于日后复查。
  卡片 4 张(封面/怎么到/怎么进/CTA)，无配图。模板复制自 003 而非 001——003 是同模板
  直系后代且已含 `.ledger-note` max-width 修正与无 frame-img 的纯文字版式，与本篇形态
  一致；已 diff 确认 004 与 003 的第 1–830 行(全部 CSS/主题 token/字体)仅 <title> 不同。
  本次会话按 daily-xhs-prompt.md 第0节未调用任何浏览器截图工具，渲染留给 render_card.py。

- **2026-08-20** | 005号 | 本周开票汇总(周四轮换位) | fact-audit 20条：19 GREEN + 1 AMBER，
  RED=0。20 条断言全部来自 `data/events.json` 的 `verified=true` 字段(本篇不涉及场馆/法条
  这类需要外部核实的客观信息，故无 WebSearch 依据行；每条都写明了具体条目+字段名)。
  选了 5 场：袁娅维悉尼站(08-22)、AKMU 墨尔本(09-18)、AKMU 悉尼(09-20)、周杰伦墨尔本
  (10-17)、周杰伦悉尼(11-21)。汇总篇不消耗"单场安利"未用池。
  **本次 fact-audit 拦下的两个问题(已改进文案，未带病发布)**：
  ① **"本周开票"这个栏目名本身站不住**——events.json 里 5 条的 `status` 都是 `on_sale`
     (已在售)，没有任何字段记录"这些票是本周开售的"。栏目定位保留，但标题和卡面 kicker
     全部改成可核实的"8 到 11 月""本周在售"，不制造一个数据支持不了的时间断言。
  ② **AKMU 两条目字段自相矛盾**：`status=on_sale`，但同条目 `notes` 写"开票时间和票价
     截至 2026-07-03 未公布"，且 `price=null`。判为 AMBER，处理方式是向保守一侧靠——
     文案只写"已官宣 + 购票平台 Ticketek + 票价未公布"，**不声称在售、不给任何票价数字、
     不写开票日期**，这样两种情况下都不构成错误断言。未升级为 RED，因为最终文案没有
     依赖这个冲突字段做出任何断言。
  另外主动剔除：袁娅维墨尔本站(`date=2026-08-20`)虽 verified，但演出日=本篇生成日，
  人工审核后发布时已开演，放进"接下来的清单"会误导，整条不用；`time=null` 的三场
  (袁娅维、AKMU×2)不写开演时间，只有周杰伦两站写了 19:30(字段有值)。
  卡片 4 张(封面/时间线/票价与平台/CTA)，无配图——汇总篇涉及 3 组艺人，挂任一张海报
  都有"张冠李戴"风险(账号已有两次该类事故)，整篇不挂图。模板复制自 004，已 diff 确认
  第 1–840 行(全部 CSS/主题 token/字体)与 001 仅 `<title>` 不同。
  版式上做了一处预防性调整：ledger-row 网格是 `96px 1fr auto`，note 吃满 460px 后
  title 列只剩约 300px，故 ledger-title 一律压到 3–4 字(艺人名/短标签)，完整巡演名与
  场馆日期放进 note，避免 42px 标题在渲染时折行。
  本次会话按 daily-xhs-prompt.md 第0节未调用任何浏览器截图工具，渲染留给 render_card.py。

- **2026-08-24** | 006号 | 单场演出安利(周一轮换位) | fact-audit 12条：12 GREEN，RED=0。
  **本次 fact-audit 拦下了一个真实事实错误(这是 fact-audit 首次拦下 events.json 本身的
  数据错误，而不只是文案措辞问题)**：
  按"日期最近/热度最高"，本应安利 AKMU 墨尔本站(2026-09-18，未用过的 verified 条目里
  最近的一场)。核实时发现该条目 `ticket_platform="Ticketek"` **已经过期失真**——
  Margaret Court Arena 所属的 Melbourne Park 自 **2026-08-22**(即两天前)起改由 **AXS**
  承接票务，官方场馆页并特别注明 "Ticketek ticket delivery for AKMU has been
  intentionally delayed. Your tickets will be issued by AXS by the end of August"。
  照 JSON 写"Ticketek 是唯一官方购票平台"会把读者导到已不承接该场的平台(RED)；改写成
  AXS 又违反"必须与 events.json 逐字一致、不得使用 JSON 没有的字段"红线。两条路都堵死，
  **该条目今天不可发**，已按第7步写入 `~/Projects/EXCEPTIONS.md` 等用户修数据。
  次选 AKMU 悉尼站(09-20)同样弃用：price/time 均为 null、status=on_sale 与 notes
  "票价截至2026-07-03未公布"自相矛盾(005 已记录过)、且场馆名存在歧义(JSON 记
  "ICC Sydney Theatre"，Ticketek 现标为 "TikTok Entertainment Centre")——一张没票价、
  没时间、场馆名与购票页对不上的票根卡，正撞账号"详情页跳错演出"的历史事故线。
  最终改用 **Rolling Donkey 中文喜剧开放麦(悉尼，每周二)**：该条目每个字段(地址/19:30/
  每周二/Eventbrite/在售/未标价)都被官方 Eventbrite 页独立佐证，零冲突字段。
  额外好处是"每周二"为常驻周场，**任何一天发布都成立**，不存在"明晚就有"这类会因用户
  手动审核延迟而失真的时效断言——文案里已刻意把 CTA 写成恒真的"每周二都有一场"。
  卡片 4 张(封面/票根/去之前先看这4条/CTA)，无配图(该条目 image=null)。
  票根大字位用「周二」两字替代 001 的日期数字(该条目 date=null)。
  模板复制自 005，已 diff 确认第 1–840 行(全部 CSS/主题 token/字体)与 001 仅 <title> 不同。
  本次会话按 daily-xhs-prompt.md 第0节未调用任何浏览器截图工具，渲染留给 render_card.py。
  ⚠️ 组合治理提醒(见文末"给用户的话")：PORTFOLIO.md 最后评审停留在 2026-07-11(已超 14 天
  心跳阈值)，且 AuShow 的杀死标准写着"若 08-24 后仍未实际发布，下次评审自动转判定"——
  今天正是 08-24，这条时钟到点了。

- **2026-08-25** | 007号 | 转票防骗指南(周二轮换位) | fact-audit 13条：13 GREEN，RED=0。
  不依赖 verified 池，本次未消耗任何未安利演出（池子仍卡在 EXCEPTIONS.md 里那两条 AKMU
  待用户修数据）。
  **同选题去重是本次的主要设计约束**：003 已经写过"转票防骗"，直接再写一篇会撞车。
  本篇换到 003 完全没碰的那一面——**假官网 / 未授权转售站 / 从搜索结果点进去的仿冒售票页**
  （003 讲的是人对人的私下转票：盗号熟人、只发二维码、追加改名费、不写原价的 listing）。
  两篇正文与卡片逐条比对确认零重叠。
  顺带对 003 做了一处**修正性补充**：003 的 P3-01 把 "Ticketmaster Resale、Ticketek
  Marketplace" 并列成"官方转售通道"，容易被读成"这两个平台通用安全"。核实 Ticketek 官方
  帮助页发现口径其实是**分场次的**——Ticketek 把 Ticketmaster Resale 也列在它的未授权
  平台清单里，并声明"只有 Ticketek Marketplace 能保证 Ticketek 出的票有效"。本篇因此把
  记忆点写成"别问哪个平台安全，要问这一场的官方售票方是谁"，口径比 003 更准，且没有
  否定 003 已发内容(003 那两个平台各自对自家场次的表述仍成立)。
  **红线处理**：官方信源(Ticketek 帮助页、LPA 准则)里逐一点名了 8 家未授权转售平台，
  照抄会违反账号"防诈内容不点名具体个人/账号"红线，全部改写为"未授权转售站"的模式表述，
  文案里一个二级平台名都没出现。文中的 Ticketek / Ticketmaster 只在"一级官方售票方"
  语境下正面引用其官方规则。
  **主动砍掉一条想写的内容**："结账时才冒出巨额手续费""仅剩2张的紧迫感"是这类骗局的
  典型特征，但这次没找到可引用的澳洲官方信源，宁缺勿编，整条不写。
  **本地性**：本账号是复用的布里斯班老号，本篇特意用**昆州**规则(Stadiums Queensland
  场馆含 Brisbane Entertainment Centre、Suncorp Stadium、The Gabba，转售价超原价 10%
  违法，Major Sports Facilities Act 2001)作为"价格离谱=违规 listing"的判据，对老粉丝
  有本地价值；同时明确只写昆州口径，没有把 10% 泛化成全澳统一规则(NSW/VIC 已在 003
  单独写过，本篇不重复也不合并)。
  卡片 4 张(封面/4个识别标记/付款前60秒4步/CTA)，无配图(防骗选题不挂任何演出海报)。
  模板复制自 003，已 diff 确认第 1–840 行(全部 CSS/主题 token/字体)与 001 仅 <title> 不同。
  已本地模拟 run_daily_xhs.sh 第 55–63 行的 fact-audit 关卡：GATE PASS。
  本次会话按 daily-xhs-prompt.md 第0节未调用任何浏览器截图工具，渲染留给 render_card.py。
  ⚠️ 组合治理(连续第二天提醒，见文末)：PORTFOLIO.md 最后评审仍停在 2026-07-11(超 14 天
  心跳阈值)，且 AuShow 杀死标准里"若 08-24 后仍未实际发布，下次评审自动转判定"这条时钟
  **昨天已经到点**，今天是逾期第 1 天。

### 2026-08-26(周三) — 第 008 篇 · 场馆攻略

- **产出**：`content/008-xhs-copy.md` + `content/cards/008/index.html`(4 张 poster)。
  标题「悉尼ENGIE球场，包别超过A4」(16 字)。
- **选题**：周三轮换位=场馆攻略。场馆选 **ENGIE Stadium(Sydney Olympic Park)**,是 verified
  条目「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」(2026-11-21)的场馆。刻意避开 004 已
  写过的 Marvel Stadium——ENGIE 是 verified 池里另一个体育场级场馆,且**入场规则与 Marvel
  差异实质**(包限 A4 vs A3、旗帜限旗面 1m×1m vs 限旗杆 1.6m、业余拍照允许 vs 专业相机
  一律禁带),对跨城看演出的受众有独立价值,不是换皮重写。
- **fact-audit**：**RED=0,CHECKED=18,SOURCES-CITED=18,未发现需要改文案的事实错误。**
  全部断言来自 sydneyshowground.com.au(官方场馆站:getting-here / engie-stadium-faqs /
  conditions-of-entry)与 transportnsw.info(官方交通站),逐条留 URL + 原文引语。
- **审计中处理掉的两处风险**(未构成 RED,但改了写法)：
  1. **渡轮距离口径冲突**——三方站点称"渡轮就在球场旁",Transport NSW 官方页写的是
     "around a 40 minute walk (3.6km)"。采信官方页,并用场馆官网"坐船来还得再转一趟巴士"
     这句互证,最后把它写成一条**反向提醒**("千万别为了浪漫坐渡轮"),是本篇最实用的差异点。
  2. **火车站步行 5 分钟**——搜索摘要有这个数字,但两次 WebFetch 官网 FAQ 页都没抓到原文,
     判定不可靠,整条剔除,只保留官网原话 "on Sydney Showground's doorstep"。
     (与 004 处理"步行 4 分钟"的做法一致:分钟数没有官方原文就不写。)
- **主动排除 7 项**：视野/座位区推荐、步行分钟数、开门检票时间、寄存(官网只说 sporting
  events 没有,演唱会未说明)、pass out 政策(官网只有 Inclosed Lands Act 的"被禁后非法
  再入场",与普通中途离场无关,不能挪用)、凭票免费坐火车(出自 Sydney Thunder 球赛推广页,
  非演唱会适用)、场馆容量/看台层数。详见 008 文末"主动排除项"。
- **价格类断言处理**：停车费 $8/小时、$40/天封顶取自场馆官网 getting-here 页,但价格是
  churn 最高的一类事实,文案里明确标注"场馆官网标价"并加"出发前再看一眼官网",不承诺
  演唱会当晚同价(官网未按活动类型区分)。
- 模板复制自 `cards/007/index.html`,`data-theme="aushow"`、主题色 token、字体、
  `.ticket`/`.ledger`/`issue-strip` 全部原样保留,只改 4 个 poster 区块 + `<title>`。
- 已确认 `render_card.py` 在计数前会剥掉 HTML 注释(`html_no_comments`),模板顶部那段
  示例注释不会被算成 poster,脚本会正确识别为 4 张。
- 本次会话按 `daily-xhs-prompt.md` 第 0 节,**未调用任何浏览器/截图工具**,渲染与 Telegram
  推送留给 `run_daily_xhs.sh` → `render_card.py`。
- ⚠️ **组合治理(连续第三天提醒)**：PORTFOLIO.md 最后评审仍停在 2026-07-11(超 14 天心跳
  阈值)。AuShow 杀死标准"若 08-24 后仍未实际发布,下次评审自动转判定"**已逾期第 2 天**。
  内容侧已积压 8 篇待发,瓶颈完全在人工发布这一步,不在生产线。建议尽快跑 /portfolio-review。

### 2026-08-27(周四) — 第 009 篇 · 本周开票汇总

- **产出**：`content/009-xhs-copy.md` + `content/cards/009/index.html`(4 张 poster)。
  标题「周杰伦要等10月，这两场不用等」(14 字)。
- **选题**：周四轮换位=本周开票汇总。收 4 场 verified 条目：周杰伦墨尔本(10-17)、
  周杰伦悉尼(11-21)、Rolling Donkey 开放麦(悉尼,每周二)、候场喜剧 Loadingzone(墨尔本,常驻)。
- **可用池子本周缩水**：袁娅维两场(08-20 / 08-22)演出日期均已早于今天，整组过期剔除
  (005 当时只需剔墨尔本站)；AKMU 两场仍卡在 EXCEPTIONS OPEN。剩下的 4 条天然分成
  "体育场大场"与"常驻开放麦"两类，本篇就按这个对比写，**不是 005 时间线的换皮重排**。
- **fact-audit**：**RED=0,CHECKED=25,SOURCES-CITED=25,未发现需要改文案的事实错误。**
- **本篇加做了外部复核(新做法)**：AKMU 那次事故证明 verified 条目也会过期失真，所以
  4 条全部另做一次外部核对，逐条留 URL——
  - 周杰伦两站：discover.ticketmaster.com.au 汇总页复核日期/场馆/在售状态/限购 6 张
    ("You may purchase a maximum of 6 tickets per person")；marvelstadium.com.au 复核
    墨尔本站 "Saturday, 17 October 2026" + "7:30 PM"。两站日期经计算均为**周六**,写进了文案。
  - Rolling Donkey：Eventbrite 页当前 live,原文 "每周二"、"7:30 PM"、
    "87-91 Abercrombie Street, Chippendale, NSW 2008",与 JSON 三个字段逐一吻合。
  - Loadingzone：主办方 Eventbrite 页当前标题为 "4 Upcoming Activities",证实"常驻"
    这一说法当下仍成立(首次 WebFetch 只抓到导航、误报"无场次",经搜索结果标题纠正)。
- **审计中剔掉的一处冲突**：Loadingzone 条目 `time="19:00"`,但 clubvoltaire.com.au 该厂牌
  场次页写 "7:30 pm – 9:30 pm",两数字冲突且无法判定哪个适用于当前场次 → **整条不写开场
  时间**,文案改为"以 Eventbrite 页面为准"。沿用 008 "没有官方原文就不写"的既定做法。
- **沿用 005 的口径**：不说"本周开票"(4 条 status 均为 on_sale=已在售,无字段支持"本周
  开售"),卡面统一用"本周在售/现在都能买"。
- **主动排除**：两场开放麦的票价与具体日期(price/date=null)、周杰伦主办方、座位视野、
  开门检票时间、退改签、余票量。详见 009 文末"主动排除项"。
- 模板复制自 `cards/008/index.html`,已 `diff` 确认第 1–840 行(`<head>`+CSS)除 `<title>`
  外与 008 完全一致,`data-theme="aushow"`、主题色 token、字体、`.ticket`/`.ledger`/
  `issue-strip` 全部原样保留,只改 4 个 poster 区块 + `<title>`。
- 已按 `render_card.py` 的 `html_no_comments` 逻辑验证:剥掉注释后恰好 4 个
  `<section class="poster xhs">`(id `xhs-01`…`xhs-04`),模板顶部示例注释不会被误计。
- 本次会话按 `daily-xhs-prompt.md` 第 0 节,**未调用任何浏览器/截图工具**,渲染与 Telegram
  推送留给 `run_daily_xhs.sh` → `render_card.py`。
- ⚠️ **组合治理(连续第四天提醒)**：PORTFOLIO.md 最后评审仍停在 2026-07-11(超 14 天心跳
  阈值)。AuShow 杀死标准"若 08-24 后仍未实际发布,下次评审自动转判定"**已逾期第 3 天**。
  内容侧已积压 9 篇待发,瓶颈完全在人工发布这一步,不在生产线。建议尽快跑 /portfolio-review。
- ⚠️ **verified 池子告急**：8 条 verified 里,袁娅维 2 条已过期、AKMU 2 条卡在 EXCEPTIONS,
  实际可用只剩 4 条(周杰伦 2 + 开放麦 2),且周杰伦两场已被 001/002 单场安利过。
  下一个"单场演出安利"轮换位(周五,即明天 08-28)会直接撞上这个空池。**建议优先处理
  EXCEPTIONS 里 AKMU 两条(修 ticket_platform/补 price)**,那是最快把池子从 4 补回 6 的动作。

### 2026-08-29(周六) — 第 011 篇 · 场馆攻略

- **产出**：`content/011-xhs-copy.md` + `content/cards/011/index.html`(**3 张** poster)。
  标题「悉尼中文开放麦，在全素酒吧地下室」(16 字)。
- **选题**：周六轮换位=场馆攻略。场馆取 The Chippo Hotel(悉尼 Chippendale)，即 verified
  条目「Rolling Donkey 中文喜剧开放麦(悉尼,每周二)」的场地。
- **本篇的差异化**：004(Marvel)、008(ENGIE)两篇场馆攻略都是"几万人体育场怎么进"，再写
  第三个大球场就是换皮。verified 池里唯一另一类场馆就是酒吧/小场，本篇写的是
  **全素 pub 的地下室 gig room**，读者动作完全不同(大场=抢票+过安检，小场=推门进去会看到
  什么、能不能吃饭)。另一个好处：该条目 `recurrence="每周二"` 是常驻场次，**攻略不会像
  单场演出那样过期**，对正在缩水的 verified 池是一种保值写法。
- **fact-audit**：**RED=0,CHECKED=14,SOURCES-CITED=14,未发现需要改文案的事实错误。**
  信源：thechippohotel.com.au(官网首页+contact 页)、Time Out Sydney、Broadsheet、
  该场次 Eventbrite 售票页，另加 events.json 字段。核心事实(全素 pub、地下室 gig room)
  均有**两个独立来源互证**(官网/Time Out、Broadsheet/Time Out)才敢写。
- **审计中处理的 3 处冲突**(沿用 008/009"没有官方原文就不写"的既定做法)：
  - **交通步行时间——整块砍掉，并把矛盾本身写成卖点**。第三方聚合站给出 10 分钟、11 分钟、
    23 分钟、335 米四种互斥说法，场馆官网与 Eventbrite 页都没有 getting-here 章节，无官方
    口径。文案因此不给任何数字，改写成一条反向提醒"别信任何固定分钟数，出门前自己用交通
    App 查"。这是本篇最有信息量的一段，也是 008 砍掉"火车站 5 分钟"那条做法的正向延伸。
  - **门牌号 87-91 vs 87-93**：官网 contact 页写 87-93，但 events.json、Eventbrite 售票页、
    Broadsheet、Time Out 四处均为 87-91。采信 87-91(读者实际会点进去的售票页口径)，冲突
    已记录在核查表备注里。
  - **营业时间只发布一半**：官网原文 "MONDAY - TUESDAY: 4PM-12PM" 自相矛盾(4PM 到 12PM
    不成立，疑为 12AM 笔误)，搜索摘要另有 4pm–10pm / 4pm–late 两种版本。**开门 4PM 是各
    来源唯一一致的部分，只写这一半，完全不写打烊时间。**
- **主动排除**：票价(该条目 price=null)、地下室容量/座位数、入场安检与包尺寸政策(该场馆
  无公开 Conditions of Entry 页，**不能套用 Marvel/ENGIE 的体育场条款**)、停车、演员阵容、
  场馆电话。详见 011 文末"主动排除项"。
- **卡片数改为 3 张(比 004/008 的 4 张精简)**：prompt 对场馆攻略建议 2–3 张。这个场馆的
  可核实事实密度本来就低于体育场(无入场条款页、无停车费率表、交通数字被砍)，硬撑 4 张
  必出凑数卡。现结构 封面／场馆4条／收尾CTA，三张都满。P3 保留账号档案写死的固定 kicker
  「澳华演出雷达 · 玩转布里斯班」作品牌锚。
- 模板复制自 `cards/010/index.html`，已 `diff` 确认第 1–840 行(`<head>`+CSS)除 `<title>`
  外与 010 完全一致，`</main>` 之后的脚本块逐字节相同；`data-theme="aushow"`、主题色 token、
  字体、`.ticket`/`.ledger`/`issue-strip` 全部原样保留，只改 poster 区块 + `<title>`。
- 已按 `render_card.py` 第 87–88 行的 `html_no_comments` 逻辑实跑验证：剥掉注释后恰好 3 个
  `<section class="poster xhs">`(id `xhs-01`…`xhs-03`)，模板顶部示例注释不会被误计。
  另已比对 `run_daily_xhs.sh` 第 55–64 行的关卡条件，FACT-AUDIT-STATUS 行可通过。
- 本次会话按 `daily-xhs-prompt.md` 第 0 节，**未调用任何浏览器/截图工具**，渲染与 Telegram
  推送留给 `run_daily_xhs.sh` → `render_card.py`。
- ⚠️ **组合治理(连续第六天提醒)**：PORTFOLIO.md 最后评审仍停在 2026-07-11(超 14 天心跳
  阈值)。AuShow 杀死标准"若 08-24 后仍未实际发布，下次评审自动转判定"**已逾期第 5 天**。
  内容侧已积压 11 篇待发，瓶颈完全在人工发布这一步，不在生产线。建议尽快跑 /portfolio-review。
- ⚠️ **verified 池子现状(与昨天一致，未改善)**：8 条 verified 中实际可用仍只有 4 条
  (周杰伦 2 + 开放麦 2)，且 4 条**全部已被单场安利过**。EXCEPTIONS 里 AKMU 两条仍未修。
  **明天(08-30 周日)轮换位=转票防骗指南，不依赖 verified 池，可正常产出**；但下周一
  (08-31)的"单场演出安利"会再次撞空池，届时只能按 prompt 第 2 步换角度重讲最久没安利过
  的那条(周杰伦墨尔本站，001 用过)。补池最快动作仍是修 AKMU 两条。

## 2026-09-01(周二) — 第 013 篇

- **选题类型**：转票防骗指南(周二轮换位)。不依赖 verified 池，本次未消耗任何演出条目。
- **fact-audit 结果**：RED=0，CHECKED=15，SOURCES-CITED=15，全部 GREEN，无需改稿。
  15 条中 5 条来自 NAB PayID 诈骗页(WebFetch 直接抓取成功)、3 条来自 Scamwatch
  buying-and-selling-scams 页(WebFetch 直接抓取成功)、3 条来自 Scamwatch overpayment-scams
  页(该 URL 直接 WebFetch 被重定向到 buying-and-selling 页，改用 WebSearch 对该官方 URL 做
  **两次独立正文抽取、结果一致**后才采信)、4 条来自 Ticketek Marketplace 帮助页与 Seller
  FAQs(两个 URL 直接 WebFetch 均 403，沿用 003/007 已确立的 WebSearch 抽取取证方式)。
- **角度选择(本篇是同选题第 4 篇，重复风险最高的一次)**：动手前先 grep 了 003/007/012 的
  关键词分布，确认 012 已把 chargeback/拒付写透(出现 14 次)、003 已用掉"新条码/原票作废/
  票面价上限"、007 已用掉"官方转售分场次不分平台"。因此**整体换到卖家视角**——前三篇主角
  全是买家，"你多出一张票要出手反被骗"这一半在账号里从未写过。三个套路(冒用 PayID 商家
  账户、多付退差额、不看货就买+要你替转钱)与前三篇零重叠。
- **主动剔除**：媒体转述的被骗金额统计(2023 年口径，非 Scamwatch 官方页原文，且 012 已
  声明不复用损失数字)；Scamwatch 那句 "make sure the name matches the person you think
  you're paying"——**原文主语是付款方，属买家视角，套到卖家身上会曲解官方口径，整句不写**；
  其他二级平台的卖家费率与结款细节(未核到官方原文)。详见 013 文末"主动剔除项"。
- **红线处理**：PayID 本身没有问题，全篇统一写"冒用 PayID 名义"，不写成"PayID 不安全"；
  不点名任何个人/账号/二级转售站。
- 卡片数 4 张，模板复制自 `cards/011/index.html`，已 `diff` 确认第 1–836 行(`<head>`+CSS)
  除 `<title>` 外与 `cards/001/index.html` 完全一致，`</main>` 之后的脚本块与 011 逐字节相同；
  `data-theme="aushow"`、主题色 token、字体、`.ticket`/`.ledger`/`issue-strip` 原样保留。
- 已按 `render_card.py` 第 87–88 行的 `html_no_comments` 逻辑实跑验证：剥掉注释后恰好 4 个
  `<section class="poster xhs">`(id `xhs-01`…`xhs-04`)，section 开闭配平，模板顶部示例注释
  未被误计。另已实跑 `run_daily_xhs.sh` 第 55–62 行的关卡条件，判定 PASS。
- 本次会话按 `daily-xhs-prompt.md` 第 0 节，**未调用任何浏览器/截图工具**，渲染与 Telegram
  推送留给 `run_daily_xhs.sh` → `render_card.py`。
- 🔴 **发现前两天的运行都被 Claude 月度额度上限打断(已写入 EXCEPTIONS OPEN)**：查
  `automation/logs/2026-08-30.log` 与 `2026-08-31.log`，两天都是同一条根因——
  `You've hit your monthly spend limit … your session limit resets …` → `FAILED: claude 非零退出`。
  - 08-30 断在第 5 步之后：`content/012-xhs-copy.md` 已完整写出(fact-audit RED=0 CHECKED=12，
    文案可用)，但脚本随即判定 `FAILED: 找不到 content/cards/012/index.html,claude 写完文案
    但没建卡片 HTML`；`git log --all -- 'content/cards/012*'` 全历史无记录，确认该 HTML
    **从未存在**，即 012 从未出图、从未推送。今天已补记 posted-log 的 012 行。
  - 08-31(周一，轮换表=单场演出安利)断得更早：`FAILED: 没有产出新的 NNN-xhs-copy.md 文件`，
    整篇缺失。连同 012 一起，**过去 3 天实际只完成了今天这 1 篇**。
  - **脚本的失败检测本身是正常工作的**，日志里两条 `FAILED:` 都写得很清楚；漏掉的是这些
    失败没有推到 Telegram，也没人翻日志，所以静默积压了两天。建议把 `run_daily_xhs.sh`
    的 `FAILED:` 分支也推一条 Telegram，让失败和成功一样能被看见。
- ⚠️ **组合治理(连续第七天提醒)**：PORTFOLIO.md 最后评审仍停在 2026-07-11(超 14 天心跳
  阈值)。AuShow 杀死标准"若 08-24 后仍未实际发布，下次评审自动转判定"**已逾期第 8 天**。
  内容侧已积压 12 篇待发(001–013 中除 012 缺图外均已成稿)，瓶颈完全在人工发布这一步。
  建议尽快跑 /portfolio-review。
- ⚠️ **verified 池子现状(与上次一致，未改善)**：今天 `data/events.json` 新增了 1 条
  「国家话剧院《四世同堂》」(悉尼，2026-04-16)，但 `verified=false`、`status=tbc`、
  `ticket_platform` 与 `ticket_url` 均为 null，**不可用**。8 条 verified 中可用仍只有 4 条
  (周杰伦 2 + 开放麦 2)，且全部已被单场安利过；EXCEPTIONS 里 AKMU 两条仍未修。
  **明天(09-02 周三)轮换位=场馆攻略，不依赖 verified 池，可正常产出。**

## 2026-09-03(周四) 值班日志

- ✅ **今天发第 14 篇：`014-xhs-copy.md`，选题类型=本周开票汇总**(周四轮换位)。
  4 张卡：封面 / 人在悉尼 / 人在墨尔本 / 收尾 CTA。`content/cards/014/index.html` 已建
  (复制自 009，同栏目同版式)，主题色 token、`.ticket`/`.ledger`/`issue-strip` 组件样式
  原样保留，仅替换 4 个 poster 区块文案 + `<title>`。渲染留给 `render_card.py`。
- ✅ **fact-audit：RED=0 CHECKED=26 SOURCES-CITED=26**。4 条演出全部另做外部复核，
  重点复核了**周杰伦两场是否仍由 Ticketmaster 承接**(AKMU 就是栽在 `ticket_platform`
  随场馆换票务商而失真)——Ticketmaster 官方巡演页今日仍列这两场、墨尔本场标
  "On Sale Now!"，未发现换票务商迹象。票价区间两场也都拿到了外部票档佐证
  (悉尼 188–748、墨尔本 208–748 +$9.90 手续费)。
- ⚠️ **审计查出 1 处 events.json 字段已过期，本篇已绕开**：Loadingzone 条目 `notes` 写的是
  "双语喜剧厂牌"，但今日 Eventbrite 主办方页原文是"澳洲**华语**文化厂牌"、Club Voltaire
  场次页是 "the only **Mandarin Speaking** Comedy club in Melbourne"，两处一手信源口径
  都不是"双语"(009 当时引的那句"专业双语喜剧厂牌"该页已改版)。文案已改写为"华语喜剧
  厂牌"，只保留两处信源共同支持的表述。**请同步修 `data/events.json` 的 notes 字段**，
  已写入 EXCEPTIONS OPEN。
- ⚠️ **可用池与 009 完全相同，本篇靠角度避免重复**：袁娅维两场早已过期、AKMU 两场仍在
  EXCEPTIONS OPEN 且 `data/events.json` 截至今日未修改，剩下的仍是周杰伦 2 + 开放麦 2。
  本篇改按**城市**切分(悉尼 2 场 / 墨尔本 2 场，每城一大一小)，与 005 的时间线、009 的
  "大场 vs 常驻"两种切分都不重叠，并首次点明"两场大的都不在布里斯班"这一老粉实际处境。
  **但这个办法有次数上限**——同一个 4 条池子已经连出 3 篇汇总，再来一次很难不重复。
- 🔴 **昨天(09-02 周三，轮换位=场馆攻略)整篇缺失，且又是静默失败**。
  `automation/logs/2026-09-02.log` 里写得很明确：`Failed to authenticate: OAuth session
  expired and could not be refreshed` → `FAILED: claude 非零退出` → `FAILED: 没有产出新的
  NNN-xhs-copy.md 文件`。**这是继 08-30/08-31 的额度耗尽之后，5 天内第 3 次静默失败**，
  这次换了个根因(OAuth 过期，不是额度)。`run_daily_xhs.sh` 的 `FAILED:` 分支仍然不推
  Telegram —— 8 月 31 日 RUNBOOK 里已经提过这条建议，至今未改，所以昨天又白丢一天没人知道。
  需要的动作：①重新登录/续期 Claude OAuth；②**把 `FAILED:` 分支也推一条 Telegram**
  (这条再不做，后面每次失败还是要靠人翻日志才发现)。
- ⚠️ **AKMU 两场进入最后窗口**：09-18(墨尔本)距今只剩 15 天、09-20(悉尼)只剩 17 天。
  两条从 08-24 挂到现在没修，再拖就会像袁娅维那两场一样直接过期作废，白白浪费 2 条
  verified 条目。修法在 EXCEPTIONS 里写得很具体(墨尔本站 `ticket_platform` 改 AXS 并换
  `ticket_url`；悉尼站场馆名改成购票页当前口径、补 `price`/`time`)。
- ⚠️ **组合治理(连续第八天提醒)**：PORTFOLIO.md 最后评审仍停在 2026-07-11(超 14 天心跳
  阈值)。AuShow 杀死标准"若 08-24 后仍未实际发布，下次评审自动转判定"**已逾期第 10 天**。
  内容侧积压 13 篇待发(001–014 中除 012 缺卡片 HTML 外均已成稿)，瓶颈完全在人工发布这一步。
  建议尽快跑 /portfolio-review。

## 2026-09-04(周五) 值班日志

- ✅ 第 **015** 篇已成稿：`content/015-xhs-copy.md` + `content/cards/015/index.html`(4 张
  `poster xhs`，`data-theme="aushow"` 主题色 token 与 `.ticket`/`.ledger`/`issue-strip`
  组件样式原样保留，head/CSS 与 tail 逐行比对与 001 一致，仅 `<title>` 和四个 poster
  区块内文案不同)。渲染按提示词第 0 步交给 `render_card.py`，本次会话未调用任何截图工具。
- 选题类型：**单场演出安利**(周五轮换位)。fact-audit：**RED=0 CHECKED=13 SOURCES-CITED=13**，
  未发现需要改文案的问题。
- 🔴 **未安利池仍然是空的，本篇是第一次触发"换角度重讲"分支**。8 条 verified 里：周杰伦
  墨/悉已由 001/002 用过、Rolling Donkey 由 006、Loadingzone 由 010；袁娅维两场演出日已过；
  AKMU 两场仍不可发。按提示词第 2 步取四条已用条目里最早的一条(001，约 19 天前)=周杰伦
  墨尔本站，角度换成**距开演 43 天的倒计时**，落点在 001 只当 bullet 列过的「限购 6 张」
  和「$208–$748 价位跨度」上，避开 004 已写透的 Marvel Stadium 场馆攻略。
- ✅ **本次做了 events.json 之外的独立复核**(该条目 `verified` 打于 07-03，已隔 2 个月，
  且有 AKMU 字段失真的前车之鉴)：Ticketmaster 官方页今日仍标 "On Sale Now!"、
  "a maximum of 6 tickets per person"、"organised by Sky Music and Horizon Production"；
  Marvel Stadium 官方页为 "17 October 2026 (Saturday)" / "7:30 PM" / "Marvel Stadium
  (Melbourne)"。日期/时间/场馆/状态/限购/主办方**六项全部与 JSON 一致，无失真**。
- ⚠️ 唯一没拿到第二信源的字段是**票价 $208–$748(+$9.90)**——今日 Ticketmaster 汇总页与
  Marvel Stadium 官方页都不展示票价。判 GREEN 的依据是 events.json 的 verified 字段本身
  (001 用的同一值)，且**未发现任何相反证据**；卡片保留"下单前建议官网复核"提示。
- ⚠️ 注意一处口径差：官方页写的是"每人最多 6 张"，events.json notes 写的是"每账户限购6张"。
  上限同为 6，文案取 JSON 逐字表述；也正因为两者有差异，本篇**刻意不给"拆两个账号下单"
  之类的操作建议**(可能触及购票条款)。
- 🔴 **AKMU 墨尔本站(09-18)只剩 14 天，悉尼站(09-20)只剩 16 天**——从 08-24 挂到今天已 11 天，
  `data/events.json` 相关字段仍未改动。再拖两周就会像袁娅维那两场一样直接过期作废，
  verified 池永久少 2 条，而这是目前唯一的增量来源。修法见 EXCEPTIONS。
- 🔴 **`run_daily_xhs.sh` 的 `FAILED:` 分支至今仍不推 Telegram** —— 这条建议 08-31 提过、
  09-03 又提过，5 天内 3 次静默失败(08-30/08-31 额度、09-02 OAuth)都是靠人翻日志才发现的。
  这是整条流水线目前最便宜也最该做的一个改动。
- ⚠️ **组合治理(连续第九天提醒)**：PORTFOLIO.md 最后评审仍停在 2026-07-11(超 14 天心跳阈值)。
  AuShow 杀死标准"若 08-24 后仍未实际发布，下次评审自动转判定"**已逾期第 11 天**。内容侧
  现积压 14 篇待发(001–015 中除 012 缺卡片 HTML 外均已成稿)，瓶颈完全在人工发布这一步。
  建议尽快跑 /portfolio-review。

## 2026-09-05(周六) 值班日志

- ✅ 第 **016** 篇已成稿：`content/016-xhs-copy.md` + `content/cards/016/index.html`(**5 张**
  `poster xhs`，id `xhs-01`…`xhs-05` 连续)。HTML 由 `cards/001/index.html` 复制而来，
  `<html data-theme="aushow">` 与顶部主题色 token、整体 CSS、字体、`.ticket`/`.ledger`/
  `issue-strip` 组件样式**原样保留**——已逐行 diff 确认：第 1–853 行与 001 唯一差异是
  `<title>`，尾部 33 行完全一致。渲染按提示词第 0 步交给 `render_card.py`，本次会话
  **未调用任何浏览器/截图工具**。
- 选题类型：**场馆攻略**(周六轮换位)。fact-audit：**RED=0 CHECKED=20 SOURCES-CITED=20**，
  未发现需要改文案的问题。
- 场馆选 **Margaret Court Arena**(Melbourne Park)——verified 池里日期最近的一场
  (AKMU 墨尔本站 2026-09-18，距今 13 天)的场馆，也是**第一个中型室内 arena**：
  004=Marvel Stadium、008=ENGIE Stadium 是露天大球场，011=Chippo Hotel 是酒吧地下室。
- 🆕 **本篇角度是四篇场馆攻略里第一次以"票务"为主角**，不是又一篇"包能带多大"。
  Melbourne Park 自 2026-08-22 起把官方票务伙伴换成 AXS，过渡期未完，官网原话是
  "你的票由 AXS 还是 Ticketek 提供，取决于你看的是哪场"；AKMU 这场的官方活动页已明写
  "Ticketek ticket purchases for AKMU have been issued by AXS"，且 ticketing 页保证
  旧订单"仍然有效、座位分配不受影响"。对手里已经有票的读者，这比入场规则要紧得多，
  而且天然接得上账号的防诈支线(官网自己点名了一串未授权转售站，本文按红线**不复读站名**，
  只给"不是场馆认的那两个出票系统就没人兜底"这个判断标准)。
- ⚠️ **红线处理**：AKMU 墨尔本站自 08-24 起就挂在 EXCEPTIONS OPEN(`ticket_platform=Ticketek`
  与官方 AXS 口径冲突、`price`/`time` 为 null)，**本篇因此只用它的"日期+场馆"两个字段**
  作时间锚点，不写票价、不写开演时间(官网有 7:00pm，但 JSON `time=null`，按红线不补)、
  **不给任何购票入口指引**。文中写的是"已买的票由谁出票"这一官网已公布的事实，与
  "去哪买票"是两件事，doc 里已单列说明。该条目**未被消耗**，仍留在未安利池。
- 🔴 **AKMU 墨尔本站(09-18)只剩 13 天、悉尼站(09-20)只剩 15 天**，从 08-24 挂到今天已 12 天，
  `data/events.json` 仍未改动。今天写这篇时又拿到一条更硬的证据：场馆官方活动页现在
  直接写着 AKMU 的 Ticketek 票已由 AXS 出票，即 JSON 里的 `ticket_platform` 与
  `ticket_url`(premier.ticketek.com.au 深链)**已确定是错的**，不是"存疑"。再拖两周这两条
  就会像袁娅维那两场一样过期作废，verified 池永久少 2 条。已追加到 EXCEPTIONS OPEN。
- 🔴 **`run_daily_xhs.sh` 的 `FAILED:` 分支至今仍不推 Telegram** —— 08-31、09-03、09-04
  已连提三次。5 天内 3 次静默失败(08-30/08-31 额度、09-02 OAuth)全靠人翻日志才发现。
  仍是整条流水线目前最便宜、性价比最高的一个改动。
- ⚠️ **组合治理(连续第十天提醒)**：PORTFOLIO.md 最后评审仍停在 2026-07-11(超 14 天心跳
  阈值)。AuShow 杀死标准"若 08-24 后仍未实际发布，下次评审自动转判定"**已逾期第 12 天**。
  内容侧现积压 15 篇待发(001–016 中除 012 缺卡片 HTML 外均已成稿)，瓶颈完全在人工发布
  这一步——内容产能不是问题，已经连着两周每天出稿。建议尽快跑 /portfolio-review。

### 2026-09-06 值班日志(小红书日更)

- 产出第 **017** 篇：《你的票，可能在账号里被卖掉》，选题类型 **转票防骗指南**(周日轮换位)。
- 文件：`content/017-xhs-copy.md` + `content/cards/017/index.html`(5 张 `.poster.xhs`，
  沿用 `data-theme="aushow"` 主题色与 `.ledger`/`issue-strip` 组件，无 `<img>`、无票根卡)。
- **fact-audit：RED=0，CHECKED=15，SOURCES-CITED=15**，全部 GREEN。
- 核查中发现并处理的问题(未带进文案)：
  1. `cyber.gov.au`(ACSC)的 MFA 页当日 **3 次 WebFetch 全部 60s 超时**，只拿得到搜索
     摘要、拿不到一手页面 → 原计划的 ACSC "MFA 是最有效手段之一"与 credential stuffing
     定义**整段删除**，文案中不出现 ACSC 任何表述。
  2. OAIC 可通报数据泄露报告：官方发布页当日抓取显示最新报告仅到 **2024 年下半年**，而
     搜索结果里的 2025 年占比数字**全部来自二手博客**，一手对不上 → 整条统计删除。
  3. `help.ticketek.com.au` 与 `premier.ticketek.com.au` 当日分别返回 **403 / 超时** →
     Ticketek 的 MFA 操作细节(验证码发到哪、何时触发)一律不写，该公司相关表述**只采用
     ABC 报道里它自己的公开表态**。
- 红线自查：不点名任何个人/账号/二级转售平台；Ticketmaster/Ticketek 均为一级官方售票方
  的正面引用。**措辞特别校正**：ABC 原文写的是账号密码来自**第三方网站泄露**，文案严格
  照此表述，未写成"票务平台泄露了你的密码"，避免责任归因错误。
- 主动设限：不引任何统计数字(007/012 用过的报损与报案数一个都不复用，也不新引)；
  不承诺账号被盗后票一定能找回(Ticketek 表态原样写成"会与客户一起处理")。
- 按提示词第 0 步，本次会话**未调用任何截图/浏览器工具**，渲染交由 `run_daily_xhs.sh` →
  `automation/render_card.py` 完成。
- ⚠️ 仍未解除的上游问题(与本篇无关，沿袭前几日)：`data/events.json` 里 AKMU 两场自
  08-24 起挂 EXCEPTIONS OPEN 未修；`content/cards/012/` 卡片 HTML 仍缺失。
- ⚠️ 组合层提醒：PORTFOLIO.md 2026-09-06 评审已把 AuShow 杀死标准改为
  **12 周净新增 500 小红书粉丝 + 每周至少实际发布 3 篇**(时钟仍从 08-16 起算，
  2026-11-08 到期)。内容侧已积压 001–017 共 17 篇待发，**瓶颈全在人工发布这一步**——
  "每周发 3 篇"是新 KPI 的硬前提，不达标会被直接判为执行失败、不算市场证伪。

### 2026-09-07 值班日志(小红书日更)

- 产出第 **018** 篇：《悉尼这场为什么叫「海洋」》，选题类型 **单场演出安利**(周一轮换位)。
- 文件：`content/018-xhs-copy.md` + `content/cards/018/index.html`(5 张 `.poster.xhs`，
  复制自 `cards/001/index.html`，保留 `data-theme="aushow"` 主题色 token 与
  `.ticket`/`.ledger`/`issue-strip` 组件样式，仅替换 poster 区块内文案)。
- **fact-audit：RED=0，CHECKED=19，SOURCES-CITED=19**，全部 GREEN，未发现事实错误。
- 选场：**第二次"换角度重讲"**。未安利池仍为空(AKMU 两场自 08-24 起挂 EXCEPTIONS OPEN，
  `data/events.json` 至今未修；袁娅维两场已过期)，按提示词第 2 步取四条已用条目里最久
  没被安利过的一条——**002 用过的周杰伦悉尼站**(2026-08-17，21 天前)。
- 角度：**「名字」**。悉尼站叫「海洋」、墨尔本站叫「粉色」，这两个主题词一直写在
  `title_zh` 里，002/008/014/015 四篇一次都没解释过。今日核实确认是该巡演"一城一主题"
  的设定，且两词合起来正好是《最伟大的作品》第 10 首《粉色海洋》。这是**只有这场给得出**
  的内容，不是把 002 换个说法重排。
- 因该条目 `verified` 打于 07-03 已隔 2 个月(有 AKMU 字段失真前车之鉴)，今日逐条独立复核：
  Sydney Showground 官方活动页 "Saturday 21 November" / "6:00pm – Gates open" /
  "7:30pm – Event starts" / "Tickets are officially on sale now"；Ticketmaster 巡演页
  "maximum of 6 tickets per person" / "organised by Sky Music and Horizon Production"。
  与 `events.json` 全部一致，**未发现失真字段**。
- 核查中主动剔除、未带进文案的内容：
  1. "城市主题灵感源自《粉色海洋》这首歌"——因果说法只见于二手媒体，维基百科巡演词条
     未写灵感出处，官方页面亦无 → 只保留"两个主题词合起来是这首歌的名字"这一可核对事实。
  2. "悉尼站 AR 沉浸式舞台""墨尔本站花瓣雨"——仅二手媒体，官方场馆页只有笼统描述 → 整条不写。
  3. 检索结果中出现的"悉尼超级穹顶"场馆说法与官方口径(ENGIE Stadium)冲突，属二手媒体
     错误 → 不采用。
  4. "悉尼站是澳洲收官场/最后一场"——官方无 final show 字样 → 只写"澳洲一共只排了两场"。
- 一处**刻意的分层处理**：Ticketmaster 艺人页今日两场状态标签均为 "Low Availability"，
  这是有价值的一手观察，但属会变的瞬时标签 → **只在正文带 09-07 日期引用一次并注明
  "是平台标签、不是余票数字"，不进任何一张卡片**(卡片是发布后长期留存的物料)。
- 红线自查：日期/场馆/票价/平台/限购/主办方逐字取自 `verified=true` 条目；正文无外链；
  封面沿用 002 的处理，alt 写"澳洲巡演官方宣传图"而非"悉尼站海报"(该图为巡演通用头图)；
  未点名任何转售个人/账号。
- 按提示词第 0 步，本次会话**未调用任何截图/浏览器工具**，渲染交由 `run_daily_xhs.sh` →
  `automation/render_card.py` 完成。
- ⚠️ 仍未解除的上游问题(与本篇无关，沿袭前几日)：AKMU 墨尔本站演出日 **09-18 只剩 11 天**、
  悉尼站 **09-20 只剩 13 天**，`data/events.json` 相关字段自 08-24 挂出至今 14 天未修，
  再不修这两条会像袁娅维那样直接过期作废，verified 池将永久少 2 条；
  `content/cards/012/` 卡片 HTML 仍缺失。
- ⚠️ 组合层提醒：AuShow 新杀死标准是 **12 周净新增 500 小红书粉丝 + 每周至少实际发布 3 篇**
  (时钟从 08-16 起算，2026-11-08 到期)。内容侧已积压 001–018 共 18 篇待发，
  **瓶颈仍全在人工发布这一步**——"每周发 3 篇"是硬前提，不达标会被判执行失败、
  不算市场证伪。

### 2026-09-08 值班日志(小红书日更)

- 产出第 **019** 篇：《白送你的票，最贵》，选题类型 **转票防骗指南**(周二轮换位)。
- 文件：`content/019-xhs-copy.md` + `content/cards/019/index.html`(5 张 `.poster.xhs`，
  沿用 `data-theme="aushow"` 主题色与 `.ledger`/`issue-strip` 组件，无 `<img>`、无票根卡；
  head/CSS 逐字复制自 `cards/001/index.html`，仅改 `<title>` 与 5 个 poster 区块内文案)。
- **fact-audit：RED=0，CHECKED=20，SOURCES-CITED=20**，全部 GREEN，未发现需要改文案的问题。
- 选题角度(第 6 篇防骗，避重复的关键)：前五篇读者能用的判断工具全部建立在**"有一笔钱在动"**
  上——比价格、看平台、查转账方式、核对原价上限(017 虽无交易，但主角是账号安全)。
  本篇这一类**开局不谈钱**：它送你一张票 / 说你中奖 / 说是粉丝福利，那套工具一条都用不上，
  收费点被推到后段("先给身份资料 → 再付运费/税费/手续费")。
  **与 003 的边界已写进正文**：003 的"被盗号朋友"是**卖家**(有价格、有交易，你会本能设防)；
  本篇的熟人**不卖你东西、不要你一分钱**，只是替一个"奖"作证说"我也中了"——防线不触发，
  这正是本篇要补的那一格。
- 四个信源在 003/007/012/013/017 中**均未出现过**：Scamwatch 中奖/竞赛/彩票类骗局页、
  社交平台假中奖官方预警(2015-08-13)、Scamwatch 真实案例页(Davin)、Scamwatch 社交平台
  骗局页。
- 核查中主动剔除、未带进文案的内容：
  1. Ticketmaster AU 帮助中心"发现可疑站点或冒名邮件怎么办"页当日 **WebFetch 返回 403**
     (与 017 当日 Ticketek 帮助中心 403 同类) → 整段删除，本篇**不出现任何票务平台的
     官方表述**。
  2. 中国驻墨尔本总领事馆 2025-04-09 演出门票诈骗领事提醒：核实后其内容是"低价转让/
     内部渠道"与事后"二次收割"退款诈骗，与 003/007/012 已写过的角度重叠，**不属本篇
     这一支** → 不采用(信息本身属实)。
  3. ACCC 某巡演门票诈骗媒体稿 → 003 已用过 Scamwatch 同一事件的警示页与报案人数，
     不复用同一事件。
  4. Scamwatch 另两则旧预警(2013-09-18 假问卷/假免费优惠、2012-06-30"代金券中奖"短信)
     确为一手页面，但主体分别是超市代金券问卷与高价手机订阅服务，离演出票场景太远 →
     不用来凑条数。
- 红线自查：不点名任何个人/账号/社群/主办方/转售平台；全篇无具体演出的日期/票价/场馆；
  正文无外链。**特别设限**：不做流行度断言(没写"澳洲演出圈最近大量出现送票骗局"这类
  无一手数据的话)，所有事实取自 Scamwatch 对该类骗局的通用官方描述，落到演出票上的部分
  一律以"这套模板放到票上就是……"写成**应用与建议**，不伪装成对票务圈的统计事实；
  Davin 个案的 250/1500 澳元在正文与卡片上都标注为**个案金额、非行业数据**；
  不复述 017 的 "Stop. Check. Protect." 与 007 的"礼品卡退款"表述。
- 按提示词第 0 步，本次会话**未调用任何截图/浏览器工具**，渲染交由 `run_daily_xhs.sh` →
  `automation/render_card.py` 完成。
- ⚠️ 仍未解除的上游问题(与本篇无关，沿袭前几日)：AKMU 墨尔本站演出日 **09-18 只剩 10 天**、
  悉尼站 **09-20 只剩 12 天**，`data/events.json` 相关字段自 08-24 挂出至今 **15 天**未修，
  再不修这两条会像袁娅维那样过期作废，verified 池将永久少 2 条；
  `content/cards/012/` 卡片 HTML 仍缺失。
- ⚠️ 组合层提醒：AuShow 杀死标准为 **12 周净新增 500 小红书粉丝 + 每周至少实际发布 3 篇**
  (时钟从 08-16 起算，2026-11-08 到期；PORTFOLIO.md 最后评审 2026-09-06，节律内)。
  内容侧已积压 001–019 共 19 篇待发，**瓶颈仍全在人工发布这一步**——"每周发 3 篇"是硬前提，
  不达标会被判执行失败、不算市场证伪。

## 值班日志 — 2026-09-09（周三）

- 今天生成 **第 020 篇**，选题类型 **场馆攻略**（周三轮换位）。
- 场馆取 verified 条目「AKMU 乐童音乐家 澳洲演唱会 悉尼站」（2026-09-20，距今 11 天，
  verified 池里日期最近的一场）的场馆。本篇**只用该条目的日期+场馆两个字段**，不写票价、
  不写开演/入场时间（JSON 中 `price`/`time` 均为 `null`，场馆官方活动页也未公布 doors/
  show time），因此**不消耗单场安利池**，该条目仍可在字段修复后另行安利。
- 品类与角度均为首次：004=Marvel Stadium、008=ENGIE Stadium（露天大球场）、011=Chippo
  Hotel（酒吧地下室）、016=Margaret Court Arena（中型室内 arena）；本篇是**第一座"开在
  会展中心里的剧院"**，也是**第一座悉尼室内场馆**。主角是**场馆改名**（events.json 仍写
  旧名 `ICC Sydney Theatre`；官方 FAQ：2025-11-25 正式更名 TikTok Entertainment Centre），
  与 016 的"票务伙伴换了"不重叠。
- **fact-audit 结果：RED=0，CHECKED=31，SOURCES-CITED=31**，无需改稿。31 条断言全部落在
  `tiktokentcent.com`（场馆官方站：event / getting-here / conditions-of-entry /
  general-admission / faq）与 `iccsydney.com.au`（运营方官方新闻页）六个页面，逐条留 URL。
  本次抓取**未出现 403/超时**（对比 017 的 Ticketek 帮助中心、019 的 Ticketmaster 帮助中心
  当日均 403）。
- **本次核实顺带解掉 AKMU 悉尼站的一个卡点**：该条目 `ticket_platform=Ticketek`
  **与场馆官方口径一致**——官方 FAQ 原文 "Ticketek is the only authorised ticket seller
  for entertainment events held at TikTok Entertainment Centre."，官方活动页 BOOK TICKETS
  指向 `premier.ticketek.com.au`。这与 016 处理的**墨尔本站**（`ticket_platform=Ticketek`
  与场馆官方 AXS 口径冲突）是两回事，请勿混为一谈。悉尼站现在只剩两个卡点：
  `price`/`time` 仍为 `null`、`venue` 写的是旧名。已写入 EXCEPTIONS OPEN 供用户修。
- 主动剔除、未进文案的内容：二手票务站标的 "Sold Out"（瞬时标签 + 非一手信源，沿用 018
  对 "Low Availability" 的处理）；"去哪买票"的购买指引（价格与时间仍 null，给指引会诱导
  读者去补一个本篇没核实的信息，因此只写"谁是授权售票方"这条场馆规则）；未授权转售渠道
  的具体名称（账号红线）；冠名交易的商业细节与营销数字；停车价格（官网未给）；视野推荐
  （官网无）；再入场 pass out 规则（本场馆官网未涉及，不照搬 016 的 Margaret Court Arena）。
- 按提示词第 0 步，本次会话**未调用任何截图/浏览器工具**，渲染交由 `run_daily_xhs.sh` →
  `automation/render_card.py` 完成。
- ⚠️ 仍未解除的上游问题：**AKMU 墨尔本站演出日 09-18 只剩 9 天、悉尼站 09-20 只剩 11 天**，
  `data/events.json` 相关字段自 08-24 挂出至今 **16 天**未修。再不修这两条会像袁娅维两场
  那样直接过期作废，verified 池将永久少 2 条（8 条中的 2 条）。`content/cards/012/` 卡片
  HTML 仍缺失。
- ⚠️ 组合层提醒：AuShow 杀死标准为 **12 周净新增 500 小红书粉丝 + 每周至少实际发布 3 篇**
  （时钟从 08-16 起算，2026-11-08 到期；PORTFOLIO.md 最后评审 2026-09-06，在 14 天节律内，
  本次不触发评审提醒）。内容侧已积压 **001–020 共 20 篇待发，瓶颈仍全在人工发布这一步**
  ——"每周发 3 篇"是硬前提，不达标会被判执行失败、不算市场证伪。

## 值班日志 — 2026-09-10（周四）

- **第 021 篇**，选题类型 **本周开票汇总**（周四轮换位）。产出
  `content/021-xhs-copy.md` + `content/cards/021/index.html`（4 张卡）。
- **fact-audit：RED=0，CHECKED=26，SOURCES-CITED=26。** 核查过程中发现并处理了 **3 处
  需要主动剔除的冲突/存疑内容**（详见文件内核查表）：
  1. **墨尔本站起价冲突（核查表第 6 行，判 AMBER）**：一处二手来源把墨尔本站写成
     "248澳元（山顶票）至748澳元（VIP区）"，与 `events.json` 的 `$208` 及今日拿到的
     完整档位表冲突（该档位表同时含 $248 与 $208 两档，即该来源很可能漏记了最低档）。
     处理=**只写价格数字，不写任何座位区域名称**——座位描述仅此一处来源，而该来源在
     相邻数字上已被证伪。
  2. **"门票绑定观演人证件，不支持转赠或转售"**：仅见于同一处二手来源，Ticketmaster
     官方巡演页与两处档位表来源均无此说法。这是一条会直接影响读者能不能走官方转售的
     **强规则断言**，单一二手来源不足以支撑，整条剔除。
  3. **"$348 以上有余票"**：瞬时余票状态，沿用 018 对 "Low Availability" 的处理，
     不进正文也不进卡片，只写"余票落在哪一档随时会变，以官方页面为准"。
- **本篇解决了 `EXCEPTIONS.md` 2026-09-03 那条预警**（"本周开票汇总的可用池已连出 3 篇，
  靠换角度避重复快到上限，下一次周四轮换 09-10 大概率只能重复"）。找到的第四种切分是
  **按票价档位排**——`price` 是这批条目里唯一一个从未被当作组织原则的字段：005 按时间线、
  009 按提前量、014 按城市，三篇都只把 "$208–$748" 当行末括注顺手列一下，没有一篇
  拿它当主线。本篇把 4 场按"官方票价现在能不能查到"分两档，落点接到账号核心差异化
  （官方票面是防骗标尺）。**预警已解除，但只解除这一次**——见下方遗留问题。
- **顺带补上了一个一直没做的核实**：整篇主线是票价，而 `price` 字段此前**从未被独立
  核实过**（009 核查表第 5 行明确记过 "Ticketmaster 汇总页不列价，指向各场次页"，即
  前三篇的票价数字一直只有 `events.json` 单一来源）。今日为两站各找到一个列出完整
  档位表的外部来源，两站均为 **7 档、最高档同为 $748**，最低档 墨 $208 / 悉 $188，
  **与 `events.json` 的区间端点完全一致**——即该字段经受住了独立复核，未发现失真。
  这也是本篇新增的内容块（前三篇只有区间端点，没有档位结构）。
- 按提示词第 0 步，本次会话**未调用任何截图/浏览器工具**，渲染交由 `run_daily_xhs.sh` →
  `automation/render_card.py` 完成。
- ⚠️ **遗留问题（本次未新增，均为上游未解除项）**：
  - **AKMU 两场演出日已进入最后窗口：墨尔本站 09-18 只剩 8 天、悉尼站 09-20 只剩 10 天**，
    `data/events.json` 相关字段自 08-24 挂出至今 **17 天**未修。本篇因主线是票价、
    而这两条 `price` 恰好都是 `null`，收进来会在主线上开洞，故一并未收。再不修就会像
    袁娅维两场那样过期作废，verified 池将从 8 条永久少 2 条。
  - **"本周开票汇总"的角度储备已见底**：四种切分（时间线/提前量/城市/票价档位）已全部
    用掉，可用池仍是同一批 4 条。下周四（09-17）若 `events.json` 仍未补池，将没有第五种
    切分可用。**根本解只有补池**：①修 AKMU 两条（+2）；②人工核实新演出打 `verified`。
  - `content/cards/012/` 卡片 HTML 仍缺失。
  - `events.json` 里 Loadingzone 的 `notes` 仍写"双语喜剧厂牌"，与官方"华语"口径不符
    （014 已认定，本篇继续沿用"华语"绕开）。
- ⚠️ 组合层提醒：AuShow 杀死标准为 **12 周净新增 500 小红书粉丝 + 每周至少实际发布 3 篇**
  （时钟从 08-16 起算，2026-11-08 到期；PORTFOLIO.md 最后评审 2026-09-06，距今 4 天，
  在 14 天节律内，本次不触发评审提醒）。内容侧已积压 **001–021 共 21 篇待发，瓶颈仍全在
  人工发布这一步**——"每周发 3 篇"是硬前提，不达标会被判执行失败、不算市场证伪。

## 值班日志 — 2026-09-11（周五）

- **第 022 篇**，选题类型 **单场演出安利**（周五轮换位）。产出
  `content/022-xhs-copy.md` + `content/cards/022/index.html`（4 张卡）。
- **fact-audit：RED=0，CHECKED=14，SOURCES-CITED=14。** 未发现事实问题。演出信息
  逐字取自 `events.json` 的 Rolling Donkey 条目，并经 Eventbrite 售票页今日复核（每周二
  7:30 PM / Chippo Hotel, 87-91 Abercrombie Street, Chippendale / 在售 / 未标价），全部一致。
- **未安利池仍为空**（自 08-28 起第 4 次撞空），本篇是 Rolling Donkey 的**首次换角度重讲**
  （选它是因为四条已用条目里它最久没被安利：006，08-24，18 天前）。角度为「开放麦≠专场」
  的预期管理，与 006（梗不用翻译）/011（场馆：全素 pub、地下室、退款、年龄）零重叠。
  新增的"开放麦是什么"内容块引用维基百科 Open mic 条目作为形式通用定义，文案口径为
  "开放麦本来就是…/通常 3–7 分钟"，**没有写成对本场的具体承诺**（本场时长/人数 JSON 与
  售票页均未写）。
- 主动剔除：售票页上的微信联系 ID（外部联系方式不进文案）、"悉尼线下最火喜剧演出"
  （售票页自我宣传语，无法独立核实）、场地距离/大小描述（011 已写且无可靠数字来源）。
- 按提示词第 0 步，本次会话**未调用任何截图/浏览器工具**，渲染交由 `run_daily_xhs.sh` →
  `automation/render_card.py` 完成。
- ⚠️ **遗留问题（本次未新增，均为上游未解除项）**：
  - **AKMU 两场演出日已到最后一周：墨尔本站 09-18 只剩 7 天、悉尼站 09-20 只剩 9 天**，
    `data/events.json` 相关字段自 08-24 挂出至今 **18 天**未修。过了演出日就永久作废，
    verified 池将从 8 条少 2 条。
  - 单场安利已连续 3 篇靠重讲（015/018/022），下周一（09-14）轮到 Loadingzone 重讲，
    之后四条已用条目各重讲过一轮，第二轮重讲的角度储备会明显变薄。**根本解只有补池**。
  - "本周开票汇总"四种切分已全部用掉，下周四（09-17）若仍未补池，将没有第五种可用。
  - `content/cards/012/` 卡片 HTML 仍缺失。
  - `events.json` 里 Loadingzone 的 `notes` 仍写"双语喜剧厂牌"，与官方"华语"口径不符。
- 组合层提醒：AuShow 杀死标准为 **12 周净新增 500 小红书粉丝 + 每周至少实际发布 3 篇**
  （时钟从 08-16 起算，2026-11-08 到期；PORTFOLIO.md 最后评审 2026-09-06，距今 5 天，
  在 14 天节律内，本次不触发评审提醒）。内容侧已积压 **001–022 共 22 篇待发，瓶颈仍全在
  人工发布这一步**。

## 值班日志 — 2026-09-12（周六）

- **第 023 篇**，选题类型 **场馆攻略**（周六轮换位）。产出
  `content/023-xhs-copy.md` + `content/cards/023/index.html`（3 张卡，复制自 011 的 3 张
  纯文字版式，head 与 001 逐字一致）。
- **fact-audit：RED=0，CHECKED=14，SOURCES-CITED=14。** 未发现事实问题。场馆取 verified
  条目「候场喜剧 Loadingzone Comedy 开放麦(墨尔本,常驻)」的 Club Voltaire；场馆客观信息
  全部来自 clubvoltaire.com.au 的 your-visit／about 两页（Level 1 地址、50 席、2003 年起、
  57 路电车 Stop 11 步行 2 分钟、North Melbourne 站步行 17 分钟 930 米、路边停车），楼梯
  一条来自 Only Melbourne 场馆条目并在文案里明确归属，57 路走向用维基百科线路条目交叉核对。
- **主动剔除**：开场时间（见下）、下一场日期（主办方页 JS 渲染读不到）、票价（null）、
  场馆营业时间（与候场周日下午场冲突）、场馆自身 Trybooking/门口售票方式（与 JSON 的
  Eventbrite 并列会误导）、"无轮椅通道/无障碍厕所"（搜索摘要有但定位不到来源页，Fringe
  场馆页 403）、场馆电话、"部分演出含裸露"。
- ⚠️ **新发现，需用户处理（非阻塞）**：`events.json` 里 Loadingzone 条目 `time=19:00`
  与 Eventbrite 上该主办方历史场次开场时间不一致——2025-05-04／05-25／08-17 为 14:00、
  2025-09-14 为 14:30（且场地是 139 Franklin St，不是 Club Voltaire）、2024-12-22 为 17:00、
  2026-03-21 为 19:30。010 号曾按 JSON 写过"19:00 开场"。建议把 `time` 改为 null，并在
  `recurrence` 保留"场次见 Eventbrite"。本篇已规避，未写任何时间。
- **场馆攻略池已见底**：verified 池里 6 座有演出挂靠的场馆已全部写过一轮（004/008/011/
  016/020/023）。下次场馆攻略（09-16 周三）起只能换角度重讲，与单场安利同样的困境——
  **根本解仍是补池**。
- 按提示词第 0 步，本次会话**未调用任何截图/浏览器工具**，渲染交由 `run_daily_xhs.sh` →
  `automation/render_card.py` 完成。
- ⚠️ **遗留问题（上游未解除项，本次未新增）**：AKMU 墨尔本站 09-18 剩 6 天、悉尼站
  09-20 剩 8 天，`events.json` 相关字段自 08-24 挂出 19 天未修；`content/cards/012/`
  卡片 HTML 仍缺失；Loadingzone `notes` 仍写"双语喜剧厂牌"与官方"华语"口径不符。
- 组合层提醒：AuShow 杀死标准为 **12 周净新增 500 小红书粉丝 + 每周至少实际发布 3 篇**
  （时钟从 08-16 起算，2026-11-08 到期；PORTFOLIO.md 最后评审 2026-09-06，距今 6 天，
  在 14 天节律内，本次不触发评审提醒）。内容侧已积压 **001–023 共 23 篇待发，瓶颈仍全在
  人工发布这一步**。

## 值班日志 — 2026-09-13（周日）

- **第 024 篇**，选题类型 **转票防骗指南**（周日轮换位）。产出
  `content/024-xhs-copy.md` + `content/cards/024/index.html`（4 张卡，复制自 001，
  已 `diff` 确认第 1–853 行 head+CSS 仅 `<title>` 一行不同、尾部 script 逐字一致）。
- **fact-audit：RED=0，CHECKED=16，SOURCES-CITED=16。** 未发现事实问题。16 条断言全部
  对应今日抓到的一手原文：总领馆 2025-04-09 提醒（10 条）、总领馆 2026-05-25 提醒（4 条）、
  Ticketmaster AU discover 站转票指引（1 条）、Scamwatch 被骗后页（1 条，012 复用）。
- **角度**：防骗第 7 篇，写的是 003/007（付款前）与 012（确认被骗后）之间没人写过的那段
  ——"钱转了、票没到、对方还在回消息"。核心两条判据都不需要对方配合：自己账号里有没有
  条码（Ticketmaster 官方流程 "Transfer Complete"）、银行的时钟（Scamwatch"立即联系银行"）。
- **信源新增**：中国驻墨尔本总领馆演唱会门票诈骗提醒，是账号第一次引用中文官方文件，
  对留学生受众比 Scamwatch 英文页更直接。已按红线把原文"小红书等网络平台"改写为"社交平台"。
- **主动剔除**：Ticketmaster/Ticketek 帮助中心今日仍 403（与 017/019 当日相同）；Scamwatch
  online-shopping 分类页 403/404；"Ticket Transfer ... completely free" 仅见搜索摘要未见一手页；
  总领馆提醒里属 007/003 支线的三条不写。详见 024 文末"主动剔除项"。
- 按提示词第 0 步，本次会话**未调用任何截图/浏览器工具**，渲染交由 `run_daily_xhs.sh` →
  `automation/render_card.py` 完成。
- ⚠️ **遗留问题（上游未解除项，本次未新增）**：AKMU 墨尔本站 09-18 剩 5 天、悉尼站
  09-20 剩 7 天，`events.json` 相关字段自 08-24 挂出 20 天未修；`content/cards/012/`
  卡片 HTML 仍缺失；Loadingzone `notes`/`time` 字段待修。明天（09-14 周一）单场安利位
  未安利池仍为空，将第四次换角度重讲（按"最久没安利"取 Loadingzone 010，08-28）。
- 组合层提醒：AuShow 杀死标准为 **12 周净新增 500 小红书粉丝 + 每周至少实际发布 3 篇**
  （时钟从 08-16 起算，2026-11-08 到期；PORTFOLIO.md 最后评审 2026-09-06，距今 7 天，
  在 14 天节律内，本次不触发评审提醒）。内容侧已积压 **001–024 共 24 篇待发，瓶颈仍全在
  人工发布这一步**。

## 2026-09-14（周一）值班日志 — xhs-daily

- **第 025 篇**，选题类型 **单场演出安利**（周一轮换位）。产出
  `content/025-xhs-copy.md` + `content/cards/025/index.html`（4 张卡，复制自 001，
  已 `diff` 确认第 1–840 行 head+CSS 仅 `<title>` 一行不同、尾部 script 逐字一致）。
- **fact-audit：RED=0，CHECKED=16，SOURCES-CITED=16。** 最终文案未发现事实问题。
  **但选题阶段发现一条 RED 并换了条目**：按"最久没安利"本应重讲 Loadingzone（010），
  今日核实 Eventbrite 主办方页只剩 2 场待售活动、无一场是开放麦或在 Club Voltaire，
  最近可查到的 Club Voltaire 开放麦是 2026-03-21——JSON `status=on_sale` 对"开放麦"
  今天证实不了，不能写"常驻开放麦售票中"。已改取周杰伦墨尔本站（015 之后的下一条），
  Loadingzone 问题写入 EXCEPTIONS OPEN。
- **角度**：「上次 vs 这次」——2024-03-16/17 Rod Laver Arena 两晚 → 2026-10-17
  Marvel Stadium 一晚，容量从约 1.42 万到 5.3 万余座（维基百科）。7 条演出字段全部于今日
  对 Marvel Stadium 官方公告页与 Ticketmaster 巡演页独立复核（"17 October 2026 (Saturday)"
  / "7:30 PM" / "On Sale Now!" / "maximum of 6 tickets per person"），与 events.json 一致。
- **主动剔除**：2024 两场票价（仅搜索摘要）、"不会加场"（预测）、Marvel 演唱会模式容量
  （词条无该数字，改用座位数）、"Low Availability" 瞬时标签。详见 025 文末。
- 按提示词第 0 步，本次会话**未调用任何截图/浏览器工具**，渲染交由 `run_daily_xhs.sh` →
  `automation/render_card.py` 完成。
- ⚠️ **遗留问题**：AKMU 墨尔本站 09-18 剩 4 天、悉尼站 09-20 剩 6 天，`events.json`
  相关字段自 08-24 挂出 21 天未修，过期后 verified 池永久掉到 6 条；**新增**：Loadingzone
  条目的"常驻开放麦/on_sale"今日无法证实（见上）；`content/cards/012/` 仍缺失；
  Loadingzone `notes`/`time` 字段待修。明天（09-15 周二）为转票防骗指南位，不依赖池子。
- 组合层提醒：AuShow 杀死标准为 **12 周净新增 500 小红书粉丝 + 每周至少实际发布 3 篇**
  （时钟从 08-16 起算，2026-11-08 到期；PORTFOLIO.md 最后评审 2026-09-06，距今 8 天，
  在 14 天节律内，本次不触发评审提醒）。内容侧已积压 **001–025 共 25 篇待发，瓶颈仍全在
  人工发布这一步**。

## 2026-09-15（周二）值班日志 — xhs-daily

- **第 026 篇**，选题类型 **转票防骗指南**（周二轮换位）。产出
  `content/026-xhs-copy.md` + `content/cards/026/index.html`（4 张卡，复制自 001，
  已 `diff` 确认第 1–853 行 head+CSS 仅 `<title>` 一行不同、尾部 script 逐字一致）。
- **fact-audit：RED=0，CHECKED=7，SOURCES-CITED=7。** 最终文案未发现事实问题，选题阶段
  也未触发 RED。
- **角度**：**"便宜"本身**——前七篇防骗的坑全在"贵"（加价/假官网/付费）或"这笔交易
  奇不奇怪"上，本篇写"便宜到你不问一句就转钱"的坑：转票"捡漏价"最常见的真相是一张
  **优惠票（学生票/长者票/健康卡票）**，票面价低、便宜长在"持有人的资格"上，你到门口
  拿不出证件进不去。三条硬规则（不可转让/进场查证/资格因活动而异）全部来自 Ticketek
  官方帮助中心原文，辅以 Ticketmaster AU 帮助中心（资格由主办方决定）与 Scamwatch
  （低价让你"以为捡到便宜其实不是"）。
- **主动剔除**：Ticketek/Ticketmaster 帮助中心今日 curl+WebFetch 仍 403（Cloudflare
  "Just a moment..."），正文取 WebSearch 对该官方 URL 的抽取（与 003/013/017/019/024
  当日相同）；首次搜索摘要里的"国际学生卡不认可""仅持卡人本人"两条未能定位到逐字原文，
  按"核实不了就不写"原则不采用；"官方转售不收优惠票"未写（Marketplace 挂票规则未单列
  优惠票）。详见 026 文末"主动剔除项"。
- 按提示词第 0 步，本次会话**未调用任何截图/浏览器工具**，渲染交由 `run_daily_xhs.sh` →
  `automation/render_card.py` 完成。
- ⚠️ **遗留问题（上游未解除项，本次未新增）**：AKMU 墨尔本站 09-18 剩 3 天、悉尼站
  09-20 剩 5 天，`events.json` 相关字段自 08-24 挂出 22 天未修，过期后 verified 池永久掉到
  6 条；Loadingzone 条目"常驻开放麦/on_sale"仍无法证实（09-14 挂出）；`content/cards/012/`
  仍缺失；Loadingzone `notes`/`time` 字段待修。**明天（09-16 周三）为场馆攻略位**——023
  日志已预警"verified 池里最后一座未写过场馆已用完"，届时需回头换角度重讲（提醒即可，
  不阻塞今天）。
- 组合层提醒：AuShow 杀死标准为 **12 周净新增 500 小红书粉丝 + 每周至少实际发布 3 篇**
  （时钟从 08-16 起算，2026-11-08 到期；PORTFOLIO.md 最后评审 2026-09-06，距今 9 天，
  在 14 天节律内，本次不触发评审提醒）。内容侧已积压 **001–026 共 26 篇待发，瓶颈仍全在
  人工发布这一步**。

## 2026-09-16（周三）值班日志 — xhs-daily

- **第 027 篇**，选题类型 **场馆攻略**（周三轮换位）。产出 `content/027-xhs-copy.md` +
  `content/cards/027/index.html`（4 张卡，复制自 023——最新一份纯文字场馆攻略模板，
  已 `diff` 确认第 1–853 行 head+CSS 仅 `<title>` 一行不同、尾部 script 逐字一致）。
- **fact-audit：RED=0，CHECKED=12，SOURCES-CITED=12。** 选题与成稿全程未触发 RED。
- **角度**：**首次"回头换角度重讲"**——023 日志已预警"verified 池里最后一座未写过场馆
  已用完"。取热度最高、日期最近的 Marvel Stadium（周杰伦墨尔本站 10-17，距今 31 天），
  与 004 严格错开：004 写"怎么到/怎么进"（进场前），本篇写**散场之后这一小时**——
  11 点前结束（噪音宵禁）/ Bourke St、La Trobe St 散场后封路 / Harbour Esplanade 是官方
  接送点 / 两个出租车排队点 / 回家（Southern Cross、Metro Tunnel 新线换乘、车位、渡轮）。
- **信源**：全部场馆事实取自 marvelstadium.com.au 官方两页（getting-to + Local Community
  Information—Special Events，后者今日列明本次周杰伦专场 "Sat 17 Oct 2026" 并与 events.json
  日期互证）。第三方票务站的 "gates 6pm / 10:30pm finish" 与官网 "11pm 前结束" 冲突处，
  一律采信官网、按"核实不了不写"整体不写开门/检票时间（官网仍标 TBC）。
- **主动剔除**：开门/检票时间（官网 TBC，第三方票务站口径不可信）；"票 10-03 才可下载"
  （第三方搜索摘要，未定位到官网原文，属灰色信息）；视野/座位区推荐、步行分钟数、停车费、
  渡轮班次、末班车时刻、免费电车区边界、叫车平台具体点位（官网均未在所查页给出）。
- 按提示词第 0 步，本次会话**未调用任何截图/浏览器工具**，渲染交由 `run_daily_xhs.sh` →
  `automation/render_card.py` 完成。
- ⚠️ **遗留问题（上游未解除项，本次未新增）**：AKMU 墨尔本站 09-18 剩 2 天、悉尼站
  09-20 剩 4 天，`events.json` 相关字段自 08-24 挂出 23 天未修，过期后 verified 池永久掉到
  6 条；Loadingzone 条目"常驻开放麦/on_sale"仍无法证实（09-14 挂出）；`content/cards/012/`
  仍缺失；Loadingzone `notes`/`time` 字段待修。**明天（09-17 周四）为本周开票汇总位**——
  021 日志已预警"四种切分（时间/提前量/城市/票价）已全部用掉，若 events.json 仍未补池，
  将没有第五种切分可用"，且 AKMU 两场明天（09-18/09-20）后彻底过期出池。
- 组合层提醒：AuShow 杀死标准为 **12 周净新增 500 小红书粉丝 + 每周至少实际发布 3 篇**
  （时钟从 08-16 起算，2026-11-08 到期；PORTFOLIO.md 最后评审 2026-09-06，距今 10 天，
  在 14 天节律内，本次不触发评审提醒）。内容侧已积压 **001–027 共 27 篇待发，瓶颈仍全在
  人工发布这一步**。

## 2026-09-17（周四）值班日志 — xhs-daily

- **第 028 篇**，选题类型 **本周开票汇总**（周四轮换位）。产出 `content/028-xhs-copy.md` +
  `content/cards/028/index.html`（3 张卡，复制自 021——最新一份纯文字汇总模板，仅 `<title>` 与
  3 个 poster 区块文案不同，head+CSS 与脚本逐字保留）。
- **fact-audit：RED=0，CHECKED=20，SOURCES-CITED=20。** 选题与成稿全程未触发 RED。
- **角度**：021 日志预警的"四种切分已用光、若 events.json 未补池将无第五种切分"**今天兑现**——
  `data/events.json` 今日仍 8 条 verified、未补池。找到的第五种切分是**按"离你还有几天"的倒计时排**
  （005=时间线、009=提前量、014=城市、021=票价）。倒计时为新增事实：5 天（下周二 09-22）/ 30 天
  （10-17，今天距开演正好满月）/ 65 天（11-21）。底料首次从 4 场缩到 **3 场**——Loadingzone
  "常驻开放麦 · on_sale"自 09-14 起无法在 Eventbrite 核实到当前场次，本轮整条不列（不点名，正文
  只写通用原则），标题"就这 3 场"即此诚实状态。
- **信源**：Rolling Donkey 今日 WebFetch Eventbrite 页（"Every Tuesday, 7:30 PM"/Chippo Hotel
  87-91 Abercrombie St/未标价，与 events.json 全一致）；周杰伦墨尔本站今日 WebSearch 复核
  （17 Oct 2026 周六/19:30/Marvel Stadium/$208–$748 七档 +$9.90/Ticketmaster，与 events.json 一致）；
  悉尼站沿用 021 已复核的 trip.com 档位表 + 今日同源 WebSearch 确认 11-21/Engie Stadium。
- **主动剔除**：Loadingzone（当前场次核实不到）；AKMU 两场（09-18 明天/09-20，字段失真仍 OPEN）；
  袁娅维两场（已过期）；"Low Availability"（瞬时余票，沿用 018 处理）；座位区域名称/门票绑定观演人
  （021 已定性剔除）；赞助商/入场限制/无障碍热线（与主线无关）。
- 按提示词第 0 步，本次会话**未调用任何截图/浏览器工具**，渲染交由 `run_daily_xhs.sh` →
  `automation/render_card.py` 完成。
- ⚠️ **遗留问题（上游未解除项，本次未新增）**：AKMU 墨尔本站 09-18 剩 1 天、悉尼站 09-20 剩 3 天，
  `events.json` 相关字段自 08-24 挂出 24 天未修，过期后 verified 池永久掉到 6 条；Loadingzone
  条目"常驻开放麦/on_sale"仍无法证实（09-14 挂出）；`content/cards/012/` 仍缺失；Loadingzone
  `notes`/`time` 字段待修。**后天（09-19 周六）为场馆攻略位**——023 日志已预警"最后一座未写过场馆
  已用完"、027 已开始"回头换角度重讲"，届时无新场馆可写。
- 组合层提醒：AuShow 杀死标准为 **12 周净新增 500 小红书粉丝 + 每周至少实际发布 3 篇**
  （时钟从 08-16 起算，2026-11-08 到期；PORTFOLIO.md 最后评审 2026-09-06，距今 11 天，
  在 14 天节律内，本次不触发评审提醒）。内容侧已积压 **001–028 共 28 篇待发，瓶颈仍全在
  人工发布这一步**。

## 2026-09-18（周五）值班日志 — xhs-daily

- **第 029 篇**，选题类型 **单场演出安利**（周五轮换位）。产出 `content/029-xhs-copy.md` +
  `content/cards/029/index.html`（4 张卡，复制自 001，仅 `<title>` + 4 个 poster 区块文案改动，
  head+CSS 与脚本逐字保留）。
- **fact-audit：RED=0，CHECKED=11，SOURCES-CITED=11。** 选题与成稿全程未触发 RED。
- **角度**：未安利池仍为空，按"最久没安利"本应取 Loadingzone(010,08-28)，但该条目自 09-14 挂
  OPEN（Eventbrite 主办方页已无开放麦场次），沿用 025"首选 RED → 换下一条"取周杰伦悉尼站
  （018,09-07,11 天前）做第三次换角度重讲。新角度为**「布里斯班人跨城选哪场」**，落点接账号
  复用自「玩转布里斯班」的受众处境：①澳洲仅两站（墨尔本 10-17、悉尼 11-21，布里斯班没有场）；
  ②悉尼更近（飞悉尼约 750km/1.5h vs 飞墨尔本约 1381km/2h 起）；③最低档更省（悉尼 $188 起
  vs 墨尔本 $208 起）；④悉尼为澳洲站最后一场。与 002(官宣)/018(名字来历)/008(ENGIE 入场攻略)/
  014(按城市)/021(票价档位)/028(倒计时)零重叠。
- **信源**：维基百科「嘉年華II世界巡迴演唱會」词条 + ausmusicscene 澳洲巡演页（澳洲仅墨尔本/
  悉尼两城、无布里斯班日期）；Sydney Showground 官方活动页（Saturday 21 November 2026 /
  7:30 pm / ENGIE Stadium, Sydney Olympic Park / Tickets officially on sale）；Ticketmaster AU
  艺人页；主办方 Sky Music & Horizon Production；距离 BNE-SYD≈750km(约1.5h) vs BNE-MEL≈1381km
  (约2h起)，distance.to/flightera/Tripadvisor。全部与 events.json 一致。
- **主动剔除**：主办方/限购6张（本角度以"为什么选悉尼"为主，不写 001 式购票须知清单，events.json
  `notes` 的"主办方/每账户限购6张"未入卡，仅保留封面底部条与票根已有的 Ticketmaster 平台）；
  "Low Availability"（瞬时余票，沿用 018 处理）；AKMU 两场（字段失真仍 OPEN）；Loadingzone
  （当前场次核实不到）；袁娅维两场（已过期）。
- 按提示词第 0 步，本次会话**未调用任何截图/浏览器工具**，渲染交由 `run_daily_xhs.sh` →
  `automation/render_card.py` 完成。
- ⚠️ **遗留问题（上游未解除项，本次未新增）**：AKMU 墨尔本站 09-18 **今天**、悉尼站 09-20 剩 2 天，
  `events.json` 相关字段自 08-24 挂出 25 天未修，墨站已到演出日、过期后 verified 池永久掉到 6 条；
  Loadingzone 条目"常驻开放麦/on_sale"仍无法证实（09-14 挂出）；`content/cards/012/` 仍缺失；
  Loadingzone `notes`/`time` 字段待修。**明天（09-19 周六）为场馆攻略位**——023 日志已预警
  "最后一座未写过场馆已用完"、027 已开始"回头换角度重讲"，届时无新场馆可写。
- 组合层提醒：AuShow 杀死标准为 **12 周净新增 500 小红书粉丝 + 每周至少实际发布 3 篇**
  （时钟从 08-16 起算，2026-11-08 到期；PORTFOLIO.md 最后评审 2026-09-06，距今 12 天，
  仍在 14 天节律内，本次不触发评审提醒）。内容侧已积压 **001–029 共 29 篇待发，瓶颈仍全在
  人工发布这一步**。

## 2026-09-19（周六）值班日志 — xhs-daily

- **第 030 篇**，选题类型 **场馆攻略**（周六轮换位）。产出 `content/030-xhs-copy.md` +
  `content/cards/030/index.html`（4 张卡，复制自 027，仅 `<title>` + 4 个 poster 区块文案改动，
  head+CSS+WebGL 脚本逐字保留）。
- **fact-audit：RED=0，CHECKED=17，SOURCES-CITED=17。** 选题与成稿全程未触发 RED。
- **场馆选择（本次重开一个旧决定）**：023 日志曾预警"最后一座未写过场馆已用完"、027 已开始
  回头重讲。但严格核对 verified 池：8 条演出、8 座场馆，实际只写过 6 座——**Palais Theatre**
  与 **Sydney Event Centre (The Star)** 从未写过，此前 004/023/027 以"袁娅维两场演出日已过"
  为由跳过、转而重讲。提示词对场馆攻略只要求场馆"出现在 verified=true 演出里"，未要求该演出
  是未来场次；场馆的交通/入场/座位是 evergreen 内容。故本次取 **Palais Theatre（St Kilda）**
  作全新场馆，写进系列第一个"老剧院/文化遗产建筑"品类，避开第三次重讲大球场。
- **红线处理**：本篇不锚定任何具体华语演出——该馆唯一 verified 演出（袁娅维墨尔本 08-20）已
  过期，同馆其余条目（宋冬野/CNBLUE/二狗等）均 `verified=false`，按"未核实的不发"一律不点名。
  全篇只写场馆本身的客观信息。
- **信源**：palaistheatre.com.au/getting-here（地址/电车 16·96·3a/火车 Balaclava/巴士 246·600 等/
  周边停车位/落客点/出租车排队点/周末拥挤/全有偿停车）、palaistheatre.com.au/accessibility
  （Lower Esplanade 正门无台阶/两层 Stalls·Lounge/电梯到 foyer/无障碍座位 AA·WW·D 排/Kulture
  City 感官友好）、维基百科 + 维州文化遗产名录（1927 建成、列入文化遗产名录）。
- **主动剔除**："没有自带停车场"硬断言（官网无此原句，只写"官方列的全是周边车位"）、具体门牌号
  （官方只给路口，第三方 12/14 歧义）、"澳洲最大有座剧院/2896 座"（维基带 citation-needed 标签）、
  "Art Deco"（维基正文写 Spanish Baroque/neoclassical，与第三方口径冲突）、"Lower Esplanade 路段
  永久封闭"（仅第三方摘要，官方无此句）、具体座位视野/容量精确数/停车价格/班次时刻（官网未给）。
- 按提示词第 0 步，本次会话**未调用任何截图/浏览器工具**，渲染交由 `run_daily_xhs.sh` →
  `automation/render_card.py` 完成。
- **遗留问题（上游未解除项，本次未新增）**：AKMU 墨尔本站 09-18 已过（墨站 ticket_platform 失真
  问题已无实际影响，条目仍挂 EXCEPTIONS OPEN）；AKMU 悉尼站 09-20 明天剩 1 天，`events.json` 相关
  字段（venue 旧名/price/time null）自 08-24 挂出仍未修；Loadingzone
  条目"常驻开放麦/on_sale"仍无法证实（09-14 挂出）；`content/cards/012/` 仍缺失；Loadingzone
  `notes`/`time` 字段待修。**明天（09-20 周日）为转票防骗指南位**，不依赖 verified 池。
- 组合层提醒：AuShow 杀死标准为 **12 周净新增 500 小红书粉丝 + 每周至少实际发布 3 篇**
  （时钟从 08-16 起算，2026-11-08 到期；PORTFOLIO.md 最后评审 2026-09-06，距今 13 天，
  仍在 14 天节律内，本次不触发评审提醒）。内容侧已积压 **001–030 共 30 篇待发，瓶颈仍全在
  人工发布这一步**。
- **2026-09-20** | 031号 | 转票防骗指南（假退款/冒名官方钓鱼） | fact-audit 11 条全 GREEN，RED=0。角度为"演出取消/改期之后，骗子冒充官方票务发'领退款'链接"，与前八篇防骗（付款前/假网站/被骗后/卖家/账号被盗/免费中奖/付款后拉黑前/优惠票资格）零重叠。信源：Ticketmaster 官方退款页（取消自动退原路/无需操作/澳洲 3–5 工作日，US 页 WebFetch 成功、AU 页 403 取 WebSearch 抽取）+ Scamwatch 冒名退款警示（WebFetch 抓取原文）。4 张卡，HTML 由 cards/026 复制仅换文案，主题 token/CSS/字体未动。渲染与 Telegram 推送交由 run_daily_xhs.sh。⚠️ PORTFOLIO.md 最后评审 2026-09-06，今日 09-20 恰满 14 天，达节律边界，建议尽快跑 /portfolio-review。
