#!/usr/bin/env bash
# 실습 자산 다운로드 링크 검증.
#   1) 페이지의 다운로드 링크가 /blob/ 이 아니라 /raw/ 인지
#   2) 각 raw URL 이 실제로 200 으로 응답하는지 (네트워크 필요)
#   3) 로컬 저장소에 해당 파일이 실제로 있는지
#   4) 매니페스트에 적힌 용량이 실제와 맞는지
#
# 사용: bash check_assets.sh [DOCS_DIR] [LOCAL_REPO]
# 종료: 0 = 결함 없음, 1 = 결함 있음, 2 = 실행 불가
set -uo pipefail

DOCS="${1:-docs}"
REPO="${2:-/Users/andy/Work/harness-edu}"
MANIFEST="_workspace/07_assets_manifest.md"

fail=0
section() { printf '\n\033[1m== %s ==\033[0m\n' "$1"; }
note()    { printf '  %s\n' "$1"; }

[ -d "$DOCS" ] || { echo "디렉토리 없음: $DOCS"; exit 2; }

section "1. /blob/ 로 링크된 다운로드 파일 (미리보기가 안 되어 빈 화면이 된다)"
# .md 를 /blob/ 로 거는 것은 정상 — GitHub 에서 읽히는 것이 의도다.
# 문제는 브라우저가 렌더할 수 없는 파일을 /blob/ 로 거는 것.
blob=$(grep -rnoE 'https://github\.com/[^"]*/blob/[^"]*\.(pptx|potx|xlsx|xlsm|docx|dotx|pdf|zip|hwpx?|ps1)' \
       "$DOCS" --include='*.html' 2>/dev/null || true)
if [ -n "$blob" ]; then
  printf '%s\n' "$blob" | sed 's/^/    /'
  note "→ /raw/ 로 바꿀 것. 이 형식은 GitHub 미리보기가 안 되어 학습자가 빈 화면을 본다"
  fail=1
else
  note "다운로드 파일의 /blob/ 링크 없음 ✓"
fi

md_blob=$(grep -rhoE 'https://github\.com/[^"]*/blob/[^"]*\.md' "$DOCS" --include='*.html' 2>/dev/null | sort -u || true)
if [ -n "$md_blob" ]; then
  note "(참고) .md 의 /blob/ 링크 $(printf '%s\n' "$md_blob" | wc -l | tr -d ' ')건 — GitHub 에서 읽는 용도이므로 정상"
fi

section "2. download 속성 오의존 (크로스 오리진에서는 무시된다)"
dl=$(grep -rnoE '<a[^>]*href="https://github\.com[^"]*"[^>]*download' "$DOCS" --include='*.html' 2>/dev/null || true)
if [ -n "$dl" ]; then
  printf '%s\n' "$dl" | cut -c1-160 | sed 's/^/    /'
  note "→ 무해하지만 효과 없음. /raw/ 가 Content-Disposition 을 붙여 준다"
else
  note "문제 없음 ✓"
fi

section "3. raw URL 응답 확인"
urls=$(grep -rhoE 'https://github\.com/[^"]*/raw/[^"]*' "$DOCS" --include='*.html' 2>/dev/null | sort -u || true)
if [ -z "$urls" ]; then
  note "raw 다운로드 링크가 없음 — 실습 3 준비물 블록이 비어 있지 않은지 확인할 것"
  fail=1
elif ! command -v curl >/dev/null 2>&1; then
  note "curl 없음 — 미검증 (통과로 처리하지 말 것)"
  fail=1
else
  while IFS= read -r u; do
    [ -z "$u" ] && continue
    code=$(curl -sIL -o /dev/null -w '%{http_code}' --max-time 20 "$u" 2>/dev/null || echo "000")
    case "$code" in
      200) note "200 ✓  $u" ;;
      000) note "응답 없음 (네트워크?) — 미검증: $u"; fail=1 ;;
      404) note "404 — 저장소에 push 되지 않았거나 브랜치명이 틀렸다: $u"; fail=1 ;;
      *)   note "$code — 확인 필요: $u"; fail=1 ;;
    esac
  done <<< "$urls"
fi

section "4. 로컬 저장소에 파일 실물 존재"
if [ -d "$REPO" ]; then
  while IFS= read -r u; do
    [ -z "$u" ] && continue
    # .../raw/<branch>/<path> → <path>
    rel=$(printf '%s' "$u" | sed -E 's#.*/raw/[^/]+/##')
    if [ -e "$REPO/$rel" ]; then
      note "$(du -h "$REPO/$rel" | cut -f1)  ✓  $rel"
    else
      note "없음 — $REPO/$rel  (push 대상 파일이 아직 만들어지지 않았다)"
      fail=1
    fi
  done <<< "$urls"
else
  note "로컬 저장소 없음 ($REPO) — 미검증"
  fail=1
fi

section "5. 매니페스트 존재"
if [ -f "$MANIFEST" ]; then
  note "$MANIFEST ✓ — 페이지의 URL·용량이 매니페스트와 같은지 눈으로 대조할 것"
else
  note "$MANIFEST 없음 — assets-steward 가 아직 작성하지 않았다"
  fail=1
fi

section "결과"
if [ "$fail" -eq 0 ]; then
  note "모든 검사 통과"
  exit 0
fi
note "확인 필요 — 미검증을 통과로 보고하지 말 것. _workspace/06_qa_report.md 에 기록"
exit 1
