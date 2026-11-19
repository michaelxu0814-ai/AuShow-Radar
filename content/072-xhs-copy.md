# 072 — 还有两天，票该在你账号里（本周开票汇总）

**选题类型**：本周开票汇总（周四轮换位，2026-11-19 生成）

**信源条目**（全部 `data/events.json` → `verified=true`，共选 2 场）：
1. 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会（2026-11-21 周六 19:30，ENGIE Stadium (Sydney Olympic Park)，Ticketmaster）
2. Rolling Donkey 中文喜剧开放麦（悉尼，每周二 19:30，Chippo Hotel，Eventbrite）

**本篇口径决定（先说清楚）**：

- **沿用 005/009/014/021/028/035/041/048/053/059/065 的"不说'本周开票'"口径。** 2 条 `status`
  都是 `on_sale`（已在售），`events.json` 里没有任何字段支持"这些票是本周开售的"。栏目定位保留
  （仍记为"本周开票汇总"），标题/卡面一律用"在售""官方票面"这类可核实的表述。

- **角度是第 12 种切分：上一期那条官方规则，今天状态翻面了。**
  005=时间线、009=提前量、014=城市、021=票价档位、028=倒计时、035=官方购票平台、041=档期月份、
  048=`time`+星期几、053=`venue`、059=`date`/`recurrence` 对立、065=官方页面上印着的非演出日。
  **本篇不另找新维度，而是把 065 的那条规则推到它的另一端**——这是本栏目第一次出现"同一条官方
  原文、两期之间状态相反"：
  - 065（10-29）写的是：官方原文 **"Tickets will become available in your account 2 weeks prior
    to the event date."** → 11-21 减两周 = **11-07**，当时**还有 9 天**，所以那期的结论是
    "这场的票还没到任何人手上，谁给你发截图都对不上"。
  - 本篇（11-19）：**11-07 已经过去 12 天**。同一句官方原文，今天的结论正好反过来——
    **票现在就该已经在你自己的 Ticketmaster 账号里了。** 于是防诈判据也从"谁有票都可疑"变成
    **"你自己打开 app 看一眼就能定案"**，这是本栏目 11 期里第一次能给出这种"自查即可结案"的动作。
  - 与 028（倒计时期）的区别：028 切的是"还有几天"这个数字本身；本篇切的是**交付状态**
    （票在不在账号里），倒计时只是触发条件。

- **本篇的新事实有六条**：
  1. **11-07 的交付线已过去 12 天**，按官方那句话，已购票的人现在账号里应当能看到票（#15）。
  2. **只剩 2 天**——本栏目写这场写过的最短倒计时（065 时是 23 天）。
  3. **官方原文：票是数字票，通过 Ticketmaster app 或手机浏览器访问**（前 11 期未用过，#16）。
  4. **官方原文：要有 Ticketmaster 账号才能取到这场的票**（前 11 期未用过，#17）。
  5. **11-24 是 2026 年 11 月最后一个周二**（11 月的周二只有 11-03 / 11-10 / 11-17 / 11-24，#28）。
  6. **后天演完之后，11 月剩下的 9 天（11-22→11-30）这份清单上只有 11-24 一个落点**（#36）。

- **清单规模**：仍是 2 场、仍然都在悉尼——本栏目**连续第三期**只有 2 条，也是**连续第三期单城**。

- **票价口径有一处变化，必须写明**：Rolling Donkey 在 `events.json` 里 `price=null`，065（10-29）
  复核时 Eventbrite 页面**全页无任何票价字样**，故 065 写的是"官方不标价"。**本次复核发现该页底部
  今日已显示 "From A$6"**。因此：
  - 本篇**不再写"官方不标价"**——那句话今天已经不成立，照抄就是错；
  - 本篇也**不写 "$6" 这个数字**——`events.json` 该字段仍是 null，红线要求演出信息与 JSON 条目
    一致、不自行添字段；
  - 文案只写"票价以官方 Eventbrite 页面为准"，这句话两边都站得住。
  - 该字段漂移已记入 `EXCEPTIONS.md`，请用户更新 `events.json` 的 `price` 字段（#31）。

