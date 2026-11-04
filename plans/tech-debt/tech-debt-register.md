# Technical Debt Register (Sổ Đăng Ký Nợ Kỹ Thuật)

> **Mục tiêu:** Quản lý, phân loại và lập lộ trình khắc phục các món nợ kỹ thuật (Tech Debt) phát sinh trong quá trình phát triển nhanh.
> **Quy định:** Không được để nợ kỹ thuật mức Critical tồn tại quá 2 sprint.

---

## 1. Danh Mục Nợ Kỹ Thuật Hiện Hữu

| ID | Ngày ghi nhận | Thành phần | Mô tả nợ kỹ thuật | Mức độ rủi ro | Chi phí khắc phục (Story Points) | Kế hoạch xử lý | Trạng thái (Open/In Progress/Resolved) |
|---|---|---|---|:---:|:---:|---|:---:|
| TD-001 | 2026-10-05 | Automation Testing | Chưa có kịch bản E2E tự động cho luồng thanh toán qua Bank Sandbox | Trung bình | 5 SP | Sprint tiếp theo | Open |
| TD-002 | 2026-10-05 | API Integration | Cơ chế retry kết nối Telco đang hardcode trong script, chưa đưa vào cấu hình dynamic | Thấp | 2 SP | Đưa vào backlog DEV | Open |
| TD-003 | 2026-10-05 | Data Model | Các bảng đối soát giao dịch TKDT chưa có index tối ưu trên trường `transaction_time` | Cao | 3 SP | Phối hợp DA & DEV | Open |
| TD-004 | 2026-10-08 | Knowledge Base | Tệp `fintech-knowledge-base.md` ngoại cỡ (40KB ~10k tokens) cần phân rã theo 5 module chuyên biệt | Trung bình | 3 SP | Phân rã 5 module tại `knowledge/product/fintech/` (DEC-007) | Resolved |
| TD-005 | 2026-10-08 | External Tools | `tools/confluence/` chưa có executable script đồng bộ tài liệu sang Confluence API | Thấp | 2 SP | Đưa vào backlog Tooling | Open |
| TD-006 | 2026-10-08 | Script Cleanliness | Thư mục `scripts/` chứa 23 scripts tiện ích ở root chưa phân nhóm theo chức năng | Thấp | 2 SP | Phân nhóm vào `scripts/diagrams/`, `scripts/converters/`, `scripts/extractors/` (DEC-007) | Resolved |
| TD-007 | 2026-10-08 | Schema Spec | `.agents/definitions/agent-spec.schema.json` chưa có automated test đối chiếu các file `persona.md` | Thấp | 2 SP | Đưa vào backlog Harness | Open |

---

## 2. Tiêu Chí Ưu Tiên Xử Lý (Tech Debt Prioritization)
1. **Critical:** Lỗ hổng bảo mật, nguy cơ thất thoát tiền/vé, rò rỉ PII -> Xử lý ngay lập tức (P0).
2. **High:** Ảnh hưởng trực tiếp tới tốc độ quay thưởng hoặc nghẽn mạng giờ cao điểm -> Xử lý trong sprint kế tiếp.
3. **Medium/Low:** Code smell, thiếu test coverage, tài liệu chưa đồng bộ -> Phân bổ 15-20% capacity mỗi sprint.
