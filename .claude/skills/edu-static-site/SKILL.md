---
name: edu-static-site
description: harness-edu2 정적 사이트 구현 규격 — 디자인 토큰, 컴포넌트 카탈로그, 프롬프트 복사 박스, 반응형·접근성, GitHub Pages 배포. "페이지 만들어", "HTML 짜줘", "CSS 고쳐", "복사 버튼", "반응형 안 맞아", "사이트 빌드", "스타일 통일", "도식 그려줘" 요청 시 반드시 사용. 빌드 도구·프레임워크를 쓰지 않는 단일 CSS·단일 JS 구조가 전제다. 사이트 전체 구축·개편처럼 여러 담당이 걸리는 작업이면 harness-edu2-build 오케스트레이터가 이 스킬을 호출한다.
---

# 정적 사이트 구현 규격

## 전제

- **프레임워크·빌드 스텝 없음.** 페이지 7장, 상호작용은 복사 버튼과 목차 하이라이트뿐이다. `docs/`를 GitHub Pages에 push하면 그대로 뜨는 상태를 유지한다.
- **CSS는 `docs/assets/site.css` 한 파일, JS는 `site.js` 한 파일.** 페이지별 `<style>` 블록을 만들면 실습 3장의 모양이 서서히 갈라진다.
- **기존 디자인 시스템을 계승한다.** `harness-edu/docs/assets/site.css`의 토큰과 클래스를 물려받는다. 색·폰트를 새로 발명하면 이관된 설치가이드가 낯설어 보인다.

## 파일 구조

```
docs/
├── .nojekyll
├── index.html                   홈  (id="flow" 섹션 필수 — 이관 문서의 앵커 대상)
├── concept.html                 개념
├── practice/
│   ├── 1-youtube.html
│   ├── 2-marketing.html
│   └── 3-pptx.html
├── install/                     이관분 — HTML을 고치지 않는다
└── assets/
    ├── site.css                 단일 스타일시트
    ├── site.js                  복사 버튼 + 목차 하이라이트
    ├── sample.pptx              실습 3 입력
    └── example-strategy.md      실습 3 우회 경로
```

**`docs/index.html`에 `id="flow"`를 반드시 만든다.** 이관된 설치 문서 5개가 `../index.html#curriculum`을 참조하며, 이를 `#flow`로 재배선하기로 확정되어 있다. 이 id가 없으면 앵커가 조용히 최상단으로 이동하고, 링크 검사만 하는 QA는 통과시켜 버린다.

## 디자인 토큰 (계승 — 변경 금지)

```css
:root{
  --canvas:#faf9f5; --surface-soft:#f5f0e8; --surface-card:#efe9de;
  --surface-dark:#181715; --surface-dark-elevated:#252320;
  --hairline:#e6dfd8;
  --primary:#cc785c; --primary-active:#a9583e; --teal:#5db8a6; --amber:#e8a55a;
  --ink:#141413; --body-strong:#252523; --body:#3d3d3a; --muted:#6c6a64;
  --on-dark:#faf9f5; --on-dark-soft:#a09d96;
  --r-md:8px; --r-lg:12px; --pill:9999px;
  --serif:"Noto Serif KR","Fraunces",Garamond,serif;
  --serif-latin:"Fraunces","Noto Serif KR",Garamond,serif;
  --sans:"Inter","Noto Sans KR",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --mono:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  --maxw:1200px;
}
```

색의 역할을 지킨다. 이것을 흐리면 사이트가 "AI가 만든 것" 같아진다:

| 토큰 | 역할 | 쓰지 않는 곳 |
|---|---|---|
| `--primary` 코랄 | 링크·주요 버튼·강조 1곳 | 본문 텍스트, 넓은 배경 |
| `--surface-dark` | 프롬프트 박스, 히어로 코드 창 | 본문 카드 |
| `--teal` / `--amber` | 상태·구분 표시만 | 장식 |
| `--surface-card` 크림 | 카드 배경 | 본문 배경 (캔버스와 구분이 사라진다) |

본문은 `--body`, 제목은 `--ink`, 부가 설명은 `--muted`. 세 단계를 넘는 텍스트 색 위계를 만들지 않는다.

## 계승하지 않는 것

1세대의 컴포넌트 중 harness-edu2에 개념이 없는 것은 옮기지 않는다. 옮기면 쓰이지 않는 CSS가 남아 다음 수정 때 혼란을 만든다.

