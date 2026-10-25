# 062 — 条码还锁着，他拿什么给你（转票防骗指南）

**选题类型**：转票防骗指南（周日轮换位）
**信源条目**：不依赖 `data/events.json`——本篇只讲**模式**，全篇**零处**引用任何单场演出的
日期／场馆／票价／平台／主办方，因此不消耗 verified 池。

**与 17 篇前作的差异（避免同选题重复）**：003/007/012/013/017/019/024/026/031/033/039/
044/046/051/052/056/057 十七篇，问的全都是**关于人和票的问题**——对方诚不诚实
（003／007／024／056）、这张票能不能转（026／046）、价格合不合法（033／044）、
钱怎么付、追不追得回（012／019／051／052）、对方要的是什么（013／017／057）。

本篇第一次问**时间**：这场演出的票，**现在到底存不存在可以交出来的形态**。

因为有一件事几乎没人跟买票的人讲过：**很多热门场次，你自己买到票之后，也一样拿不出票。**
票务系统会把条码锁住，一直锁到演出前几天。官方给这段时间起了名字，叫 **delivery delay**。
这件事一旦知道，"他离演出还有三周就给你看条码截图"这句话的性质就变了。

- **与 051 的边界（最接近的一篇）**：051 是**票还没开卖**，标的物根本不存在，所以"预付定金
  抢票"是纯空手。本篇是**票已经卖出去了、也真实存在，但还没解锁**——两个完全不同的时间窗。
  051 用的是限购与"主办方可自行裁量改成 venue collect"那组事实；**条码锁定期与 delivery
  delay 的定义，051 一条未用。**
- **与 003 的边界**：003 第②格用**一句话**提过"私下发来的截图不等于有效票"，依据是官方转售
  会重新配发条码。本篇不重复那条，而是补上 003 完全没有的**上游**：在解锁之前，按官方规则
  那张截图**连存在的条件都没有**；并且第一次引到官方把"不能截图"写成明文规则的原话。
- **与 046 的边界**：046 问的是**资格**——这张票在规则上能不能挂上官方转售（主办方关了／
  属套票／是转售买来的）。本篇问的是**时点**——就算资格齐全，现在也可能还取不出来。
  一个是"能不能"，一个是"什么时候"。
- **与 057 的边界（必须说清的一条）**：057 讲官方转票流程**要你填哪些字段**（只要邮箱或
  手机号），用的是转让功能的**输入端**。本篇用的是**交付端**。⚠️ 另外 057 核查表里出现过
  一个"48 小时"，指的是**分享出去的票若 48 小时未被接受会自动退回**；本篇的"48 小时"是
  **条码解锁时点**（Ticketek 侧约为演出前 48 小时）。**两个 48 小时是两件事**，正文里特意
  写明了，避免读者（和我自己）串线。
- **与 044 的边界**：044 讲抢票脚本把好票秒掉。本篇引到的官方原话里，delivery delay 的目的
  恰好就是"在确认没人用不公平抢票技术批量买票之前不放票"——这是 044 那条主线的**下游补丁**，
  但这组事实 044 未用，044 也没提过票买到后还会被锁。
- **与 017 的边界**：017 是账号被撞库盗走、票被转出去。本篇与账号安全无关，讲的是正常账号里
  一张正常的票，在时间上处于什么状态。
- **与 031 的边界**：031 是演出取消后的"退款链接"钓鱼。本篇只用到一条相邻事实（官方明说购票后
  不会给你发短信票链接），用途是**正向识别交付方式**，不讲退款，也不重讲钓鱼页面那套。

**红线自查**：全篇不点名任何具体个人、账号、群组或卖家，只讲模式。提到的两家票务平台
（Ticketmaster／Ticketek）**仅作官方交付规则的正面引用**，不绑定任何场次、不作推荐或批评。
不写任何统计数字，不写任何演出的日期／场馆／票价。

**本篇主动声明的局限（写进正文，不藏）**：
① **锁条码不是每场都有。** Ticketmaster 的原话是 "For some events"，Ticketek 的原话是
   "Promoters may request this"——都是**部分场次**。所以本篇给的不是"凡是提前给票的都是骗子"
   这种一刀切判定，而是一个**可以去问、可以去查的问题**。这一点正文写在最前面，不藏在末尾。
