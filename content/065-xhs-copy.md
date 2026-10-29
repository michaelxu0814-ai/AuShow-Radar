# 065 — 一场还拿不到票，一场已不能退（本周开票汇总）

**选题类型**：本周开票汇总（周四轮换位，2026-10-29 生成）

**信源条目**（全部 `data/events.json` → `verified=true`，共选 2 场）：
1. 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会（2026-11-21 周六，ENGIE Stadium (Sydney Olympic Park)，Ticketmaster）
2. Rolling Donkey 中文喜剧开放麦（悉尼，每周二，Chippo Hotel，Eventbrite）

**本篇口径决定（先说清楚）**：

- **沿用 005/009/014/021/028/035/041/048/053/059 的"不说'本周开票'"口径。** 2 条 `status` 都是
  `on_sale`（已在售），`events.json` 里没有任何字段支持"这些票是本周开售的"。栏目定位保留
  （仍记为"本周开票汇总"），标题/卡面一律用"在售""官方票面"这类可核实的表述。

- **角度是第 11 种切分：按"官方页面上印着的、不是演出当天的那个日子"分。**
  005=时间线、009=提前量、014=城市、021=票价档位、028=倒计时、035=官方购票平台、
  041=档期月份、048=`time`+星期几、053=`venue`、059=`date`/`recurrence` 对立。
  **本篇不再切 JSON 字段**——池子只剩 2 条，字段维度上周（059）已经切到对立面为止。本篇改切
  **两个官方页面今天各自印着的一句时间规则**，这两句话此前 64 篇一次都没出现过：
  - 周杰伦悉尼站：Ticketmaster 官方巡演页原文 **"Tickets will become available in your account
    2 weeks prior to the event date."**（票要到演出前两周才会出现在你的账号里）→ 11-21 减两周
    = **11-07**，距今 9 天。
  - Rolling Donkey：Eventbrite 官方售票页 Refund Policy 原文 **"Refunds up to 7 days before
    event"**（演出前 7 天以上可退）→ 下一场 11-03 往前 7 天 = **10-27**，前天。
  两句话凑出一组刚好相反的状态：**一场的票还没到任何人手上，一场的退款窗口已经关上。**

- **与 024 的区别要说清楚（两条都是"账号里的条码"，但不是同一件事）**：024 讲的是**转票**流程
  ——Ticketmaster 官方指引里收票方要见到 "Transfer Complete" 条码才进账号；本篇讲的是**原始购票
  的交付时点**——这场演出的票本身要到演出前两周才进账号。024 回答"别人转给我的票到没到"，
  本篇回答"这场的票什么时候才可能存在于任何人的账号里"。两条合起来才完整，文案里把 024 那条
  规则作为搭配提了一句，但不重复其细节。

- **本篇的新事实有五条**：
  1. **悉尼站的票 11-07 才进账号**（官方原文，见上）。这一条有两层用处：买了的人现在看不到条码
     是正常的；而今天（10-29）若有人拿"票的截图"来找你，官方时间线本身就对不上。
  2. **下周二那场的退款窗口在 10-27 已经按字面关上**（官方原文，见上）。
  3. **10 月的周二已经用完了。** 2026 年 10 月只有 4 个周二（10-06 / 10-13 / 10-20 / 10-27），
     最后一个是前天。
  4. **这份清单上，10 月剩下的 2 天（10-30、10-31）一场都没有。** 唯一带日期的场次是 11-21，
     而每周二那条的下一场要到 11-03。
  5. **11 月这份清单上只有两个落点**：每周二，和 11-21 那一场。
- **清单规模与 059 一致**：仍是 2 场、仍然都在悉尼——这是本栏目**连续第二期**只有 2 条，也是
  连续第二期单城（059 是首次单城）。

