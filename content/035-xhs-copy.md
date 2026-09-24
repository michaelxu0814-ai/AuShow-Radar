# 035 — 本周在售3场，只认两个官方平台（本周开票汇总）

**选题类型**：本周开票汇总（周四轮换位，2026-09-24 生成）

**信源条目**（全部 `data/events.json` → `verified=true`，共选 3 场）：
1. Rolling Donkey 中文喜剧开放麦（悉尼，每周二，Eventbrite）
2. 周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会（2026-10-17，Ticketmaster）
3. 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会（2026-11-21，Ticketmaster）

**本篇口径决定（先说清楚）**：

- **沿用 005/009/014/021/028 的"不说'本周开票'"口径。** 3 条 `status` 都是 `on_sale`（已在售），
  `events.json` 里没有任何字段支持"这些票是本周开售的"。栏目定位保留（仍记为"本周开票汇总"），
  标题/卡面一律用"在售""官方票面"这类可核实的表述。

- **角度与 005/009/014/021/028 刻意错开，这是第 6 种切分：按官方购票平台分。**
  005=时间线、009=提前量（大场 vs 常驻）、014=城市、021=票价档位、028=倒计时——五篇都没有用过
  `ticket_platform` 这个字段当组织原则。本篇把 3 场按官方平台切成 **Eventbrite 1 场 /
  Ticketmaster 2 场**，落点接到账号核心差异化（官方渠道是唯一标准）：买票只认这两个名字，
  官方渠道以外的"转票""内部渠道"入口先打个问号。

- **平台切分本身是 events.json 里已有的字段，非新编造。** `ticket_platform` 逐字取自 JSON：
  Rolling Donkey=Eventbrite，两站周杰伦=Ticketmaster。倒计时数字随生成日更新：5 天（下周二
  09-29）/ 23 天（10-17）/ 58 天（11-21）。

**排除项摘要**：

- **袁娅维 TIA RAY 墨尔本站（08-20）/ 悉尼站（08-22）**——两条均 `verified=true`，演出日期
  早已早于生成日，已开演，不进"接下来能买"的清单。
- **AKMU 乐童音乐家 墨尔本站（09-18）/ 悉尼站（09-20）**——两条演出日均已早于生成日
  2026-09-24（已开演），且仍挂在 `EXCEPTIONS.md` OPEN（墨站 `ticket_platform` 失真、悉站
  `venue` 旧名 + `price`/`time` null）。双重原因不收。
- **候场喜剧 Loadingzone Comedy（墨尔本，常驻）**——"常驻开放麦 · on_sale"自 09-14 起无法在
  Eventbrite 主办方页核实到当前开放麦场次（OPEN），本轮整条不列。**不点名**，正文只写通用原则。

**红线自查**：3 条全部 `verified=true`；日期/场馆/票价/平台逐字取自 JSON 字段；`price` 为 null 的
Rolling Donkey 不编造票价；正文无外链；未点名任何个人/账号/转售平台。

## 标题（15字）

本周在售3场，只认两个官方平台

## 正文（发帖文案，无外链）

这周的华人演出在售清单，还是 3 场，但今天换个更实用的切法：**按官方购票平台分**。

在售场次只挂在这两个官方平台名下——**Ticketmaster** 和 **Eventbrite**。买票只认这两个名字，其他"转票""内部渠道"入口先打个问号 👇

**【Eventbrite】悉尼 · 每周二**
🐴 Rolling Donkey 中文喜剧开放麦
每周二晚 7:30，Chippo Hotel（87-91 Abercrombie St, Chippendale），官方未标价。下周二 09-29 就有，下班解压刚好。

**【Ticketmaster】墨尔本 · 10-17 周六**
🌸 周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会
晚 7:30，Marvel Stadium，官方票面 $208–$748（另加 $9.90 手续费）。还有 23 天开演，跨城看的可以订机票住宿了。

**【Ticketmaster】悉尼 · 11-21 周六**
🌊 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会
晚 7:30，ENGIE Stadium (Sydney Olympic Park)，官方票面 $188–$748（另加 $9.90 手续费）。最远的一场，先盯着。

📌 老规矩：只列逐字核实过的。两站周杰伦都是 Ticketmaster 官方每人最多 6 张；官方票面最高一档就是 $748——超过这个数的"内部渠道""前排锁位"，多出来的钱不会变成更好的座位。

