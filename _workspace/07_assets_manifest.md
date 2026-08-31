# 실습 자산 매니페스트

**저장소:** `namojo/harness-edu` · 기본 브랜치 `main` (2026-08-31 확인)
**정본 위치:** 저장소 `workshop/`. `docs/assets/` 에 사본을 두지 않는다.
**로컬 준비 위치:** `_workspace/assets/workshop/` → push 전 보관

| 파일 | 용량 | 실습 | 저장소 경로 | 웹 다운로드 URL |
|---|---|---|---|---|
| `README.md` | 3.2KB | 전체 | `workshop/README.md` | https://github.com/namojo/harness-edu/raw/main/workshop/README.md |
| `practice-1-youtube/README.md` | 2.4KB | 1 | `workshop/practice-1-youtube/README.md` | https://github.com/namojo/harness-edu/raw/main/workshop/practice-1-youtube/README.md |
| `practice-2-marketing/README.md` | 2.7KB | 2 | `workshop/practice-2-marketing/README.md` | https://github.com/namojo/harness-edu/raw/main/workshop/practice-2-marketing/README.md |
| `practice-3-pptx/README.md` | 3.1KB | 3 | `workshop/practice-3-pptx/README.md` | https://github.com/namojo/harness-edu/raw/main/workshop/practice-3-pptx/README.md |
| **`practice-3-pptx/sample.pptx`** | **976KB** | 3 | `workshop/practice-3-pptx/sample.pptx` | https://github.com/namojo/harness-edu/raw/main/workshop/practice-3-pptx/sample.pptx |
| `practice-3-pptx/example-strategy.md` | 7.6KB | 3 | `workshop/practice-3-pptx/example-strategy.md` | https://github.com/namojo/harness-edu/raw/main/workshop/practice-3-pptx/example-strategy.md |

총 1.0MB. `/raw/` 경로 사용 — `/blob/` 은 pptx 미리보기가 안 되어 학습자가 빈 화면을 본다.

## sample.pptx — 요구 조건 9개 검증

**가상 브랜드 '핀치(PINCH)' 반려견 덴탈 츄 '데일리츄' 제안서.** 5장 · 16:9 · 1,023KB.
`codex exec` 의 `image_generation` 툴로 5장을 병렬 생성한 뒤 후처리했다.

| 조건 | 결과 |
|---|---|
| 대표 장이 분명 | ✓ 5장 (표지 / 02 시장 분석 / 03 제품 분석 / KEY CONCEPT / 04 캠페인 효과) |
| 폰트 계층 3단 이상 | ✓ 5단 (섹션번호 · 소제목 · 대제목 · 스탯 수치 · 캡션) |
| 외곽 여백 일정 | ✓ |
| 좌측 정렬선 뚜렷 | ✓ 섹션번호·대제목·부제가 같은 x 에서 시작 |
| 색의 역할 구분 | ✓ **실측** — 크림 `#fbf0dc` 55.5%(지배) / 크림슨 `#d10624`(강조) / 잉크 `#000`(본문) |
| 반복 단위 2개 이상 | ✓ 3열 스탯 카드(원형 아이콘+라벨+수치+캡션), 2열 번호 카드, 3열 번호 카드 |
| 텍스트 편집 가능 | **✗ — 렌더 이미지** (아래 참조) |
| 저작권 명확 | ✓ **가상 브랜드 · AI 생성** |
| 50MB 미만 | ✓ 1.00MB |

### 왜 가상 브랜드로 교체했는가

이전 버전은 사용자가 제공한 **동원 고추참치 'GO-TO TUNA' 캠페인 제안서**(외부 제작물)에서 5장을 발췌한 것이었다. 공개 저장소에 배포하는 교육 자료로서 권리 관계가 불확실했다.

지금은 **가상 브랜드 '핀치(PINCH)'의 반려견 덴탈 츄 '데일리츄'** 제안서를 새로 생성해 쓴다. 원본의 디자인 문법(크림 배경 + 브랜드 레드 + 잉크 3색, 섹션번호 + 룰 + 소제목, 3열 카드 그리드, 브러시 배너)은 그대로 계승하되 내용은 전부 가공이므로 권리 문제가 없다.

**카테고리를 일부러 다르게 했다.** 실습 2의 예시 전략보고서는 오르빗 그래놀라(아침 대용식)이고 샘플은 반려견 덴탈 츄다. 둘이 같은 카테고리면 학습자가 "샘플의 내용을 쓰는 건가"로 혼동한다 — 샘플에서 가져올 것은 형식뿐이다.

### 생성 방법

`codex exec` 의 `image_generation` 툴로 5장을 **병렬 생성**했다 (`codex-image` 스킬).

한 가지 반드시 필요한 후처리가 있다 — **codex 는 배경을 투명(alpha 0)으로 내보낸다.** 실측 67.5% 가 완전 투명이었다. 그대로 두면 뷰어에 따라 검게 보이거나 흰 배경이 되어 "크림색이 지배색"이라는 형식 규칙 자체가 사라진다. `slides/sample-src/flatten.py` 가 크림 `#FAF0DC` 에 합성하고 1920×1080 으로 정규화한다.

재생성 절차는 `slides/sample-src/` 참조.

### "텍스트 편집 불가"를 결함으로 처리하지 않은 이유

이것은 **입력**의 조건이고, 실습 3이 요구하는 편집 가능성은 **출력**의 조건이다. 오히려 입력이 이미지라서 학습자가 텍스트를 복사할 수 없고, 그래서 *"예쁘게 따라 해" 대신 규칙을 언어로 뽑는다*는 이 실습의 교육 목표가 강제된다.
