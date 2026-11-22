# 075 — 他没问你密码，票却转走了（转票防骗指南）

**选题类型**：转票防骗指南（周日轮换位，2026-11-22 生成）
**信源条目**：不依赖 `data/events.json`——本篇只讲**模式**，全篇**零处**引用任何单场演出的
日期／场馆／票价／主办方，因此不消耗 verified 池（池内仍为 8 条，未变）。

**与 22 篇前作的差异（避免同选题重复）**：003/007/012/013/017/019/024/026/031/033/039/
044/046/051/052/056/057/062/063/068/069/070 二十二篇，坏人想从你这里拿走的东西只有五类——

- **你的钱**（003 私下转票／007 假站／012·024 追款／033·044 加价与抢票脚本／039 门口／051 代抢定金）
- **你的票**（017 账号被登入转卖／026 优惠票资格／046 不可转／062 条码锁定期／069 不是那一张）
- **你的身份资料**（057）
- **你的银行账户和你的名字**（063 钱骡）
- **你的账号密码**（017 被盗；051 你自愿交出去换"代抢"）

本篇第一次写**第六类，而它根本不是一样"东西"**：

**他要的是你那块已经登录好的屏幕。**

他不需要你的密码——**因为你已经替他登录好了**。他不需要骗你转钱——**因为他可以在你
屏幕上自己转**。官方把这类叫 **remote access（远程访问）**，并且写明了它能走多远：
取得远程访问后，对方"可以控制你的屏幕，并访问你设备上的任何文件、**以及你打开着的任何
应用**"。

- **与 051 的边界（最接近的一篇）**：051 是你把**票务账号的密码**交出去换"代抢"——交出去的是
  一串可以改掉的凭证，改完就失效；本篇交出去的是**实时的控制权**，密码无关，改密码也不能
  把正在你屏幕上的那只手请走（官方还提醒：骗子常留一个"后门"方便再回来）。
- **与 017 的边界**：017 的主线是**凭证**（密码独一无二、验证码谁都不给），全程没有人在你
  屏幕上；本篇的核心冷点正好相反——**验证码确实只发给你本人，但它显示在他正在看的那块
  屏幕上。**"谁都不给"这条防线在这里不是被突破，是**用不上**。
- **与 063 的边界**：063 你是工具、损失不是你的；本篇你是受害人，且全程坐在原位看着它发生。

**红线自查**：全篇不点名任何具体个人、账号、群组、代抢渠道或卖家，只讲模式。文中出现的
TeamViewer／Zoho Assist／AnyDesk 三个软件名**是澳洲政府网络安全中心官方公告里逐字点名的**，
原文语境为"若对方已通过这三款软件访问过你的设备，该怎么做"，本篇照原文语境引用，不暗示
任何一款软件本身不正当。

**主动剔除（查不到官方信源，一律不写）**：
1. **"转票场景里确实发生过远程访问诈骗"**——官方描述这套骗局时，冒充的身份是电信公司／
   电脑公司／技术支持服务商，**没有任何官方来源把它和买票／转票绑在一起**。本篇因此只写
   **机制**（它成立的条件只有一个：你把屏幕交出去了），不声称这是票圈已发生的案件。
2. **具体话术剧本**（"对方会说……"的台词）——无官方来源，不编。
3. **任何涉案数字**（损失金额／案件数）——未核实，不写。
4. **手机被 port 走之后票务账号会怎样**——官方只写到银行短信码与一次性密码会转到骗子那里，
   没写票务平台，不外推。

## 标题（12字）

他没问你密码，票却转走了

## 正文（发帖文案，无外链）

防骗写到第二十三篇，我把前面二十二篇摊开数了一遍：骗子想从你这儿拿走的东西，一共只有五样——

**你的钱**、**你的票**、**你的身份资料**、**你的银行账户**、**你的账号密码**。

今天这篇是第六样，而它根本不是一样"东西"：

**他要的是你那块已经登录好的屏幕。**

这一类里，**他从头到尾没问过你密码。** 不是他客气，是**没必要**——账号你自己登着呢。

下面的原话分别出自 **Scamwatch（澳洲国家反诈中心）** 和 **ASD's ACSC（澳洲信号局网络安全
中心）**，票务那一段出自 **Ticketmaster 澳洲官方帮助中心** 👇

**第一句，是这篇的地基，也是最冷的一句。**

Scamwatch 写远程访问这类骗局时，有一句把边界划得非常干脆：

**一旦骗子取得你设备的远程访问权限，他们就能控制你的屏幕，并访问你设备上的任何文件，
以及你打开着的任何应用。**