- 대상별 필터 (`.filter`) — harness-edu2에는 대상 구분이 없다
- 차시 카드·스테이지 (`.stage`, `.mod`) — 차시 체계가 없다
- 확장트랙 배지 — 확장트랙이 없다

단, **이관된 설치 문서가 쓰는 클래스는 하나도 지우지 않는다.** `install-porter`가 필수 클래스 목록을 보내오면 그것을 기준으로 유지한다. 확인 방법:

```bash
grep -rhoE 'class="[^"]*"' docs/install/ | tr -d '"' | sed 's/^class=//' | tr ' ' '\n' | sort -u > /tmp/install_classes.txt
# 이 목록의 클래스가 site.css에 정의되어 있는지 대조한다
```

## 컴포넌트 카탈로그

### 1. 프롬프트 박스 — 이 사이트의 핵심 컴포넌트

실습 페이지의 브리프는 **복사 실패가 곧 실습 실패**다. 구조를 고정한다:

```html
<div class="brief-card">
  <div class="brief-bar">
    <span class="brief-label">COPY &amp; RUN</span>
    <button class="brief-copy" data-copy type="button">복사</button>
  </div>
  <pre class="brief">하네스를 구성해줘.
[브랜드/주제]를 위한 유튜브 콘텐츠 기획 팀이 필요해.
트렌드 조사, 8–10분 대본 기획, 제목·태그 SEO, 썸네일 콘셉트를 맡기고,
최종적으로 1주치 콘텐츠 기획안을 만들어줘.
대상은 [20대 직장인]이고, 주장마다 근거 출처를 남겨줘.</pre>
</div>
```

지켜야 할 것:

1. **원문은 `<pre class="brief">` 안에 그대로 넣는다.** `<p>`로 감싸면 줄바꿈이 사라지고, `<pre>` 밖이면 연속 공백이 하나로 합쳐진다. 실습 2 브리프에는 의도된 이중 공백이 있다.
2. **플레이스홀더에 태그를 넣지 않는다.** `[브랜드/주제]`를 `<span>`으로 감싸 강조하면 클립보드에 태그가 섞인다. 강조가 필요하면 **CSS만으로** 처리한다:
   ```css
   /* 대괄호 자체를 시각 단서로 쓴다 — 마크업을 추가하지 않는다 */
   .brief{color:var(--on-dark);font-family:var(--mono);white-space:pre;overflow-x:auto}
   ```
   브라우저에서 텍스트 일부만 색칠하려면 마크업이 필요하므로, **플레이스홀더 강조는 프롬프트 밖 해설에서 한다.** 복사 정확성이 시각 강조보다 우선이다.
3. **`site.js`의 복사 로직은 `pre.innerText`를 읽는다.** 구조를 바꾸면 `.code-card` / `.terminal` 셀렉터에 걸리도록 클래스를 맞춘다 (아래 §JS 참조).
4. **복사 버튼을 실제로 눌러 붙여넣어 확인한다.** 5행이 5행으로 들어오는지, 이중 공백이 살아 있는지.

`.brief`는 `white-space:pre`를 쓴다. `pre-wrap`은 좁은 화면에서 줄바꿈을 만들어 학습자가 원문 행 수를 오해하게 한다. 대신 `overflow-x:auto`로 가로 스크롤을 허용한다.

### 2. 준비물 · 다운로드 (`.prep`)

실습 페이지 블록 2. **두 경로를 나란히** 보여야 한다 — `clone`한 학습자와 그러지 못한 학습자가 같은 화면에서 각자 자기 경로를 찾아야 한다.

```html
<section class="prep">
  <h2 id="준비물">준비물</h2>
  <div class="prep-grid">
    <div class="prep-col">
      <span class="prep-k">A · 실습 저장소를 받았다면</span>
      <p>설치가이드를 마쳤다면 이미 있습니다.
         <code>harness-edu/workshop/practice-3-pptx/</code> 를 Claude Code에서 엽니다.</p>
    </div>
    <div class="prep-col">
      <span class="prep-k">B · 개별 다운로드</span>
      <ul class="dl-list">
        <li><a class="dl" href="https://github.com/namojo/harness-edu/raw/main/workshop/practice-3-pptx/sample.pptx">
          <strong>sample.pptx</strong>
          <span class="dl-meta">형식·디자인 참조 원본 · 412KB</span></a></li>
      </ul>
    </div>
  </div>
</section>
```

지켜야 할 것:

