# 017 — 你的票，可能在账号里被卖掉（转票防骗指南）

**选题类型**：转票防骗指南（周日轮换位）
**信源条目**：不依赖 `data/events.json` 的具体演出——本篇只讲**模式与官方口径**，不涉及
任何单场演出的日期/票价/场馆断言，因此不消耗 verified 池。

**与 003 / 007 / 012 / 013 的差异（避免同选题重复）**：
- 003 = **买家视角**，人对人的私下转票怎么识别（盗号熟人、只发二维码、追加改名费、不写原价）
- 007 = **买家视角**，假售票网站 / 未授权转售站怎么识别（搜索结果陷阱、"官方转售分场次不分平台"）
- 012 = **买家视角**，钱已经付出去之后的第一小时（银行止付、chargeback、报案、追款诈骗）
- 013 = **卖家视角**，你手里多一张票要出手时反被"买家"骗（假 PayID、多付退差、不看货就买）
- 本篇 = **没有交易发生**。前四篇的坑全部长在"你和另一个人的一笔交易"里；本篇的坑长在
  **你自己的票务账号**里——你没跟任何人聊过天、没付过一分钱、也没转过一张票，票就已经
  不在账号里了。入口是**别处泄露的密码被拿来登你的票务账号**，不是转票纠纷。
- **与 003 的"盗号"是两回事，需要说清楚**：003 里被盗的是**别人的社交账号**（骗子冒充你
  朋友来私信你），你是被骗的买家；本篇里被盗的是**你自己的票务账号**，你是失主。对象、
  入口、后果、动作全都不同，零重叠。
- 与 012 的边界：012 写"钱没了之后"的银行/报案流程，本篇只写**票那一侧**，一句带过，
  不复述任何银行、chargeback、AFCA、IDCARE 内容。

**红线自查**：全篇不点名任何具体个人、账号、卖家或二级转售平台。文中出现的
Ticketmaster / Ticketek 均为**一级官方售票方**语境：引用的是它们自己公开发布的账号安全
建议与官方表态，属于正面引用，不是点名批评。**特别注意的一处措辞**：ABC 报道明确写的是
账号密码来自**第三方网站泄露**后被拿来登录票务账号，文案严格照此表述，**不写成"票务平台
自己泄露了你的密码"**，避免把责任归因错。

**主动设限**：
- 不引用任何统计数字（007 用过 NASC 下架站点数与季度报损，012 用过 Scamwatch 季度报案数，
  本篇一个都不复用，也不新引——本篇的说服力来自机制和官方建议本身）。
- **不承诺账号被盗后票一定能找回**。Ticketek 的公开表态写成"会与客户一起处理"这个原样，
  不加工成成功率或赔付承诺。
- 不写具体的密码管理器/杀毒软件品牌，不带任何商业推荐。

## 标题（13字）

你的票，可能在账号里被卖掉

## 正文（发帖文案，无外链）

前四篇讲的坑，都长在"你和另一个人的一笔交易"里。今天这个不一样——**你没跟任何人聊过天，没付过钱，也没转过票，票就已经不在你账号里了。**

ABC News 报道过澳洲这一类案子：受害者的用户名、邮箱或密码是在**第三方网站**的数据泄露里流出去的，被卖到暗网，骗子拿着这套账号密码**直接登进他们的票务账号**，把票转卖给毫不知情的买家。有人一直到**演出当天站在场馆门口**，才知道自己的票早就没了。Ticketek 在这篇报道里确认：澳洲是账号钓鱼与诈骗的"**global hot spot**"（全球重灾区）。

请先接受一件反直觉的事：**漏的那个网站，多半不是票务网站。** 报道里网络安全专家指出的原因很朴素——**很多人在多个网站重复使用同一套密码**，所以随便哪个不相干的小网站被拖库，你的票务账号就跟着一起开了门。

**所以真正该做的事，在你抢票之前就该做完 👇**

