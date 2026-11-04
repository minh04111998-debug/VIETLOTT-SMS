# Golden Set — Đánh giá chất lượng nội dung deliverable (Evaluation Harness, DEC-008)

> **Vấn đề cần giải quyết:** Suite `validators` và `behavior` chỉ bắt lỗi bề mặt (PII, từ cấm, regex câu trả lời). Chúng không trả lời được câu hỏi "PRD/SRS này có **tốt** không". Golden set là tập deliverable mẫu đã được Human ký duyệt, dùng làm thước đo khi sửa rules/skills/workflows.

## 1. Phân vai: validators vs evaluations

| | `validators/` | `evaluations/` |
|---|---|---|
| Khi nào chạy | Trực tuyến — mỗi lần ghi artifact (hook) hoặc trước bàn giao (`gate_runner.py`) | Ngoại tuyến — trước và sau khi sửa harness (`run_evals.py`) |
| Trả lời câu hỏi | "Artifact này có vi phạm rào chắn không?" | "Harness tốt lên hay tệ đi?" |
| Kết quả FAIL nghĩa là | Sửa artifact | Sửa rule/skill/workflow vừa đổi |

## 2. Cấu trúc

| File | Vai trò |
|---|---|
| `manifest.json` | Danh sách mẫu golden (đường dẫn, vai trò, điểm rubric tối thiểu) |
| `rubric.md` | Thang chấm 5 tiêu chí × 0–2 điểm cho người chấm (hoặc LLM-as-judge sau này) |

Suite `golden` trong `evaluations/run_evals.py` kiểm tra **tự động** mỗi mục trong manifest:
1. File tồn tại.
2. File ghi trạng thái `Approved` hoặc `Baseline`.
3. File vẫn PASS 4 validator an toàn (PII, secret, từ cấm, mơ hồ) — mẫu golden không được tự vi phạm rào chắn.
4. Có điểm rubric do Human chấm và điểm ≥ `min_score`.

Manifest rỗng → suite báo `NOT_RUN` (không làm fail).

## 3. Thêm một mẫu golden (chỉ Human)

1. Chọn deliverable đã qua Quality Gate và đã được Human Sign-off (trạng thái `Approved`/`Baseline`).
2. Chấm theo `rubric.md`, ghi điểm vào trường `human_score`.
3. Thêm mục vào `manifest.json`:
   ```json
   {"id": "GOLD-PRD-01", "path": "artifacts/product/<file>.md", "role": "PO", "human_score": 9, "min_score": 8, "approved_by": "<tên>", "approved_on": "YYYY-MM-DD"}
   ```

> Hiện chưa có artifact nào ở trạng thái `Approved`/`Baseline` — xem `observability/open-questions.md` Q-007.
