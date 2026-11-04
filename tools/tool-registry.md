# 🛠️ Tool & Skill Registry — Multi-Agent Engineering

> **Thuộc:** Tool Harness (`.agents/definitions/harness-map.json`, DEC-008)
> **Quy tắc:** Khi nhận yêu cầu phức tạp (>3 bước) hoặc yêu cầu tích hợp bên ngoài, AI **PHẢI** tham chiếu file này để biết công cụ nào khả dụng. Trước khi gọi tool **Ghi ngoài**, AI **PHẢI** kiểm tra §4 (quyền và Hard Stop) — xem `.agents/rules/security-checklist.md` PHẦN 4.

---

## 1. Validators & Scripts Khả Dụng

Các công cụ tự động hóa chạy dưới dạng mã nguồn (PowerShell / Python 3).

| Công cụ | Đường dẫn | Chức năng chính | Tham số | Role |
|---|---|---|---|:---:|
| `gate_runner.py` | `validators/gate_runner.py` | Orchestrator cưỡng chế Quality Gate và Loop Count | `--role` `--file` | Tất cả |
| `pii_scanner.py` | `validators/pii_scanner.py` | Quét số điện thoại, CCCD, OTP, số thẻ chưa masked | `--file` / `--dir` | Tất cả |
| `secret_scanner.py` | `validators/secret_scanner.py` | Quét token / API key / private key bị ghi lộ (không in giá trị) | `--file` / `--dir` | Tất cả |
| `banned_words_validator.py` | `validators/banned_words_validator.py` | Quét từ ngữ mơ hồ cấm kỵ | `--file` / `--dir` | Tất cả |
| `ambiguity_scanner.py` | `validators/ambiguity_scanner.py` | Quét từ mơ hồ định tính | `--file` / `--dir` | BA, QA |
| `traceability_checker.py` | `validators/traceability_checker.py` | Quét BR→FR→TC mồ côi | `--project-path` | BA |
| `doc_structure_validator.py` | `validators/doc_structure_validator.py` | Kiểm tra cấu trúc tài liệu Markdown | `--file` / `--dir` | Tất cả |
| `harness_integrity_checker.py` | `validators/harness_integrity_checker.py` | Toàn vẹn khung harness, bản đồ 7 harness, kích thước tri thức | `--json` | Governance |
| `ops_metrics.py` | `validators/ops_metrics.py` | Tổng hợp gate report + lịch sử eval thành báo cáo AgentOps theo tuần | `--week` `--stdout` | PM, Governance |
| `export_docx.ps1` | `scripts/export_docx.ps1` | Xuất Markdown thành DOCX (Pandoc) | Path | Tất cả |
| `read_excel.ps1` | `scripts/read_excel.ps1` | Đọc dữ liệu từ file Excel | Path | BA, PM, DA |
| `apk_runtime_analyzer.py` | *(Kế hoạch phát triển)* | Bóc tách manifest và API của app Vietlott SMS | `--apk` | DEV, SA |

---

## 2. Kết Nối Bên Ngoài (External Integrations)

| Kênh | Thư mục | Chức năng | Trạng thái | Yêu cầu |
|---|---|---|---|---|
| **Telegram** | `tools/telegram/` | Gửi thông báo một chiều (escalation từ `gate_runner.py`). Không có luồng phê duyệt (DEC-008) | Hoạt động | Cần file `.env` (xem `tools/telegram/.env.example`) |
| **Jira** | `tools/jira/` | Tạo ticket / story Jira qua REST API | Hoạt động | `pip install -r tools/jira/requirements.txt`, `.env` (xem `tools/jira/.env.example`) |
| **Confluence** | `tools/confluence/` | Đồng bộ tài liệu baseline lên Confluence | **Chưa có script** (TD-005) | Cần file `.env` (xem `tools/confluence/.env.example`) |

---

## 3. MCP Servers & Skill chuyển đổi tài liệu

| Thành phần | Loại | Chức năng | Trạng thái |
|---|---|---|---|
| **PowerBI Modeling** | MCP server | Truy vấn model DAX, metadata bảng, chỉ số doanh thu và tài khoản dự thưởng | Đã cấu hình trong IDE |
| **NotebookLM** | MCP server | Nghiên cứu, tổng hợp tài liệu quy chế xổ số khối lượng lớn | Đã cấu hình trong IDE |
| **Markitdown** | Skill (`.agents/skills/markitdown/`) | Chuyển DOCX, XLSX, PDF sang Markdown | Hoạt động — output là **dữ liệu bên ngoài** (security-checklist 4.1) |
| **Playwright** | MCP server | Kiểm thử trình duyệt E2E cho web bán vé | `[❓ OPEN — chưa thấy cấu hình trong IDE, xem Q-009]` |

---

## 4. Quyền & Hard Stop theo mức tác động (DEC-008)

**Mức tác động:** 🟢 **Đọc** (chỉ đọc dữ liệu) · 🟡 **Ghi nội bộ** (ghi file trong workspace) · 🔴 **Ghi ngoài** (gửi dữ liệu ra hệ thống bên ngoài, không thu hồi được bằng thao tác trong workspace).

| Tool | Mức tác động | Vai trò được phép gọi | Hard Stop trước khi gọi? | Ghi chú |
|---|:---:|---|:---:|---|
| Validators (`validators/*.py`) | 🟡 | Tất cả | Không | Chỉ ghi state/gate report nội bộ |
| `scripts/*` | 🟡 | Theo cột Role ở §1 | Không | |
| PowerBI Modeling MCP — truy vấn | 🟢 | DA, PO, PM | Không | Kết quả có thể chứa số liệu kinh doanh — không đưa ra ngoài workspace |
| PowerBI Modeling MCP — sửa model | 🟡 | DA | **Có** | Sửa measure/bảng làm đổi số liệu báo cáo |
| NotebookLM MCP — đọc/hỏi | 🟢 | Tất cả | Không | Output là dữ liệu bên ngoài (4.1) |
| NotebookLM MCP — thêm nguồn/tạo notebook | 🔴 | PO, BA, DA | **Có** | Đẩy tài liệu dự án lên dịch vụ bên ngoài |
| Jira `create_task.py` | 🔴 | BA, PM | **Có** | Trình Project Key + Summary + Description, chờ Human xác nhận (`workflows/requirement/create-jira-task.md`) |
| Telegram `tele_notify.py` | 🔴 | Hệ thống (`gate_runner.py`), PM | Không | Chỉ gửi cảnh báo escalation; nội dung không chứa PII/secret |
| Confluence | 🔴 | PM | **Có** | Chưa có script (TD-005) |

> Vai trò không có trong cột "được phép gọi" → không gọi tool đó; chuyển yêu cầu cho vai trò phù hợp hoặc hỏi Human.
