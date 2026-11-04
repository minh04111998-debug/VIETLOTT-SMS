---
name: dev
description: Kỹ năng phát triển phần mềm, code review và thiết kế kỹ thuật
---

# Kỹ Năng: DEV Coding (Core Index)

## Mô Tả
Skill gốc cho vai trò Developer. File này là **dispatch table**.

---

## Skill Dispatch Table

| Khi task liên quan đến... | Nạp skill | Mô tả |
|--------------------------|-----------|-------|
| Code review, PR workflow, review checklist | `dev-review` | Code Review & PR |
| Refactoring, tech debt, TDD, branching strategy | `dev-refactor` | Refactoring & Tech Debt |

---

## Core DEV Skills (luôn có sẵn)

### 1. Thiết Kế API (RESTful)
**Convention:** `GET /resources`, `POST /resources`, `PUT /resources/:id`, `DELETE /resources/:id`
**Response:** Consistent JSON envelope: `{ success, data, error, meta }`
**Versioning:** URL-based (`/api/v1/`) hoặc Header-based

### 2. Database Design
**Normalization:** 3NF minimum cho OLTP
**Naming:** snake_case, plural table names, `_id` suffix for FK
**Index:** Primary key auto | Foreign keys | Frequently queried columns

### 3. Technical Documentation
**README.md:** Mô tả | Tech Stack | Cài đặt | Chạy project | Cấu trúc thư mục | API docs | Contributing

### 4. Solution Design & Tech Design
**ADR Format:** Context → Decision → Status → Consequences
**Tech Design Doc:** Problem → Options → Decision → Implementation Plan → Risks

### 5. Production-Grade Code Scaffolding
**Checklist:** Error handling | Logging | Config management | Health check | Graceful shutdown

### 6. Performance & Scalability Patterns
**Patterns:** Caching (Redis) | Connection pooling | Pagination | Lazy loading | CDN
**Monitoring:** APM (response time, error rate, throughput)

### 7. Feature Flag Strategy
**Types:** Release flag | Experiment flag | Permission flag | Ops flag
**Cleanup:** Remove flags after full rollout (max 30 days)
