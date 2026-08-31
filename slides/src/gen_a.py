# -*- coding: utf-8 -*-
"""슬라이드 01~08 — 표지 + 개념"""
S = {}

S[1] = ('cover', '', '', '''
<div class="cover">
  <div class="top">HARNESS ENGINEERING WORKSHOP</div>
  <div class="mid">
    <h1>프롬프트 한 번을<br>반복 가능한 AI 팀으로</h1>
    <p class="sub">답을 잘 받는 프롬프트보다, 반복해서 쓸 수 있는<br><b style="color:#faf9f5;font-weight:700">역할 · 흐름 · 검토 기준</b>을 만듭니다.</p>
  </div>
  <div class="strip">
    <div><div class="i">CONCEPT</div><div class="n">하네스 엔지니어링</div><div class="d">3축 · 메타스킬 · 6패턴</div></div>
    <div><div class="i">PRACTICE 01</div><div class="n">유튜브 기획 팀</div><div class="d">팀을 만든다</div></div>
    <div><div class="i">PRACTICE 02</div><div class="n">마케팅 전략보고서</div><div class="d">구조를 고른다</div></div>
    <div><div class="i">PRACTICE 03</div><div class="n">샘플 형식으로 새 PPT</div><div class="d">산출물을 다듬는다</div></div>
  </div>
</div>''')

S[2] = ('light', '01', 'OUTCOME', '''
<h1>결론 — 답을 받는 법이 아니라<br>일하는 방식을 설계합니다</h1>
<div class="body">
<div class="grid g3">
  <div class="card flat"><div class="k">BEFORE</div><h3>프롬프트를 잘 쓴다</h3>
    <p>이번 결과가 좋아집니다. 다음 주에 같은 일을 하려면 그 문장을 다시 찾아야 하고, 옆자리 동료는 다른 답을 받습니다.</p></div>
  <div class="card accent"><div class="k">AFTER</div><h3>하네스를 만든다</h3>
    <p>역할·흐름·검토 기준이 <b>파일로 남습니다.</b> 다음 사람도, 다음 달에도 같은 품질이 나옵니다.</p></div>
  <div class="card"><div class="k">HOW</div><h3>한 문장으로 시작한다</h3>
    <p><span style="font-family:var(--mono);font-size:19px;color:var(--coral-deep)">하네스를 구성해줘</span> 로 시작해, 업무 설명을 팀 구조로 바꿉니다.</p></div>
</div>
<div class="banner coral" style="margin-top:30px">
  이 워크샵에서 만드는 것은 <b>결과물이 아니라 결과물을 만드는 구조</b>입니다.
  그래서 결과가 아쉬울 때 결과를 고치지 않고 <b>구조를 고칩니다.</b>
</div>
</div>''')

