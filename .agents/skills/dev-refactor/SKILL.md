---
name: dev-refactor
description: Refactoring techniques, tech debt management, TDD workflow, branching strategy, DB migration
---

# Kỹ Năng: Refactoring & Tech Debt

---

## 1. Refactoring Techniques

> **Kích hoạt:** Code smells detected, cần cải thiện code quality.

**Common Refactoring Patterns:**
- **Extract Method:** Function quá dài → tách thành sub-functions
- **Rename:** Tên biến/function không rõ ràng → đổi tên có nghĩa
- **Move Method:** Method nằm sai class → move to appropriate class
- **Replace Conditional with Polymorphism:** if-else chain → Strategy/Factory pattern
- **Introduce Parameter Object:** Nhiều params → group vào 1 object

**Nguyên tắc:** Refactor = thay đổi structure, KHÔNG thay đổi behavior. Tests PHẢI pass trước và sau.

## 2. Technical Debt Tracker

**Debt Categories:**
| Category | Priority | Example |
|----------|----------|---------|
| **Reckless + Deliberate** | 🔴 Fix now | "Không có thời gian design" |
| **Prudent + Deliberate** | 🟡 Plan fix | "Ship now, refactor later" |
| **Reckless + Inadvertent** | 🟠 Fix soon | "Didn't know patterns" |
| **Prudent + Inadvertent** | 🟢 Monitor | "Now we know better" |

**Inventory:** Item | Category | Impact | Effort | Priority | Sprint target

## 3. TDD Workflow Guide

**Red → Green → Refactor:**
1. **Red:** Write failing test first
2. **Green:** Write minimum code to pass
3. **Refactor:** Clean up code, tests still pass

**When to TDD:** Complex business logic | Bug fix (write test that reproduces bug first) | API contracts

## 4. Branching Strategy Decision

| Strategy | Team size | Release cadence | Complexity |
|----------|-----------|----------------|------------|
| **Trunk-based** | Small (<5) | Continuous | Low |
| **GitHub Flow** | Medium (5-15) | Weekly | Medium |
| **GitFlow** | Large (>15) | Scheduled | High |

## 5. Database Migration Checklist

- [ ] Migration script tested on staging
- [ ] Rollback script prepared
- [ ] Data backup completed
- [ ] Zero-downtime migration possible?
- [ ] Index changes impact assessed
- [ ] Foreign key constraints handled
- [ ] Data migration (seed/transform) validated
