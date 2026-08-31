# -*- coding: utf-8 -*-
"""슬라이드 15~20 — 실습 2 브리프·팀 · 실습 3 · 시작하기"""
S = {}

S[15] = ('light', 'P2', 'BRIEF', '''
<h1 class="sm">실습 2 · 브랜드 마케팅 전략보고서</h1>
<p class="lede">이 브리프는 <b>팀 구조를 직접 지정합니다</b> — 하네스에게 맡기지 않습니다.</p>
<div class="body" style="margin-top:28px">
<div class="brief">
  <div class="bar"><span>COPY &amp; RUN</span><em>대괄호 두 곳만 바꿉니다</em></div>
<pre><span class="ph">[브랜드]</span>의 <span class="ph">[제품/서비스]</span>를 위한  마케팅 전략보고서 하네스를 구성해줘.
시장·고객·경쟁·채널을 <span style="color:#e8a55a">독립적으로 조사한 뒤 전략가가 통합</span>하고,
<span style="color:#8fd6c7">별도 리뷰어가</span> 근거·실행 가능성·누락을 점검하게 해줘.
최종 산출물은 1페이지 요약, 실행 우선순위 표, 측정지표를 포함해줘.
사실과 가정을 구분하고 모든 외부 주장에 출처를 남겨줘.</pre>
</div>
<div class="grid g2" style="margin-top:30px;gap:30px">
  <div class="card accent">
    <div class="k">이 문장이 만드는 것</div>
    <h3 style="font-size:27px">팬아웃 / 팬인</h3>
    <p style="font-size:20px">조사자 4명이 <b>서로를 기다리지 않고</b> 각자 조사하고, 전략가 1명이 합칩니다.</p>
  </div>
  <div class="card verify">
    <div class="k">이 문장이 만드는 것</div>
    <h3 style="font-size:27px">생성-검증</h3>
    <p style="font-size:20px">만든 담당과 검사하는 담당이 <b>다른 사람</b>이 됩니다.</p>
  </div>
</div>
<div class="banner coral" style="margin-top:26px">
  <b>“별도”라는 단어 하나가 에이전트 하나를 만듭니다.</b> 이 단어를 빼면 전략가가 자기 결과를 자기가 검토하고 — 그러면 거의 언제나 “문제 없음”이 나옵니다.
</div>
</div>''')