- **今日外部复核**（两场逐条过了一手源）：
  Ticketmaster AU 官方巡演页今日原文 "November 21, 2026, – ENGIE Stadium, Sydney NSW" /
  "You may purchase a maximum of **6** tickets per person." / "Only purchase through
  **Ticketmaster Australia** to guarantee you have a valid ticket for entry on event day." /
  "Please Note – Tickets will become available in your account 2 weeks prior to the event date." /
  "All tickets purchased through Ticketmaster Australia are digital, meaning you can easily access
  your tickets on your phone via the Ticketmaster app or mobile web browser" / "Ticketholders need
  a Ticketmasteraccount to access **Jay Chou** tickets."，该页仍不列票价、明文指向场馆售票页
  （与 009/021/048/053/059/065 一致）；Sydney Showground 官方场次页今日原文 "Saturday 21 November" /
  "ENGIE Stadium" / "7:30pm – Event starts"，"Tickets" 入口指向 ticketmaster.com.au；
  Eventbrite 售票页今日原文 "每周二 晚7:30"（"Every Tuesday, 7:30 PM"）/ "87-91 Abercrombie St
  （Chippo Hotel）" / "87-91 Abercrombie Street, Chippendale, NSW 2008" / "Refunds up to 7 days
  before event" / 日期行 "Multiple dates" / 底部 "From A$6"。
  Ticketmaster 悉尼站场馆售票页（`/event/1300648FB741630B`）今日抓取**全部引擎失败**（与历史上
  Ticketmaster 事件页被拒的情况一致），故票价仍以 `events.json` 字段 + 021 已完成的档位外部核实
  为依据。

**排除项摘要**：

- **周杰伦「粉色 墨尔本 嘉年华Ⅱ」（10-17，Marvel Stadium）**——演出日已过 33 天，退出清单。
- **袁娅维 TIA RAY 墨尔本站（08-20）/ 悉尼站（08-22）**——`verified=true` 但演出日已过。
- **AKMU 乐童音乐家 墨尔本站（09-18）/ 悉尼站（09-20）**——演出日均已过，且仍挂 `EXCEPTIONS.md`
  OPEN（墨站 `ticket_platform` 失真、悉站 `venue` 旧名 + `price`/`time` null）。
- **候场喜剧 Loadingzone Comedy（墨尔本，常驻）**——**本次排除理由与 065 不同，必须记清楚**：
  该主办方 Eventbrite 页今日**可以访问、而且有多场在售场次**（09-14 起"页面无法核实场次"那条
  OPEN 已不再是当前状态）。但今日页面上的场次**没有一场落在 `events.json` 记的字段上**——JSON 记
  `venue="Club Voltaire, 1st Floor/14 Raglan St, North Melbourne"`、`time="19:00"`，今日在售场次
  分别在 Eno Cafe / Library at The Dock / SOAZ 22 / Fringe Common Rooms，时间为 19:30 或 19:00 以外
  的时段。**即"场次有，但 JSON 里那条常驻信息已失真"**，照 JSON 写就会写错场馆和时间，照页面写就
  超出 `verified` 字段范围，两头都不合红线，故本轮整条不列、**不点名**（#35）。
  ⚠️ 这条的 `EXCEPTIONS.md` 条目需要改写：旧表述"无法核实到当前场次"已过期，真实问题是**字段漂移**。

**主动剔除的 8 项**：

1. **"本周开票"的字面说法**——沿 005 起的既定口径，`status` 字段只说明"在售"，无任何字段支持
   "本周开售"。
2. **Rolling Donkey 的 "From A$6"**——见上文票价口径，`events.json` 该字段为 null，不写数字。
3. **开门 / 检票 / 最后入场 / 散场时间**——Sydney Showground 官方页今日**确实**印着
   "6:00pm – Gates open" / "8:30pm - Final Entry" / "10:30pm – Event finishes"，但账号红线明确把
   "检票时间/入场须知"列为不可自行添加项，本栏目前十一篇一律不写，本篇**保持同一口径不写**。
   （倒计时只剩 2 天、这批信息又确实来自场馆官方页，适合放进"场馆攻略"位并注明以场馆页为准——
   已写进值班日志，与 065 同一建议。）
4. **年龄限制 / 禁带物品 / 无障碍安排 / 禁止露营 / 场馆无现金**——Showground 页今日都印着，同属
   入场须知，一律不写（064 场馆攻略位已写过 ENGIE 无障碍，不重复）。
5. **二级市场价**——任何转售聚合站自述的价格均非票面价，与"官方票价是唯一标准"口径冲突，不写。
6. **Eventbrite 页面上的活动名「Rolling Donkey 驴打滚每周二中文喜剧开放麦」**——与 JSON
   `title_zh` 不同名，文案一律只用 `title_zh` 的「Rolling Donkey 中文喜剧开放麦」。
