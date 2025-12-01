# Author Card Plugin

MkDocs 플러그인: 작성자 카드 자동 생성

## 사용법

### 1. mkdocs.yml에 작성자 프로필 등록

```yaml
extra:
  authors:
    username:
      name: 작성자 이름
      github: GitHub 사용자명
      email: 이메일 (선택)
      bio: 짧은 소개 (선택)
      avatar: 아바타 이미지 URL (선택)
```

### 2. 문서에 작성자 카드 추가

문서 어디서든 다음 문법을 사용:

```markdown
{!author:username}
```

이 문법이 자동으로 작성자 카드로 변환됩니다.

### 3. 플러그인 활성화

`mkdocs.yml`의 `plugins` 섹션에 추가:

```yaml
plugins:
  - author_card:
      enabled: true
```

## 예시

```markdown
## 작성자

{!author:kkooonsj}
```

이렇게 하면 `mkdocs.yml`에 등록된 `kkooonsj` 작성자의 정보를 자동으로 불러와서 작성자 카드를 생성합니다.

## GitHub 아바타 URL

GitHub 아바타를 사용하려면:
- `https://avatars.githubusercontent.com/u/{user_id}?v=4` 형식 사용
- 또는 GitHub 사용자명으로 자동 생성 (플러그인이 처리)

