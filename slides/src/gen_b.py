# -*- coding: utf-8 -*-
"""슬라이드 09~14 — 패턴 선택 · 진화 · 실습 개요 · 실습 1"""
S = {}

S[9] = ('light', '08', 'CHOOSING', '''
<h1 class="sm">정의를 외우지 말고 세 가지를 물어보세요</h1>
<div class="body">
<div class="grid g3">
  <div class="card accent">
    <div class="k">QUESTION 01</div>
    <h3>앞 단계 결과가<br>다음 단계에 꼭 필요한가?</h3>
    <p style="margin-top:20px"><b style="color:var(--coral-deep);font-size:23px">예 → 파이프라인</b></p>
    <p class="sm">조사가 끝나야 기획을 할 수 있는 경우</p>
  </div>
  <div class="card accent">
    <div class="k">QUESTION 02</div>
    <h3>독립된 관점을<br>동시에 모을 수 있는가?</h3>
    <p style="margin-top:20px"><b style="color:var(--coral-deep);font-size:23px">예 → 팬아웃 / 팬인</b></p>
    <p class="sm">시장·고객·경쟁을 따로 보는 경우</p>
  </div>
  <div class="card accent">
    <div class="k">QUESTION 03</div>
    <h3>만든 사람이 아닌<br>다른 눈이 검사해야 하는가?</h3>
    <p style="margin-top:20px"><b style="color:var(--coral-deep);font-size:23px">예 → 생성-검증</b></p>
    <p class="sm">타 부서 검토를 거치는 문서</p>
  </div>
</div>
<div class="banner dark-b" style="margin-top:32px;display:flex;align-items:center;gap:48px">
  <div style="flex:1">
    <b style="font-size:29px">패턴은 하나를 고르는 것이 아닙니다.</b><br>
    <span style="font-size:23px;color:var(--on-dark-mid)">세 질문에 다 “예”라면 세 패턴을 겹쳐 씁니다 — 실습 2와 실습 3이 정확히 그 경우입니다.</span>
  </div>
  <svg width="520" height="96" viewBox="0 0 520 96" role="img" aria-label="실습 2는 팬아웃 팬인과 생성 검증을, 실습 3은 파이프라인과 생성 검증을 겹쳐 씁니다">
    <g font-size="18">
      <text x="0" y="30" fill="#7c766d" font-size="17">실습 2</text>
      <rect x="70" y="12" width="180" height="28" rx="14" fill="#cc785c"/><text x="160" y="32" text-anchor="middle" fill="#fff" font-size="16">팬아웃 / 팬인</text>
      <text x="258" y="32" fill="#7c766d" font-size="17">+</text>
      <rect x="278" y="12" width="150" height="28" rx="14" fill="#4fa595"/><text x="353" y="32" text-anchor="middle" fill="#fff" font-size="16">생성-검증</text>
      <text x="0" y="80" fill="#7c766d" font-size="17">실습 3</text>
      <rect x="70" y="62" width="180" height="28" rx="14" fill="#cc785c"/><text x="160" y="82" text-anchor="middle" fill="#fff" font-size="16">파이프라인</text>
      <text x="258" y="82" fill="#7c766d" font-size="17">+</text>
      <rect x="278" y="62" width="150" height="28" rx="14" fill="#4fa595"/><text x="353" y="82" text-anchor="middle" fill="#fff" font-size="16">검토 분리</text>
    </g>
  </svg>
</div>
</div>''')