S[16] = ('light', 'P2', 'TEAM', '''
<h1 class="sm">관점은 병렬로, 결론은 하나로, 품질은 별도로</h1>
<div class="body" style="margin-top:26px">
<svg class="dg" width="1720" height="470" viewBox="0 0 1720 470" role="img" aria-labelledby="p2-t p2-d">
  <title id="p2-t">실습 2의 팬아웃/팬인 + 생성-검증 구조</title>
  <desc id="p2-d">브리프가 시장·고객·경쟁·채널 네 조사로 갈라지고, 전략가가 하나로 통합한 뒤 별도 리뷰어가 검증해 최종 전략보고서가 됩니다. 리뷰어의 수정 요청은 전략가로 되돌아갑니다.</desc>
  <defs>
    <marker id="a2" viewBox="0 0 12 12" refX="9" refY="6" markerWidth="9" markerHeight="9" orient="auto"><path d="M1 1L10 6L1 11z" fill="#cc785c"/></marker>
    <marker id="a2t" viewBox="0 0 12 12" refX="9" refY="6" markerWidth="9" markerHeight="9" orient="auto"><path d="M1 1L10 6L1 11z" fill="#4fa595"/></marker>
  </defs>

  <rect x="0" y="182" width="200" height="100" rx="14" fill="#181715"/>
  <text x="100" y="240" text-anchor="middle" fill="#faf9f5" font-size="25" font-weight="700">브리프</text>
  <path d="M214 232h50" stroke="#cc785c" stroke-width="2.5" marker-end="url(#a2)"/>

  <rect x="280" y="56" width="330" height="80" rx="12" fill="#fff" stroke="#e2dad0"/>
  <text x="310" y="90" fill="#141413" font-size="23" font-weight="700">시장 조사</text><text x="310" y="118" fill="#6c6a64" font-size="18">카테고리 · 변화</text>
  <rect x="280" y="148" width="330" height="80" rx="12" fill="#fff" stroke="#e2dad0"/>
  <text x="310" y="182" fill="#141413" font-size="23" font-weight="700">고객 조사</text><text x="310" y="210" fill="#6c6a64" font-size="18">니즈 · 장벽</text>
  <rect x="280" y="240" width="330" height="80" rx="12" fill="#fff" stroke="#e2dad0"/>
  <text x="310" y="274" fill="#141413" font-size="23" font-weight="700">경쟁 조사</text><text x="310" y="302" fill="#6c6a64" font-size="18">포지션 · 빈 자리</text>
  <rect x="280" y="332" width="330" height="80" rx="12" fill="#fff" stroke="#e2dad0"/>
  <text x="310" y="366" fill="#141413" font-size="23" font-weight="700">채널 조사</text><text x="310" y="394" fill="#6c6a64" font-size="18">도달 · 비용</text>

  <text x="445" y="446" text-anchor="middle" fill="#a9583e" font-size="19" font-weight="700">각자 사실 + 출처</text>

  <path d="M624 96h56M624 188h56M624 280h56M624 372h56" stroke="#d8cec2" stroke-width="2"/>
  <path d="M680 96v136M680 188v44M680 280v-48M680 372v-140" stroke="#d8cec2" stroke-width="2" fill="none"/>
  <path d="M680 232h44" stroke="#cc785c" stroke-width="2.5" marker-end="url(#a2)"/>

  <rect x="742" y="182" width="230" height="100" rx="14" fill="#efe9de"/>
  <text x="857" y="222" text-anchor="middle" fill="#141413" font-size="25" font-weight="700">전략가</text>
  <text x="857" y="252" text-anchor="middle" fill="#6c6a64" font-size="18">통합 — 하나의 선택으로</text>

  <path d="M986 232h50" stroke="#4fa595" stroke-width="2.5" marker-end="url(#a2t)"/>

  <rect x="1054" y="182" width="230" height="100" rx="14" fill="#fff" stroke="#4fa595" stroke-width="2.5"/>
  <text x="1169" y="222" text-anchor="middle" fill="#141413" font-size="25" font-weight="700">리뷰어</text>
  <text x="1169" y="252" text-anchor="middle" fill="#6c6a64" font-size="18">근거 · 실행 가능성 · 누락</text>

  <path d="M1169 176V128H857v48" stroke="#4fa595" stroke-width="2" stroke-dasharray="6 5" fill="none"/>
  <path d="M857 182l-6-11h12z" fill="#4fa595"/>
  <text x="1013" y="116" text-anchor="middle" fill="#2f7d70" font-size="19" font-weight="700">수정 요청</text>

  <path d="M1298 232h44" stroke="#cc785c" stroke-width="2.5" marker-end="url(#a2)"/>
  <rect x="1360" y="164" width="360" height="136" rx="14" fill="#fff" stroke="#cc785c" stroke-width="2.5"/>
  <text x="1540" y="206" text-anchor="middle" fill="#141413" font-size="27" font-weight="900">전략보고서</text>
  <text x="1540" y="240" text-anchor="middle" fill="#3d3d3a" font-size="19">1페이지 요약 · 실행 우선순위 표</text>
  <text x="1540" y="268" text-anchor="middle" fill="#3d3d3a" font-size="19">측정지표</text>

  <text x="445" y="30" text-anchor="middle" fill="#cc785c" font-family="Fraunces, Georgia, serif" font-size="21" font-weight="700">FAN-OUT / FAN-IN</text>
  <text x="1169" y="30" text-anchor="middle" fill="#2f7d70" font-family="Fraunces, Georgia, serif" font-size="21" font-weight="700">GENERATE — VERIFY</text>
</svg>
<div class="banner dark-b" style="margin-top:20px">
  <b style="font-size:27px">좋은 전략보고서는 정보보다 “선택”을 보여줍니다.</b><br>
  <span style="font-size:22px;color:var(--on-dark-mid)">그래서 1페이지 요약에는 <b style="color:#faf9f5">“무엇을 하지 않을 것인가”</b>가 반드시 있어야 합니다. 그 문장이 없으면 그것은 아직 전략이 아니라 조사 결과입니다.
  &nbsp;·&nbsp; 결과는 <b style="color:#faf9f5">파일로 저장하세요</b> — 실습 3의 입력입니다.</span>
</div>
</div>''')