② **"锁定期内官方分享点不动"这句话我只敢对 Ticketek 说。** Ticketek 官方明文写了解锁前
   "cannot be added to a mobile wallet or shared"；Ticketmaster 侧我只找到"票不寄出、条码
   不可用"，**没有**任何官方页面说转让功能在延迟期间被禁用，所以我不替它推论。两家分开写。
③ 不写"票上名字对不上就进不去"。Ticketek 官方对这个问题的回答恰恰是**可以**入场（只要
   持有有效票），正文把这条写进去用来**拆掉**一个常见的错误安全感，而不是制造新的。

## 标题（12字）

条码还锁着，他拿什么给你

## 正文（发帖文案，无外链）

防骗写到第十八篇，我回头看了一遍前十七篇，发现它们问的全是**关于人的问题**：

这个人诚不诚实、这张票能不能转、价格合不合法、钱从哪条通道走、追不追得回来。

今天换一个维度。**问时间。**

先把结论放前面，顺便把它的边界也放前面——

**很多热门场次，你自己买到票之后，也一样拿不出票。** 不是系统坏了，是票务按主办方要求
把条码**锁着**，一直锁到演出前几天。但**不是每一场都这样**，所以下面这套不是"提前给票
就是骗子"的一刀切，它是一个你可以当场去查的问题 👇

**官方给这段时间起了名字。**

Ticketmaster 的帮助页定义得很干脆：delivery delay 是**"购买与取用一张票之间的一段时间"**
（原话 "a period of time between the purchase and access to a ticket"）。

为什么要有这段时间？原话也写了：主办方用它来**防止票被取用**，直到票务**确认每个人都遵守了
限购、并且没有使用不公平的抢票技术批量买票**。

（这里顺手接上第 044 篇——那篇讲好票为什么秒没，答案是脚本。今天这条是那件事的下半段：
平台知道脚本的存在，所以干脆让票**先不要能用**，留出时间回头清算。）

**这段锁期有多长？两家都给了数字。**

- **Ticketmaster**：对部分场次，手机条码会有交付延迟，作为**附加的安全特性**；你通常会在
  **演出前 3–7 天**才能取用条码。延迟期间，票不会寄出，手机票条码也不可用，要等延迟被解除。
- **Ticketek**：延迟期间票不会发出，手机或 App 票的条码会**一直锁定到演出前大约 48 小时**。

⚠️ 插一句，免得串线：这个 48 小时是**条码解锁**的 48 小时。第 057 篇里出现过另一个
48 小时，那个是"分享出去的票若 48 小时内没人接受就自动退回"。**两件事，别记混。**

**锁着的时候，这张票"不能"做哪些事？这才是今天真正有用的部分。**

Ticketek 写得最明确：条码解锁之前，票**不能加进手机钱包，也不能分享**。

也就是说——**在解锁之前，官方那个"把票分享给你"的按钮，本来就点不动。**

（这句我只对 Ticketek 说。Ticketmaster 那边我只查到"票不寄出、条码不可用"，**没有**任何
官方页面讲转让功能在延迟期间被禁用，所以我不替它推论。）

**还有一条更硬的规则，是我这次查到最想让你记住的。**

"能不能把手机票打印出来？"——Ticketek 的官方回答是**不能**，原话是手机和 App 内的票
**"不能被打印，也不能被截图"**，必须在场馆**从 Ticketek App 或手机钱包里直接扫**。

所以请把这件事想清楚：**"我截图发给你"在官方那边根本不是一种交付方式。** 那是一张图片。
图片可以同时发给十个人，条码不能。

**顺带一个很好用的识别点：** Ticketek 官方明说，购票之后你**不会**收到短信。手机票主要
通过 App 取用，也可以走确认邮件里的链接或订单记录。所以"票务给我发了短信票链接，我转给你"
这句话，在它这边**不成立**。

**反过来也有坑——给已经买到真票的人。**