**① 票务账号的密码，只能用在这一个地方。**
Ticketmaster 澳洲官方的账号安全页写得很直：你的密码应当是**这个账号独有**的，因此**不要用在任何其他账号上**（银行、购物网站、邮箱等等）。这一句不是客套话，它正对着上面那个"重复使用"的入口。

**② 先守住邮箱，它才是总闸。**
同一页还有一条更容易被忽略的：给你的个人邮箱设一个强而独有的密码——因为**邮箱一旦被入侵，别人就可能用它来尝试进入你的票务账号**。想想找回密码走的是哪条路，你就明白邮箱为什么排在票前面。

**③ 手机号保持最新，而且只绑一个账号。**
Ticketmaster 官方建议更新并维护你登记的手机号，购票时**你可能会被要求输入发到手机上的验证码**来完成身份验证；官方同时提醒，**你使用的这个手机号最好只关联一个账号**。

**④ 验证码，谁都不给。**
Scamwatch 的钓鱼页原话是：**永远不要把你的个人信息、信用卡资料、密码或一次性验证码，交给任何主动联系你的人——哪怕对方自称来自你的银行或其他你信任的机构。**

**那封"你的票有异常，请立即登录"，怎么认？** Scamwatch 给了四个警号，按这个顺序过一遍就够用：
- 邮件/短信/来电自称是**你平常就有往来**的那家公司；
- 内容**要求你马上处理**；
- 通篇**没有叫出你的正确姓名**；
- 网址跟你平常用的**只差一点点**。

配套的动作只有两条，都是官方原话：**不要点短信或邮件里的链接**，**不要打开或下载任何附件、App**；要核实，就用你自己查到的官方联系方式**反过来联系**那家机构。Scamwatch 把整套动作压成三个词：**Stop. Check. Protect.（停下来、查一查、护住自己）**

**万一已经出事了。** 票那一侧是有正式路径的：Ticketek 在同一篇报道里表示，如果原持票人**能证明票确实是本人购买、信息确实遭到泄露、且该笔售出属欺诈**，公司会与客户一起处理；同时它也在为关键账户变更加上**多因素验证**等额外安全措施。注意这句话的重量——**它说的是"会一起处理"，不是"一定拿得回来"。** 与其赌这一步，不如把上面四件事今晚做完。

买票这件事最讽刺的地方是：你把所有力气都花在开票那 30 秒，而票丢掉的那一刻，你甚至不在线上。

评论区扣 1，私信发你这份"票务账号自查清单"，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #演唱会 #抢票 #防骗 #账号安全 #留学生 #悉尼演唱会 #墨尔本演唱会

## 卡片文案结构（5张，票根美学）

> 张数说明：003/007/012/013 四篇防骗都是 4 张，因为它们只有"识别"和"动作"两块内容。
> 本篇多了一块前四篇不需要的内容——**这件事到底是怎么发生的**（密码在别处泄露 → 撞进
> 票务账号 → 票被转卖），读者不理解这条链路就不会相信"该改的是别的网站的密码"。所以
> 拆成三块内容卡（机制 / 认钓鱼 / 现在做什么）+ 封面 + CTA = 5 张。每张都是满的，
> 无空卡、无凑数卡。防骗选题一律不挂任何演出海报，沿用 003/007/012/013 做法。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 防骗指南 · 账号篇
- 大字标题: 票没被转错 / 是账号被登了
- 分隔线 + 副标题: 这一次，骗子没跟你说过一句话
- lead: 你没聊过天，没付过钱，没转过票。票就是不在了。
- 底部条: 账号视角 — 别处泄露 · 登入 · 转卖

**P2 它是怎么发生的（ledger 3条）**
1. 密码从别处漏 — ABC 报道：用户名/邮箱/密码在第三方网站泄露后被卖，骗子拿着直接登进票务账号
2. 你重复用了它 — 报道里安全专家指出的原因：很多人在多个网站用同一套密码，拖一处等于开一串
3. 到门口才发现 — 票被转卖给不知情的买家，有人直到演出当天站在场馆门口才知道
- 收尾: 漏的那个网站，多半不是票务网站。
- 底部条: 来源 ABC News — Ticketek 称澳洲是账号钓鱼"global hot spot"

