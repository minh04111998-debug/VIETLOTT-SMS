# PM Examples — Practical References

---

## Example 1: Risk Register

```markdown
## Risk Register — VIETLOTT-SMS Project

### Risk Heat Map
|  | Low Impact | Medium Impact | High Impact |
|--|-----------|--------------|------------|
| **High Prob** | 🟡 R-005 | 🟠 R-003 | 🔴 R-001 |
| **Medium Prob** | 🟢 R-006 | 🟡 R-004 | 🟠 R-002 |
| **Low Prob** | 🟢 R-007 | 🟢 R-008 | 🟡 R-009 |

### Active Risks
| ID | Risk | Prob | Impact | Score | Strategy | Owner | Status |
|----|------|------|--------|-------|----------|-------|--------|
| R-001 | SMS gateway rate limit ảnh hưởng performance | High | High | 9 | Mitigate: Implement queue + retry logic | DevOps | 🟠 Active |
| R-002 | Vietlott API thay đổi format response | Medium | High | 6 | Transfer: Tạo adapter layer + monitor | DEV | 🟡 Monitoring |
| R-003 | Team member nghỉ giữa sprint (1 FE dev) | High | Medium | 6 | Accept: Cross-train, buffer 20% capacity | PM | 🟢 Planned |
| R-004 | Compliance requirement từ telco | Medium | Medium | 4 | Avoid: Pre-check regulation trước khi build | BA | 🟢 Planned |

### Closed/Resolved Risks
| ID | Risk | Resolution | Closed Date |
|----|------|-----------|-------------|
| R-010 | Server hosting chưa quyết định | Đã chọn AWS ap-southeast-1 (ADR-002) | 15/04/2025 |
```

---

## Example 2: Weekly Status Report

```markdown
# Weekly Status Report — VIETLOTT-SMS — Week 12 (17/06/2025)

## Overall Status: 🟡 At Risk

### Reason: QA resource bị reduce 50% do teammate sick.

---

### Accomplishments This Week
- ✅ SMS sending core module — code complete + unit tests (DEV)
- ✅ Vietlott API integration — adapter pattern implemented (DEV)
- ✅ Admin dashboard wireframes — approved by PO (Designer)
- ✅ SRS-Auth module — baseline v1.2 (BA)

### Planned Next Week
- 📋 QA: Start test SMS module (nếu resource available)
- 📋 DEV: Begin admin dashboard frontend
- 📋 BA: SRS-Order module kickoff
- 📋 DevOps: CI/CD pipeline setup for staging

### Risks & Issues
| # | Type | Description | Severity | Owner | Action |
|---|------|------------|----------|-------|--------|
| 1 | 🔴 Issue | QA resource 50% — delay testing 3 days | High | PM | Extend sprint 2 days OR de-scope 1 story |
| 2 | 🟡 Risk | SMS gateway sandbox rate limit = 10 req/min | Medium | DevOps | Request production API key sớm hơn |
| 3 | 🟢 Risk | Figma license expiry 30/06 | Low | PM | Renew trước 25/06 |

### Decisions Needed from Stakeholder
| # | Decision | Deadline | Impact if Delayed |
|---|----------|----------|-------------------|
| 1 | Extend sprint hoặc de-scope story SC-015? | 19/06 | Sprint failure risk |
| 2 | Budget approval for SMS gateway production tier | 20/06 | Block staging testing |

### Metrics Dashboard
| Metric | This Week | Last Week | Trend |
|--------|-----------|-----------|-------|
| Sprint velocity | 28 SP | 32 SP | 📉 -12.5% |
| Open bugs | 3 | 1 | 📈 +2 |
| Budget spent | 42% | 38% | → On track |
| Stories completed | 5/8 | 7/8 | 📉 |
```
