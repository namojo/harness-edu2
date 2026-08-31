---
name: harness-edu2-build
description: harness-edu2 교육 사이트를 에이전트 팀으로 구축·개편하는 오케스트레이터. 설치가이드 이관 · 하네스 개념 페이지 · 실습 3개(유튜브 기획 팀 / 마케팅 전략보고서 / 샘플 형식 PPT) · 실습 자산과 저장소 환경 · 정적 사이트 구현 · QA를 한 워크플로우로 엮는다. "harness-edu2 만들어", "교육 사이트 만들어", "워크샵 교재 만들어", "사이트 개편", "블로그 만들어", "전체 다시 빌드", "다시 실행", "재실행", "업데이트", "보완", "실습 2만 다시", "이전 결과 기반으로", "처음부터 다시" 요청 시 반드시 이 스킬을 사용. 여러 페이지·여러 담당이 걸리는 작업 전체를 조율하는 것이 이 스킬의 역할이다. 한 가지만 손보는 요청(설치가이드 이관, 실습 한 편 집필, 자산 준비, CSS 수정, QA 실행)은 각각 install-guide-port · practice-page-writing · practice-assets · edu-static-site · edu-site-qa 가 직접 담당한다. 단순 질문(파일 위치, 개념 확인)은 직접 응답 가능.
---

# harness-edu2 구축 오케스트레이터

## 무엇을 만드는가

`namojo.github.io/harness-edu`(7차시 + 확장트랙)를 **120분 워크샵 교재 한 벌**로 개편한다.

```
설치가이드(이관) → 개념 15분 → 실습 1 (25분) → 실습 2 (30분) → 실습 3 (40분)
```

산출물은 **두 저장소에 걸친다:**

| 어디 | 무엇 |
|---|---|
| `harness-edu2` → `docs/` | 웹사이트 (GitHub Pages) |
| `namojo/harness-edu` → `workshop/` | 실습 파일 원본. 학습자가 `git clone`으로 받는 것 |

**저장소를 새로 만들지 않는다.** 실습 환경은 기존 `namojo/harness-edu`에 추가한다. 그래서 이관된 설치가이드의 `git clone` URL과 실습 폴더 경로(51곳)를 하나도 건드리지 않는다 — 이관에서 가장 위험한 작업이 사라진다.

기존 사이트의 문제는 콘텐츠가 나빴던 것이 아니라 **어디서 시작해 어디서 끝나는지 안 보였던 것**이다. 그래서 이 하네스의 모든 판단은 하나의 질문으로 귀결된다: **이것이 120분 완주에 기여하는가?**

**실행 모드: 에이전트 팀** (Phase 2·3은 팀 내 병렬, Phase 4는 생성-검증 루프)

## Phase 0 · 컨텍스트 확인 — 반드시 먼저

무엇을 하는 실행인지 판별한다. 이걸 건너뛰면 이미 한 일을 다시 하거나, 적용된 수정을 되돌린다.

```bash
ls -la docs/ _workspace/ 2>/dev/null
cat _workspace/06_qa_report.md 2>/dev/null | head -40
```

| 상태 | 실행 모드 | 무엇을 하나 |
|---|---|---|
| `_workspace/` 없음 | **초기 실행** | Phase 1~5 전체 |
| `_workspace/` 있음 + 사용자가 **부분 수정** 요청 | **부분 재실행** | 해당 담당 에이전트만 재호출. 다른 산출물은 손대지 않는다 |
| `_workspace/` 있음 + **새 입력**(범위 변경, 실습 교체) | **새 실행** | 기존 `_workspace/`를 `_workspace_prev/`로 이동한 뒤 Phase 1부터 |
| `06_qa_report.md`에 미해소 결함 있음 | **결함 수정** | Phase 5로 직행. 결함별 담당에게 전달 |

부분 재실행에서 **어느 에이전트를 부를지의 매핑**:

| 사용자 요청 | 담당 |
|---|---|
| "실습 N 고쳐", "체크리스트 바꿔", "브리프 해설" | `practice-designer` |
| "개념 어려워", "패턴 설명 다시" | `concept-curator` |
| "설치가이드 링크 깨졌어" | `install-porter` |
| "디자인 바꿔", "복사 버튼 안 돼", "모바일에서 깨져" | `web-builder` |
| "실습 파일 준비", "sample.pptx", "다운로드 링크 404", "저장소에 추가" | `assets-steward` |
| "페이지 너무 많아", "용어 통일", "분량 줄여" | `edu-architect` |
| "점검해줘", "빠진 거 없나" | `edu-qa` |