S[3] = ('light', '02', 'WHY', '''
<h1>같은 일을 두 번째로 할 때<br>무엇이 남아 있는가</h1>
<div class="body">
<div class="vs">
  <div class="bad">
    <div class="lab">프롬프트</div>
    <h3>매번 처음부터</h3>
    <svg class="dg" width="720" height="200" viewBox="0 0 720 200" role="img" aria-label="프롬프트는 질문마다 결과가 따로 나오고 남는 것이 없습니다">
      <g font-size="18" fill="#6c6a64">
        <rect x="2" y="14" width="150" height="54" rx="9" fill="#efe9de"/><text x="77" y="47" text-anchor="middle" fill="#3d3d3a">질문</text>
        <path d="M160 41h48" stroke="#c9c1b6" stroke-width="2"/><path d="M208 41l-9-5v10z" fill="#c9c1b6"/>
        <rect x="216" y="14" width="150" height="54" rx="9" fill="#fff" stroke="#e2dad0"/><text x="291" y="47" text-anchor="middle" fill="#3d3d3a">결과 A</text>
        <rect x="2" y="86" width="150" height="54" rx="9" fill="#efe9de"/><text x="77" y="119" text-anchor="middle" fill="#3d3d3a">질문 (다시)</text>
        <path d="M160 113h48" stroke="#c9c1b6" stroke-width="2"/><path d="M208 113l-9-5v10z" fill="#c9c1b6"/>
        <rect x="216" y="86" width="150" height="54" rx="9" fill="#fff" stroke="#e2dad0"/><text x="291" y="119" text-anchor="middle" fill="#3d3d3a">결과 B</text>
        <rect x="2" y="158" width="364" height="38" rx="9" fill="none" stroke="#e2dad0" stroke-dasharray="6 5"/>
        <text x="184" y="183" text-anchor="middle" fill="#928d84" font-size="17">서로를 모른다 · 남는 것이 없다</text>
        <text x="440" y="100" font-size="46" fill="#c9c1b6">✕</text>
        <text x="500" y="92" font-size="19" fill="#6c6a64">축적되지 않음</text>
        <text x="500" y="120" font-size="19" fill="#6c6a64">사람마다 다름</text>
      </g>
    </svg>
  </div>
  <div class="good">
    <div class="lab">하네스</div>
    <h3>구조가 남는다</h3>
    <svg class="dg" width="720" height="200" viewBox="0 0 720 200" role="img" aria-label="하네스는 역할과 흐름이 파일로 남아 실행할 때마다 같은 품질을 냅니다">
      <g font-size="18">
        <rect x="2" y="24" width="196" height="120" rx="11" fill="#181715"/>
        <text x="100" y="66" text-anchor="middle" fill="#faf9f5" font-size="20" font-weight="700">하네스</text>
        <text x="100" y="94" text-anchor="middle" fill="#b3aea5" font-size="16">에이전트 · 스킬</text>
        <text x="100" y="118" text-anchor="middle" fill="#7c766d" font-size="15">파일로 존재</text>
        <path d="M206 60h44" stroke="#cc785c" stroke-width="2"/><path d="M250 60l-9-5v10z" fill="#cc785c"/>
        <path d="M206 108h44" stroke="#cc785c" stroke-width="2"/><path d="M250 108l-9-5v10z" fill="#cc785c"/>
        <rect x="258" y="34" width="160" height="52" rx="9" fill="#fff" stroke="#cc785c"/><text x="338" y="66" text-anchor="middle" fill="#141413">결과 · 1회차</text>
        <rect x="258" y="82" width="160" height="52" rx="9" fill="#fff" stroke="#cc785c"/><text x="338" y="114" text-anchor="middle" fill="#141413">결과 · 2회차</text>
        <path d="M2 156h416" stroke="#cc785c" stroke-width="2"/>
        <text x="210" y="184" text-anchor="middle" fill="#a9583e" font-size="17">같은 구조 → 같은 품질</text>
        <text x="470" y="70" font-size="19" fill="#3d3d3a">다음 사람도 쓴다</text>
        <text x="470" y="102" font-size="19" fill="#3d3d3a">고칠 곳이 분명하다</text>
      </g>
    </svg>
  </div>
</div>
</div>''')