S[17] = ('light', 'P3', 'BRIEF', '''
<h1 class="sm">실습 3 · 샘플 형식으로 새 PPT 만들기</h1>
<p class="lede">형식은 샘플에서, 내용은 실습 2에서 — <b>둘을 분리해 말하는 것</b>이 이 실습의 기술입니다.</p>
<div class="body" style="margin-top:26px">
<div class="brief">
  <div class="bar"><span>COPY &amp; RUN</span><em>sample.pptx + 실습 2의 산출물</em></div>
<pre>sample.pptx의 형식과 디자인을 재해석해 전략 보고서를 PPT로 만드는 하네스를 구성해줘.
먼저 sample.pptx에서 형식 규칙 — <span style="color:#e8a55a">폰트 계층, 외곽 여백, 정렬선, 색의 역할,
카드·표현 방식, 한 장의 정보량</span> — 을 추출하게 해줘.
그 규칙과 실습 2에서 만든 마케팅 전략보고서를 이용해 새 슬라이드 3장을 만들어줘.
1장은 문제와 기회, 2장은 실행 우선순위, 3장은 측정과 다음 행동으로 구성해줘.
<span style="color:#8fd6c7">내용 리뷰와 형식 리뷰를 맡는 리뷰어를 각각 두고</span>, 텍스트·표·도형은 편집 가능하게 유지해줘.</pre>
</div>
<div class="grid g2" style="margin-top:28px;gap:30px">
  <div class="banner coral" style="font-size:22px;padding:26px 32px">
    <b>sample.pptx 는 렌더된 이미지입니다 — 텍스트를 복사할 수 없습니다.</b><br>
    그것이 의도입니다. 붙여넣기가 통하지 않으므로 <b>눈으로 읽어 규칙을 언어로 정리</b>하는 것부터 시작해야 합니다.
  </div>
  <div class="banner" style="font-size:22px;padding:26px 32px;background:#e6f2ef;border-left:6px solid var(--teal)">
    <b>실습 2를 건너뛰었어도 됩니다.</b><br>
    <span style="font-family:var(--mono);font-size:19px">example-strategy.md</span> 를 내려받아 대신 쓰면 실습 3만 따로 할 수 있습니다.
  </div>
</div>
</div>''')