读第二遍，重音放在最后六个字：**你打开着的任何应用。**

不是"你的密码被偷了"。是**根本不需要密码这一步**——你的邮箱开着、银行 app 开着、票务账号
登着，他看到的就是你看到的那一屏。

**第二句，官方把"装个软件"这件事，和转钱放在了同一排。**

ACSC 的《个人网络安全手册》把骗局拆成三个阶段：**接触**（你收到一条没预料到的消息或来电）→
**操控**（对方施压让你快点动手）→ **付款或数据窃取**。

第三阶段里，官方并列写出了对方想让你做的几件事：**转钱、交出个人资料、把验证码给他、
装一个软件、点开恶意链接或扫恶意二维码。**

看清这个并列——**"装一个软件"和"转钱"是同一档**。前二十二篇里，"你有没有把钱转出去"
一直是那条生死线；这一类的生死线往前挪了一步，挪到**"你有没有装那个东西"**。

同一份手册给远程访问骗局的定义也只有一句：**有人自称来自技术支持，要你装软件、或者给他
远程访问你设备的权限。**

**第三句，官方替你把"对方是谁"这一层直接封死。**

ASD's ACSC 的公告原话：**澳洲政府机构绝不会联系个人、要求远程访问使用他们的电脑，也不会
要求为某项调查转账。**

这句好用的地方在于：它不要你去判断对方像不像真的。**这一类不存在"真的那一版"。**

还有一条相关的，也是整篇里我最想你记住的判据——ACSC 列钓鱼警讯时写了一条：

**来电者要你跳过正常的安全步骤。**

**第四句，为什么这一类在转票这件事上特别致命。**

先看官方转票流程本来长什么样。Ticketmaster 澳洲帮助中心写的第一步是：**登录你自己的
Ticketmaster 账号**；流程中间还有一步：**你可能会收到一条发到手机的一次性验证码，用来验证
你的身份，输入后点确认。**

这一步在 017 那篇里是防线——"验证码谁都不给"。但在这一类里，它**不是被突破，是用不上**：

码**确实**只发给你本人。**它就显示在他正在看的那块屏幕上。**

（这句是我把上面两条官方原话拼起来的推导，不是官方原话，先标明。）

再看后果，这两条都是官方写的：**转让被对方接受后，收票人会拿到一张只有他能用的新条码，
而发送方账号里那张票同时不再具备入场效力**；以及 **只有发送方可以取消一次 Ticket
Transfer**（未被接受前取消，票会回到账号里）。

把这两条和"控制你的屏幕"连起来读——**当"发送方"是坐在你屏幕上的那个人时，撤销那一步的
权限也在他手里。**

顺带一句，官方自己在收票那一节也写了：**为你自身安全起见，最好认识并信任向你转票的那个人。**

**第五句，这一类的警讯不在聊天记录里，在你自己的设备上。**

Scamwatch 列的警讯里有这几条，你会发现它们**没有一条跟"对方说了什么"有关**：

- 你**登不进**自己的电脑或手机，或者邮箱、社交媒体和其他在线账号
- 电脑屏幕上**出现新的图标**
- 开始**跳出弹窗**
- 电脑上的文件**被移动或删除**
- 有人联系你、**要你买一个软件或订一项服务**
- 你的账户里出现**异常活动**

**第六句，如果已经发生了：官方把动作和顺序都写了，而且和前几篇不一样。**

ASD's ACSC 原话：**若网络犯罪者已经通过 TeamViewer、Zoho Assist 或 AnyDesk 访问过你的设备，
应向 ReportCyber 报告，并立即通知你的银行；你的金融机构可能可以对你的账户做临时冻结。**

接着：**更改所有重要在线账号（含银行、邮箱、社交媒体）的密码，并开启多因素验证。**

这里有一条是前二十二篇**从没出现过**的动作，而它恰恰是这一类独有的——Scamwatch 写：

**把那个远程访问软件从你的设备上删掉，并用杀毒软件检查对方有没有再装别的恶意软件；
骗子往往会留一个"后门"，方便再次访问你的设备。**

**换句话说：这一类里，"把钱追回来"不是最后一步，"把人请出去"才是。** 前几篇的处置清单
到"报案+止付"就结束了，是因为那些骗局结束在转账那一刻；这一类**不会自己结束**。

还有一条路径值得单独记，因为它绕开了所有"码只发给你"的前提——Scamwatch 写的号码被
"port"（携号转移）走：骗子用钓鱼、数据泄露或你社交平台上的信息冒充你，联系你的运营商，
要求把你的号码转到他控制的新 SIM 卡上；**一旦转移完成，所有来电和短信，包括银行短信码
这类双因素验证和一次性密码，都会到骗子那里。**

