# 028 — 就这3场：下周、下月、11月（本周开票汇总）

**选题类型**：本周开票汇总（周四轮换位，2026-09-17 生成）

**信源条目**（全部 `data/events.json` → `verified=true`，共选 3 场）：
1. Rolling Donkey 中文喜剧开放麦（悉尼，每周二）
2. 周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会（2026-10-17）
3. 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会（2026-11-21）

**本篇口径决定（先说清楚）**：

- **沿用 005/009/014/021 的"不说'本周开票'"口径。** 3 条 `status` 都是 `on_sale`（已在售），
  `events.json` 里没有任何字段支持"这些票是本周开售的"。栏目定位保留（仍记为"本周开票汇总"），
  标题/卡面一律用"在售""官方票面"这类可核实的表述。

- **角度与 005/009/014/021 刻意错开，这是第 5 种切分：按"你离它还有几天"的倒计时排。**
  005=按日期时间线、009=按提前量（大场 vs 常驻）、014=按城市、021=按票价档位——四篇都没有
  用过"从今天起倒数还剩几天 + 现在该做什么"这个决策视角。本篇的底料也从 4 场缩到 **3 场**：
  候场喜剧 Loadingzone"常驻开放麦 · on_sale"自 2026-09-14 起无法在 Eventbrite 主办方页核实到
  当前开放麦场次（已挂 EXCEPTIONS OPEN，见 025 值班日志），按红线"未核实的不发"本轮整条不列。
  所以本篇是**第一次只有 3 场的清单**，标题里的"就这 3 场"正是这个诚实状态。

- **倒计时数字是本篇新增事实。** 生成日 2026-09-17 到三场分别是 5 天（下周二 09-22）、
  30 天（10-17，今天正好满月）、65 天（11-21）。前四篇只把"距今 N 天"当行末括注顺手列一下
  （021 写过 37/72 天），从没把它当组织原则，更没把"今天距开演正好 30 天"当成时间钩子。

**排除项摘要**：

- **袁娅维 TIA RAY 墨尔本站（2026-08-20）/ 悉尼站（2026-08-22）**——两条均 `verified=true`，
  但演出日期都早于生成日 2026-09-17，已开演，不进"接下来能买"的清单。
- **AKMU 乐童音乐家 墨尔本站（09-18，明天）/ 悉尼站（09-20）**——仍在 `EXCEPTIONS.md` OPEN：
  墨尔本站 `ticket_platform="Ticketek"` 已确证失真（Melbourne Park 自 2026-08-22 改由 AXS 承接），
  悉尼站 `venue="ICC Sydney Theatre"` 为旧名且 `price`/`time` 仍为 null。两条字段未修，按红线不收。
- **候场喜剧 Loadingzone Comedy（墨尔本，常驻）**——`title_zh`/`city`/`venue` 均 verified，但
  "常驻开放麦 · on_sale"今日在 Eventbrite 主办方页核实不到当前开放麦场次（09-14 已挂 OPEN），
  本轮整条不列。**不点名**，正文只写通用原则"核实不到当前场次的宁可空着也不写"。

**红线自查**：3 条全部 `verified=true`；日期/场馆/票价/平台逐字取自 JSON 字段；`price` 为 null 的
Rolling Donkey 不编造票价；`time` 存疑的场次不写时间（Rolling Donkey 19:30 已由 Eventbrite 原文
"Every Tuesday, 7:30 PM" 佐证）；正文无外链；未点名任何个人/账号/转售平台。

## 标题（14字）

就这3场：下周、下月、11月

## 正文（发帖文案，无外链）

这份清单按日期排过、按城市排过、按票价排过，今天换个问法——**你离下一场还有几天**？

官方在售、我们逐字核实过的华人演出，现在能列给你的就这 3 场，从下周二一路排到 11 月 👇

**⏱ 5 天后 · 下周二 09-22 · 悉尼**
🐴 Rolling Donkey 中文喜剧开放麦
每周二晚 7:30，Chippo Hotel（87-91 Abercrombie St, Chippendale）
Eventbrite 报名，官方未标价。这周就能去，下班解压刚好。