S[10] = ('light', '09', 'EVOLUTION', '''
<h1 class="sm">하네스는 쓸수록 나아집니다</h1>
<p class="lede" style="margin-top:18px;font-size:26px">결과를 손으로 고치지 않고 <b>하네스를 고칩니다.</b> 결과를 고치면 이번 한 번만 좋아지고, 하네스를 고치면 다음부터 계속 좋아집니다.</p>
<div class="body" style="margin-top:6px">
<svg class="dg" width="1560" height="530" viewBox="0 0 1720 590" style="margin:0 auto" role="img" aria-labelledby="evo-t evo-d">
  <title id="evo-t">하네스 진화 메커니즘 — 사용에서 기록으로 이어지는 순환</title>
  <desc id="evo-d">하네스를 실제 프로젝트에 쓰고, 거기서 나온 피드백을 일반화해 에이전트·스킬·오케스트레이터에 반영하고, 그 변경을 workspace 산출물과 변경 이력에 기록합니다. 기록이 남으므로 다음 사용자는 개선된 하네스에서 시작합니다.</desc>
  <defs>
    <marker id="ar" viewBox="0 0 12 12" refX="9" refY="6" markerWidth="9" markerHeight="9" orient="auto">
      <path d="M1 1L10 6L1 11z" fill="#cc785c"/></marker>
    <marker id="art" viewBox="0 0 12 12" refX="9" refY="6" markerWidth="9" markerHeight="9" orient="auto">
      <path d="M1 1L10 6L1 11z" fill="#4fa595"/></marker>
  </defs>

  <!-- 순환 호 (반시계 방향 흐름을 시계 방향 배치로) -->
  <circle cx="860" cy="290" r="228" fill="none" stroke="#ece6de" stroke-width="2"/>

  <!-- 중앙 -->
  <text x="860" y="278" text-anchor="middle" font-size="27" font-weight="900" fill="#141413">세대를 거쳐</text>
  <text x="860" y="316" text-anchor="middle" font-size="27" font-weight="900" fill="#141413">나아진다</text>

  <!-- ① 하네스 (상단) -->
  <rect x="706" y="20" width="308" height="86" rx="13" fill="#181715"/>
  <text x="860" y="56" text-anchor="middle" fill="#faf9f5" font-size="25" font-weight="700">하네스</text>
  <text x="860" y="84" text-anchor="middle" fill="#b3aea5" font-size="17">에이전트 · 스킬 · 오케스트레이터</text>

  <!-- ② 실제 사용 (우상) -->
  <rect x="1218" y="196" width="228" height="86" rx="13" fill="#fff" stroke="#e2dad0"/>
  <text x="1332" y="232" text-anchor="middle" fill="#141413" font-size="24" font-weight="700">실제 프로젝트</text>
  <text x="1332" y="260" text-anchor="middle" fill="#6c6a64" font-size="18">사용</text>

  <!-- ③ 피드백 (우하) -->
  <rect x="1064" y="452" width="228" height="86" rx="13" fill="#fff" stroke="#cc785c" stroke-width="2"/>
  <text x="1178" y="488" text-anchor="middle" fill="#141413" font-size="24" font-weight="700">피드백</text>
  <text x="1178" y="516" text-anchor="middle" fill="#6c6a64" font-size="18">아쉬운 곳 · 반복된 수정</text>

  <!-- ④ 진화 (좌하) -->
  <rect x="428" y="452" width="228" height="86" rx="13" fill="#efe9de"/>
  <text x="542" y="488" text-anchor="middle" fill="#141413" font-size="24" font-weight="700">진화</text>
  <text x="542" y="516" text-anchor="middle" fill="#6c6a64" font-size="18">일반화해 하네스에 반영</text>

  <!-- ⑤ 기록 (좌상) -->
  <rect x="274" y="196" width="228" height="86" rx="13" fill="#fff" stroke="#4fa595" stroke-width="2"/>
  <text x="388" y="232" text-anchor="middle" fill="#141413" font-size="24" font-weight="700">기록</text>
  <text x="388" y="260" text-anchor="middle" fill="#6c6a64" font-size="18">_workspace · 변경 이력</text>

  <!-- 호 화살표 -->
  <path d="M1020 90 A 228 228 0 0 1 1258 186" stroke="#cc785c" stroke-width="2.5" fill="none" marker-end="url(#ar)"/>
  <path d="M1330 294 A 228 228 0 0 1 1216 448" stroke="#cc785c" stroke-width="2.5" fill="none" marker-end="url(#ar)"/>
  <path d="M1052 512 A 228 228 0 0 1 668 512" stroke="#cc785c" stroke-width="2.5" fill="none" marker-end="url(#ar)"/>
  <path d="M504 448 A 228 228 0 0 1 390 294" stroke="#4fa595" stroke-width="2.5" fill="none" marker-end="url(#art)"/>
  <path d="M462 186 A 228 228 0 0 1 700 90" stroke="#4fa595" stroke-width="2.5" fill="none" marker-end="url(#art)"/>

  <text x="1470" y="232" font-size="19" fill="#928d84">조사가 얕다 · 검토가 형식적이다</text>
  <text x="1470" y="260" font-size="19" fill="#928d84">형식이 매번 다르다</text>
  <text x="16" y="66" font-size="19" fill="#2f7d70" font-weight="700">기록이 순환을 완성합니다</text>
  <text x="16" y="96" font-size="19" fill="#928d84">남기지 않으면 다음 사람이</text>
  <text x="16" y="124" font-size="19" fill="#928d84">같은 아쉬움을 다시 겪습니다</text>
</svg>
<div class="grid g2" style="margin-top:6px;gap:26px">
  <div class="banner coral" style="font-size:21px;padding:20px 26px">
    <b>피드백을 일반화합니다.</b> “서론이 길었다”를 “10% 이내로”라고 고치면 그 문서에만 맞는 규칙이 됩니다. <b>왜 길어졌는지</b>를 고쳐야 다음에도 통합니다.
  </div>
  <div class="banner" style="font-size:21px;padding:20px 26px;background:#e6f2ef;border-left:6px solid var(--teal)">
    <b>무엇을 왜 바꿨는지 기록합니다.</b> 기록이 있어야 <b>퇴행</b>을 막습니다 — 과거에 줄인 것을 다시 늘리려 할 때 알아챕니다.
  </div>
</div>
</div>''')

