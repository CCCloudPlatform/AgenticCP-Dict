---
title: 문서 구조
---

# 문서 구조

AgenticCP Dict는 다음과 같은 상위 구조를 가집니다.

```text
docs/
  index.md                 # 메인 랜딩 페이지
  getting-started/
    overview.md            # 빠른 시작
    docs-structure.md      # 문서 구조 설명
  encyclopedia/            # 백과사전 항목
    _index.md              # 전체 인덱스/분류
    template.md            # 새 항목 작성 템플릿
  glossary/                # 용어사전
    index.md               # 용어 인덱스
    template.md            # 새 용어 템플릿
  design/
    style-guide.md         # 디자인/톤&매너 가이드
  contributing.md          # 기여 가이드
```

## 백과사전 vs 용어사전

- **백과사전 (`encyclopedia/`)**
  - “문장으로 설명해야 이해되는 것들”
  - 예: 아키텍처, 도메인 개념, 플로우, 패턴
  - 한 항목당 하나의 파일: `cloud-provider.md`, `policy-engine.md` 등

- **용어사전 (`glossary/`)**
  - “한 줄 정의가 있는 명사형 용어들”
  - 예: `Tenant`, `Workspace`, `Execution`, `Run`
  - 파일명은 소문자-하이픈 스타일: `tenant.md`, `execution-context.md`

## 태그 기반 유사 항목 연결

MkDocs Material의 `tags` 플러그인을 사용해 문서 간 **유사도 링크의 기본 신호**로 활용합니다.

- 예시 태그:
  - `cloud`, `workflow`, `policy`, `security`, `tenant`, `core-domain` 등
- 유사 검색 UX에서:
  - 같은 태그를 공유하는 항목을 **“이 개념과 비슷한 항목”** 영역에 노출

## 파일 네이밍 규칙

- 영어 소문자 + 하이픈(`-`) 조합 사용
- 도메인 이름과 최대한 일관성 유지  
  - 예: 자바 클래스 `CloudProvider` → `cloud-provider.md`

---

이 구조를 바탕으로 실제 AgenticCP 도메인 개념들을 백과사전/용어사전에 채워나가면 됩니다.