**⏱ 30 天后 · 10-17 周六 · 墨尔本**
🌸 周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会
晚 7:30，Marvel Stadium
官方票面 $208 – $748（另加 $9.90 手续费），Ticketmaster。今天距开演正好 30 天整，跨城看的朋友可以开始订机票住宿了。

**⏱ 65 天后 · 11-21 周六 · 悉尼**
🌊 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会
晚 7:30，ENGIE Stadium (Sydney Olympic Park)
官方票面 $188 – $748（另加 $9.90 手续费），Ticketmaster。最远的一场，可以先盯着，不急这一周。

📌 老规矩：只列逐字核实过的，核实不到当前场次的宁可空着也不写。两站周杰伦都是 Ticketmaster 官方每人最多 6 张；官方票面最高一档就是 **$748**，超过这个数的"内部渠道""前排锁位"，多出来的钱不会变成更好的座位。

评论区扣 1，私信发你这份 3 场清单和官方票价档位，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #悉尼 #墨尔本 #周杰伦 #开放麦 #脱口秀 #演唱会情报 #留学生活

## 卡片文案结构（3张，票根美学）

> 张数说明：本篇是"倒计时清单"结构，3 场演出各一行、字段密度接近（都有日期+场馆+平台，
> 两场有票价、一场未标价），合进一张 ledger 即可。封面与 CTA 是账号固定品牌结构。
> 比 005/009/014/021（4 张）少一张，是因为本篇没有"两档对照"这种需要第二张内容卡的结构，
> 不硬凑空卡。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 本周在售 · 倒计时清单
- 大字标题: 就这3场 / 下周·下月·11月
- 副标题: 5 天 · 30 天 · 65 天，离你最近的三场
- 说明: 官方在售、逐字核实过的华人演出，数得出来的就这 3 场。
- 底部条: 现在都在售 — 3 场 · 悉尼 & 墨尔本
- 配图: 无（汇总篇涉及多组演出方，挂任一张海报都有"张冠李戴"风险，整篇不挂图；沿用 004/005/008/009/014/021）

**P2 倒计时清单（ledger 3条）**
1. 5 天后 — 下周二 09-22 · Rolling Donkey 中文喜剧开放麦 · 每周二 19:30 · Chippo Hotel，87-91 Abercrombie St, Chippendale · Eventbrite（官方未标价）
2. 30 天后 — 10.17 周六 19:30 · 周杰伦「粉色 墨尔本 嘉年华Ⅱ」· Marvel Stadium · Ticketmaster · $208–$748（另加 $9.90 手续费）
3. 65 天后 — 11.21 周六 19:30 · 周杰伦「海洋 悉尼 嘉年华Ⅱ」· ENGIE Stadium (Sydney Olympic Park) · Ticketmaster · $188–$748（另加 $9.90 手续费）
- 收尾: 两站周杰伦都是 Ticketmaster 官方规则每人最多 6 张，官方票面最高一档就是 $748。
- 底部条: 官方票价是唯一标准 — 别从站外二维码走
- 版式说明: ledger-row 网格沿用 021（`96px 1fr auto`，note 占 460px 后 title 列只剩约 300px），
  title 一律压到 "5/30/65 天后" 这种 2–4 字，完整演出名/场馆/票价放进 note，避免 42px 标题折行

**P3 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 先盯哪场 / 看日子就知道
- 正文: 评论区扣 1，私信发你这份 3 场清单和官方票价档位，还有后续开票提醒。
- 底部条: VOL. 028 — 简介里有完整演出日历

