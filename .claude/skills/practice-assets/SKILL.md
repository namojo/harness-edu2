---
name: practice-assets
description: 실습 자산(sample.pptx, 예시 전략보고서, 브리프 텍스트 등)의 정의·제작·저장소 배치·웹 다운로드 안내 규격. namojo/harness-edu 저장소에 실습 환경을 추가하고 harness-edu2 웹페이지에 다운로드 블록을 만들 때 반드시 사용. "실습 파일 준비", "샘플 pptx 만들어", "다운로드 링크 추가", "저장소에 실습 환경 추가", "자산 확인", "학습자가 파일을 못 받아" 요청 시 사용. 사이트 전체 구축·개편처럼 여러 담당이 걸리는 작업이면 harness-edu2-build 오케스트레이터가 이 스킬을 호출한다.
---

# 실습 자산 준비와 다운로드 안내

## 왜 자산이 별도 관심사인가

실습 페이지에 "샘플 PPT를 첨부하세요"라고 쓰는 것은 쉽다. 그 파일이 학습자 손에 들어가게 만드는 것은 별개의 일이고, 이쪽을 빼먹으면 페이지는 완벽해 보이지만 실습은 시작되지 않는다.

**교실에서 실제로 벌어지는 것:** 사전 준비를 마친 학습자는 `clone`한 폴더에서 파일을 찾는다. 지각한 학습자와 노트북을 바꿔 온 학습자는 그 폴더가 없다. **두 경로를 모두 제공하지 않으면 반드시 절반이 막힌다.**

## 저장소 구조 — `namojo/harness-edu`에 추가한다

**저장소를 새로 만들지 않는다.** 사이트만 harness-edu2로 개편하고, 실습 파일은 기존 저장소에 추가한다.

이 결정의 실질적 효과: 이관된 설치가이드의 `git clone` URL과 실습 폴더 경로(`~/harness-edu`, `C:\harness-edu` — 총 51곳, `.ps1` 자동 점검 스크립트 포함)를 **하나도 건드리지 않는다.** 저장소를 새로 만들면 그 51곳이 전부 치환 대상이 되고, 한 곳만 남아도 학습자는 존재하지 않는 폴더로 `cd`하려다 막힌다. 그리고 그 원인이 문서에 있다는 것을 알아낼 방법이 없다.

추가할 구조:

```
namojo/harness-edu/                     ← 기존 저장소, 기존 폴더들은 그대로
├── ...(기존 ad/ codex/ harness/ map/ slide/ tool/ xlsx/ 유지)
└── workshop/                           ← 신규. 120분 워크샵 실습 환경
    ├── README.md                        무엇이 들어 있고 각 실습에서 어떻게 쓰는지
    ├── practice-1-youtube/
    │   └── README.md                    브리프 원문 + 실행 방법 (파일 입력 없음)
    ├── practice-2-marketing/
    │   └── README.md                    브리프 원문 + 결과를 어디에 저장할지
    └── practice-3-pptx/
        ├── README.md                    브리프 원문 + sample.pptx 사용법
        ├── sample.pptx                  형식·디자인 참조 원본
        └── example-strategy.md          실습 2를 건너뛴 학습자용 우회 입력
```

`workshop/`으로 묶는 이유: 기존 저장소에는 1세대 7차시용 폴더가 이미 여럿 있다. 워크샵 자산을 루트에 흩으면 학습자가 자기 실습과 무관한 폴더 사이에서 헤맨다.

**각 실습 폴더에 `README.md`를 반드시 둔다.** 폴더만 있고 설명이 없으면 학습자는 그 파일을 어떻게 쓰는지 웹페이지로 돌아가 확인해야 한다. README에는 브리프 원문을 그대로 넣는다 — 오프라인에서도 실습이 가능해진다.

## 자산 목록

| 자산 | 실습 | 왜 필요한가 | 없으면 |
|---|---|---|---|
| `sample.pptx` | 3 | 형식 규칙 6종을 추출할 대상 | 실습 3이 시작되지 않는다 (BLOCKER) |
| `example-strategy.md` | 3 | 실습 2를 건너뛴 학습자의 입력 | 교실 절반이 실습 3에서 멈춘다 |
| 실습별 `README.md` | 1·2·3 | 브리프 원문 오프라인 사본 | 웹을 계속 왕복해야 한다 |

실습 1·2는 **입력 파일이 없다.** 브리프 한 편이 전부이므로 자산을 억지로 만들지 않는다. 실습 1·2의 준비물은 "Claude Code가 실행 가능한 상태"뿐이며, 그것은 설치가이드가 담당한다.

### sample.pptx 요구 조건

파일이 존재하는 것으로 끝이 아니다. **열어 보고 아래를 확인한다.** 규칙이 흐릿한 슬라이드를 주면 실습 3의 첫 단계(규칙 추출)가 성립하지 않는다.

