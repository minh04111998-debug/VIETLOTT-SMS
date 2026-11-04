# Mẫu Tài Liệu Nghiệp Vụ (BA)

> Tham chiếu từ: `.agents/skills/ba/SKILL.md` — Sections 2, 4, 5, 6, 19, 20, 21, 22, 23

---

## 1. Tạo SRS Document (Section 2)

### Bước 1: Xác định phạm vi
- Liệt kê tất cả module/chức năng
- Xác định ranh giới hệ thống (system boundary)
- Phân biệt In-scope vs Out-of-scope

### Bước 2: Viết Use Case chi tiết
Cho mỗi Use Case, viết đầy đủ:
- UC ID, Tên, Actor
- Mô tả, Precondition, Postcondition
- Main Flow (đánh số từng bước)
- Alternative Flow, Exception Flow
- Business Rules
- Interface Specification

### Bước 3: Xác định yêu cầu phi chức năng
- Hiệu năng: Response time < Xs, concurrent users
- Bảo mật: Authentication, Authorization, Encryption
- Khả dụng: Uptime SLA
- Tương thích: Browsers, devices, OS

### Bước 4: Review & Sign-off
- BA self-review → Technical review (DEV) → Stakeholder review → Baseline

---

## 2. Gap Analysis Template (Section 4)

```markdown
# Phân Tích Gap - [Tên chức năng]

## As-Is (Hiện tại)
### Quy trình hiện tại
[Mô tả quy trình với flowchart]

### Hạn chế hiện tại
1. [Hạn chế 1]
2. [Hạn chế 2]

## To-Be (Mong muốn)
### Quy trình mong muốn
[Mô tả quy trình mới với flowchart]

### Cải tiến
1. [Cải tiến 1]
2. [Cải tiến 2]

## Gap Matrix
| # | Khía cạnh | As-Is | To-Be | Gap | Giải pháp | Effort | Priority |
|---|----------|-------|-------|-----|-----------|--------|----------|

## Đề Xuất Lộ Trình
### Phase 1: [Quick wins]
### Phase 2: [Core changes]
### Phase 3: [Advanced features]
```

---

## 3. Data Dictionary (Section 5)

```markdown
## Bảng: [tên_bảng]

| # | Trường | Kiểu dữ liệu | Bắt buộc | Mặc định | Mô tả | Ràng buộc |
|---|--------|--------------|----------|----------|-------|-----------| 
| 1 | id | INT | Có | Auto | Mã định danh | PK, Auto Increment |
| 2 | name | VARCHAR(100) | Có | - | Tên | Unique |
| 3 | status | ENUM | Có | 'ACTIVE' | Trạng thái | IN ('ACTIVE','INACTIVE') |
| 4 | created_at | DATETIME | Có | NOW() | Ngày tạo | - |

### Mối quan hệ
- [tên_bảng].field → [bảng_khác].field (1-N)
```

---

## 4. Traceability Matrix (Section 6)

**PHẢI** duy trì truy vết từ yêu cầu đến implementation:

```markdown
| BR ID | FR ID | Use Case | User Story | Test Case | Status |
|-------|-------|----------|-----------|-----------|--------|
| BR-001 | FR-001 | UC-1.1 | US-001 | TC-001 | ✅ |
| BR-001 | FR-002 | UC-1.2 | US-002 | TC-002,003 | ✅ |
| BR-002 | FR-003 | UC-2.1 | US-003 | TC-004 | 🔄 |
```

---

## 5. NFR Analysis — FURPS+ Framework (Section 19)