S[4] = ('light', '03', 'THREE AXES', '''
<h1>하네스는 세 가지의 조합입니다</h1>
<p class="lede">무엇을 언제 쓰는지 구분하는 것 — 이 워크샵에서 얻어 갈 감각입니다.</p>
<div class="body" style="margin-top:44px">
<style>.card{padding:34px 36px}.card p{margin-top:16px}</style>
<div class="grid g3">
  <div class="card"><div class="k">AGENT · 누가</div><h3>역할과 경계</h3>
    <p><span class="mono" style="font-family:var(--mono);font-size:18px;color:var(--coral-deep)">.claude/agents/이름.md</span></p>
    <p class="sm">일을 나눠 맡길 담당자.<br>예: 시장 조사자, 리뷰어</p>
    <span class="tag">지시문 파일</span></div>
  <div class="card"><div class="k">SKILL · 어떻게</div><h3>절차와 기준</h3>
    <p><span class="mono" style="font-family:var(--mono);font-size:18px;color:var(--coral-deep)">.claude/skills/이름/SKILL.md</span></p>
    <p class="sm">담당자가 따르는 설명서.<br>맥락에 따라 판단이 달라지는 일</p>
    <span class="tag">모델이 읽는 문서</span></div>
  <div class="card"><div class="k">TOOL · 무엇으로</div><h3>실행</h3>
    <p><span class="mono" style="font-family:var(--mono);font-size:18px;color:var(--coral-deep)">MCP 서버 등 실제 코드</span></p>
    <p class="sm">계산기.<br>언제 실행해도 같은 값이 나와야 하는 일</p>
    <span class="tag">선택 학습</span></div>
</div>
<svg class="dg" style="margin-top:46px" width="1720" height="150" viewBox="0 0 1720 150" role="img" aria-label="에이전트에 스킬이 붙고 필요하면 툴이 붙어 하나의 팀이 됩니다">
  <g font-size="21">
    <rect x="0" y="30" width="230" height="66" rx="11" fill="#181715"/>
    <text x="115" y="70" text-anchor="middle" fill="#faf9f5" font-weight="700">에이전트</text>
    <text x="252" y="70" font-size="30" fill="#cc785c">+</text>
    <rect x="296" y="30" width="230" height="66" rx="11" fill="#efe9de"/>
    <text x="411" y="70" text-anchor="middle" fill="#141413" font-weight="700">스킬</text>
    <text x="548" y="70" font-size="30" fill="#c9c1b6">(+</text>
    <rect x="600" y="30" width="230" height="66" rx="11" fill="#fff" stroke="#e2dad0" stroke-dasharray="7 5"/>
    <text x="715" y="70" text-anchor="middle" fill="#6c6a64" font-weight="700">툴</text>
    <text x="846" y="70" font-size="30" fill="#c9c1b6">)</text>
    <path d="M886 63h60" stroke="#cc785c" stroke-width="2.5"/><path d="M946 63l-11-6v12z" fill="#cc785c"/>
    <rect x="964" y="22" width="330" height="82" rx="12" fill="#fff" stroke="#cc785c" stroke-width="2"/>
    <text x="1129" y="58" text-anchor="middle" fill="#141413" font-weight="700" font-size="23">하나의 담당자</text>
    <text x="1129" y="86" text-anchor="middle" fill="#6c6a64" font-size="18">이것이 여럿 모여 팀이 된다</text>
    <text x="1330" y="55" fill="#6c6a64" font-size="19">이 워크샵의 실습 1·2·3은</text>
    <text x="1330" y="84" fill="#141413" font-size="19" font-weight="700">에이전트와 스킬만 씁니다</text>
  </g>
</svg>
</div>''')

S[5] = ('light', '04', 'THE RULE', '''
<h1 class="sm">툴인가 스킬인가 — 질문 하나로 갈립니다</h1>
<div class="body">
<svg class="dg" width="1720" height="330" viewBox="0 0 1720 330" role="img" aria-label="늘 같은 답이 나와야 하면 툴, 맥락에 따라 달라지면 스킬입니다">
  <g font-size="22">
    <rect x="0" y="118" width="470" height="94" rx="13" fill="#181715"/>
    <text x="235" y="155" text-anchor="middle" fill="#faf9f5" font-size="25" font-weight="700">늘 같은 답이</text>
    <text x="235" y="188" text-anchor="middle" fill="#faf9f5" font-size="25" font-weight="700">나와야 하는가?</text>

    <path d="M486 150h96V72h58" stroke="#cc785c" stroke-width="2.5" fill="none"/><path d="M640 72l-11-6v12z" fill="#cc785c"/>
    <text x="510" y="60" fill="#a9583e" font-size="20" font-weight="700">예</text>
    <path d="M486 180h96v78h58" stroke="#4fa595" stroke-width="2.5" fill="none"/><path d="M640 258l-11-6v12z" fill="#4fa595"/>
    <text x="510" y="300" fill="#2f7d70" font-size="20" font-weight="700">아니오</text>

    <rect x="656" y="24" width="300" height="96" rx="13" fill="#fff" stroke="#cc785c" stroke-width="2"/>
    <text x="806" y="62" text-anchor="middle" fill="#141413" font-size="27" font-weight="900">툴</text>
    <text x="806" y="95" text-anchor="middle" fill="#6c6a64" font-size="19">실제 코드에 맡긴다</text>
    <text x="990" y="52" fill="#3d3d3a" font-size="20">계산 · 조회 · API 호출 · 사내 시스템 연동</text>
    <text x="990" y="84" fill="#928d84" font-size="19">AI 가 “못 하는 일”을 넘긴다 — 환각이 생길 수 없다</text>

    <rect x="656" y="210" width="300" height="96" rx="13" fill="#fff" stroke="#4fa595" stroke-width="2"/>
    <text x="806" y="248" text-anchor="middle" fill="#141413" font-size="27" font-weight="900">스킬</text>
    <text x="806" y="281" text-anchor="middle" fill="#6c6a64" font-size="19">설명서로 남긴다</text>
    <text x="990" y="238" fill="#3d3d3a" font-size="20">무엇이 중요한가 · 어떤 순서로 · 어디까지가 완료인가</text>
    <text x="990" y="270" fill="#928d84" font-size="19">AI 가 “잘하는 일”의 기준을 정한다</text>
  </g>
</svg>
<div class="banner" style="margin-top:14px">
  그 둘을 <b>누구에게 맡길지</b>가 <b>에이전트</b>입니다. 세 축은 경쟁하지 않고 층을 이룹니다.
</div>
</div>''')

