# 032 — 演唱会要等，这场每周都有（单场演出安利）

**选题类型**：单场演出安利（周一轮换位，2026-09-21 生成）
**信源条目**：`data/events.json` → Rolling Donkey 中文喜剧开放麦(悉尼,每周二)（verified=true）

**选题决策**：未安利池仍为空——8 条 verified 中周杰伦墨/悉已由 001/002 用过（并分别于
015/018/025/029 换角度重讲），Rolling Donkey 由 006/022 用过，Loadingzone 由 010 用过但
自 09-14 挂 EXCEPTIONS OPEN（Eventbrite 已无开放麦场次，详见 025 日志），袁娅维两场
（08-20/08-22）演出日已过，AKMU 两场自 08-24 挂 EXCEPTIONS OPEN 至今 `data/events.json`
相关字段仍未改动（墨站 `ticket_platform` 与官方 AXS 口径冲突；悉站 `venue` 为旧名、
`price`/`time` 仍 null），按红线不可发。故按提示词第 2 步取**已用条目里最久没被安利过的一条**：
Loadingzone（010，08-28）按"首选 RED → 换下一条"跳过后，取 **Rolling Donkey**（022，09-11，
10 天前）。这是该条目**第二次换角度重讲**。

**角度**：「周更的确定性」——把看华语演出从"一年等一次"变成"每周二的一次固定小节目"。
006 讲的是"为什么去"（梗不用翻译），011 讲的是"在哪看"（Chippo Hotel 场馆攻略），022 讲的是
"台上会发生什么"（开放麦≠专场）。**没有一篇把"每周二固定有"这件事本身当作卖点展开**——
022 只在收尾一句话带过"每周二都有——不用抢票"。本篇把这条单独拎出来做成一整篇：演唱会
按巡回排期、开票要掐点抢，而常驻周场给你的是确定性——不用盯开票、错过这周下周照常开。
与 006/011/022 零重叠。

**红线自查**：演出信息（名称/场馆/时间/每周二/常驻周场/平台/状态/无票价）逐字取自
`events.json` 的 `verified=true` 条目并经 Eventbrite 售票页复核；`price=null` 故全文不给任何
价格数字；"不用抢票"沿 022 已通过审核的口径（源自"常驻周场 + on_sale + Multiple dates"）；
未点名任何个人/账号（含售票页微信联系方式）。

## 标题（14字）

演唱会要等，这场每周都有

## 正文（发帖文案，无外链）

在悉尼想看华语现场，演唱会按巡回排期、一年就那几站；这场不一样——Rolling Donkey 中文喜剧开放麦，**每周二 19:30**，Chippo Hotel（Chippendale），Eventbrite 订票，常驻周场，哪一周去都有。

把它当成每周二的一个固定小节目：不用等巡回排期，也不用为开票时间设闹钟——周二到了就有场。错过这周，下周二照常开门。

官方页面没标票价，所以我也不写数字。"内部价""渠道价"一律别信。

评论区扣 1，私信发你订票页和后续演出提醒～ 澳华演出雷达帮你盯紧全澳华语演出，不再错过任何一场。

#悉尼脱口秀 #中文开放麦 #悉尼生活 #澳洲华人 #演出情报

## 卡片文案结构（4张，票根美学）

> 张数说明：4 张（封面 / 周更的确定性 ledger / 票根 / CTA）。与 022 相比把"开放麦≠专场"
> 那张换成"周更的确定性"——022 那张（轮番登场/试段子/3–7 分钟）已写透，本篇不重复。
> 票价未标、场馆、时间照旧压进票根卡。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 演出情报 · 单场安利
- 大字标题: 演唱会要等 / 这场每周都有
- 副标题: Rolling Donkey 中文喜剧开放麦 · 悉尼
- 配图: 无（events.json 该条目 `image=null`，不外挂任何图）
- 说明: 每周二 19:30，Chippo Hotel，Eventbrite 订票。常驻周场，哪一周去都有。
- 底部条: 每周二 · SYD — Eventbrite 售票中

**P2 周更的确定性（ledger 3条）**
1. 每周二固定 — 常驻周场，每周二 19:30。不是一年一次，是每周一次
2. 不用抢票 — 演唱会开票要掐点抢；这场 Eventbrite 常驻售票中，周二到了就有
3. 错过也不慌 — 这周没空，下周二照常开门。它不是"错过就没了"，是"每周都在"
- 收尾: 段子是最新鲜的那一版，这份"每周都有"的确定性，只有常驻场给得了。
- 底部条: 售票页原话 — 常驻周场 · 每周二

**P3 票根组件**
- 演出: Rolling Donkey 中文喜剧开放麦（悉尼）
- 大字: 周二 EVERY TUE ｜ 状态徽章: ON SALE 售票中
- 场馆: Chippo Hotel（Chippendale · 悉尼 Sydney）
- 时间: 19:30
- 票价: 官方未标（不给数字）

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 每周二 / 你还不来？
- 正文: 官方页面没标票价，"内部价"一律别信。评论区扣 1，私信发你订票页和后续演出提醒。
- 底部条: Vol. 032 — 简介里有完整演出日历