S[11] = ('dark', '', 'PRACTICE', '''
<div class="cover" style="height:100%">
  <div class="top">PRACTICE 01 — 03</div>
  <div class="mid">
    <h1 style="font-size:88px">세 실습은<br>한 팀이 성장하는 세 단계입니다</h1>
    <p class="sub" style="font-size:29px;max-width:44ch">난이도 순서가 아닙니다. 그리고 <b style="color:#faf9f5">실습 3은 실습 2의 결과물을 입력으로 씁니다.</b></p>
  </div>
  <svg width="1720" height="200" viewBox="0 0 1720 200" style="margin-top:auto" role="img" aria-label="실습 1은 팀을 만들고, 실습 2는 구조를 고르고, 실습 3은 산출물을 다듬습니다. 실습 2의 산출물이 실습 3의 입력이 됩니다.">
    <g font-size="20">
      <rect x="0" y="40" width="520" height="112" rx="14" fill="#252320"/>
      <text x="36" y="80" fill="#cc785c" font-family="Fraunces, Georgia, serif" font-size="20" font-weight="700">PRACTICE 01</text>
      <text x="36" y="118" fill="#faf9f5" font-size="30" font-weight="700">팀을 만든다</text>
      <text x="36" y="146" fill="#7c766d" font-size="18">업무 설명 한 문장 → 전문 역할</text>

      <path d="M540 96h56" stroke="#cc785c" stroke-width="3"/><path d="M596 96l-12-7v14z" fill="#cc785c"/>

      <rect x="600" y="40" width="520" height="112" rx="14" fill="#252320"/>
      <text x="636" y="80" fill="#cc785c" font-family="Fraunces, Georgia, serif" font-size="20" font-weight="700">PRACTICE 02</text>
      <text x="636" y="118" fill="#faf9f5" font-size="30" font-weight="700">구조를 고른다</text>
      <text x="636" y="146" fill="#7c766d" font-size="18">독립 조사 → 통합 → 별도 검토</text>

      <path d="M1140 96h56" stroke="#cc785c" stroke-width="3"/><path d="M1196 96l-12-7v14z" fill="#cc785c"/>

      <rect x="1200" y="40" width="520" height="112" rx="14" fill="#252320"/>
      <text x="1236" y="80" fill="#cc785c" font-family="Fraunces, Georgia, serif" font-size="20" font-weight="700">PRACTICE 03</text>
      <text x="1236" y="118" fill="#faf9f5" font-size="30" font-weight="700">산출물을 다듬는다</text>
      <text x="1236" y="146" fill="#7c766d" font-size="18">형식과 내용을 분리해 검토</text>

      <path d="M860 30V8h600v22" stroke="#4fa595" stroke-width="2" stroke-dasharray="6 5" fill="none"/>
      <path d="M1460 34l-5-9h10z" fill="#4fa595"/>
      <text x="1160" y="0" text-anchor="middle" fill="#4fa595" font-size="17" dy="-2">산출물을 그대로 입력으로</text>
    </g>
  </svg>
</div>''')