## Phase 1 · 기준 확정 (단독)

**`edu-architect`를 먼저 단독 실행한다.** 용어사전이 확정되기 전에 다른 팀원이 원고를 시작하면 나중에 전부 고쳐야 한다.

```
Agent(subagent_type: "general-purpose", model: "opus", name: "edu-architect",
      prompt: "edu-site-ia 스킬을 읽고, .claude/agents/edu-architect.md 의 역할대로
               _workspace/00_architect_sitemap.md / _glossary.md / _tone.md 를 확정하라.
               기존 harness-edu/docs/ 구조를 참고하되, 버릴 것을 명시하라.")
```

산출: `00_architect_sitemap.md`, `00_architect_glossary.md`, `00_architect_tone.md`

**게이트:** 사이트맵의 본문 페이지가 5장인지 확인한다. 6장 이상이면 사용자에게 승인을 받고 진행한다.

## Phase 2 · 자료 확보와 원고 (팀 · 병렬)

세 갈래가 서로를 기다리지 않는다. 팬아웃이다.

| 팀원 | 작업 | 산출물 |
|---|---|---|
| `install-porter` | 설치가이드 5문서 이관 + 링크 재배선 + `workshop/` 안내 1행 | `docs/install/*`, `_workspace/03_porter_*.md` |
| `concept-curator` | 개념 페이지 원고 + 출처표 + 도식 명세 | `_workspace/02_curator_*.md` |
| `practice-designer` | 실습 3장 원고(9블록) + 필요 자산 정의 | `_workspace/04_practice_*.md` |

세 명을 **한 메시지에 함께 스폰**한다. 각각 `model: "opus"`.

### 이 Phase에서 확정해야 하는 결정 — sample.pptx

`practice-designer`가 후보 3개를 제시하고, **사용자 확인을 받는다.** 없는 파일을 가정한 설명은 실습 시간에 그대로 사고가 된다.

| 후보 | 판단 |
|---|---|
| 워크샵 덱에서 1장 발췌 | **권장** — 규칙 6종이 뚜렷, 저작권 명확, 2.7MB → 발췌로 축소 |
| `harness-edu/slide/AI행동계획_이행현황.pptx` | 표·차트 다양하나 마케팅과 톤이 멀다 |
| `harness-edu/slide/Cheil-NoSauce-47.pptx` | 마케팅에 근접하나 **외부 제작물 — 공개 배포 가능 여부 확인 전에는 쓰지 않는다** |

저장소 URL은 확인할 필요가 없다 — `namojo/harness-edu`를 계속 쓰기로 확정되어 있다.

### 팀 내 통신

- `concept-curator` ↔ `practice-designer`: 패턴 이름을 맞춘다. 개념 페이지와 실습 페이지의 패턴 이름이 갈리면 학습자는 15분 전에 배운 것을 못 알아본다. 정본은 `harness-concept-source` 스킬.
- `install-porter` → `edu-architect`: 차시→실습 매핑 승인 요청
- 세 명 모두 → `edu-architect`: 원고 제출

## Phase 2-B · 실습 자산과 저장소 환경 (단독, Phase 2와 병행 가능)

`assets-steward`가 실습 파일을 만들고 저장소 배치 계획을 세운다. **`practice-designer`가 필요 자산을 정의한 직후 시작**하며, `web-builder`보다 먼저 끝나야 한다 — 다운로드 URL이 확정되지 않으면 준비물 블록을 구현할 수 없다.

만드는 것:

```
namojo/harness-edu/workshop/
├── README.md
├── practice-1-youtube/README.md          브리프 원문 (입력 파일 없음)
├── practice-2-marketing/README.md        브리프 원문 + 결과 저장 안내
└── practice-3-pptx/
    ├── README.md
    ├── sample.pptx                        형식·디자인 참조 (확정 후)
    └── example-strategy.md                실습 2 우회 입력 (가상 브랜드)
```

산출: `_workspace/07_assets_manifest.md`, `_workspace/07_assets_repo_plan.md`, 준비물 블록 원고

**게이트:** `sample.pptx`가 요구 조건 9개를 충족하는지 **열어서** 확인했는가. 파일 존재만으로는 실습 3의 첫 단계(규칙 추출)가 성립하지 않는다.

