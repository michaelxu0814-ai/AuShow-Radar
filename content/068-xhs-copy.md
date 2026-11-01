# 068 — 演出一改期，退款不退给你（转票防骗指南）

**选题类型**：转票防骗指南（周日轮换位，2026-11-01 生成）
**信源条目**：不依赖 `data/events.json`——本篇只讲**模式**，全篇**零处**引用任何单场演出的
日期／场馆／票价／平台／主办方，因此不消耗 verified 池。

**与 18 篇前作的差异（避免同选题重复）**：003/007/012/013/017/019/024/026/031/033/039/
044/046/051/052/056/057/062 十八篇，全部站在**付钱前后那一小段时间**里——这个人诚不诚实、
这张票能不能转、价格合不合法、钱从哪条通道走、现在票到底存不存在。

本篇第一次把时间轴**拉到演出之后**，问一个更晚才会爆的问题：

**票你拿到了，顺利进场也没问题——可只要这场演出改期或者取消，你会发现官方系统里
压根没有"你"这个人。**

这件事的依据不是传闻，是 **Ticketmaster 澳洲购买政策第 5 条的一句原话**：
"If an event is cancelled or rescheduled, only the original purchaser of a forwarded ticket
will be entitled to any available refund."（演出取消或改期时，**只有**被转发票的**原购票人**
有权获得任何可得的退款。）

- **与 031 的边界（最接近的一篇，而且是 031 自己留下的口子）**：031 写的是**取消**之后的
  "退款链接"钓鱼，主信源是 Scamwatch 冒名警示。031 的核查表末尾**明确写了一条主动剔除**：
  "演出改期/延期时的退款规则……与本篇'取消自动退'主线易混淆，故正文只写取消，不展开改期
  的机制。"本篇就是去把那条被挂起来的线补完，并且**完全不碰 031 的钓鱼主线**——本篇零次
  提到钓鱼页面、假退款链接、Scamwatch。
- **与 052 的边界（必须说清的一条）**：052 讲**你付给对方的那笔钱**走哪条通道、追不追得回。
  本篇讲**官方退出来的那笔钱**流向谁。**两笔钱，方向相反**，一笔出一笔进，事实源也不同
  （052 走支付／消费者保护口径，本篇走票务合同条款），不重叠。
- **与 046 的边界**：046 用的是帮助文章"第三方网站买的票有效吗"，讲的是**票有不有效**，
  且只对原购票人确认有效性。本篇用的是**购买政策条款正文**（clause 5／6），讲的是
  **事后那笔钱和那份合同归谁**。一个是入场资格，一个是退款资格。
- **与 051 的边界**：051 用过同一个 `purchase.html` 页面，但取的是 **clause 9（账号不得
  他人使用）与 clause 16.4（限购／不经通知取消）**。**clause 5（Ticket Forward）与
  clause 6（Cancelled and Rescheduled Events）全部 18 篇前作一条未用。**
- **与 062 的边界**：062 在**付钱之前**（条码还锁着，拿不出票）。本篇在**票已经稳稳到手
  之后**。两篇是同一条时间轴的两端，062 零次提及退款／改期，本篇零次提及 delivery delay。
- **与 013 的边界**：013 是卖票方视角的"反向被骗"。本篇只有一句话落在卖方侧
  （多次转发只有最后一张有效），事实源为 clause 5，与 013 无共用事实，且不展开。
- **与 017 的边界**：017 是账号被盗、票被转出去。本篇全程假设账号正常、交易正常、
  票真实有效——风险恰恰来自"一切正常"。

**红线自查**：全篇不点名任何具体个人、账号、群组或卖家，只讲模式。提到的两家票务平台
（Ticketmaster／Ticketek）**仅作官方规则的正面引用**，不绑定任何场次、不作推荐或批评。
不写任何统计数字，不写任何演出的日期／场馆／票价／主办方。

**本篇主动声明的局限（写进正文，不藏）**：
① **"退款只给原购票人"这句话是 Ticketmaster 的条款原话，我不把它推广成全澳通则。**
   Ticketek 的改期页与取消页**没有**这句话，所以两家**分开写**：Ticketek 侧我只写它页面上
   实际写了的（卡购自动退、改期要自己申请、票对新日期仍然有效）。