S[12] = ('light', 'P1', 'BRIEF', '''
<style>.brief pre{font-size:21.5px;line-height:1.6;padding:24px 30px}.brief .bar{padding:16px 30px}td{padding:13px 20px 13px 0;font-size:21px}</style>
<h1 class="sm">실습 1 · 유튜브 콘텐츠 기획 팀</h1>
<p class="lede" style="margin-top:18px">업무 설명 한 문장으로 <b>전문가 팀이 만들어지는 것</b>을 직접 봅니다.</p>
<div class="body" style="margin-top:24px">
<div class="grid" style="grid-template-columns:1.42fr 1fr;gap:34px">
  <div class="brief">
    <div class="bar"><span>COPY &amp; RUN</span><em>대괄호 두 곳만 바꿉니다</em></div>
<pre>하네스를 구성해줘.
<span class="ph">[브랜드/주제]</span>를 위한 유튜브 콘텐츠 기획 팀이 필요해.
트렌드 조사, 8–10분 대본 기획, 제목·태그 SEO,
썸네일 콘셉트를 맡기고,
최종적으로 1주치 콘텐츠 기획안을 만들어줘.
대상은 <span class="ph">[20대 직장인]</span>이고, 주장마다 근거 출처를 남겨줘.</pre>
  </div>
  <div>
    <div style="font-size:21px;font-weight:700;letter-spacing:1.4px;text-transform:uppercase;color:var(--muted)">좋은 브리프의 네 요소</div>
    <table style="margin-top:18px">
      <tr><td style="width:92px"><b>목표</b><br><span style="font-size:17px;color:var(--faint)">무엇을 받고 싶은가</span></td><td>1주치 콘텐츠 기획안</td></tr>
      <tr><td><b>대상</b><br><span style="font-size:17px;color:var(--faint)">누구를 위한 것인가</span></td><td>20대 직장인</td></tr>
      <tr><td><b>역할</b><br><span style="font-size:17px;color:var(--faint)">누가 필요한가</span></td><td>트렌드 조사 · 대본 기획<br>제목·태그 SEO · 썸네일 콘셉트</td></tr>
      <tr><td><b>기준</b><br><span style="font-size:17px;color:var(--faint)">무엇을 지켜야 하는가</span></td><td>주장마다 근거 출처</td></tr>
    </table>
  </div>
</div>
<div class="banner" style="margin-top:24px;font-size:23px;padding:24px 32px">
  네 요소 중 <b>하나라도 비면 하네스가 대신 정합니다.</b> 그래서 결과가 매번 달라집니다 — 결과가 흔들릴 때는 브리프의 빈 요소를 먼저 찾으세요.
</div>
</div>''')

