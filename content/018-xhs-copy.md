# 018 — 悉尼这场为什么叫「海洋」（单场演出安利）

**选题类型**：单场演出安利（周一轮换位，2026-09-07 生成）
**信源条目**：`data/events.json` → 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会（verified=true）

**选场说明（池子仍为空，属"换角度重讲"）**：8 条 verified 中未被单场安利过的只剩 AKMU 两场，
两条自 08-24 起挂在 `EXCEPTIONS.md` OPEN（墨站 `ticket_platform=Ticketek` 与场馆官方 AXS 口径
冲突；悉站 `venue` 为旧名且 `price`/`time` 仍为 null），今日 `git log -- data/events.json` 确认
相关字段仍未改动，按红线不可发。袁娅维两场（08-20 / 08-22）演出日已过。故按提示词第 2 步
"全部用过一轮就选最久没被安利过的那条换角度重讲"，取 **002（2026-08-17 生成，21 天前）
安利过的周杰伦悉尼站**——它是四条已用条目里最久没被单场安利过的一条
（001 已于 015 在 09-04 重讲、006 用于 08-24、010 用于 08-28）。

**与既有篇目的差异化**：
- **002**（21 天前）是"开票了"的播报式安利，把 JSON 七个字段平铺一遍。
- **015**（09-04）是墨尔本站的倒计时决策篇（凑齐 6 人 / 先定价位档）。
- **008**（08-26）是 ENGIE Stadium 的入场攻略（包别超 A4、交通、禁带物）。
- **014**（09-03）是按城市排的汇总，悉尼站只占其中一条。
- **本篇（018）的角度是「名字」**：悉尼站叫「海洋」、墨尔本站叫「粉色」，这两个主题词就写在
  两条 `title_zh` 里，前四篇一次都没解释过它们是什么意思。今天查证后确认这是该巡演"一城一主题"
  的设定，且两个词合起来正好是他一首收录曲的名字。这是一条**只有这场有、别的场次给不出**的
  内容，也是账号"情绪价值"那一栏第一次真正落到演出本身而不是抢票动作上。
- 场馆交通/入场规则一句不碰（008 的范畴），倒计时不做主叙事（015 的范畴）。

**本次额外核实**：该条目 `verified` 打于 2026-07-03，距今 2 个月，且有 AKMU 字段随场馆换票务商
而失真的前车之鉴，故今日对日期/星期/时间/场馆/平台/状态/限购/主办方逐条做了 `events.json`
之外的独立复核（见事实核查表），并新查了主题名与曲目两项本篇新增内容。

**主动排除项**：
- **不写"主题灵感来自《粉色海洋》这首歌"**——该因果说法只见于二手媒体（新浪等），维基百科
  巡演词条只写"本次演唱會將有城市的獨特主題"，未写灵感出处。本篇只陈述"两个主题词合起来
  正好是这首歌的名字"这一可核对的事实，不替主办方宣称创作动机。
- **不写"悉尼站是澳洲收官场/最后一场"**——官方页面无"final show"字样，只能说澳洲一共排了
  两场、悉尼是靠后开唱的那场。
- **不写"AR 沉浸式舞台""花瓣雨"等舞美细节**——仅见于二手媒体，官方场馆页只写到
  "a groundbreaking stage, combining innovative structures and unprecedented design"。
- **不写余票水位**——"Low Availability" 是 Ticketmaster 平台今日的状态标签，会随时间变化，
  只在正文里带日期标注引用一次，**不进任何一张卡片**（卡片是发布后长期留存的物料，
  不放会过期的瞬时标签）。
- **不写入场规则/交通/禁带物**——008 场馆攻略已写透，且属该栏目范畴。本篇只取"6:00pm 开门"
  一条（与 JSON 里 19:30 开演直接配对，回答"当天几点到"）。

## 标题（12字）

悉尼这场为什么叫「海洋」

## 正文（发帖文案，无外链）

周杰伦「**海洋** 悉尼 嘉年华Ⅱ」世界巡回演唱会——很多人扫过一眼就划走了，没注意演出全名里那两个字。

