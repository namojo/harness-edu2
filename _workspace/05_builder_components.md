# 구현 기록

## 파일

```
docs/
├── .nojekyll
├── index.html            홈 (id="flow", id="practice")
├── concept.html          개념 (1부 하네스 엔지니어링 / 2부 메타스킬 6단계 / 3부 6패턴 + 3질문)
├── practice/
│   ├── 1-youtube.html    실습 1 (9블록)
│   ├── 2-marketing.html  실습 2 (9블록)
│   └── 3-pptx.html       실습 3 (9블록, 체크리스트 2열)
├── install/              이관 5문서 + ps1 (HTML 무손실)
└── assets/
    ├── site.css          1세대 358줄 계승 + harness-edu2 145줄 추가 = 503줄
    └── site.js           **수정 없음** (1세대 그대로)
```

프레임워크·빌드 스텝 없음. `docs/` 를 push하면 GitHub Pages에서 그대로 뜬다.

## site.js 를 고치지 않은 방법

브리프 박스를 새 컴포넌트로 만들지 않고 **기존 `.code-card.is-prompt` 를 그대로 재사용**했다. `site.js` 의 복사 로직이 `btn.closest('.code-card')` 로 카드를 찾으므로 셀렉터가 그대로 맞는다.

`pre` 에만 `class="brief"` 를 더해 줄바꿈 규칙을 덮어썼다:

```css
.code-card.is-prompt pre.brief{white-space:pre;overflow-x:auto;font-family:var(--sans);font-size:15px;line-height:1.75}
```

`white-space:pre` 를 쓴 이유 — 상속된 `pre-wrap` 은 좁은 화면에서 줄을 접어 학습자가 원문 행 수를 오해한다. 가로 스크롤을 허용하는 대신 5행이 항상 5행으로 보인다. 이중 공백은 두 값 모두 보존한다.

## 계승한 것 / 안 옮긴 것

**계승 (이관 설치가이드가 쓰므로 하나도 지우지 않음):** 디자인 토큰 전체, `.topnav` · `.brand` · `.skip-link` · `.prose` · `.table-wrap` · `.code-card`(+`is-prompt`/`is-term`/`is-lite`/`is-out`) · `.callout-*` · `.next-grid`/`.next-card` · `.pager` · `.prep`/`.prep-item` · `.checklist` · `.side-toc`/`.toc-list` · `.os-grid` · `.flow` · `.terms` · `.worksheet` 등

**안 옮긴 것 (harness-edu2에 개념이 없음):** 대상별 필터(`.filter`), 차시 카드/스테이지(`.stage`/`.mod`), 확장트랙 배지

## 신설 컴포넌트

| 클래스 | 쓰이는 곳 | 비고 |
|---|---|---|
| `.page` | 홈·개념·실습 | 사이드바 없는 960px 본문 |
| `.hero` / `.btn` | 홈·개념·실습 상단 | |
| `.sec` | 전 페이지 섹션 | eyebrow + h2 + sub |
| `.flowline` / `.fl` | 홈 `#flow` | 6열 고정 → 1000px 3열 → 640px 2열 |
| `.pcards` / `.pcard` | 홈 `#practice` | 실습 3장 카드 |
| `pre.brief` / `.brief-note` | 실습 3장 | 위 참조 |
| `.mission` / `.mi` | 실습 3장 | "이번 실습에서 확인할 것" |
| `.dl-list` / `.dl` | 실습 3 준비물 | `/raw/` 다운로드 |
| `.checks` / `.checks-gate` / `.checks-2col` | 실습 3장 | **실제 `<input type=checkbox>`** — 학습자가 누른다 |
| `.diagram` | 개념·실습 3장 | 인라인 SVG + `role="img"` + `<title>` + `<desc>` |
| `.patterns` / `.pt` | 개념 3부 | 6패턴 카드 (동일 4슬롯) |
| `.qs` / `.q` | 개념 3부 | 패턴 선택 3질문 |
| `.steps` / `.st` | 개념 2부 | 메타스킬 6단계 |
| `.src` | 개념 | 출처 표기 |
| `.foot` | 전 페이지 | |

## 도식 4개 (전부 인라인 SVG)

| 위치 | 무엇을 보여주는가 |
|---|---|
| 개념 1부 | 하네스 진화 메커니즘 (초기 → 사용 → 출시 → 팩토리 되먹임) |
| 실습 1 | 브리프 → 4담당 병렬 → 편집 통합 → 1주치 기획안 |
| 실습 2 | 팬아웃/팬인 4조사 → 전략가 → 리뷰어(수정 요청 역방향 화살표) |
| 실습 3 | 형식·내용 2입력 → 제작자 → 내용/형식 리뷰어 2갈래 → 3장 |

전부 `role="img"` + `aria-labelledby` 로 `<title>`·`<desc>` 를 연결했다. `.diagram{overflow-x:auto}` + `svg{min-width:520px}` 이므로 좁은 화면에서 도식만 스크롤되고 본문은 스크롤되지 않는다.

## 원고 대비 변형

| 항목 | 원고/계획 | 구현 | 사유 |
|---|---|---|---|
| 홈 "실습 파일" 섹션 | 별도 섹션 | 실습 카드 아래 **한 줄 안내**로 흡수 | `edu-site-ia` 규칙("홈에는 한 줄 안내") 준수 + 분량 상한 |
| 실습 3 체크리스트 소제목 | `<h4>` | `<h3>` (모양은 h4 크기로 CSS 유지) | 제목 레벨 건너뜀 방지 |
| `docs/assets/sample.pptx` | 사본 배치 검토 | **두지 않음** | 저장소 `workshop/` 이 정본. 사본을 두면 갱신이 갈린다 |

## 로컬 확인

`python3 -m http.server` 로 홈·개념·실습 1·2·3·설치가이드 6페이지 확인. 복사 버튼 실제 클릭 및 클립보드 문자열 검증 완료(`06_qa_report.md` 참조).