评论区扣 1，私信发你这份 3 场清单和官方票价档位，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #悉尼 #墨尔本 #周杰伦 #开放麦 #演唱会情报 #留学生活

## 卡片文案结构（3张，票根美学）

> 张数说明：本篇是"官方平台清单"结构，3 场演出各一行、字段密度接近（都有日期+城市+场馆+平台，
> 两场有票价、一场未标价），合进一张 ledger 即可，平台名放进 ledger 的 title 列作为切分主线。
> 封面与 CTA 是账号固定品牌结构。与 028（同为 3 场清单）同为 3 张，不硬凑空卡。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 本周在售 · 官方平台清单
- 大字标题: 买票只认 / 这两个平台
- 副标题: Ticketmaster · Eventbrite
- 说明: 官方在售、逐字核实过的华人演出，买票先认准这两个官方名字。
- 底部条: 现在都在售 — 3 场 · 悉尼 & 墨尔本
- 配图: 无（汇总篇涉及多组演出方，挂任一张海报都有"张冠李戴"风险，整篇不挂图；沿用 004/005/008/009/014/021/028）

**P2 官方平台清单（ledger 3条）**
- kicker: 本周在售 · 按官方平台分
- 大字标题: 官方渠道 / 就这两个
1. Eventbrite — 每周二 19:30 · 悉尼 · Rolling Donkey 中文喜剧开放麦 · Chippo Hotel，87-91 Abercrombie St, Chippendale · 官方未标价
2. Ticketmaster — 10.17 周六 19:30 · 周杰伦「粉色 墨尔本 嘉年华Ⅱ」· Marvel Stadium · $208–$748（另加 $9.90 手续费）
3. Ticketmaster — 11.21 周六 19:30 · 周杰伦「海洋 悉尼 嘉年华Ⅱ」· ENGIE Stadium (Sydney Olympic Park) · $188–$748（另加 $9.90 手续费）
- 收尾: 两站周杰伦都是 Ticketmaster 官方规则每人最多 6 张，官方票面最高一档就是 $748。
- 底部条: 只认官方平台 — 别的入口先问一句
- 版式说明: ledger-row 网格沿用 021/028（`96px 1fr auto`，note 占 460px 后 title 列剩约 300px）。
  title 列放平台名（Eventbrite / Ticketmaster，均为 10–11 个半角字符，约 210–260px，不折行），
  完整演出名/场馆/票价/城市放进 note，避免 42px 标题折行。

**P3 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 认准平台 / 再动手买
- 正文: 评论区扣 1，私信发你这份 3 场清单和官方票价档位，还有后续开票提醒。
- 底部条: Vol. 035 — 简介里有完整演出日历

