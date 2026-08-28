# 010 — 墨尔本常驻双语开放麦（单场演出安利）

**选题类型**：单场演出安利（周五轮换位）
**信源条目**：`data/events.json` → 候场喜剧 Loadingzone Comedy 开放麦(墨尔本,常驻)（verified=true）

## 标题（15字）

墨尔本想笑一场？这有常驻开放麦

## 正文（发帖文案，无外链）

在墨尔本想找个地方笑一场？候场喜剧 Loadingzone Comedy 有常驻开放麦。📍Club Voltaire（1st Floor/14 Raglan St, North Melbourne），19:00 开场，Eventbrite 订票。

这是 AUNZ Comedy Media 旗下的双语喜剧厂牌——除了自己的常驻场，也承接国内演员的澳洲巡演。所以它不只是"周中随便找点乐子"的地方，值得长期蹲。

具体是哪一场、哪天开演，都在 Eventbrite 上更新，出发前记得再看一眼当周场次。想去的评论区扣 1，私信把地址和订票页发你～ 澳华演出雷达帮你盯紧全澳华语演出，不再错过任何一场。

#墨尔本脱口秀 #开放麦 #墨尔本生活 #澳洲华人 #演出情报

## 卡片文案结构（4张，票根美学）

**P1 封面**
- kicker: 演出情报 · 单场安利
- 大字标题: 墨尔本想笑一场？/ 这有常驻开放麦
- 副标题: 候场喜剧 Loadingzone Comedy
- 配图: 无（该条目 `image` 是厂牌通用 banner，非本场海报，主动不外挂，详见"主动排除项"）
- 说明: Club Voltaire，19:00 开场，Eventbrite 订票。
- 底部条: 常驻 · MELB — Eventbrite 售票中

**P2 票根组件**
- 演出: 候场喜剧 Loadingzone Comedy 开放麦（墨尔本）
- 大字: 常驻 ｜ 单位: 场次见 EVENTBRITE ｜ 状态徽章: ON SALE 售票中
- 场馆: Club Voltaire（North Melbourne · 墨尔本 Melbourne）
- 时间: 19:00

**P3 去之前先看这 4 条（ledger 4条）**
1. 常驻场次 — 场次与日期见 Eventbrite
2. Club Voltaire — 1st Floor/14 Raglan St, North Melbourne
3. Eventbrite — 官方订票平台
4. 票价未标 — 我们收录时官方页面未标价，这里不给数字
- 收尾: 官方页面是唯一标准——加价转票、来源不明的二手票，风险自己扛。
- 底部条: 信息来自主办方页面 — 出发前再复核当周场次

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 墨尔本的中文笑点 / 你摸清了吗？
- 正文: 评论区扣 1，私信把地址和订票页发你，还有后续演出提醒。
- 底部条: VOL. 010 — 简介里有完整演出日历

## 事实核查表

| 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|
| 演出名「候场喜剧 Loadingzone Comedy 开放麦（墨尔本，常驻）」 | GREEN | `data/events.json` events[].title_zh，该条目 verified=true | 逐字复制 |
| 厂牌 候场喜剧 Loadingzone Comedy | GREEN | 同上 events[].artist；另经 WebFetch 核实 https://www.eventbrite.com/o/loadingzone-comedy-75417874333 organizer 名即「候场喜剧Loadingzone Comedy」 | JSON 与官方票务页一致 |
| 类别 开放麦 | GREEN | 同上 events[].category | 逐字复制；未升格成"专场/演出"等更强说法 |
| 城市 墨尔本 | GREEN | 同上 events[].city | 逐字复制 |
| 场馆 Club Voltaire | GREEN | 同上 events[].venue；另经 WebFetch 核实场馆官网 https://www.clubvoltaire.com.au/your-visit 存在且为同名演出场地 | JSON 与场馆官网一致 |
| 地址 1st Floor/14 Raglan St, North Melbourne | GREEN | 同上 events[].venue；另经上述场馆官网核实其自述地址为 "Level 1 / 14 Raglan Street, North Melbourne 3051, VIC AUSTRALIA" | JSON 的 "1st Floor" 与官网 "Level 1" 同义、门牌街道逐字一致 |
| 开演时间 19:00 | GREEN | 同上 events[].time（该条目 verified=true） | organizer 页未列出单场时间，无独立佐证；故卡片/正文同时写明"场次见 Eventbrite、出发前复核当周场次"，不把 19:00 说成某一具体日期的承诺 |
| 常驻场次、具体场次见 Eventbrite | GREEN | 同上 events[].recurrence="常驻(场次见Eventbrite)" | 逐字采用该口径；不编造任何"每周几"的固定星期（与 006 的 Rolling Donkey"每周二"不同，本条 JSON 未给星期） |
| 购票平台 Eventbrite | GREEN | 同上 events[].ticket_platform；另经 WebFetch 核实上述 organizer 页为 live 的 Eventbrite 主办方页 | 正文/卡片未放外链，仅写平台名 |
| 状态 on_sale（售票中） | GREEN | 同上 events[].status；另经上述 organizer 页核实页面 live、含 Upcoming 场次入口、非已结束 | 该条 status 与 notes 无冲突（对比 AKMU 悉尼站），可直接采用 |
| 厂牌背景「AUNZ Comedy Media 旗下双语喜剧厂牌，也承接国内演员澳洲巡演」 | GREEN | 同上 events[].notes；另经上述 organizer 页核实其自述为"澳大利亚AUNZ COMEDY MEDIA旗下运营的专业双语喜剧厂牌"，并自述提供"国内喜剧演员的澳洲巡演机会" | 正文为 notes 的同义转述，未加"最大/最知名"等 JSON 无据的修饰 |
| 不给任何票价数字 | GREEN | 同上 events[].price=null；另经上述 organizer 页核实页面未列出票价 | JSON 无票价且官方页亦未标价，故 P3 第4条明写"未标价、不给数字" |
| link_ok=true（订票链接可访问） | GREEN | 同上 events[].link_ok；WebFetch 实测该 URL 页面 live 且返回 organizer 正文 | 未在正文/卡片放外链，仅用于内部核实 |