② **本篇讲的是"规规矩矩走官方转让"都会发生的事。** 正因为连官方流程下的结果都是这样，
   完全不走官方流程的私下转票只会更糟——但"更糟"三个字是我的判断，**不是官方原话**，
   这里标明。
③ **不写"所以永远别接转票"。** 官方转发（Ticket Forward）是平台自己提供的功能。本篇给的
   不是一刀切劝退，是**付钱之前该问清的一个问题**。
④ "官方全程只认订单、没有任何一步会问票现在在谁手里"——这句是我把几条 GREEN 事实拼起来的
   **编辑框架**，不是某一条可逐字引用的官方断言，正文里按框架写，不计入核查表。

## 标题（12字）

演出一改期，退款不退给你

## 正文（发帖文案，无外链）

防骗写到第十九篇，我发现前十八篇有一个共同的盲区：**它们全都停在付钱那一刻前后。**

这个人诚不诚实、这张票能不能转、价格合不合法、钱从哪条通道走、票现在到底存不存在——
问完这些，票到手了，进场了，大家都觉得这件事结束了。

今天这篇讲的是**它没结束的那一段**。

先说结论，顺便把它的适用范围也说在前面：

**票你拿到了、顺利进场也没问题——可只要这场演出改期或者取消，你会发现官方系统里
压根没有"你"这个人。**

下面这套原话出自 **Ticketmaster 澳洲的购买政策**。另一家 Ticketek 的规则不一样，
我放在后面**分开写**，不合并成"全澳都这样" 👇

**第一句，先把合同关系讲清楚。**

购买政策第 5 条（Ticket Forward，也就是转发／转让）写得非常直白：**你把自己买的票转发出去，
只是在让另一个人"使用"这张票**；而这张票的**购买协议、以及随之而来的各项权利和义务，
始终在 Ticketmaster 和你——原购票人——之间，无论这张票被转发多少次。**

读懂这句话，后面所有事都顺理成章了。

**第二句，是我这次查到最想让你记住的。**

同一条里：**演出取消或改期时，只有被转发票的原购票人，有权获得任何可得的退款。**

还有紧接着的一句：**关于这张票以及这场演出的一切事务，Ticketmaster 只与原购票人交涉。**

再加一句更冷的：在法律允许的范围内，Ticketmaster 对一张票可能承担的任何责任，
**只对原购票人负，不对票被转发到的任何接收人负。**

**第三句，连钱的去向都写死了。**

帮助中心那页写得更不留余地：**Ticketmaster 必须把款项退给账户持有人、以及购买时使用的
那个支付方式。** 购买政策第 6.5 条也是同一口径：**退款将使用你初次购买时的同一支付方式。**

所以不要指望"到时候让他把钱转给我"是个有保障的安排。**在官方那边，那笔钱必然回到
付钱那张卡、那个账号。** 它之后会不会到你手上，官方不管——那已经是你们两个人之间的事了。

**第四句，连通知也只走他。**

第 6.1 条：改期或取消时，平台会用**你 My Ticketmaster 账号里的联系资料**通知你，所以要
保持资料更新。但同一条里还有一句官方自己写下的提醒：**平台无法保证你能在演出日期之前
被告知**取消或改期，**你应当自己盯着账号和官网**，去确认这场有没有变动、改到了哪天。

而第 5 条把"通知你"这件事的责任，明明白白分配给了他：**作为原购票人，有责任把平台提供的
任何信息，持续告知所有收到你转发票的人。**

翻译成人话：**官方把"通知你"这件事，外包给了那个卖你票的人。**

**第五句，是真正要命的——改期退款有截止日。**

第 6.3 条：演出改期后，票对新日期仍然有效。如果你在**指定截止日**之前告知无法出席新日期，
可以取消订单并拿回票款。**但未在合理的指定截止日前告知，将被视为重新确认了这笔订单，
你将无法再因为改期索取退款。**

