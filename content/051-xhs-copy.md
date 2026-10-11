# 051 — 票还没开卖，钱已经没了（转票防骗指南）

**选题类型**：转票防骗指南（周日轮换位）
**信源条目**：不依赖 `data/events.json` 的具体演出——本篇只讲**模式**，不涉及任何单场
演出的日期/票价/场馆断言，因此不消耗 verified 池。唯一引用的 JSON 字段是周杰伦两站
`notes` 里的"每账户限购6张"（`verified=true`），仅作"限购是真实存在的规则"的实例，
不播报该演出、不构成安利。

**与 13 篇前作的差异（避免同选题重复）**：003/007/012/013/017/019/024/026/031/033/039/
044/046 十三篇全部建立在同一个时间前提上——**这张票已经存在**（在别人手里／在假网站上／
在你被盗的账号里／在取消退款流程里／在门口黄牛手里／在规则上不可转）。本篇第一次写
**票还不存在的那一段时间**：演出刚官宣、还没开票，钱已经走了。这使得前十三篇所有判据
（比价格／看页面／查票号／要截图／核对原价上限／查转售资格）**一条都用不上**——不是
你不会用，是确实没有东西可看。收费点被推到"票出现之前"，标的物是一个承诺。

- 与 044 的边界：044 的主角是 **bot 与加价上限**（"秒没"为什么发生、用脚本抢票违不违法、
  WA/SA 两州罚则），"代抢"在 044 里只作为一句反面词出现（"别找加价代抢"），044 **零处**
  写过定金/预售码/限购串联/账号出借这组机制。本篇主角是**代抢这笔交易本身的结构**：
  钱先走、票后有、票不在你名下。044 用过的"自动化手段下单可被取消"一条，本篇**主动
  不写**，留给 044，避免事实重叠。
- 与 046 的边界：046 是"票已存在、但规则上不能转"（转售资格开关）；本篇是"票还不存在"。
- 与 017 的边界：017 是你的票务账号**被别人撞库盗走**（你被动、是失主）；本篇是你**主动
  把账号密码交出去**换"代抢"（你同意了，且违反平台条款）。两者法律/条款处境完全不同。
- 与 003 的边界：003 是买**别人手里的现成票**，交易双方都认同"有一张票"；本篇成交时
  双方都知道票还没有。
- 与 019 的边界：019 是"不谈钱开局"（送你票/说你中奖）；本篇开局**就谈钱**，而且是
  正常价甚至偏贵的"服务费"，看起来比 019 那类正规得多。

**红线自查**：全篇不点名任何具体个人、账号、代抢卖家或群组。文中出现的 Ticketmaster /
Ticketek 均为**一级官方售票方**语境（正面引用其官方条款与帮助页规则），非点名批评。
未使用任何未经核实的演出信息。

## 标题（11字）

票还没开卖，钱已经没了

## 正文（发帖文案，无外链）

演出刚官宣，票还没开卖，有人已经在收钱了。

这一类的坑和之前讲过的都不一样。之前那些，不管多假，总有**一张票**可以让你查：票号、
订单截图、转售页面、原价上限。这一类没有——成交的时候，票还不存在。你付的不是票，是
一个承诺 👇

**① "先付定金／服务费，开票那天我帮你抢"。** 票还没出来，钱已经过去了。抢不到、或者
对方根本没去抢，你手里连一个可以追问的凭证都没有。

**② "我有内部预售码／预售名额"。** Ticketek 官方帮助页把这件事写得很死：**收到预售
邀请或预售码，并不保证你能拿到票**；就算码是有效的，也**不保证有余票**。另外预售
"不保证更好的座位，也不是优先选座服务"——放出来的座位由主办方决定，可能在场馆任何
位置。更关键的一句：码如果用不了，要去找**发这个码给你的那个机构**，不是找票务平台。
预售入口本来是主办方、赞助商、艺人或相关方发给特定人的。所以从陌生人手里买来的码，
出了问题**没有任何一方对你负责**。