S[18] = ('light', 'P3', 'TEAM', '''
<h1 class="sm">형식과 내용이 따로 들어와 하나로 합쳐지고, 검토도 따로 이뤄집니다</h1>
<div class="body" style="margin-top:30px">
<svg class="dg" width="1720" height="420" viewBox="0 0 1720 420" role="img" aria-labelledby="p3-t p3-d">
  <title id="p3-t">실습 3의 파이프라인 + 검토 분리 구조</title>
  <desc id="p3-d">샘플 pptx는 형식 분석가로, 실습 2의 전략은 내용 구성자로 들어갑니다. 둘의 결과가 슬라이드 제작자로 합쳐지고, 내용 리뷰어와 형식 리뷰어가 각각 검토해 편집 가능한 3장이 됩니다.</desc>
  <defs>
    <marker id="a3" viewBox="0 0 12 12" refX="9" refY="6" markerWidth="9" markerHeight="9" orient="auto"><path d="M1 1L10 6L1 11z" fill="#cc785c"/></marker>
    <marker id="a3t" viewBox="0 0 12 12" refX="9" refY="6" markerWidth="9" markerHeight="9" orient="auto"><path d="M1 1L10 6L1 11z" fill="#4fa595"/></marker>
  </defs>

  <rect x="0" y="46" width="228" height="86" rx="12" fill="#efe9de"/>
  <text x="114" y="82" text-anchor="middle" fill="#141413" font-size="23" font-weight="700">sample.pptx</text>
  <text x="114" y="110" text-anchor="middle" fill="#6c6a64" font-size="18">형식 참조</text>
  <rect x="0" y="288" width="228" height="86" rx="12" fill="#efe9de"/>
  <text x="114" y="324" text-anchor="middle" fill="#141413" font-size="23" font-weight="700">실습 2 전략</text>
  <text x="114" y="352" text-anchor="middle" fill="#6c6a64" font-size="18">또는 예시 보고서</text>

  <path d="M242 89h52M242 331h52" stroke="#cc785c" stroke-width="2.5" marker-end="url(#a3)"/>

  <rect x="312" y="46" width="300" height="86" rx="12" fill="#fff" stroke="#e2dad0"/>
  <text x="462" y="82" text-anchor="middle" fill="#141413" font-size="23" font-weight="700">형식 분석가</text>
  <text x="462" y="110" text-anchor="middle" fill="#6c6a64" font-size="18">규칙 6종 추출</text>
  <rect x="312" y="288" width="300" height="86" rx="12" fill="#fff" stroke="#e2dad0"/>
  <text x="462" y="324" text-anchor="middle" fill="#141413" font-size="23" font-weight="700">내용 구성자</text>
  <text x="462" y="352" text-anchor="middle" fill="#6c6a64" font-size="18">3장 스토리로 재구성</text>

  <path d="M626 89h44v122M626 331h44V211" stroke="#d8cec2" stroke-width="2" fill="none"/>
  <path d="M670 211h40" stroke="#cc785c" stroke-width="2.5" marker-end="url(#a3)"/>

  <rect x="728" y="164" width="266" height="96" rx="13" fill="#181715"/>
  <text x="861" y="204" text-anchor="middle" fill="#faf9f5" font-size="24" font-weight="700">슬라이드 제작자</text>
  <text x="861" y="234" text-anchor="middle" fill="#b3aea5" font-size="18">규칙 + 내용</text>

  <path d="M1008 212h40v-96h44M1008 212h40v96h44" stroke="#4fa595" stroke-width="2.5" fill="none"/>
  <path d="M1092 116l-11-6v12zM1092 308l-11-6v12z" fill="#4fa595"/>

  <rect x="1100" y="74" width="272" height="84" rx="12" fill="#fff" stroke="#4fa595" stroke-width="2.5"/>
  <text x="1236" y="108" text-anchor="middle" fill="#141413" font-size="23" font-weight="700">내용 리뷰어</text>
  <text x="1236" y="136" text-anchor="middle" fill="#6c6a64" font-size="18">메시지 · 근거 · 수치</text>
  <rect x="1100" y="266" width="272" height="84" rx="12" fill="#fff" stroke="#4fa595" stroke-width="2.5"/>
  <text x="1236" y="300" text-anchor="middle" fill="#141413" font-size="23" font-weight="700">형식 리뷰어</text>
  <text x="1236" y="328" text-anchor="middle" fill="#6c6a64" font-size="18">규칙 준수 · 오버플로 · 정렬</text>

  <path d="M1386 116h42v96M1386 308h42v-96" stroke="#cc785c" stroke-width="2" fill="none"/>
  <path d="M1428 212h34" stroke="#cc785c" stroke-width="2.5" marker-end="url(#a3)"/>

  <rect x="1480" y="152" width="240" height="120" rx="13" fill="#fff" stroke="#cc785c" stroke-width="2.5"/>
  <text x="1600" y="196" text-anchor="middle" fill="#141413" font-size="28" font-weight="900">PPT 3장</text>
  <text x="1600" y="230" text-anchor="middle" fill="#a9583e" font-size="20" font-weight="700">편집 가능</text>
  <text x="1600" y="256" text-anchor="middle" fill="#6c6a64" font-size="17">이미지로 굽히면 실패</text>

  <text x="462" y="24" text-anchor="middle" fill="#cc785c" font-family="Fraunces, Georgia, serif" font-size="21" font-weight="700">PIPELINE</text>
  <text x="1236" y="24" text-anchor="middle" fill="#2f7d70" font-family="Fraunces, Georgia, serif" font-size="21" font-weight="700">SPLIT REVIEW</text>
  <text x="861" y="404" text-anchor="middle" fill="#928d84" font-size="19">한 사람이 내용과 형식을 동시에 보면 둘 다 놓칩니다</text>
</svg>
</div>''')

