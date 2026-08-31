# harness-edu2

`namojo.github.io/harness-edu`(7차시 + 확장트랙)를 **120분 워크샵 교재 한 벌**로 개편하는 프로젝트.

```
설치가이드(이관) → 개념 15분 → 실습 1 (25분) → 실습 2 (30분) → 실습 3 (40분)
```

## 하네스: 교육 사이트 구축

**목표:** 설치가이드는 무손실 이관하고, 하네스 개념과 실습 3개만 남긴 실습 중심 사이트를 만든다.

**트리거:** 사이트 구조·개념 원고·실습 페이지·설치가이드 이관·실습 자산·다운로드 링크·QA 관련 작업 요청 시 `harness-edu2-build` 스킬을 사용하라. 단순 질문(파일 위치, 개념 확인)은 직접 응답 가능.

## 두 저장소에 걸친 산출물

| 어디 | 무엇 |
|---|---|
| 이 저장소 → `docs/` | 웹사이트 (GitHub Pages) |
| `namojo/harness-edu` → `workshop/` | 실습 파일 원본. 학습자가 `git clone`으로 받는 것 |

**실습 저장소를 새로 만들지 않는다.** 기존 `namojo/harness-edu`(기본 브랜치 `main`)에 `workshop/`을 추가한다. 이 결정 덕분에 이관된 설치가이드의 `git clone` URL과 실습 폴더 경로(`~/harness-edu`, `C:\harness-edu` — 51곳, `.ps1` 포함)를 하나도 건드리지 않는다. 한 곳만 놓쳐도 학습자는 존재하지 않는 폴더로 이동하려다 막히고, 원인이 문서에 있다는 것을 알아낼 방법이 없다.

## 절대 바꾸지 않는 것

| 대상 | 이유 |
|---|---|
| 실습 브리프 프롬프트 3편의 원문 | 복사해서 붙여넣는 것이 실습의 첫 동작이다. en dash(`8–10분`)와 이중 공백(`위한  마케팅`)까지 보존. 정본은 `.claude/skills/practice-page-writing/references/practice-briefs.md` |
| 이관된 설치 문서의 명령어·절 번호·앵커 id | 현장에서 검증된 자산이다. 한 글자가 바뀌면 학습자의 터미널이 멈춘다 |
| `namojo/harness-edu` 저장소 URL과 실습 폴더 경로 | 위 참조 |

## 변경 이력

