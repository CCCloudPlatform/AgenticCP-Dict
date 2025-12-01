---
title: 테넌트 (Tenant)
tags:
  - tenant
  - core-domain
---

## 한 줄 정의

AgenticCP에서 **하나의 조직에 대응되는 클라우드 리소스의 논리적 집합체(컨테이너)**.

## 상세 설명

- 멀티 테넌트 아키텍처에서 각 테넌트는 **서로 격리된 리소스·데이터·정책 단위**를 의미한다.  
- 이 프로젝트에서는 **1 조직 = 1 테넌트** 규칙을 사용하여,  
  “조직이 사용하는 모든 클라우드 리소스는 해당 조직의 테넌트에 속한다”는 전제를 둔다.
- 보안 정책, 비용 한도, 기능 플래그, 플랫폼 설정 등은 기본적으로 **테넌트 단위로 관리**된다.

## 관련 항목

- [[테넌트와 조직 (Tenant & Organization)]](../encyclopedia/tenant-and-organization.md)
- [[조직 (Organization)]](./organization.md)

---

## 작성자

{!author:kkooonsj}