## 事实核查表

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | 演出名「Rolling Donkey 中文喜剧开放麦(悉尼,每周二)」 | GREEN | `data/events.json` 该条目 `title_zh`，`verified=true`，逐字复制；外部复核 https://www.eventbrite.com/e/rolling-donkey-tickets-1983189907399 页面标题「Rolling Donkey 驴打滚每周二中文喜剧开放麦」 |
| 2 | Rolling Donkey 每周二举行 | GREEN | 同条目 `recurrence="每周二"`；外部复核同上 Eventbrite 页标题含「每周二」 |
| 3 | Rolling Donkey 19:30 开演 | GREEN | 同条目 `time="19:30"`；外部复核 Eventbrite 页「每周二 晚 7:30」 |
| 4 | Rolling Donkey 城市悉尼 | GREEN | 同条目 `city="悉尼"`；外部复核 Eventbrite/Chippo 地址 "Chippendale, NSW 2008" |
| 5 | Rolling Donkey 场馆 Chippo Hotel，87-91 Abercrombie St, Chippendale | GREEN | 同条目 `venue` 逐字复制；外部复核 https://www.eventbrite.com/e/rolling-donkey-tickets-1983189907399 「The Chippo Hotel · 87-91 Abercrombie St, Chippendale, NSW 2008」 |
| 6 | Rolling Donkey 报名平台 Eventbrite | GREEN | 同条目 `ticket_platform="Eventbrite"`；外部复核同上页面域名 eventbrite.com |
| 7 | Rolling Donkey 官方未标价 | GREEN | 同条目 `price=null`；外部复核同上页面全文未列票价（032 已核实） |
| 8 | Rolling Donkey "下周二 09-29"（距生成日 5 天） | GREEN | 生成日 2026-09-24 为周四 + 同条目「每周二」推算：下一个周二 = 2026-09-29，09-29 − 09-24 = 5 天 |
| 9 | 演出名「周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` 该条目 `title_zh`，`verified=true`，逐字复制 |
| 10 | 墨尔本站 2026-10-17（周六） | GREEN | 同条目 `date="2026-10-17"`；外部复核 https://www.marvelstadium.mediaservices.com.au/events/916/jay-chou-carnival-world-tour 与 dealmoon「2026年10月17日（星期六）」；日期距生成日 23 天，23 mod 7 = 2，周四 + 2 = 周六 |
| 11 | 墨尔本站 19:30 开演 | GREEN | 同条目 `time="19:30"`；外部复核 Ticketmaster.ch / festivaly / 澳洲微报均标「19:30 / 晚上7点30分」。注：Marvel Stadium 官方页今日标 7:00 pm，疑为开门时间，采信 events.json 与多源一致的 19:30 |
| 12 | 墨尔本站场馆 Marvel Stadium、城市墨尔本 | GREEN | 同条目 `venue="Marvel Stadium"` / `city="墨尔本"`；外部复核同上 Marvel Stadium 官方活动页与 dealmoon「Marvel Stadium, Melbourne」 |
| 13 | 墨尔本站票价 $208–$748（另加 $9.90 手续费） | GREEN | 同条目 `price` 逐字复制；外部复核 dealmoon 档位表 "AUD$748 / $648 / $548 / $448 / $348 / $248 / $208（不含 $9.90 手续费）"，端点与 JSON 一致 |
| 14 | 墨尔本站平台 Ticketmaster | GREEN | 同条目 `ticket_platform="Ticketmaster"`；外部复核多个结果均指 ticketmaster.com.au 官方售票 |
| 15 | 墨尔本站距生成日 23 天 | GREEN | 生成日 2026-09-24 与同条目 `date` 计算：2026-10-17 − 2026-09-24 = 23 天 |
| 16 | 演出名「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` 该条目 `title_zh`，`verified=true`，逐字复制 |
| 17 | 悉尼站 2026-11-21（周六） | GREEN | 同条目 `date="2026-11-21"`；外部复核 https://www.sopa.nsw.gov.au/things-to-see-and-do/jay-chou-carnival-ii-world-tour 与 Shazam「21 nov. 2026」；58 mod 7 = 2，周四 + 2 = 周六 |
| 18 | 悉尼站 19:30 开演 | GREEN | 同条目 `time="19:30"`；外部复核 Shazam「7:30 PM」 |
| 19 | 悉尼站场馆 ENGIE Stadium (Sydney Olympic Park)、城市悉尼 | GREEN | 同条目 `venue` / `city="悉尼"` 逐字复制；外部复核同上 sopa.nsw.gov.au「Sydney Olympic Park, ENGIE Stadium」 |
| 20 | 悉尼站票价 $188–$748（另加 $9.90 手续费） | GREEN | 同条目 `price` 逐字复制；外部复核 021 已核实 https://hk.trip.com/events/ 原文档位 "AUD 748 / 648 / 548 / 448 / 348 / 248 / 188"，端点与 JSON 一致 |
| 21 | 悉尼站平台 Ticketmaster | GREEN | 同条目 `ticket_platform="Ticketmaster"`；外部复核 Ticketmaster AU 艺人页 https://www.ticketmaster.com.au/artist/1260229 |
| 22 | 悉尼站距生成日 58 天（为三场中最远） | GREEN | 生成日 2026-09-24 与同条目 `date` 计算：2026-11-21 − 2026-09-24 = 58 天，58 > 23 > 5 |
| 23 | 两站周杰伦都是 Ticketmaster 官方规则每人限购 6 张 | GREEN | 两条目 `notes="主办方 Sky Music & Horizon Production;每账户限购6张"`；外部复核 dealmoon「每个账户最多购买 6 张门票」 |
| 24 | 官方票面最高一档就是 $748 | GREEN | 两站 `price` 区间上端均为 $748；外部复核墨站档位表（见第 13 行）与悉站档位表（见第 20 行）最高档均 $748 |
| 25 | 在售场次官方平台只有 Ticketmaster / Eventbrite 两个 | GREEN | 三条目 `ticket_platform` 集合 = {Ticketmaster, Eventbrite}，纯集合运算，无新增断言 |
| 26 | "就这 3 场（逐字核实、官方在售）"表述成立 | GREEN | `data/events.json` 中 `verified=true` 共 8 条，逐条排除后剩 3：袁娅维×2 演出日（08-20/08-22）已早于生成日；AKMU×2 演出日（09-18/09-20）已早于生成日且字段失真（OPEN）；Loadingzone 常驻开放麦当前无法核实（OPEN）。剩 3 条 `status="on_sale"` 且字段可逐字核实 |
| 27 | 正文 CTA"评论区扣1私信"与"官方票价是唯一标准"防骗口径 | GREEN | 账号档案 `~/.claude/skills/xhs-content/accounts/aushow.md` CTA 模板 + 红线段，与已发布 001/005/009/014/021/028 同款表述一致 |

