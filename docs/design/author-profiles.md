---
title: 작성자 프로필 시스템
tags:
  - guide
  - design
---

# 작성자 프로필 시스템

AgenticCP Dict에서는 문서에 작성자 정보를 표시할 수 있는 작성자 프로필 시스템을 제공합니다.

## 작성자 프로필 등록

`mkdocs.yml`의 `extra.authors` 섹션에 작성자 프로필을 등록합니다:

```yaml
extra:
  authors:
    username:
      name: 작성자 이름
      github: GitHub 사용자명
      email: 이메일 (선택사항)
      bio: 짧은 소개 (선택사항)
      avatar: 아바타 이미지 URL (선택사항)
```

### 예시

```yaml
extra:
  authors:
    honggildong:
      name: 홍길동
      github: honggildong
      email: hong@example.com
      bio: "백엔드 개발자, AgenticCP Core 담당"
      avatar: "https://github.com/honggildong.png"
    
    kimyounghee:
      name: 김영희
      github: kimyounghee
      email: kim@example.com
      bio: "프론트엔드 개발자, AgenticCP UI 담당"
```

## 문서에 작성자 카드 추가하기

문서의 front matter에 `author` 필드를 추가하고, 문서 하단에 작성자 카드를 표시합니다.

### 방법 1: Front matter + 수동 카드 (권장)

**1. Front matter에 작성자 추가:**

```markdown
---
title: 문서 제목
author: honggildong
tags:
  - example
---
```

**2. 문서 하단에 작성자 카드 추가:**

```markdown
---

## 작성자

!!! info "작성자"
    **[[홍길동]](https://github.com/honggildong)**  
    백엔드 개발자, AgenticCP Core 담당
    
    [:material-github: GitHub](https://github.com/honggildong){ .md-button .md-button--primary }
    [:material-email: 이메일](mailto:hong@example.com){ .md-button }
```

### 방법 2: 간단한 작성자 링크

문서 하단에 간단하게 작성자 링크만 추가:

```markdown
---

**작성자**: [[홍길동]](https://github.com/honggildong) - 백엔드 개발자
```

## 작성자 카드 템플릿

다음 템플릿을 복사해서 사용하세요:

```markdown
!!! info "작성자"
    **[[작성자 이름]](https://github.com/username)**  
    짧은 소개
    
    [:material-github: GitHub](https://github.com/username){ .md-button .md-button--primary }
    [:material-email: 이메일](mailto:email@example.com){ .md-button }
```

## 여러 작성자 표시

여러 명이 작성한 경우:

```markdown
---

## 작성자

!!! info "작성자"
    **[[홍길동]](https://github.com/honggildong)**  
    백엔드 개발자
    
    [:material-github: GitHub](https://github.com/honggildong){ .md-button .md-button--primary }

!!! info "작성자"
    **[[김영희]](https://github.com/kimyounghee)**  
    프론트엔드 개발자
    
    [:material-github: GitHub](https://github.com/kimyounghee){ .md-button .md-button--primary }
```

## 자동화 (향후 개선)

향후 커스텀 플러그인을 통해 다음과 같은 문법을 지원할 예정입니다:

```markdown
{!author:honggildong}
```

이 문법을 사용하면 `mkdocs.yml`에 등록된 작성자 프로필을 자동으로 불러와 카드를 표시합니다.

## 관련 항목

- [[디자인 가이드]](./style-guide.md)

