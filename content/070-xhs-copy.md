# 070 — 你以为在平台买，其实不算（转票防骗指南）

**选题类型**：转票防骗指南（周二轮换位）
**信源条目**：不依赖 `data/events.json`——本篇只讲**模式**，全篇**零处**引用任何单场演出的
日期／场馆／票价／平台／主办方，连 051 那样的 `notes` 字段举例也不做，因此不消耗 verified 池。

**与 19 篇前作的差异（避免同选题重复）**：003/007/012/013/017/019/024/026/031/033/039/
044/046/051/052/056/057/062/068 十九篇，问的全部是**关于这笔交易内部的问题**——对方是谁
（003／013／039）、票是什么（026／046／051／056／062）、页面真不真（007／031）、价格合不合法
（033／044）、钱从哪条通道走（052）、钱怎么追回（012／024）、账号安不安全（017）、
对方真正要的是什么（057）、演出之后谁有退款资格（068）。

本篇第一次问**这笔交易在平台条款里算不算一笔交易**：你在某个二手平台上看到这张票、
在站内私信里谈成、当面交钱拿码——**从平台保障条款的角度看，这一笔从来没有发生过。**
保障的开关不是"我在哪看到这张票"，而是"这笔钱有没有走平台结账"。

- **与 052 的边界（最关键的一条）**：052 写的是**支付通道**——刷卡／PayPal 选哪个选项／
  银行转账／礼品卡，四条通道追回机制不同，主体是**支付机构**，且引用的是 **PayPal 自家的
  Buyer Protection**（Goods and Services vs Friends and Family）。本篇主体是**成交平台**，
  引用的是 **Meta 的 Marketplace Purchase Protection**——052 **零处**引用过这份政策
  （本次会话 grep 全部 69 篇确认）。本篇**主动不写**任何支付通道的追回机制、不写
  chargeback、不复述 PayPal 的 G&S／F&F，整条留给 052。
- **与 013 的边界**：013 写过"私聊转微信、转 WhatsApp 的那一步，就是证据开始消失的那一步"，
  落点是**举证**。本篇落点是**资格**——不是"你拿不出证据"，是"条款上这笔订单不存在，
  连可以申请的东西都没有"。本篇不展开证据保全。
- **与 007 的边界**：007 教你查假售票网站的页面与域名。本篇引用 Scamwatch 2026-11-03 的
  原话——**外观本身已经越来越不可靠**——把判据从"页面像不像真的"移到"这笔钱走在哪条轨道上"。
- **与 003／019 的边界**：003 写过"票款付完又冒出改名费／手续费"这套追加收费，019 写过
  "出票费／邮费／改名费"。本次信源里虽然也出现了 transfer／authorisation／name-change fees
  这组名目，但该事实**已被 003 占用**，本篇**主动完全不写**，避免事实重叠。
- **与 057 的边界**：057 写"对方要的是你的证件"。本次信源里关于卖家被钓取银行凭证／身份
  文件的那一段（Vinted 一节）**主动完全不写**，整条留给 057。

**红线自查**：全篇不点名任何具体个人、账号、群组或卖家，只讲模式。文中出现的
Facebook Marketplace／Messenger／TikTok／WhatsApp，均为 **Meta 自家政策文本与 Scamwatch
官方通报原文中出现的渠道名称**，用于说明条款适用范围与官方统计口径，**不构成对任何平台
或任何账号的点名批评**。不写任何演出的日期／场馆／票价／主办方。

**本篇主动声明的局限（写进正文，不藏）**：
① **Purchase Protection 是 Facebook Marketplace 自家的政策，我不把它推广成"所有二手平台
   都这样"。** 别的平台各有各的条款，本篇不替它们发言，读者要看自己用的那个平台怎么写。
② **"走平台结账就一定安全"不是本篇结论。** Meta 原话是"**许多**（many）走发货或结账的
   购买受覆盖"，不是全部；并且善意退款（goodwill refunds）明写由平台自行裁量。
③ **58.7% 的口径必须讲清**：它是"买卖类诈骗占**所有涉及资金损失的报告数**的比例"，
   **不是**"58.7% 的二手交易是骗局"。本篇正文按原口径写。
④ **"同一张票，走结账和当面转账是两个商品"** 是我的编辑判断，**不是官方原话**，正文标明。

## 标题（12字）

你以为在平台买，其实不算

## 正文（发帖文案，无外链）

防骗写到第二十篇了。

回头看前十九篇，它们问的其实都是**同一类问题**：这个人诚不诚实、这张票能不能转、
价格合不合法、钱从哪条通道走、票现在存不存在、演出之后退款归谁。