**所以这篇给你三个动作，都不用你判断对方是真是假。**

**① 把"要操作你的设备"本身当成结论，不当成请求。** 不管对方是来帮你转票、帮你退款、帮你
"验证付款"，还是帮你修电脑——**要屏幕、要装软件、要远程协助，到这里就可以停了。** 官方给
的那条判据可以直接搬：**要你跳过正常安全步骤的，就是警讯。** 政府机构那一档更干脆：
**绝不会要求远程访问你的电脑**，所以这一类压根没有"真的那一版"。

**② 要核实，就自己另起一条线。** ACSC 写得很明白：**想核实一通来电是否属实，应当另行从
该机构官网取得联系方式，不要用来电里给你的号码或其他信息。** 票务侧同理——**自己打开官方
app、自己登录自己的账号去看**，别顺着别人给你的那条路走回去。

**③ 真发生了，先"请人出去"，再谈钱。** 顺序照官方写的来：**删掉那个远程访问软件 → 杀毒
软件查后门 → 立即通知银行（可能可以临时冻结）→ 向 ReportCyber 报告 → 改掉所有重要账号的
密码并开多因素验证。** 把这一步当成和止付同等重要的事，因为**门不关，后面全是白做**。

最后说句自己的话。这二十三篇写下来，坑的形状一直在变，我这次最想你带走的是一句很短的分别：

**凭证可以改，控制权不行。**

密码泄露了，你改一次就追回来了；会话被人握住的那段时间里，你改什么都在他眼前改。所以这
一类不靠"我能看出他是骗子"来防——**它只有一道门，就是"我不把屏幕交出去"，而这道门永远在
你手上。**

想要我把"开票就提醒你"这件事做了的，评论区扣 1，私信发你这份"**有人要操作我的设备**"
自查卡，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #演唱会 #转票 #防骗 #买票避坑 #留学生 #网络安全 #悉尼演唱会 #墨尔本演唱会

## 卡片文案结构（4张，票根美学）

**P1 封面**
- kicker: 防骗指南 · 控制权篇
- 大字标题: 他没问你密码 / 票却转走了
- 副标题: 前二十二篇写的都是凭证和钱 · 这篇写那块已经登录好的屏幕
- 说明: 官方原话：取得远程访问后，对方可以控制你的屏幕，并访问你打开着的任何应用。
- 底部条: 只讲模式 不点名 — 依 Scamwatch 与 ASD's ACSC 原文

**P2 官方原文（ledger 4条）**
- kicker: Scamwatch · ASD's ACSC 原文
- 大字: 他不需要 / 你的密码
1. 控制你的屏幕 — 官方：一旦取得远程访问，对方可控制你的屏幕，并访问设备上任何文件、以及你打开着的任何应用
2. "装个软件"= 转钱同一档 — ACSC 把骗局拆成接触→操控→付款或数据窃取，第三阶段并列写着：转钱、交资料、给验证码、装一个软件、点恶意链接
3. 这一类没有"真的那一版" — ACSC：澳洲政府机构绝不会联系个人、要求远程访问使用他们的电脑
4. 最好记的一条判据 — ACSC 钓鱼警讯之一：来电者要你跳过正常的安全步骤
- 收尾: 警讯不在聊天记录里，在你的设备上：登不进自己账号、屏幕冒出新图标、开始跳弹窗、文件被移动或删除、账户出现异常活动。
- 底部条: 官方描述的冒充身份是电信/电脑公司与技术支持 — 本篇只写机制

**P3 三个动作（ledger 3条）**
- kicker: 不用判断对方真假 · 做这 3 件事
- 大字: 凭证可以改 / 控制权不行
1. 要屏幕就是结论 — 帮你转票、帮你退款、帮你"验证付款"都一样：要装软件、要远程协助，到这里停
2. 核实另起一条线 — ACSC：另行从官网取得联系方式，不要用来电里给你的号码；票务侧同理，自己开官方 app 自己登录
3. 真发生了先请人出去 — 删远程访问软件 → 杀毒查后门 → 立即通知银行（可能临时冻结）→ 报 ReportCyber → 改密码开多因素验证
- 收尾: 官方提醒：骗子往往留一个"后门"方便再次访问你的设备。门不关，后面全是白做。
- 底部条: 转票那一步：官方说只有发送方能取消 — 屏幕在谁手上，这一步就在谁手上

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 我不把 / 屏幕交出去
- 正文: 评论区扣 1，私信发你这份"有人要操作我的设备"自查卡，还有后续开票提醒。
- 底部条: VOL. 075 — 简介里有完整演出日历

