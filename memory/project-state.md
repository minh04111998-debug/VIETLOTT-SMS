# Project State — Vietlott SMS

> **Cập nhật gần nhất:** 2026-10-10 | **Kiến trúc:** Multi-Agent Harness Engineering v3.1 (7 AI Harnesses Logical Overlay — DEC-008)

---

## 1. Trạng Thái Hiện Tại (Current Active Focus)

- **Cấu trúc thư mục:** Ánh xạ logic 14 thư mục root và `.agents/` vào 7 AI Harnesses chuẩn (`.agents/definitions/harness-map.json`).
- **Vai trò đang kích hoạt:** Hệ thống phân quyền 8 Personas (`pm`, `po`, `ba`, `da`, `dev`, `qa`, `designer`, `governance`).
- **An ninh & Kiểm soát:** Tích hợp `validators/secret_scanner.py` (OWASP LLM Top 10), gỡ bỏ cổng duyệt Telegram (thay bằng Human in-session trực tiếp; Telegram chuyển sang notify-only).
- **Đánh giá & Vận hành:** Khung Golden Dataset (`evaluations/golden/`), AgentOps Weekly Metrics (`validators/ops_metrics.py`), bộ kiểm chứng hồi quy 45 checks PASS.

---

## 2. Bản Đồ Trạng Thái Theo Value Stream

| Value Stream | Trạng thái | Artifacts chính | Người phụ trách chính |
|---|---|---|---|
| **Product Discovery** | Hoàn thành sơ bộ | `artifacts/product/` | PO |
| **Requirement** | Đang thực hiện | `artifacts/requirements/` | BA |
| **Feature Development** | Sẵn sàng triển khai | `artifacts/technical/` | DEV / Designer |
| **Bug Fix & Testing** | Sẵn sàng triển khai | `artifacts/testing/` | QA |
| **Data Analysis** | Hoàn thành báo cáo Q3 | `artifacts/analysis/` | DA |
| **Release & Readiness** | Chuẩn bị quy trình | `plans/active/` | PM |

---

## 3. Milestones Đã Hoàn Thành & Tiếp Theo

1. [x] Khởi tạo bộ khung 20 thành phần Harness Engineering (DEC-001).
2. [x] Di chuyển và phân loại toàn bộ tài liệu từ các thư mục cũ (DEC-001, DEC-005).
3. [x] Thiết lập hợp đồng bàn giao (Handoff Contracts) và Persona Governance (DEC-001, DEC-008).
4. [x] Khởi chạy quy trình kiểm thử và đánh giá tự động (Quality Gate Runner & Regression Evals 45/45 PASS — DEC-003, DEC-005, DEC-008).
5. [x] Hợp nhất Single Source of Truth về `.agents/` (DEC-004).
6. [x] Tái cấu trúc 7 AI Harnesses, loại bỏ cổng duyệt Telegram, bổ sung Secret Scanner & AgentOps Metrics (DEC-008).
7. [x] Đóng gói 4 bộ Skill Checklist thẩm định Senior Output cho BA, PO, QA, DA (30 skills toàn hệ thống).
8. [ ] Nạp các tài liệu mẫu (exemplar deliverables) đã phê duyệt vào `evaluations/golden/manifest.json` (Q-007).

