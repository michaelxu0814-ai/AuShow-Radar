# 006 — 悉尼每周二中文开放麦（单场演出安利）

**选题类型**：单场演出安利（周一轮换位）
**信源条目**：`data/events.json` → Rolling Donkey 中文喜剧开放麦(悉尼,每周二)（verified=true）

## 标题（12字）

悉尼每周二 有场中文开放麦

## 正文（发帖文案，无外链）

在悉尼想找个地方笑一场？Rolling Donkey 每周二有中文喜剧开放麦。📍Chippo Hotel（87-91 Abercrombie St, Chippendale），晚上 7:30 开场，Eventbrite 上订票。

中文开放麦的好处是——梗不用翻译，笑点直接砸到你身上。留学生、上班族、刚落地的新移民，台上讲五分钟，台下全是听得懂的人。

想去的评论区扣 1，私信把地址和订票页发你～ 澳华演出雷达帮你盯紧全澳华语演出，不再错过任何一场。

#悉尼脱口秀 #中文开放麦 #悉尼生活 #澳洲华人 #演出情报

## 卡片文案结构（4张，票根美学）

**P1 封面**
- kicker: 演出情报 · 单场安利
- 大字标题: 悉尼每周二 / 有场中文开放麦
- 副标题: Rolling Donkey 中文喜剧开放麦
- 配图: 无（events.json 该条目 `image=null`，不外挂任何图）
- 说明: Chippo Hotel，晚上 7:30 开场，Eventbrite 订票。
- 底部条: 每周二 · SYD — Eventbrite 售票中

**P2 票根组件**
- 演出: Rolling Donkey 中文喜剧开放麦（悉尼，每周二）
- 大字: 周二 EVERY TUE ｜ 状态徽章: ON SALE 售票中
- 场馆: Chippo Hotel（Chippendale，悉尼 Sydney）
- 时间: 19:30

**P3 去之前先看这 4 条（ledger 4条）**
1. 每周二 — 常驻周场，19:30 开场
2. Chippo Hotel — 87-91 Abercrombie St, Chippendale
3. Eventbrite — 官方订票平台
4. 票价未标 — 我们收录时官方页面未标价，这里不给数字
- 收尾: 官方页面是唯一标准——加价转票、来源不明的二手票，风险自己扛。
- 底部条: 信息来自主办方页面 — 出发前再复核当周场次

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 每周二都有一场 / 你去不去？
- 正文: 评论区扣 1，私信把地址和订票页发你，还有后续演出提醒。
- 底部条: VOL. 006 — 简介里有完整演出日历

## 事实核查表

| 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|
| 演出名「Rolling Donkey 中文喜剧开放麦（悉尼，每周二）」 | GREEN | `data/events.json` events[].title_zh，该条目 verified=true | 逐字复制；未采用外部页面上的「驴打滚」别名，保持与 JSON 一致 |
| 厂牌 Rolling Donkey 喜剧 | GREEN | 同上 events[].artist | 逐字复制 |
| 类别 开放麦 | GREEN | 同上 events[].category | 逐字复制 |
| 城市 悉尼 | GREEN | 同上 events[].city | 逐字复制 |
| 场馆 Chippo Hotel | GREEN | 同上 events[].venue | 逐字复制 |
| 地址 87-91 Abercrombie St, Chippendale | GREEN | 同上 events[].venue；另经 WebFetch 核实 https://www.eventbrite.com/e/copy-of-rolling-donkey-tickets-1983189907399 页面写明 "Chippo Hotel, 87-91 Abercrombie Street, Chippendale, NSW 2008" | JSON 与官方票务页一致 |
| 开演时间 19:30（晚上7:30） | GREEN | 同上 events[].time；另经上述 Eventbrite 页面核实 "every Tuesday, 7:30 PM" | JSON 与官方票务页一致 |
| 每周二常驻周场 | GREEN | 同上 events[].recurrence="每周二" / events[].notes="常驻周场"；另经上述 Eventbrite 页面核实为 weekly recurring、列 "Multiple dates" | JSON 与官方票务页一致 |
| 购票平台 Eventbrite | GREEN | 同上 events[].ticket_platform；另经上述 Eventbrite 页面核实为在售票务页 | 正文/卡片未放外链，仅写平台名 |
| 状态 on_sale（售票中） | GREEN | 同上 events[].status；另经上述 Eventbrite 页面核实页面 live、可订票、非已结束 | 与 001 不同，此条 status 无 notes 冲突，可直接采用 |
| 不给任何票价数字 | GREEN | 同上 events[].price=null；另经上述 Eventbrite 页面核实 "Ticket Price: Not specified on the page" | JSON 无票价且官方页亦未标价，故 P3 第4条明写"未标价、不给数字" |
| link_ok=true（订票链接可访问） | GREEN | 同上 events[].link_ok；WebFetch 实测该 URL 页面 live | 未在正文/卡片放外链，仅用于内部核实 |