S[6] = ('light', '05', 'AGENT', '''
<h1 class="sm">에이전트는 추상적인 개념이 아니라 파일 한 개입니다</h1>
<div class="body" style="margin-top:34px">
<style>.code pre{font-size:18.5px;line-height:1.56;padding:22px 28px}.card.soft{padding:22px 28px!important}.card.soft h3{font-size:24px!important}</style>
<div class="grid" style="grid-template-columns:1.32fr 1fr;gap:34px">
  <div class="code">
    <div class="bar">.claude/agents/reviewer.md</div>
<pre><span class="c2">---</span>
<span class="c1">name</span>: reviewer
<span class="c1">description</span>: 근거·실행 가능성·누락을 점검하는 리뷰어 …
<span class="c1">model</span>: opus
<span class="c2">---</span>

<span class="c3"># reviewer — 검증 담당</span>

<span class="c3">## 핵심 역할</span>
전략가가 만든 보고서를 <span class="c1">만든 사람이 아닌 눈</span>으로 검사한다.

<span class="c3">## 작업 원칙</span>
1. “문제 없음”으로 끝내지 않는다 — 지적 없이
   통과시키면 검증이 아니다.
2. 근거 없는 주장, 실행 주체가 없는 항목을 찾는다.

<span class="c3">## 사용 스킬</span>
<span class="c1">strategy-review</span> — 검토 기준과 지적 형식</pre>
  </div>
  <div>
    <div class="card soft" style="padding:26px 30px">
      <div class="k">FRONTMATTER</div>
      <h3 style="font-size:26px">언제 부를지</h3>
      <p class="sm"><b style="color:var(--ink)">name</b> · <b style="color:var(--ink)">description</b> · <b style="color:var(--ink)">model</b> 세 줄이 이 담당자를 호출할 조건을 정합니다.</p>
    </div>
    <div class="card soft" style="padding:26px 30px;margin-top:20px">
      <div class="k">BODY</div>
      <h3 style="font-size:26px">무엇을 어디까지</h3>
      <p class="sm">역할 · 작업 원칙 · 입출력. <b style="color:var(--ink)">원칙에 “왜”를 적어 두면</b> 예외 상황에서도 판단이 흔들리지 않습니다.</p>
    </div>
    <div class="card" style="padding:26px 30px;margin-top:20px;border-color:var(--coral);border-width:2px">
      <div class="k">사용 스킬</div>
      <h3 style="font-size:26px">여기서 두 축이 만난다</h3>
      <p class="sm">에이전트가 자기 설명서를 가리킵니다. 결과가 아쉬울 때 <b style="color:var(--ink)">고칠 곳은 대개 이쪽</b>입니다.</p>
    </div>
  </div>
</div>
<p class="lede" style="margin-top:20px;max-width:none;font-size:23px">실습에서 <b>하네스가 만들어 주는 것이 바로 이 모양</b>입니다. 스킬 하나만 새로 만들거나 다듬을 때는 <span style="font-family:var(--mono);font-size:19px">skill-creator</span> 스킬을 씁니다.</p>
</div>''')

