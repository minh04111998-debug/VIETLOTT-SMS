# ⚙️ Project Conventions — Shared Conventions

> Quy ước dùng chung cho toàn bộ dự án. Mọi role đều phải tuân thủ.
> Khi thay đổi convention → update file này trước → notify team.

---

## 1. File & Folder Naming

| Loại | Convention | Ví dụ |
|------|-----------|-------|
| Tài liệu Markdown | `kebab-case.md` | `prd-feature-otp.md`, `srs-payment-module.md` |
| ADR files | `adr-[NNN]-[tên-kebab].md` | `adr-001-chon-kien-truc-monolith.md` |
| Thư mục | `kebab-case` | `artifacts/`, `workflows/` |
| Files code | Theo convention của ngôn ngữ | Python: `snake_case.py`, JS: `camelCase.js` |

---

## 2. Folder Structure — Dự Án (20-Node Architecture)

Chi tiết cấu trúc xem tại `ARCHITECTURE.md`. Phân bổ chính:

- `artifacts/` — Kết quả bàn giao chính thức (product, requirements, analysis, technical, testing, decisions)
- `knowledge/` — Tri thức tĩnh & quy tắc nghiệp vụ (domain, product, glossary, business-rules)
- `references/` — Khung tham chiếu chuẩn quốc tế (BABOK, CPOA, ISTQB, OWASP)
- `workflows/` — 6 Value Streams quy trình (product-discovery, requirement, feature-dev, bug-fix, data-analysis, release)
- `templates/` — Biểu mẫu chuẩn (Golden Templates)
- `plans/` — Kế hoạch (active, completed, tech-debt)
- `observability/` — Giám sát chất lượng, câu hỏi mở, giả định, quyết định, bế tắc
- `memory/` — Bộ nhớ ngữ cảnh tác vụ (working-context, project-state, scratchpad)
- `validators/` — Scripts tự động cưỡng chế tiêu chuẩn
- `evaluations/` — Đánh giá năng lực agent và kiểm thử hồi quy
- `hooks/` — Lifecycle hooks (agent_gate_hook.py, ps1 scripts)
- `tools/` — Công cụ tích hợp ngoại vi (Jira, Telegram)
- `scripts/` — Utility scripts
- `.agents/` — Unified Hub: Single Source of Truth chứa personas, definitions, rules, skills, hooks.json

---

## 3. ADR Format

> **Nguồn:** Michael Nygard — [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)

```markdown
# ADR-[NNN]: [Tên quyết định ngắn gọn]

**Ngày:** DD/MM/YYYY  
**Trạng thái:** Proposed | Accepted | Deprecated | Superseded by ADR-XXX  
**Người quyết định:** [SA/TL tên]  
**Stakeholders đã review:** [danh sách]

## Bối cảnh (Context)
[Vấn đề cần giải quyết, constraints, forces]

## Quyết định (Decision)
[Quyết định cụ thể — dùng active voice: "Chúng ta sẽ dùng..."]

## Lý do (Rationale)
[Tại sao chọn option này — dựa trên 5 chiều: Scale, Cost, Team, Time, Risk]

## Phương án đã cân nhắc (Alternatives Considered)
| Option | Pros | Cons | Lý do không chọn |
|--------|------|------|-----------------|

## Hệ quả (Consequences)
- **Tích cực:** [...]
- **Tiêu cực / Đánh đổi:** [...]
- **Rủi ro còn lại:** [...]

## Review lại khi nào
[Điều kiện trigger review: VD "Khi traffic > 10K req/day" hoặc "Sau 6 tháng"]
```

---

## 4. Document Lifecycle — Draft → Approved

```
Tạo tài liệu mới
      ↓
Lưu tại artifacts/requirements/[tên-file].md
      ↓
AI thông báo: "File đang ở artifacts/requirements/. Duyệt để chuyển sang [thư mục chính]?"
      ↓
User duyệt (tại Hard Stop hoặc explicit approval)
      ↓
Chuyển sang thư mục chính (artifacts/requirements/, artifacts/decisions/, etc.)
      ↓
Không xóa bản draft — archive hoặc để nguyên
```

---

## 5. Meeting Notes Format

```markdown
# [Tên cuộc họp] — [DD/MM/YYYY]

**Participants:** [danh sách]  
**Facilitator:** [tên]  
**Ghi chú bởi:** [tên / AI]

## Decisions Made ✅
1. [Quyết định cụ thể]

## Action Items 📋
| # | Việc cần làm | Owner | Deadline |
|---|-------------|-------|---------|

## Open Items ❓
1. [Câu hỏi chưa có câu trả lời]

## Next Meeting
[Ngày / thời gian / agenda]
```

---

## 6. Status Report Cadence

| Loại | Frequency | Owner | Format |
|------|-----------|-------|--------|
| Daily Standup notes | Daily (nếu có) | PM | 3 bullets: Done/Doing/Blocked |
| Sprint Review | Mỗi sprint end | PM + PO | `artifacts/analysis/meetings/sprint-[N]-review.md` |
| Status Report | Weekly | PM | `artifacts/analysis/meetings/status-report-week-[N].md` |
| Retrospective | Mỗi sprint end | SM/PM | `artifacts/analysis/meetings/retro-sprint-[N].md` |
