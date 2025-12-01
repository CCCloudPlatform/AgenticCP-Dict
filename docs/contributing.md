---
title: 기여 가이드
---

# 기여 가이드

AgenticCP Dict에 기여해 주셔서 감사합니다!  
이 문서는 새 백과사전/용어사전 항목을 추가하는 방법을 설명합니다.

## 1. 환경 설정

```bash
pip install -r requirements.txt
mkdocs serve
```

브라우저에서 `http://localhost:8000` 을 열면 로컬 미리보기를 확인할 수 있습니다.

## 2. 새 문서 추가

- 백과사전 항목: `docs/encyclopedia/template.md` 복사
- 용어사전 항목: `docs/glossary/template.md` 복사

파일명을 도메인 개념에 맞게 변경한 후 내용을 채웁니다.

## 3. 네비게이션에 추가

`mkdocs.yml` 의 `nav` 섹션에 새 항목을 추가합니다.

```yaml
  - 백과사전:
      - 사용 가이드: encyclopedia/how-to-use.md
      - Cloud Provider: encyclopedia/cloud-provider.md
```

## 4. GitHub Pages 배포 (초안)

1. GitHub 리포지토리 설정에서 **Pages** 활성화
2. 브랜치: `gh-pages`, 폴더: `/ (root)` 선택 (또는 Actions 워크플로 사용)
3. 로컬에서:

   ```bash
   mkdocs gh-deploy
   ```

   이 명령은 `gh-pages` 브랜치를 자동으로 생성/업데이트합니다.


