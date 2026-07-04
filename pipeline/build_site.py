#!/usr/bin/env python3
"""从 data/events.json 生成 site/index.html(单文件,零依赖)

用法: python3 pipeline/build_site.py
"""
import html
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "index.html"

# 留言板(Cusdis匿名评论)。到 https://cusdis.com 免费注册建站后,把 App ID 填到这里重新build即可开启
CUSDIS_APP_ID = "d140ace5-62f1-4d69-bee8-5efe86b9324a"
SITE_URL = "https://michaelxu0814-ai.github.io/AuShow-Radar"  # 部署后改成真实域名(Cusdis回链用)

STATUS = {
    "on_sale": ("在售", "s-onsale"),
    "announced": ("已官宣", "s-announced"),
    "tbc": ("待核实", "s-tbc"),
}
MONTH_NAMES = ["一月", "二月", "三月", "四月", "五月", "六月",
               "七月", "八月", "九月", "十月", "十一月", "十二月"]


def esc(v):
    return html.escape(str(v)) if v else ""


def card(e):
    st_label, st_cls = STATUS.get(e.get("status"), STATUS["tbc"])
    cat = e.get("category") or "其他"
    city = e.get("city") or "其他"

    if e.get("date"):
        d = date.fromisoformat(e["date"])
        when = f"{d.month}月{d.day}日 {'周' + '一二三四五六日'[d.weekday()]}"
        if e.get("time"):
            when += f" · {esc(e['time'])}"
    elif e.get("recurrence"):
        when = esc(e["recurrence"]) + (f" · {esc(e['time'])}" if e.get("time") else "")
    else:
        when = "日期待公布"

    meta = []
    if e.get("venue"):
        meta.append(f'<span class="m">📍 {esc(e["venue"])} · {esc(city)}</span>')
    else:
        meta.append(f'<span class="m">📍 {esc(city)} · 场馆待公布</span>')
    if e.get("price"):
        meta.append(f'<span class="m">🎫 {esc(e["price"])}</span>')
    if e.get("ticket_platform"):
        meta.append(f'<span class="m">🏛 {esc(e["ticket_platform"])}</span>')

    main_url = e.get("ticket_url") or e.get("source_url")
    links = []
    if e.get("ticket_url"):
        links.append(f'<a class="buy" href="{esc(e["ticket_url"])}" target="_blank" rel="noopener">购票 ↗</a>')
    elif e.get("source_url"):
        links.append(f'<a class="buy" href="{esc(e["source_url"])}" target="_blank" rel="noopener">详情 ↗</a>')
    if e.get("ticket_url") and e.get("source_url"):
        links.append(f'<a class="src" href="{esc(e["source_url"])}" target="_blank" rel="noopener">信源</a>')
    unverified = '' if e.get("verified") else '<span class="unv">ⓘ 信息待人工核实</span>'

    glyph = (e.get("category") or "演")[0]
    img = (f'<img src="{esc(e["image"])}" alt="{esc(e.get("title_zh"))}" loading="lazy" '
           f'referrerpolicy="no-referrer" onerror="this.remove()">') if e.get("image") else ''
    title = esc(e.get("title_zh") or e.get("title_en"))
    if main_url:
        title = f'<a href="{esc(main_url)}" target="_blank" rel="noopener">{title}</a>'

    return f'''<article class="card" data-city="{esc(city)}" data-cat="{esc(cat)}">
  <div class="art"><span class="ph">{glyph}</span>{img}</div>
  <div class="body">
  <div class="stub"><span class="when">{when}</span><span class="badge {st_cls}">{st_label}</span></div>
  <h3>{title}</h3>
  {f'<p class="en">{esc(e.get("title_en"))}</p>' if e.get("title_en") else ''}
  <div class="meta">{''.join(meta)}</div>
  <div class="foot">{''.join(links)}{unverified}</div>
  </div>
</article>'''