**主动排除项（无依据、依据冲突、瞬时状态或已过期，本篇一律不写）**：

- **袁娅维 TIA RAY 墨尔本站（08-20）/ 悉尼站（08-22）**——`verified=true` 但演出日期早于生成日
  2026-09-24，已开演，整组剔除。
- **AKMU 乐童音乐家 墨尔本站（09-18）/ 悉尼站（09-20）**——演出日均已早于生成日（已开演），
  且仍挂 `EXCEPTIONS.md` OPEN（墨站 `ticket_platform` 已确证失真应改 AXS、悉站 `venue` 为旧名且
  `price`/`time` 为 null），`data/events.json` 截至今日未修。整组不收。
- **候场喜剧 Loadingzone Comedy（墨尔本，常驻）**——"常驻开放麦 · on_sale"今日无法在 Eventbrite
  主办方页核实到当前开放麦场次（09-14 挂 OPEN），整条不列；正文不点名，只写通用原则。
- **"Low Availability / 余票紧张"**——今日 WebSearch 见 Ticketmaster 对悉尼站标 "Low Availability"，
  属瞬时余票状态，沿用 018/028 的既定处理不进正文/卡片。
- **墨站开演时间 7:00 pm vs 19:30 分歧**——Marvel Stadium 官方页今日标 7:00 pm，Ticketmaster /
  festivaly / 澳洲微报标 19:30。采信 events.json（19:30）与多源一致口径，已在核查表第 11 行注明。
- **座位区域名称、赞助商、6 岁以下不建议观看、无障碍票热线**——与读者"该认哪个平台、何时动手"的
  主线无关，汇总篇信息密度已高，不写（省略不等于错误）。
- **周杰伦两场的主办方（Sky Music & Horizon Production）**——JSON `notes` 有，但汇总篇只取限购条款，
  与 005/009/014/021/028 处理一致。
- **`verified=false` 的其余条目**——events.json 未核实条目一条不进本篇（账号红线）。
- **开门/检票时间、座位视野、寄存、退改签政策、余票量**——events.json 无对应字段，不写。

FACT-AUDIT-STATUS: RED=0 CHECKED=27 SOURCES-CITED=27

## 渲染状态

- 模板: `cards/035/index.html`，复制自 `cards/028/index.html`。选 028 为基底的原因：① 028 与 001 的
  `<head>`+CSS 段经 `diff` 比对除 `<title>` 外完全一致（028 自记"复制自 021，而 021 已验证与 001 一致"）；
  ② 028 已是同模板中"无外链配图 + `.ledger-note` 内联 `max-width:460px`"这一纯文字版式的验证后代，
  且与本篇同为"3 场清单"的汇总结构，结构匹配度最高。`<html data-theme="aushow">`、主题色 token、
  字体、`.ticket`/`.ledger`/`issue-strip` 组件样式全部原样保留，仅替换 poster 区块内文案 + `<title>`。
- 卡片数: 3 张 `<section class="poster xhs" id="xhs-01…03">`（与 028 同为 3 场清单，不凑空卡）。
- `render_card.py` 在计数前会剥掉 HTML 注释（`html_no_comments`），模板顶部示例注释里的
  `id="xhs-01"` 不会被算成 poster，脚本会正确识别为 3 张。
- 渲染: 交由 `automation/render_card.py`（headless Chrome 逐张截图 + PIL 校验 1080×1440）。
  本次会话按 `daily-xhs-prompt.md` 第 0 节要求，**未调用任何浏览器/截图工具**。