7. **Ticketmaster 巡演页的 "Sydney General Public Sale: 12pm on Tuesday 28th April"**——无年份，
   且该页自身标注日期为 2026-03-26，属已过去的开票窗口，不写进任何倒计时（同 059/065）。
8. **Eventbrite 页 metadata 里的 `event:start_time`（2026-02-24）与 `event:end_time`（2026-12-08）、
   主办方微信号、"悉尼线下最火喜剧演出"自述、"under 14 with parent or legal guardian"**——分别属
   页面元数据（与正文"Multiple dates"矛盾，不采信）、联系方式、无法核实的营销自述、入场须知，均不写。

**红线自查**：2 条全部 `verified=true`；日期/时间/场馆/城市/票价/平台/限购逐字取自 JSON 字段；
`price` 为 null 的 Rolling Donkey 既不编票价、也不再沿用已失效的"官方不标价"说法；开门/检票/散场
时间与入场须知一律不写；三条新增官方原文（数字票/需账号/两周进账号）均为官方页面今日原文并在文案里
标明出处性质（"官方页面上写着"）；正文无外链；未点名任何个人/账号/转售平台，防诈部分只讲模式。

## 标题（12字）

还有两天，票该在你账号里

## 正文（发帖文案，无外链）

清单今天还是 **2 场**，都在悉尼。但这期有件事跟上期**正好相反**，必须单独说 👇

**【11.21 这场：后天开演，票现在就该在你账号里了】**

🌊 **11.21 周六 晚7:30 · 悉尼 ENGIE Stadium（Sydney Olympic Park）**
周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会
$188–$748（另加 $9.90 手续费）· Ticketmaster 官方售票 · 每人最多 6 张 · **还有 2 天**

上期我写过官方页面上那句很多人没读到的话：**票要到演出前两周才会出现在你的账号里**。
11.21 往前两周是 **11.07**——**那天已经过去 12 天了。**

所以同一句话，今天的意思彻底翻过来了：

① **你已经买了的话，票现在就该在你账号里。** 官方页面还写着两件事：这场的票**是数字票**，
用 Ticketmaster app 或手机浏览器打开；而且**得有 Ticketmaster 账号才能取到票**。
现在就去 app 里看一眼条码在不在——别等到周六下午在场馆门口才第一次打开。

② **万一账号里是空的，这两天正是该去官方渠道问清楚的时候，不是去外面找人买票的时候。**
开演前 48 小时是最容易出事的窗口：时间紧、人慌、对方催你"马上转账不然就卖别人了"。
记住一句话——**票在不在，看的是你自己账号里有没有条码，不是任何人的截图。**
截图能做，条码进不了你的账号。

**【每周二这场：11 月最后一次】**

🎤 **每周二 晚7:30 · 悉尼 Chippo Hotel（87-91 Abercrombie St, Chippendale）**
Rolling Donkey 中文喜剧开放麦 · Eventbrite 官方售票 · 票价以官方页面为准

下一场是 **11.24 周二**，还有 5 天——**这是 2026 年 11 月最后一个周二**（这个月只有
11.03、11.10、11.17、11.24 四个）。另外这场的官方退款政策写的是"演出前 7 天以上可退"，
按字面，11.24 那场的退款线 11.17 已经过了（具体以 Eventbrite 页面为准），所以想去就直接定。

顺手一个日历事实：**后天那场演完之后，11 月剩下的 9 天里，这份清单上只剩 11.24 一个落点。**

说明一句：清单之外当然还有别的演出，但**没过我这边核实的，我就不往上写**——日期场馆票价错一次
就伤号，这条我不想赌。

官方票面是唯一标准。周杰伦那场是 Ticketmaster 官方、每人最多 6 张；别的入口先问一句。

评论区扣 1，私信发你这 2 场的官方日期、票价区间和"票到没到怎么自查"，还有后续开票提醒 🎫

#周杰伦 #悉尼演唱会 #澳洲华人 #演出情报 #中文脱口秀 #悉尼生活

## 卡片文案结构（3张，票根美学）