把前面几句叠起来看，你就明白这条为什么要命：**那个截止日的通知，只会进他的邮箱。**
他忘了转告、懒得转告、或者干脆算准了不转告，窗口就那么无声无息地关上了——而根据第 5 条，
到时候有资格去谈的人，也不是你。

**第六句，还有一层兜底条款。**

第 6.4 条：**场次专属退款条款**可以规定"不支付任何退款"，或者用别的补偿方式代替退款；
并且这类条款**优先于**上面 6.2、6.3 的通用退款条款。所以"改期一定能退"本身就不是铁律。

**顺带一条给要往下转的人。** 第 5 条：一张票如果被**多次转发，只有最后一次转发出来的那张
有效，之前所有条码都会作废**。另外，平台**可以取消**以欺诈手段、或违反相关条款取得的
转发票。（这里我守住边界：官方写的是"接受之后，发送方原票不能再用于入场"，**没有**写
"发送方还能再转一次把你那张弄作废"，所以我不替它推论。）

**那另一家呢？分开写，不合并。**

Ticketek 的改期页与取消页，**没有**"退款只给原购票人"这句话。它实际写的是：

- **改期**：Ticketek 会发邮件告知新日期、时间和场馆；你不需要联系他们，除非你想因为
  去不了新日期而申请退款。而且**即使你留的邮箱已经过期，票对新日期依然有效**。去不了
  新日期的，有权获得**全额退款**，通过退款与付款表单提交申请。
- **取消**：线上用信用卡／借记卡买的，会**自动**收到全额退款，**你不需要做任何事**；
  **即使平台没有你现在在用的邮箱，退款也仍然会自动处理**。在代理点用现金、EFTPOS 或
  礼券买的，才需要自己提交退款申请。

看出这套流程的性质了吗——**它从头到尾都只认那笔订单。**自动退款是按**付款方式**退的，
改期申请是**账号持有人**去提的。整个流程里，**没有任何一步会问"这张票现在在谁手里"。**
（这句是我把上面几条事实拼起来的判断，不是官方原话，标明。）

**所以这篇给你三个动作，全是付钱之前就能做完的。**

**① 把"退款归谁"当成价格的一部分，当场问清。** 这张票是谁的账号买的、用谁的卡付的、
万一改期或取消，官方会把钱退到谁那里。**这不是信任问题，是合同问题**——上面那些条款
已经替你们两个人把答案写好了，你只是去确认一下而已。真遇到含糊其辞、觉得你问得太多的，
那本身就是信息。

**② 别把"能进场"当成风险结束。** 这是本篇唯一真正想换掉的那个念头。过去十八篇教你
验票、验人、验时点，验完了票到手了，大多数人就松手了。**可这张票的风险尾巴，一直拖到
演出真正结束那一天。**

**③ 真要接票，自己盯官方状态，别等他转告。** 这不是多疑——**是官方自己写的**：平台
不保证在演出日之前通知到你，还让你自己盯账号和官网；同时把转告的义务，写给了原购票人。
所以别人的邮箱不是你的信息渠道，**活动页才是。**

最后说句自己的话。这个号为什么宁可一周少发几条，也只发自己能对上来源的场次——

因为这些事的共同点都是：**一个东西"实际在你手上"，和"制度上算你的"，是两回事。**
票在你手机里，但在合同上它还是别人的。日期场馆我对不上官方来源就不写；一场演出的退款
归谁，我也宁可把条款原话抄给你，你自己判断。

想要我把"开票就提醒你"这件事做了的，评论区扣 1，私信发你这份"**接票前先问退款归谁**"
自查卡，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #演唱会 #转票 #防骗 #买票避坑 #留学生 #悉尼演唱会 #墨尔本演唱会 #布里斯班

## 卡片文案结构（4张，票根美学）

> 张数说明：防骗类按 prompt 可精简到 2–3 张，本篇用 4 张，理由与 052／056／057／062 相同——
> "官方条款的四句原话"和"付钱前能做的三件事"是两块各自饱满的内容，拆开比塞进一张清楚；
> 封面与 CTA 为账号固定结构。无空卡、无凑数卡。P1 不配图（防骗类不绑定任何单场演出视觉）。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 防骗指南 · 改期退款归谁篇
- 大字标题: 演出一改期 / 退款不退给你
- 副标题: 前十八篇都停在付钱那一刻 · 这一篇讲之后
- lead: 票在你手机里，但在合同上，它还是别人的。
- 底部条: 两家规则不同 — 本篇分开写不合并

