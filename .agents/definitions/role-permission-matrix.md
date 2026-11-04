# Role Permission Matrix & Access Boundaries

> **Nguồn chân lý duy nhất (SSOT):** Chi tiết ranh giới cứng xem tại [.agents/rules/boundaries.md](file:///f:/VIETLOTT-SMS/.agents/rules/boundaries.md).  
> **Mục tiêu:** Định nghĩa ma trận phân quyền thực thi và quyền truy cập tập tin cho 7 vai trò kỹ thuật + Governance.

---

## 1. Ma Trận Phân Quyền Vai Trò (Role RACI Matrix)

| Hoạt động hệ thống | PO | BA | DEV | QA | PM | DA | Designer | Governance | Human |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Định hình Problem & Outcome | **R** | C | I | I | C | C | I | I | **A** |
| Phân tích Requirement & SRS | C | **R** | C | C | I | I | C | I | **A** |
| Thiết kế UI/UX & Design Tokens | C | C | C | C | I | I | **R** | I | **A** |
| Triển khai Code & Architecture | I | C | **R** | C | I | I | I | I | **A** |
| Kiểm thử Test Cases & Quality Gate | I | C | C | **R** | C | I | I | I | **A** |
| Báo cáo Tiến độ & Release Readiness | C | I | I | C | **R** | I | I | I | **A** |
| Phân tích Dữ liệu Doanh thu / KPI | C | I | I | I | I | **R** | I | I | **A** |
| Kiểm soát Tuân thủ PII / Ranh giới | I | I | I | I | I | I | I | **R** | **A** |
| Ký duyệt Baseline (Hard Stop) | - | - | - | - | - | - | - | - | **A (Sign-off)** |

*Ghi chú: R = Responsible (Thực hiện), A = Accountable (Chịu trách nhiệm tối cao/Duyệt), C = Consulted (Tham vấn), I = Informed (Nhận thông tin).*

---

## 2. Phân Quyền Truy Cập Thư Mục (File Access Permissions)

| Thư mục | Quyền hạn Agent | Mục đích sử dụng |
|---|:---:|---|
| `knowledge/` | 🟢 READ ONLY | Tri thức nền, luật chơi Vietlott, glossary — Không tự sửa |
| `references/` | 🟢 READ ONLY | Khung chuẩn quốc tế (BABOK, CPOA, ISTQB) |
| `templates/` | 🟢 READ ONLY | Biểu mẫu chuẩn (Golden templates) |
| `artifacts/` (trạng thái Draft) | 🟡 READ + WRITE | Soạn thảo tài liệu bàn giao với `status: Draft` |
| `artifacts/` (trạng thái Baseline) | 🔴 WRITE BLOCKED | Chỉ chuyển sang `Approved`/`Baseline` sau Quality Gate + Human Sign-off |
| `plans/` | 🟡 READ + WRITE | Cập nhật tiến độ sprint, task và nợ kỹ thuật |
| `observability/` | 🟡 READ + WRITE | Ghi nhận câu hỏi mở, giả định, quyết định, log bế tắc |
| `memory/` | 🟡 READ + WRITE | Ghi chép working context của tác vụ hiện hành |

---

## 3. Ranh Giới Bắt Buộc (Mandatory Guardrails Reference)

Mọi Agent phải tuân thủ nghiêm ngặt 8 điều cấm và quy tắc gắn nhãn giả định tại [.agents/rules/boundaries.md](file:///f:/VIETLOTT-SMS/.agents/rules/boundaries.md).
