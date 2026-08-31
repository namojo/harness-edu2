---
name: install-guide-port
description: 기존 harness-edu 설치가이드를 harness-edu2로 무손실 이관하는 절차 — 복사 범위, 링크·차시 참조 재배선, 잔여 문자열 검증. "설치가이드 가져와", "설치 문서 이관", "install 페이지 옮겨", "링크 깨졌어", "차시 참조 남았어", "설치가이드 링크 고쳐" 요청 시 반드시 사용. 설치 문서의 본문을 새로 쓰는 것이 아니라 그대로 옮기는 것이 이 스킬의 전제다. 사이트 전체 구축·개편처럼 여러 담당이 걸리는 작업이면 harness-edu2-build 오케스트레이터가 이 스킬을 호출한다.
---

# 설치가이드 무손실 이관

## 왜 "무손실"이 원칙인가

설치 문서의 명령어는 이미 현장에서 검증됐다. 문장을 다듬다가 명령 한 글자가 바뀌면 학습자의 터미널이 멈추고, 그 순간 강의가 멈춘다. 개선 아이디어가 떠올라도 이관 작업에서는 실행하지 않는다 — 이관이 끝난 뒤 별도 작업으로 분리한다.

**이관에서 바꾸는 것은 네 종류뿐이다:** 네비게이션 링크 · 브랜드 표기 · 상대 경로 · 차시 참조.

## 대상 파일

| 원본 | 대상 | 위계 |
|---|---|---|
| `harness-edu/docs/install/index.html` | `docs/install/index.html` | 설치가이드 홈 |
| `harness-edu/docs/install/setup-windows.html` | 동일 | **필수** · 공통 준비 |
| `harness-edu/docs/install/setup-mac.html` | 동일 | **필수** · 공통 준비 |
| `harness-edu/docs/install/codex.html` | 동일 | 선택 |
| `harness-edu/docs/install/mcp-server.html` | 동일 | 선택 |
| `harness-edu/docs/install/setup-windows.ps1` | 동일 | 자동 점검 스크립트 |
| `harness-edu/docs/assets/site.css` · `site.js` | `docs/assets/` | 설치 문서가 의존 |

"필수 1개 + 선택 2개" 위계는 새 사이트에서도 보존한다. 위계를 흐리면 학습자가 MCP까지 다 설치해야 하는 줄 안다.

### 이관하면서 한 곳만 내용을 보탠다 — 실습 파일 안내

설치가이드의 "실습 파일 여는 방법" 절은 1세대 폴더들(`ad/`, `xlsx/`, `map/` 등)을 전제로 쓰여 있다. 워크샵 실습 환경은 같은 저장소의 `workshop/` 아래에 추가되므로, **그 폴더를 가리키는 한 문장을 보탠다:**

> 이 과정의 실습 파일은 `workshop/` 폴더에 있습니다. 실습 1·2는 입력 파일이 없고, 실습 3은 `workshop/practice-3-pptx/sample.pptx` 를 씁니다.

**넣을 위치는 정해져 있다.** `install/index.html`의 194~199행 부근에 이미 실습 폴더 구조 트리가 있다(`xlsx/`, `ad/`, `codex/` … 를 나열한 블록). 그 트리에 한 행을 추가하고 위 문장을 붙인다:

```
├── workshop/      ← 이 과정의 실습 (1·2·3)
├── xlsx/
├── ad/
...
```

별도 절을 새로 만들지 않는다. 학습자가 폴더 구조를 확인하는 바로 그 자리에 두는 것이 찾아가야 하는 새 절보다 낫다.

이것이 무손실 원칙의 유일한 예외다. 이유: 학습자가 clone은 성공했는데 자기 실습 폴더를 못 찾는 상황을 막는 것이 문서를 그대로 두는 것보다 우선한다. 명령어·절 번호·앵커는 여전히 건드리지 않는다.

## 절차

### 1단계 · 원본 스냅샷 확보

```bash
cp -R /Users/andy/Work/harness-edu/docs/install ./docs/install
mkdir -p docs/assets
cp /Users/andy/Work/harness-edu/docs/assets/site.css docs/assets/
cp /Users/andy/Work/harness-edu/docs/assets/site.js  docs/assets/
touch docs/.nojekyll
```

`.nojekyll`이 없으면 GitHub Pages가 `_`로 시작하는 경로를 무시한다. 지금 문제가 없어도 나중에 자산을 추가할 때 조용히 깨진다.

### 2단계 · 차시 → 실습 매핑을 먼저 확정한다

**문서를 읽으면서 즉석에서 고치지 않는다.** 문서마다 다른 표현이 남는다. 먼저 표를 만들고 승인받은 뒤 일괄 치환한다.