**P2 官方条款原话**
- kicker: Ticketmaster 购买政策 · clause 5 / 6
- 大字: 系统里 / 没有"你"
- ledger 4条:
1. 合同归谁 — 转发只是让另一个人"使用"这张票；购买协议与各项权利义务，始终在平台与原购票人之间
2. 退款归谁 — 取消或改期时，只有被转发票的原购票人有权获得任何可得的退款
3. 钱退到哪 — 必须退给账户持有人与购买时使用的那个支付方式（6.5：同一支付方式）
4. 谁来通知你 — 平台不保证你在演出日前被告知；而转告收票人的责任，写给了原购票人
- 收尾: 改期退款有指定截止日：未在截止前告知无法出席，视为重新确认订单，不能再因改期索取退款。
- 底部条: 只讲模式 不点名 — 依官方购买政策与帮助页
- 备注: 第 6.4 条另规定场次专属退款条款可写"不退款"，并优先于通用条款

**P3 付钱前的 3 件事**
- kicker: 付钱之前 · 做这 3 件事
- 大字: 问清楚 / 不是多疑
- ledger 3条:
1. 把"退款归谁"当价格的一部分 — 谁的账号买的、谁的卡付的、改期退到谁那里；这是合同问题，不是信任问题
2. 别把"能进场"当风险结束 — 这张票的风险尾巴，一直拖到演出真正结束那天
3. 自己盯官方状态 — 别人的邮箱不是你的信息渠道，活动页才是
- 收尾: 另一家 Ticketek 没写"退款只给原购票人"：卡购取消自动退、改期要自己申请、邮箱过期票仍对新日期有效。
- 底部条: 实际在你手上 — 不等于制度上算你的
- 备注: Ticketek 侧只写其页面实际写了的内容，不与 Ticketmaster 合并成通则

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 先问 / 退款归谁
- 正文: 评论区扣 1，私信发你这份"接票前先问退款归谁"自查卡，还有后续开票提醒。
- 底部条: VOL. 068 — 简介里有完整演出日历

## 事实核查表

> 全部 19 条均为**一手官方页面**（Ticketmaster AU 购买政策与帮助中心 / Ticketek AU 帮助
> 中心），2026-11-01 本次会话经 Firecrawl scrape 以 `maxAge:0`（强制实时抓取，不走缓存）
> 取得，四个页面均 **HTTP 200**，引文为页面正文逐字。本篇不含任何 `events.json` 字段断言，
> 也不含任何统计数字。
>
> 信源 A＝`https://www.ticketmaster.com.au/h/purchase.html`（Purchase Policy，Update
> Effective: 12 December 2023；clause 5 与 clause 6 为全部 18 篇前作**零次引用**，051 仅用
> 过同页的 clause 9 与 16.4）
> 信源 B＝`https://help.ticketmaster.com.au/hc/en-au/articles/43006802273169-How-do-I-request-a-refund`（前作零次引用）
> 信源 C＝`https://help.ticketek.com.au/hc/en-us/articles/360044955693-My-event-has-been-rescheduled-and-I-can-t-attend-the-new-date-what-should-I-do-now`（前作零次引用）
> 信源 D＝`https://help.ticketek.com.au/hc/en-us/articles/360044428414-My-event-has-been-cancelled-what-should-I-do-now`（前作零次引用）

