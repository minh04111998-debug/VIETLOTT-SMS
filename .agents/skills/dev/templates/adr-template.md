# ADR & Architecture Templates (DEV)

> Tham chiếu từ: `.agents/skills/dev/SKILL.md` — Sections SA-01, SA-02, SA-03, SA-04

---

## 1. Context Analysis — 7 Câu Hỏi Bắt Buộc (SA-01)

| # | Câu hỏi | Tại sao quan trọng |
|---|---------|-------------------|
| 1 | Số người dùng dự kiến: 6 tháng / 1 năm / 3 năm? | Quyết định cần scale dọc hay ngang |
| 2 | Traffic pattern: đều hay spike (VD: 9-17h cao điểm, đêm thấp)? | Quyết định cần Auto-scaling không |
| 3 | Team: bao nhiêu người? Junior/Mid/Senior ratio? | Kiến trúc phức tạp cần team mature |
| 4 | Timeline go-live? Có hard deadline không? | Monolith ship nhanh hơn Microservices nhiều tuần |
| 5 | Budget hạ tầng hàng tháng (VND/USD)? | K8s cluster ≠ budget nhỏ |
| 6 | SLA: có thể downtime không? Bao lâu? | Quyết định cần HA/failover không |
| 7 | Tích hợp hệ thống legacy/3rd party nào quan trọng? | Có thể ảnh hưởng lớn đến kiến trúc |

**Output:** Bảng Context Summary — căn cứ để chọn kiến trúc ở SA-02.

---

## 2. Bảng So Sánh Kiến Trúc (SA-02)

### Kiến Trúc Tổng Thể

| Kiến trúc | Phù hợp khi | Không phù hợp khi | Complexity |
|----------|-------------|-------------------|-----------| 
| **Monolith** | Team ≤5, MVP, deadline gấp, budget thấp | Traffic cực lớn, team 10+ người | 🟢 Thấp |
| **Modular Monolith** | Team 5-10, SRS rõ, growth stage | Team rất nhỏ (over-engineering) | 🟡 Trung bình |
| **Microservices** | Team ≥10, SLA cao, domain rõ, DevOps mature | Startup, deadline ngắn, team nhỏ | 🔴 Cao |
| **Serverless** | Event-driven, traffic spike, cost per use | Latency-sensitive, long-running | 🟡 Trung bình |
| **Event-Driven** | Audit trail quan trọng, async workflow | Simple CRUD, team chưa quen async | 🔴 Cao |
| **BFF** | Multi-platform (web + mobile khác UX) | Single client, team nhỏ | 🟡 Trung bình |

### Tech Stack Trade-off

| Quyết định | Lựa chọn A | Lựa chọn B | Chọn A khi | Chọn B khi |
|-----------|-----------|-----------|-----------|-----------| 
| Database | PostgreSQL/MySQL | MongoDB | Cần ACID, JOIN phức tạp | Schema flexible, rapid prototype |
| API Style | REST | GraphQL | Public API, caching quan trọng | Mobile-first, client cần flexible query |
| Realtime | Polling | WebSocket | Data ít thay đổi | Chat, live dashboard |
| Queue | Không cần | RabbitMQ/Kafka | CRUD synchronous ổn | Async required, decoupling cần |
| Deployment | VPS + PM2 | Docker + K8s | Small scale, budget thấp | Large scale, microservices |

### Template Bảng So Sánh (Output Format)

```markdown
| Tiêu chí | PA1: [Tên] | PA2: [Tên] | PA3: [Tên] |
|---------|-----------|-----------|-----------| 
| Time-to-market | 🟢 2 tuần | 🟡 4 tuần | 🔴 8 tuần |
| Chi phí vận hành | 🟢 ~2M/tháng | 🟡 ~8M/tháng | 🔴 ~25M/tháng |
| Khả năng Scale | 🟡 Vertical | 🟢 Horizontal | 🟢 Horizontal |
| Yêu cầu DevOps | 🟢 Thấp | 🟡 Trung bình | 🔴 Cao |
| Phù hợp team hiện tại | 🟢 Có | 🟡 Cần training | 🔴 Không |
| Long-term flexibility | 🟡 Trung bình | 🟢 Tốt | 🟢 Tốt |

**→ ĐỀ XUẤT: PA[X]** vì [lý do cụ thể dựa trên bối cảnh]
**Con đường tiến hóa:** PA1 → [điều kiện] → PA2 → [điều kiện] → PA3
```

🛑 **[Hard Stop]** — Trình bày, chờ duyệt.

---

## 3. Architecture Decision Record — ADR (SA-03)

```markdown
# ADR-[NNN]: [Tiêu đề quyết định]

**Ngày:** DD/MM/YYYY | **Trạng thái:** Accepted
**Người quyết định:** [Tên] | **Người liên quan:** [PM, BA, Tech Lead]

## Bối Cảnh
[Context Summary từ SA-01: scale, team, timeline, budget...]

## Quyết Định
Chúng tôi sử dụng **[Kiến trúc/Công nghệ X]** vì [lý do cụ thể].

## Phương Án Đã Xem Xét
| Phương án | Lý do không chọn |
|----------|-----------------| 
| [PA2] | [Lý do cụ thể] |
| [PA3] | [Lý do cụ thể] |

## Hậu Quả
**Tích cực:** [Lợi ích cụ thể]
**Tiêu cực / Rủi ro:** [Rủi ro] → Giảm thiểu bằng [cách gì]

## Khi Nào Review Lại
Khi [điều kiện] xảy ra. Ví dụ: "Khi MAU vượt 50,000 → xem xét tách sang Modular Monolith"
```

Lưu tại: `artifacts/decisions/adr-[NNN]-[tên-kebab].md`

---

## 4. Tech Design Plan (SA-04)

Sau khi ADR được duyệt, xuất Tech Design Plan:

1. **Architecture Diagram (Mermaid):** Context → Component → Sequence
2. **Database Changes:** Schema mới/sửa, migration script, rollback script
3. **API Contracts:**
   ```
   | Method | Endpoint | Mô tả | Request | Response | Auth |
   |--------|----------|-------|---------|----------|------|
   ```
4. **Files to Create/Modify:** Danh sách cụ thể từng file
5. **Dependencies:** Thư viện mới cần cài — **PHẢI hỏi approve trước khi cài**
6. **Estimated Effort:** Man-days per task

🛑 **[Hard Stop]** — Chờ duyệt Tech Design Plan → Mới được code.