📍ENGIE Stadium（Sydney Olympic Park），11 月 21 日**周六**，晚 7:30 开演，6 点开门，Ticketmaster 官方开票中。

**先说那个名字。** 澳洲这轮一共只排了两场，一城一个主题词：墨尔本站叫「粉色」（10 月 17 日 Marvel Stadium），悉尼站叫「海洋」。两个词合起来，正好是他 2022 年那张《最伟大的作品》里的第 10 首——《粉色海洋》，方文山作词、周杰伦作曲，副歌里那段童声是他儿子 Romeo 唱的，MV 当年也是在澳洲取的景。

所以澳洲这两场不是随手排的两个日期。你去的那场叫什么，本身就是一句话。

**再说要花的钱和该定的事。**

🎫 票价 $188–$748，另加 $9.90 手续费。
🎫 官方购票平台 Ticketmaster，每账户限购 6 张。
🎫 主办方 Sky Music & Horizon Production。

还有 75 天，听着不急，但 9 月 7 日我去看官方售票页，墨尔本和悉尼两场的状态标签**都已经是 "Low Availability"** 了。这只是平台标签、不是余票数字，具体以官网当下为准——但"再等等看"这四个字，在这种标签下的性价比不高。

官方票价永远是唯一标准。加价转票、来源不明的二手票，风险自己扛。

想去的评论区扣 1，私信告诉你怎么抢票，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出，不再错过任何一场。

#周杰伦 #悉尼演唱会 #澳洲华人 #演唱会情报 #粉色海洋

## 卡片文案结构（5张，票根美学）

> 张数说明：前四篇单场安利均为 4 张（封面／票根／购票须知／CTA）。本篇多出的一张是 **P2「名字的来历」**——
> 它就是本篇区别于 002/015 的全部内容，塞进封面的 lead 一行放不下三条并列事实（两个主题词 + 一首歌），
> 压进 P4 购票须知又会把"该花多少钱"和"名字的故事"两件不相干的事混在一张 ledger 里。
> 五张各自饱满，无空卡、无凑数卡。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 演出情报 · 单场安利
- 大字标题: 悉尼这场 / 叫「海洋」
- 副标题: 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会
- 配图: 官方澳洲巡演艺人页头图（Ticketmaster 提供，即该条目 `image` 字段；alt 写"澳洲巡演官方宣传图"，
  不宣称其为悉尼专属海报——沿用 002 的处理，对应账号红线"海报张冠李戴"）
- 说明: 11 月 21 日（周六）ENGIE Stadium，晚 7:30 开演，官方开票中。
- 底部条: 11.21 · SYD — Ticketmaster 开票中

**P2 名字的来历（ledger 3条）**
- kicker: 名字的来历
- 大字: 澳洲两场 / 各带一个词
1. 墨尔本叫「粉色」 — 10 月 17 日 Marvel Stadium，主题词就写在演出全名里
2. 悉尼叫「海洋」 — 11 月 21 日 ENGIE Stadium，同一轮巡演的另一个主题词
3. 合起来是首歌 — 《粉色海洋》，2022 年《最伟大的作品》第 10 首，方文山作词、周杰伦作曲，儿子 Romeo 献声，MV 在澳洲取景
- 收尾: 澳洲一共只排了两场，一城一个主题词。你去的那场叫什么，本身就是一句话。
- 底部条: 主题名取自演出全名 — 曲目资料来自公开唱片条目

**P3 票根组件**
- 演出: 周杰伦「海洋 悉尼嘉年华Ⅱ」世界巡回演唱会
- 日期: 21 NOV 2026 ｜ 状态徽章: ON SALE 开票中
- 场馆: ENGIE Stadium（悉尼 Sydney Olympic Park）
- 时间: 19:30（18:00 开门）

**P4 购票须知（ledger 4条）**
- kicker: 购票须知
- 大字: 下单前 / 先看这 4 条
1. $188–$748 — 票价区间（另加 $9.90 手续费）
2. Ticketmaster — 官方购票平台
3. 限购 6 张 — 每账户购买上限
4. 官方主办 — Sky Music & Horizon Production
- 收尾: 官方票价是唯一标准——加价转票、来源不明的二手票，风险自己扛。
- 底部条: 信息来自主办方公告 — 下单前建议官网复核