全都是**在这笔交易里面**找答案。

今天这篇换一个方向。它不问人，也不问票，它问的是——

**你这一笔，在平台的条款里，算不算一笔交易？**

先说结论：**你在哪看到这张票，和你在哪买了这张票，是两回事。** 而平台保障认的是后者。

**① 先看 Meta 自己怎么划这条线。**

Facebook Marketplace 的买家保障叫 Purchase Protection。它的帮助中心原话是：

**走发货或平台结账的"许多"购买，受 Purchase Protection 政策覆盖。**

紧接着的下一句，是今天最该被抄下来的一句：

**通过第三方网站、当面自提、Messenger 交易、或者其他消息服务完成的购买，不符合
Purchase Protection 的资格。**

读一遍就知道这句话覆盖掉了什么——**转票几乎全在这句话里面。**

站内私信里谈好的、约在场馆门口当面交钱的、加个微信私下转账的，不管你是在哪个平台
刷到这条信息的，在条款上，这些**都不是"在平台买的"**。

**② 保障到底保什么，也值得你读一遍。**

同一页写明，Purchase Protection 是**免费**的，**自动**覆盖符合条件的订单。
你可以在这几种情况下申请退款：

- 你**没有收到**订单；
- 货到了但**损坏**，或者**和列表描述不一致**；
- 卖家**没有遵守他自己声明的退款政策**；
- 这笔购买是**未经授权**的；
- 卖家**已被 Facebook 移除**。

看出共同点了吗——**这五条全都长在"一笔订单"上面。**

没有订单号、没有列表、没有平台结账记录的那一笔，不是"申请起来比较难"，
而是**五条里一条都挂不上去**。平台审核索赔时会看什么，它也写了：**订单详情（含物流
追踪信息）、列表描述、你和卖家之间的消息、以及支撑文件。** 审核批准的话，退的是
**全额货款加运费**；另外它明写，善意退款由平台**自行裁量**。

所以"我在平台上买的，平台会管"这个安全感，**挂钩的不是平台，是结账那一步**。

**③ 那"他看起来很正规"还能不能当判据？**

这是我这次最想更新的一条。

Scamwatch 在 **2026 年 11 月 3 日**那份通报里，用了很重的话讲这件事：AI 正在让购物类
诈骗变得**更便宜、更快、更可信**——骗子用它生成商品图、做出精致的网站、编出关于商品
和卖家的完整故事，再配上复制来的商号、logo 和各种身份细节。

然后是官方自己写下的这一句：

**随着 AI 发展，"外观"本身，正在变成一个越来越不可靠的判断依据。**

这句话的分量在于：前面十九篇里，有好几篇教你的就是**看外观**——查域名、查页面、
查原价有没有写。那些仍然有用，但官方现在亲口说了，**别把"看起来正规"当成结论**。

判据得往后退一步，退到那个不随外观变化的地方：**这笔钱，走的是哪条轨道。**

**④ 顺便给你两个数，知道这事有多常见。**

同一份通报里，国家反诈中心的统计：**2026 年 1 月到 9 月，买卖类诈骗占了 Scamwatch
全部"涉及资金损失"报告的 58.7%**——**11,537 人**报告了损失，总额 **1720 万澳元**
（比 2025 年同期还降了 16.3%）。

口径我说清楚：这个 58.7% 是**占有损失的报告数**的比例，**不是说 58.7% 的二手交易是骗局**。

而**演出票**，就是这份通报点名的场景之一：报告里的人是**通过 Facebook 和 TikTok**
被接触上的。另外，光是 2026 年，官方已经成功下架了 **20,353 个**诈骗网站。

**所以这篇给你三个动作，全都在付钱之前。**

**① 先把"看到"和"买到"分开问一次。** 这张票我是在哪刷到的——和这笔钱会怎么走出去，
是两个问题。如果钱不经过平台结账，那就坦白承认：**这是一笔平台条款上不存在的交易。**
不存在不代表一定会被骗，但它代表**出事之后没有那条救济通道**，这件事最好是你提前知道，
而不是出事那天才知道。

**② 把"有没有保障"算进价格里。** 同一张票，走平台结账和当面转账，在我看来其实是
**两个不同的商品**：一个带救济，一个不带。（这句是我的判断，**不是官方原话**。）
所以如果一笔转票便宜了几十块，但代价是整条保障通道——这个账，你自己算。

