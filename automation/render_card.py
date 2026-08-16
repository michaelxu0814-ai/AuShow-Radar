#!/usr/bin/env python3
"""
确定性渲染:把 guizang 卡片模板(N 个 .poster.xhs section 纵向堆叠)渲染成
每张 1080x1440 的 PNG。

不用 chrome-devtools-mcp/CDP 截图(2026-08-16 实测反复 Page.captureScreenshot
超时,不可靠),改用 headless Chrome CLI + PIL,两步都是确定性命令,不依赖任何
交互式浏览器会话。

**逐张单独截图,不整页堆叠截图再裁切**——根因是种子模板的 `body{padding:64px 32px;
background:#1a1a1a}` 是给多卡片 workbench 预览用的:窗口固定 1080x1440 时,这段
padding 会把 poster 主体向下挤出可视区,顶部露出一截 body 背景色(近黑),底部同时
被裁掉一截。AUComplianceAI 那边 2026-08-16 独立踩过同一个坑,修法是给单卡渲染的
wrapper 手动加 `body{padding:0} .sheet{gap:0}` 覆盖——本脚本把等效覆盖直接做进
`shoot_one()`(注入 CSS 把目标 poster 设为 `position:absolute; top:0; left:0`,
同时显式清零 body/.sheet 间距),不依赖每次记得手动加覆盖样式,也不依赖源文件本身
是否已经修过 body padding。

用法: render_card.py <index.html路径> <输出目录> <文件名前缀>
例:   render_card.py content/cards/005/index.html content/cards/005/output xhs-005
      → 按 index.html 里实际的 <section class="poster xhs"> 数量,自动产出
        xhs-005-01.png, xhs-005-02.png, ... 不需要调用方预先知道卡片张数。
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CARD_W, CARD_H = 1080, 1440


def shoot_one(html_path: Path, poster_index: int, poster_count: int, out_path: Path):
    """只截第 poster_index 张(0-based):注入 CSS 隐藏其余所有 .poster.xhs,
    窗口高度固定为单张卡片高度,避免整页截图的高度瑕疵。"""
    html = html_path.read_text(encoding="utf-8")
    hide_style = (
        "<style>"
        "body { padding: 0 !important; background: transparent !important; }"
        ".sheet { gap: 0 !important; }"
        ".poster.xhs { display: none !important; }"
        f".poster.xhs:nth-of-type({poster_index + 1}) {{ display: block !important; "
        "position: absolute !important; top: 0 !important; left: 0 !important; }"
        "</style></head>"
    )
    patched = html.replace("</head>", hide_style, 1)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".html", dir=html_path.parent, delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(patched)
        tmp_path = Path(tmp.name)

    try:
        result = subprocess.run(
            [
                CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                f"--window-size={CARD_W},{CARD_H}",
                f"--screenshot={out_path}",
                "--virtual-time-budget=4000",
                f"file://{tmp_path}",
            ],
            capture_output=True, text=True, timeout=45,
        )
        if not out_path.exists():
            raise RuntimeError(f"chrome headless produced no file, stderr: {result.stderr[-1000:]}")
        from PIL import Image
        img = Image.open(out_path)
        if img.size != (CARD_W, CARD_H):
            raise RuntimeError(f"rendered {img.size}, expected ({CARD_W},{CARD_H})")
    finally:
        tmp_path.unlink(missing_ok=True)


def main():
    if len(sys.argv) != 4:
        print("usage: render_card.py <index.html> <output_dir> <name_prefix>", file=sys.stderr)
        sys.exit(1)

    html_path = Path(sys.argv[1]).resolve()
    out_dir = Path(sys.argv[2]).resolve()
    prefix = sys.argv[3]
    out_dir.mkdir(parents=True, exist_ok=True)

    html = html_path.read_text(encoding="utf-8")
    html_no_comments = re.sub(r"<!--.*?-->", "", html, flags=re.DOTALL)
    poster_count = len(re.findall(r'<section\s+class="poster\s+xhs"', html_no_comments))
    if poster_count == 0:
        print(f"FAILED: no <section class=\"poster xhs\"> found in {html_path}", file=sys.stderr)
        sys.exit(1)

    for i in range(poster_count):
        name = f"{prefix}-{i+1:02d}"
        out_path = out_dir / f"{name}.png"
        try:
            shoot_one(html_path, i, poster_count, out_path)
        except Exception as e:
            print(f"FAILED: poster {i+1}/{poster_count}: {e}", file=sys.stderr)
            sys.exit(1)
        print(f"wrote {out_path} ({CARD_W}x{CARD_H})")


if __name__ == "__main__":
    main()