**③ "把账号密码给我，我登进去帮你抢"。** Ticketmaster 购买政策第 9 条原文就一句：
"You shall not permit anyone other than you to use your account."（不得允许除你本人以外
的任何人使用你的账号）。Ticketek 那边还补了一刀：账号密码**只用于登录 My Ticketek**，
**与预售、特惠无关**。换句话说，"把密码给我才能帮你抢预售"这个说法本身就不成立。

**④ "我多账号多设备，比你手快"。** 两家官方都写了同一件事：超过限购，可以**不经通知**
取消你的订单——而且会按**同一个姓名、同一个邮箱、同一个账单地址、同一个信用卡号**
串起来算。Ticketek 还专门回答过"要不要多开标签或多设备"，答案是 **No**，多开只会
让你更慢、还可能干扰下单流程。限购不是摆设：我们在跟的周杰伦澳洲两站，官方规则就是
每账户限购 6 张。

也就是说，花钱请人多开号帮你刷，最好的结果是票，最坏的结果是**整单被静默取消**，钱
和票一起没。Ticketek 甚至写明，为了压黄牛，它可以自行把你的取票方式改成"到场馆取票"。

**开票前就把三件事定下来：**
① **只认官方入口**——Ticketek 写得很清楚，官方票只有三个来源：官网、官方 App、官方
代理点（Ticketek Agencies）；
② **码只认发码的人**——预售码来自主办方／赞助商／艺人／官方会员邮件，不从陌生人手里买；
③ **账号是你自己的**——密码不给任何人，开票那天自己登进去排队。

抢不到票只是今天不开心；把钱和账号一起交出去，是接下来几个月都不开心。

官方渠道是唯一凭证。评论区扣 1，私信发你这份"开票前避坑清单"，还有后续开票提醒～
澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #演唱会 #抢票 #防骗 #代抢 #买票避坑 #悉尼演唱会 #墨尔本演唱会

## 卡片文案结构（4张，票根美学）

> 张数说明：防骗类按 prompt 可精简到 2–3 张，本篇用 4 张，理由与 003/007/044/046 相同——
> "四个预付信号"（4 条，每条一个官方规则做底）和"开票前定三件事"（3 条动作）是两块
> 各自饱满的内容，拆开比塞进一张清楚；封面与 CTA 为账号固定结构。无空卡、无凑数卡。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 防骗指南 · 开票前篇
- 大字标题: 票还没开卖 / 钱已经没了
- 副标题: 代抢费 · 预售码 · 借账号
- 说明: 成交的时候票还不存在——票号、截图、转售页面、原价上限，一条都用不上。
- 底部条: 票还不存在 — 就没有凭证可追
- 配图: 无（本篇不涉及任何单场演出，不使用任何演出海报，避免"海报张冠李戴"）

**P2 开票前的 4 个预付信号（ledger 4条）**
1. 先收定金 — 票还没开卖就要定金／服务费，你买的是一个承诺，不是票
2. "内部预售码" — Ticketek 官方：收到预售邀请或码，都不保证能拿到票
3. 要你的密码 — Ticketmaster 政策第 9 条：不得允许除你本人以外的任何人使用你的账号
4. "多号更快" — 超限购可不经通知取消，按同名／同邮箱／同账单地址／同卡号串联
- 收尾: 四条的共同点：收费点被推到了"票出现之前"。
- 底部条: 只讲模式 不点名 — Ticketmaster／Ticketek 官方条款

**P3 开票前就定这 3 件事（ledger 3条）**
1. 只认官方入口 — Ticketek 明文：官方票只有官网、官方 App、官方代理点三处
2. 码只认发码方 — 预售码来自主办方／赞助商／艺人；码用不了要找发码机构，不是票务平台
3. 账号不外借 — 密码只用于登录，与预售／特惠无关；多开标签或多设备只会更慢
- 收尾: 抢不到票是今天不开心；交出账号和钱，是之后几个月都不开心。
- 底部条: 开票当天 — 自己登进去排队

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 开票前 / 先别转钱
- 正文: 评论区扣 1，私信发你这份"开票前避坑清单"，还有后续开票提醒。
- 底部条: VOL. 051 — 简介里有完整演出日历