**③ 别再拿"他看起来很正规"说服自己。** 这不是我多疑，**是 Scamwatch 自己写的**：
外观已经不再可靠。它给的办法也很朴素——**自己独立去访问官方网站，而不是顺着别人
发来的消息或广告点进去。**

最后抄一句官方的原话，这句我特别想让你看见。

Scamwatch 在那份通报结尾写：**被骗，不是消费者没能看出危险信号的失败；它是骗子的
欺骗能力随技术变强的证据。**

所以万一真中过招，别先骂自己。先去做该做的事，然后把这篇转给还没中招的那个朋友。

这个号为什么宁可一周少发几条，也只发自己能对上官方来源的场次——因为这些事的共同点
都是：**你以为自己在一个有人管的地方，其实条款上那地方不包括你站的位置。**

想要我把"开票就提醒你"这件事做了的，评论区扣 1，私信发你这份"**付钱前先问走哪条轨道**"
自查卡，还有后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出。

#澳洲华人 #演唱会 #转票 #防骗 #买票避坑 #留学生 #悉尼演唱会 #墨尔本演唱会 #布里斯班

## 卡片文案结构（4张，票根美学）

> 张数说明：防骗类按 prompt 可精简到 2–3 张，本篇用 4 张，理由与 052／056／057／062／068
> 相同——"Meta 条款的资格边界"和"付钱前能做的三件事"是两块各自饱满的内容，拆开比塞进
> 一张清楚；封面与 CTA 为账号固定结构。无空卡、无凑数卡。P1 不配图（防骗类不绑定任何
> 单场演出视觉）。

**P1 封面**
- issue-row: AuShow · 澳华演出雷达
- kicker: 防骗指南 · 平台保障资格篇
- 大字标题: 你以为在平台买 / 其实不算
- 副标题: 第二十篇防骗 · 这次不问人，也不问票
- lead: 保障的开关不是你在哪看到这张票，是这笔钱有没有走平台结账。
- 底部条: 只讲模式 不点名 — 依 Meta 与 Scamwatch 官方文本

**P2 Meta 条款原话**
- kicker: Facebook Marketplace · Purchase Protection
- 大字: 这一笔 / 条款上不存在
- ledger 4条:
1. 不符合资格的 — 第三方网站、当面自提、Messenger 交易、其他消息服务完成的购买
2. 符合资格的 — 走发货或平台结账的"许多"购买；免费、自动覆盖符合条件的订单
3. 保障保什么 — 没收到货／与列表描述不符／卖家不守自己的退款政策／未授权购买／卖家被平台移除
4. 审核看什么 — 订单详情与物流追踪、列表描述、你与卖家的消息、支撑文件
- 收尾: 这五条全都长在"一笔订单"上——没有订单的那一笔，不是难申请，是一条都挂不上。
- 底部条: 原话为"许多"非全部 — 善意退款由平台自行裁量
- 备注: 仅为 Facebook Marketplace 自家政策，不推广为所有二手平台通则

**P3 付钱前的 3 件事**
- kicker: 付钱之前 · 做这 3 件事
- 大字: 先问 / 走哪条轨道
- ledger 3条:
1. 把"看到"和"买到"分开问 — 钱不经过平台结账，就是一笔条款上不存在的交易
2. 把"有没有保障"算进价格 — 走结账和当面转账，是两个商品（此为本号判断，非官方原话）
3. 别拿"看起来正规"说服自己 — Scamwatch 原话：外观已越来越不可靠；自己独立访问官网
- 收尾: 2026 年 1–9 月，买卖类诈骗占 Scamwatch 全部"有损失"报告的 58.7%；演出票是其点名场景之一。
- 底部条: 口径是占有损失报告数 — 不是 58.7% 的交易是骗局
- 备注: 11,537 人报告损失、合计 1720 万澳元，同比降 16.3%

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 被骗 / 不是你蠢
- 正文: 评论区扣 1，私信发你这份"付钱前先问走哪条轨道"自查卡，还有后续开票提醒。
- 底部条: VOL. 070 — 简介里有完整演出日历

## 事实核查表

