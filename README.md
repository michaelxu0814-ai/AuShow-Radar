# 澳华演出雷达 AuShow Radar

澳洲华语演出聚合日历(悉尼/墨尔本)。AI 管道自动抓取 → 解析 → 生成静态站。

## 结构

```
sources.json          信息源清单(Exa搜索 / Jina网页 / 小红书)
pipeline/fetch.py     抓取所有源 -> data/raw/<日期>/
pipeline/parse.py     claude CLI 抽取演出条目 -> data/events.json(新条目 verified=false)
pipeline/enrich.py    从购票页/信源页抓 og:image 海报
pipeline/build_site.py 生成 docs/index.html(单文件,零依赖)
run_daily.sh          以上四步串联 + 有git远程时自动push
data/events.json      唯一数据库,可直接手改
```

## 自动化

- launchd 每天 09:00 跑 `run_daily.sh`(配置在 `~/Library/LaunchAgents/com.aushow.daily.plist`)
- 日志: `logs/<日期>.log`;手动跑一次: `./run_daily.sh`
- 停用: `launchctl unload ~/Library/LaunchAgents/com.aushow.daily.plist`
- Mac 关机/睡眠时不会跑;开机后 launchd 不补跑(错过就等第二天)

## 每周人工审核(约20分钟,质量闸门)

1. `grep -n '"verified": false' data/events.json` 逐条打开 source_url 核对日期/场馆/票价,改 `verified: true` 或删除
2. 海报图抽查:信源页若涉及多个演出,og:image 可能张冠李戴(已出过 BIGBANG 挂袁娅维海报的案例),错图置 `"image": null`
3. 已结束的演出会自动不再展示(按日期过滤),不用手删

## 发布(已配置)

- 线上地址: https://aushow.com.au/
- 仓库: https://github.com/michaelxu0814-ai/AuShow-Radar (Pages: main 分支 /docs 目录)
- git 凭证走 `gh auth setup-git`,不依赖 keychain
- 每天 09:00 run_daily.sh 自动 push,Pages 随之自动更新(约1分钟延迟)

## 开启留言板(待办,5分钟)

1. https://cusdis.com 免费注册 → 新建站点 → 拿 App ID
2. 填进 `build_site.py` 顶部 `CUSDIS_APP_ID`,重新 build

## 已知限制

- 小红书直连(opencli):登录态正常(Default profile, web_session 到2027),但小红书风控会拦自动化搜索并伪装成"未登录"错误,时通时不通;管道自动跳过。小红书内容的稳定通道是 exa-xhs-* 源(Exa索引)
- mcporter 的 exa 配置按家目录解析,fetch.py 已固定 cwd,别改
- Eventbrite 直抓被 CAPTCHA 拦,靠 Exa 间接覆盖