| 조건 | 확인 방법 |
|---|---|
| 1장 (또는 대표 1장이 분명) | 슬라이드 수 확인 |
| 폰트 계층이 3단 이상 구분됨 | 제목/소제목/본문의 크기 차이가 눈에 보이는가 |
| 외곽 여백이 일정함 | 가장자리 안전 영역이 눈에 잡히는가 |
| 좌측 정렬선이 뚜렷함 | 요소들이 같은 x좌표에서 시작하는가 |
| 색의 역할이 구분됨 | 지배색 / 강조색 / 상태색이 나뉘어 쓰이는가 |
| 반복 단위(카드 등)가 있음 | 정보를 담는 같은 모양이 2개 이상 있는가 |
| 텍스트가 편집 가능 | 이미지로 굽힌 슬라이드가 아닌가 |
| 저작권이 명확 | 자체 제작 또는 공개 자료인가 |
| 50MB 미만 | `ls -lh` — GitHub는 100MB 초과를 거부, 50MB부터 경고 |

```bash
python3 -c "
from pptx import Presentation
p = Presentation('sample.pptx')
print('슬라이드:', len(p.slides))
print('크기:', p.slide_width, 'x', p.slide_height)
for sh in p.slides[0].shapes:
    kind = sh.shape_type
    if sh.has_text_frame and sh.text_frame.text.strip():
        sizes = {r.font.size.pt for para in sh.text_frame.paragraphs
                 for r in para.runs if r.font.size}
        print(f'  {kind} 폰트pt={sorted(sizes) or \"상속\"} :: {sh.text_frame.text.strip()[:40]!r}')
    else:
        print(f'  {kind}')
"
```

폰트 크기가 전부 "상속"으로 나오면 레이아웃 마스터에 있는 것이므로, 실습에서 규칙 추출이 한 단계 더 어려워진다. 그런 파일은 후보에서 내린다.

### 후보와 권장

| 후보 | 경로 | 장점 | 단점 |
|---|---|---|---|
| **워크샵 덱에서 1장 발췌** (권장) | 이 저장소의 `harness-engineering-workshop-ko-final*.pptx` | 규칙 6종이 매우 뚜렷, 교재와 톤 일치, 저작권 명확, 발췌로 용량 축소 가능 | 학습자가 "이미 본 디자인"을 재현하게 됨 |
| KRDS 보고 슬라이드 | `harness-edu/slide/AI행동계획_이행현황.pptx` | 표·차트·상태색이 다양, 공공 보고 형식 | 마케팅 전략보고서와 톤이 멀다 |
| 광고 제안서 | `harness-edu/slide/Cheil-NoSauce-47.pptx` | 마케팅 맥락에 가장 근접 | **외부 제작물 — 공개 배포 가능 여부 확인 전에는 쓰지 않는다** |

**권장은 워크샵 덱 발췌.** "이미 본 디자인" 문제는 실습 3 페이지에서 프레이밍으로 해소한다: *"익숙한 디자인의 규칙을 언어로 뽑아 보는 것이 이 실습의 목적입니다."* 오히려 학습자가 결과를 판정하기 쉬워진다 — 원본을 알고 있으니까.

저작권이 불확실한 파일은 후보에서 제외한다. "아마 괜찮을 것"으로 공개 저장소에 올리지 않는다.

### example-strategy.md 요구 조건

실습 2의 산출물 **형태를 그대로** 갖춰야 한다. 형태가 다르면 실습 3의 팀이 입력을 해석하는 데서 시간을 쓴다.

- 1페이지 요약 (**"무엇을 하지 않을 것인가"를 포함** — 실습 2 체크리스트 항목이다)
- 실행 우선순위 표 (판단 근거 열 포함)
- 측정지표
- `[사실]` / `[가정]` 표기 구분
- 외부 주장에 출처 표기

**가상의 브랜드로 작성한다.** 실제 브랜드의 전략을 교육용으로 배포하면 그 자체가 문제가 된다. 출처 표기는 형식을 보여주기 위한 것이므로, 가상 브랜드에는 "교육용 예시 — 실제 데이터 아님"을 문서 상단에 명시한다.

## 웹 다운로드 안내 — 실습 페이지 "준비물" 블록

별도 다운로드 페이지를 만들지 않는다. 실습 중에 아무도 찾아가지 않는다. **각 실습 페이지의 블록 2(준비물)** 에 그 실습에 필요한 것만 둔다.

두 경로를 나란히 제시한다:

```html
<section class="prep">
  <h2 id="준비물">준비물</h2>

  <div class="prep-row">
    <span class="prep-k">A. 실습 저장소를 받은 경우</span>
    <p>설치가이드를 마쳤다면 이미 있습니다.
       <code>harness-edu/workshop/practice-3-pptx/</code> 폴더를 Claude Code에서 열면 됩니다.</p>
  </div>

  <div class="prep-row">
    <span class="prep-k">B. 개별 다운로드</span>
    <ul class="dl-list">
      <li><a class="dl" href="https://github.com/namojo/harness-edu/raw/main/workshop/practice-3-pptx/sample.pptx"
             download>sample.pptx <span class="dl-meta">형식 참조 원본 · 약 400KB</span></a></li>
      <li><a class="dl" href="https://github.com/namojo/harness-edu/raw/main/workshop/practice-3-pptx/example-strategy.md">
             example-strategy.md <span class="dl-meta">실습 2를 건너뛴 경우의 입력</span></a></li>
    </ul>
  </div>
</section>
```