S[13] = ('light', 'P1', 'TEAM', '''
<h1 class="sm">네 담당이 각자 결과를 내고, 통합 담당이 하나로 묶습니다</h1>
<div class="body" style="margin-top:30px">
<svg class="dg" width="1720" height="430" viewBox="0 0 1720 430" role="img" aria-labelledby="p1-t p1-d">
  <title id="p1-t">실습 1의 팀 구조</title>
  <desc id="p1-d">브리프 한 문장에서 트렌드 조사·대본 기획·제목 태그 SEO·썸네일 콘셉트 네 담당으로 갈라지고, 편집 통합 담당이 그 넷을 하나의 1주치 콘텐츠 기획안으로 묶습니다.</desc>
  <defs><marker id="a1" viewBox="0 0 12 12" refX="9" refY="6" markerWidth="9" markerHeight="9" orient="auto">
    <path d="M1 1L10 6L1 11z" fill="#cc785c"/></marker></defs>

  <rect x="0" y="160" width="230" height="106" rx="14" fill="#181715"/>
  <text x="115" y="204" text-anchor="middle" fill="#faf9f5" font-size="26" font-weight="700">브리프</text>
  <text x="115" y="236" text-anchor="middle" fill="#b3aea5" font-size="19">한 문장</text>

  <path d="M244 213h60" stroke="#cc785c" stroke-width="2.5" marker-end="url(#a1)"/>

  <rect x="320" y="16" width="420" height="86" rx="12" fill="#fff" stroke="#e2dad0"/>
  <text x="352" y="52" fill="#141413" font-size="24" font-weight="700">트렌드 리서처</text>
  <text x="352" y="80" fill="#6c6a64" font-size="18">소재 후보 + 근거 링크</text>

  <rect x="320" y="114" width="420" height="86" rx="12" fill="#fff" stroke="#e2dad0"/>
  <text x="352" y="150" fill="#141413" font-size="24" font-weight="700">대본 기획자</text>
  <text x="352" y="178" fill="#6c6a64" font-size="18">구성안 (도입·전개·마무리)</text>

  <rect x="320" y="226" width="420" height="86" rx="12" fill="#fff" stroke="#e2dad0"/>
  <text x="352" y="262" fill="#141413" font-size="24" font-weight="700">SEO 담당</text>
  <text x="352" y="290" fill="#6c6a64" font-size="18">제목 3안 + 태그 세트</text>

  <rect x="320" y="324" width="420" height="86" rx="12" fill="#fff" stroke="#e2dad0"/>
  <text x="352" y="360" fill="#141413" font-size="24" font-weight="700">썸네일 콘셉트</text>
  <text x="352" y="388" fill="#6c6a64" font-size="18">콘셉트 문구 + 구도 설명</text>

  <text x="530" y="430" text-anchor="middle" fill="#a9583e" font-size="19" font-weight="700">서로를 기다리지 않는다</text>

  <path d="M756 59h84M756 157h84M756 269h84M756 367h84" stroke="#d8cec2" stroke-width="2"/>
  <path d="M840 59v154M840 157v56M840 269v-56M840 367v-154" stroke="#d8cec2" stroke-width="2" fill="none"/>
  <path d="M840 213h48" stroke="#cc785c" stroke-width="2.5" marker-end="url(#a1)"/>

  <rect x="906" y="160" width="250" height="106" rx="14" fill="#efe9de"/>
  <text x="1031" y="198" text-anchor="middle" fill="#141413" font-size="26" font-weight="700">편집 통합</text>
  <text x="1031" y="230" text-anchor="middle" fill="#6c6a64" font-size="18">네 결과를 하나로</text>

  <path d="M1170 213h58" stroke="#cc785c" stroke-width="2.5" marker-end="url(#a1)"/>

  <rect x="1246" y="146" width="474" height="134" rx="14" fill="#fff" stroke="#cc785c" stroke-width="2.5"/>
  <text x="1483" y="192" text-anchor="middle" fill="#141413" font-size="30" font-weight="900">1주치 콘텐츠 기획안</text>
  <text x="1483" y="228" text-anchor="middle" fill="#3d3d3a" font-size="20">조사한 소재에 대본 · 제목 · 썸네일이</text>
  <text x="1483" y="256" text-anchor="middle" fill="#3d3d3a" font-size="20">각각 붙어 있어야 합니다</text>
</svg>
<div class="grid g2" style="margin-top:24px;gap:26px">
  <div class="banner coral" style="font-size:22px;padding:24px 30px">
    <b>정답이 아니라 대조용 기준선입니다.</b> 하네스는 실행할 때마다 다른 팀을 만듭니다 — <b>역할 경계 · 전달 관계 · 최종 형식 · 별도 리뷰</b> 네 가지가 정해졌으면 성공입니다.
  </div>
  <div class="banner" style="font-size:22px;padding:24px 30px">
    <b>브리프는 편수를 정하지 않습니다.</b> 몇 편이 나오는지는 하네스가 정하며 개수는 판정 기준이 아닙니다. 볼 것은 <b>네 결과가 서로 연결되어 있는가</b>입니다.
  </div>
</div>
</div>''')

