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
