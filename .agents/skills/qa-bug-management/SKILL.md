---
name: qa-bug-management
description: Kỹ năng quản lý bug — bug report, triage, regression plan, security checklist, test monitoring
---

# Kỹ Năng: Bug Management & Regression

> **Nguồn gốc:** Tách từ QA monolith §6, §11-§13

---

## 1. Bug Report Chuẩn Mực

> **Kích hoạt:** Phát hiện bug, cần report rõ ràng.

**Template:**
```markdown
## Bug Report: [Tiêu đề ngắn gọn]
- **ID:** BUG-XXXX
- **Severity:** Critical / Major / Minor / Trivial
- **Priority:** P1 / P2 / P3 / P4
- **Environment:** [Browser, OS, Version]
- **Steps to Reproduce:** 1. ... 2. ... 3. ...
- **Expected Result:** ...
- **Actual Result:** ...
- **Screenshot/Video:** [Đính kèm]
- **Workaround:** [Nếu có]
```

**Severity vs Priority:**
| Severity | Priority | Ví dụ |
|----------|----------|-------|
| Critical + P1 | Hotfix ngay | Mất dữ liệu, crash production |
| Major + P2 | Fix trong sprint | Chức năng chính bị lỗi |
| Minor + P3 | Fix backlog | UI sai nhưng không block |
| Trivial + P4 | Nice to fix | Typo, cosmetic |

## 2. Security Testing Checklist

> **Kích hoạt:** Cần kiểm tra bảo mật cho module/release.

**OWASP Top 10 Check:**
- [ ] Injection (SQL, XSS, Command)
- [ ] Broken Authentication
- [ ] Sensitive Data Exposure
- [ ] XML External Entities (XXE)
- [ ] Broken Access Control
- [ ] Security Misconfiguration
- [ ] Cross-Site Scripting (XSS)
- [ ] Insecure Deserialization
- [ ] Using Components with Known Vulnerabilities
- [ ] Insufficient Logging & Monitoring

## 3. Regression Test Management

> **Kích hoạt:** Mỗi release/sprint cần chạy regression.

**Regression Suite Selection:**
- **Core regression:** Luôn chạy — luồng chính (mua vé, thanh toán, nạp tiền)
- **Impact-based:** Chạy thêm dựa trên Impact Analysis từ BA
- **Risk-based:** Ưu tiên areas có thay đổi code nhiều nhất

## 4. Test Monitoring Dashboard

> **Kích hoạt:** Cần theo dõi tiến độ test trong sprint/release.

**Metrics:**
| Metric | Mô tả | Target |
|--------|--------|--------|
| Test Execution Rate | % TC đã chạy / tổng TC | >95% |
| Pass Rate | % TC pass / đã chạy | >90% |
| Defect Density | Bugs / KLOC | <5 |
| Defect Leakage | Bugs found in UAT / total bugs | <10% |
| Test Coverage | % requirements có TC | 100% |
