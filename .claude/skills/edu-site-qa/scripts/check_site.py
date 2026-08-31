#!/usr/bin/env python3
"""harness-edu2 사이트 구조 검사.

링크·앵커 대상 존재, 제목 레벨 순서, 잔여 문자열, SVG 접근성,
프롬프트 <pre> 배치, 필수 id, 판정 불가능한 체크리스트 표현을 점검한다.

사용: python3 check_site.py [DOCS_DIR]
종료 코드: 0 = 결함 없음, 1 = 결함 있음, 2 = 실행 불가
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

# 판정 불가능한 체크리스트 표현 — 학습자가 O/X를 매길 수 없다
VAGUE = re.compile(r"적절(한|하)|충분(한|하)|품질이 (좋|높)|잘 (되|나)|논리적|명확한가|우수(한|하)")
# 이관 잔여 문자열
# 이관 잔여 검사.
# 저장소는 namojo/harness-edu 를 계속 쓰므로 저장소 URL·실습 폴더 경로는 보존 대상이다.
# 오히려 그것들이 harness-edu2 로 바뀐 것이 결함이다 (학습자가 없는 폴더로 이동한다).
RESIDUAL = {
    "차시 체계 잔여": re.compile(r"\d\s*차시"),
    "chapters/ 경로": re.compile(r"chapters/"),
    "#curriculum 앵커 (→ #flow)": re.compile(r"#curriculum"),
    "저장소 URL이 잘못 바뀜": re.compile(r"github\.com/namojo/harness-edu2"),
    "실습 폴더 경로가 잘못 바뀜": re.compile(r"~/harness-edu2|C:\\harness-edu2"),
    "이중치환": re.compile(r"harness-edu22"),
}
# 홈에 반드시 있어야 하는 id (이관 문서 5개의 앵커 대상 #curriculum → #flow)
REQUIRED_HOME_IDS = ["flow"]

findings: list[tuple[str, str, str]] = []   # (severity, location, message)
passed: list[str] = []


def add(sev: str, loc: str, msg: str) -> None:
    findings.append((sev, loc, msg))


def strip_tags(s: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def line_of(text: str, idx: int) -> int:
    return text.count("\n", 0, idx) + 1


def check_links(path: Path, text: str, docs: Path) -> None:
    for m in re.finditer(r'href="([^"]*)"', text):
        href = m.group(1)
        ln = line_of(text, m.start())
        if not href or href.startswith(("http://", "https://", "mailto:", "tel:", "data:", "javascript:")):
            continue
        target, _, frag = href.partition("#")
        tf = path if not target else (path.parent / target)
        if not tf.exists():
            add("BLOCKER", f"{path.relative_to(docs)}:{ln}",
                f"링크 대상 없음: {href} — 학습자가 이 링크를 누르면 404")
            continue
        if frag and tf.suffix in (".html", ".htm"):
            body = tf.read_text(encoding="utf-8", errors="replace")
            if not re.search(rf'(id|name)="{re.escape(frag)}"', body):
                add("MAJOR", f"{path.relative_to(docs)}:{ln}",
                    f"앵커 없음: {href} — 에러 없이 조용히 페이지 최상단으로 이동함")


def check_heading_order(path: Path, text: str, docs: Path) -> None:
    prev = 0
    for m in re.finditer(r"<h([1-6])\b", text):
        lvl = int(m.group(1))
        if prev and lvl > prev + 1:
            add("MINOR", f"{path.relative_to(docs)}:{line_of(text, m.start())}",
                f"제목 레벨 건너뜀: h{prev} → h{lvl} — 스크린리더 목차가 끊긴다")
        prev = lvl


def check_residual(path: Path, text: str, docs: Path) -> None:
    rel = str(path.relative_to(docs))
    for label, pat in RESIDUAL.items():
        for m in pat.finditer(text):
            # 실습 폴더 경로(~/harness-edu2, C:\harness-edu2)는 위 정규식이 이미 제외함
            add("MAJOR", f"{rel}:{line_of(text, m.start())}",
                f"이관 잔여 문자열 [{label}]: {text[m.start():m.start()+40]!r}")


def check_svg_a11y(path: Path, text: str, docs: Path) -> None:
    for m in re.finditer(r"<svg\b([^>]*)>(.*?)</svg>", text, re.S):
        attrs, inner = m.group(1), m.group(2)
        ln = line_of(text, m.start())
        # 장식용 아이콘은 통과. svg 자신 또는 감싼 요소에 aria-hidden 이 있으면 장식이다
        # (예: <span class="spike" aria-hidden="true"><svg ...>)
        if "aria-hidden" in attrs or 'aria-hidden="true"' in text[max(0, m.start() - 120):m.start()]:
            continue
        if 'role="img"' not in attrs:
            add("MINOR", f"{path.relative_to(docs)}:{ln}",
                'SVG에 role="img" 없음 — 장식이면 aria-hidden="true"를 붙일 것')
        if "<title" not in inner:
            add("MAJOR", f"{path.relative_to(docs)}:{ln}",
                "도식 SVG에 <title> 없음 — 스크린리더가 도식을 읽지 못한다")


def check_briefs_placement(path: Path, text: str, docs: Path) -> None:
    """브리프는 반드시 <pre> 안에 있어야 한다 — 밖이면 이중 공백·줄바꿈이 유실된다."""
    if "practice" not in str(path):
        return
    rel = str(path.relative_to(docs))
    pres = re.findall(r'<pre[^>]*>(.*?)</pre>', text, re.S)
    has_brief_pre = any("하네스를 구성해줘" in p or "하네스를 구성해줘" in p
                        or "형식과 디자인을 재해석" in p or "하네스를 구성해줘." in p
                        for p in pres)
    body_wo_pre = re.sub(r'<pre[^>]*>.*?</pre>', "", text, flags=re.S)
    # <code> 안의 짧은 인용은 유출이 아니다 — 트러블슈팅에서 "첫 줄이 있는지 확인하세요"
    # 처럼 브리프의 한 줄을 인라인으로 가리키는 것은 정상적인 안내다.
    body_wo_pre = re.sub(r'<code[^>]*>.{0,80}?</code>', "", body_wo_pre, flags=re.S)
    leaked = [kw for kw in ("하네스를 구성해줘", "형식과 디자인을 재해석")
              if kw in strip_tags(body_wo_pre)]
    if leaked and not has_brief_pre:
        add("BLOCKER", rel,
            f"브리프가 <pre> 밖에 있음 {leaked} — 이중 공백과 줄바꿈이 렌더에서 유실된다")
    elif leaked:
        add("MAJOR", rel,
            f"브리프 문구가 <pre> 밖에도 등장 {leaked} — 학습자가 어느 쪽을 복사할지 모른다")

    # 복사 버튼과 pre 의 짝
    n_copy = len(re.findall(r"data-copy", text))
    if pres and n_copy == 0:
        add("BLOCKER", rel, "<pre>는 있으나 data-copy 버튼이 없음 — 손으로 타이핑하게 된다")

    # 플레이스홀더에 태그가 섞였는지
    for p in pres:
        if re.search(r"\[<[^>]+>|<[^>]+>\]", p):
            add("BLOCKER", rel,
                "브리프 <pre> 안 플레이스홀더에 태그가 섞임 — 클립보드에 마크업이 들어간다")
            break


def check_vague_checks(path: Path, text: str, docs: Path) -> None:
    if "practice" not in str(path):
        return
    for m in re.finditer(r"<li\b[^>]*>(.*?)</li>", text, re.S):
        t = strip_tags(m.group(1)).strip()
        if VAGUE.search(t):
            add("MAJOR", f"{path.relative_to(docs)}:{line_of(text, m.start())}",
                f"판정 불가능한 체크리스트 항목: {t[:60]!r} — 학습자가 O/X를 매길 수 없다")


def check_required(docs: Path) -> None:
    home = docs / "index.html"
    if not home.exists():
        add("BLOCKER", "docs/index.html", "홈이 없음")
        return
    body = home.read_text(encoding="utf-8", errors="replace")
    for rid in REQUIRED_HOME_IDS:
        if f'id="{rid}"' in body:
            passed.append(f'홈에 id="{rid}" 존재')
        else:
            add("BLOCKER", "docs/index.html",
                f'id="{rid}" 없음 — 이관된 설치 문서 5개의 앵커 대상이다')

    for rel in ("assets/site.css", "assets/site.js", ".nojekyll"):
        if (docs / rel).exists():
            passed.append(f"{rel} 존재")
        else:
            add("MAJOR", f"docs/{rel}", "필수 파일 없음")

    # 실습 자산은 docs/assets/ 가 아니라 namojo/harness-edu 저장소의 workshop/ 이 정본이다.
    # 여기서는 각 실습 페이지가 준비물 블록을 갖췄는지, 실습 3이 자산을 링크하는지 본다.
    # raw URL 의 실제 응답은 check_assets.sh 가 검증한다.
    for rel in ("practice/1-youtube.html", "practice/2-marketing.html", "practice/3-pptx.html"):
        page = docs / rel
        if not page.exists():
            continue
        body = page.read_text(encoding="utf-8", errors="replace")
        if 'class="prep' in body or 'id="준비물"' in body:
            passed.append(f"{rel} 준비물 블록 존재")
        else:
            add("MAJOR", f"docs/{rel}",
                "준비물 블록(블록 2) 없음 — 입력 파일이 없는 실습도 빈 채로 두지 않고 "
                '"입력 파일 없음"으로 채운다 (9블록 골격 일관성)')

    p3 = docs / "practice/3-pptx.html"
    if p3.exists():
        body = p3.read_text(encoding="utf-8", errors="replace")
        if "sample.pptx" in body:
            passed.append("실습 3이 sample.pptx 를 링크함")
        else:
            add("BLOCKER", "docs/practice/3-pptx.html",
                "sample.pptx 참조 없음 — 형식 규칙을 추출할 대상이 없어 실습 3이 시작되지 않는다")
        if "example-strategy" in body:
            passed.append("실습 3에 실습 2 우회 경로 있음")
        else:
            add("BLOCKER", "docs/practice/3-pptx.html",
                "실습 2 우회 경로(example-strategy.md) 없음 — 실습 2를 건너뛴 학습자가 멈춘다")


def main() -> int:
    docs = Path(sys.argv[1] if len(sys.argv) > 1 else "docs").resolve()
    if not docs.is_dir():
        print(f"디렉토리 없음: {docs}", file=sys.stderr)
        return 2

    pages = sorted(p for p in docs.rglob("*.html"))
    if not pages:
        print(f"HTML 없음: {docs}", file=sys.stderr)
        return 2

    for p in pages:
        text = p.read_text(encoding="utf-8", errors="replace")
        check_links(p, text, docs)
        check_heading_order(p, text, docs)
        check_svg_a11y(p, text, docs)
        check_briefs_placement(p, text, docs)
        check_vague_checks(p, text, docs)
        if "install" in str(p.relative_to(docs)):
            check_residual(p, text, docs)
    check_required(docs)

    order = {"BLOCKER": 0, "MAJOR": 1, "MINOR": 2}
    findings.sort(key=lambda f: (order[f[0]], f[1]))

    print(f"검사한 페이지: {len(pages)}개  ({docs})")
    if passed:
        print("\n[통과]")
        for p in passed:
            print(f"  ✓ {p}")
    if not findings:
        print("\n결함 없음 ✓")
        return 0

    print(f"\n[결함] {len(findings)}건")
    cur = None
    for sev, loc, msg in findings:
        if sev != cur:
            print(f"\n-- {sev} --")
            cur = sev
        print(f"  {loc}\n    {msg}")
    print("\n각 결함을 담당 에이전트에게 전달하고 _workspace/06_qa_report.md 에 기록할 것.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