**P5 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 「海洋」那场 / 你去不去？
- 正文: 评论区扣 1，私信告诉你怎么抢票，还有后续开票提醒。
- 底部条: VOL. 018 — 简介里有完整演出日历

## 事实核查表

| 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|
| 演出名「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` 该条目 `title_zh`（`verified=true`） | 逐字复制 |
| 日期 2026-11-21 | GREEN | `events[].date`；独立复核 Sydney Showground 官方活动页 https://www.sydneyshowground.com.au/whats-on/jay-chou-carnival--world-tour/ 原文 "Saturday 21 November"；Ticketmaster 艺人页 https://www.ticketmaster.com.au/jay-chou-tickets/artist/1260229 列 "Sydney - November 21, 2026" | 三处一致 |
| 11 月 21 日是周六 | GREEN | 同上 Sydney Showground 官方页原文 "Saturday 21 November"；`python3` 核算 2026-11-21 = Saturday | 002 未写过，本篇新增 |
| 开演时间 19:30 | GREEN | `events[].time`；独立复核 Sydney Showground 官方页 "7:30pm – Event starts"；Ticketmaster 艺人页 "Sydney - November 21, 2026, 7:30 PM" | 三处一致 |
| 6:00pm 开门 | GREEN | Sydney Showground 官方活动页原文 "6:00pm – Gates open" | `events.json` 无此字段，属外部一手核实新增项（与 015 新增"周六"同一处理方式）；与 19:30 配对回答"当天几点到" |
| 场馆 ENGIE Stadium（悉尼 Sydney Olympic Park） | GREEN | `events[].venue` / `events[].city`；独立复核 Sydney Showground 官方页（ENGIE Stadium 位于 Sydney Showground）；Ticketmaster 艺人页 "ENGIE Stadium, Olympic Park, NSW" | 三处一致 |
| 票价 $188–$748（另加 $9.90 手续费） | GREEN | `events[].price`（`verified=true` 字段，002 已用同一值） | 今日 Ticketmaster 巡演页与场馆官方页均不展示票价，无第二信源，但**亦无任何相反证据**；卡片保留"下单前建议官网复核"提示。注意与墨尔本站 $208 起不同，未串用 |
| 购票平台 Ticketmaster | GREEN | `events[].ticket_platform`；独立复核 Sydney Showground 官方页写 "Tickets are officially on sale now" 并指向 Ticketmaster；Ticketmaster 巡演页 https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 为官方售票页 | 两处一致；表述用"官方购票平台"而非"唯一"，沿用 002 口径（JSON 未断言排他性） |
| 状态 on_sale（开票中） | GREEN | `events[].status`；独立复核 Sydney Showground 官方页今日原文 "Tickets are officially on sale now" | 两处一致 |
| 每账户限购 6 张 | GREEN | `events[].notes`「每账户限购6张」；独立复核 Ticketmaster 巡演页原文 "You may purchase a maximum of 6 tickets per person." | 上限同为 6。官方页口径是"每人"、JSON 是"每账户"，文案取 JSON 逐字表述；正因两者有差异，本篇不给"拆账号下单"之类操作建议（沿用 015） |
| 主办方 Sky Music & Horizon Production | GREEN | `events[].notes`；独立复核 Ticketmaster 巡演页原文 "proudly organised by Sky Music and Horizon Production" | 两处一致（官方页另列赞助商 CovaU / Petmima，本篇不提，非主办方） |
| 澳洲一共只排了两场（墨尔本 10-17、悉尼 11-21） | GREEN | Ticketmaster 巡演页只列 "October 17, 2026 – Marvel Stadium, Melbourne VIC" 与 "November 21, 2026 – ENGIE Stadium, Sydney NSW" 两场；维基百科「嘉年華II世界巡迴演唱會」词条记大洋洲段 2 场；`data/events.json` 中周杰伦条目亦仅此两条 | 只说"只排了两场"，**不说"收官场/最后一场"**——官方无此字样 |
| 墨尔本站主题词「粉色」／悉尼站主题词「海洋」 | GREEN | `data/events.json` 两条 `title_zh` 内即含「粉色 墨尔本」「海洋 悉尼」；独立复核维基百科「嘉年華II世界巡迴演唱會」词条，墨尔本场城市主題「粉色」、悉尼场城市主題「海洋」，并写明 "本次演唱會將有城市的獨特主題" | 两处一致；本篇只陈述主题名，不宣称其创作动机 |
| 《粉色海洋》为 2022 年《最伟大的作品》专辑第 10 首，方文山作词、周杰伦作曲，其子 Romeo 献声 | GREEN | 维基百科「最偉大的作品」词条曲目表第 10 轨：「粉色海洋（兒子Romeo獻聲）」，作詞 方文山、作曲 周杰倫 | 逐字对应曲目表字段 |
| 《粉色海洋》MV 在澳洲取景 | GREEN | 同上维基百科「最偉大的作品」词条 MV 段落记该曲 MV 于澳洲拍摄 | 文案只写"MV 在澳洲取景"，**不点具体湖名**——词条给出的地名与常见报道说法不一致，未逐字确证，故不写 |
| 2026-09-07 Ticketmaster 艺人页两场状态标签均为 "Low Availability" | GREEN | 今日实取 https://www.ticketmaster.com.au/jay-chou-tickets/artist/1260229 ，Melbourne 与 Sydney 两条均标 "Low Availability" | 正文带日期标注引用，并明写"这只是平台标签、不是余票数字"；**不进任何卡片**（瞬时标签不做长期物料） |
| 距演出 75 天（2026-09-07 → 2026-11-21） | GREEN | 由 `events[].date` 与生成日算术得出，`python3` 核算 = 75 天 | 派生值，非新事实 |
| link_ok=true（购票链接可访问） | GREEN | `events[].link_ok`；今日 WebFetch 该 Ticketmaster 巡演 URL 成功返回内容 | 未在正文/卡片放外链，仅用于内部核实 |
| 封面图为周杰伦澳洲巡演官方宣传图 | GREEN | `events[].image`（Ticketmaster 官方站资源，与 002 同一 URL） | 该图为巡演艺人页通用头图，文件名含 "Mel"；alt 写"澳洲巡演官方宣传图"而非"悉尼站海报"，避免宣称其为悉尼专属物料 |

**主动判为不可用、已从文案剔除的内容**（不计入 CHECKED）：
- "主题灵感源自《粉色海洋》这首歌"——只有二手媒体（新浪等）如此叙述，维基百科巡演词条未写灵感出处，
  官方页面亦无。已剔除因果表述，只保留"两个主题词合起来是这首歌的名字"这一可核对事实。
- "悉尼站舞台用 AR 打造沉浸式效果""墨尔本站有花瓣雨"——仅见二手媒体，官方场馆页只有笼统的
  "groundbreaking stage… unprecedented design"，无法核实具体舞美，整条不写。
- "悉尼超级穹顶"——检索结果中出现的这一场馆说法与官方口径（ENGIE Stadium）冲突，属二手媒体错误，
  不采用；本篇场馆一律以 JSON + 场馆官方页为准。
- 检索中再次出现社交平台账号兜售"澳洲站 VIP 门票预定"，按账号红线不作为信源、不点名（同 014）。

FACT-AUDIT-STATUS: RED=0 CHECKED=19 SOURCES-CITED=19

## 渲染状态

- 模板: `cards/018/index.html`（复制自 `cards/001/index.html`，保留 `<html data-theme="aushow">`
  与全部主题色 token、`.ticket`/`.ledger`/`issue-strip` 组件样式与字体，仅替换 poster 区块内的文案/数据）
- 卡片数: 5 张 `<section class="poster xhs" id="xhs-01…05">`
- 渲染: 交由 `automation/render_card.py`（headless Chrome 逐张截图，1080×1440）
- 本次会话按提示词第 0 节要求，未调用任何浏览器/截图工具