```markdown
## Yêu Cầu Phi Chức Năng — [Module/System Name]

### Performance
| Metric | Requirement | Measurement Method |
|--------|------------|-------------------|
| Response Time (95th percentile) | < 2 giây | APM monitoring |
| Throughput | ≥ 500 requests/giây | Load test with JMeter |
| Concurrent Users | ≥ 200 users đồng thời | Stress test |

### Reliability
| Metric | Requirement | Measurement Method |
|--------|------------|-------------------|
| Uptime SLA | ≥ 99.5% | Monitoring dashboard |
| MTTR (Mean Time To Recovery) | < 30 phút | Incident log |
| Data Backup | Daily automated backup, RPO < 24h | Backup verification |

### Usability
| Metric | Requirement | Measurement Method |
|--------|------------|-------------------|
| Onboarding Time | < 5 phút cho user mới | User testing |
| Accessibility | WCAG 2.1 Level AA | Automated + manual audit |
| Mobile Responsive | iOS 14+, Android 10+ | Device testing matrix |

### Security
| Metric | Requirement | Measurement Method |
|--------|------------|-------------------|
| Authentication | MFA for admin, password policy | Security audit |
| Data Encryption | AES-256 at rest, TLS 1.3 in transit | Penetration test |
| Session Timeout | 30 phút inactive | Functional test |
| Audit Log | All admin actions logged | Log review |

### Supportability
| Metric | Requirement | Measurement Method |
|--------|------------|-------------------|
| Log Format | Structured JSON logging | Code review |
| Deployment | Zero-downtime deployment | Deployment verification |
| Configuration | Environment-based config | DevOps review |
```

---

## 6. Interface Specification (Section 20)

```markdown
## Interface: [System A] ↔ [System B]

**Loại interface:** API REST / SOAP / File Transfer / Message Queue / Webhook
**Hướng:** [A → B] / [B → A] / [Bidirectional]
**Tần suất:** Real-time / Batch (daily/hourly) / Event-driven
**Protocol:** HTTPS / SFTP / AMQP / gRPC

### Data Contract
| Field | Type | Required | Description | Validation |
|-------|------|---------|-------------|------------|
| id | string (UUID) | Yes | Unique identifier | Format: UUID v4 |
| amount | decimal(10,2) | Yes | Transaction amount | > 0, ≤ 999999999.99 |

### Error Handling
| Error Code | Meaning | Action |
|-----------|---------|--------|
| 400 | Invalid request | Show validation errors |
| 401 | Unauthorized | Redirect to login |
| 429 | Rate limited | Retry with exponential backoff |
| 500 | Server error | Log + alert ops + show friendly error |

### SLA
- Availability: [X]%
- Max Response Time: [X]ms
- Rate Limit: [X] requests/minute
- Retry Policy: [X] retries, [X]s backoff
```

---

## 6b. Exception Analysis Table (Bắt buộc — ba-rules §3.5)

> **Khi nào dùng:** Mỗi Use Case có gọi external system **PHẢI** kèm bảng này. BA **KHÔNG ĐƯỢC** submit SRS/User Story mà thiếu bảng Exception Analysis cho luồng tích hợp.

```markdown
### Exception Analysis — [Tên Use Case]

| # | Bước | Trigger | Exception Type | Hệ thống phản hồi (User thấy gì?) | Timeout | Retry Policy | Compensating Action |
|---|------|---------|---------------|-----------------------------------|---------|-------------|---------------------|
| E1 | [Bước N] | [Điều kiện gây exception] | Integration Error / Timeout / User Error / System Error / Hung State | [Message/behavior user nhận được] | [Xs/Xm] | [N lần, backoff Xs] | [Rollback/Cancel/Queue/Manual] |

### Ví dụ đã điền:

| # | Bước | Trigger | Exception Type | Hệ thống phản hồi | Timeout | Retry Policy | Compensating Action |
|---|------|---------|---------------|-------------------|---------|-------------|---------------------|
| E1 | Bước 3: Gọi API Bank nạp tiền | Bank trả HTTP 500 | Integration Error | "Giao dịch thất bại. Vui lòng thử lại sau." | 30s | 3 lần, backoff 5s/10s/20s | Rollback: hoàn HMDT về trạng thái trước |
| E2 | Bước 3: Gọi API Bank nạp tiền | Không nhận response | Timeout/Hung | GD chuyển "Đang xử lý" → push thông báo | 60s | Job reconciliation mỗi 5m | Auto-cancel sau 30m, hoàn HMDT |
| E3 | Bước 4: User xác nhận OTP | User không nhập OTP | User Timeout | "Phiên giao dịch hết hạn. Vui lòng thực hiện lại." | 3m | Không retry | Hủy GD pending, giải phóng lock HMDT |
| E4 | Bước 2: Kiểm tra HMDT | Số dư không đủ | Business Rule | "Số dư không đủ. Nạp thêm tiền?" + link nạp tiền | — | — | Không cần (chưa thay đổi state) |
| E5 | Bước 5: Ghi DB kết quả | DB connection pool exhausted | System Error | 503 → auto-retry ẩn → nếu fail: "Hệ thống đang bận" | 10s | 2 lần, backoff 3s | Queue request, xử lý khi DB available |
| E6 | Bước 3: Gọi API Bank | User double-tap nút Submit | Concurrency | Chỉ xử lý 1 request (idempotency key) | — | — | Reject duplicate, trả kết quả GD đầu tiên |
```