FACT-AUDIT-STATUS: RED=0 CHECKED=13 SOURCES-CITED=13

## 本次选题决策 & 主动排除项

**未安利池的实际状态**：8 条 verified 中，周杰伦墨尔本/悉尼两场已由 001/002 安利过，
Rolling Donkey 已由 006 安利过；袁娅维墨尔本(08-20)/悉尼(08-22)两场**演出日期已过**；
AKMU 两场仍卡在 `EXCEPTIONS.md` OPEN（见下）。真正干净且未被单场安利用过的只剩本条，
故本次选它——不是随机挑的，是唯一不触红线的可用条目。

**为什么今天仍然不是 AKMU 悉尼站（09-20，日期最近、热度最高）**：该条目 JSON notes 已
更新为"Ticketek深链场馆代码EICC=ICC Sydney"，但本次 fact-audit 用 WebSearch 独立核实
后判定**仍不可发**：

- 场馆已于 2025 年 11 月**正式更名**——ICC Sydney 的剧院（前 Aware Super Theatre）冠名
  权归 TikTok，官方名为 **TikTok Entertainment Centre**
  （https://ftnnews.com/travel-news/mice/sydneys-icc-theatre-renamed-tiktok-entertainment-centre-in-global-first/ ，
  另 https://www.contentgrip.com/tiktok-sydney-venue-naming-rights/ 佐证）。多个票务/演出
  站现均把这场 AKMU 标为 "TikTok Entertainment Centre (formerly Aware Super Theatre) at
  ICC Sydney"（https://concerts.consequence.net/events/akmu-at-tiktok-entertainment-centre-formerly-aware-super-theatre-at-icc-sydney-complex-on-2026-09-20-19-00 ）。
- 即 JSON 的 `venue="ICC Sydney Theatre"` 是**旧名**。照抄会让读者到了购票页/现场对不上
  名字，正撞账号红线里"详情页跳错演出、日期场馆错一次就伤号"那条；而改写成
  TikTok Entertainment Centre 又违反"只能用 JSON 实际有的字段"。两条路都堵死 → 判定
  该条目今天仍不可安利。
- 且该条目 `price=null` + `time=null` 依旧未补（外部页面显示 7:00 PM，但那是 JSON 没有
  的字段，不能拿来用）。
- 已把这一条新证据补进 `EXCEPTIONS.md` 对应 OPEN 项。

**为什么也不是 AKMU 墨尔本站（09-18）**：`ticket_platform="Ticketek"` 失真问题（Melbourne
Park 自 2026-08-22 起改由 AXS 承接票务）自 006 起未修，仍在 OPEN，维持不发。

**主动排除项**：
- **不外挂配图**：该条目 `image` 字段虽非 null，但同一个 `img.evbuc.com` URL 在
  events.json 里**同时挂在另外两条完全无关的条目上**（候场喜剧"她在场"格斗体验课、
  候场喜剧"抓马大会"嗑瓜子小赛），说明它是厂牌 Eventbrite 主办方页的通用 banner，
  不是本场开放麦的海报。账号已有两次"海报张冠李戴"事故，故本篇不放图。
- 不写票价（`price=null`，官方页亦未标价）
- 不写"每周X"（`recurrence` 只写"常驻(场次见Eventbrite)"，未给固定星期，不能仿照 006 的
  "每周二"句式）
- 不写具体某一场的日期（`date=null`）
- 不写"明晚/本周"这类依赖发布日的说法——用户手动审核后发布日期不可控
- 不写入场须知/检票时间/座位视野/场地容量等 JSON 无字段的内容（场馆官网提到的
  "50-seat""laneway 入口"等细节一律不进文案）
- 不点名任何具体转票个人/账号（P3 收尾只讲"加价转票、来源不明的二手票"这一模式）

## 渲染状态

- 模板: `cards/010/index.html`（复制自 `cards/001/index.html`；已 diff 确认 001/003/006/009
  的第 1–845 行即全部 CSS / `data-theme="aushow"` 主题色 token / 字体逐字相同，仅
  `<title>` 不同）
- 卡片: 4 张（封面 / 票根 / 去之前先看这4条 / CTA），无配图
- 版式预防：`.ledger-title` 为 42px，`.ledger-row` 网格 `96px 1fr auto` 且 note 吃满
  460px 后 title 列仅剩约 300px。本篇 02 行标题 "Club Voltaire"（13 个拉丁字符）按 42px
  估算约 273px，余量不足 30px，故对该行单独内联 `font-size:36px` 保证不折行；其余
  ledger 标题（"常驻场次""Eventbrite""票价未标"）均在安全宽度内
- P2 票根大字位用「常驻」两字替代日期数字（该条目 `date=null` 且无固定星期），
  `.tk-num` 为 168px/weight 900，两个中文字约 336px，票根内可用宽度约 808px，不会溢出；
  unit 位写"场次见 EVENTBRITE"承接"具体哪天要自己查"这个事实
- 渲染方式：本次会话按 `daily-xhs-prompt.md` 第0节**未调用任何浏览器截图工具**，
  渲染交给 `automation/render_card.py`（headless Chrome 逐张单独截图）由
  `run_daily_xhs.sh` 在本任务结束后执行
