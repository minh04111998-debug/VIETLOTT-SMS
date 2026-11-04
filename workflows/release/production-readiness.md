---
description: Quy trình kiểm tra sẵn sàng Production trước khi release - Vai trò PM (lead)
---

# Workflow: Production Readiness Check

> **Slash command**: `/production-readiness`
> **Vai trò**: `[⚪ ROLE: PM]` (lead) — BA, QA, DEV contribute
> **Khi nào dùng**: Trước mỗi lần release ra thị trường, dù là version mới, hotfix, hay MVP lần đầu
> **Đầu ra**: Production Readiness Checklist tại `artifacts/testing/production-readiness-[tên-version].md`

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo:** `[⚪ ROLE: PM]`
- **Nạp Rules:** Đọc ngầm `pm-rules.md` (primary) — tham chiếu `ba-rules.md`, `qa-rules.md`, `dev-rules.md` khi cần
- **Bản chất:** Workflow này là công cụ **kiểm soát rủi ro**, không phải thủ tục hành chính. Mỗi checkpoint đều có hậu quả thực tế nếu bỏ qua.
- **Dừng cứng:** Gặp ký hiệu 🛑 = BẮT BUỘC DỪNG, chờ người dùng

> [!WARNING]
> Bỏ qua bất kỳ giai đoạn nào bên dưới trước khi release là chấp nhận rủi ro có tính toán. AI PHẢI cảnh báo rõ ràng về hậu quả cụ thể của từng mục chưa hoàn thành.

---

## Bối Cảnh: Tại Sao Local Demo ≠ Production?

| Yếu tố | Local Demo | Production |
|--------|-----------|------------|
| Người dùng | 1-5 (nội bộ) | Hàng trăm → hàng ngàn |
| Dữ liệu | Giả, ít, clean | Thật, nhiều, không đoán trước |
| Uptime yêu cầu | Không quan trọng | 99.9% → 24/7 |
| Bảo mật | Không cần thiết | Bắt buộc |
| Lỗi gặp | Tự sửa được | Mất tiền, mất khách, mất uy tín |
| AI code quality | MVP, fast | Có thể có SQL Injection, no error handling |

---

## Các Bước Thực Hiện

### BƯỚC 1: Thu Thập Thông Tin Dự Án

AI hỏi người dùng **tối đa 5 câu**:
1. Tên dự án và version sắp release?
2. Loại release: MVP lần đầu / Feature mới / Hotfix / Nâng cấp lớn?
3. Ngày dự kiến go-live?
4. Đội ngũ thực hiện (DEV/QA/Infra/DevOps)?
5. Đã có môi trường Staging chưa? CI/CD Pipeline chưa?

🛑 **[DỪNG CỨNG]** — Chờ người dùng trả lời trước khi tạo checklist

---

### BƯỚC 2: Tạo Production Readiness Checklist

Dựa trên thông tin đã thu thập, sinh ra checklist theo 5 giai đoạn sau:

---

#### ⚙️ GIAI ĐOẠN 1: Code & Security Review

> **Rủi ro nếu bỏ qua:** Lỗ hổng bảo mật → rò rỉ dữ liệu khách hàng → phạt pháp lý, mất khách, headline báo.

| # | Hạng mục | Công cụ đề xuất | Người thực hiện | Status | Ghi chú |
|---|---------|----------------|----------------|--------|---------|
| 1.1 | **Code Review** bởi Senior Dev / Tech Lead | GitHub PR / GitLab MR | Tech Lead | ☐ | Tập trung: AI-generated code cần kiểm tra logic, pattern |
| 1.2 | **Static Analysis (SAST)** — Quét code smells, lỗi tiềm ẩn | SonarQube / ESLint | DEV | ☐ | Không được có Critical/Blocker issues |
| 1.3 | **Dependency Vulnerability Scan** — Thư viện lỗi thời | `npm audit` / Snyk / OWASP Dependency Check | DEV | ☐ | Vá hết HIGH/CRITICAL trước release |
| 1.4 | **Dynamic Scan (DAST)** — Quét lỗ hổng runtime | OWASP ZAP / Burp Suite | QA/Security | ☐ | Bắt buộc với app xử lý dữ liệu KH |
| 1.5 | **Secret Scan** — Không có key/password trong code | git-secrets / TruffleHog | DEV | ☐ | Check cả git history |
| 1.6 | **SQL Injection Test** — Kiểm tra parameterized queries | Manual test + DAST | QA | ☐ | AI code thường dùng string concat |

---

#### 🧪 GIAI ĐOẠN 2: Testing & QA

> **Rủi ro nếu bỏ qua:** Bug sản xuất → khách hàng bực bội → churn → review 1 sao.

