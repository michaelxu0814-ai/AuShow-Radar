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