| 날짜 | 변경 내용 | 대상 | 사유 |
|------|----------|------|------|
| 2026-08-31 | 초기 구성 — 에이전트 6, 스킬 6 + 오케스트레이터 1 | 전체 | - |
| 2026-08-31 | `assets-steward` 에이전트 + `practice-assets` 스킬 추가 | agents/assets-steward.md, skills/practice-assets/ | 실습 환경을 `namojo/harness-edu`에 추가하고 웹에 다운로드 안내가 필요하다는 요구 |
| 2026-08-31 | 실습 페이지 골격 8블록 → 9블록 (준비물을 2번에 삽입) | skills/practice-page-writing/ | 파일이 없다는 것을 브리프 실행 전에 알아야 한다 |
| 2026-08-31 | 설치가이드 이관 정책 변경 — 브랜드 표기만 치환, 저장소·경로 보존 | skills/install-guide-port/ | 실습 저장소를 유지하기로 결정되어 51곳 치환이 불필요해짐 |
| 2026-08-31 | **초기 빌드 완료** — `docs/` 본문 5장 + 이관 5문서, `workshop/` 자산 6개 | docs/, _workspace/ | 사이트 구축 실행 |
| 2026-08-31 | `check_length.py` 추가, `check_site.py` 오탐 2건 수정 | skills/edu-site-qa/scripts/ | 중첩 태그 미처리로 브리프·타임라인을 본문으로 오산, `<code>` 인라인 인용을 브리프 유출로 오판 |
| 2026-08-31 | **Python 을 필수 공통 준비에서 선택 학습(MCP)으로 이동** | docs/install/ 4문서 | 실습 1·2·3에 Python 이 쓰이지 않는데 필수 흐름에 남아 앞뒤가 안 맞았다. 공통 준비 30~40분 → 25~35분 |
| 2026-08-31 | 사이드바 레이블 `h4` → `p.side-label` (5문서 15건) + CSS | docs/install/, docs/assets/site.css | 제목 레벨 건너뜀(h2→h4) 5건 해소. 본문 h3→h4 는 정상이라 유지 |
| 2026-08-31 | **GitHub Pages 배포** | namojo/harness-edu2 | https://namojo.github.io/harness-edu2 |
| 2026-08-31 | 진화 메커니즘 도식·설명 재작성 — 사용→피드백→진화→기록 순환 | docs/concept.html, skills/harness-concept-source/ | README 의 "팩토리 되먹임" 표현만 인용해 **피드백 일반화와 기록 단계가 빠졌다**. `evolve` 스킬의 실제 도식을 정본으로 채택 |
| 2026-08-31 | 안전 원칙류 문구 전량 제거 | docs/ 7문서, workshop/ 4문서, agents/practice-designer.md, skills/practice-page-writing/ | 사용자 지시 — "말로 설명할 수 있다". "실 데이터 넣지 말라·보안 검토 거쳐라" 류만 제거하고 도구 사용법(승인 프롬프트·사내 보안 프로그램)은 유지 |
| 2026-08-31 | 실습 1의 `5편`·`요일별`·`한 시리즈` 창작 내용 제거 | docs/practice/1-youtube.html, workshop/, skills/practice-page-writing/ | **브리프에 없는 숫자를 판정 기준으로 제시**했다. 학습자가 자기 결과를 틀렸다고 판단하게 만든다. 스킬과 에이전트 정의에 재발 방지 규칙 추가 |
| 2026-08-31 | 실습 2 앞쪽에 멀티에이전트 개념 절 추가 | docs/practice/2-marketing.html | 실습 2가 정하는 구조가 왜 필요한지 없이 브리프로 바로 들어갔다. 패턴 선택 3질문을 이 실습에 적용한 표로 개념과 연결 |
| 2026-08-31 | **검토 체크리스트 전량 제거** | docs/practice/ 3장, workshop/ 3문서 | 사용자 지시 |
| 2026-08-31 | **워크샵·실습 시간 배분 전량 제거** | docs/ 5문서, workshop/ 4문서 | 사용자 지시. 브리프 원문의 `8–10분` 과 설치 소요시간은 성격이 달라 보존 |
| 2026-08-31 | 개념 1부에 **Agent · Skill · Tool 3축** 절 추가 | docs/concept.html | 3축 구분·판단 규칙이 빠져 있었다. 에이전트 정의 파일 실물 예시, `skill-creator` 와 하네스 생성의 구분, 스킬(맥락 판단) ↔ 툴(고정 계산) 차이 포함. 1세대 harness-edu 의 3축 프레이밍 계승 |
| 2026-08-31 | `namojo/harness-edu` 에 `workshop/` push (sample.pptx 포함) | 외부 저장소 | 실습 3 다운로드 링크 3개 **200 확인**. 저장소가 PUBLIC 임을 사용자에게 알린 뒤 승인받아 진행 |
| 2026-08-31 | 설치가이드 소요시간 표기 전량 제거 | docs/install/ 5문서 | 사용자 지시. `⏱ 25~35분`·절 제목 `(5분)` 등 26건. **개별 명령의 예상 대기시간(`1~3분`)은 보존** — 학습자가 멈춘 건지 진행 중인지 판단하는 정보 |
| 2026-08-31 | 폴더 트리에서 1세대 폴더 목록·`이전 과정(7차시)` 문장 제거 | docs/install/index.html | 사용자 지시. QA 잔여 결함 0건 달성 |

## 현재 상태 (2026-08-31)

**배포 완료:** https://namojo.github.io/harness-edu2 — 저장소 `namojo/harness-edu2` (public), Pages 소스 `main` 브랜치 `/docs`.
배포본이 로컬과 12파일 전부 바이트 일치, 13개 URL 전부 200, 브리프 3편 정본 일치 확인.

**사이트:** BLOCKER 0건. 미해소 결함 1건이며 의도된 문장(`install/index.html:208`). 깨진 링크·앵커 0, 5페이지 분량 전부 상한 이내, 700px/390px 가로 스크롤 0.

**저장소에 넣지 않은 것:** `.gitignore` 로 `*.pptx` 전량과 `_workspace/assets/` 를 제외했다. 원본 `sample.pptx`(93.9MB)와 파생본(976KB)이 외부 제작물이고, 실습 자산의 정본은 `namojo/harness-edu` 의 `workshop/` 이기 때문이다.

**자산:** `namojo/harness-edu` 의 `workshop/` 에 **push 완료** (텍스트 5파일 + `sample.pptx` 972KB). 실습 3의 다운로드 링크 3개 전부 200 확인. `harness-edu` 는 PUBLIC 저장소이며, 그 사실을 알린 뒤 사용자 승인으로 `sample.pptx` 를 올렸다.

**sample.pptx:** 사용자 제공 93.9MB(동원 고추참치 'GO-TO TUNA' 제안서 10장)에서 인물 사진과 72MB 동영상을 제외한 5장을 렌더해 **976KB**로 축소. 외부 제작물이므로 공개 저장소 push 전 배포 가능 여부 확인 권장 — `_workspace/07_assets_manifest.md` §저작권.

**미해소 결함:** 이관분의 `h2 → h4` 5건 (MINOR, 원본 유래, 화면에 감춰진 사이드바 요소). 무손실 원칙상 손대지 않음 — `_workspace/06_qa_report.md`.