S[7] = ('light', '06', 'META-SKILL', '''
<h1 class="sm">“하네스를 구성해줘” 한 문장이 지나가는 6단계</h1>
<div class="body">
<svg class="dg" width="1720" height="120" viewBox="0 0 1720 120" role="img" aria-label="도메인 분석에서 검증까지 6단계가 순서대로 진행됩니다">
  <line x1="20" y1="60" x2="1700" y2="60" stroke="#e2dad0" stroke-width="3"/>
  <g font-family="Fraunces, Georgia, serif" font-size="26" font-weight="700" fill="#a9583e">
    <circle cx="20" cy="60" r="19" fill="#181715"/><text x="20" y="69" text-anchor="middle" fill="#faf9f5" font-size="20">1</text>
    <circle cx="356" cy="60" r="19" fill="#181715"/><text x="356" y="69" text-anchor="middle" fill="#faf9f5" font-size="20">2</text>
    <circle cx="692" cy="60" r="19" fill="#181715"/><text x="692" y="69" text-anchor="middle" fill="#faf9f5" font-size="20">3</text>
    <circle cx="1028" cy="60" r="19" fill="#181715"/><text x="1028" y="69" text-anchor="middle" fill="#faf9f5" font-size="20">4</text>
    <circle cx="1364" cy="60" r="19" fill="#181715"/><text x="1364" y="69" text-anchor="middle" fill="#faf9f5" font-size="20">5</text>
    <circle cx="1700" cy="60" r="19" fill="#cc785c"/><text x="1700" y="69" text-anchor="middle" fill="#fff" font-size="20">6</text>
  </g>
</svg>
<div class="grid g6" style="margin-top:4px">
  <div><div style="font-size:26px;font-weight:900;color:var(--ink);letter-spacing:-.02em">도메인 분석</div>
    <p style="font-size:19px;color:var(--muted);margin-top:12px;line-height:1.5">목표 · 대상 · 제약이<br>무엇인지</p></div>
  <div><div style="font-size:26px;font-weight:900;color:var(--ink);letter-spacing:-.02em">아키텍처 설계</div>
    <p style="font-size:19px;color:var(--muted);margin-top:12px;line-height:1.5">순차인가 병렬인가,<br>검토가 따로 필요한가</p></div>
  <div><div style="font-size:26px;font-weight:900;color:var(--ink);letter-spacing:-.02em">에이전트 정의</div>
    <p style="font-size:19px;color:var(--muted);margin-top:12px;line-height:1.5">누가 무엇까지<br>책임지는가</p></div>
  <div><div style="font-size:26px;font-weight:900;color:var(--ink);letter-spacing:-.02em">스킬 생성</div>
    <p style="font-size:19px;color:var(--muted);margin-top:12px;line-height:1.5">각자가 따를 절차와<br>완료 기준</p></div>
  <div><div style="font-size:26px;font-weight:900;color:var(--ink);letter-spacing:-.02em">오케스트레이션</div>
    <p style="font-size:19px;color:var(--muted);margin-top:12px;line-height:1.5">누가 언제 무엇을<br>누구에게 넘기는가</p></div>
  <div><div style="font-size:26px;font-weight:900;color:var(--coral-deep);letter-spacing:-.02em">검증</div>
    <p style="font-size:19px;color:var(--muted);margin-top:12px;line-height:1.5">산출물이 기준을<br>통과했는가</p></div>
</div>
<div class="banner coral" style="margin-top:34px">
  <b>2단계가 가장 중요합니다.</b> 역할 수를 늘리기 전에 <b>일의 모양</b>을 먼저 정합니다 — 그 모양이 다음 장의 패턴입니다.
</div>
<p style="font-size:18px;color:var(--faint);margin-top:22px">출처 · revfactory/harness <span style="font-family:var(--mono)">skills/harness/SKILL.md</span> §워크플로우 — 원본은 현황 감사와 진화를 더한 8단계이며, 그 둘은 이미 만든 하네스를 고칠 때 앞뒤에 붙습니다.</p>
</div>''')