| # | Hạng mục | Công cụ đề xuất | Người thực hiện | Status | Ghi chú |
|---|---------|----------------|----------------|--------|---------|
| 2.1 | **Unit Tests** pass 100% | Jest / JUnit / Pytest | DEV | ☐ | Coverage ≥ 80% |
| 2.2 | **Integration Tests** pass | Postman / REST Assured | DEV/QA | ☐ | Test API end-to-end |
| 2.3 | **Performance / Load Test** — Giả lập tải thực tế | K6 / JMeter / Locust | QA/DevOps | ☐ | Target: [X] concurrent users, <[Y]ms response |
| 2.4 | **UAT** — Đối chiếu với BDD/SRS, người dùng thực thao tác | Manual | BA + End User | ☐ | Xem `artifacts/testing/test-cases-*.md` |
| 2.5 | **Regression Test** — Tính năng cũ không bị vỡ | Automated suite | QA | ☐ | Chạy full suite trước release |
| 2.6 | **Cross-browser Test** — Chrome, Firefox, Safari, Edge | BrowserStack / Manual | QA | ☐ | |
| 2.7 | **Mobile Responsive Test** | DevTools / Real device | QA | ☐ | iOS + Android |
| 2.8 | **Accessibility Test (WCAG 2.2 AA)** | axe / Lighthouse | QA | ☐ | Xem `references/owasp-top-10.md` Phần 3 |

---

#### 🏗️ GIAI ĐOẠN 3: Infrastructure & CI/CD

> **Rủi ro nếu bỏ qua:** Server sập giờ cao điểm, deploy tay nhầm file, không rollback được.

| # | Hạng mục | Công cụ đề xuất | Người thực hiện | Status | Ghi chú |
|---|---------|----------------|----------------|--------|---------|
| 3.1 | **3 môi trường** tách biệt: DEV / STAGING / PRODUCTION | Cloud / VPS | DevOps | ☐ | STAGING phải mirror PRODUCTION |
| 3.2 | **CI/CD Pipeline** hoạt động: Build → Test → Deploy tự động | GitHub Actions / GitLab CI / Jenkins | DevOps | ☐ | Không deploy tay lên PROD |
| 3.3 | **Database Migration** — Script up + rollback | Flyway / Liquibase / custom | DEV | ☐ | Test migration trên STAGING trước |
| 3.4 | **DB Backup** — Tự động, lịch định kỳ | Cron + mysqldump / pg_dump | DevOps | ☐ | Có policy restore tested |
| 3.5 | **Environment Variables** — Không hardcode | `.env` / Secret Manager / Vault | DEV | ☐ | Mỗi môi trường có config riêng |
| 3.6 | **SSL/TLS Certificate** — HTTPS bắt buộc | Let's Encrypt / Cert Manager | DevOps | ☐ | Cấu hình auto-renew |
| 3.7 | **Auto-scaling** / Resource limits | K8s HPA / Cloud Auto-scale | DevOps | ☐ | Quan trọng với traffic fluctuation |

---

#### 📡 GIAI ĐOẠN 4: Monitoring & Observability

> **Rủi ro nếu bỏ qua:** Lỗi xảy ra mà không biết, chờ khách hàng phản ánh mới hay → quá muộn.

| # | Hạng mục | Công cụ đề xuất | Người thực hiện | Status | Ghi chú |
|---|---------|----------------|----------------|--------|---------|
| 4.1 | **Error Tracking** — Alert ngay khi có exception | Sentry / Rollbar | DEV | ☐ | Setup trước go-live |
| 4.2 | **APM** — Theo dõi response time, throughput, tài nguyên | Datadog / New Relic / Prometheus+Grafana | DevOps | ☐ | Đặt alert ngưỡng cụ thể |
| 4.3 | **Log Management** — Tập trung, tìm kiếm được | ELK Stack / Loki / CloudWatch | DevOps | ☐ | Log đủ context (user, timestamp, input) |
| 4.4 | **Uptime Monitoring** — Alert khi site down | UptimeRobot / Pingdom | DevOps | ☐ | Notify qua Slack/Email/SMS |
| 4.5 | **User Analytics** — Hành vi người dùng thực tế | Google Analytics / Mixpanel / PostHog | BA/Product | ☐ | Track conversion funnel, feature adoption |
| 4.6 | **Business KPI Dashboard** — Báo cáo cho stakeholders | Metabase / PowerBI / Grafana | BA/PM | ☐ | Map với KPI đã cam kết trong BRD |

---

#### 🚀 GIAI ĐOẠN 5: Release Management

> **Rủi ro nếu bỏ qua:** Không rollback được khi sự cố, 100% user bị ảnh hưởng thay vì 5%.