| # | 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|---|
| 1 | Ticketmaster AU 的转发功能名为 Ticket Forward，亦称 Ticket Transfer，适用于大多数活动 | GREEN | 信源 A clause 5，逐字 "Ticketmaster offers 'Ticket Forward' functionality, which may also be referred to as 'Ticket Transfer', in respect of most events." | 正文仅用于点明术语；"most events" 未写成"所有场次" |
| 2 | 转发一张自己买的票，只是在让另一个人**使用**该票；购买协议与随之而来的权利义务始终在 Ticketmaster 与原购票人之间，无论被转发多少次 | GREEN | 同上 clause 5，逐字 "By forwarding a ticket you have purchased, you are only facilitating another person **using** that ticket for event entry - the agreement (and associated rights and obligations) for the purchase of that ticket remains between Ticketmaster and you, the original ticket purchaser, regardless of the number of times the ticket is forwarded." | 本篇第一支柱；"only facilitating…using" 的强调为原文自带 |
| 3 | 演出取消或改期时，只有被转发票的原购票人有权获得任何可得的退款 | GREEN | 同上 clause 5，逐字 "If an event is cancelled or rescheduled, only the original purchaser of a forwarded ticket will be entitled to any available refund." | **本篇主线与标题的唯一依据**；范围严格限定于 Ticketmaster，见局限① |
| 4 | 关于该票及其所属演出的一切事务，Ticketmaster 只与原购票人交涉 | GREEN | 同上 clause 5，逐字 "Ticketmaster will only deal with the original purchaser of a forwarded ticket in respect of all matters relating to the ticket and the event for which it is issued." | — |
| 5 | 作为原购票人，有责任将 Ticketmaster 提供的任何信息持续告知所有转发票的接收人 | GREEN | 同上 clause 5，逐字 "As the original purchaser of a ticket, it is your responsibility to keep all the recipients of your forwarded ticket updated with any information Ticketmaster provides to you." | 正文"官方把通知你这件事外包给了他"一句的依据 |
| 6 | 在法律允许范围内，Ticketmaster 对一张票的任何责任只对原购票人负，不对票被转发到的接收人负 | GREEN | 同上 clause 5，逐字 "To the extent permitted by law (including, without limitation, the Australian Consumer Law), any liability Ticketmaster may have in connection with a ticket will only be owed to the original purchaser of the ticket and not to any recipient to whom that ticket may have been forwarded." | 原文"在法律允许范围内／不限于澳洲消费者法"的限定已在正文保留为"在法律允许的范围内" |
| 7 | 一张票若被多次转发，只有最近一次转发的票对入场有效，之前所有条码都会被取消 | GREEN | 同上 clause 5，逐字 "If a ticket is forwarded multiple times, only the ticket from the most recent Ticket Forward will be valid for entry - all previous ticket barcodes will be cancelled." | 正文只用一句、不展开（卖方侧属 013）；并明写官方**未**说"发送方接受后还能再转"——官方写的是接受后发送方原票不能入场，不作推论 |
| 8 | Ticketmaster 可取消以欺诈手段、或违反相关条款取得的转发票 | GREEN | 同上 clause 5，逐字 "Ticketmaster may cancel a forwarded ticket if the ticket was obtained fraudulently or otherwise in violation of the relevant terms and conditions." | 括注一句，未据此做任何判定 |
| 9 | 取消或改期时，Ticketmaster 会使用 My Ticketmaster 账号的联系资料通知；但不保证购票人能在演出日期之前被告知 | GREEN | 信源 A clause 6.1，逐字 "If you book online, we will use your My Ticketmaster account contact details, so you should ensure these details remain up to date. However, we cannot guarantee that you will be informed of such cancellation or rescheduling before the date of the event." | 正文动作③的依据之一 |
| 10 | 购票人应自行关注 My Ticketmaster 账号与 Ticketmaster 网站，以确认演出是否取消或改期、以及改期后的日期时间 | GREEN | 同上 clause 6.1，逐字 "You should monitor your My Ticketmaster account and the Ticketmaster website to ascertain whether an event has been cancelled or rescheduled and the date and time of any rescheduled event." | 正文"活动页才是你的信息渠道"一句的依据 |
| 11 | 演出改期后，票对新日期仍然有效（或按原票价值另行提供对应票品，视供应情况） | GREEN | 信源 A clause 6.3，逐字 "if an event for which you have purchased tickets or Packages is rescheduled, tickets and Packages will be valid for the new date (or you will be offered tickets or Packages of a value corresponding with your original tickets or Packages for the rescheduled event) subject to availability." | 正文保留"仍然有效"，未写成无条件承诺 |
| 12 | 若在指定截止日前告知无法出席改期后的演出，可取消订单并取得票款退款 | GREEN | 同上 clause 6.3，逐字 "If you notify us before the specified deadline (which will be a reasonable period from the time the rescheduled event date is announced) that you are unable to attend the rescheduled event, you will be able to cancel your order and obtain a refund of the sale price of your tickets or Packages" | 正文写明"指定截止日"，未编造具体天数 |
| 13 | 未在合理指定截止日前告知无法出席，将被视为重新确认该订单，且不能再因改期索取退款 | GREEN | 同上 clause 6.3，逐字 "Failure to notify us by any reasonable specified deadline that you are unable to attend the rescheduled event will be deemed to be a reconfirmation of your order for tickets or Packages for the rescheduled event, and you will not be able to claim a refund as a result of the reschedule (unless required by applicable law)." | 本篇第二支柱；原文 "(unless required by applicable law)" 的例外已在卡片与正文以"视为重新确认"口径保守陈述，未写成绝对无退路 |
| 14 | 场次专属退款条款（Event Specific Refund Terms）可规定不支付退款或以其它补偿代替，并优先于 6.2、6.3 的通用退款条款 | GREEN | 信源 A clause 6.4，逐字 "Event Partners may have Event Specific Terms which provide that no refunds are payable or provide for other remedies in place of a refund…Any Event Specific Refund terms shall take precedence over the refund terms set out at clauses 6.2 and 6.3 above." | 正文用于拆掉"改期一定能退"这个错误安全感 |
| 15 | 退款将使用购票人初次购买时所用的同一支付方式 | GREEN | 信源 A clause 6.5，逐字 "Refunds will be made using the same means of payment as you used for the initial purchase." | 与 031 的边界：031 第 2 条用的是 **Ticketmaster 美国页**的 "processed to the original method of payment"，本条为**澳洲购买政策条款正文**，且本篇不复用 031 的"3–5 个工作日"与 Scamwatch 钓鱼主线 |
| 16 | Ticketmaster 必须将款项退给账户持有人、以及购买时使用的支付方式 | GREEN | 信源 B，逐字 "Ticketmaster must refund payment to the account holder and the payment method used at the time of purchase." | 本篇第三支柱；"account holder"（账户持有人）一语为全部 18 篇前作零次引用，是把"钱必然回到他那边"说死的那一句 |
| 17 | Ticketek：演出改期时会邮件告知新日期／时间／场馆；购票人无需联系平台，除非想因无法出席新日期而申请退款；且即使留存邮箱过期，票对新日期依然有效 | GREEN | 信源 C，逐字 "If your event has been rescheduled, Ticketek will email you with all relevant details, including the new date, time, and venue (if applicable). You do not need to contact us unless you wish to request a refund because you are unable to attend the new date." 与 "Even if your email address on file is out of date, your tickets will remain valid for the new date." | 两家分开写的依据之一，见局限①；Ticketek 页**无**"退款只给原购票人"之表述，故本篇不替它写 |
| 18 | Ticketek：无法出席改期后的演出者有权获得全额退款，退款申请经退款与付款表单提交 | GREEN | 同信源 C，逐字 "If you cannot attend the new date, you are entitled to a full refund. Refund requests can be submitted via the Refund and Payment Form." | 正文据此说明"改期申请是账号持有人去提的" |
| 19 | Ticketek：线上以信用卡／借记卡购票者在演出取消时自动获全额退款、无需进一步操作；即使平台没有当前邮箱，退款仍自动处理；代理点现金／EFTPOS／礼券购票则需自行提交退款申请 | GREEN | 信源 D，逐字 "If you purchased your tickets online using a credit or debit card, you will automatically receive a full refund…No further action is required from you."、"Even if we do not have your current email address on file, your refund will still be processed automatically." 与 "If you purchased tickets at an agency using cash, EFTPOS, or a Ticketek Gift Voucher, you will need to submit a refund request via the Refund and Payment Form." | 正文据此说明自动退款是**按付款方式**退的 |