Ticketmaster 有一条规则，我觉得少有人知道：**如果票务改了你的配送方式，票会重新出条码；
你那张旧票即便寄到了，在配送方式改掉之后也不能让你入场。**（它家纸质 Collector Tickets
的目标送达时间是演出前一周。）

所以"我有纸票""我有票根"同样不等于能进场。**有效的永远是系统里那条活着的条码，不是你
手上那张纸。**

**那"名字对不上就进不去"能不能当护身符？不能。**

这一条我必须写清楚，因为它反过来：Ticketek 对"别人能不能用我名下这张票"的官方回答是
**可以**——只要持有有效票，持票人就会被放进去。

听着像利好，其实是提醒：**门口验的是票有效，不是你是谁。** 所以别指望"他名字对不上，
门口会帮我拦住"。门口不会。**唯一能保护你的，是让那条有效条码在解锁后真的落到你账号里。**

**所以这篇给你三个动作，全是现在就能做的。**

**① 先查这一场有没有交付延迟、条码什么时候解锁。** Ticketmaster 说交付信息就写在
**购买确认邮件、你账号里的订单页，或者活动页上**。这是你和对方聊之前就该查的一件事，
查完你就知道他"现在能不能拿出票"这句话站不站得住。

**② 对方在解锁之前催你付钱，就是在你无法验证的时间点要钱。** 不用判断他是不是骗子——
你只需要知道，这个时间点你**没有任何办法验证**。那就等。时间站在你这边，不站在他那边。

**③ 真要接票，只认流程走完那一刻。** 官方转让的终点很具体：对方接受之后，系统给收票人
出**一张只有他能用的新条码**，发送方账号里那张**同时失效**。在这一刻之前，截图、订单号、
"已发送"都只是中间状态。

最后说句自己的话。这个号为什么只发核实过的场次、宁可一周少发几条——和今天这篇是同一件事：
**一个东西"看起来有"和"系统里真的有"，是两回事。** 日期场馆我自己对不上来源就不写；
一张票在系统里还没解锁，你也别当它已经在手上。

想要我把"开票就提醒你"这件事做了的，评论区扣 1，私信发你这份"**解锁前不付钱**"自查卡，
还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #演唱会 #转票 #防骗 #买票避坑 #留学生 #悉尼演唱会 #墨尔本演唱会 #布里斯班

## 卡片文案结构（4张，票根美学）

> 张数说明：防骗类按 prompt 可精简到 2–3 张，本篇用 4 张，理由与 052／056／057 相同——
> "两家的锁期时间表"和"三个现在就能做的动作"是两块各自饱满的内容，拆开比塞进一张清楚；
> 封面与 CTA 为账号固定结构。无空卡、无凑数卡。P1 不配图（防骗类不绑定任何单场演出视觉）。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 防骗指南 · 条码锁定期篇
- 大字标题: 条码还锁着 / 他拿什么给你
- 副标题: 前十七篇都在问人 · 这一篇问时间
- lead: 很多热门场次，你自己买到票之后，也一样拿不出票。
- 底部条: 不是每场都锁 — 所以这是个要去查的问题

**P2 两家的锁期时间表**
- kicker: 官方叫它 delivery delay
- 大字: 买到了 / 也拿不出来
- ledger 3条:
1. 它是什么 — "购买与取用一张票之间的一段时间"；用来在确认没人违规限购、没用抢票技术批量买之前，先不放票
2. Ticketmaster — 部分场次条码有延迟，作为附加安全特性；通常演出前 3–7 天才能取用
3. Ticketek — 延迟期间票不发出，手机／App 条码锁到演出前约 48 小时
- 收尾: 锁定期内，Ticketek 明说票不能加进手机钱包、也不能分享——那个"分享给你"的按钮本来就点不动。
- 底部条: 只讲模式 不点名 — 依两家官方帮助页
- 备注: 该"48 小时"为条码解锁时点，与 057 的"分享 48 小时未接受自动退回"不是同一件事

