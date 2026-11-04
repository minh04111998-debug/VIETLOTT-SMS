# 🛡️ Guardrails — Ranh Giới Cứng

> **Mục đích:** Định nghĩa rào chắn KHÔNG THỂ vượt qua cho AI Agent.
> Áp dụng cho MỌI vai trò, MỌI task. Không có ngoại lệ.
>
> **Nguồn:** [StoriesOnBoard — AI Agent Playbook](https://storiesonboard.com/blog/?p=6316)

---

## 1. Phân Vai Human ↔ AI (Bước 0)

### AI Tự Làm (Phần Rộng & Nhanh)

- Gom ý tưởng thành nhóm (Affinity clustering)
- Viết nháp User Story theo INVEST + AC dạng Given-When-Then
- Lập danh sách câu hỏi làm rõ và giả định
- Chuẩn hóa thuật ngữ theo `knowledge/glossary/glossary.md`
- Phân tích exception & edge cases
- Viết nháp SRS/BRD/PRD theo template `templates/`
- Cross-review bản nháp (đội mũ DEV, QA, PO)

### Human Giữ (Phần Quyết Định & Xác Nhận)

- Xác định kết quả kinh doanh (business outcome) & chỉ số thành công
- Quyết định cắt scope và phân lát MVP
- Xác nhận quy tắc nghiệp vụ với stakeholder và pháp lý
- Viết/phê duyệt yêu cầu phi chức năng (NFR)
- Cân nhắc đánh đổi (trade-offs)
- Ký duyệt cuối cùng (Sign-off) — 🛑 Hard Stop

---

## 2. Hành Động CẤM (Hard Boundaries)

| # | Hành động CẤM | Lý do |
|---|---------------|-------|
| 1 | KHÔNG tự đẩy nội dung lên backlog thật (Jira/Confluence) | Chỉ tạo bản nháp trong `artifacts/` với trạng thái `Draft` |
| 2 | KHÔNG bịa số liệu, thống kê, hoặc trích dẫn stakeholder | Mọi số liệu phải có nguồn từ `knowledge/standards/source-registry.md` |
| 3 | KHÔNG đưa dữ liệu khách hàng nhạy cảm (PII) vào output | Chưa có approval bảo mật |
| 4 | KHÔNG tự phê duyệt tài liệu | Mọi baseline phải qua 🛑 Human Sign-off |
| 5 | KHÔNG tự thay đổi scope hoặc priority | Chỉ PO (Human) quyết định |
| 6 | KHÔNG viết NFR (yêu cầu phi chức năng) chính thức | Chỉ gợi ý dạng `[📌 CẦN HUMAN QUYẾT ĐỊNH]` |
| 7 | KHÔNG tự chuyển tài liệu từ `Draft` sang `Approved` hoặc `Baseline` | Chỉ sau khi Quality Gate PASS và Human approve |
| 8 | KHÔNG dùng thuật ngữ ngoài `knowledge/glossary/glossary.md` mà không gắn nhãn | Gắn `[⚠️ THUẬT NGỮ MỚI]` |

---

## 3. Giả Định Phải Gắn Nhãn

Mọi giả định AI đưa ra **PHẢI** có tag rõ ràng:

| Tag | Ý nghĩa | Ví dụ |
|-----|---------|-------|
| `[⚠️ GIẢ ĐỊNH — cần stakeholder xác nhận]` | AI suy luận nhưng chưa có nguồn xác nhận | "Timeout SMS = 30s `[⚠️ GIẢ ĐỊNH]`" |
| `[❓ CÂU HỎI MỞ]` | Thông tin cần làm rõ trước khi tiếp tục | "Ngưỡng giải lớn là bao nhiêu? `[❓ CÂU HỎI MỞ]`" |
| `[📌 CẦN HUMAN QUYẾT ĐỊNH]` | Quyết định thuộc quyền Human | "NFR: Uptime 99.9% `[📌 CẦN HUMAN QUYẾT ĐỊNH]`" |
| `[✅ ĐÃ XÁC NHẬN bởi: ...]` | Human đã verify | "Bingo18 = 159 kỳ/ngày `[✅ ĐÃ XÁC NHẬN]`" |

---

## 4. Permission Matrix — Quyền Truy Cập File

| Vùng | Permission | Ghi chú |
|------|-----------|---------|
| `knowledge/` | 🟢 READ | Glossary, business rules, kiến trúc — chỉ đọc, sửa cần approval |
| `references/` | 🟢 READ | Chuẩn quốc tế (BABOK, CPOA, ISTQB) — chỉ đọc |
| `templates/` | 🟢 READ | Template mẫu — chỉ đọc |
| `artifacts/` (nháp) | 🟡 READ + WRITE | Soạn thảo tài liệu với trạng thái `Draft` trong frontmatter |
| `artifacts/` (baseline) | 🔴 WRITE BLOCKED | Chỉ chuyển `Approved` hoặc `Baseline` sau Quality Gate + Human Sign-off |
| `plans/` | 🟡 READ + WRITE | Cập nhật tiến độ task/sprint và nợ kỹ thuật |
| `observability/` | 🟡 READ + WRITE | Ghi câu hỏi mở, giả định, quyết định, biên bản bế tắc |
| `memory/` | 🟡 READ + WRITE | Ghi scratchpad, working context hiện tại |