```bash
grep -rn "차시\|chapters/" docs/install/   # 실측 44건 + chapters/ 1건
```

매핑 기준선 (실제 grep 결과로 검증 후 확정한다):

| 원본 참조 | 대응 | 처리 |
|---|---|---|
| `1차시 · 나의 업무 지도` | 실습 1 | `실습 1 · 유튜브 콘텐츠 기획 팀` + `../practice/1-youtube.html` |
| `4차시 전문가 팀 만들기` | 실습 1 | 같음 |
| `5차시 지저분한 데이터` | 대응 없음 | 문장 삭제 또는 일반화 |
| `6차시 계산 도구(MCP)` | 선택 · MCP | `MCP 서버 설치가이드` (차시 표현 제거, 문서 링크만) |
| `7차시 커리큘럼` | 대응 없음 | `120분 워크샵 흐름` + `../index.html` |
| `chapters/ch1.html` 등 | — | 위 매핑에 따라 재배선, 대응 없으면 링크 해제 |

**대응이 없는 참조는 임의로 가장 가까운 실습에 붙이지 않는다.** 예를 들어 "5차시에서 배운 지저분한 데이터 처리"를 실습 2에 연결하면 실습 2에 없는 내용을 배웠다고 학습자가 오해한다. 문장을 삭제하거나 "본 과정에서는 다루지 않습니다"로 일반화한다.

### 3단계 · 네비게이션 재배선

새 구조의 상단 네비게이션 (`_workspace/00_architect_sitemap.md`가 정본):

```html
<nav aria-label="주요 메뉴">
  <a href="../index.html">과정 홈</a>
  <a href="../concept.html">개념</a>
  <a href="../practice/1-youtube.html">실습 1</a>
  <a href="../practice/2-marketing.html">실습 2</a>
  <a href="../practice/3-pptx.html">실습 3</a>
  <a href="index.html" aria-current="page">설치가이드</a>
</nav>
```

`aria-current="page"`는 현재 페이지 링크에만 남긴다. 설치 문서 5개 모두 설치가이드 항목에 붙는다.

하단 페이저·"다음 단계" 카드도 함께 고친다. 특히 **설치 완료 후의 다음 목적지는 "개념"이 아니라 "실습 1"** 로 향하게 한다. 설치를 끝낸 사람의 관심은 "이게 진짜 돌아가나"이고, 그 확인은 실습에서 된다.

### 4단계 · 브랜드·경로·저장소 URL

| 대상 | 처리 |
|---|---|
| `<title>` 접미사 `· harness-edu` | `· harness-edu2` |
| `.brand-full` 텍스트 `harness-edu` | `harness-edu2` |
| `github.com/namojo/harness-edu` | **그대로 둔다.** 실습 저장소는 계속 이 저장소를 쓴다 (§4-1) |
| `../assets/site.css` 등 상대 경로 | 새 디렉토리 깊이(`docs/install/` → `../assets/`)가 원본과 같으므로 그대로 둔다. 확인만 한다 |

### 4-1. `harness-edu` 문자열은 세 가지 서로 다른 것이다 — ①만 치환한다

원본 5문서에 `harness-edu`는 90회 등장하는데, 의미가 셋으로 갈린다. 셋을 같은 규칙으로 치환하면 그중 둘이 반드시 틀린다.

| 종류 | 실제 등장 | 처리 |
|---|---|---|
| **① 브랜드·제목** — `<title>`, `.brand-full`, 설명문 | 약 10회 | `harness-edu2` **로 치환** |
| **② 저장소 URL** — `github.com/namojo/harness-edu` | 6회 (`git clone` 4회 + 링크 2회, `.ps1` 포함) | **그대로 둔다** |
| **③ 실습 폴더 경로** — `~/harness-edu`(20회), `C:\harness-edu`(31회) | 51회 | **그대로 둔다** |

### 왜 ②·③을 건드리지 않는가

**실습 저장소는 `namojo/harness-edu`를 계속 쓴다.** 사이트만 harness-edu2로 개편하고, 워크샵 실습 환경은 기존 저장소의 `workshop/` 아래에 **추가**한다 (`practice-assets` 스킬 참조).

이 결정 덕분에 이관에서 가장 위험한 작업이 사라진다. ③의 폴더 경로는 `git clone <URL> <경로>` → 이후 모든 `cd`·`Set-Location`·경로 확인 명령·트러블슈팅 예시·`setup-windows.ps1` 자동 점검 스크립트에 걸쳐 51회 반복된다. **한 곳만 놓쳐도 학습자는 존재하지 않는 폴더로 이동하려다 막히고, 원인이 문서에 있다는 것을 알아낼 방법이 없다.** 그 51곳을 치환하지 않는 것이 가장 안전하다.

