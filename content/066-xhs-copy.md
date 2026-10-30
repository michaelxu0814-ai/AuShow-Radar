# 066 — 常驻不等于每周几（单场演出安利）

**选题类型**：单场演出安利（周五轮换位，2026-10-30 生成）
**信源条目**：`data/events.json` → 候场喜剧 Loadingzone Comedy 开放麦(墨尔本,常驻)（`verified=true`）

**本次选题决策（为什么是这一条）**：

池子状态——8 条 `verified=true` 里，**6 条的演出日期已过**（袁娅维墨/悉 08-20、08-22；
AKMU 墨/悉 09-18、09-20；周杰伦墨尔本站 **10-17 已演完 13 天**），真正还能安利的只剩 3 条：
周杰伦悉尼站（11-21）、Rolling Donkey（悉尼每周二）、本条。按提示词第 2 步"选最久没被安利过
的那条"：

| 可用条目 | 上次被单场安利 | 距今 |
|---|---|---|
| 周杰伦「海洋 悉尼」 | 060（2026-10-23） | 7 天 |
| Rolling Donkey 开放麦 | 054（2026-10-16） | 14 天 |
| **候场喜剧 Loadingzone（本条）** | **010（2026-08-28）** | **63 天** |

本条是三者里最久没讲的，且它是**唯一不带固定日期**的墨尔本条目（另两条一个在悉尼、一个带
11-21 这个硬日期），不会因为发布日漂移而过期。

**与 010 的角度区别（同一条目第二次讲，必须换切口）**：010 讲的是**存在性**——"墨尔本想笑一场？
这有常驻开放麦"，核心是告诉你这个场子存在。本篇不再介绍存在，改讲**两个最容易被误读的词**：

1. **「常驻」被默认读成「每周几」**。`recurrence` 字段原文是"常驻(场次见Eventbrite)"——它
   **没有公布固定星期**。这跟 006/022/032/042/054 写的 Rolling Donkey 是对立面：那条 JSON 明写
   "每周二"，可以放心告诉读者哪天去；本条不行，凭印象挑个晚上过去就是白跑。两条都是中文开放麦，
   一条能背下来、一条每次都得查，这个对比此前 65 篇没写过。
2. **「开放麦」被默认读成「专场」**。010 全篇没解释过开放麦这个形式是什么。本篇补上，并且
   用它来校准期待值：一晚上很多张面孔、段子有炸有冷是这个形式的**本质**，不是演出翻车。

## 标题（15字）

墨尔本这个中文开放麦，别凭印象去

## 正文（发帖文案，无外链）

墨尔本有个中文开放麦是常驻的：候场喜剧 Loadingzone Comedy。📍Club Voltaire（1st Floor/14 Raglan St, North Melbourne），19:00 开场，Eventbrite 订票。

但"常驻"这两个字最容易被读成"每周几"。我们收录这条时，官方给的口径就是**常驻、场次见 Eventbrite**——它没有公布固定的星期。所以别凭印象挑个晚上直接杀过去，出发前一定自己看一眼当周到底有没有场。

第二件值得先搞清楚的：开放麦不是专场。开放麦这种形式，台下的人也能上台，从新手到职业演员都有，不少人就是来第一次试新段子的；按这类场的通例，喜剧开放麦每个演员一般只有 3–7 分钟。所以一个晚上你会看到很多张面孔、段子有炸也有冷——这是它的本质，不是演出质量翻车。反过来说，它也就是你用最小代价试试"中文脱口秀到底合不合我胃口"的入口。

厂牌本身是 AUNZ Comedy Media 旗下的喜剧厂牌，除了自己的常驻场，也承接国内演员的澳洲巡演，所以值得长期蹲一下。

想去的评论区扣 1，私信把地址和订票页发你～ 澳华演出雷达帮你盯紧全澳华语演出，不再错过任何一场。

#墨尔本脱口秀 #开放麦 #墨尔本生活 #澳洲华人 #演出情报

## 卡片文案结构（4张，票根美学）

**P1 封面**
- kicker: 演出情报 · 单场安利
- 大字标题: 常驻 / 不等于每周几
- 副标题: 候场喜剧 Loadingzone Comedy 开放麦（墨尔本）
- 配图: 无（该条目 `image` 是厂牌通用 banner，非本场海报，沿用 010 的处置，详见"主动排除项"）
- 说明: Club Voltaire，19:00 开场，Eventbrite 订票。官方没给固定星期。
- 底部条: 常驻 · MELB — Eventbrite 售票中

**P2 票根组件**
- 演出: 候场喜剧 Loadingzone Comedy 开放麦（墨尔本）
- 大字: 常驻 ｜ 单位: 场次见 EVENTBRITE ｜ 状态徽章: ON SALE 售票中
- 场馆: Club Voltaire（North Melbourne · 墨尔本 Melbourne）
- 时间: 19:00