- **今日外部复核**（两场逐条过了一手源，全部与 `events.json` 一致）：
  Ticketmaster AU 官方巡演页今日原文 "November 21, 2026, – ENGIE Stadium, Sydney NSW" /
  "You may purchase a maximum of **6** tickets per person." / "Only purchase through
  **Ticketmaster Australia** to guarantee you have a valid ticket for entry on event day." /
  "Please Note – Tickets will become available in your account 2 weeks prior to the event date."，
  该页不列票价、明文指向场馆售票页（与 009/021/048/053/059 一致）；Sydney Showground 官方场次页
  今日原文 "Saturday 21 November" / "ENGIE Stadium" / "7:30pm – Event starts"，页面 "Tickets"
  入口指向 ticketmaster.com.au；Eventbrite 售票页今日原文 "每周二 晚7:30"（"Every Tuesday,
  7:30 PM"）/ "87-91 Abercrombie St （Chippo Hotel）" / "87-91 Abercrombie Street, Chippendale,
  NSW 2008" / "Refunds up to 7 days before event"，日期行显示 "Multiple dates"、全页无任何票价字样。
  Ticketmaster 悉尼站场馆售票页（`/event/1300648FB741630B`）今日抓取被拒（与历史上 Ticketmaster
  事件页 403 的情况一致），故票价仍以 `events.json` 字段 + 021 已完成的档位外部核实为依据。

**排除项摘要**：

- **周杰伦「粉色 墨尔本 嘉年华Ⅱ」（10-17，Marvel Stadium）**——演出日已过 12 天，退出清单。
- **袁娅维 TIA RAY 墨尔本站（08-20）/ 悉尼站（08-22）**——`verified=true` 但演出日已过。
- **AKMU 乐童音乐家 墨尔本站（09-18）/ 悉尼站（09-20）**——演出日均已过，且仍挂 `EXCEPTIONS.md`
  OPEN（墨站 `ticket_platform` 失真、悉站 `venue` 旧名 + `price`/`time` null）。
- **候场喜剧 Loadingzone Comedy（墨尔本，常驻）**——自 09-14 起无法在 Eventbrite 主办方页核实到
  当前场次（OPEN，已逾六周未修），本轮整条不列、**不点名**。它的不可用是本篇第 4、5 条新事实
  （"10 月剩下 2 天清单上没有场次""11 月只有两个落点"）成立的前提，已在核查表第 29/30 条写明。

**主动剔除的 8 项**：

1. **"本周开票"的字面说法**——沿 005 起的既定口径，`status` 字段只说明"在售"，无任何字段支持
   "本周开售"。
2. **开门 / 检票 / 最后入场 / 散场时间**——Sydney Showground 官方页今日**确实**印着
   "6:00pm – Gates open" / "8:30pm - Final Entry" / "10:30pm – Event finishes"，但账号红线明确
   把"检票时间/入场须知"列为不可自行添加项，且本栏目前十篇一律不写，本篇**保持同一口径不写**。
   （这批信息来源可靠、可核实，更适合放进"场馆攻略"位并注明以场馆页为准——已写进值班日志。）
3. **场馆的入场年龄限制 / 禁带物品 / 无障碍安排**——同上，属入场须知，且 064（场馆攻略位）刚写过
   ENGIE 的无障碍，本篇不重复。
4. **二级市场价**——任何转售聚合站自述的价格均非票面价，与"官方票价是唯一标准"口径冲突，不写。
5. **场馆容量 / 顶棚是否露天**——053 已记录来源之间打架，一字不写。
6. **Eventbrite 页面上的活动名「Rolling Donkey 驴打滚每周二中文喜剧开放麦」**——与 JSON
   `title_zh` 不同名，文案一律只用 `title_zh` 的「Rolling Donkey 中文喜剧开放麦」。
7. **Ticketmaster 巡演页的 "Sydney General Public Sale: 12pm on Tuesday 28th April"**——无年份，
   且该页自身标注日期为 2026-03-26，属已过去的开票窗口，不写进任何倒计时（同 059）。
8. **Eventbrite 页上的主办方微信号与"悉尼线下最火喜剧演出"自述**——前者属联系方式、不属演出字段；
   后者是主办方营销自述、无法核实，均不写。

**红线自查**：2 条全部 `verified=true`；日期/时间/场馆/城市/票价/平台/限购逐字取自 JSON 字段；
`price` 为 null 的 Rolling Donkey 不编造票价；开门/检票/散场时间与入场须知一律不写；两条新增的
时间规则均为官方页面今日原文并在文案里标明出处性质（"官方页面上写着"）；正文无外链；未点名任何
个人/账号/转售平台，防诈部分只讲模式。

## 标题（13字）

一场还拿不到票，一场已不能退

## 正文（发帖文案，无外链）

