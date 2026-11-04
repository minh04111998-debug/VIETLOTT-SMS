---
name: dev-review
description: Code review chi tiết, PR workflow, review checklist, coding standards
---

# Kỹ Năng: Code Review & PR Workflow

---

## 1. Code Review Chi Tiết

> **Kích hoạt:** Review PR hoặc code trước khi merge.

**Review Dimensions:**
| Dimension | Check |
|-----------|-------|
| **Correctness** | Logic đúng? Edge cases handled? |
| **Security** | Input validation? SQL injection? XSS? Auth check? |
| **Performance** | N+1 queries? Unnecessary loops? Memory leaks? |
| **Readability** | Naming clear? Comments useful? Function length <50 lines? |
| **Maintainability** | DRY? Single Responsibility? Easy to extend? |
| **Testing** | Unit tests added? Coverage maintained? |

**PR Checklist:**
- [ ] Meaningful PR title + description
- [ ] Tests pass (CI green)
- [ ] No console.log / debug code
- [ ] No secrets/credentials committed
- [ ] Migration script included (if DB change)
- [ ] Breaking changes documented

## 2. Coding Standards

**Naming:** camelCase (JS/TS), snake_case (Python), PascalCase (classes/components)
**Comments:** WHY not WHAT. Code should be self-documenting.
**Error Handling:** Never swallow errors. Log + re-throw or handle gracefully.