> 全部 20 条均为**一手官方页面**（Meta 帮助中心 / Scamwatch·ACCC 国家反诈中心），
> 2026-11-17 本次会话经 Firecrawl scrape 以 `maxAge:0`（强制实时抓取，不走缓存）取得，
> 两个页面均 **HTTP 200**，引文为页面正文逐字翻译。本篇不含任何 `events.json` 字段断言，
> 不含任何演出的日期／场馆／票价／平台／主办方。
>
> 信源 A＝`https://www.messenger.com/help/messenger-app/228307904608701`
> （《How Purchase Protection works on Facebook Marketplace》，Meta 自家帮助中心；
> **全部 69 篇前作零次引用**，本次会话 grep `Purchase Protection`／`Marketplace`／
> `messenger.com` 全目录确认——052 引用过的是 **PayPal** 自家的 Buyer Protection，
> 与本政策是两家不同主体的两份不同文件）
> 信源 B＝`https://www.scamwatch.gov.au/about-us/news-and-alerts/media-update-when-the-shopfront-is-a-scam`
> （《Media update: When the shopfront is a scam》，发布日 **2026-11-03**，距本篇 14 天；
> **全部 69 篇前作零次引用**——该页发布于 068 生成日 2026-11-01 之后，069 为场馆攻略）

| # | 断言 | 判定 | 依据 |
|---|---|---|---|
| 1 | 走发货或平台结账的"许多"购买受 Purchase Protection 政策覆盖 | GREEN | 信源 A 原文 "Many purchases made with shipping or checkout on Facebook Marketplace are covered by our Purchase Protection Policies." |
| 2 | 第三方网站、当面自提、Messenger 交易、其他消息服务完成的购买**不符合资格** | GREEN | 信源 A 原文 "Purchases made through third-party sites, local pickups, Messenger transactions, or through other messaging services don't qualify for Purchase Protection." |
| 3 | Purchase Protection 免费，且自动覆盖符合条件的订单 | GREEN | 信源 A 原文 "Purchase Protection is free, and automatically covers eligible orders purchased with shipping or checkout on Facebook Marketplace." |
| 4 | 覆盖情形：没有收到订单 | GREEN | 信源 A 原文 "You didn't receive your order." |
| 5 | 覆盖情形：到货损坏或与列表描述不一致 | GREEN | 信源 A 原文 "The product arrived damaged or different than described on the listing" |
| 6 | 覆盖情形：卖家未遵守其声明的退款政策 | GREEN | 信源 A 原文 "The seller didn't follow their stated refund policy." |
| 7 | 覆盖情形：该笔购买未经授权 | GREEN | 信源 A 原文 "The purchase was unauthorized." |
| 8 | 覆盖情形：卖家已被 Facebook 移除 | GREEN | 信源 A 原文 "The seller has been removed from Facebook." |
| 9 | 审核索赔时会查看订单详情（含物流追踪）、列表描述、买卖双方消息、支撑文件 | GREEN | 信源 A 原文 "Facebook may review order details, including tracking information and listing description, messages sent between you and the seller, and supporting documents." |
| 10 | 善意退款由 Facebook 自行裁量 | GREEN | 信源 A 原文 "Goodwill refunds are at Facebook's discretion." |
| 11 | 索赔获批后退还全额货款与运费 | GREEN | 信源 A 原文 "you'll get a refund for the full purchase price of the product and any shipping costs" |
| 12 | 2026 年 1–9 月，买卖类诈骗占 Scamwatch 全部"涉及资金损失"报告的 58.7% | GREEN | 信源 B 原文 "buying and selling scams accounted for 58.7% of Scamwatch reports involving a financial loss in the first nine months of 2026" |
| 13 | 11,537 人报告买卖类诈骗损失；2026 年 1–9 月总额 1720 万澳元，同比降 16.3% | GREEN | 信源 B 原文 "11,537 people reported a loss to these scams. Total losses to buying in selling scams in 2026 (Jan – Sep) was $17.2 million, down 16.3% from the same period in 2025." |
| 14 | 演出票为该通报点名场景之一，报告人**通过 Facebook 与 TikTok**被接触 | GREEN | 信源 B 原文 "Fake concert-ticket offers exploited demand… People reported being approached through Facebook and TikTok" |
| 15 | AI 正让购物类诈骗更便宜、更快、更可信（生成商品图、做精致网站、编造卖家故事） | GREEN | 信源 B 原文 "Artificial intelligence is making shopping scams cheaper, faster and more convincing. Scammers use AI to generate product images, build polished websites and craft compelling stories about products and sellers." |
| 16 | 随 AI 发展，"外观"本身正变成越来越不可靠的判断依据 | GREEN | 信源 B 原文 "As AI advances, appearance alone becomes an increasingly unreliable way to gauge if something is a scam." |
| 17 | 被骗不是消费者没看出危险信号的失败，而是骗子欺骗能力随技术变强的证据 | GREEN | 信源 B 原文 "Being scammed is not evidence of consumers' failure to miss red flags; it's evidence of scammers' increasing powers of deception owed to advances in technology." |
| 18 | 2026 年至今官方已成功下架 20,353 个诈骗网站 | GREEN | 信源 B 原文 "the National Anti-Scam Centre has recorded 20,353 successful takedowns of scam websites" |
| 19 | 官方建议：独立访问零售商网站，而不是顺着未经请求的消息或广告点进去 | GREEN | 信源 B 原文（STOP 段）"Visit a retailer's website independently rather than following an unsolicited message or advertisement." |
| 20 | 自述"前十九篇防骗无一篇以'平台保障资格'为主线"、且两个信源前作零引用 | GREEN | `automation/posted-log.md` 中 003/007/012/013/017/019/024/026/031/033/039/044/046/051/052/056/057/062/068 十九行本次会话逐条读取；并对 `content/*.md` 全目录 grep `Purchase Protection`／`Marketplace`／`messenger.com`／`shopfront`／`58.7`／`WhatsApp` 验证 |

