#!/usr/bin/env python3
"""본문 분량 검사 — edu-site-ia 의 페이지 예산 대비.

학습 시간 1분 ≈ 한국어 본문 250자. 표·도식·카드·코드블록·네비게이션은 제외한다
(읽는 시간이 아니라 훑는 시간이므로).

중첩 태그를 깊이 기반으로 제거한다 — 정규식 `.*?</div>` 는 중첩된 블록에서
첫 번째 닫힘 태그에 걸려 내용을 남긴다. 그 버그는 브리프 원문과 타임라인을
본문으로 세어 페이지가 상한을 넘은 것처럼 보이게 만든다.

사용: python3 check_length.py [DOCS_DIR]
종료: 0 = 전부 통과, 1 = 초과, 2 = 실행 불가
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

# 본문 분량에서 제외할 클래스 (블록 통째로)
DROP_CLASS = {
    "table-wrap", "checks", "checks-2col", "mission", "prep", "diagram", "code-card",
    "patterns", "qs", "steps", "flowline", "pcards", "next-grid", "pager",
    "foot", "topnav", "hero-tags", "hero-actions", "dl-list", "side", "skip-link",
}
DROP_TAG = {"script", "style", "svg", "head", "nav", "header", "footer"}

BUDGET = {
    "index.html": 800,
    "concept.html": 4000,
    "practice/1-youtube.html": 2000,
    "practice/2-marketing.html": 2500,
    "practice/3-pptx.html": 3000,
}

TAG = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)((?:\"[^\"]*\"|'[^']*'|[^>\"'])*)(/?)>")
VOID = {"area","base","br","col","embed","hr","img","input","link","meta",
        "param","source","track","wbr"}


def body_text(src: str) -> str:
    """깊이를 세면서 제외 대상 블록을 건너뛰고 텍스트만 모은다."""
    out: list[str] = []
    pos = 0
    skip_depth = 0          # 0 이면 수집 중
    skip_tag: str | None = None
    depth = 0               # skip 중인 블록 내부의 같은 태그 깊이

    for m in TAG.finditer(src):
        if skip_depth == 0:
            out.append(src[pos:m.start()])
        pos = m.end()

        closing, tag, attrs, selfclose = m.group(1), m.group(2).lower(), m.group(3), m.group(4)

        if skip_depth:
            if tag == skip_tag and not selfclose and tag not in VOID:
                depth += -1 if closing else 1
                if depth == 0:
                    skip_depth, skip_tag = 0, None
            continue

        if closing or selfclose or tag in VOID:
            continue

        if tag in DROP_TAG:
            skip_depth, skip_tag, depth = 1, tag, 1
            continue

        cls = re.search(r'class\s*=\s*"([^"]*)"', attrs)
        if cls and (set(cls.group(1).split()) & DROP_CLASS):
            skip_depth, skip_tag, depth = 1, tag, 1

    if skip_depth == 0:
        out.append(src[pos:])

    txt = html.unescape("".join(out))
    return re.sub(r"\s+", " ", txt).strip()


def main() -> int:
    docs = Path(sys.argv[1] if len(sys.argv) > 1 else "docs")
    if not docs.is_dir():
        print(f"디렉토리 없음: {docs}", file=sys.stderr)
        return 2

    over = 0
    missing = 0
    print(f"본문 분량 (표·도식·카드·코드·네비 제외) — {docs}\n")
    for rel, lim in BUDGET.items():
        f = docs / rel
        if not f.exists():
            print(f"  {rel:32s}  미생성 — 미검증")
            missing += 1
            continue
        n = len(body_text(f.read_text(encoding="utf-8")))
        mark = "✓" if n <= lim else f"초과 +{n - lim}"
        print(f"  {rel:32s}  {n:5d}자 / 상한 {lim:5d}   {mark}")
        if n > lim:
            over += 1

    print()
    if missing:
        print(f"미생성 {missing}건 — 미검증을 통과로 보고하지 말 것")
    if over:
        print(f"초과 {over}건 — 줄이는 순서: ① 배경 설명 삭제 → ② 산문을 표로 "
              "→ ③ 예시 축소 → ④ 섹션 통합.")
        print("검토 체크리스트·브리프 원문·준비물 블록은 마지막까지 줄이지 않는다.")
        return 1
    if missing:
        return 1
    print("전부 상한 이내 ✓")
    return 0


if __name__ == "__main__":
    sys.exit(main())