| # | Hạng mục | Người thực hiện | Status | Ghi chú |
|---|---------|----------------|--------|---------|
| 5.1 | **Release Notes** — Dành cho khách hàng | BA/PM | ☐ | Ngôn ngữ nghiệp vụ, không kỹ thuật |
| 5.2 | **User Manual / Hướng dẫn vận hành** | BA | ☐ | Cho đội CSKH, Sale, Operation |
| 5.3 | **Phased Rollout plan** — Không bật 100% ngay | PM/DevOps | ☐ | 5% → 25% → 50% → 100% với tiêu chí rõ ràng |
| 5.4 | **Roll-back Procedure** — Quy trình lùi về phiên bản cũ | DevOps | ☐ | Mục tiêu: ≤ 5 phút, zero-downtime |
| 5.5 | **Go/No-Go Meeting** — Cuộc họp chốt quyết định | PM + Tech Lead + QA | ☐ | Tất cả Critical checklist phải xanh |
| 5.6 | **Communication Plan** — Thông báo trước cho users (nếu có downtime) | PM/Marketing | ☐ | Báo trước ≥ 24h nếu maintenance |
| 5.7 | **War Room** — Ai on-call trong 24h đầu? | PM + DEV + DevOps | ☐ | Nhóm Zalo/Slack sẵn sàng |

---

### BƯỚC 3: Đánh Giá Tổng Thể & Đề Xuất Go/No-Go

Sau khi điền checklist, AI tổng kết:

```markdown
## Tóm tắt Production Readiness — [Tên dự án] v[X.Y]

| Giai đoạn | Hoàn thành | Tổng | Tỷ lệ |
|-----------|-----------|-------|-------|
| G1: Security | X | 6 | X% |
| G2: Testing | X | 8 | X% |
| G3: Infra | X | 7 | X% |
| G4: Monitoring | X | 6 | X% |
| G5: Release | X | 7 | X% |
| **TỔNG** | **X** | **34** | **X%** |

### 🟢 RECOMMENDED GO / 🔴 NO-GO: [Kết luận]
**Lý do:** [Giải thích cụ thể]
**Rủi ro còn mở:** [Danh sách các item chưa xanh và tác động]
**Điều kiện để GO:** [Các item tối thiểu cần hoàn thành trước]
```

🛑 **[DỪNG CỨNG]** — Trình bày tóm tắt, chờ xác nhận từ PM/Tech Lead

---

### BƯỚC 4: Lưu Trữ

- Lưu **nháp** tại `artifacts/testing/production-readiness-[tên]-v[version].md`
- Sau khi Go-Live thành công → chuyển sang `artifacts/testing/production-readiness-[tên]-v[version].md`
- Bổ sung vào Change Log của dự án

---

## 💡 AI-Project DoD — Definition of Done (Mở Rộng)

> Khi làm việc với AI-generated code, DoD truyền thống ("code chạy đúng trên máy Dev") là **KHÔNG ĐỦ**.

### DoD Chuẩn Cho AI-Assisted Projects

```markdown
## Definition of Done — [Tên Feature/Sprint]

### ✅ Functional
- [ ] Tất cả Acceptance Criteria trong User Story đã pass
- [ ] Tất cả BDD scenarios (Given/When/Then) đã được kiểm thử

### ✅ Code Quality
- [ ] Code review bởi ≥ 1 Senior Dev
- [ ] SonarQube: không có Critical/Blocker issue
- [ ] Test coverage ≥ 80%
- [ ] Không có hardcoded secrets

### ✅ Security
- [ ] SAST scan: clean
- [ ] SQL Injection test: pass
- [ ] Input validation: có đủ

### ✅ Performance
- [ ] Load test với [X] users concurrent: response < [Y]ms
- [ ] Không có N+1 query issues

### ✅ Operability
- [ ] Sentry error tracking: đã cài và test
- [ ] Logging đủ context
- [ ] Health check endpoint: hoạt động
- [ ] Rollback script: có và test OK

### ✅ Documentation
- [ ] README cập nhật
- [ ] API docs cập nhật (nếu có thay đổi API)
- [ ] Release notes viết xong
```

---

## Cross-References (Phase 2 additions)

> [!NOTE]
> **Liên kết Quality Gate (pm-rules.md §8):**
> - Production Readiness Check là **superset** của Quality Gate. Trước khi chạy `/production-readiness`, nên chạy `/pm quality` (SKILL.md Skill 14) để có Quality Gate Assessment sẵn.
> - Quality Gate criteria (test coverage, bugs, security, performance, code review, docs) map trực tiếp vào Giai đoạn 1 (Security) và Giai đoạn 2 (Testing) của Production Readiness Checklist.
> - Nếu Quality Gate = 🔴 FAIL → **KHÔNG** nên tiến hành Production Readiness Check. Fix issues trước.