S[14] = ('light', 'P2', 'MULTI-AGENT', '''
<h1 class="sm">멀티에이전트는 “여러 답변”이 아니라 “협업 구조”입니다</h1>
<div class="body" style="margin-top:34px">
<div class="vs">
  <div class="bad">
    <div class="lab">이것은 멀티에이전트가 아니다</div>
    <h3>같은 질문을 여러 번</h3>
    <svg class="dg" width="740" height="188" viewBox="0 0 740 188" role="img" aria-label="같은 질문을 여러 번 물어 답이 여러 개 나오지만 서로를 모릅니다">
      <g font-size="19" fill="#3d3d3a">
        <rect x="0" y="10" width="130" height="48" rx="9" fill="#e8e0d2"/><text x="65" y="40" text-anchor="middle">질문</text>
        <rect x="0" y="70" width="130" height="48" rx="9" fill="#e8e0d2"/><text x="65" y="100" text-anchor="middle">질문</text>
        <rect x="0" y="130" width="130" height="48" rx="9" fill="#e8e0d2"/><text x="65" y="160" text-anchor="middle">질문</text>
        <path d="M140 34h40M140 94h40M140 154h40" stroke="#c9c1b6" stroke-width="2"/>
        <rect x="190" y="10" width="150" height="48" rx="9" fill="#fff" stroke="#e2dad0"/><text x="265" y="40" text-anchor="middle">답 1</text>
        <rect x="190" y="70" width="150" height="48" rx="9" fill="#fff" stroke="#e2dad0"/><text x="265" y="100" text-anchor="middle">답 2</text>
        <rect x="190" y="130" width="150" height="48" rx="9" fill="#fff" stroke="#e2dad0"/><text x="265" y="160" text-anchor="middle">답 3</text>
        <text x="380" y="82" font-size="46" fill="#c9c1b6">✕</text>
        <text x="448" y="76" font-size="20" fill="#6c6a64">서로를 모른다</text>
        <text x="448" y="106" font-size="20" fill="#6c6a64">합쳐 줄 사람이 없다</text>
      </g>
    </svg>
  </div>
  <div class="good">
    <div class="lab">이것이 멀티에이전트다</div>
    <h3>담당을 나누고 넘긴다</h3>
    <svg class="dg" width="740" height="188" viewBox="0 0 740 188" role="img" aria-label="담당을 나누고 누가 누구에게 무엇을 넘기는지 정합니다. 조사하는 사람과 통합하는 사람과 검사하는 사람이 다릅니다.">
      <g font-size="19" fill="#3d3d3a">
        <rect x="0" y="10" width="150" height="48" rx="9" fill="#efe9de"/><text x="75" y="40" text-anchor="middle">조사 A</text>
        <rect x="0" y="70" width="150" height="48" rx="9" fill="#efe9de"/><text x="75" y="100" text-anchor="middle">조사 B</text>
        <rect x="0" y="130" width="150" height="48" rx="9" fill="#efe9de"/><text x="75" y="160" text-anchor="middle">조사 C</text>
        <path d="M158 34h34v60M158 94h34M158 154h34V94" stroke="#cc785c" stroke-width="2" fill="none"/>
        <path d="M192 94h34" stroke="#cc785c" stroke-width="2"/><path d="M226 94l-9-5v10z" fill="#cc785c"/>
        <rect x="234" y="70" width="150" height="48" rx="9" fill="#181715"/><text x="309" y="100" text-anchor="middle" fill="#faf9f5">통합</text>
        <path d="M392 94h34" stroke="#4fa595" stroke-width="2"/><path d="M426 94l-9-5v10z" fill="#4fa595"/>
        <rect x="434" y="70" width="150" height="48" rx="9" fill="#fff" stroke="#4fa595" stroke-width="2"/><text x="509" y="100" text-anchor="middle">검증</text>
        <path d="M509 66V40H309v26" stroke="#4fa595" stroke-width="1.8" stroke-dasharray="5 4" fill="none"/>
        <path d="M309 70l-5-9h10z" fill="#4fa595"/>
        <text x="409" y="30" text-anchor="middle" fill="#2f7d70" font-size="17">수정 요청</text>
        <text x="600" y="88" font-size="20" fill="#141413" font-weight="700">전달 관계가</text>
        <text x="600" y="116" font-size="20" fill="#141413" font-weight="700">정해져 있다</text>
      </g>
    </svg>
  </div>
</div>
<div class="banner dark-b" style="margin-top:28px">
  <b style="font-size:27px">구분 질문은 하나입니다 — 담당끼리 결과를 주고받아야 하는가.</b><br>
  <span style="font-size:22px;color:var(--on-dark-mid)">주고받을 것이 없으면 그냥 여러 번 물어보는 것이고, 주고받아야 하면 구조가 필요합니다.
  구조를 나누는 것은 <b style="color:#faf9f5">능력을 늘리는 것이 아니라 편향을 끊는 것</b>입니다 — 조사한 사람이 통합까지 하면 자기가 찾은 것에 맞춰 결론을 만듭니다.</span>
</div>
</div>''')
