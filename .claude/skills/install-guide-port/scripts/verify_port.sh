#!/usr/bin/env bash
# 설치가이드 이관 검증 — 잔여 문자열, 깨진 상대경로, 앵커 보존을 점검한다.
# 사용: bash .claude/skills/install-guide-port/scripts/verify_port.sh [DOCS_DIR] [ORIG_DIR]
set -uo pipefail

DOCS="${1:-docs}"
ORIG="${2:-/Users/andy/Work/harness-edu/docs/install}"
INST="$DOCS/install"

fail=0
section() { printf '\n\033[1m== %s ==\033[0m\n' "$1"; }
note()    { printf '  %s\n' "$1"; }

[ -d "$INST" ] || { echo "이관 디렉토리 없음: $INST"; exit 2; }

section "1. 문자열 검사 — ①만 치환, ②③은 보존"
# 저장소는 namojo/harness-edu 를 계속 쓴다. 그래서 검사는 두 방향이다:
#  (a) 브랜드가 아직 안 바뀐 곳
#  (b) 저장소 URL / 실습 폴더 경로가 잘못 바뀐 곳  ← 이쪽이 학습자를 막는다

note "(a) 브랜드 미치환 — harness-edu2 로 바뀌어야 하는 곳"
brand_left=0
for pat in '· harness-edu<' 'brand-full">harness-edu<' 'harness-edu 설치가이드' 'harness-edu 과정' 'harness-edu 커리큘럼'; do
  hits=$(grep -rnF "$pat" "$INST" 2>/dev/null || true)
  if [ -n "$hits" ]; then
    printf '%s\n' "$hits" | cut -c1-150 | sed 's/^/      /'
    brand_left=$((brand_left+1)); fail=1
  fi
done
[ "$brand_left" -eq 0 ] && note "    브랜드 치환 완료 ✓"

note "(b) 저장소 URL·실습 폴더 경로가 잘못 바뀐 곳 — 하나라도 있으면 BLOCKER"
path_broken=0
for pat in 'github.com/namojo/harness-edu2' '~/harness-edu2' 'C:\\harness-edu2' 'harness-edu22'; do
  hits=$(grep -rnF "$pat" "$INST" 2>/dev/null || true)
  if [ -n "$hits" ]; then
    note "    [$pat] — 학습자가 존재하지 않는 저장소/폴더로 이동하게 된다"
    printf '%s\n' "$hits" | cut -c1-150 | sed 's/^/      /'
    path_broken=$((path_broken+1)); fail=1
  fi
done
[ "$path_broken" -eq 0 ] && note "    저장소 URL·폴더 경로 보존 ✓"

note "(c) 차시 체계 잔여 — 실습 1~3 으로 재배선되어야 하는 곳"
for pat in 'chapters/' '차시'; do
  hits=$(grep -rnE "$pat" "$INST" 2>/dev/null || true)
  if [ -n "$hits" ]; then
    note "    [$pat] — $(printf '%s\n' "$hits" | wc -l | tr -d ' ')건 (각 건이 의도된 것인지 판단할 것)"
    printf '%s\n' "$hits" | cut -c1-150 | sed 's/^/      /'
    fail=1
  else
    note "    [$pat] — 없음 ✓"
  fi
done

note "(d) clone URL 과 cd 대상 일치 — 사람이 눈으로 확인할 것"
grep -rnE 'git clone|cd (~|C:)|Set-Location' "$INST" 2>/dev/null | cut -c1-170 | sed 's/^/      /' || true

note "(e) workshop/ 실습 파일 안내 문장 존재"
if grep -rqF 'workshop/' "$INST" 2>/dev/null; then
  note "    workshop/ 안내 있음 ✓"
else
  note "    workshop/ 안내 없음 — 학습자가 clone 후 자기 실습 폴더를 못 찾는다"
  fail=1
fi

section "2. 내부 링크 대상 존재 확인"
missing=0
while IFS='|' read -r f href; do
  case "$href" in http*|mailto:*|tel:*|data:*|'#'*|'') continue;; esac
  target="${href%%#*}"
  [ -z "$target" ] && continue
  if [ ! -e "$(dirname "$f")/$target" ]; then
    note "없는 대상: $f -> $href"
    missing=$((missing+1)); fail=1
  fi
done < <(grep -rnoE 'href="[^"]*"' "$INST" --include='*.html' 2>/dev/null \
         | sed -E 's/^([^:]+):[0-9]+:href="([^"]*)"$/\1|\2/')
[ "$missing" -eq 0 ] && note "깨진 내부 링크 없음 ✓"

section "2-B. 앵커(#fragment) 대상 존재 확인"
bad_anchor=0
while IFS='|' read -r f href; do
  case "$href" in http*|mailto:*|tel:*|data:*|'') continue;; esac
  case "$href" in *'#'*) : ;; *) continue;; esac
  frag="${href#*#}"
  [ -z "$frag" ] && continue
  target="${href%%#*}"
  if [ -z "$target" ]; then tf="$f"; else tf="$(dirname "$f")/$target"; fi
  if [ ! -e "$tf" ]; then
    note "앵커 대상 파일 없음: $f -> $href"; bad_anchor=$((bad_anchor+1)); fail=1; continue
  fi
  if ! grep -qE "id=\"$frag\"|name=\"$frag\"" "$tf" 2>/dev/null; then
    note "앵커 없음(조용히 최상단으로 이동함): $f -> $href"
    bad_anchor=$((bad_anchor+1)); fail=1
  fi
done < <(grep -rnoE 'href="[^"]*"' "$INST" --include='*.html' 2>/dev/null \
         | sed -E 's/^([^:]+):[0-9]+:href="([^"]*)"$/\1|\2/' | sort -u)
[ "$bad_anchor" -eq 0 ] && note "깨진 앵커 없음 ✓"

section "3. 앵커 id 보존 (원본 대비)"
if [ -d "$ORIG" ]; then
  for f in "$ORIG"/*.html; do
    [ -f "$f" ] || continue
    b="$(basename "$f")"
    if [ ! -f "$INST/$b" ]; then
      note "이관 누락: $b"; fail=1; continue
    fi
    lost=$(comm -23 \
      <(grep -oE 'id="[^"]*"' "$f"        | sort -u) \
      <(grep -oE 'id="[^"]*"' "$INST/$b"  | sort -u))
    if [ -n "$lost" ]; then
      note "$b — 유실된 id:"; printf '%s\n' "$lost" | sed 's/^/    /'; fail=1
    else
      note "$b — id 보존 ✓"
    fi
  done
else
  note "원본 디렉토리 없음 ($ORIG) — 앵커 비교 미검증"
  fail=1
fi

section "4. 자산·필수 파일"
for p in "$DOCS/assets/site.css" "$DOCS/assets/site.js" "$DOCS/.nojekyll"; do
  if [ -e "$p" ]; then note "$p ✓"; else note "$p 없음"; fail=1; fi
done

section "결과"
if [ "$fail" -eq 0 ]; then
  note "모든 검사 통과"
else
  note "확인 필요 항목 있음 — _workspace/03_porter_residual.md 에 판단과 함께 기록할 것"
fi
exit 0
