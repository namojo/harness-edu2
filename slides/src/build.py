# -*- coding: utf-8 -*-
"""슬라이드 HTML 생성 → Chrome headless 로 1920×1080 PNG 렌더"""
import pathlib, subprocess, sys, shutil
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import gen_a, gen_b, gen_c

ROOT = pathlib.Path(__file__).parent.parent          # slides/
SRC  = ROOT/'src'; HTML = ROOT/'html'; PNG = ROOT/'png'
for d in (HTML, PNG): d.mkdir(exist_ok=True)

S = {}
for m in (gen_a, gen_b, gen_c): S.update(m.S)
CSS = (SRC/'base.css').read_text(encoding='utf-8')
TOTAL = len(S)

TPL = '''<!doctype html><html lang="ko"><head><meta charset="utf-8">
<title>{n:02d}</title><style>{css}</style></head><body>
<div class="slide {cls}">{head}{body}{foot}</div></body></html>'''

def head(num, eyebrow):
    if not (num or eyebrow): return ''
    return (f'<div class="head"><span class="num">{num}</span>'
            f'<span class="eyebrow">{eyebrow}</span></div><div class="rule"></div>')

def build():
    for n in sorted(S):
        kind, num, eyebrow, body = S[n]
        cls = 'dark' if kind in ('cover','dark') else ''
        h = '' if kind in ('cover','dark') else head(num, eyebrow)
        foot = ('' if kind=='cover' else
                f'<div class="foot"><span>harness-edu2 · 하네스 엔지니어링 워크샵</span>'
                f'<span class="pg">{n:02d} / {TOTAL:02d}</span></div>')
        (HTML/f'{n:02d}.html').write_text(
            TPL.format(n=n, css=CSS, cls=cls, head=h, body=body, foot=foot), encoding='utf-8')
    return sorted(HTML.glob('*.html'))

CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
def render(files):
    ok = []
    for f in files:
        out = PNG/(f.stem + '.png')
        if out.exists(): out.unlink()
        r = subprocess.run([CHROME,'--headless=new','--disable-gpu','--hide-scrollbars',
            '--force-device-scale-factor=1', f'--screenshot={out}',
            '--window-size=1920,1080','--virtual-time-budget=8000',
            f'file://{f.resolve()}'], capture_output=True, text=True, timeout=120)
        ok.append((f.stem, out.exists(), out.stat().st_size//1024 if out.exists() else 0))
    return ok

def check_overflow(files):
    """1920×1080 을 넘는 슬라이드를 검출한다. 넘치면 렌더 결과가 잘려 나간다."""
    from playwright.sync_api import sync_playwright
    bad = []
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width':1920,'height':1080})
        for f in files:
            pg.goto('file://'+str(f.resolve())); pg.wait_for_timeout(450)
            r = pg.evaluate("""() => {
              const s=document.querySelector('.slide'), de=document.documentElement;
              const over=[...document.querySelectorAll('.slide *')]
                .filter(e=>{const b=e.getBoundingClientRect();
                  return b.height>0 && (b.bottom>1072 || b.right>1912);})
                .map(e=>e.tagName.toLowerCase()+(e.className?'.'+String(e.className).split(' ')[0]:''));
              return {h:Math.round(s.scrollHeight), sw:de.scrollWidth, over:[...new Set(over)].slice(0,6)};
            }""")
            if r['h']>1080 or r['sw']>1920:
                bad.append((f.stem, r['h'], r['over']))
        b.close()
    return bad

if __name__ == '__main__':
    files = build()
    print(f'HTML {len(files)}장 생성')
    bad = check_overflow(files)
    if bad:
        print('\n넘침 검출 — 렌더가 잘립니다:')
        for stem,h,over in bad: print(f'  ✗ {stem}  높이 {h}  {over}')
    else:
        print('넘침 없음 ✓')
    print()
    for stem, exists, kb in render(files):
        print(f'  {stem}.png  {"✓" if exists else "✗ 실패"}  {kb}KB')