### 本次主动剔除（写下来，避免下次重复踩）

- 🔴 **031 的全部钓鱼主线**（Scamwatch 冒名退款警示、假退款链接、十一条红旗与自保步骤）：
  本篇**零次**提及。本篇讲的是官方退款**真实发生时钱流向谁**，不讲假退款。
- 🔴 **"3–5 个工作日到账"**：031 核查表第 3 条已占用，本篇不复用，正文一个数字都不写。
- 🔴 **Hyperwallet 退款流程**（信源 B 占该页一半篇幅：原卡退款失败时改走第三方支付商、
  365 天验证期、汇率费用等）：事实已核实为 GREEN，但它属**原购票人自己的退款操作细节**，
  对本篇"退款归谁"的主线没有增量，且会把文案拖进操作教程，**整段不写**。
- 🔴 信源 B 该页关于**可疑邮件／冒名 Ticketmaster 或 Hyperwallet** 的提示：虽在同页且为
  GREEN，但属 **031 主线**，为保持两篇边界清晰，**主动不写**。
- 🔴 **clause 12.4(a)**（即使因取消／改期造成损失，机票住宿等个人安排费用自担、平台与主办方
  不负责）：事实为 GREEN 且与本篇主题相邻，但它谈的是**连带损失**而非**退款归谁**，会分散
  本篇唯一的那个念头（"能进场≠风险结束"已足够承载），**本篇不写**，留给未来一篇。