**P3 那封"账号异常"邮件（ledger 4条）**
1. 自称熟面孔 — 自称是你平常就有往来的那家公司
2. 催你马上办 — 内容要求你立即处理
3. 不叫你名字 — 通篇没有用上你的正确姓名
4. 网址差一点 — 域名跟你平常用的只差一点点
- 收尾: 不点链接、不下附件；要核实就用自己查到的官方联系方式反过来联系。
- 底部条: 来源 Scamwatch 钓鱼页 — Stop. Check. Protect.

**P4 现在就做的 4 件事（ledger 4条）**
1. 密码只用一次 — Ticketmaster 官方：票务账号的密码应当独有，不要用在银行、购物、邮箱等任何其他账号
2. 先守住邮箱 — 官方同页：邮箱被入侵，就可能被用来尝试进入你的票务账号
3. 手机号保持最新 — 官方：购票时可能要输入手机收到的验证码；这个号最好只关联一个账号
4. 验证码谁都不给 — Scamwatch：绝不把密码或一次性验证码给主动联系你的人，哪怕自称是银行
- 收尾: 票在账号里，账号在邮箱后面——防线其实要往前挪一格。
- 底部条: 抢票前就该做完 — 不是开票当天才想起

**P5 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 力气花在 / 开票那 30 秒
- lead: 可票丢掉的那一刻，你甚至不在线上。
- 正文: 评论区扣 1，私信发你这份"票务账号自查清单"，还有后续开票提醒。
- 底部条: VOL. 017 — 简介里有完整演出日历

## 事实核查表

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | 澳洲发生过票务账号被他人登入、票被转卖的案件 | GREEN | ABC News 2026-09-06 WebFetch 核实：https://www.abc.net.au/news/2025-02-23/billie-eilish-scammers-ticketek-accounts-tickets-protection/104966286 —— "hackers can resell tickets to unsuspecting buyers" |
| 2 | 入口是第三方网站数据泄露的用户名/邮箱/密码被卖后拿去登录票务账号 | GREEN | 同上，原文："Account holders' usernames, emails or passwords were likely leaked and sold on the dark web to criminals, who then logged into their Ticketek accounts" |
| 3 | 有受害者直到抵达场馆才发现票已被转卖 | GREEN | 同上，原文："Some victims didn't discover the theft until arriving at venues" |
| 4 | 原因之一是多站重复使用同一套密码 | GREEN | 同上，报道引述网络安全专家："people often reuse passwords across multiple sites, making it easier for hackers to exploit compromised credentials" |
| 5 | Ticketek 确认澳洲是账号钓鱼与诈骗的 "global hot spot" | GREEN | 同上，公司表态原文："Australia is a 'global hot spot' for account phishing and scams" |
| 6 | Ticketek 表示在为关键账户变更加入多因素验证等额外安全措施 | GREEN | 同上："implementing additional security measures including multi-factor authentication for key account changes" |
| 7 | Ticketek 表示若原持票人能证明本人购买、信息遭泄露且售出属欺诈，会与客户一起处理 | GREEN | 同上："work with customers to resolve issues if original purchasers could demonstrate legitimate compromise and fraudulent sales occurred"。文案照此写"会一起处理"，未加工成成功率或赔付承诺 |
| 8 | Ticketmaster 澳洲官方：密码应为该账号独有，不得用于其他任何账号（银行/购物/邮箱） | GREEN | Ticketmaster AU 官方账号安全页 2026-09-06 WebFetch 核实：https://discover.ticketmaster.com.au/tips/news/how-to-secure-your-account-and-protect-your-tickets-20618 —— 原文 "Your password should be unique to your Ticketmaster account, and therefore not used for any other accounts (banking, shopping sites, email, etc)" |
| 9 | Ticketmaster 澳洲官方：邮箱被入侵可能被用来尝试进入你的票务账号 | GREEN | 同上，原文："if your email gets hacked it could allow someone to use it to try to gain access to your Ticketmaster account" |
| 10 | Ticketmaster 澳洲官方：购票时可能被要求输入发到手机的验证码 | GREEN | 同上，原文："may also be asked to authenticate your account by inputting a code sent to your phone" |
| 11 | Ticketmaster 澳洲官方：建议所用手机号只关联一个账号 | GREEN | 同上，原文："the phone number you use is only associated with one account" |
| 12 | Scamwatch：绝不把个人信息/信用卡资料/密码/一次性验证码给主动联系你的人 | GREEN | Scamwatch 钓鱼页 2026-09-06 WebFetch 核实：https://www.scamwatch.gov.au/types-of-scams/phishing —— 原文 "Never share your personal information, credit card details, passwords or one-time codes with anyone who contacts you unexpectedly, even if they claim to be from your bank or another trusted organisation" |
| 13 | Scamwatch 列出的钓鱼四个警号（自称常打交道的商家 / 要求紧急处理 / 没用你的正确姓名 / 网址与平常略有不同） | GREEN | 同上，原文四条："You receive an email, text or phone call claiming to be from a business you regularly deal with"／"The communication requires urgent action from you"／"The email or text message doesn't use your proper name"／"The website address is slightly different to normal" |
| 14 | Scamwatch：不要点邮件短信里的链接、不要打开下载附件或 App；用官方联系方式自行反向核实 | GREEN | 同上，原文："Don't click on links in text messages or emails"／"Don't open or download any attachments or apps"／"Verify authenticity by contacting organizations directly using official contact details" |
| 15 | Scamwatch 的官方口号为 "Stop. Check. Protect." | GREEN | 同上，页面核心指引即 "Stop. Check. Protect." |