## 事实核查表

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | Ticketmaster AU 购买政策第 9 条原文 "You shall not permit anyone other than you to use your account." | GREEN | https://www.ticketmaster.com.au/h/purchase.html （2026-10-11 WebFetch 抓取成功，返回 clause 9 原文逐字）。该页此前仅 003 以"Resale 板块"用过另一子页，**本条款为 13 篇前作均未使用的新事实** |
| 2 | Ticketmaster AU：超过或试图超过公示限购，保留**不经通知**取消订单的权利（clause 16.4） | GREEN | 同上 purchase.html，原文 "If you exceed or attempt to exceed the posted ticket limits, we reserve the right to cancel, without notice," + "We reserve the right to cancel any orders where we identify breaches of these limits," |
| 3 | Ticketmaster AU：不得用多个账号规避或超过公示限购 | GREEN | 同上 purchase.html，原文 "Multiple accounts may not be used to circumvent or exceed published ticket limits." |
| 4 | Ticketek：超过限购，可由 Ticketek 自行裁量**不经通知**取消任意或全部订单与门票；且串联**同名／同邮箱／同账单地址／同信用卡号或其它信息**的订单 | GREEN | Ticketek《Terms and Conditions of Sale》原文 "When purchasing tickets for a particular event you may be limited to a specified number of tickets. If you exceed the stated ticket limit, you may have any or all of your orders and tickets cancelled without notice by Ticketek at its discretion. This includes orders associated with the same name, e-mail address, billing address, credit card number or other information."（2026-10-11 经 help.ticketek.com.au Zendesk API `articles/26000971458969.json` 取得正文，直接 WebFetch premier 页超时、help 页历来 403，沿用 003/013/039/044 的"官方站 403 改走等价官方接口"路径）https://help.ticketek.com.au/hc/en-us/articles/26000971458969-Ticketek-Terms-and-Conditions-of-Sale |
| 5 | Ticketek 同页：限购目的为保障粉丝公平获取并压制黄牛 | GREEN | 同上原文 "Ticket limits apply to ensure fair access to tickets for fans, and as a measure to minimise ticket scalping." |
| 6 | Ticketek：为压制黄牛，可自行裁量把配送方式改为 "venue collect" | GREEN | 同上原文 "In the interests of minimising ticket scalping, Ticketek may change your delivery method to \"venue collect\" at its discretion." |
| 7 | Ticketek：**收到预售邀请或预售码，并不保证拿到票**；持有有效码也不保证有余票 | GREEN | Ticketek《What is a Pre-sale & How do I sign up?》原文 "Receiving a pre-sale invitation or code does not guarantee tickets." 与 "Please note that having a valid code does not guarantee ticket availability."（2026-10-11 Zendesk API `articles/360001880467.json`）https://help.ticketek.com.au/hc/en-us/articles/360001880467-What-is-a-Pre-sale-How-do-I-sign-up |
| 8 | Ticketek：预售**不保证更好的座位、不是优先选座服务**；放出的座位由主办方裁量，可能在场馆任何位置 | GREEN | 同上原文 "They do not guarantee better seats and are not a preferential seating service." + "Seats released during a pre-sale are chosen at the discretion of the promoter and may be located anywhere in the venue." |
| 9 | Ticketek：预售入口由主办方／赞助商／艺人或相关方提供；码用不了应联系**发码的机构** | GREEN | 同上原文 "Access may be offered through a promoter, sponsor, artist, or associated party and may require a password or specific link to purchase." + "If it still doesn't work, contact the organisation that issued the code for assistance." |
| 10 | Ticketek：官方票只能从**官网、官方 App、Ticketek Agencies（官方代理点）**购买 | GREEN | Ticketek《On-Sale Information》原文 "You can only purchase official tickets from: The Ticketek website The Ticketek App Ticketek Agencies"（2026-10-11 Zendesk API `articles/360001862168.json`）https://help.ticketek.com.au/hc/en-us/articles/360001862168--On-Sale-FAQs-General-Public-and-Pre-sale |
| 11 | Ticketek：**不建议**多开浏览器／窗口／标签／设备，会减慢访问并干扰下单流程 | GREEN | 同上原文 "Should I open Ticketek in multiple tabs or devices? No. Using multiple browsers, windows, tabs, or devices can slow your access and interfere with the booking process." |
| 12 | Ticketek：主办方可设每客户上限，超限可能导致部分或全部订单**不经通知**被取消，限制可按姓名／邮箱／账单地址／信用卡等识别信息串联 | GREEN | 同上 On-Sale Information 原文 "Promoters may set a maximum number of tickets per customer to ensure fair access. Exceeding this limit may result in some or all of your orders being cancelled without notice. Limits may apply to orders linked by name, email, billing address, credit card, or other identifying information."（与第 4 条互为印证，一为条款、一为帮助页） |
| 13 | Ticketek：账号密码**仅用于登录 My Ticketek 账号，不用于访问预售或特惠** | GREEN | Ticketek《Password and Account Access Help》原文 "Your Ticketek account password is only used to sign in to your My Ticketek account. It is not used to access event presales or special offers."（2026-10-11 Zendesk API `articles/360001861628.json`）https://help.ticketek.com.au/hc/en-us/articles/360001861628-Password-and-Account-Access-Help |
| 14 | 周杰伦澳洲两站官方规则为每账户限购 6 张 | GREEN | `data/events.json` 墨尔本站／悉尼站两条 `verified=true` 条目的 `notes="主办方 Sky Music & Horizon Production;每账户限购6张"` 逐字复制；035/038 曾以 sopa.nsw.gov.au "A maximum of 6 tickets per customer applies" 外部复核 |
| 15 | 正文"前十三篇都默认票已存在"这一自述 | GREEN | `automation/posted-log.md` 中 003/007/012/013/017/019/024/026/031/033/039/044/046 十三行记录逐条比对（本次运行实际读取），无一篇以"票尚未开售"为主线 |

