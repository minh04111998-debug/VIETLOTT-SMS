---
name: qa-test-plan
description: Kỹ năng lập kế hoạch kiểm thử, thiết kế test cases, test data management, performance test plan
---

# Kỹ Năng: Test Plan & Design

> **Nguồn gốc:** Tách từ QA monolith §1-§4, §9-§10, §14-§15

---

## 1. Tạo Test Plan

> **Kích hoạt:** Bắt đầu test cho module/release mới.

**Cấu trúc:** Scope → Test Approach → Entry/Exit Criteria → Test Schedule → Resource → Risk → Deliverables
**Test Levels:** Unit → Integration → System → UAT
**Estimation:** Dùng test point analysis hoặc % of dev effort (30-50%)

## 2. Viết Test Cases Chi Tiết

> **Kích hoạt:** Cần chi tiết test cases từ test plan.

**Format:** ID | Tiêu đề | Precondition | Steps | Expected Result | Actual Result | Status
**Kỹ thuật:** Equivalence Partitioning | Boundary Value | Decision Table | State Transition | Error Guessing

## 3. Test Data Management

> **Kích hoạt:** Cần chuẩn bị dữ liệu test cho từng scenario.

**Nguyên tắc:** Realistic data | Edge cases covered | PII anonymized | Reproducible | Version controlled

## 4. Performance Testing Plan

> **Kích hoạt:** Cần test hiệu năng (load, stress, spike, endurance).

**Template:** Test Objectives → Workload Model → Test Environment → Performance Metrics → Acceptance Criteria → Tools

## 5. API Testing Template

> **Kích hoạt:** Cần kiểm thử API endpoints.

**Coverage:** Happy path | Error codes (4xx, 5xx) | Validation | Auth/Auth | Pagination | Rate limiting

## 6. Static Testing / Review Facilitation

> **Kích hoạt:** Review tài liệu (SRS, Design) trước khi test.

**4 Types:** Informal Review | Walkthrough | Technical Review | Inspection
**QA Focus:** Testability, completeness, consistency, ambiguity

## 7. Agile Testing Quadrants Guide

```
        Business-Facing
    ┌───────────┬───────────┐
    │  Q2       │  Q3       │
    │ Functional│ Exploratory│
    │ User Story│ Usability  │
    │ Prototype │ UAT        │
    ├───────────┼───────────┤
    │  Q1       │  Q4       │
    │ Unit Tests│ Performance│
    │ Component │ Security   │
    │ API Tests │ Load       │
    └───────────┴───────────┘
        Technology-Facing
    ← Support Team    Critique Product →
```