**P3 去之前先弄清这 4 条（ledger 4条）**
1. 常驻 — 官方口径只写"场次见 Eventbrite"，没有固定星期
2. 开放麦 — 多位演员轮番上台，每人一般 3–7 分钟（这类场的通例）
3. Club Voltaire — 1st Floor/14 Raglan St, North Melbourne
4. 票价未标 — 我们收录时官方页面未标价，这里不给数字
- 收尾: 官方页面是唯一标准——加价转票、来源不明的二手票，风险自己扛。
- 底部条: 信息来自主办方页面 — 出发前再复核当周场次

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 常驻的那个晚上 / 你赶上过吗？
- 正文: 评论区扣 1，私信把地址和订票页发你，还有后续演出提醒。
- 底部条: VOL. 066 — 简介里有完整演出日历

## 事实核查表

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | 演出名「候场喜剧 Loadingzone Comedy 开放麦（墨尔本，常驻）」 | GREEN | `data/events.json` events[].title_zh，该条目 `verified=true`；逐字复制 |
| 2 | 厂牌名 候场喜剧 Loadingzone Comedy | GREEN | 同上 events[].artist；另今日 WebFetch 核实 https://www.eventbrite.com/o/loadingzone-comedy-75417874333 organizer 名即「候场喜剧Loadingzone Comedy」 |
| 3 | 类别 开放麦 | GREEN | 同上 events[].category；逐字复制，未升格成"专场/演出" |
| 4 | 城市 墨尔本 | GREEN | 同上 events[].city |
| 5 | 场馆 Club Voltaire | GREEN | 同上 events[].venue；另今日 WebFetch 核实场馆官网 https://www.clubvoltaire.com.au/your-visit 为 live 的演出场地（自述 "PERFORMANCES / Wednesday to Sunday / 7pm–11pm"、售票与门口售余票） |
| 6 | 地址 1st Floor/14 Raglan St, North Melbourne | GREEN | 同上 events[].venue；另经上述场馆官网今日原文 "Level 1 / 14 Raglan Street, North Melbourne 3051, VIC AUSTRALIA" 核实（"1st Floor" 与 "Level 1" 同义，门牌街道逐字一致） |
| 7 | 开演时间 19:00 | GREEN | 同上 events[].time（`verified=true`）；旁证为上述场馆官网 "7pm–11pm" 的演出时段与之吻合，**但该时段是场馆通用节目时段、不是本场次承诺**，故文案同时写"出发前复核当周场次"，不把 19:00 绑成某一具体日期的承诺 |
| 8 | 常驻、场次见 Eventbrite、**没有固定星期** | GREEN | 同上 events[].recurrence="常驻(场次见Eventbrite)"；逐字采用。该字段未给任何星期，故全篇不写"每周X"（与 006/022/032/042/054 的 Rolling Donkey "每周二" 不同，那条 JSON 明写了星期） |
| 9 | 购票平台 Eventbrite | GREEN | 同上 events[].ticket_platform；另今日实测上述 organizer 页为 live 的 Eventbrite 主办方页（curl HTTP 200）。正文/卡片未放外链，仅写平台名 |
| 10 | 状态 on_sale（售票中） | **AMBER** | 同上 events[].status。**今日无法独立枚举当周场次**：Eventbrite organizer 页的事件列表为 JS 渲染，静态 HTML 无 JSON-LD（今日 curl 200 但 154KB 正文内 `startDate`/`Club Voltaire`/`开放麦` 零命中）；`/org/75417874333/showmore/?type=future` 端点今日返回 **403 CloudFront**；Club Voltaire 的 Eventbrite 聚合页今日列出 7 场喜剧但**无中文/开放麦场次**。→ 处置：文案**不写"现在就有场次"**，只写"常驻、场次见 Eventbrite、出发前自己看当周"，并把这条列为 AMBER 同步进 EXCEPTIONS 待人工复核 |
| 11 | 厂牌背景「AUNZ Comedy Media 旗下」 | GREEN | 同上 events[].notes；另经上述 organizer 页今日原文 "候场喜剧是澳大利亚AUNZ COMEDY MEDIA旗下运营的…" 核实 |
| 12 | 「也承接国内演员澳洲巡演」 | GREEN | 同上 events[].notes；另经上述 organizer 页今日自述业务覆盖"演出、巡演、线下娱乐、品牌合作、原创内容"核实，正文为 notes 的同义转述，未加"最大/最知名"等 JSON 无据的修饰 |
| 13 | **本篇整块剔除"双语"这个形容词**，只写"喜剧厂牌" | GREEN（处置项） | `events.json` notes 写的是"双语喜剧厂牌"，但上述 organizer 页**今日**自述已是"以喜剧内容为核心的澳洲华语文化厂牌"——与 010（2026-08-28）当时抓到的"专业双语喜剧厂牌"措辞不同。两处口径不一致 → 按本号"打架一律不写"的纪律剔除该形容词，取两者的交集"喜剧厂牌" |
| 14 | 不给任何票价数字 | GREEN | 同上 events[].price=null；另经上述 organizer 页今日核实页面未列票价。故 P3 第 4 条明写"未标价、不给数字" |
| 15 | 开放麦这种形式：台下观众也能上台、新手与职业演员都有、常有人第一次试新段子 | GREEN | https://en.wikipedia.org/wiki/Open_mic 今日原文 "in which audience members may perform on stage whether they are amateurs or professionals" / "often for the first time or to promote an upcoming performance" / "Writers may attend an open mic to try out a new piece for an audience" |
| 16 | 喜剧开放麦每个演员一般 3–7 分钟 | GREEN | 同上，原文 "At a typical comedy open mic, acts will get 3–7 minutes of stage time"。文案已标注为"**这类场的通例**"，不写成本场次的规则 |
| 17 | `link_ok=true`（订票链接可访问） | GREEN | 同上 events[].link_ok；今日 curl 实测该 organizer URL HTTP 200。未在正文/卡片放外链，仅用于内部核实 |
| 18 | 不写具体某一场的日期 | GREEN（处置项） | 同上 events[].date=null，且第 10 条所述三条路径今日均无法取到当周场次 → 全篇零处出现具体日期 |

