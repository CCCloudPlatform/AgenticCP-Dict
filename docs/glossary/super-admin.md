---
title: Super Admin
tags:
  - super-admin
  - core-domain
---

## 한 줄 정의

AgenticCP 전체를 관할하며, **모든 조직/테넌트와 전역 리소스·설정을 조정할 수 있는 최상위 플랫폼 관리자**.

## 상세 설명

- 일반적으로 `ROLE_SUPER_ADMIN` 또는 이에 상응하는 전역 관리자 역할로 표현된다.  
- 모든 테넌트의 생성/승인/일시정지/종료, 전역 보안 정책, 기능 플래그, 플랫폼 Config,  
  멀티 클라우드 통합 설정 등 **플랫폼 레벨의 운영과 보안**을 책임진다.
- 잘못된 조작이 전체 서비스에 영향을 줄 수 있으므로,  
  MFA, IP 제한, 강력한 감사 로깅 등 **강화된 통제 하에서만 부여되어야 하는 역할**이다.

## 관련 항목

- [[사용자 주체 (User / Admin / Super Admin)]](../encyclopedia/subject-user-admin-superadmin.md)
- [[User]](./user.md)
- [[Admin]](./admin.md)
- [[테넌트와 조직 (Tenant & Organization)]](../encyclopedia/tenant-and-organization.md)

---

## 작성자

{!author:kkooonsj}

