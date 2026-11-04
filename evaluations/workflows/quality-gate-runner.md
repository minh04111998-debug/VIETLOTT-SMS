# 🚀 Quality Gate Runner

> **Mục đích:** Hướng dẫn AI cách tự động gọi các scripts kiểm thử chất lượng (Quality Gates) sau khi hoàn thành một bản draft. Kết hợp với `.agents/rules/self-correction-rules.md`.

## Bảng Mapping (Role → Checklist → Script)

Khi bạn (AI) hoàn thành xong 1 output, hãy xác định mình đang ở vai trò nào, mở file Checklist tương ứng, và chạy các lệnh Script hỗ trợ bên dưới để tự bắt lỗi.

| Vai trò / Loại output | File Checklist cần check | Các Scripts tự động có thể gọi | Lệnh ví dụ (sử dụng Orchestrator) |
|-----------------------|--------------------------|--------------------------------|-----------|
| **BA** (SRS, BRD, CR) | `evaluations/skills/ba-output-checklist.md` | `traceability_checker.py`<br>`ambiguity_scanner.py` | `python validators/gate_runner.py --role BA --file [đường_dẫn]` |
| **PO** (PRD, Roadmap) | `evaluations/skills/po-output-checklist.md` | `ambiguity_scanner.py` | `python validators/gate_runner.py --role PO --file [đường_dẫn]` |
| **PM** (Plan, Status) | `evaluations/skills/pm-output-checklist.md` | `doc_structure_validator.py` | `python validators/gate_runner.py --role PM --file [đường_dẫn]` |
| **DEV** (Source code) | `evaluations/skills/dev-output-checklist.md` | (Chạy Linter / Unit test / SAST scanner nếu dự án có setup) | `npm run lint` hoặc `pytest` |
| **QA** (Test Plan) | `evaluations/skills/qa-output-checklist.md` | `doc_structure_validator.py` | `python validators/gate_runner.py --role QA --file [đường_dẫn]` |
| **Designer** (UI/UX) | `evaluations/skills/designer-output-checklist.md` | (Manual review bằng checklist) | `python validators/gate_runner.py --role Designer --file [đường_dẫn]` |
| **DA** (Dashboard, Report, Insight) | `evaluations/skills/da-output-checklist.md` | `doc_structure_validator.py` | `python validators/gate_runner.py --role DA --file [đường_dẫn]` |

---

## Các Bước Thực Thi (Dành cho AI)

1. Đọc nội dung file Checklist tương ứng.
2. Nếu có Script hỗ trợ, HÃY GỌI LUÔN Orchestrator bằng lệnh ví dụ ở trên để quét file draft vừa tạo. Orchestrator sẽ tự đếm số vòng lặp và chặn nếu vượt quá.
3. Thu thập kết quả lỗi từ Orchestrator.
4. Tự động sửa lại file draft để triệt tiêu lỗi (Tối đa 2 vòng lặp, xem chi tiết ở `.agents/rules/self-correction-rules.md`).
5. Trình bày output cuối cùng cho User cùng với Gate Report.
