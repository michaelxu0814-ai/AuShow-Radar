# STATE — 澳华演出雷达 AuShow Radar

> 每次会话开场先读本文件 + 跑 `./status.sh`。技术结构与运维手册见 README.md。

最后更新：2026-07-08

## 部署事实（已验证）

- 线上 https://aushow.com.au （2026-07-08 核实 HTTP 200；Cloudflare DNS + GitHub Pages，main 分支 /docs）
- 仓库 github.com/michaelxu0814-ai/AuShow-Radar（gh 账号 michaelxu0814-ai，`gh auth setup-git` 已配）
- launchd 每天 09:00 自动跑 run_daily.sh（com.aushow.daily），最近一次自动提交 2026-07-07 ✅
- Cusdis 留言板已上线（评论在 cusdis.com 后台审核）

## 已修复的事故（防复发）

1. **详情页跳错演出**（袁娅维点进去是别的演出）：deep link 修复 + verifier 覆盖 verified 条目（commit 3966ddf）。改 build/parse 后必须抽查 3 条演出的跳转。
2. **GoDaddy 默认页顶掉网站**：DNS 变更后必须 `dig +short aushow.com.au` + curl 真实内容验证，不能只看 HTTP 200。
3. **海报张冠李戴**（BIGBANG 挂袁娅维图）：og:image 多演出页面会错，周审时错图置 `"image": null`。

## 每周人工职责（约 20 分钟，质量闸门）

`grep -n '"verified": false' data/events.json` → 逐条核对 → 改 true 或删。流程细节见 README「每周人工审核」。

## 凭证与限制

- Cloudflare token 曾泄露待轮换（~/Desktop/密钥轮换清单.md）；重建时只给 aushow zone 的 DNS Edit
- 小红书自动化搜索被风控拦（时通时不通），稳定通道是 sources.json 的 exa-xhs-* 源
- Mac 关机时 launchd 不补跑，错过等第二天

## 阶段目标

12 周验证：500 订阅用户，或证伪"发现碎片化"痛点。策略三步走的第一步（聚合发现层 → 主办方工具 → 担保转票）。

## 下一步

1. 上线推广未开始：小红书发帖引流（注意平台外链限制，用评论区/私信策略）
2. 订阅入口（邮件或微信群）尚未建——没有订阅就无法度量 12 周目标