1. **URL을 조립하지 않는다.** `_workspace/07_assets_manifest.md`의 URL을 그대로 복사한다. 브랜치명(`main`)이나 경로를 추측하면 전부 404다.
2. **`/raw/` 경로여야 한다.** `/blob/`은 GitHub의 HTML 미리보기 페이지이고, pptx는 미리보기가 안 되므로 학습자는 빈 화면을 본다.
3. **`download` 속성에 의존하지 않는다.** 크로스 오리진(github.com)에서는 브라우저가 `download`를 무시한다. 그래서 `/raw/`가 필수다 — GitHub가 `Content-Disposition`을 붙여 내려준다.
4. **파일명 · 용도 한 줄 · 용량**을 함께 보인다. 파일명만으로는 학습자가 이 파일이 자기에게 필요한지 판단할 수 없고, 용량을 모르면 교실 와이파이에서 40MB를 그냥 누른다.
5. **`target="_blank"`를 붙이지 않는다.** 다운로드는 페이지 이동이 아니므로 새 탭이 빈 창으로 남는다.
6. **실습 1·2도 이 블록을 가진다.** 입력 파일이 없어도 블록을 지우지 않고 "입력 파일 없음"으로 채운다. 지우면 세 페이지의 골격이 갈리고, 학습자는 실습 3에서 처음 보는 블록을 만난다.
7. **좁은 화면에서 `.prep-grid`는 1열로 떨어진다.** A가 위, B가 아래. 순서를 뒤집지 않는다 — 대부분의 학습자는 A에 해당한다.

`.prep-col`의 배경은 `--surface-card`, 좌측에 `--primary` 3px 보더. 두 열이 시각적으로 대등해야 한다. 한쪽을 강조하면 다른 쪽 학습자가 자기가 예외라고 느낀다.

### 3. 체크리스트

```html
<ul class="checks">
  <li>에이전트가 4개 이상 만들어졌고, 두 에이전트의 책임이 겹치는 곳이 없다</li>
  ...
</ul>
<p class="checks-gate">6개 중 5개 이상이면 통과입니다.</p>
```

체크박스는 `<input type="checkbox">`를 쓴다 — 학습자가 실제로 누를 수 있어야 한다. 상태를 저장할 필요는 없다(정적 사이트이고, 한 번 쓰는 것이다). `::before`로 만든 가짜 체크박스는 쓰지 않는다.

### 4. 역할 표 · 패턴 도식

역할 표는 3열(`역할 | 책임 | 전달물`) 고정. 좁은 화면에서 `overflow-x:auto` 컨테이너에 넣는다.

패턴 도식은 **인라인 SVG**로 만든다. 이미지 파일은 확대·수정·테마에 모두 취약하다.

```html
<figure class="diagram">
  <svg viewBox="0 0 720 200" role="img" aria-labelledby="d2-t d2-d">
    <title id="d2-t">실습 2의 팬아웃/팬인 + 생성-검증 구조</title>
    <desc id="d2-d">브리프가 시장·고객·경쟁·채널 4개 조사로 갈라진 뒤 전략가에서 하나로 합쳐지고, 별도 리뷰어가 검증합니다.</desc>
    <!-- ... -->
  </svg>
  <figcaption>관점은 병렬로, 결론은 하나로, 품질은 별도로.</figcaption>
</figure>
```

`role="img"` + `<title>` + `<desc>`를 항상 함께 둔다. `aria-labelledby`로 연결하지 않으면 스크린리더가 읽지 않는다.

도식은 `concept-curator` / `practice-designer`가 준 **관계 명세**를 그린다. 장식용 도식은 만들지 않는다 — 화면 공간과 로딩만 쓴다.

### 5. 콜아웃

```html
<section class="callout callout-stop">   <!-- 멈추고 확인해야 하는 것 -->
<section class="callout callout-tip">    <!-- 알아 두면 편한 것 -->
<section class="callout callout-dep">    <!-- 의존성 고지 (실습 3 상단) -->
```

이관된 설치가이드가 `.callout` / `.callout-stop`을 이미 쓴다. **같은 클래스를 재사용하고 새로 만들지 않는다.**

### 6. 페이저

모든 본문 페이지 하단에 이전/다음. 학습자가 다음에 뭘 할지 스스로 판단하게 만들지 않는다. 설치가이드에서 돌아오는 다음 목적지는 **실습 1**이다.

## JS — `site.js`

1세대 `site.js`를 그대로 계승한다. 두 기능뿐이다:

1. `[data-copy]` 버튼 → 같은 카드 안의 `<pre>` 텍스트를 클립보드로 (`clipboard API` + `execCommand` 폴백)
2. `.toc-list a[href^="#"]` → `IntersectionObserver`로 현재 위치 표시