### Hướng dẫn điền:
1. **Bước:** Tham chiếu số bước trong Main Flow
2. **Exception Type:** Chọn từ: `Integration Error` | `Timeout/Hung` | `User Timeout` | `User Error` | `Business Rule` | `System Error` | `Concurrency` | `Data Integrity`
3. **Retry Policy:** Format: `[N] lần, backoff [strategy]` — strategy: fixed / linear / exponential
4. **Compensating Action:** Mô tả cách rollback hoặc khôi phục trạng thái nhất quán

> **Nguồn:** [Microsoft — Compensating Transaction Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction)

---

## 6c. Timeout & Hung State Checklist (Bắt buộc — ba-rules §3.6)

> **Khi nào dùng:** Cho MỖI bước gọi external system trong luồng nghiệp vụ. BA **PHẢI** điền checklist này.

```markdown
### ⏱️ Timeout & Hung State — [Tên Use Case]

| # | Bước gọi external | Q1: Timeout Value | Q2: Hung Detection | Q3: Post-Timeout State | Q4: Recovery Owner | Q5: User Notification | Q6: Idempotency | Q7: Reconciliation |
|---|-------------------|-------------------|-------------------|----------------------|-------------------|---------------------|-----------------|-------------------|
| 1 | [Bước N: Gọi API X] | [Xs] | [circuit breaker / polling / heartbeat] | [Cancelled / Pending / Retry] | [Auto-job / Manual / Escalation] | [Push / SMS / In-app / Không] | [Có: request ID / Không cần] | [Có: nằm trong file đối soát / Không] |

### Ví dụ đã điền — Luồng "Mua vé Mega 6/45":

| # | Bước gọi external | Q1: Timeout | Q2: Hung Detect | Q3: Post-Timeout | Q4: Recovery | Q5: Notify User | Q6: Idempotency | Q7: Reconciliation |
|---|-------------------|-------------|-----------------|-------------------|-------------|----------------|-----------------|-------------------|
| 1 | Bước 3: Gọi API VNPay thanh toán | 30s | Circuit breaker (Hystrix pattern) | Pending → Job check | Auto-job mỗi 5m, escalate sau 30m | Push: "GD đang xử lý" | Có: transaction_id | Có: file đối soát VNPay hàng ngày |
| 2 | Bước 4: Gửi vé lên Vietlott BGT | 60s | Polling mỗi 10s, max 6 lần | Pending → Manual review | Manual: Operator kiểm tra trên Admin | Push khi có KQ + SMS nếu > 15m | Có: ticket_request_id | Có: đối soát BGT mỗi kỳ |
| 3 | Bước 6: Callback kết quả về App | 15s | Heartbeat mỗi 5s | Retry → fallback pull | Auto-retry 3 lần | In-app: refresh để cập nhật | Không cần (read-only) | Không (không phải GD tài chính) |
```

