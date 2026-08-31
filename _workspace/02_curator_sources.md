# 개념 페이지 출처 매핑

원본이 갱신되었을 때 어느 문장을 고쳐야 하는지 찾기 위한 표.

| 개념 페이지의 주장 | 출처 | 인용 형태 |
|---|---|---|
| 하네스는 업무 설명을 AI 팀 구조로 바꿔 준다 | `README_KO.md` §개요 | 재서술 |
| 에이전트(누가) × 스킬(어떻게) 분리 | `README_KO.md` §개요 · `SKILL.md` 핵심 원칙 | 재서술 |
| 하네스 진화 메커니즘 + 도식 구조 | `README_KO.md` §하네스 진화 메커니즘 | 도식 구조 인용 |
| 메타스킬 6단계 (도메인 분석 → 아키텍처 설계 → 에이전트 정의 → 스킬 생성 → 오케스트레이션 → 검증) | `skills/harness/SKILL.md` §워크플로우 | **단계명 직접 인용** |
| 6패턴 이름·정의 (파이프라인 / 팬아웃·팬인 / 전문가 풀 / 생성-검증 / 감독자 / 계층적 위임) | `README_KO.md` §아키텍처 패턴 | **이름 직접 인용** |
| 각 패턴의 "이럴 때 고른다" | `references/agent-design-patterns.md` | 재서술 |
| 패턴 선택 3질문 | 워크샵 pptx 슬라이드 9 | 표현 계승 |
| 설치 명령 `/plugin marketplace add revfactory/harness` | `README_KO.md` §설치 | 직접 인용 |
| 트리거 `하네스를 구성해줘` | `README_KO.md` §사용법 | 직접 인용 — **실습 1 브리프 첫 줄이 이것이다** |

## 교재가 의도적으로 원본과 다르게 한 것

각주로 본문에 명시했다. QA는 이것을 불일치로 잡지 않는다.

| 항목 | 원본 | 교재 | 본문 각주 위치 |
|---|---|---|---|
| 아키텍처 패턴 개수 | 8개 | **6개** + 심화 2종 이름만 | 3부 패턴 카드 아래 `.src` |
| 메타스킬 단계 | Phase 0~7 (8단계) | **6단계** (Phase 1~6) | 2부 `.src` |

## 원본 갱신 감지

개념 페이지를 손볼 때 실행한다.

```bash
grep -n -A 14 "### 아키텍처 패턴" /Users/andy/Work/harness/README_KO.md
grep -n "^### Phase" /Users/andy/Work/harness/skills/harness/SKILL.md
grep -rn "plugin marketplace add\|plugin install harness" /Users/andy/Work/harness/README_KO.md
```

바뀐 것이 있으면 위 표를 먼저 갱신하고, 그 다음 `docs/concept.html` 의 해당 문장을 고친다.

## 이 실행에서 중간 원고 파일을 만들지 않은 이유

원고(`02_curator_concept.md`, `04_practice_*.md`)를 마크다운으로 거치지 않고 HTML에 직접 썼다. 따라서 **원고의 정본은 `docs/` 의 HTML**이다.

부분 재실행 시 주의: `docs/concept.html` · `docs/practice/*.html` 을 직접 읽고 고친다. 없는 중간 원고를 찾지 말 것. 브리프 원문의 정본만 `_workspace/briefs/*.txt` 에 별도로 있고, 이것이 QA 대조 기준이다.