清单今天还是 **2 场**，都在悉尼，跟上周一样。

但我今天把这 2 场的官方页面从头读到尾，发现一件比"有几场"更要紧的事：**它们各自有一个你得记住
的日子，而且都不是演出当天** 👇

**【11.21 这场：票要到 11.07 才会进你账号】**

🌊 **11.21 周六 晚7:30 · 悉尼 ENGIE Stadium（Sydney Olympic Park）**
周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会
$188–$748（另加 $9.90 手续费）· Ticketmaster 官方售票 · 每人最多 6 张 · **还有 23 天**

官方页面上有一句很多人没读到：**票要到演出前两周才会出现在你的账号里**。
11.21 往前两周就是 **11.07**，距今 9 天。这句话有两层意思：

① 你已经买了但账号里看不到条码——**正常**，别慌，也别因为"怎么还没票"去外面找人问。
② 反过来说，**今天谁给你发"票的截图"，官方时间线本身就对不上**。到了 11.07 之后也一样：
票到没到，看的是**你自己账号里有没有条码**，不是对方的截图。

**【每周二这场：想退票的那条线，前天已经过了】**

🎤 **每周二 晚7:30 · 悉尼 Chippo Hotel（87-91 Abercrombie St, Chippendale）**
Rolling Donkey 中文喜剧开放麦 · Eventbrite · 官方不标价

这场的官方退款政策写的是：**演出前 7 天以上可退**。下一场是 **11.03 周二**，往前 7 天是
**10.27**——前天。按这句话的字面，那一场现在已经退不了了（具体以 Eventbrite 页面为准）。
所以这场的正确打法是：**要去就当天去，别留"到时候再退"这个念头。**

顺手两个日历事实：

① **10 月的周二已经用完了。** 2026 年 10 月只有 4 个周二，最后一个是 10.27。
② **这份清单上，10 月剩下的两天（10.30、10.31）一场都没有。** 11 月只有两个落点：每周二，
和 11.21 那一场。

说明一句：清单之外当然还有别的演出，但**没过我这边核实的，我就不往上写**——日期场馆票价错一次
就伤号，这条我不想赌。

官方票面是唯一标准。周杰伦那场是 Ticketmaster 官方、每人最多 6 张；别的入口先问一句。

评论区扣 1，私信发你这 2 场的官方日期、票价区间和这两个关键日子，还有后续开票提醒 🎫

#周杰伦 #悉尼演唱会 #澳洲华人 #演出情报 #中文脱口秀 #悉尼生活

## 卡片文案结构（3张，票根美学）

**P1 封面**（无配图：汇总篇涉及多组演出方，不挂任何海报）
- issue-row: AuShow · 澳华演出雷达
- kicker: 在售清单 · 两个关键日子
- 大字标题: 一场还拿不到票 / 一场已经不能退
- 分隔线
- 副标题: 票 11.07 才进账号 · 退款线 10.27 已过
- lead: 清单还是 2 场。但这 2 场各有一个日子不是演出当天——官方页面上写着，很多人没读到。
- 底部条: 两条都在售 — 2 场 · 都在悉尼

**P2 在售清单（按"官方印着的那个日子"，ledger 2条）**
- kicker: 同一份清单 · 两种时间规则
- 大字: 一个还没到手 / 一个已经过线
- 1. **票 11.07 才进账号** — 11.21 周六 · 19:30 · 悉尼 ENGIE Stadium (Sydney Olympic Park) · 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会 · $188–$748（另加 $9.90 手续费）· Ticketmaster · 每人最多 6 张 · 还有 23 天 · 官方原文：票于演出前两周进账号
- 2. **退款线 10.27 已过** — 每周二 · 19:30 · 悉尼 Chippo Hotel，87-91 Abercrombie St, Chippendale · Rolling Donkey 中文喜剧开放麦 · Eventbrite · 官方未标价 · 下一场 11.03 周二 · 官方原文：演出前 7 天以上可退
- 收尾: 前者今天不该有人"手上有票"；后者今天已经不该指望能退。10 月的周二用完了（最后一个 10.27），清单上 10.30、10.31 没有场次；11 月只有两个落点。
- 底部条: 官方票面是唯一标准 — 别的入口先问一句