## 事实核查表

全部信源均于 **2026-11-22 当日**实际抓取核实（Firecrawl scrape，HTTP 200）。

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | 远程访问骗局中，骗子冒充电信公司、电脑公司或技术支持服务商 | GREEN | Scamwatch《Account or identity takeover scams》"Remote access" 小节原文 "Scammers impersonate a telecommunications or computer company, or a technical support service provider."（https://www.scamwatch.gov.au/types-of-scams/account-or-identity-takeover-scams ，旧路径 /types-of-scams/remote-access-scams 现 301 至此页；页面 dcterms.modified 2026-01-28） |
| 2 | 他们试图让你相信电脑或网络有问题、需要买新软件来修 | GREEN | 同上，原文 "They try to convince you that you have a computer or internet problem and that you need to buy new software to fix the problem." |
| 3 | 来电者会以"查清问题所在"为由要求远程访问你的设备 | GREEN | 同上，原文 "The caller will request remote access to your device to 'find out what the problem is'." |
| 4 | 一旦取得远程访问，对方可以控制你的屏幕 | GREEN | 同上，原文 "Once a scammer gains remote access to your device, they can control your screen…" |
| 5 | 并可访问设备上的任何文件、以及你打开着的任何应用 | GREEN | 同上，同句后半 "…and access any files located on your device or any apps you may have open." |
| 6 | 警讯包含：登不进自己的电脑/手机或邮箱、社交媒体及其他在线账号 | GREEN | 同上，Warning signs 列表 "You can't log in to your computer or mobile, or your email, social media and other online accounts." |
| 7 | 警讯包含：屏幕出现新图标、开始跳出弹窗、文件被移动或删除 | GREEN | 同上，列表 "New icons appear on your computer screen." / "Pop-up boxes start appearing on your computer screen." / "Files on your computer have been moved or deleted." |
| 8 | 警讯包含：有人联系你要你买软件或订一项服务；你的账户出现异常活动 | GREEN | 同上，列表 "Someone contacts you and asks you to buy software or sign up to a service." / "Unusual activity in your accounts." |
| 9 | 处置动作：删除设备上的远程访问软件，并用杀毒软件检查是否被植入其他恶意软件 | GREEN | 同上，Protect yourself 列表 "Delete the remote access software from your device. Check to see if the scammer has added any additional malware to your device by using antivirus software." |
| 10 | 骗子往往会留一个"后门"以便再次访问你的设备 | GREEN | 同上，紧接一句 "Often scammers will leave a 'back door' to gain access to your device again." |
| 11 | 号码被 port 到骗子控制的新 SIM 后，所有来电与短信（含银行短信码与一次性密码）都会到骗子那里 | GREEN | 同上，Identity theft 小节原文 "Once ported, all calls and messages including 2 factor authentication like bank SMS codes and one-time-pins, go to the scammer."（骗子先经 phishing／数据泄露／社交平台信息冒充你联系运营商要求 port） |
| 12 | 澳洲政府机构绝不会联系个人要求远程访问使用其电脑，也不会要求为某项调查转账 | GREEN | ASD's ACSC《Protect yourself from remote access scams》原文 "Australian Government agencies will never contact individuals asking for remote access to use computers or request funds to be transferred for an investigation."（https://www.cyber.gov.au/advisory/protect-yourself-from-remote-access-scams ） |
| 13 | 官方逐字点名的三款远程访问软件为 TeamViewer、Zoho Assist、AnyDesk | GREEN | 同上，原文 "If the cybercriminal has accessed your device via Team Viewer, Zoho Assist or AnyDesk…"（原文语境为事后处置，非指软件本身不正当） |
| 14 | 该情形下应向 ReportCyber 报告并立即通知银行；金融机构可能可以临时冻结账户 | GREEN | 同上，原文 "…you should report it to ReportCyber and **immediately** notify your bank. Your financial institution may be able to put a temporary freeze on your financial accounts." |
| 15 | 之后应更改所有重要在线账号（含银行、邮箱、社交媒体）密码并开启多因素验证 | GREEN | 同上，原文 "change passwords on all your important online accounts including banking, email and social media, and turn on multi-factor authentication for extra security." |
| 16 | 核实来电是否属实应另行从该机构官网取得联系方式，不要用来电提供的号码或信息 | GREEN | 同上，原文 "contact the organisation by sourcing their details separately from their website, NOT using the phone number or other details from the incoming call." |
| 17 | ACSC 把骗局拆为三阶段：接触 → 操控 → 付款或数据窃取 | GREEN | ACSC《Personal cyber security handbook — Learn how to spot scams》原文小节 "Contact / Manipulation / Payment or data theft"（https://www.cyber.gov.au/publication/personal-cyber-security-handbook/learn-how-to-spot-scams ） |
| 18 | 第三阶段官方并列的目标包含"装一个软件"，与转钱、交资料、给验证码、点恶意链接/二维码同列 | GREEN | 同上，原文 "The scammer tries to get you to transfer money, share personal details, provide them with a verification code, install software, or click malicious links or QR codes." |
| 19 | 远程访问骗局定义：有人自称来自技术支持，要你装软件或给他远程访问设备的权限 | GREEN | 同上，原文 "Someone claims to be from technical support and asks you to install software or give them remote access to your device." |
| 20 | 钓鱼警讯之一："来电者要你跳过正常的安全步骤" | GREEN | 同上，Warning signs of phishing 列表 "Callers asking you to skip normal security steps." |
| 21 | Ticketmaster 澳洲官方转票流程第一步为登录你自己的 Ticketmaster 账号 | GREEN | Ticketmaster AU 帮助中心文章 20172934446097《How does Ticket Transfer work?》原文步骤 1 "Sign into your Ticketmaster Account."（https://help.ticketmaster.com.au/hc/en-au/articles/20172934446097-How-does-Ticket-Transfer-work ） |
| 22 | 转票流程中可能收到一条发到手机的一次性码用于验证身份 | GREEN | 同上，步骤 4 原文 "You may receive a text with a one-time code to verify your identity. Type in the code and select Confirm."（**057 已引用过同句**，本篇复用，结论不同） |
| 23 | 转让被接受后收票人获得只有他能用的新条码，发送方账号内的票不再具备入场效力 | GREEN | 同上，原文 "the recipient is issued a new barcode that only they can use. The tickets in the sender's account will no longer be valid for entry."（**062 已引用过同句**，本篇复用作后果） |
| 24 | 只有发送方可以取消一次 Ticket Transfer；未被接受前取消，票会回到其账号 | GREEN | 同上，Cancelling 小节原文 "Only the sender can cancel a Ticket Transfer." 与 "Your ticket will be returned to your account."（前作零次引用） |
| 25 | 官方建议：为你自身安全起见，最好认识并信任向你转票的那个人 | GREEN | 同上，Accepting Tickets 小节原文 "For your own security, it's a good idea to know and trust the person transferring tickets to you."（前作零次引用） |
| 26 | 推导：在远程访问场景下，"验证码谁都不给"（017 主线）不成立——码仍只发给本人，但显示在对方正在看的屏幕上 | AMBER | 非官方原话，为 #4+#5（可控制屏幕、可访问打开着的应用）与 #22（码发到本人手机）两条官方原文的推导，正文与卡片均已标注"这是推导不是官方原话" |
| 27 | 推导：当"发送方"是控制你屏幕的那个人时，#24 的撤销权也在他手上 | AMBER | 非官方原话，为 #4+#5 与 #24 的推导，正文已标注 |
| 28 | 本篇不声称"转票场景已发生远程访问诈骗" | GREEN | 主动剔除项：#1 官方描述的冒充身份仅为电信／电脑公司／技术支持服务商，无任何官方来源将其与买票／转票绑定，故全篇只写机制成立条件，不作案件断言 |

**RED 项**：无。两条推导（#26／#27）已在正文和核查表双处标注为推导，并给出其所依据的官方原文编号；一条可能被误读为案件断言的说法（#28）已在"主动剔除"中明确不写。

FACT-AUDIT-STATUS: RED=0 CHECKED=28 SOURCES-CITED=28

## 渲染状态

- 模板: `cards/075/index.html`（复制 `cards/001/index.html`，保留 `data-theme="aushow"` 主题色 token 与 `.ticket`/`.ledger`/`issue-strip` 组件样式，仅替换 4 个 `<section class="poster xhs">` 区块内的文案）
- 卡片张数: 4（P1 封面 / P2 官方原文 ledger / P3 三个动作 ledger / P4 CTA）——防骗类不使用任何演出海报，无 `figure.frame-img`
- 输出: 待 `automation/render_card.py` 渲染至 `cards/075/output/`
- 渲染不在本次会话内进行（2026-08-16 实测 chrome-devtools-mcp 截图工具反复超时，渲染已移交 `run_daily_xhs.sh` → `render_card.py` 确定性完成）
