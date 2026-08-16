# STATE — 澳华演出雷达 AuShow Radar

> 每次会话开场先读本文件 + 跑 `./status.sh`。技术结构与运维手册见 README.md。

最后更新：2026-07-26

## 部署事实（已验证）

- 线上 https://aushow.com.au （2026-07-08 核实 HTTP 200；Cloudflare DNS + GitHub Pages，main 分支 /docs）
- 仓库 github.com/michaelxu0814-ai/AuShow-Radar（gh 账号 michaelxu0814-ai，`gh auth setup-git` 已配）
- launchd 每天 09:00 自动跑 run_daily.sh（com.aushow.daily），最近一次自动提交 2026-07-07 ✅
- Cusdis 留言板已上线（评论在 cusdis.com 后台审核）

## 已修复的事故（防复发）

1. **详情页跳错演出**（袁娅维点进去是别的演出）：deep link 修复 + verifier 覆盖 verified 条目（commit 3966ddf）。改 build/parse 后必须抽查 3 条演出的跳转。
2. **GoDaddy 默认页顶掉网站**：DNS 变更后必须 `dig +short aushow.com.au` + curl 真实内容验证，不能只看 HTTP 200。
3. **海报张冠李戴**（BIGBANG 挂袁娅维图）：og:image 多演出页面会错，周审时错图置 `"image": null`。
4. **push 长期被拒导致12个commit积压未推送**（2026-07-26发现并修复）：gh 全局 active account 常被 AUComplianceAI 那边的 `gh auth switch -u UEXU` 切走，AuShow 这边 push 到 michaelxu0814-ai/AuShow-Radar 就被拒(403)。`run_daily.sh` 的 push 步骤已改为显式用 `gh auth token -u michaelxu0814-ai` 现取token拼URL推送，不再依赖 gh 的全局 active account 状态。已手动补推积压的12个commit并验证新推送方式生效。

## 每周人工职责（约 20 分钟，质量闸门）

`grep -n '"verified": false' data/events.json` → 逐条核对 → 改 true 或删。流程细节见 README「每周人工审核」。

## 凭证与限制

- Cloudflare token 曾泄露待轮换（~/Desktop/密钥轮换清单.md）；重建时只给 aushow zone 的 DNS Edit
- 小红书自动化搜索被风控拦（时通时不通），稳定通道是 sources.json 的 exa-xhs-* 源
- Mac 关机时 launchd 不补跑，错过等第二天

## 阶段目标

12 周验证：500 订阅用户，或证伪"发现碎片化"痛点。策略三步走的第一步（聚合发现层 → 主办方工具 → 担保转票）。

## 小红书内容自动化（2026-08-16 装机）

- 账号：复用老号"玩转布里斯班"（~3000 真实布里斯班华人粉丝），简介加后缀"· 华人演出资讯"，
  不整体改名（详见 `~/.claude/skills/xhs-content/accounts/aushow.md` 的"账号复用说明"）
- 自动化：`run_daily_xhs.sh` + launchd `com.aushow.xhs-daily`，每天 10:15（在主 `run_daily.sh`
  09:00-09:54 抓取窗口之后）跑一次，内容由 `claude -p` 按 `automation/daily-xhs-prompt.md`
  的选题轮换表生成，渲染由确定性脚本 `automation/render_card.py`（headless Chrome CLI + PIL
  裁切）完成——**不用 chrome-devtools-mcp**，2026-08-16 实测那条路径的截图工具反复
  `Page.captureScreenshot` 超时/卡死，不适合无人值守自动化，两个独立 fork 尝试都卡死过
- 选题轮换（防止 verified 演出池子太薄被打空）：周一/五=单场演出安利，周二/日=转票防骗
  指南，周三/六=场馆攻略，周四=本周开票汇总
- 内容不自动发布，只推送 Telegram（bot token 复用 AUComplianceAI 那个，同一收件人，消息前缀
  "🎫 AuShow:" 区分），用户手机审核后自己手动发布小红书，规避风控
- 001 号内容（周杰伦墨尔本站单场安利）已于 2026-08-16 生成、渲染、发送 Telegram（Telegram API
  `"ok":true` 确认送达），等用户发布
- KPI 基线：宪法"首帖起12周500订阅"的500，指复用后净新增订阅，不含账号已有3000基础粉丝

## 下一步

1. ~~上线推广未开始~~ ✅ 内容管道已装机，001号已推送 Telegram 待用户发布
2. 订阅入口（邮件或微信群）尚未建——没有订阅就无法度量 12 周目标