S[19] = ('light', 'P3', 'OUTPUT', '''
<h1 class="sm">규칙 6종을 뽑고, 세 장의 결정 스토리로 만듭니다</h1>
<div class="body" style="margin-top:34px">
<div class="grid" style="grid-template-columns:1fr 1.16fr;gap:44px">
  <div>
    <div style="font-size:21px;font-weight:700;letter-spacing:1.4px;text-transform:uppercase;color:var(--muted)">추출할 형식 규칙 6종</div>
    <table style="margin-top:18px">
      <tr><td style="width:200px"><b>폰트 계층</b></td><td>제목 / 소제목 / 본문 / 캡션의 크기·굵기 관계</td></tr>
      <tr><td><b>외곽 여백</b></td><td>슬라이드 가장자리의 안전 영역</td></tr>
      <tr><td><b>정렬선</b></td><td>요소들이 공통으로 시작하는 좌측 기준선</td></tr>
      <tr><td><b>색의 역할</b></td><td>지배색 / 강조색 / 상태색이 각각 어디에</td></tr>
      <tr><td><b>카드·표현 방식</b></td><td>정보를 담는 반복 단위</td></tr>
      <tr><td><b>한 장의 정보량</b></td><td>한 슬라이드가 다루는 메시지 개수</td></tr>
    </table>
    <div class="banner coral" style="margin-top:26px;font-size:21px;padding:22px 28px">
      “예쁘게 따라 해”라고 하면 AI 는 자기 취향으로 만듭니다. <b>뽑을 항목을 지정하면 규칙이 언어로 남고, 다음에 재사용할 수 있습니다.</b>
    </div>
  </div>
  <div>
    <div style="font-size:21px;font-weight:700;letter-spacing:1.4px;text-transform:uppercase;color:var(--muted)">만들 3장 — 문제 → 선택 → 측정</div>
    <div style="margin-top:18px">
      <div class="card" style="border-left:6px solid var(--coral);padding:26px 30px">
        <div style="display:flex;align-items:baseline;gap:18px">
          <span style="font-family:var(--lat);font-size:34px;font-weight:700;color:var(--coral-deep)">01</span>
          <div><h3 style="font-size:29px;margin:0">문제와 기회</h3>
          <p style="font-size:20px;margin-top:8px">왜 지금 이 타깃과 이 메시지인가?</p></div>
        </div>
      </div>
      <div class="card" style="border-left:6px solid var(--coral);padding:26px 30px;margin-top:18px">
        <div style="display:flex;align-items:baseline;gap:18px">
          <span style="font-family:var(--lat);font-size:34px;font-weight:700;color:var(--coral-deep)">02</span>
          <div><h3 style="font-size:29px;margin:0">실행 우선순위</h3>
          <p style="font-size:20px;margin-top:8px">무엇을 먼저, 누가, 언제 할 것인가?</p></div>
        </div>
      </div>
      <div class="card" style="border-left:6px solid var(--coral);padding:26px 30px;margin-top:18px">
        <div style="display:flex;align-items:baseline;gap:18px">
          <span style="font-family:var(--lat);font-size:34px;font-weight:700;color:var(--coral-deep)">03</span>
          <div><h3 style="font-size:29px;margin:0">측정과 다음 행동</h3>
          <p style="font-size:20px;margin-top:8px">무엇으로 성공을 판단할 것인가?</p></div>
        </div>
      </div>
    </div>
    <div class="banner" style="margin-top:22px;font-size:21px;padding:22px 28px;background:#e6f2ef;border-left:6px solid var(--teal)">
      세 장 모두 <b>편집 가능</b>해야 합니다 — 텍스트는 텍스트 프레임, 표는 표, 도형은 도형.
    </div>
  </div>
</div>
</div>''')