## 事实核查表

| 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|
| 演出名「Rolling Donkey 中文喜剧开放麦(悉尼,每周二)」 | GREEN | `data/events.json` events[].title_zh，该条目 verified=true；另经 WebFetch 核实 https://www.eventbrite.com/e/copy-of-rolling-donkey-tickets-1983189907399 页面标题含 "Rolling Donkey 中文喜剧开放麦" | 逐字取 JSON 口径；沿用 006/022 做法未采用 Eventbrite 标题里的"驴打滚"别名 |
| 厂牌 Rolling Donkey 喜剧 | GREEN | 同上 events[].artist="Rolling Donkey 喜剧" | 逐字复制 |
| 类别 开放麦 / 中文脱口秀 | GREEN | 同上 events[].category="开放麦"；Eventbrite 页标题含 "中文喜剧开放麦" | 与 JSON 一致 |
| 城市 悉尼 | GREEN | 同上 events[].city="悉尼"；Eventbrite 页地址 "Chippendale, NSW 2008" | 逐字复制 |
| 场馆 Chippo Hotel（Chippendale） | GREEN | 同上 events[].venue="Chippo Hotel, 87-91 Abercrombie St, Chippendale"；Eventbrite 页 "The Chippo Hotel at 87-91 Abercrombie St, Chippendale, NSW 2008" | JSON 与官方票务页一致；本篇卡片只写场馆名+区名，不重复 011 已写过的门牌地址 |
| 开演时间 19:30 | GREEN | 同上 events[].time="19:30"；Eventbrite 页 "Every Tuesday, 7:30 PM / 每周二 晚7:30" | JSON 与官方票务页一致 |
| 每周二 | GREEN | 同上 events[].recurrence="每周二"；Eventbrite 页 "Every Tuesday"、"Multiple dates" | JSON 与官方票务页一致；文案统一用恒真的"每周二"，不写依赖发布日的日期 |
| 常驻周场 | GREEN | 同上 events[].notes="常驻周场" | 逐字复制 |
| 购票平台 Eventbrite | GREEN | 同上 events[].ticket_platform="Eventbrite"；上述 Eventbrite 页为在售票务页 | 正文/卡片未放外链，仅写平台名 |
| 状态 on_sale（售票中） | GREEN | 同上 events[].status="on_sale"；WebFetch 实测上述页面今日 live、有 active ticket link、"Multiple dates"、非已结束 | 与 JSON 一致 |
| 票价：官方未标，不给数字 | GREEN | 同上 events[].price=null；Eventbrite 页无任何价格数字、仅 "Get tickets" 按钮 | JSON 无票价且官方页亦未标价，故全文不出现任何价格数字 |
| link_ok=true（订票链接可访问） | GREEN | 同上 events[].link_ok=true；WebFetch 实测该 URL 页面 live | 未在正文/卡片放外链，仅用于内部核实 |

FACT-AUDIT-STATUS: RED=0 CHECKED=12 SOURCES-CITED=12

## 主动排除项

- 不写票价（`price=null`，官方页亦未标价）
- 不写具体某一场的日期（`date=null`，周期性场次；卡片一律只写"每周二"）
- 不写"本周二/明晚"这类依赖发布日的说法——用户手动审核后发布日期不可控
- 不写本场演出时长、每人上台时长、演员人数（JSON 与售票页均未写）
- 不写退款政策与年龄条款（011 已写，重复无增量）
- 不写售票页上的微信联系方式（外部联系 ID，不进文案）
- 不写"悉尼线下最火喜剧演出"等自我宣传语（无法独立核实）
- 未采用"驴打滚"别名（沿 006/022 口径，JSON title_zh 无此字，逐字一致优先）
- 不外挂任何配图（该条目 `image=null`；账号已有两次海报张冠李戴事故）

## 渲染状态

- 模板: `cards/032/index.html`（复制自 `cards/022/index.html`——同一条目、同为 `date=null`
  的票根组件；已 diff 确认其第 1–845 行即全部 CSS / `data-theme="aushow"` 主题色 token /
  字体与 `cards/001/index.html` 逐字相同，仅 `<title>` 不同，故等价于按提示词要求复制自 001）
- 卡片: 4 张（封面 / 周更的确定性 ledger / 票根 / CTA），无配图
- 版式预防：`.ledger-title` 控制在 4–5 字以内（"每周二固定""不用抢票""错过也不慌"），
  note 均 ≤ 40 字并沿用 `max-width:460px`；P3 票根大字位沿用 022 的「周二」两字（`date=null`），
  第三栏"票价 / 官方未标"与"场馆/时间"同行 flex 排列，与 022 一致
- 渲染方式：本次会话按 `daily-xhs-prompt.md` 第 0 节**未调用任何浏览器截图工具**，
  渲染交给 `automation/render_card.py`（headless Chrome 逐张单独截图）由
  `run_daily_xhs.sh` 在本任务结束后执行