**P3 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 票到没到 / 看你自己账号 / 不看截图
- 正文: 评论区扣 1，私信发你这 2 场的官方日期、票价区间和这两个关键日子，还有后续开票提醒。
- 底部条: VOL. 065 — 简介里有完整演出日历

## 事实核查表

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | 演出名「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` → `title_zh`（该条 `verified=true`），逐字复制 |
| 2 | 悉尼站日期 2026-11-21 | GREEN | 同条目 `date`；今日复核 Ticketmaster AU 官方巡演页原文 "November 21, 2026, – ENGIE Stadium, Sydney NSW" https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 ；Sydney Showground 官方场次页原文 "Saturday 21 November" https://www.sydneyshowground.com.au/whats-on/jay-chou-carnival--world-tour/ |
| 3 | 2026-11-21 是周六 | GREEN | 本地 `date` 推导（`python3 datetime`，11-21 weekday=5）；Sydney Showground 官方页原文 "Saturday 21 November"（同 #2 第二个 URL） |
| 4 | 悉尼站开演 19:30 | GREEN | 同条目 `time`；Sydney Showground 官方场次页原文 "7:30pm – Event starts"（同 #2 第二个 URL） |
| 5 | 悉尼站场馆 ENGIE Stadium (Sydney Olympic Park) | GREEN | 同条目 `venue`；Sydney Showground 官方页原文 "ENGIE Stadium" + "ENGIE Stadium, Sydney Showground"（同 #2 第二个 URL）；Ticketmaster 巡演页原文 "ENGIE Stadium, Sydney NSW"（同 #2 第一个 URL） |
| 6 | 悉尼站城市 = 悉尼 | GREEN | 同条目 `city`；Ticketmaster 巡演页原文 "ENGIE Stadium, Sydney NSW"（同 #2 第一个 URL） |
| 7 | 悉尼站票价 $188–$748（另加 $9.90 手续费） | GREEN | 同条目 `price`，逐字复制（档位结构已于 021 外部核实，本篇只用区间端点）。今日巡演页仍不列票价、原文 "For Sydney pricing refer to the venue event page"；该场馆售票页 `/event/1300648FB741630B` 今日抓取被拒（与 Ticketmaster 事件页历史 403 一致），故以 JSON 字段为准（同 #2 第一个 URL） |
| 8 | 悉尼站官方购票平台 Ticketmaster | GREEN | 同条目 `ticket_platform`；Sydney Showground 官方场次页 "Tickets" 入口指向 ticketmaster.com.au（同 #2 第二个 URL）；Ticketmaster 巡演页原文 "Only purchase through Ticketmaster Australia to guarantee you have a valid ticket for entry on event day."（同 #2 第一个 URL） |
| 9 | 悉尼站状态 = 在售 | GREEN | 同条目 `status="on_sale"`；辅证同 #8（场馆官方页购票入口今日仍直指 Ticketmaster AU）。口径说明：沿 059，巡演页的 "On Sale Now!" 只印在已结束的墨尔本站那一栏，不挪用；文案只写"官方售票"，不声称有新开票动作 |
| 10 | 悉尼站每账户限购 6 张 | GREEN | 同条目 `notes`；Ticketmaster AU 官方巡演页原文 "You may purchase a maximum of 6 tickets per person."（同 #2 第一个 URL） |
| 11 | 悉尼站距今还有 23 天 | GREEN | 本地 `date` 计算（2026-11-21 − 2026-10-29 = 23） |
| 12 | 悉尼站的票要到演出前两周才会出现在购票人账号里 | GREEN | Ticketmaster AU 官方巡演页 "How will I get my tickets for Jay Chou?" 段今日原文 "Please Note – Tickets will become available in your account 2 weeks prior to the event date."（同 #2 第一个 URL）。该页为本次巡演官方指引页（页面标注日期 2026-03-26、最后修改 2026-04-17，今日仍在线）；文案明确标注这是"官方页面上写着"的规则，不作任何延伸承诺 |
| 13 | 演出前两周 = 2026-11-07 | GREEN | 本地 `date` 计算（2026-11-21 − 14 天 = 2026-11-07），依据为 #12 的官方原文 "2 weeks prior to the event date" |
| 14 | 11-07 距今 9 天 | GREEN | 本地 `date` 计算（2026-11-07 − 2026-10-29 = 9） |
| 15 | 票到没到以购票人自己账号里的条码为准 | GREEN | Ticketmaster AU 官方转票指引原文 "Once you see 'Transfer Complete' the barcode will be available in your Ticketmaster account" https://discover.ticketmaster.com.au/guide-to/ticket-forward-how-to-14657 （024 第 15 条已核实同一出处）；并与 #12 的交付时点规则相互印证。文案只复述"看自己账号不看截图"这一既有规则，不新增机制描述 |
| 16 | 演出名「Rolling Donkey 中文喜剧开放麦」 | GREEN | `data/events.json` → `title_zh`（`verified=true`），逐字复制 |
| 17 | Rolling Donkey 每周二 | GREEN | 同条目 `recurrence="每周二"`；今日复核 Eventbrite 售票页原文 "每周二 晚7:30" / "Every Tuesday, 7:30 PM" https://www.eventbrite.com/e/copy-of-rolling-donkey-tickets-1983189907399 |
| 18 | Rolling Donkey 开演 19:30 | GREEN | 同条目 `time`；同 #17 Eventbrite 页原文 "晚7:30" / "7:30 PM" |
| 19 | Rolling Donkey 没有单一演出日期（`date` 为 null） | GREEN | 同条目 `date=null`；Eventbrite 售票页日期行今日显示 "Multiple dates"，不列任何具体单场日期（同 #17 URL） |
| 20 | Rolling Donkey 场馆 Chippo Hotel，87-91 Abercrombie St, Chippendale | GREEN | 同条目 `venue`，逐字复制；Eventbrite 页原文 "87-91 Abercrombie St （Chippo Hotel）" + "87-91 Abercrombie Street, Chippendale, NSW 2008"（同 #17 URL） |
| 21 | Rolling Donkey 城市 = 悉尼 | GREEN | 同条目 `city`；Eventbrite 页地址栏 "Chippendale, NSW 2008"（同 #17 URL） |
| 22 | Rolling Donkey 官方不标价 | GREEN | 同条目 `price=null`；Eventbrite 售票页今日全页无任何票价或"免费"字样（同 #17 URL） |
| 23 | Rolling Donkey 购票平台 Eventbrite | GREEN | 同条目 `ticket_platform`，逐字复制；#17 的 URL 本身即该条目 `ticket_url` 指向的 Eventbrite 售票页 |
| 24 | Rolling Donkey 官方退款政策为"演出前 7 天以上可退" | GREEN | Eventbrite 售票页 "Good to know → Refund Policy" 段今日原文 "Refunds up to 7 days before event"（同 #17 URL）；文案标明这是官方页面上的政策原文 |
| 25 | 下一场 Rolling Donkey 是 2026-11-03 周二 | GREEN | 本地 `date` 计算（2026-10-29 为周四，其后首个周二 = 2026-11-03）+ `recurrence="每周二"`（经 #17 外部复核） |
| 26 | 11-03 往前 7 天 = 2026-10-27 | GREEN | 本地 `date` 计算（2026-11-03 − 7 天 = 2026-10-27），依据为 #24 的官方原文 |
| 27 | 按 #24 字面，11-03 那场的可退窗口已于 10-27 关闭（今天 10-29 已过线 2 天） | AMBER | 推导自 #24 + #26（本地 `date` 计算：2026-10-29 − 2026-10-27 = 2 天）。**降为 AMBER 的理由**：Eventbrite 该页只给 "Refunds up to 7 days before event" 一句，未定义截止时点/时区/是否含当日，故这是**按字面的推导**而非平台明示结论；文案已写明"按这句话的字面"并加"具体以 Eventbrite 页面为准"，不作绝对断言 |
| 28 | 2026 年 10 月只有 4 个周二，最后一个是 10-27 | GREEN | 本地 `date` 枚举（2026-10-06 / 10-13 / 10-20 / 10-27，`python3 datetime` weekday=1） |
| 29 | 这份清单上 10-30、10-31 没有任何场次 | GREEN | 推导自 `events.json`：`verified=true` 且 `date` 晚于今日的条目仅 11-21 一条；唯一的重复型条目 Rolling Donkey 下一场为 11-03（#25）。另一条同为重复型的 Loadingzone（墨尔本常驻）自 09-14 起挂 `EXCEPTIONS.md` OPEN、无法核实当前场次，整条不计入——文案同时明示"清单之外还有别的演出，未核实的不写"，不声称全澳无演出（见 #31） |
| 30 | 11 月这份清单上只有两个落点（每周二 + 11-21） | GREEN | 同 #29 的枚举结果：`verified=true` 条目中 11 月内有效者为 Rolling Donkey（每周二）与周杰伦悉尼站（11-21）两条 |
| 31 | 本号只写核实过的演出，清单之外的不写 | GREEN | 账号档案 `~/.claude/skills/xhs-content/accounts/aushow.md` 红线原文："演出信息必须与 data/events.json 中 verified=true 的条目一致，未核实的不发"；`events.json` 现有 160 条、`verified=true` 仅 8 条，可见清单窄于市场是口径所致 |
| 32 | 清单仍是 2 场，且两条都在悉尼 | GREEN | 两条目 `city` 字段均为"悉尼"；条目数由 `verified=true` 池（今日程序化枚举：共 8 条）扣除演出日已过的 5 条（周杰伦墨站 10-17、袁娅维 08-20/08-22、AKMU 09-18/09-20）与挂 OPEN 的 Loadingzone 后得出：8 − 5 − 1 = 2 |
| 33 | 本栏目连续第二期只有 2 条、连续第二期单城 | GREEN | 枚举 `content/` 内本栏目各篇写明的"共选 N 场"：005=5 / 009=4 / 014=4 / 021=4 / 028=3 / 035=3 / 041=3 / 048=3 / 053=3 / 059=2 / 本篇=2；059 文件内已写明"本栏目第一次只有一座城市"，本篇两条 `city` 同为悉尼（#32），故为连续第二期 |
| 34 | 两条 `status` 均为在售 | GREEN | 两条目 `status="on_sale"`；悉尼站辅证见 #9，Rolling Donkey 的 Eventbrite 售票页今日仍在线可访问且带 "Get tickets" 入口（同 #17 URL） |
| 35 | 两条的官方购票平台不同（Ticketmaster / Eventbrite） | GREEN | 两条目 `ticket_platform` 字段（并分别经 #8 / #23 外部复核） |

**剔除项未进文案**（不计入核查表，仅记录）：Sydney Showground 官方页今日印着的 "6:00pm – Gates
open" / "8:30pm - Final Entry" / "10:30pm – Event finishes" 与入场年龄、禁带物品、无障碍安排
（属入场须知，账号红线列为不可自行添加项，本栏目前十篇一律不写，口径保持一致）、二级市场价、
场馆容量与顶棚状况（053 已记录来源打架）、Eventbrite 页上的活动名「驴打滚…」（与 `title_zh`
不同名）、主办方微信号与"悉尼线下最火喜剧演出"自述（联系方式 / 无法核实的营销自述）、
Ticketmaster 巡演页旧开票窗口 "12pm on Tuesday 28th April"（无年份、页面自身日期为 2026-03-26）、
Eventbrite 页面 metadata 里的 `event:end_time`（2026-12-08，属页面元数据而非正文明示场次，不采信）。

FACT-AUDIT-STATUS: RED=0 CHECKED=35 SOURCES-CITED=35

## 渲染状态

- 模板: `cards/065/index.html`（复制自 `cards/053/index.html`——本栏目最近一份真正建成并渲染过的
  3 卡汇总模板；`cards/059/` 从未建成，见 `EXCEPTIONS.md` 2026-10-23 条。保留
  `data-theme="aushow"` 主题色 token 与 `.ticket`/`.ledger`/`issue-strip` 组件样式，仅替换 3 个
  `<section class="poster xhs">` 区块内的文案。**注意**：`cards/` 下各期目录里都没有 `assets/`，
  index.html 末尾那句 `assets/magazine-bg-webgl.js` 自 001 起一直 404、`mag-bg` canvas 留空，
  053 的 3 张 PNG 就是在这个状态下渲染出来的，属已验证的既有状态，本期不改）
- 张数: 3 张（封面 / 按"官方印着的那个日子" 2 行 ledger / CTA）——本期只有 2 场，ledger 两行，不凑空卡
- 渲染: 交由 `automation/render_card.py`（headless Chrome 逐张单独截图），本次会话不调用任何截图工具