FACT-AUDIT-STATUS: RED=0 CHECKED=18 SOURCES-CITED=18

## 主动排除项

- **不外挂配图**（沿用 010 的判断）：该条目 `image` 字段虽非 null，但同一个 `img.evbuc.com` URL
  在 `events.json` 里**同时挂在另外三条无关条目上**（候场喜剧"她在场"格斗体验课、"抓马大会"嗑
  瓜子小赛、张慧专场），说明它是厂牌 Eventbrite 主办方页的通用 banner，不是本场开放麦的海报。
  账号已有两次"海报张冠李戴"事故，本篇不放图。
- **不写"每周X"**（`recurrence` 未给星期）——这正是本篇的主题，更不能自己编一个。
- **不写票价**（`price=null`，官方页今日亦未标价）。
- **不写具体场次日期**（`date=null`，且今日三条路径都取不到当周场次，见核查表第 10 条）。
- **不写"本周/明晚"这类依赖发布日的说法**——用户手动审核后发布日期不可控。
- **不写"双语"**（两处官方口径不一致，见核查表第 13 条）。
- **不写入场须知/检票时间/座位视野/场地容量/报名上台流程**——`events.json` 无这些字段；场馆官网
  提到的演出时段 "Wednesday to Sunday" 也**不写进文案**，因为那是场馆整体节目时段，照搬会被读成
  "这个开放麦周三到周日都有"，恰好是本篇要破的那个误读。
- **不写 Club Voltaire 聚合页上那 7 场喜剧的任何一场**（均非本条目、也非 `verified=true`）。
- **不点名任何具体转票个人/账号**（P3 收尾只讲"加价转票、来源不明的二手票"这一模式）。

## 渲染状态

- 模板: `cards/066/index.html`（复制自 `cards/001/index.html`；已 diff 确认 001 与 065 的第 1–845 行
  即全部 CSS / `data-theme="aushow"` 主题色 token / 字体逐字相同，仅 `<title>` 不同）
- 卡片: 4 张（封面 / 票根 / 去之前先弄清这4条 / CTA），无配图
- 版式预防：`.ledger-row` 网格为 `96px 1fr auto`，`.ledger-title` 默认 42px。本篇 03 行标题
  "Club Voltaire"（13 个拉丁字符，按 42px 估算约 273px，余量不足 30px）沿用 010 的处置，单独内联
  `font-size:36px` 保证不折行；其余三行标题（"常驻""开放麦""票价未标"）均在安全宽度内。
  第 02 行 note 较长（"多位演员轮番上台，每人一般 3–7 分钟（这类场的通例）"），标题"开放麦"仅
  3 字，不挤
- P2 票根大字位用「常驻」两字替代日期数字（该条目 `date=null` 且无固定星期），`.tk-num` 为
  168px/weight 900，两个中文字约 336px，票根内可用宽度约 808px，不会溢出；unit 位写
  "场次见 EVENTBRITE" 承接"具体哪天要自己查"这个事实
- P1 大字"常驻／不等于每周几"分两行（`<br>` 后 6 字），`.h-display` 下不溢出
- 渲染方式：本次会话按 `daily-xhs-prompt.md` 第 0 节**未调用任何浏览器截图工具**，渲染交给
  `automation/render_card.py`（headless Chrome 逐张单独截图）由 `run_daily_xhs.sh` 在本任务结束后执行