**RED 项**：无。

**核查过程中被主动剔除的内容（未进入文案）**：
- 原计划引用 cyber.gov.au（ACSC）关于"多因素验证是保护账号最有效手段之一"与 credential
  stuffing 的定义。该站点 2026-09-06 连续 3 次 WebFetch 全部 60s 超时，**只拿到搜索结果
  摘要、拿不到一手页面**，按"核实不了的就不写"原则整段删除，文案中不出现 ACSC 任何表述。
- 原计划引用 OAIC 可通报数据泄露报告中"泄露/被盗凭证占比"的数字。OAIC 发布页当日抓取
  返回的最新报告仅到 2024 年下半年，而搜索结果里的 2025 年数字全部来自二手博客，
  **一手来源对不上**，整条删除（也与本篇"不引统计数字"的主动设限一致）。
- 原计划引用 Ticketek 帮助中心的 MFA 页与密码页原文。该站 help.ticketek.com.au 与
  premier.ticketek.com.au 当日分别返回 403 与超时，抓不到一手页面，故文中关于 Ticketek
  的全部表述**只采用 ABC 报道中该公司的公开表态**，不写任何未核实的 MFA 操作细节
  （例如验证码发到邮箱还是手机、是否只在改资料时触发，均一律不写）。
- Ticketmaster 官方页里"绝不会要你买礼品卡来退款"一条已在 007 用过，本篇不复用。

FACT-AUDIT-STATUS: RED=0 CHECKED=15 SOURCES-CITED=15

## 渲染状态

- 模板: `cards/017/index.html`（复制自 `cards/001/index.html`，保留 `data-theme="aushow"`
  主题色 token、字体栈与 `.ticket`/`.ledger`/`issue-strip` 组件样式，仅替换 5 个
  `<section class="poster xhs">` 区块内的文案）
- 张数: 5 张（xhs-01 ~ xhs-05），均 1080×1440
- 本篇不含 `.ticket` 票根卡（无单场演出可放）与任何 `<img>`（防骗选题不挂演出海报）
- 渲染: 由 `run_daily_xhs.sh` 在本次会话结束后调用 `automation/render_card.py` 完成
  （headless Chrome 逐张截图），本次会话按提示词第 0 步要求**未调用任何截图工具**
