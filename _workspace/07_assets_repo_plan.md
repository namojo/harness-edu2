# namojo/harness-edu 저장소 적용 절차

본 하네스는 파일만 준비했다. **push는 사용자 승인 후 진행한다.**

## 1. 파일 복사

```bash
cp -R /Users/andy/Work/harness-edu2/_workspace/assets/workshop \
      /Users/andy/Work/harness-edu/workshop
```

## 2. 확인

```bash
cd /Users/andy/Work/harness-edu
git status --short workshop/
du -sh workshop/            # 약 1.0MB
git rev-parse --abbrev-ref HEAD   # main 이어야 함 (다운로드 URL이 /raw/main/ 을 가리킴)
```

## 3. 커밋·push

```bash
cd /Users/andy/Work/harness-edu
git add workshop
git commit -m "workshop: 120분 워크샵 실습 3개 환경 추가 (브리프·sample.pptx·예시 전략보고서)"
git push origin main
```

## 4. push 후 링크 재검증 — 생략하지 말 것

**push 전에 만든 raw URL은 전부 404다.** 링크 검사는 push 후에만 의미가 있다.

```bash
cd /Users/andy/Work/harness-edu2
bash .claude/skills/edu-site-qa/scripts/check_assets.sh docs
```

6개 URL이 모두 `200 ✓` 여야 한다. 404가 나오면 브랜치명(`main`)과 경로를 확인한다.

## 추가 고려

- `.gitignore` 에 `*.pptx` 가 잡히지 않는지 확인 (현재 harness-edu의 `.gitignore` 는 213바이트 — 확인 필요)
- 저작권 확인이 끝나지 않았다면 `sample.pptx` 만 보류하고 나머지 5개를 먼저 push할 수 있다. 그 경우 실습 3 페이지의 sample.pptx 링크가 404이므로, 페이지에 `[준비 중]` 표시를 남긴다.
