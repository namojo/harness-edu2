# harness-edu2 — 하네스 엔지니어링 120분 워크샵

> **교재: https://namojo.github.io/harness-edu2**

프롬프트 한 번을 반복 가능한 AI 팀으로. 코드를 쓰지 않는 실무자를 위한 **개념 15분 + 실습 3개** 워크샵 교재입니다.

## 구성

```
설치가이드(사전 25~35분) → 개념 15분 → 실습 1 (25분) → 실습 2 (30분) → 실습 3 (40분)
```

| 페이지 | 내용 |
|---|---|
| [개념](https://namojo.github.io/harness-edu2/concept.html) | 하네스 엔지니어링 · 메타스킬 6단계 · 6가지 아키텍처 패턴 · 패턴 선택 3질문 |
| [실습 1](https://namojo.github.io/harness-edu2/practice/1-youtube.html) | 유튜브 콘텐츠 기획 팀 — 한 문장으로 팀을 만든다 |
| [실습 2](https://namojo.github.io/harness-edu2/practice/2-marketing.html) | 브랜드 마케팅 전략보고서 — 팬아웃/팬인 + 생성-검증 |
| [실습 3](https://namojo.github.io/harness-edu2/practice/3-pptx.html) | 샘플 형식으로 새 PPT — 파이프라인 + 검토 분리 |
| [설치가이드](https://namojo.github.io/harness-edu2/install/) | 필수 1개 + 선택 2개. 터미널을 처음 열어도 됩니다 |

세 실습은 난이도 순서가 아니라 **한 팀이 성장하는 세 단계**입니다 — 팀을 만든다 → 구조를 고른다 → 산출물을 다듬는다. 실습 3은 실습 2의 산출물을 입력으로 씁니다.

## 시작하기

```
/plugin marketplace add revfactory/harness
/plugin install harness@harness-marketplace
```

Claude Pro / Max / Team / Enterprise 중 하나가 필요하고 **API Key는 필요하지 않습니다.** 자세한 절차는 [설치가이드](https://namojo.github.io/harness-edu2/install/)에 있습니다.

## 실습 파일

실습 파일은 **[namojo/harness-edu](https://github.com/namojo/harness-edu) 저장소의 `workshop/` 폴더**에 있습니다. 이 저장소에는 웹 교재만 들어 있습니다.

```bash
git clone https://github.com/namojo/harness-edu.git
cd harness-edu/workshop
```

실습 1·2는 입력 파일이 없고 브리프 한 편이 전부입니다. 실습 3만 `sample.pptx` 와 실습 2의 산출물을 씁니다.

## 이 저장소의 구성

```
docs/                     GitHub Pages (웹 교재)
├── index.html            홈
├── concept.html          개념
├── practice/             실습 1·2·3
├── install/              설치가이드 (1세대 harness-edu에서 이관)
└── assets/               단일 CSS + 단일 JS
.claude/                  이 사이트를 만든 하네스 (에이전트 7 + 스킬 8)
_workspace/               설계 판단 기록 · QA 리포트 · 브리프 정본
```

빌드 도구·프레임워크를 쓰지 않습니다. `docs/` 를 push하면 그대로 배포됩니다.

## 1세대와의 관계

1세대 [harness-edu](https://github.com/namojo/harness-edu)는 7차시 + 확장트랙으로 커져, 어디서 시작해 어디서 끝나는지가 보이지 않았습니다. harness-edu2는 **120분 워크샵 하나**만을 위해 설치가이드 + 개념 + 실습 3개로 줄인 것입니다. 설치가이드는 1세대에서 무손실 이관했습니다.

## 출처

개념·메타스킬·아키텍처 패턴은 [revfactory/harness](https://github.com/revfactory/harness)를 정본으로 인용했습니다. 교재가 원본과 의도적으로 다르게 한 부분(패턴 8→6개, 메타스킬 8→6단계)은 본문 각주에 명시했습니다.

## 라이선스

교재 텍스트는 교육 목적으로 자유롭게 쓰되, 실습에 쓰이는 참조 자료(`sample.pptx` 등)는 각 자료의 권리자에게 귀속됩니다.
