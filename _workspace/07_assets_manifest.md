# 실습 자산 매니페스트

**저장소:** `namojo/harness-edu` · 기본 브랜치 `main` (2026-08-31 확인)
**정본 위치:** 저장소 `workshop/`. `docs/assets/` 에 사본을 두지 않는다.
**로컬 준비 위치:** `_workspace/assets/workshop/` → push 전 보관

| 파일 | 용량 | 실습 | 저장소 경로 | 웹 다운로드 URL |
|---|---|---|---|---|
| `README.md` | 3.2KB | 전체 | `workshop/README.md` | https://github.com/namojo/harness-edu/raw/main/workshop/README.md |
| `practice-1-youtube/README.md` | 2.4KB | 1 | `workshop/practice-1-youtube/README.md` | https://github.com/namojo/harness-edu/raw/main/workshop/practice-1-youtube/README.md |
| `practice-2-marketing/README.md` | 2.7KB | 2 | `workshop/practice-2-marketing/README.md` | https://github.com/namojo/harness-edu/raw/main/workshop/practice-2-marketing/README.md |
| `practice-3-pptx/README.md` | 3.1KB | 3 | `workshop/practice-3-pptx/README.md` | https://github.com/namojo/harness-edu/raw/main/workshop/practice-3-pptx/README.md |
| **`practice-3-pptx/sample.pptx`** | **976KB** | 3 | `workshop/practice-3-pptx/sample.pptx` | https://github.com/namojo/harness-edu/raw/main/workshop/practice-3-pptx/sample.pptx |
| `practice-3-pptx/example-strategy.md` | 7.6KB | 3 | `workshop/practice-3-pptx/example-strategy.md` | https://github.com/namojo/harness-edu/raw/main/workshop/practice-3-pptx/example-strategy.md |

총 1.0MB. `/raw/` 경로 사용 — `/blob/` 은 pptx 미리보기가 안 되어 학습자가 빈 화면을 본다.

## sample.pptx — 요구 조건 9개 검증

원본(사용자 제공 93.9MB, 10장)에서 **인물 사진이 없는 5장을 발췌**해 1920px JPEG로 렌더한 것.

| 조건 | 결과 |
|---|---|
| 대표 장이 분명 | ✓ 5장 (표지 / 02 시장 분석 / 03 제품 분석 / KEY CONCEPT / 09 광고 효과) |
| 폰트 계층 3단 이상 | ✓ 5단 (섹션번호 · 소제목 · 대제목 · 스탯 수치 · 캡션) |
| 외곽 여백 일정 | ✓ 좌우 상하 안전 영역 일관 |
| 좌측 정렬선 뚜렷 | ✓ 섹션번호·대제목·부제가 같은 x에서 시작 |
| 색의 역할 구분 | ✓ 크림 배경(지배) / 브랜드 레드(강조) / 잉크(본문) 3역 |
| 반복 단위 2개 이상 | ✓ 3열 카드 그리드 (원형 아이콘 + 라벨 + 수치 + 설명), 세로 구분선 |
| 텍스트 편집 가능 | **✗ — 렌더 이미지** |
| 저작권 명확 | **△ 확인 권장** (아래) |
| 50MB 미만 | ✓ 976KB (93.9MB → 1/96) |

### "텍스트 편집 불가"를 결함으로 처리하지 않은 이유

원본 10장이 전부 풀블리드 이미지였다(텍스트 런 총 13개). 편집 가능한 형태로 되돌릴 수 없다.

그러나 이것은 **입력**의 조건이고, 실습 3이 요구하는 편집 가능성은 **출력**의 조건이다. 오히려 입력이 이미지라서 학습자가 텍스트를 복사할 수 없고, 그래서 *"예쁘게 따라 해" 대신 규칙을 언어로 뽑는다*는 이 실습의 교육 목표가 강제된다. 실습 3 페이지와 저장소 README에 이 점을 명시했다.

### 원본에서 제외한 5장과 사유

| 원본 장 | 제외 사유 |
|---|---|
| 2 (01 문제 상황) | 실인물 사진 포함(연예인 이미지) — 공개 저장소 배포 부적합 |
| 5 (소스로써 인식시키자) | 제품 사진 위주로 형식 규칙이 적게 읽힘 |
| **7** | **72MB mp4 동영상** — 93.9MB 용량의 대부분 |
| 8 (반응 그리드) | 실인물 사진 8장 |
| 10 (확장 캠페인) | 실인물 사진 3장 |

### 저작권 — 배포 전 확인 권장

이 파일은 **동원 고추참치 'GO-TO TUNA' 캠페인 제안서**로 보이는 외부 제작물이다. 인물 사진과 동영상은 제외했고 교육용 형식 참조로만 쓰지만, **공개 저장소에 push하기 전 배포 가능 여부를 확인**하는 편이 안전하다.

대안이 필요하면 이 저장소의 워크샵 덱(`harness-engineering-workshop-ko-final*.pptx`)에서 발췌할 수 있다 — 저작권이 명확하고 형식 규칙도 뚜렷하다. 다만 마케팅 제안서 톤이 실습 2의 산출물과 더 잘 맞는 것은 현재 파일이다.