**저장소 push는 사용자 몫이다.** 이 하네스는 `_workspace/assets/`에 파일을 만들고 `07_assets_repo_plan.md`에 적용 절차를 쓴다. 임의로 push하거나 다른 저장소를 만들지 않는다. **push 전에 만든 raw URL은 전부 404이므로, 링크 검증은 push 후에만 의미가 있다.**

## Phase 3 · 구현 (단독)

`web-builder`가 원고를 `docs/`로 조립한다. Phase 2가 **전부** 끝난 뒤 시작한다 — 원고가 반쯤 온 상태에서 시작하면 CSS를 두 번 쓴다.

`web-builder`에게 넘길 것:
- `_workspace/00_architect_sitemap.md`
- `_workspace/02_curator_concept.md` + `02_curator_diagrams.md`
- `_workspace/04_practice_1~3.md`
- `_workspace/07_assets_manifest.md` — **다운로드 URL과 용량은 여기서 복사한다. 페이지에서 조립하지 않는다**
- `install-porter`가 정리한 필수 CSS 클래스 목록

**게이트 — 구현 직후 확인:** `docs/index.html`에 `id="flow"`가 있는가. 이관된 설치 문서 5개의 앵커 대상이다. 없으면 5개 문서의 링크가 조용히 최상단으로 이동하고, 링크 검사만으로는 잡히지 않는다.

## Phase 4 · QA와 수정 루프 (생성-검증)

`edu-qa`가 검증하고 결함을 담당에게 직접 보낸다. **최대 2회 루프.** 3회째에도 같은 결함이 남으면 개별 결함이 아니라 골격 문제이므로 `edu-architect`에게 올린다.

```bash
# 정본 브리프를 텍스트로 떼어 둔다 (최초 1회)
mkdir -p _workspace/briefs
# practice-briefs.md 의 코드블록 3개를 practice-1.txt ~ practice-3.txt 로 저장

python3 .claude/skills/edu-site-qa/scripts/check_site.py    docs
python3 .claude/skills/edu-site-qa/scripts/check_briefs.py  docs _workspace/briefs
bash   .claude/skills/edu-site-qa/scripts/check_assets.sh   docs
bash   .claude/skills/install-guide-port/scripts/verify_port.sh docs
```

`check_assets.sh`는 네트워크를 쓴다. 저장소 push 전에는 raw URL이 404이므로, **push 전 실행 결과는 "미검증"으로 기록**하고 push 후 재실행한다.

**`BLOCKER`가 하나라도 있으면 완료 보고를 하지 않는다.**

스크립트로 잡히지 않는 것은 `edu-qa`가 사람 판단으로 본다: 체크리스트 판정 가능성, 예상 팀이 정답처럼 읽히는지, 분량, 복사 버튼 실제 동작, 학습자 시점 통과.

## Phase 5 · 인수와 피드백

1. **학습자 시점 통과 테스트** 결과 보고 — 홈 → 설치가이드 → 개념 → 실습 1·2·3 완주 가능 여부
2. **결함 요약** — BLOCKER 0건 확인, MAJOR/MINOR 잔여 목록
3. **미확정 항목 명시** — 자산 미확보, 사용자 확인 대기 중인 결정
4. 사용자에게 묻는다: *"실습 페이지에서 고치고 싶은 부분이 있나요? 팀 구성이나 흐름에 바꾸고 싶은 점은요?"*

피드백은 유형에 따라 반영 대상이 다르다:

| 피드백 | 고칠 곳 |
|---|---|
| "실습 결과 판정이 애매하다" | `practice-page-writing` 스킬의 체크리스트 규칙 |
| "개념이 어렵다" | `harness-concept-source` — 추상도를 낮춘다(예시를 실습에서 끌어온다). 분량을 줄이는 것보다 효과적이다 |
| "설치가이드가 새 사이트와 안 어울린다" | `edu-static-site`의 CSS. 이관 HTML은 고치지 않는다 |
| "파일을 못 받았다", "다운로드가 빈 화면" | `practice-assets` — `/raw/` 경로·브랜치명·push 여부 |
| "페이지가 너무 많다" | `edu-site-ia`의 페이지 예산 |
| "같은 지적이 두 번 나왔다" | 개별 원고가 아니라 **스킬**을 고친다 |

변경은 `CLAUDE.md` 변경 이력에 기록한다.

## 데이터 전달 규약

- **파일 기반**(산출물) + **메시지 기반**(조율)
- 중간 산출물은 `_workspace/{순번}_{담당}_{산출물}.md`. 최종물만 `docs/`
- **`_workspace/`는 지우지 않는다** — 부분 재실행과 회귀 검사의 근거다