FACT-AUDIT-STATUS: RED=0 CHECKED=15 SOURCES-CITED=15

**主动剔除、未写进文案的内容**：

1. 🔴 **"预售码不对公众发放 / cannot be offered to members of the public"** —— 首轮
   WebSearch 摘要里出现过这句疑似 Ticketmaster 帮助页原文，但针对该短语的定向检索
   **无任何官方页面可确证**（返回的全是 SEO 内容农场与无关站点），Ticketmaster 帮助页
   本身 403。判定为**无法验证**，整句剔除，不以任何形式进入正文或卡片。
2. **Ticketmaster "Use of automated means to purchase tickets is strictly prohibited."**
   —— 本次 purchase.html 抓取中确实存在（可用），但 044 已以 Ticketmaster 条款 PDF
   写过"自动化手段下单可被取消"。为保持与 044 的事实边界清晰，**主动不写**。
3. **Amex 等持卡人预售需用本人该卡完成购买** —— 首轮 WebSearch 摘要提及，但未能
   在官方页面取得逐字原文（Ticketmaster 帮助页 403），不写入。
4. **Ticketek 条款中"为规避已有封禁而新开账号可被限制／停用"** —— 原文已取得，但
   指向的是"被封禁者"场景，与本篇"你被代抢连带取消"主线不同，为免读者误解为同一
   机制，不写入。
5. **任何具体代抢渠道、群组、平台或个人** —— 按账号红线，全篇只讲模式。
6. **具体金额**（代抢费／定金行情价）—— 无官方或可核实信源，不编造数字。

## 渲染状态

- 模板: `cards/051/index.html`（复制 `cards/001/index.html`，保留 `data-theme="aushow"`
  主题色 token 与 `.ticket`/`.ledger`/`issue-strip` 组件样式，仅替换 4 个
  `<section class="poster xhs">` 内的文案）
- 本篇不使用演出海报配图（P1 无 `figure.frame-img`），与 003/007/012/013/017/019/024/
  026/031/033/039/044/046 同一处理：防骗类不绑定任何单场演出的视觉
- 输出: 由 `automation/render_card.py` 在本次会话结束后渲染为
  `cards/051/output/xhs-01…04.png`，均 1080×1440
- 渲染不在本次对话内进行（2026-08-16 起的既定分工：chrome-devtools-mcp 截图不可靠，
  渲染交由确定性脚本 `render_card.py` 完成）