> **Nguồn:**
> - [Microsoft — Circuit Breaker Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker)
> - [Microsoft — Retry Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry)
> - [AWS — Saga Pattern for Compensating Transactions](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/saga-pattern.html)

---

## 7. Scope Modeling — Context Diagram (Section 21)

```markdown
## Scope Definition: [Tên hệ thống]

### In Scope (Hệ thống SẼ làm)
- [Chức năng 1]
- [Chức năng 2]

### Out of Scope (Hệ thống KHÔNG làm)
- [Chức năng X] — Lý do: [do hệ thống khác handle / phase 2]

### External Systems (Cần tích hợp)
| System | Direction | Purpose |
|--------|-----------|---------| 

### Assumptions
1. [Giả định 1]

### Constraints
1. [Ràng buộc 1]
```

---

## 8. Business Glossary (Section 22)

```markdown
## Business Glossary — [Tên Dự Án]

| Thuật ngữ | Định nghĩa (Business) | Alias/Synonym | Không phải là | Ví dụ |
|-----------|----------------------|---------------|---------------|-------|
| Khách hàng | Người/tổ chức đã MUA sản phẩm (≥ 1 giao dịch) | Customer, Buyer | Không phải User (có thể chưa mua) | Công ty ABC đã mua gói Pro |
| Đơn hàng | Yêu cầu mua hàng đã được CONFIRM (có OrderID) | Order, Purchase | Không phải Giỏ hàng (chưa confirm) | Order #12345 |
```

**Nguyên tắc:**
- Glossary là **living document** — cập nhật khi phát hiện thuật ngữ mới
- Mỗi thuật ngữ có **1 định nghĩa duy nhất** (Single Source of Truth)
- Cột "Không phải là" rất quan trọng — prevent confusion
- Review glossary với stakeholder khi kickoff dự án

---

## 9. Requirements Lifecycle Management (Section 23)

```markdown
## Requirements Status — [Module/Sprint]

| Req ID | Title | Type | Priority | State | Owner | Last Updated |
|--------|-------|------|----------|-------|-------|-------------|
| FR-001 | Login OTP | Functional | Must | ✅ Approved | BA Minh | 10/06/2026 |
| FR-002 | Dashboard | Functional | Should | 🔄 In Review | BA Minh | 12/06/2026 |
| NFR-001 | Response < 2s | Performance | Must | 📝 Draft | BA Minh | 08/06/2026 |

### Traceability Matrix
| BR ID | FR IDs | UC/US IDs | Test Case IDs | Status |
|-------|--------|-----------|--------------|--------|

### Change Log
| Date | Req ID | Change Type | Description | Requested By | Impact |
|------|--------|-------------|-------------|-------------|--------|
```

---

## 10. RACI Matrix — BA Governance (BABOK KA1)

> Tham chiếu từ: `.agents/skills/ba/SKILL.md` — §30, `ba-rules.md` — §2.5

```markdown
## RACI Matrix — [Tên Dự Án/Module]

### Requirements Governance
| Hoạt động | BA | PO | SA | PM | DEV | QA |
|-----------|----|----|----|----|-----|-----|
| Viết requirement | R | C | C | I | I | I |
| Review requirement | A | C | R | I | R | R |
| Approve requirement | C | A | C | R | I | I |
| Thay đổi baselined req | R | A | C | A | I | I |
| Escalate conflict | R | C | C | A | I | I |

R = Responsible | A = Accountable | C = Consulted | I = Informed

### Approval Authority
| Loại Requirement | Approver | Escalation |
|-----------------|----------|------------|
| Business Req (BR) | PO / Sponsor | Sponsor |
| Functional Req (FR) | PO + SA | PM |
| Non-Functional (NFR) | SA + PM | CTO |
| Change Request (CR) | PM + PO | Sponsor |

### Escalation Path
BA → PM → PO → Sponsor
```

---

## 11. Roles & Permissions Matrix (BABOK Technique #39)

> Tham chiếu từ: `.agents/skills/ba/SKILL.md` — §33