**P3 现在就能做的 3 件事**
- kicker: 解锁前 · 做这 3 件事
- 大字: 时间站在 / 你这边
- ledger 3条:
1. 先查这一场的交付延迟 — 信息就在购买确认邮件、账号订单页或活动页上，聊之前先查
2. 解锁前催你付钱 = 在你无法验证的时点要钱 — 不用判断人，只需要知道此刻你验不了。那就等
3. 只认流程走完那一刻 — 对方接受后，收票人拿到只有他能用的新条码，发送方那张同时失效
- 收尾: 手机与 App 内的票，官方明文"不能打印，也不能截图"。截图不是交付方式，是一张图片。
- 底部条: 门口验票有效 — 不验你是谁

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 解锁之前 / 不付钱
- 正文: 评论区扣 1，私信发你这份"解锁前不付钱"自查卡，还有后续开票提醒。
- 底部条: VOL. 062 — 简介里有完整演出日历

## 事实核查表

> 全部 19 条均为**一手官方帮助页**（Ticketmaster AU / Ticketek AU），2026-10-25 本次会话
> 经 Firecrawl scrape 以 `maxAge:0`（强制实时抓取，不走缓存）取得，四个 Ticketmaster 页与
> 一个 Ticketek 页均 **HTTP 200**，引文为页面正文逐字。本篇不含任何 `events.json` 字段断言，
> 也不含任何统计数字。