```
_workspace/
├── 00_architect_sitemap.md / _glossary.md / _tone.md
├── 02_curator_concept.md / _sources.md / _diagrams.md
├── 03_porter_mapping.md / _residual.md
├── 04_practice_1_youtube.md / _2_marketing.md / _3_pptx.md / _assets.md
├── 05_builder_components.md
├── 06_qa_report.md
├── 07_assets_manifest.md / _repo_plan.md
├── assets/                          ← 저장소에 넣을 파일 실물 (push 전 보관)
└── briefs/practice-1.txt ~ practice-3.txt
```

## 에러 핸들링

| 상황 | 처리 |
|---|---|
| 에이전트 실패 | 1회 재시도. 재실패 시 그 산출물 없이 진행하고 **최종 보고에 누락을 명시**한다 |
| 원본 문서 접근 불가 | 추측으로 채우지 않는다. `[원본 확인 필요]`로 표시 |
| 자산 미확보 (sample.pptx 등) | 해당 페이지를 완성하지 않고 `[자산 미확정]` 표시 + 사용자 확인 |
| 저작권 불확실한 자산 | 후보에서 **제외**. "아마 괜찮을 것"으로 공개 저장소에 올리지 않는다 |
| 저장소 push 권한 없음 | `07_assets_repo_plan.md`에 절차를 쓰고 사용자에게 넘긴다. 다른 저장소를 만들지 않는다 |
| 다운로드 링크 404 | push 전이면 정상. push 후 404면 브랜치명(`main`)·경로 확인 |
| 원고끼리 상충 | 삭제하지 않고 병기 + `edu-architect`가 판정 |
| 사용자 지시 ↔ pptx 정본 충돌 | **사용자 지시 우선**, 차이를 리포트에 남긴다 |
| QA 스크립트 실패 | 결함 없음으로 처리하지 않는다. "검사 실패 — 미검증" 명시 |
| 페이지 수가 5장을 넘음 | 사용자 승인 없이 늘리지 않는다 |

## 테스트 시나리오

### 정상 흐름 — 초기 실행

입력: *"harness-edu2 사이트를 만들어줘"*

1. Phase 0 → `_workspace/` 없음 → 초기 실행
2. Phase 1 → 사이트맵 5장 확정, 용어사전 배포
3. Phase 2 시작 시 사용자에게 sample.pptx 후보 확인 → 3명 병렬 실행
4. Phase 2-B → `assets-steward`가 `workshop/` 파일 생성 + 매니페스트
5. Phase 3 → `docs/` 7페이지 + `id="flow"` + 준비물 블록 3개 확인
6. Phase 4 → 스크립트 4종 통과, BLOCKER 0 (raw URL은 push 후 재검증)
7. Phase 5 → 학습자 시점 통과 보고 + 저장소 적용 절차 안내 + 피드백 요청

기대: 본문 5장 + 이관 5문서, 브리프 3편 정본 일치, 깨진 링크 0, `workshop/` 파일 6개 준비 완료

### 에러 흐름 — 자산 미확보 상태에서 완주 요구

입력: *"실습 3까지 다 만들어줘"* (sample.pptx 미확정)

1. Phase 2에서 `practice-designer`가 후보 3개 제시하며 확인 요청
2. 사용자가 답하지 않으면 → 실습 3 페이지를 `[자산 미확정]`으로 표시하고 **나머지는 전부 완성**
3. Phase 4 → `check_site.py`가 실습 3의 `sample.pptx` 참조 누락을 `BLOCKER`로 검출
4. Phase 5 → "실습 1·2와 개념·설치가이드는 완성. 실습 3은 샘플 pptx 확정 후 마감 가능"으로 보고

기대: 미확정을 완료로 보고하지 않는다. 확정된 부분은 전부 완성한다.

### 부분 재실행 흐름

입력: *"실습 2 체크리스트가 애매해. 다시 써줘"*

1. Phase 0 → `_workspace/` 있음 + 부분 수정 → `practice-designer`만 재호출
2. `04_practice_2_marketing.md`를 읽고 체크리스트 블록만 수정 (다른 블록·다른 실습은 손대지 않는다)
3. `web-builder`가 해당 섹션만 재구현
4. `edu-qa`가 회귀 검사 — 이전 결함이 되살아나지 않았는지

기대: 실습 1·3과 개념 페이지가 변하지 않는다.
