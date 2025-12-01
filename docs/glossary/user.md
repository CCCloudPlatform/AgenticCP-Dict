---
title: User
tags:
  - user
  - core-domain
---

## 한 줄 정의

조직(=테넌트)에 소속되어, **자신에게 부여된 역할·권한 범위 내에서 AgenticCP 기능과 클라우드 리소스를 사용하는 일반 사용자**.

## 상세 설명

- AgenticCP의 기본 사용 주체로, 보통 `ROLE_USER` 또는 이에 상응하는 역할을 가진다.  
- 자신이 속한 조직(=테넌트)의 리소스만 조회·조작할 수 있으며,  
  플랫폼 전역 설정이나 다른 조직의 리소스에는 접근할 수 없다.
- 실제 권한 범위는 RBAC 설정에 따라 달라질 수 있지만,  
  개념적으로는 “**운영/업무를 수행하는 기본 사용자**”를 의미한다.

## 관련 항목

- [[사용자 주체 (User / Admin / Super Admin)]](../encyclopedia/subject-user-admin-superadmin.md)
- [[Admin]](./admin.md)
- [[Super Admin]](./super-admin.md)
- [[조직 (Organization)]](./organization.md)

---

## 작성자

{!author:kkooonsj}

