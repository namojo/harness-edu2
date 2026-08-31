# -*- coding: utf-8 -*-
"""codex 생성 PNG 후처리 — 투명 배경을 크림색에 합성하고 16:9 로 정규화.

codex 의 image_generation 은 배경을 투명(alpha 0)으로 내보내는 경우가 많다.
그대로 pptx 에 넣으면 뷰어에 따라 검게 보이거나 흰 배경으로 보여
'크림색이 지배색'이라는 형식 규칙 자체가 사라진다. 그래서 합성은 선택이 아니다.
"""
import pathlib, sys
from PIL import Image

CREAM = (250, 240, 220)      # #FAF0DC
W, H = 1920, 1080            # 16:9

def flatten(src: pathlib.Path, dst: pathlib.Path):
    im = Image.open(src).convert('RGBA')
    bg = Image.new('RGBA', im.size, CREAM + (255,))
    flat = Image.alpha_composite(bg, im).convert('RGB')

    # 16:9 로 정규화 — 비율이 다르면 크림 배경에 얹어 레터박스
    ratio = flat.width / flat.height
    if abs(ratio - W/H) < 0.02:
        out = flat.resize((W, H), Image.LANCZOS)
    else:
        out = Image.new('RGB', (W, H), CREAM)
        s = min(W/flat.width, H/flat.height)
        r = flat.resize((round(flat.width*s), round(flat.height*s)), Image.LANCZOS)
        out.paste(r, ((W-r.width)//2, (H-r.height)//2))
    out.save(dst, optimize=True)
    return im.size, out.size

if __name__ == '__main__':
    outdir = pathlib.Path('flat'); outdir.mkdir(exist_ok=True)
    for f in sorted(pathlib.Path('.').glob('s0*.png')):
        a, b = flatten(f, outdir/f.name)
        print(f'  {f.name}  {a[0]}×{a[1]} → {b[0]}×{b[1]}')