FACT-AUDIT-STATUS: RED=0 CHECKED=12 SOURCES-CITED=12

## 本次选题决策 & 主动排除项

**为什么不是 AKMU（本来的首选）**：按"日期最近/热度最高"，未被单场安利用过的 verified
条目里首选应是 AKMU 墨尔本站（2026-09-18）。fact-audit 阶段核实时发现该条目
`ticket_platform="Ticketek"` **已经过期失真**，无法在不违反红线的前提下写：

- Margaret Court Arena 所属的 Melbourne Park 自 **2026-08-22** 起改由 **AXS** 承接票务
  （官方场馆页 https://margaretcourtarena.com.au/event/akmu-australia-tour-melbourne-2026/
  明写 "Melbourne Park is introducing AXS as its new Official Ticketing Partner"，并特别
  注明 "Ticketek ticket delivery for AKMU has been intentionally delayed. Your tickets
  will be issued by AXS by the end of August"）。
- 即今天（2026-08-24）若按 JSON 写"Ticketek 是唯一官方购票平台"，会把读者导到已经不
  承接该场的平台 → 判定 **RED**（事实错误）。
- 而改写成 AXS 又会违反"演出信息必须与 events.json 逐字一致、不能用 JSON 没有的字段"
  这条红线。两条路都堵死 → 该条目今天不可发，已按第7步写入 `~/Projects/EXCEPTIONS.md`
  等用户修 events.json。

**为什么也不是 AKMU 悉尼站（09-20）**：该条目 `price=null` + `time=null` +
`status=on_sale` 与 notes 自相矛盾（005 已记录过该冲突），且场馆名存在歧义——JSON 记
"ICC Sydney Theatre"，而 Ticketek 现将同场馆标为 "TikTok Entertainment Centre"
（JSON notes 亦承认此分歧）。一张没有票价、没有开演时间、场馆名与购票页对不上的票根卡，
正撞账号"详情页跳错演出/日期场馆票价错一次就伤号"的历史事故线，故本次不用，留待
events.json 补全后再安利。

**为什么 Rolling Donkey 可用**：该条目每一个字段都被官方票务页独立佐证（地址/时间/
每周二/平台/在售/未标价），零冲突字段，且"每周二"是常驻周场，任何一天发布都成立，
不存在"明晚就有"这类会因人工审核延迟而失真的时效断言。

**主动排除项**：
- 不写票价（`price=null`，官方页亦未标价）
- 不写具体某一场的日期（`date=null`，该条目本就是周期性场次；卡片一律只写"每周二"）
- 不写"明晚/本周二"这类依赖发布日的说法——用户手动审核后发布日期不可控，
  统一改成恒真的"每周二都有一场"
- 不写入场须知/检票时间/座位视野等 JSON 无字段、官方页也未写明的内容
- 不外挂任何配图（该条目 `image=null`；账号已有两次海报张冠李戴事故）
- 未采用外部页面出现的"驴打滚"别名，卡片与正文一律用 JSON 的 title_zh 口径

## 渲染状态

- 模板: `cards/006/index.html`（复制自 `cards/005/index.html`；已 diff 确认其第 1–840 行
  即全部 CSS / `data-theme="aushow"` 主题色 token / 字体与 `cards/001/index.html` 逐字
  相同，仅 `<title>` 不同，故等价于按提示词要求复制自 001，且额外继承了 003→004→005
  一路修过的 `.ledger-note` max-width 修正）
- 卡片: 4 张（封面 / 票根 / 去之前先看这4条 / CTA），无配图
- 版式预防：`.ledger-row` 网格为 `96px 1fr auto`，note 吃满 460px 后 title 列仅剩约
  300px，故 `.ledger-title` 一律压到 3–4 字（"每周二""票价未标"）或短拉丁词
  （"Chippo Hotel""Eventbrite"），避免 42px 标题渲染时折行
- P2 票根大字位用「周二」两字替代 001 的日期数字（该条目 `date=null`），
  `.tk-num` 为 168px/weight 900，两个中文字约 336px，票根内可用宽度约 808px，不会溢出
- 渲染方式：本次会话按 `daily-xhs-prompt.md` 第0节**未调用任何浏览器截图工具**，
  渲染交给 `automation/render_card.py`（headless Chrome 逐张单独截图）由
  `run_daily_xhs.sh` 在本任务结束后执行