## 事实核查表

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | 演出名「Rolling Donkey 中文喜剧开放麦(悉尼,每周二)」 | GREEN | `data/events.json` 该条目 `title_zh`，`verified=true`，逐字复制；外部复核 https://www.eventbrite.com/e/copy-of-rolling-donkey-tickets-1983189907399 页面标题 "Rolling Donkey 驴打滚每周二中文喜剧开放麦" |
| 2 | Rolling Donkey 每周二举行、19:30 开演 | GREEN | 同条目 `time="19:30"`；外部复核同上 Eventbrite 页原文 "Every Tuesday, 7:30 PM" |
| 3 | Rolling Donkey 场馆 Chippo Hotel，87-91 Abercrombie St, Chippendale（悉尼） | GREEN | 同条目 `venue` / `city="悉尼"`；外部复核同上 Eventbrite 页原文 "Chippo Hotel, 87-91 Abercrombie Street, Chippendale, NSW 2008" |
| 4 | Rolling Donkey 报名平台 Eventbrite、官方未标价 | GREEN | 同条目 `ticket_platform="Eventbrite"`、`price=null`；外部复核同上页面今日仍为 live 的 recurring 场次页，全文未列出任何票价 |
| 5 | Rolling Donkey 距生成日 5 天，且为"下周二 09-22" | GREEN | 由生成日 2026-09-17 与 Eventbrite 原文 "Every Tuesday" 计算：2026-09-22 − 2026-09-17 = 5 天；09-22 为周二（09-17 是周四） |
| 6 | 演出名「周杰伦「粉色 墨尔本 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` 该条目 `title_zh`，`verified=true`，逐字复制 |
| 7 | 墨尔本站 2026-10-17（周六）、19:30 开演 | GREEN | 同条目 `date="2026-10-17"` / `time="19:30"`；外部复核 https://musick.com.au/gig/jay-chou-carnival-ii-world-tour-in-melbourne-2026-10-17/ 原文 "17 Oct 2026" 及 WebSearch 汇总 "2026年10月17日（星期六）""晚上7:30开演" |
| 8 | 墨尔本站场馆 Marvel Stadium，城市墨尔本 | GREEN | 同条目 `venue="Marvel Stadium"` / `city="墨尔本"`；外部复核 WebSearch 汇总 "Marvel Stadium, Harbour Esplanade, Docklands, Melbourne, VIC" |
| 9 | 墨尔本站票价 $208–$748（另加 $9.90 手续费）、平台 Ticketmaster | GREEN | 同条目 `price="$208–$748 (+$9.90手续费)"` / `ticket_platform="Ticketmaster"`；外部复核 WebSearch 汇总档位表 "AUD$748 / $648 / $548 / $448 / $348 / $248 / $208（不含 $9.90 手续费）"，端点与 JSON 一致 |
| 10 | 墨尔本站距生成日 30 天（今天正好满月） | GREEN | 由生成日 2026-09-17 与同条目 `date` 计算：2026-10-17 − 2026-09-17 = 30 天 |
| 11 | 演出名「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` 该条目 `title_zh`，`verified=true`，逐字复制 |
| 12 | 悉尼站 2026-11-21（周六）、19:30 开演 | GREEN | 同条目 `date="2026-11-21"` / `time="19:30"`；外部复核今日 WebSearch 汇总 "同巡演悉尼站为2026年11月21日" 及 021 已复核 https://hk.trip.com/events/ 原文 "2026 年 11 月 21 日（星期六）""19 時 30 分" |
| 13 | 悉尼站场馆 ENGIE Stadium (Sydney Olympic Park)，城市悉尼 | GREEN | 同条目 `venue` / `city="悉尼"`；外部复核今日 WebSearch 汇总 "Engie Stadium"（主题「海洋」） |
| 14 | 悉尼站票价 $188–$748（另加 $9.90 手续费）、平台 Ticketmaster | GREEN | 同条目 `price="$188–$748 (+$9.90手续费)"` / `ticket_platform="Ticketmaster"`；外部复核 021 已核实 https://hk.trip.com/events/ 原文档位 "AUD 748 / 648 / 548 / 448 / 348 / 248 / 188"，端点与 JSON 一致 |
| 15 | 悉尼站距生成日 65 天 | GREEN | 由生成日 2026-09-17 与同条目 `date` 计算：2026-11-21 − 2026-09-17 = 65 天 |
| 16 | 三场按倒计时排序 5 天 < 30 天 < 65 天 | GREEN | 由第 5/10/15 行三个天数直接比较得出，纯算术，未引入新断言 |
| 17 | 两站周杰伦都是 Ticketmaster 官方规则每人限购 6 张 | GREEN | 两条目 `notes="主办方 Sky Music & Horizon Production;每账户限购6张"`；外部复核 WebSearch 汇总 "每个 Ticketmaster 账户最多可购买 6 张门票" |
| 18 | 官方票面最高一档就是 $748 | GREEN | 由 021 已复核的两张档位表（https://www.wesydney.com.au/03271740/ 墨站 "AUD$748…"、https://hk.trip.com/events/ 悉站 "AUD 748…"）比对得出：两站最高档均 $748 |
| 19 | "就这 3 场（逐字核实、官方在售）"表述成立 | GREEN | `data/events.json` 中 `verified=true` 共 8 条，逐条排除后剩 3：袁娅维×2 演出日（08-20/08-22）已早于生成日；AKMU×2 字段失真（OPEN）；Loadingzone 常驻开放麦当前无法核实（OPEN）。剩 3 条 `status="on_sale"` 且字段可逐字核实 |
| 20 | 正文 CTA"评论区扣1私信"与"官方票价是唯一标准"防骗口径 | GREEN | 账号档案 `~/.claude/skills/xhs-content/accounts/aushow.md` CTA 模板 + 红线段，与已发布 001/005/009/014/021 同款表述一致 |

