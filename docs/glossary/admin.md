---
title: Admin
tags:
  - admin
  - core-domain
---

## 한 줄 정의

특정 조직(=테넌트) 내에서 **사용자, 리소스, 일부 정책·설정을 관리하는 책임을 가진 관리자**.

## 상세 설명

- 보통 `ROLE_ADMIN` 또는 이에 상응하는 역할로 표현되며,  
  자신이 관리하는 조직(=테넌트)의 User 계정과 리소스, 일부 정책을 관리한다.
- 사용자 생성/초대/비활성화, 역할·권한 부여/회수,  
  테넌트 수준의 보안/비용/기능 플래그 설정 조정 등의 작업을 수행한다.
- 다른 조직/테넌트나 플랫폼 전역(Global) 설정에는 권한을 가지지 않는 것이 기본 전제다.

!!! tip "기본 설정"
    **조직을 생성한 사용자는 기본적으로 해당 조직의 Admin 역할을 자동으로 부여받는다.**  
    이후 Super Admin이 필요에 따라 다른 사용자에게도 Admin 역할을 부여하거나 변경할 수 있다.

## 관련 항목

- [[사용자 주체 (User / Admin / Super Admin)]](../encyclopedia/subject-user-admin-superadmin.md)
- [[User]](./user.md)
- [[Super Admin]](./super-admin.md)
- [[조직 (Organization)]](./organization.md)

---

## 작성자

{!author:kkooonsj}