def main():
    db = json.loads((ROOT / "data" / "events.json").read_text())
    events = db["events"]
    today = date.today().isoformat()

    dated = sorted([e for e in events if e.get("date") and e["date"] >= today],
                   key=lambda e: e["date"])
    undated = [e for e in events if not e.get("date")]

    sections = []
    cur = None
    for e in dated:
        d = date.fromisoformat(e["date"])
        key = (d.year, d.month)
        if key != cur:
            if cur is not None:
                sections.append("</div></section>")
            sections.append(f'<section><h2><em>{d.year}</em>{MONTH_NAMES[d.month - 1]}</h2><div class="grid">')
            cur = key
        sections.append(card(e))
    if cur is not None:
        sections.append("</div></section>")
    if undated:
        sections.append('<section><h2><em>常驻</em>&amp;待定</h2><div class="grid">')
        sections.extend(card(e) for e in undated)
        sections.append("</div></section>")

    cities = ["全部"] + sorted({e.get("city") or "其他" for e in events})
    cats = ["全部"] + sorted({e.get("category") or "其他" for e in events})
    chips_city = "".join(f'<button class="chip{" on" if c == "全部" else ""}" data-f="city" data-v="{esc(c)}">{esc(c)}</button>' for c in cities)
    chips_cat = "".join(f'<button class="chip{" on" if c == "全部" else ""}" data-f="cat" data-v="{esc(c)}">{esc(c)}</button>' for c in cats)

    if CUSDIS_APP_ID:
        comments = (f'<div id="cusdis_thread" data-host="https://cusdis.com" '
                    f'data-app-id="{CUSDIS_APP_ID}" data-page-id="aushow-board" '
                    f'data-page-url="{SITE_URL}" data-page-title="澳华演出雷达留言板"></div>\n'
                    f'<script async defer src="https://cusdis.com/js/cusdis.es.js"></script>')
    else:
        comments = ('<div style="border:2px dashed var(--line);border-radius:10px;padding:16px 18px;'
                    'font-size:13px;color:var(--tan)">💬 留言板筹备中 —— 有演出情报或购票踩坑经历,'
                    '先通过页脚小红书账号私信投稿。</div>')

    page = TEMPLATE.replace("__CHIPS_CITY__", chips_city) \
                   .replace("__CHIPS_CAT__", chips_cat) \
                   .replace("__SECTIONS__", "\n".join(sections)) \
                   .replace("__COMMENTS__", comments) \
                   .replace("__UPDATED__", db.get("updated", today)) \
                   .replace("__COUNT__", str(len(dated) + len(undated)))
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(page)
    print(f"built {OUT} ({len(dated)} dated + {len(undated)} undated events)")


TEMPLATE = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>澳华演出雷达 · 澳洲华语演出日历 | AuShow Radar</title>
<meta name="description" content="悉尼、墨尔本华语演出全览:演唱会、脱口秀、开放麦、音乐会、见面会。只列官方购票渠道,拒绝黄牛。">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@600;900&display=swap" rel="stylesheet">
<style>
:root{
  --paper:#F6F1E6; --ink:#1C1712; --red:#D6402B; --red-dk:#A82C1C;
  --tan:#8C7B62; --line:#D8CDB8; --card:#FFFDF7;
}
*{margin:0;padding:0;box-sizing:border-box}
body{
  background:var(--paper); color:var(--ink);
  font-family:-apple-system,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
  background-image:radial-gradient(rgba(140,123,98,.10) 1px,transparent 1px);
  background-size:22px 22px;
}
.wrap{max-width:680px;margin:0 auto;padding:0 18px 60px}
header{padding:44px 0 10px;border-bottom:3px solid var(--ink);position:relative}
.kicker{display:inline-block;background:var(--ink);color:var(--paper);font-size:11px;
  letter-spacing:.35em;padding:4px 10px 4px 13px;margin-bottom:14px}
h1{font-family:"Noto Serif SC",serif;font-weight:900;font-size:clamp(34px,9vw,52px);line-height:1.1}
h1 .accent{color:var(--red)}
.tagline{margin:10px 0 4px;color:var(--tan);font-size:14px}
.tagline b{color:var(--red-dk)}
.stamp{position:absolute;right:0;top:48px;transform:rotate(8deg);border:2px solid var(--red);
  color:var(--red);font-family:"Noto Serif SC",serif;font-weight:900;font-size:12px;
  padding:5px 9px;border-radius:4px;opacity:.85}
.filters{padding:16px 0 6px;border-bottom:1px dashed var(--line)}
.frow{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:8px}
.flabel{font-size:11px;letter-spacing:.2em;color:var(--tan);min-width:3.5em}
.chip{border:1.5px solid var(--ink);background:transparent;color:var(--ink);font-size:13px;
  padding:5px 14px;border-radius:999px;cursor:pointer;transition:all .15s}
.chip.on{background:var(--ink);color:var(--paper)}
.chip:hover{border-color:var(--red);color:var(--red)}
.chip.on:hover{background:var(--red);border-color:var(--red);color:var(--paper)}
section{margin-top:34px}
h2{font-family:"Noto Serif SC",serif;font-weight:900;font-size:26px;display:flex;
  align-items:baseline;gap:10px;margin-bottom:16px}
h2 em{font-style:normal;font-size:13px;color:var(--red);letter-spacing:.15em;
  border:1.5px solid var(--red);padding:2px 8px;border-radius:3px}
h2::after{content:"";flex:1;border-bottom:2px solid var(--ink);margin-left:6px}
.grid{display:grid;gap:16px}
.card{background:var(--card);border:1.5px solid var(--ink);border-radius:10px;
  padding:0;overflow:hidden;position:relative;
  box-shadow:4px 4px 0 rgba(28,23,18,.16);transition:transform .15s,box-shadow .15s}