- 🔴 **clause 6.2**（全场取消的退款与手续费不退规则）、**clause 8**（演出照常举行则一般无退换）：
  GREEN 但偏离主线，且 6.2 与 031 的"取消"主题重叠，**不写**。
- 🔴 **clause 16.3**（Ticketmaster 不保证未授权第三方转售平台所售票的真伪）：属
  **007／046 支线**，不重讲。
- 🔴 **clause 9／16.4**（账号不得他人使用、限购与不经通知取消）：**051 已占用同页这两条**，
  本篇一条不复用。
- 🔴 **Ticketek Marketplace 买家保障（Buyer Guarantee）**：检索中出现且页面可取，但
  Marketplace 规则属 **026／046 支线**，且本篇主线是官方转发而非官方转售，**不写**。
- 🔴 **"所以永远不要接转票"这类一刀切结论**：不写，见局限③。
- 🔴 被骗之后的处置顺序（银行／报案／chargeback／IDCARE）：属 **012／024／052／057 支线**，
  本篇**零提及**——本篇全部动作都在付钱之前，这是有意的结构选择。
- 全篇未引用任何统计数字（被骗金额／报案数／黄牛比例一律不写）。

FACT-AUDIT-STATUS: RED=0 CHECKED=19 SOURCES-CITED=19

## 渲染状态

- 模板基底：**复制 `cards/062/index.html`**。本次已用 Python 逐字节确认其 `<style>` 区块与
  `cards/001/index.html` **完全一致**（两侧均 27000 字节，`==` 比较为 True），因此"保留 001 的
  aushow 主题色 token 与全部已验证组件样式"这一要求已满足。062 另带 046 验证过的
  `.ledger-note{max-width:460px}` 长中文处理，以及"防骗类封面不配图"的 poster 结构。
- `<title>` 已改为"演出一改期，退款不退给你 · AuShow 068"（062 曾遗留 057→056 的串号问题，
  本次逐一核对过，无串号）。
- `<html lang="zh-CN" data-theme="aushow">` 与主题色 token 未改动。
- 4 张 `<section class="poster xhs" id="xhs-01..04">`，`<main class="sheet">` 内无其它
  `<section>` 元素——`automation/render_card.py` 用 `nth-of-type` 逐张单独截图，依赖这一点。
- P2 为本篇唯一的 4 行 ledger（前作防骗类多为 3 行）：第 4 行文案长度已按 `max-width:460px`
  的既有约束控制在与前三行同量级，未新增任何内联样式。
- 输出：`cards/068/output/xhs-068-01.png` ~ `xhs-068-04.png`，预期均 1080×1440。
- **本步骤未渲染、未截图**（按 prompt 第 0／5 步：渲染交给 `run_daily_xhs.sh` 调用的
  `automation/render_card.py`，不在本会话用 chrome-devtools-mcp 打开页面截图）。