### 그래서 치환은 ①만, 좁게 한다

`harness-edu`를 통째로 치환하면 ②·③까지 잡혀 51곳이 깨진다. **브랜드가 나타나는 자리만 지정해 치환한다:**

```bash
# ① 브랜드·제목만. 저장소 URL(github.com/...)과 폴더 경로(~/, C:\)는 건드리지 않는다
LC_ALL=C find docs/install -type f -name '*.html' -exec sed -i '' -E \
  -e 's|· harness-edu<|· harness-edu2<|g' \
  -e 's|(class="brand-full">)harness-edu<|\1harness-edu2<|g' \
  -e 's|harness-edu (설치가이드\|과정\|커리큘럼)|harness-edu2 \1|g' {} +
```

**일괄 치환 후 반드시 눈으로 확인한다.** `<title>`·`.brand-full`·`<meta name="description">` 세 곳이 바뀌었고, `git clone` 줄과 `cd` 줄은 그대로인지. 이 검증은 스크립트로 못 잡는다 — 5단계 잔여 검색이 잡아 주는 것은 "남았다"는 사실뿐이고, 남은 것이 남아야 할 것인지는 사람이 판단한다.

**`.ps1`은 치환 대상이 아니다.** 자동 점검 스크립트에는 브랜드 표기가 없고 폴더 경로만 있다. 건드리면 스크립트가 옛 경로를 찾다가 "설치 실패"로 오판정한다.

### 4-2. `#curriculum` 앵커 — 5문서가 새 홈의 존재하지 않는 앵커를 가리킨다

원본 설치 문서는 `../index.html#curriculum`을 5문서에서 참조한다(1세대 홈의 "7차시 커리큘럼" 섹션). harness-edu2 홈에는 커리큘럼 섹션이 없다.

처리 방법은 둘 중 하나이고, **①을 기본으로 한다:**

1. **새 홈에 `id="flow"`(120분 흐름) 섹션을 두고 링크를 `../index.html#flow`로 바꾼다.** 설치 문서가 학습자를 보내려던 곳은 "전체 그림"이고, 새 사이트에서 그 역할은 120분 흐름 섹션이 한다. `web-builder`에게 이 id를 반드시 만들어 달라고 요청한다.
2. 앵커를 떼고 `../index.html`만 남긴다 — 홈이 짧아 스크롤이 필요 없을 때만.

**절대 하지 않을 것:** 앵커를 그대로 두는 것. 존재하지 않는 앵커는 404를 내지 않고 조용히 페이지 최상단으로 보내므로, QA에서 링크 검사만 하면 통과해 버린다. 그래서 `verify_port.sh`는 앵커 부분까지 함께 검사한다.

### 5단계 · 잔여 검증

`scripts/verify_port.sh`를 실행한다. 남은 항목마다 "의도된 것인가"를 판단해 `_workspace/03_porter_residual.md`에 근거를 적는다. **판단 없이 목록만 남기는 것은 검증이 아니다.**

## 산출물

- `docs/install/*`, `docs/assets/site.css`, `docs/assets/site.js`, `docs/.nojekyll`
- `_workspace/03_porter_mapping.md` — 차시→실습 매핑 확정표, 변경 링크 목록(파일 · 이전 → 이후), 삭제/일반화 문장과 사유
- `_workspace/03_porter_residual.md` — 잔여 문자열과 각 건의 판단

## 자주 나는 결함

| 결함 | 왜 생기나 | 어떻게 막나 |
|---|---|---|
| `harness-edu22` | 치환 경계 미지정 | ①만 좁게 치환 (§4-1), 치환 후 grep |
| 앵커 링크 깨짐 | 절 제목을 다듬으면 `id`가 바뀐다 | 본문 제목을 건드리지 않는다 |
| 없는 실습으로 연결 | 대응 없는 차시를 억지 매핑 | 삭제 또는 일반화 |
| `cd`가 없는 폴더를 가리킴 | `harness-edu`를 통째로 치환해 폴더 경로 51곳이 함께 바뀜 | §4-1 — ②·③은 건드리지 않는다 |
| `#curriculum`이 조용히 최상단으로 | 없는 앵커는 에러를 내지 않는다 | §4-2, 새 홈에 `id="flow"` 확보 |
| 레이아웃 깨짐 | 새 `site.css`가 이관 문서의 클래스를 잃음 | 필수 클래스 목록을 `web-builder`에게 전달, HTML을 고치지 않는다 |
| 재실행 시 재배선 유실 | 전체 재복사 | 이미 이관된 상태면 diff로 부분 수정 |