S[8] = ('light', '07', 'SIX PATTERNS', '''
<h1 class="sm">6가지 패턴 — 일의 모양에 붙은 이름</h1>
<div class="body" style="margin-top:32px">
<div class="grid g3" style="gap:20px">
  <div class="card" style="padding:24px 26px">
    <svg width="300" height="52" viewBox="0 0 300 52" role="img" aria-label="A에서 B, B에서 C로 순서대로 이어집니다">
      <g font-size="15" fill="#3d3d3a"><rect x="0" y="10" width="72" height="32" rx="7" fill="#efe9de"/><text x="36" y="31" text-anchor="middle">A</text>
      <path d="M78 26h26" stroke="#cc785c" stroke-width="2"/><path d="M104 26l-8-4.5v9z" fill="#cc785c"/>
      <rect x="110" y="10" width="72" height="32" rx="7" fill="#efe9de"/><text x="146" y="31" text-anchor="middle">B</text>
      <path d="M188 26h26" stroke="#cc785c" stroke-width="2"/><path d="M214 26l-8-4.5v9z" fill="#cc785c"/>
      <rect x="220" y="10" width="72" height="32" rx="7" fill="#efe9de"/><text x="256" y="31" text-anchor="middle">C</text></g>
    </svg>
    <h3 style="font-size:27px;margin-top:16px">파이프라인</h3>
    <p style="font-size:19px;margin-top:10px">앞 단계 결과가 다음 단계의 입력이 됩니다.</p>
    <p class="sm" style="margin-top:10px"><b style="color:var(--coral-deep)">순서를 바꿀 수 없는 일</b></p>
    <span class="tag">실습 3</span>
  </div>
  <div class="card" style="padding:24px 26px">
    <svg width="300" height="52" viewBox="0 0 300 52" role="img" aria-label="하나가 셋으로 갈라진 뒤 다시 하나로 합쳐집니다">
      <g font-size="15" fill="#3d3d3a"><circle cx="14" cy="26" r="10" fill="#181715"/>
      <path d="M26 26h30M26 26q16 0 16-16h14M26 26q16 0 16 16h14" stroke="#cc785c" stroke-width="2" fill="none"/>
      <rect x="62" y="0" width="66" height="20" rx="5" fill="#efe9de"/><rect x="62" y="16" width="66" height="20" rx="5" fill="#efe9de"/><rect x="62" y="32" width="66" height="20" rx="5" fill="#efe9de"/>
      <path d="M134 10q16 0 16 16h14M134 26h30M134 42q16 0 16-16h14" stroke="#cc785c" stroke-width="2" fill="none"/>
      <rect x="176" y="10" width="80" height="32" rx="7" fill="#fff" stroke="#cc785c"/><text x="216" y="31" text-anchor="middle">통합</text></g>
    </svg>
    <h3 style="font-size:27px;margin-top:16px">팬아웃 / 팬인</h3>
    <p style="font-size:19px;margin-top:10px">독립된 관점을 동시에 모아 하나로 합칩니다.</p>
    <p class="sm" style="margin-top:10px"><b style="color:var(--coral-deep)">서로를 기다릴 필요 없는 조사</b></p>
    <span class="tag">실습 2</span>
  </div>
  <div class="card" style="padding:24px 26px">
    <svg width="300" height="52" viewBox="0 0 300 52" role="img" aria-label="만드는 쪽과 검사하는 쪽이 분리되고 수정 요청이 되돌아갑니다">
      <g font-size="15" fill="#3d3d3a"><rect x="0" y="14" width="90" height="32" rx="7" fill="#efe9de"/><text x="45" y="35" text-anchor="middle">생성</text>
      <path d="M96 30h30" stroke="#4fa595" stroke-width="2"/><path d="M126 30l-8-4.5v9z" fill="#4fa595"/>
      <rect x="132" y="14" width="90" height="32" rx="7" fill="#fff" stroke="#4fa595" stroke-width="1.6"/><text x="177" y="35" text-anchor="middle">검증</text>
      <path d="M177 10V2H45v8" stroke="#4fa595" stroke-width="1.6" stroke-dasharray="4 3" fill="none"/><path d="M45 14l-4-8h8z" fill="#4fa595"/>
      <text x="234" y="35" fill="#928d84" font-size="14">수정</text></g>
    </svg>
    <h3 style="font-size:27px;margin-top:16px">생성-검증</h3>
    <p style="font-size:19px;margin-top:10px">만드는 쪽과 검사하는 쪽을 다른 담당자로 분리합니다.</p>
    <p class="sm" style="margin-top:10px"><b style="color:var(--coral-deep)">품질 기준이 명확한 산출물</b></p>
    <span class="tag">실습 2 · 3</span>
  </div>
  <div class="card" style="padding:24px 26px">
    <svg width="300" height="52" viewBox="0 0 300 52" role="img" aria-label="상황에 맞는 담당자만 골라 호출합니다">
      <g font-size="15" fill="#3d3d3a"><rect x="0" y="14" width="76" height="32" rx="7" fill="#181715"/><text x="38" y="35" text-anchor="middle" fill="#faf9f5">상황</text>
      <path d="M82 30h26" stroke="#cc785c" stroke-width="2"/><path d="M108 30l-8-4.5v9z" fill="#cc785c"/>
      <rect x="116" y="2" width="58" height="20" rx="5" fill="#fff" stroke="#e2dad0" stroke-dasharray="4 3"/>
      <rect x="116" y="26" width="58" height="20" rx="5" fill="#cc785c"/>
      <rect x="182" y="2" width="58" height="20" rx="5" fill="#fff" stroke="#e2dad0" stroke-dasharray="4 3"/>
      <rect x="182" y="26" width="58" height="20" rx="5" fill="#fff" stroke="#e2dad0" stroke-dasharray="4 3"/>
      <text x="252" y="42" fill="#a9583e" font-size="14">1명만</text></g>
    </svg>
    <h3 style="font-size:27px;margin-top:16px">전문가 풀</h3>
    <p style="font-size:19px;margin-top:10px">전원이 아니라 상황에 맞는 담당자만 부릅니다.</p>
    <p class="sm" style="margin-top:10px"><b style="color:var(--coral-deep)">건마다 필요한 전문성이 다른 일</b></p>
    <span class="tag">실습 1 확장</span>
  </div>
  <div class="card soft" style="padding:24px 26px">
    <svg width="300" height="52" viewBox="0 0 300 52" role="img" aria-label="중앙 담당자가 진행 상태를 보며 일을 나눕니다">
      <g font-size="15" fill="#3d3d3a"><rect x="98" y="14" width="90" height="32" rx="7" fill="#181715"/><text x="143" y="35" text-anchor="middle" fill="#faf9f5">감독</text>
      <path d="M143 10V4M110 18l-24-8M176 18l24-8" stroke="#c9c1b6" stroke-width="2"/>
      <rect x="40" y="0" width="46" height="16" rx="4" fill="#e8e0d2"/><rect x="200" y="0" width="46" height="16" rx="4" fill="#e8e0d2"/>
      <path d="M143 50v2M120 44l-30 6M166 44l30 6" stroke="#c9c1b6" stroke-width="2"/>
      <rect x="44" y="44" width="46" height="16" rx="4" fill="#e8e0d2"/><rect x="196" y="44" width="46" height="16" rx="4" fill="#e8e0d2"/></g>
    </svg>
    <h3 style="font-size:27px;margin-top:16px">감독자</h3>
    <p style="font-size:19px;margin-top:10px">중앙 담당자가 상태를 보며 일을 그때그때 나눕니다.</p>
    <p class="sm" style="margin-top:10px"><b style="color:var(--muted)">양·순서를 미리 못 정하는 경우</b></p>
    <span class="tag" style="color:var(--muted);background:var(--cream-strong)">개념만</span>
  </div>
  <div class="card soft" style="padding:24px 26px">
    <svg width="300" height="52" viewBox="0 0 300 52" role="img" aria-label="상위 담당자가 하위에게 다시 쪼개 맡깁니다">
      <g font-size="15" fill="#3d3d3a"><rect x="0" y="14" width="70" height="32" rx="7" fill="#181715"/><text x="35" y="35" text-anchor="middle" fill="#faf9f5">상위</text>
      <path d="M76 30h20" stroke="#c9c1b6" stroke-width="2"/>
      <rect x="102" y="14" width="62" height="32" rx="7" fill="#e8e0d2"/><text x="133" y="35" text-anchor="middle">하위</text>
      <path d="M170 30h20" stroke="#c9c1b6" stroke-width="2"/>
      <rect x="196" y="18" width="54" height="24" rx="6" fill="#efe9de"/>
      <path d="M256 30h14" stroke="#c9c1b6" stroke-width="2" stroke-dasharray="3 3"/></g>
    </svg>
    <h3 style="font-size:27px;margin-top:16px">계층적 위임</h3>
    <p style="font-size:19px;margin-top:10px">상위 담당자가 하위에게 다시 쪼개 맡깁니다.</p>
    <p class="sm" style="margin-top:10px"><b style="color:var(--muted)">큰 일을 계속 쪼개야 하는 경우</b></p>
    <span class="tag" style="color:var(--muted);background:var(--cream-strong)">개념만</span>
  </div>
</div>
<p style="font-size:18px;color:var(--faint);margin-top:20px">출처 · revfactory/harness <span style="font-family:var(--mono)">README_KO.md</span> §아키텍처 패턴 — 원본은 조건부 토론 · 단계별 팀 재구성을 더한 8가지이며, 두 심화 패턴은 15명 이상 규모의 이야기입니다.</p>
</div>''')