**主动排除项（无依据、依据冲突、瞬时状态或已过期，本篇一律不写）**：

- **袁娅维 TIA RAY 墨尔本站（08-20）/ 悉尼站（08-22）**——`verified=true` 但演出日期早于生成日
  2026-09-17，已开演，整组剔除。
- **AKMU 乐童音乐家 墨尔本站（09-18）/ 悉尼站（09-20）**——仍在 `EXCEPTIONS.md` OPEN：
  墨站 `ticket_platform` 已确证失真应改 AXS，悉站 `venue` 为旧名且 `price`/`time` 为 null，
  截至今日 `data/events.json` 未修。整组不收。
- **候场喜剧 Loadingzone Comedy（墨尔本，常驻）**——"常驻开放麦 · on_sale"今日无法在 Eventbrite
  主办方页核实到当前开放麦场次（09-14 挂 OPEN），整条不列；正文不点名，只写通用原则。
- **"Low Availability / 余票紧张"**——今日 WebSearch 见 Ticketmaster 对墨尔本站标 "Low Availability"，
  属瞬时余票状态，沿用 018 的既定处理不进正文/卡片。
- **座位区域名称（"山顶票""VIP区"）**——021 已定性：唯一来源在相邻数字上被证伪，剔除。
- **门票绑定观演人/不支持转赠**——021 已定性：单一二手来源，Ticketmaster 官方页无此说法，剔除。
- **赞助商 CovaU / Petmima、6 岁以下不得入场、无障碍订票热线**——与读者"该盯哪场、何时动手"的
  主线无关，汇总篇信息密度已高，不写（省略不等于错误）。
- **周杰伦两场的主办方**——JSON `notes` 有 "Sky Music & Horizon Production"，但汇总篇只取限购条款，
  与 005/009/014/021 处理一致。
- **`verified=false` 的其余条目**——events.json 未核实条目一条不进本篇（账号红线）。
- **开门/检票时间、座位视野、寄存、退改签政策、余票量**——events.json 无对应字段，不写。

FACT-AUDIT-STATUS: RED=0 CHECKED=20 SOURCES-CITED=20

## 渲染状态

- 模板: `cards/028/index.html`，复制自 `cards/021/index.html`。选 021 为基底的原因：① 其
  `<head>`+CSS 段经 `diff` 比对与 `cards/001/index.html` 除 `<title>` 外完全一致；② 021 已是同模板中
  "无 `frame-img` 外链配图 + `.ledger-note` 内联 `max-width:460px`"这一纯文字版式的验证后代，
  且与本篇同为"倒计时清单"的汇总结构，结构匹配度最高。`<html data-theme="aushow">`、主题色 token、
  字体、`.ticket`/`.ledger`/`issue-strip` 组件样式全部原样保留，仅替换 poster 区块内文案 + `<title>`。
- 卡片数: 3 张 `<section class="poster xhs" id="xhs-01…03">`（比 021 少一张，本篇无"两档对照"
  的第二张内容卡，不凑空卡）。
- `render_card.py` 在计数前会剥掉 HTML 注释（`html_no_comments`），模板顶部示例注释里的
  `id="xhs-01"` 不会被算成 poster，脚本会正确识别为 3 张。
- 渲染: 交由 `automation/render_card.py`（headless Chrome 逐张截图 + PIL 校验 1080×1440）。
  本次会话按 `daily-xhs-prompt.md` 第 0 节要求，**未调用任何浏览器/截图工具**。