FACT-AUDIT-STATUS: RED=0 CHECKED=20 SOURCES-CITED=20

**主动剔除、未写进文案的内容**：

1. **transfer／authorisation／name-change fees（转让费／授权费／改名费）** —— 信源 B
   的演出票一段确实写了骗子索要这组费用，但"追加改名费／手续费"这一事实**已由 003
   占用**（003 引 Scamwatch 页面写过同一套追加收费），019 亦写过"出票费／邮费／改名费"。
   为保持事实边界清晰，**整组名目主动不写**。
2. **Vinted 卖家被钓取银行凭证／安全码／身份文件那一整段**（含 $1,800 被盗、
   chatbot 诱导输入多个账户）—— 身份与凭证线**已由 057 占用**（"对方要的是你的证件"），
   钓鱼链接线由 007／031 占用，**整段不写**。
3. **"conversations often moving to WhatsApp"** —— 该迁移动作**已由 013 以"证据开始消失
   的那一步"写过**。本篇只写信源 B 的"通过 Facebook 和 TikTok 被接触"这半句（接触渠道，
   属 2026 新统计），**不重复迁移—举证那条线**。
4. **假车辆销售网站一整段**（澳洲地址／电话／ABN／全国配送的假店面）—— 与演出票受众无关，
   且"假网站"主线属 007，不写。
5. **PayPal 的 Goods and Services／Friends and Family、chargeback、ePayments Code
   等支付通道机制** —— 整条属 052，本篇**零处触碰**。
6. **Meta《Purchase Protection Policy》政策全文中的其他除外项**（如金额上限、
   服务类／车辆类商品是否覆盖）—— `facebook.com/policies/purchase_protection` 与
   `facebook.com/help/112050761628033` 两次抓取**均未取得正文**（前者返回空白，后者
   显示 "This Page Isn't Available"）。帮助页底部那段"不覆盖 local pickups、peer-to-peer
   payments、services、vehicles、2000 USD/GBP 以上订单"的文字**由 Meta AI 助手生成**，
   非政策原文，**判定为无法逐字确证，一律不写**，正文只用帮助页正文已明确写出的资格边界。
7. **"票类商品是否被 Purchase Protection 列为不覆盖品类"** —— 首轮 WebSearch 有多个
   第三方博客称"tickets 属不覆盖品类"及"Meta 商务政策把演出票列为受限内容"，
   **均未能在 Meta 自家页面取得原文确证**，判定为**无法验证**，整句剔除，不以任何形式
   进入正文或卡片。
8. **任何具体群组、卖家、代抢渠道或个人** —— 按账号红线，全篇只讲模式。

## 渲染状态

- 模板: `cards/070/index.html`（复制 `cards/068/index.html`——该文件与 `cards/001/index.html`
  逐字相同，仅 `<title>` 与四个 `<section class="poster xhs">` 内文案不同，本次会话 diff 确认；
  保留 `<html data-theme="aushow">`、文件顶部全部主题色 token、整体 CSS 结构、字体，
  以及 `.ticket`／`.ledger`／`issue-strip` 等已验证组件样式，仅替换 4 个 poster 区块内的文案）
- 4 张卡，`id` 为 `xhs-01`…`xhs-04` 连续编号；本篇不使用演出海报配图（P1 无
  `figure.frame-img`），与全部 19 篇防骗前作同一处理
- 输出: 由 `automation/render_card.py` 在本次会话结束后渲染为
  `cards/070/output/xhs-070-01.png` ~ `xhs-070-04.png`，均 1080×1440
- 渲染不在本次对话内进行（2026-08-16 起的既定分工：chrome-devtools-mcp 截图不可靠，
  渲染交由确定性脚本 `render_card.py` 完成）