| # | 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|---|
| 1 | Ticketmaster 把购买与取用之间那段时间称为 delivery delay，定义为"购买与取用一张票之间的一段时间" | GREEN | `help.ticketmaster.com.au` 文章 34452091076497《What is a delivery delay?》，逐字 "A delivery delay is a period of time between the purchase and access to a ticket." | 本篇主线定义；该页为全部 17 篇前作**从未引用过**的 URL |
| 2 | 其用途：主办方用它防止票被取用，直到平台确认所有人都遵守了限购、且未使用不公平抢票技术批量购买 | GREEN | 同上文章，逐字 "Event Organisers use it to prevent tickets from being accessed until we can confirm everyone has adhered to the event ticket limit and didn't use unfair ticket technology to buy in bulk." | 正文据此接回 044（抢票脚本），但未复用 044 任何事实 |
| 3 | 有交付延迟的订单：票不会寄出，手机票条码不可用，直到延迟被解除 | GREEN | 同上文章，逐字 "If your order has a delivery delay, the tickets won't be shipped and mobile ticket barcodes won't be available until the delivery delay has been removed." | — |
| 4 | 交付信息会出现在购买确认邮件、Ticketmaster 账号的订单上，或活动页上 | GREEN | 同上文章，逐字 "Delivery information is provided within your purchase confirmation email, on your order in your Ticketmaster Account or on the event page." | P3 动作①的唯一依据 |
| 5 | Ticketmaster：部分场次手机条码有交付延迟，作为附加安全特性 | GREEN | `help.ticketmaster.com.au` 文章 34451846151697《Why can't I access my mobile tickets yet?》，逐字 "For some events, your mobile barcodes may have a delivery delay as an added security feature." | "For some events" 即本篇局限①的来源，正文写明"不是每场都锁" |
| 6 | Ticketmaster：通常在演出前 3–7 天才能取用条码 | GREEN | 同上文章，逐字 "You'll be able to access the ticket barcodes typically within 3-7 days before your event." | 正文保留 "typically"→"通常"，未写成承诺 |
| 7 | Ticketmaster：演出前两天仍看不到条码应联系 Fan Support | GREEN | 同上文章，逐字 "If you haven't received your tickets or still can't see a ticket barcode two days before the event, contact Fan Support."（34452091076497 同页亦有等义句） | 辅证，正文未展开成动作 |
| 8 | Ticketmaster：看不到条码时应确认登录的是购票时所用的同一账号 | GREEN | 同上文章，逐字 "Check that you're signed in to the same account used to purchase the tickets." | 辅证；与 017（账号安全）无重叠，此处仅为排查步骤 |
| 9 | Ticketmaster：若平台改了配送方式，票会有新条码；旧票即便及时寄到，在配送方式改掉后也不能入场 | GREEN | `help.ticketmaster.com.au` 文章 44486488730385《I haven't received my tickets in the post yet. What should I do?》，逐字 "If we've changed the delivery method of your tickets, the tickets will have new barcodes. If your old tickets arrive in time, they won't grant you entry into the event after we've changed the delivery method." | 正文"纸票／票根不等于能进场"一段的唯一依据 |
| 10 | Ticketmaster：纸质 Collector Tickets 的目标是演出前一周送达 | GREEN | 同上文章，逐字 "Our goal is for you to have your Collector Tickets in the mailbox by one week before your event." | 括注，正文未据此做任何判定 |
| 11 | Ticketek：delivery delay 是购票后对取用的临时性保留；主办方可要求，用于管理限购并降低黄牛风险 | GREEN | `help.ticketek.com.au` 文章 360001877308《Ticket Delivery Information & FAQs》，逐字 "A delivery delay is a temporary hold on ticket access after purchase. Promoters may request this to manage ticket limits and reduce the risk of scalping." | "may request" 即局限①的第二来源 |
| 12 | Ticketek：延迟期间票不发出，手机或 App 票条码锁定至演出前约 48 小时 | GREEN | 同上文章，逐字 "During a delay, your tickets will not be sent, and mobile or app ticket barcodes will remain locked until approximately 48 hours before the event." | 正文保留 "approximately"→"大约"；并明写此 48 小时与 057 的接受窗口不是同一件事 |
| 13 | Ticketek：App／Mobile Ticket 的条码可能锁定至演出前约 48 小时，解锁前不能加入手机钱包、也不能分享 | GREEN | 同上文章，逐字 "Barcodes may remain locked until approximately 48 hours before the event. Tickets cannot be added to a mobile wallet or shared until they are unlocked." | 本篇最关键一条（"分享按钮点不动"）；正文明确限定只对 Ticketek 成立，见局限② |
| 14 | Ticketek：手机和 App 内的票不能打印、也不能截图，必须在场馆从 App 或手机钱包直接扫描入场 | GREEN | 同上文章，逐字 "No. Mobile and in-app tickets cannot be printed or screenshotted. They must be scanned directly from the Ticketek app or your phone's wallet at the venue for entry." | 全部 17 篇前作**零次**引用过"不能截图"的官方明文（003 仅从"官方转售换发新条码"侧面推出截图无效） |
| 15 | Ticketek：购票后不会收到含手机票链接的短信；手机票主要经 App 取用，亦可走确认邮件链接或订单记录 | GREEN | 同上文章，逐字 "No. Following your purchase, you will not receive an SMS. The Ticketek App is the primary way to access your mobile tickets. Alternatively, tickets can be accessed via your confirmation email or order history." | 正文作正向识别点使用；不展开钓鱼页面（属 031） |
| 16 | Ticketek：只要持有有效票，持票人即可入场（票上是他人姓名不构成阻碍） | GREEN | 同上文章，逐字 "Yes. As long as a valid ticket is held, the holder will be allowed entry." | 正文用它**拆掉**"名字对不上门口会拦住"的错误安全感，而非制造新的安全感；见局限③ |
| 17 | Ticketek：若到演出当天票仍未到或条码仍锁定，应前往 box office 求助 | GREEN | 同上文章，逐字 "If your tickets have not arrived or your barcode is still locked on the day of the event, please visit the box office for assistance." | 辅证，正文未展开 |
| 18 | Ticketek：订单确认后配送方式不可更改 | GREEN | 同上文章，逐字 "Once your order is confirmed, the delivery method cannot be changed." | 与第 9 条（Ticketmaster 可改配送方式）两家规则不同，故**两家分开陈述、未合并成通则**；正文只用了 Ticketmaster 侧 |
| 19 | 官方转让完成后，收票人获得一张只有他能用的新条码，发送方账号内的票同时不再有效 | GREEN | `help.ticketmaster.com.au` 文章 20172934446097《How does Ticket Transfer work?》，逐字 "the recipient is issued a new barcode that only they can use. The tickets in the sender's account will no longer be valid for entry." | **与 057 核查表第 3 条同源**，本篇仅作 P3 动作③的终点定义复用，不再展开转让字段（属 057） |