**P1 封面**（无配图：汇总篇涉及多组演出方，不挂任何海报）
- issue-row: AuShow · 澳华演出雷达
- kicker: 在售清单 · 倒计时 2 天
- 大字标题: 还有两天 / 票该在你账号里
- 分隔线
- 副标题: 交付线 11.07 已过 12 天 · 现在能自查
- lead: 上期这条官方规则说的是"票还没到任何人手上"。今天同一句话，结论正好反过来。
- 底部条: 两条都在售 — 2 场 · 都在悉尼

**P2 在售清单（按"现在该做的那个动作"，ledger 2条）**
- kicker: 同一份清单 · 两个动作
- 大字: 一个现在去查 / 一个现在就定
- 1. **现在打开 app 查条码** — 11.21 周六 · 19:30 · 悉尼 ENGIE Stadium (Sydney Olympic Park) · 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会 · $188–$748（另加 $9.90 手续费）· Ticketmaster · 每人最多 6 张 · 还有 2 天 · 官方原文：票于演出前两周进账号（11.07，已过 12 天）；票为数字票，经 app 或手机浏览器访问，需 Ticketmaster 账号
- 2. **想去就直接定** — 每周二 · 19:30 · 悉尼 Chippo Hotel，87-91 Abercrombie St, Chippendale · Rolling Donkey 中文喜剧开放麦 · Eventbrite · 票价以官方页面为准 · 下一场 11.24 周二（11 月最后一个周二）· 官方原文：演出前 7 天以上可退
- 收尾: 后天那场演完，11 月剩下的 9 天里这份清单只剩 11.24 一个落点。开演前 48 小时最容易出事——票在不在，看你自己账号里的条码。
- 底部条: 官方票面是唯一标准 — 别的入口先问一句

**P3 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 截图能做 / 条码进不了 / 你的账号
- 正文: 评论区扣 1，私信发你这 2 场的官方日期、票价区间和"票到没到怎么自查"，还有后续开票提醒。
- 底部条: VOL. 072 — 简介里有完整演出日历

