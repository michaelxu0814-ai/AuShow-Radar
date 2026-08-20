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