### 本次主动剔除（写下来，避免下次重复踩）

- 🔴 Ticketek 关于**分享票 48 小时未接受自动退回**、以及**接受前可 Cancel／Recall**
  这两条事实：**057 核查表第 7、8 条已占用**。本篇一条都不复用，并在正文明确区分两个
  "48 小时"，防止读者把"解锁期"和"接受窗口"记混。
- 🔴 原定的"**一张条码卖给多人、先到先扫**"主线：核查时发现其所需事实（官方转让换发新条码／
  发送方失效）已是 046 与 057 的既有内容，novelty 不足，**整条主线弃用**，改走本篇的
  交付时点线（delivery delay 为全部前作零引用）。此处记录，避免下次又绕回这条。
- 🔴 "Ticketmaster 锁定期内也无法使用转让功能"：**无任何官方页面这样写**，属我方推论，
  **不写**，并在正文把这句话的适用范围显式限定在 Ticketek（见局限②）。
- 🔴 Ticketmaster 的具体场次交付时间表（`360009452834` 页逐场列出 Ticket Release Date）：
  属**瞬时状态**且会点到具体赛事／演出名，沿用 018 对 "Low Availability" 的处理原则，**不写**。
- 🔴 "延迟期也防黄牛"合并成一句通则：两家措辞不同（Ticketmaster 讲限购与批量抢票技术，
  Ticketek 讲 ticket limits 与 scalping），**分开引用两家原话，不合并**。
- Ticketek 场馆／预付取票须由 My Ticketek 账户持有人或持卡人本人、并出示带照片身份证件
  （原文 "Only the My Ticketek account holder or the cardholder can collect tickets, and a
  valid photo ID is required."）：事实已核实为 GREEN，但"取票要证件"会与 **057 的身份资料
  主线**产生读者层面的混淆（057 的要点是对方无权向你索要证件），**本篇不写**。
- Ticketek "条码仍锁定时 Ticketek 可自行裁量改为 venue collect"一类限购／配送裁量事实：
  属 **051 支线**，不重讲。
- 官方转售换发新条码、原票作废：属 **003／046 支线**，正文仅以"流程终点"一句带过，不展开。
- 被骗之后的处置顺序（银行／报案／chargeback／IDCARE）：属 **012／024／052／057 支线**，
  本篇**零提及**——本篇全部动作都在付钱之前，这是有意的结构选择。
- 全篇未引用任何统计数字（被骗金额／报案数／黄牛比例一律不写）。

FACT-AUDIT-STATUS: RED=0 CHECKED=19 SOURCES-CITED=19

## 渲染状态

- 模板基底：**复制 `cards/057/index.html`**。本次已用 Python 逐字节确认其 `<style>` 区块与
  `cards/001/index.html` **完全一致**（两侧均 26896 字节，`==` 比较为 True），因此"保留 001 的
  aushow 主题色 token 与全部已验证组件样式"这一要求已满足。057 另带 046 验证过的
  `.ledger-note{max-width:460px}` 长中文处理，以及"防骗类封面不配图"的 poster 结构，
  正是本篇需要的。
- 已修正 057 遗留的 `<title>` 串号问题（057 的 `<title>` 实际写的是 056 的标题），
  本篇 `<title>` 为"条码还锁着，他拿什么给你 · AuShow 062"。
- `<html lang="zh-CN" data-theme="aushow">` 与主题色 token 未改动。
- 4 张 `<section class="poster xhs" id="xhs-01..04">`，`<main class="sheet">` 内无其它
  `<section>` 元素——`automation/render_card.py` 用 `nth-of-type` 逐张单独截图，依赖这一点。
- 输出：`cards/062/output/xhs-062-01.png` ~ `xhs-062-04.png`，预期均 1080×1440。
- **本步骤未渲染、未截图**（按 prompt 第 0／5 步：渲染交给 `run_daily_xhs.sh` 调用的
  `automation/render_card.py`，不在本会话用 chrome-devtools-mcp 打开页面截图）。