.card:hover{transform:translate(-2px,-2px);box-shadow:7px 7px 0 rgba(214,64,43,.25)}
.card .body{padding:0 18px 14px}
.art{position:relative;aspect-ratio:2.3/1;overflow:hidden;
  background:linear-gradient(130deg,var(--red-dk) 0%,var(--red) 58%,#E58A5B 100%);
  border-bottom:1.5px solid var(--ink)}
.art .ph{position:absolute;right:10px;bottom:-18px;font-family:"Noto Serif SC",serif;
  font-weight:900;font-size:92px;line-height:1;color:rgba(246,241,230,.28);
  transform:rotate(-6deg);user-select:none}
.art img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.card h3 a{color:inherit;text-decoration:none}
.card h3 a:hover{color:var(--red)}
.stub{display:flex;justify-content:space-between;align-items:center;
  border-bottom:2px dashed var(--line);padding:12px 0 10px;margin-bottom:12px;position:relative}
.stub::before,.stub::after{content:"";position:absolute;bottom:-8px;width:16px;height:16px;
  border-radius:50%;background:var(--paper);border:1.5px solid var(--ink)}
.stub::before{left:-27px}.stub::after{right:-27px}
.when{font-family:"Noto Serif SC",serif;font-weight:900;font-size:15px;color:var(--red-dk)}
.badge{font-size:11px;letter-spacing:.15em;padding:3px 9px;border-radius:3px;font-weight:600}
.s-onsale{background:var(--red);color:#fff}
.s-announced{border:1.5px solid var(--ink);color:var(--ink)}
.s-tbc{border:1.5px dashed var(--tan);color:var(--tan)}
.card h3{font-family:"Noto Serif SC",serif;font-weight:900;font-size:19px;line-height:1.35}
.en{color:var(--tan);font-size:12px;margin-top:3px;letter-spacing:.02em}
.meta{display:flex;flex-direction:column;gap:4px;margin:10px 0 12px;font-size:13.5px;color:#4a4238}
.foot{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.buy{background:var(--ink);color:var(--paper);text-decoration:none;font-size:13px;
  font-weight:600;padding:7px 18px;border-radius:999px;transition:background .15s}
.buy:hover{background:var(--red)}
.src{color:var(--tan);font-size:12px;text-decoration:underline dotted}
.unv{font-size:11px;color:var(--red-dk);margin-left:auto}
.notice{margin-top:40px;border:2px solid var(--red);border-radius:10px;padding:16px 18px;
  background:rgba(214,64,43,.05)}
.notice h4{font-family:"Noto Serif SC",serif;color:var(--red-dk);font-size:15px;margin-bottom:6px}
.notice p{font-size:13px;line-height:1.7}
footer{margin-top:44px;border-top:3px solid var(--ink);padding-top:16px;
  font-size:12px;color:var(--tan);line-height:2}
footer a{color:var(--red-dk)}
.hidden{display:none}
@media(min-width:560px){.grid{grid-template-columns:1fr 1fr}}
</style>
</head>
<body>
<div class="wrap">
<header>
  <span class="kicker">AUSHOW RADAR</span>
  <h1>澳华<span class="accent">演出</span>雷达</h1>
  <p class="tagline">悉尼 · 墨尔本华语演出全览 —— 演唱会 / 脱口秀 / 音乐会 / 见面会。<b>只列官方渠道,拒绝黄牛。</b></p>
  <span class="stamp">已收录 __COUNT__ 场</span>
</header>

<div class="filters">
  <div class="frow"><span class="flabel">城市</span>__CHIPS_CITY__</div>
  <div class="frow"><span class="flabel">类型</span>__CHIPS_CAT__</div>
</div>

__SECTIONS__

<section id="board">
  <h2><em>留言板</em>情报征集</h2>
  <p style="font-size:13px;color:var(--tan);margin-bottom:12px">发现新演出?被黄牛坑过?想看谁来澳洲?留个言。</p>
  __COMMENTS__
</section>

<div class="notice">
  <h4>⚠ 防骗提示</h4>
  <p>本站只收录官方售票渠道。微信群 / 小红书私聊转票诈骗高发(中国驻墨尔本总领馆已发布专门提醒),任何"低价转让""内部渠道"要求直接转账的,一律不要相信。二手票请只走带担保的正规平台。</p>
</div>

<footer>
  <p>📮 想要"官宣即提醒"?订阅功能筹备中 —— 先关注小红书 @澳华演出雷达(占位)</p>
  <p>数据更新于 __UPDATED__ · 信息以主办方官方渠道为准 · 本站不售票、不转票</p>
</footer>
</div>

<script>
const state={city:"全部",cat:"全部"};
document.querySelectorAll(".chip").forEach(ch=>ch.addEventListener("click",()=>{
  const f=ch.dataset.f;state[f]=ch.dataset.v;
  document.querySelectorAll(`.chip[data-f="${f}"]`).forEach(c=>c.classList.toggle("on",c===ch));
  document.querySelectorAll(".card").forEach(card=>{
    const ok=(state.city==="全部"||card.dataset.city===state.city)&&(state.cat==="全部"||card.dataset.cat===state.cat);
    card.classList.toggle("hidden",!ok);
  });
  document.querySelectorAll("section").forEach(s=>{
    if(!s.querySelector(".card"))return; // 留言板等非卡片区块不参与筛选
    s.classList.toggle("hidden",!s.querySelector(".card:not(.hidden)"));
  });
}));
</script>
</body>
</html>
'''

if __name__ == "__main__":
    main()