### 다운로드 링크 규칙

1. **`/raw/` 경로를 쓴다.** `github.com/{user}/{repo}/raw/{branch}/{path}` 는 파일 자체를 내려준다. `github.com/.../blob/...` 는 HTML 미리보기 페이지이며, pptx는 미리보기가 안 되므로 학습자가 "빈 화면"을 보게 된다.
2. **기본 브랜치는 `main`이다** (2026-08-31 확인: `namojo/harness-edu` → `origin/main`). 확인 없이 `master`로 쓰면 전부 404다. 저장소가 바뀌면 다시 확인한다:
   ```bash
   git -C /Users/andy/Work/harness-edu rev-parse --abbrev-ref HEAD   # → main
   ```
3. **파일 크기를 링크에 표시한다.** 교실 와이파이에서 40MB를 모르고 누르는 것과 알고 누르는 것은 다르다.
4. **무엇에 쓰는 파일인지 한 줄로 적는다.** 파일명만으로는 학습자가 이 파일이 자기에게 필요한지 판단할 수 없다.
5. **`docs/assets/`에도 사본을 둘지 결정한다.** 두면 사이트에서 바로 서브되어 저장소 접근 문제와 무관해지지만, 같은 파일이 두 곳에 생겨 갱신이 갈린다.
   - **권장: 저장소 raw 링크 하나만.** 자산이 곧 실습 환경이므로 저장소가 정본이다. 사본을 두면 어느 쪽이 최신인지 알 수 없게 된다.
   - 예외 — 저장소가 private이거나 사내망에서 GitHub 접근이 막히는 환경이면 `docs/assets/`에 두고 매니페스트에 "사본 있음, 저장소가 정본"을 명시한다.

## 매니페스트

`_workspace/07_assets_manifest.md`에 자산별로 기록한다. 표만 있고 검증 결과가 없으면 매니페스트가 아니라 희망 목록이다.

| 파일 | 용량 | 실습 | 저장소 경로 | 웹 다운로드 URL | 출처/저작권 | 검증 |
|---|---|---|---|---|---|---|
| `sample.pptx` | 412KB (워크샵 덱 원본은 2.7MB — 1장 발췌로 축소) | 3 | `workshop/practice-3-pptx/sample.pptx` | `.../raw/main/workshop/practice-3-pptx/sample.pptx` | 자체 제작 (워크샵 덱 발췌) | 규칙 6종 확인 ✓ / 편집 가능 ✓ / 링크 200 ✓ |

## 저장소 반영

저장소에 직접 push할 권한이 없거나 사용자 확인이 필요하면, `_workspace/07_assets_repo_plan.md`에 **그대로 실행 가능한 형태**로 쓴다. 임의로 다른 저장소를 만들지 않는다.

```markdown
## namojo/harness-edu 에 추가할 것

1. `workshop/` 디렉토리 생성
2. 아래 파일 추가 (본 하네스가 `_workspace/assets/` 에 생성해 둠)
   - workshop/README.md
   - workshop/practice-1-youtube/README.md
   - workshop/practice-2-marketing/README.md
   - workshop/practice-3-pptx/README.md
   - workshop/practice-3-pptx/sample.pptx
   - workshop/practice-3-pptx/example-strategy.md
3. 기본 브랜치에 push (다운로드 링크가 `/raw/<브랜치>/` 를 가리킴)
4. push 후 각 raw URL을 실제로 열어 200을 확인
```

**4번을 생략하지 않는다.** push 전에 만든 링크는 전부 404이고, 링크 검사는 push 후에만 의미가 있다.

## 자주 나는 결함

| 결함 | 왜 생기나 | 어떻게 막나 |
|---|---|---|
| 다운로드 링크가 HTML 페이지를 열어 준다 | `/blob/` 경로 사용 | `/raw/` 로 |
| 링크 전부 404 | 브랜치 이름 추측 (`main` vs `master`) | `git rev-parse --abbrev-ref HEAD` 로 확인 |
| push 전 링크를 "확인했다"고 보고 | 링크 검사 시점을 놓침 | push 후 재검증 |
| 저장소 clone 경로가 안 맞음 | 저장소를 새로 만들려고 함 | `namojo/harness-edu` 유지 — 설치가이드 51곳을 안 건드린다 |
| sample.pptx로 규칙 추출이 안 됨 | 파일 존재만 확인 | 요구 조건 9개를 열어서 확인 |
| 예시 전략보고서가 실습 2 형태와 다름 | 자유롭게 작성 | 실습 2 체크리스트 7항목을 그대로 만족시킨다 |
| 실제 브랜드 전략을 예시로 배포 | 그럴듯한 예시를 만들려다 | 가상 브랜드 + "교육용 예시" 명시 |
| 같은 파일이 두 곳에서 갈림 | 저장소와 `docs/assets/`에 사본 | 저장소를 정본으로 하고 사본을 두지 않는다 |
