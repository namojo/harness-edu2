#!/usr/bin/env python3
"""브리프 프롬프트 문자 단위 대조.

웹페이지의 브리프 <pre>에서 추출한 텍스트를 정본 텍스트 파일과 비교한다.
눈으로 읽어서 "같다"고 판정할 수 없는 차이(en dash, 이중 공백, 전각 문자,
줄 끝 공백, NBSP)를 잡는 것이 목적이다.

정본 파일 준비:
  .claude/skills/practice-page-writing/references/practice-briefs.md 의
  각 코드블록을 아래 이름으로 저장한다.
    <BRIEFS_DIR>/practice-1.txt
    <BRIEFS_DIR>/practice-2.txt
    <BRIEFS_DIR>/practice-3.txt

사용: python3 check_briefs.py [DOCS_DIR] [BRIEFS_DIR]
종료 코드: 0 = 전부 일치, 1 = 불일치, 2 = 실행 불가
"""
from __future__ import annotations

import difflib
import html
import re
import sys
import unicodedata
from pathlib import Path

PAGES = {
    "practice-1.txt": "practice/1-youtube.html",
    "practice-2.txt": "practice/2-marketing.html",
    "practice-3.txt": "practice/3-pptx.html",
}

# 보이지 않는 문자 — 있으면 정본과 다른 것이므로 이름을 붙여 보여준다
INVISIBLE = {
    "–": "EN DASH(–)",
    "—": "EM DASH(—)",
    " ": "NBSP(줄바꿈없는공백)",
    "​": "ZERO WIDTH SPACE",
    "　": "전각 공백",
    "［": "전각 [",
    "］": "전각 ]",
    "‧": "HYPHENATION POINT(‧)",
}


def visualize(s: str) -> str:
    """차이를 눈으로 볼 수 있게 보이지 않는 문자를 이름으로 바꾼다."""
    out = []
    for ch in s:
        if ch in INVISIBLE:
            out.append(f"⟨{INVISIBLE[ch]}⟩")
        elif ch == " ":
            out.append("␣")
        elif unicodedata.category(ch) in ("Cf", "Cc") and ch != "\n":
            out.append(f"⟨U+{ord(ch):04X}⟩")
        else:
            out.append(ch)
    return "".join(out)


def extract_brief(page: Path) -> str | None:
    """브리프 <pre>의 텍스트를 추출한다. class에 brief가 있는 것을 우선."""
    text = page.read_text(encoding="utf-8", errors="replace")
    cands = re.findall(r'<pre[^>]*class="[^"]*\bbrief\b[^"]*"[^>]*>(.*?)</pre>', text, re.S)
    if not cands:
        # class 없이 쓴 경우 — 하네스 구성 문구가 든 pre 를 찾는다
        cands = [m for m in re.findall(r"<pre[^>]*>(.*?)</pre>", text, re.S)
                 if "하네스를 구성해줘" in m or "재해석" in m]
    if not cands:
        return None
    if len(cands) > 1:
        print(f"  ! {page.name}: 브리프로 보이는 <pre>가 {len(cands)}개 — 첫 번째를 검사합니다")
    inner = cands[0]
    if re.search(r"<[a-zA-Z/][^>]*>", inner):
        print(f"  ! {page.name}: 브리프 <pre> 안에 태그가 있습니다 "
              f"— 클립보드에 마크업이 섞입니다 (BLOCKER)")
    return html.unescape(re.sub(r"<[^>]+>", "", inner)).strip("\n")


def compare(name: str, want: str, got: str) -> bool:
    if want == got:
        print(f"  ✓ {name} — 일치 ({len(want.splitlines())}행)")
        return True

    print(f"  ✗ {name} — 불일치")
    for line in difflib.unified_diff(
        [visualize(l) for l in want.splitlines()],
        [visualize(l) for l in got.splitlines()],
        "정본", "HTML", lineterm="", n=1,
    ):
        print(f"      {line}")

    wl, gl = want.splitlines(), got.splitlines()
    if len(wl) != len(gl):
        print(f"      → 행 수 다름: 정본 {len(wl)}행, HTML {len(gl)}행. "
              f"<pre> 대신 <p>를 썼거나 줄바꿈이 유실되었습니다")
    for w, g in zip(wl, gl):
        if w != g and w.replace(" ", "") == g.replace(" ", ""):
            print("      → 공백만 다름. 이중 공백이 렌더에서 합쳐졌습니다 "
                  "(<pre> 밖 배치 또는 white-space 설정)")
            break
        if w != g and w.replace("–", "-") == g.replace("–", "-"):
            print("      → en dash(–)가 하이픈(-)으로 바뀌었습니다. 에디터 자동 교정")
            break
    return False


def main() -> int:
    docs = Path(sys.argv[1] if len(sys.argv) > 1 else "docs").resolve()
    briefs = Path(sys.argv[2] if len(sys.argv) > 2 else "_workspace/briefs").resolve()

    if not briefs.is_dir():
        print(f"정본 디렉토리 없음: {briefs}", file=sys.stderr)
        print("practice-briefs.md 의 코드블록을 practice-1.txt ~ practice-3.txt 로 저장하세요.",
              file=sys.stderr)
        return 2

    print(f"브리프 대조: {docs} ↔ {briefs}\n")
    ok = True
    checked = 0
    for fname, rel in PAGES.items():
        src, page = briefs / fname, docs / rel
        if not src.exists():
            print(f"  - {rel}: 정본 {fname} 없음 — 미검증")
            ok = False
            continue
        if not page.exists():
            print(f"  - {rel}: 페이지 미생성 — 미검증")
            continue
        got = extract_brief(page)
        if got is None:
            print(f"  ✗ {rel}: 브리프 <pre>를 찾지 못했습니다 (BLOCKER)")
            ok = False
            continue
        want = src.read_text(encoding="utf-8").strip("\n")
        ok &= compare(rel, want, got)
        checked += 1

    print(f"\n검사한 브리프: {checked}/{len(PAGES)}")
    if not ok:
        print("불일치는 전부 BLOCKER입니다 — 복사해서 붙여넣는 것이 실습의 첫 동작입니다.")
        return 1
    if checked < len(PAGES):
        print("미검증 항목이 있습니다. 미검증을 통과로 보고하지 마세요.")
        return 1
    print("전부 일치 ✓")
    return 0


if __name__ == "__main__":
    sys.exit(main())