복사 로직은 `btn.closest('.code-card') || btn.closest('.terminal')`에서 카드를 찾는다. **프롬프트 박스에 `.code-card`를 함께 붙이거나**, `site.js`의 셀렉터에 `.brief-card`를 추가한다. 어느 쪽이든 하고, `_workspace/05_builder_components.md`에 어느 쪽을 했는지 남긴다. 이 연결을 놓치면 복사 버튼이 조용히 아무것도 하지 않는다.

기능을 추가하지 않는다. 진도 저장·다크모드 토글·검색은 전부 유지보수 부담이며, 120분 워크샵에서 아무도 쓰지 않는다.

## 반응형

- 본문 최대 폭 `--maxw:1200px`, 읽기 영역은 `max-width:70ch`
- **표·도식·코드블록은 각자 `overflow-x:auto` 컨테이너 안.** 페이지 `body`가 가로로 스크롤되면 실패다
- `word-break:keep-all; overflow-wrap:break-word` — 한글 어절이 중간에서 끊기지 않게
- 브레이크포인트는 2개면 충분: `900px`(2열→1열), `640px`(패딩·폰트 축소)
- 실습 페이지는 노트북에서 Claude Code와 나란히 놓인다. **폭 절반(약 700px)에서 읽히는지** 확인한다

## 접근성 기본선

| 항목 | 요구 |
|---|---|
| skip link | `<a class="skip-link" href="#main">본문으로 건너뛰기</a>` — 이관분과 동일 |
| 제목 레벨 | h1 → h2 → h3 순서, 건너뛰지 않기 |
| 현재 위치 | 네비게이션 현재 페이지에 `aria-current="page"` |
| 링크 텍스트 | "여기", "클릭" 금지. 목적지를 말하는 텍스트 |
| 색 단독 전달 금지 | 상태를 색으로만 표시하지 않고 텍스트·아이콘 병기 |
| SVG | `role="img"` + `<title>` + `<desc>` + `aria-labelledby` |
| 대비 | 본문 4.5:1 이상. `--muted`(#6c6a64) on `--canvas`(#faf9f5)는 통과하지만, 그보다 옅은 색을 본문에 쓰지 않는다 |
| 버튼 | `<button type="button">`. `<div onclick>`을 쓰지 않는다 |

## 원고를 재작성하지 않는다

마크다운을 HTML로 옮기면서 문장을 고치고 싶어지면 작성자에게 요청한다. 구현자가 문장을 고치면 검토를 통과한 원고와 실제 사이트가 어긋나고, 다음 수정 때 어느 쪽이 정본인지 알 수 없게 된다.

## 로컬 확인

```bash
cd docs && python3 -m http.server 8765
# http://localhost:8765/ 에서 홈 → 개념 → 실습 1·2·3 → 설치가이드 순으로 링크만 눌러 이동
```

확인한 페이지 목록과 발견한 문제를 `_workspace/05_builder_components.md`에 남긴다. "빌드했다"는 확인이 아니다.

## 자주 나는 결함

| 결함 | 왜 생기나 | 어떻게 막나 |
|---|---|---|
| 복사 버튼이 아무것도 안 한다 | `site.js` 셀렉터에 `.brief-card`가 없다 | 클래스 맞추기 + 실제로 눌러 확인 |
| 프롬프트 이중 공백 유실 | `<pre>` 밖에 넣음 | `.brief`는 항상 `<pre>` |
| 클립보드에 `<span>`이 섞임 | 플레이스홀더를 마크업으로 강조 | 강조는 프롬프트 밖 해설에서 |
| 이관 설치가이드 레이아웃 깨짐 | `site.css`를 새로 쓰면서 클래스 유실 | 필수 클래스 목록 대조, CSS 전체 재생성 금지 |
| `#curriculum` 앵커가 최상단으로 | 홈에 `id="flow"` 미생성 | 홈 구현 시 먼저 만든다 |
| 좁은 화면에서 본문이 가로 스크롤 | 표를 컨테이너 없이 넣음 | 표·도식·코드는 `overflow-x:auto` |
| 다운로드가 빈 화면을 띄운다 | `/blob/` 경로 | `/raw/` 로. `download` 속성은 크로스 오리진에서 무시된다 |
| 다운로드 링크 전부 404 | 페이지에서 URL 조립 | `07_assets_manifest.md`의 URL을 그대로 복사 |
| 페이지마다 모양이 다름 | 페이지별 `<style>` | 단일 CSS 유지 |