S[20] = ('dark', '', 'START HERE', '''
<div class="cover" style="height:100%">
  <div class="top">START HERE</div>
  <div class="mid">
    <h1 style="font-size:80px">설치는 사전에,<br>실습은 수업에서</h1>
    <div class="grid g2" style="margin-top:46px;gap:40px;max-width:1500px">
      <div style="background:#252320;border-radius:16px;padding:34px 38px">
        <div style="font-family:var(--lat);font-size:19px;font-weight:700;letter-spacing:2.2px;color:var(--coral)">COPY &amp; RUN</div>
        <pre style="font-family:var(--mono);font-size:24px;line-height:1.8;color:#faf9f5;margin-top:18px;white-space:pre">/plugin marketplace add revfactory/harness
/plugin install harness@harness-marketplace</pre>
        <p style="font-size:19px;color:var(--on-dark-faint);margin-top:18px">Claude Pro / Max / Team / Enterprise 중 하나가 필요합니다.<br><b style="color:#faf9f5">API Key 는 필요하지 않습니다.</b></p>
      </div>
      <div style="padding-top:6px">
        <div style="font-size:23px;color:var(--on-dark-mid);line-height:1.6">
          <div style="font-size:20px;font-family:var(--lat);font-weight:700;letter-spacing:2px;color:var(--coral)">교재</div>
          <div style="font-size:31px;color:#faf9f5;font-weight:700;margin-top:10px;font-family:var(--mono)">namojo.github.io/harness-edu2</div>
          <div style="height:1px;background:#35322c;margin:30px 0"></div>
          <div style="font-size:20px;font-family:var(--lat);font-weight:700;letter-spacing:2px;color:var(--coral)">실습 파일</div>
          <div style="font-size:24px;color:#faf9f5;margin-top:10px;font-family:var(--mono)">github.com/namojo/harness-edu</div>
          <div style="font-size:19px;color:var(--on-dark-faint);margin-top:8px">clone 후 <b style="color:#b3aea5">workshop/</b> 폴더</div>
        </div>
      </div>
    </div>
  </div>
  <div class="strip" style="border-top:1px solid #35322c;padding-top:30px">
    <div><div class="i">RECAP 01</div><div class="n">팀을 만든다</div><div class="d">업무 설명 → 전문 역할</div></div>
    <div><div class="i">RECAP 02</div><div class="n">구조를 고른다</div><div class="d">병렬 조사 → 통합 → 검토</div></div>
    <div><div class="i">RECAP 03</div><div class="n">산출물을 다듬는다</div><div class="d">형식과 내용을 분리</div></div>
    <div><div class="i">NEXT</div><div class="n">내 업무로 다시 쓴다</div><div class="d">목표 · 대상 · 역할 · 기준</div></div>
  </div>
</div>''')
