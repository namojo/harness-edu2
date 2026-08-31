# 잔여 문자열 판단

`verify_port.sh docs` 결과 기준.

| 검사 | 결과 | 판단 |
|---|---|---|
| (a) 브랜드 미치환 | 0건 | 통과 |
| (b) 저장소 URL·폴더 경로 오치환 (`harness-edu2/`, `~/harness-edu2`, `C:\harness-edu2`, `harness-edu22`) | **0건** | 통과 — 51곳 전부 보존 |
| (c) `chapters/` | 0건 | 통과 |
| (c) `차시` | **1건** | `index.html:208` — 의도된 문장. 1세대 폴더가 저장소에 있음을 밝힘 |
| (d) clone URL ↔ cd 대상 일치 | 눈으로 확인 | `git clone … harness-edu` → `cd ~/harness-edu` / `cd C:\harness-edu` 일치 ✓ (`ps1` 포함) |
| (e) `workshop/` 안내 | 있음 | `index.html` 폴더 트리 + `setup-mac/windows` 각 2곳 |
| 앵커 id 보존 (원본 대비) | 유실 0 | 5문서 전부 통과 |

## 링크 미해결 (예정)

`../index.html`, `../concept.html`, `../practice/*.html`, `../index.html#flow` — Phase 3에서 생성. 생성 후 재검증 필요.
