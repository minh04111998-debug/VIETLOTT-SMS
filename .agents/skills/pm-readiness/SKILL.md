---
name: pm-readiness
description: Production readiness checklist, project closing, quality gate assessment, release planning
---

# Kỹ Năng: Release Readiness & Project Closure

---

## 1. Production Readiness Checklist

> **Kích hoạt:** Trước mỗi release lên production.

**Categories:**
- [ ] Code: All PRs merged, no critical bugs, code freeze
- [ ] Testing: Regression passed, UAT signed off, perf test OK
- [ ] Documentation: Release notes, API docs, user guide updated
- [ ] Infrastructure: Monitoring configured, alerts set, rollback plan ready
- [ ] Business: Stakeholder notified, training completed, support briefed

## 2. Release Planning

**Template:** Release scope → Schedule → Dependencies → Risks → Rollback Plan
**Release Types:** Big Bang | Phased | Canary | Blue-Green | Feature Toggle

## 3. Quality Gate Assessment

> **Kích hoạt:** Chuyển phase (Dev→QA, QA→UAT, UAT→Prod).

| Gate | Criteria | Status |
|------|----------|--------|
| Code Complete | All stories coded + unit tested | ✅/❌ |
| Test Complete | TC pass rate >95%, no P1/P2 bugs | ✅/❌ |
| UAT Approved | PO/Stakeholder sign-off | ✅/❌ |
| Prod Ready | Infra, monitoring, rollback confirmed | ✅/❌ |

## 4. Project Closure Checklist

- [ ] All deliverables accepted by stakeholder
- [ ] Lessons learned documented
- [ ] Project artifacts archived
- [ ] Team performance review
- [ ] Budget reconciliation
- [ ] Stakeholder satisfaction survey
- [ ] Knowledge transfer completed
