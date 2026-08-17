# 002 — 周杰伦悉尼站开票中（单场演出安利）

**选题类型**：单场演出安利（周一轮换位）
**信源条目**：`data/events.json` → 周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会（verified=true）

**选题说明**：001 已用掉周杰伦墨尔本站，本篇取同巡演悉尼站（verified 池中未用过、
热度最高、且演出日期在 11 月，不受当前"内容已产出但尚未实际发布"的时间差影响）。
verified 池里日期最近的两条是袁娅维墨尔本 8/20、悉尼 8/22——按当前发布节奏（001 计划
08-24 起手动发布）这两场在发布时已过期，故本次未选用，详见文末备注。

## 标题（13字）

周杰伦悉尼站开票中！别错过

## 正文（发帖文案，无外链）

周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会——📍ENGIE Stadium（Sydney Olympic Park），11月21日晚7:30，Ticketmaster 官方正式开票中。

票价 $188–$748（另加 $9.90 手续费），每账户限购 6 张，主办方 Sky Music & Horizon Production。悉尼这场值得为它跨个城。

想去的姐妹评论区扣1，私信告诉你抢票窍门和后续开票提醒～ 澳华演出雷达帮你盯紧全澳华语演出，不再错过任何一场。

#周杰伦 #悉尼演唱会 #澳洲华人 #演唱会情报

## 卡片文案结构（4张，票根美学）

**P1 封面**
- kicker: 演出情报 · 单场安利
- 大字标题: 周杰伦 / 悉尼站开票了！
- 副标题: 「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会
- 配图: 官方澳洲巡演艺人页头图（Ticketmaster 提供）
- 说明: 11月21日 ENGIE Stadium，官方正式开票中。
- 底部条: 11.21 · SYD — Ticketmaster 开票中

**P2 票根组件**
- 演出: 周杰伦「海洋 悉尼嘉年华Ⅱ」世界巡回演唱会
- 日期: 21 NOV 2026 ｜ 状态徽章: ON SALE 开票中
- 场馆: ENGIE Stadium（悉尼 Sydney Olympic Park）
- 时间: 19:30

**P3 购票须知（ledger 4条）**
1. $188–$748 — 票价区间（另加 $9.90 手续费）
2. Ticketmaster — 官方购票平台
3. 限购 6 张 — 每账户购买上限
4. 官方主办 — Sky Music & Horizon Production
- 收尾: 官方票价是唯一标准——加价转票、来源不明的二手票，风险自己扛。
- 底部条: 信息来自主办方公告 — 购票前建议官网复核

**P4 收尾 CTA**
- kicker: 澳华演出雷达 · 玩转布里斯班
- 大字: 悉尼这场 / 你去不去？
- 正文: 评论区扣 1，私信告诉你怎么抢票，还有后续开票提醒。
- 底部条: VOL. 002 — 简介里有完整演出日历

## 事实核查表

| 断言 | 判定 | 依据 | 备注 |
|---|---|---|---|
| 演出名「周杰伦「海洋 悉尼 嘉年华Ⅱ」世界巡回演唱会」 | GREEN | `data/events.json` events[1].title_zh，该条目 verified=true | 逐字复制 |
| 日期 2026-11-21 / 时间 19:30 | GREEN | 同上 events[1].date / events[1].time | 逐字复制 |
| 场馆 ENGIE Stadium（悉尼 Sydney Olympic Park） | GREEN | 同上 events[1].venue / events[1].city | 逐字复制，venue 括号内 Sydney Olympic Park 亦来自该字段 |
| 票价 $188–$748（+$9.90手续费） | GREEN | 同上 events[1].price | 逐字复制；注意与墨尔本站($208起)不同，未串用 |
| 购票平台 Ticketmaster | GREEN | 同上 events[1].ticket_platform | 逐字复制；表述用"官方购票平台"而非"唯一官方平台"，JSON 未断言排他性 |
| 状态 on_sale（开票中） | GREEN | 同上 events[1].status | 逐字复制 |
| 每账户限购6张 / 主办 Sky Music & Horizon Production | GREEN | 同上 events[1].notes | 逐字复制 |
| 封面图为周杰伦澳洲巡演官方宣传图 | GREEN | 同上 events[1].image（Ticketmaster 官方站资源），2026-08-17 curl 校验返回 HTTP 200 image/jpeg | 该图为巡演艺人页通用头图，文件名含 "Mel"；alt 文案写"澳洲巡演官方宣传图"而非"悉尼站海报"，避免宣称其为悉尼专属物料（对应账号红线"海报张冠李戴"） |
| link_ok=true（购票链接可访问） | GREEN | 同上 events[1].link_ok | 未在正文/卡片放外链，仅用于内部核实 |

未写入任何 events.json 之外的信息：本篇不含入场须知、检票时间、座位视野、开票倒计时等
JSON 无对应字段的内容。

FACT-AUDIT-STATUS: RED=0 CHECKED=9 SOURCES-CITED=9

## 渲染状态

- 模板: `cards/002/index.html`（复制自 001，保留 `data-theme="aushow"` 主题色 token、
  `.ticket`/`.ledger`/`issue-strip` 组件样式与字体，仅替换 4 个 poster 区块内的文案/数据）
- 卡片数: 4 张 `<section class="poster xhs" id="xhs-01…04">`
- 渲染: 交由 `automation/render_card.py`（headless Chrome CLI 逐张截图 + PIL 校验 1080×1440），
  本次会话按 daily-xhs-prompt.md 第0节要求未调用任何浏览器截图工具

## 备注（需用户裁决，不阻塞本篇）

verified 池中袁娅维 TIA RAY「月亮撒野」墨尔本站（8/20）、悉尼站（8/22）两条日期最近，
但若沿用"001 于 08-24 起手动发布"的节奏，这两场在发布时已演完，本次因此跳过。
如果计划在 8/20 前就发布，告诉我一声，可以立刻改产一篇袁娅维的加急安利。