## 事实核查表

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | 演出名「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` → `title_zh`（该条 `verified=true`），逐字复制 |
| 2 | 悉尼站日期 2026-11-21 | GREEN | 同条目 `date`；今日复核 Ticketmaster AU 官方巡演页原文 "November 21, 2026, – ENGIE Stadium, Sydney NSW" https://discover.ticketmaster.com.au/music/jay-chou-carnival-ii-world-tour-in-australia-21666 ；Sydney Showground 官方场次页原文 "Saturday 21 November" https://www.sydneyshowground.com.au/whats-on/jay-chou-carnival--world-tour/ |
| 3 | 2026-11-21 是周六 | GREEN | 本地 `date` 推导（`python3 datetime`，11-21 weekday=5）；Sydney Showground 官方页原文 "Saturday 21 November"（同 #2 第二个 URL） |
| 4 | 悉尼站开演 19:30 | GREEN | 同条目 `time`；Sydney Showground 官方场次页原文 "7:30pm – Event starts"（同 #2 第二个 URL） |
| 5 | 悉尼站场馆 ENGIE Stadium (Sydney Olympic Park) | GREEN | 同条目 `venue`；Sydney Showground 官方页原文 "ENGIE Stadium"（页面 Where 段）（同 #2 第二个 URL）；Ticketmaster 巡演页原文 "ENGIE Stadium, Sydney NSW"（同 #2 第一个 URL） |
| 6 | 悉尼站城市 = 悉尼 | GREEN | 同条目 `city`；Ticketmaster 巡演页原文 "ENGIE Stadium, Sydney NSW"（同 #2 第一个 URL） |
| 7 | 悉尼站票价 $188–$748（另加 $9.90 手续费） | GREEN | 同条目 `price`，逐字复制（档位结构已于 021 外部核实，本篇只用区间端点）。今日巡演页仍不列票价、原文 "For Sydney pricing refer to the venue event page"；该场馆售票页 `/event/1300648FB741630B` 今日抓取全部引擎失败（与 Ticketmaster 事件页历史被拒一致），故以 JSON 字段为准（同 #2 第一个 URL） |
| 8 | 悉尼站官方购票平台 Ticketmaster | GREEN | 同条目 `ticket_platform`；Sydney Showground 官方场次页 "Tickets" 入口指向 ticketmaster.com.au（同 #2 第二个 URL）；Ticketmaster 巡演页原文 "Only purchase through Ticketmaster Australia to guarantee you have a valid ticket for entry on event day."（同 #2 第一个 URL） |
| 9 | 悉尼站状态 = 在售 | GREEN | 同条目 `status="on_sale"`；辅证同 #8（场馆官方页购票入口今日仍直指 ticketmaster.com.au）。口径说明：沿 059/065，巡演页的 "On Sale Now!" 只印在已结束的墨尔本站那一栏，不挪用；文案只写"官方售票"，不声称有新开票动作 |
| 10 | 悉尼站每账户限购 6 张 | GREEN | 同条目 `notes`；Ticketmaster AU 官方巡演页原文 "You may purchase a maximum of 6 tickets per person."（同 #2 第一个 URL） |
| 11 | 悉尼站距今还有 2 天 | GREEN | 本地 `date` 计算（2026-11-21 − 2026-11-19 = 2） |
| 12 | 官方规则：这场的票于演出前两周进购票人账号 | GREEN | Ticketmaster AU 官方巡演页 "How will I get my tickets for Jay Chou?" 段今日原文 "Please Note – Tickets will become available in your account 2 weeks prior to the event date."（同 #2 第一个 URL）。该页为本次巡演官方指引页（页面标注日期 2026-03-26、最后修改 2026-04-17，今日仍在线）；文案明确标注这是"官方页面上写着"的规则 |
| 13 | 演出前两周 = 2026-11-07 | GREEN | 本地 `date` 计算（2026-11-21 − 14 天 = 2026-11-07），依据为 #12 的官方原文 |
| 14 | 11-07 距今已过去 12 天 | GREEN | 本地 `date` 计算（2026-11-19 − 2026-11-07 = 12） |
| 15 | 按 #12 的字面，已购票者现在账号里应当已能看到票 | AMBER | 推导自 #12 + #14。**降为 AMBER 的理由**：官方原文只承诺"演出前两周起可在账号中取得"，未承诺任何具体账号在某一时点的状态（个别订单仍可能有平台侧延迟）。文案写法已做相应限制——写"就该在你账号里了"并紧接"万一账号里是空的，这两天正是该去官方渠道问清楚的时候"，把空账号明确列为需向官方核实的情形，不断言人人都已收到 |
| 16 | 这场的票是数字票，通过 Ticketmaster app 或手机浏览器访问 | GREEN | Ticketmaster AU 官方巡演页今日原文 "All tickets purchased through Ticketmaster Australia are digital, meaning you can easily access your tickets on your phone via the Ticketmaster app or mobile web browser via ticketmaster.com.au."（同 #2 第一个 URL）；本栏目前 11 期未引用过该句 |
| 17 | 需要 Ticketmaster 账号才能取到这场的票 | GREEN | 同页今日原文 "Ticketholders need a Ticketmasteraccount to access Jay Chou tickets."（原文此处 "Ticketmaster" 与 "account" 间缺空格，系该页排版，含义不受影响）（同 #2 第一个 URL）；本栏目前 11 期未引用过该句 |
| 18 | 票到没到以购票人自己账号里的条码为准，不以他人截图为准 | GREEN | 直接推导自 #16 + #17 两条今日官方原文（票为数字票、须经本人 Ticketmaster 账号访问，截图不构成入场凭证）；另与 024/065 已核实的官方转票指引原文 "Once you see 'Transfer Complete' the barcode will be available in your Ticketmaster account" https://discover.ticketmaster.com.au/guide-to/ticket-forward-how-to-14657 一致（该指引链接今日仍挂在 #2 第一个 URL 页内）。文案只复述这一既有规则，不新增机制描述 |
| 19 | 演出名「Rolling Donkey 中文喜剧开放麦」 | GREEN | `data/events.json` → `title_zh`（`verified=true`），逐字复制 |
| 20 | Rolling Donkey 每周二 | GREEN | 同条目 `recurrence="每周二"`；今日复核 Eventbrite 售票页原文 "每周二 晚7:30" / "Every Tuesday, 7:30 PM" https://www.eventbrite.com/e/copy-of-rolling-donkey-tickets-1983189907399 |
| 21 | Rolling Donkey 开演 19:30 | GREEN | 同条目 `time`；同 #20 Eventbrite 页原文 "晚7:30" / "7:30 PM" |
| 22 | Rolling Donkey 没有单一演出日期（`date` 为 null） | GREEN | 同条目 `date=null`；Eventbrite 售票页日期行今日显示 "Multiple dates"，不列任何具体单场日期（同 #20 URL） |
| 23 | Rolling Donkey 场馆 Chippo Hotel，87-91 Abercrombie St, Chippendale | GREEN | 同条目 `venue`，逐字复制；Eventbrite 页原文 "87-91 Abercrombie St （Chippo Hotel）" + "87-91 Abercrombie Street, Chippendale, NSW 2008"（同 #20 URL） |
| 24 | Rolling Donkey 城市 = 悉尼 | GREEN | 同条目 `city`；Eventbrite 页地址栏 "Chippendale, NSW 2008"（同 #20 URL） |
| 25 | Rolling Donkey 购票平台 Eventbrite | GREEN | 同条目 `ticket_platform`，逐字复制；#20 的 URL 本身即该条目 `ticket_url` 指向的 Eventbrite 售票页 |
| 26 | Rolling Donkey 状态 = 在售 | GREEN | 同条目 `status="on_sale"`；Eventbrite 售票页今日仍在线可访问、底部带 "Check availability" 入口（同 #20 URL） |
| 27 | 下一场 Rolling Donkey 是 2026-11-24 周二，距今 5 天 | GREEN | 本地 `date` 计算（2026-11-19 为周四，其后首个周二 = 2026-11-24，差 5 天）+ `recurrence="每周二"`（经 #20 外部复核） |
| 28 | 11-24 是 2026 年 11 月最后一个周二，该月共 4 个周二（11-03/11-10/11-17/11-24） | GREEN | 本地 `date` 枚举（`python3 datetime`，2026 年 11 月内 weekday=1 者为 11-03、11-10、11-17、11-24，11-24 之后该月无周二） |
| 29 | Rolling Donkey 官方退款政策为"演出前 7 天以上可退" | GREEN | Eventbrite 售票页 "Good to know → Refund Policy" 段今日原文 "Refunds up to 7 days before event"（同 #20 URL）；文案标明这是官方页面上的政策原文 |
| 30 | 按 #29 字面，11-24 那场的可退窗口已于 11-17 关闭 | AMBER | 推导自 #29 + 本地 `date` 计算（2026-11-24 − 7 天 = 2026-11-17，距今 2 天前）。**降为 AMBER 的理由（同 065 #27）**：Eventbrite 该页只给 "Refunds up to 7 days before event" 一句，未定义截止时点/时区/是否含当日，故这是**按字面的推导**而非平台明示结论；文案已写明"按字面"并加"具体以 Eventbrite 页面为准" |
| 31 | 本篇不写 Rolling Donkey 的票价数字，也不再写"官方不标价" | AMBER | `events.json` 该条 `price=null`；但今日 Eventbrite 售票页底部已显示 "From A$6"（同 #20 URL），与 065（10-29）复核时"全页无票价字样"的状态不同。**两边取交集的处理**：不写数字（JSON 无此字段，红线禁止自行添字段），也不沿用 065 的"官方不标价"（今日已不成立），文案只写"票价以官方页面为准"。判 AMBER 是因为 JSON 与一手源现已不一致，**字段漂移已记入 `EXCEPTIONS.md` 待用户更新 `events.json`** |
| 32 | 本期清单共 2 场，且两条都在悉尼 | GREEN | 两条目 `city` 字段均为"悉尼"；条目数由 `verified=true` 池（今日程序化枚举：共 8 条，总条目 171）扣除演出日已过的 5 条（周杰伦墨站 10-17、袁娅维 08-20/08-22、AKMU 09-18/09-20）与因字段漂移排除的 Loadingzone 后得出：8 − 5 − 1 = 2 |
| 33 | 本栏目连续第三期只有 2 条、连续第三期单城 | GREEN | 枚举 `content/` 内本栏目各篇写明的"共选 N 场"：005=5 / 009=4 / 014=4 / 021=4 / 028=3 / 035=3 / 041=3 / 048=3 / 053=3 / 059=2 / 065=2 / 本篇=2；059 文件内写明"本栏目第一次只有一座城市"、065 文件内写明"连续第二期单城"，本篇两条 `city` 同为悉尼（#32），故为连续第三期 |
| 34 | 本期两条的官方购票平台不同（Ticketmaster / Eventbrite） | GREEN | 两条目 `ticket_platform` 字段（并分别经 #8 / #25 外部复核） |
| 35 | Loadingzone 本轮排除的理由是字段漂移，而非"页面无法核实" | GREEN | 今日复核主办方页 https://www.eventbrite.com/o/loadingzone-comedy-75417874333 可访问（HTTP 200）且列有多场在售场次（11-19 Box Hill 开放麦 @ Eno Cafe 7:30 PM、11-20 Rachel47 专场 @ Library at The Dock 7:30 PM、11-28 抓马大会 @ SOAZ 22 7:00 PM、12-05 三周年 @ Fringe Common Rooms 7:30 PM 等），但无一场落在该条目 JSON 字段 `venue="Club Voltaire, 1st Floor/14 Raglan St, North Melbourne"` / `time="19:00"` 上，故照 JSON 写会写错场馆与时间、照页面写会超出 `verified` 字段范围，两头均违红线，本轮整条不列且不点名 |
| 36 | 后天（11-21）那场演完后，11 月剩下的 9 天（11-22→11-30）这份清单上只有 11-24 一个落点 | GREEN | 推导自 `events.json` 枚举：`verified=true` 且演出日晚于今日的条目仅 11-21 一条（#32）；唯一仍有效的重复型条目 Rolling Donkey 下一场为 11-24（#27），其后该月无周二（#28）；Loadingzone 整条按 #35 不计入。本地 `date` 枚举 11-22→11-30 共 9 天。文案同时明示"清单之外还有别的演出，未核实的不写"，不声称全澳无演出（见 #37） |
| 37 | 本号只写核实过的演出，清单之外的不写 | GREEN | 账号档案 `~/.claude/skills/xhs-content/accounts/aushow.md` 红线原文："演出信息必须与 data/events.json 中 verified=true 的条目一致，未核实的不发"；`events.json` 现有 171 条、`verified=true` 仅 8 条，可见清单窄于市场是口径所致 |
| 38 | 周杰伦墨尔本站演出日已过 33 天 | GREEN | 该条目 `date="2026-10-17"` + 本地 `date` 计算（2026-11-19 − 2026-10-17 = 33） |

**剔除项未进文案**（不计入核查表，仅记录）：Sydney Showground 官方页今日印着的
"6:00pm – Gates open" / "8:30pm - Final Entry" / "10:30pm – Event finishes"、
"Children under 6 years old are not permitted at this event."、"ENGIE Stadium is a CASHLESS venue"、
禁带物品（unofficial light sticks / selfie sticks / signs larger than A3）、禁止露营、无障碍与
Quiet Room 安排（均属入场须知，账号红线列为不可自行添加项，本栏目前十一篇一律不写，口径保持一致）、
二级市场价、场馆容量与顶棚状况（053 已记录来源打架）、Eventbrite 页上的活动名「驴打滚…」（与
`title_zh` 不同名）、"From A$6"（见 #31）、主办方微信号与"悉尼线下最火喜剧演出"自述（联系方式 /
无法核实的营销自述）、"under 14 with parent or legal guardian"（入场须知）、Ticketmaster 巡演页旧
开票窗口 "12pm on Tuesday 28th April"（无年份、页面自身日期为 2026-03-26）、Eventbrite 页 metadata
里的 `event:start_time`（2026-02-24）与 `event:end_time`（2026-12-08，属页面元数据且与正文
"Multiple dates" 矛盾，不采信）、Loadingzone 今日页面上的全部具体场次（见 #35，整条不点名）。

FACT-AUDIT-STATUS: RED=0 CHECKED=38 SOURCES-CITED=38

## 渲染状态

- 模板: `cards/072/index.html`（复制自 `cards/065/index.html`——本栏目最近一份已建成并渲染过的
  3 卡汇总模板。保留 `data-theme="aushow"` 主题色 token 与 `.ticket`/`.ledger`/`issue-strip`
  组件样式，仅替换 3 个 `<section class="poster xhs">` 区块内的文案。**注意**：`cards/` 下各期
  目录里都没有 `assets/`，index.html 末尾那句 `assets/magazine-bg-webgl.js` 自 001 起一直 404、
  `mag-bg` canvas 留空，065 的 3 张 PNG 就是在这个状态下渲染出来的，属已验证的既有状态，本期不改）
- 张数: 3 张（封面 / 按"现在该做的那个动作" 2 行 ledger / CTA）——本期只有 2 场，ledger 两行，不凑空卡
- 渲染: 交由 `automation/render_card.py`（headless Chrome 逐张单独截图），本次会话不调用任何截图工具