```markdown
## Roles & Permissions — [Tên Module]

| Chức năng / Hành động | Admin | Manager | Staff | User | Guest |
|-----------------------|-------|---------|-------|------|-------|
| [Chức năng 1] | ✅ CRUD | ✅ CRU | ✅ R | ✅ R | ❌ |
| [Chức năng 2] | ✅ CRUD | ✅ CRU | ✅ CR | ❌ | ❌ |
| [Chức năng 3] | ✅ CRUD | ❌ | ❌ | ❌ | ❌ |

C = Create | R = Read | U = Update | D = Delete

### Quy tắc phân quyền đặc biệt
| Rule | Mô tả | Actor |
|------|--------|-------|
| [Rule 1] | [Mô tả chi tiết] | [Role] |
```

---

## 12. Lessons Learned — BA Retrospective (BABOK KA1)

> Tham chiếu từ: `.agents/skills/ba/SKILL.md` — §40, `babok-knowledge-areas.md` — KA1 §5

```markdown
## Lessons Learned — [Tên Dự Án/Release] — [DD/MM/YYYY]

### BA Process Metrics
| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| Requirements miss rate | [N] reqs missed post-baseline | < 5% | ✅/❌ |
| DEV/QA clarification requests | [N] questions | < 3 per story | ✅/❌ |
| Change rate post-baseline | [N]% | < 15% | ✅/❌ |
| Elicitation → SRS cycle time | [N] days | < [target] | ✅/❌ |
| Stakeholder satisfaction | [N]/5 | ≥ 4/5 | ✅/❌ |

### What Went Well
| # | Item | Impact |
|---|------|--------|
| 1 | [Mô tả] | [Positive impact] |

### What Didn't Go Well
| # | Item | Root Cause | Improvement Action | Owner |
|---|------|-----------|-------------------|-------|
| 1 | [Mô tả] | [Nguyên nhân] | [Cải thiện] | [Tên] |

### Technique Effectiveness
| Technique | Used for | Effective? | Keep/Drop/Modify |
|-----------|----------|-----------|-------------------|
| Interview | [Context] | ✅/❌ | Keep/Drop/Modify |
| Workshop | [Context] | ✅/❌ | Keep/Drop/Modify |

### Action Items for Next Project/Sprint
| # | Action | Owner | Deadline |
|---|--------|-------|----------|
```

---

## 13. Solution Options Comparison (BABOK KA5)

> Tham chiếu từ: `.agents/skills/ba/SKILL.md` — §30, `babok-knowledge-areas.md` — KA5 Define Design Options

```markdown
## Solution Options — [Tên Vấn Đề Nghiệp Vụ]

### Bối Cảnh
[Mô tả vấn đề cần giải quyết]

### So Sánh Options
| Tiêu chí | Option A: [Tên] | Option B: [Tên] | Option C: [Tên] |
|----------|-----------------|-----------------|-----------------|
| Mô tả | [Chi tiết] | [Chi tiết] | [Chi tiết] |
| Ưu điểm | [1. ... 2. ...] | [1. ... 2. ...] | [1. ... 2. ...] |
| Nhược điểm | [1. ... 2. ...] | [1. ... 2. ...] | [1. ... 2. ...] |
| Effort | [X man-days] | [Y man-days] | [Z man-days] |
| Risk | 🟢/🟡/🔴 | 🟢/🟡/🔴 | 🟢/🟡/🔴 |
| User impact | [Mô tả] | [Mô tả] | [Mô tả] |
| Integration | [Complexity] | [Complexity] | [Complexity] |

### Recommendation
**BA đề xuất:** Option [X]
**Rationale:** [Lý do dựa trên data, KHÔNG dựa trên opinion]
**Trade-offs accepted:** [Nhược điểm chấp nhận được]

### Decision
**Stakeholder chọn:** Option [X] / Cần thêm thông tin
**Ngày:** DD/MM/YYYY
**Ghi chú:** [Lý do stakeholder chọn]
```

