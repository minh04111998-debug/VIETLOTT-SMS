# Lifecycle Hooks System — Vietlott SMS Multi-Agent Engineering

> **Mục tiêu:** Tự động hóa các điểm kiểm tra an toàn (Guardrail Checkpoints) trước và sau mỗi tác vụ phân tích, thiết kế, lập trình và kiểm thử.

---

## 1. Danh Mục Các Hook

| Hook | File thực thi | Khi nào kích hoạt | Mục đích kiểm tra |
|---|---|---|---|
| **Agent Gate (tự động)** | `agent_gate_hook.py` | IDE tự gọi: `PostToolUse` sau mỗi lần ghi file + `PreInvocation` trước mỗi lượt model | Quét `artifacts/**/*.md` vừa đổi (mơ hồ, PII, từ cấm); FAIL → ghi Gate Report + báo vi phạm lại cho agent |
| **Pre-Task** | `pre-task.ps1` | Chạy tay, trước khi bắt đầu task | Kiểm tra môi trường, role rules, và các câu hỏi mở chặn đường (Blockers). |
| **Post-Task** | `post-task.ps1` | Chạy tay, sau khi hoàn thành bản thảo | Quét từ mơ hồ, PII, từ cấm cho 1 file chỉ định, sinh Gate Report. |
| **Critique-Failure** | `on-critique-failure.ps1` | Chạy tay, khi bước CRITIQUE thất bại > 2 lần | Kích hoạt Deadlock Escalation, lập hồ sơ bất đồng. |
| **Pre-Commit** | `pre-commit.ps1` | Trước khi commit (cần cài vào Git hook) | Ngăn commit file chứa số điện thoại thật, OTP, secret key. |

---

## 2. Cấu Hình Hook Tự Động

- **File cấu hình duy nhất được IDE nạp:** [`.agents/hooks.json`](../.agents/hooks.json). Không tạo `hooks.json` ở nơi khác (IDE bỏ qua → gây hiểu nhầm).
- **Thư mục làm việc khi hook chạy** = thư mục chứa `hooks.json` (`.agents/`) → đường dẫn script viết dạng `../hooks/...`.
- **Ràng buộc payload (theo docs Antigravity):**
  - `PostToolUse` **không** chứa tên file vừa ghi → hook tự dò file đổi theo `mtime` trong `artifacts/`.
  - `PostToolUse` chỉ được trả `{}` → vi phạm được xếp hàng trong `hooks/.gate_hook_state.json` và bơm cho agent ở `PreInvocation` (`ephemeralMessage`), mỗi vi phạm báo **1 lần**.
  - stdout phải là JSON thuần → không dùng `Write-Host`/`print` tự do trong hook tự động.
- **Tắt tạm:** thêm `"enabled": false` vào khối `quality-gate` / `quality-gate-feedback` trong `.agents/hooks.json`.
- **Kiểm tra tính toàn vẹn cấu hình:** `python validators/harness_integrity_checker.py` (check `HOOKS`).

---

## 3. Cách Sử Dụng Thủ Công

Người dùng hoặc Agent có thể gọi trực tiếp:
```powershell
# Chạy pre-task cho vai trò BA và tính năng campaign-tang-ve:
powershell -ExecutionPolicy Bypass -File ./hooks/pre-task.ps1 -Role "ba" -Feature "campaign-tang-ve"

# Chạy post-task kiểm tra tài liệu vừa tạo:
powershell -ExecutionPolicy Bypass -File ./hooks/post-task.ps1 -ArtifactPath "artifacts/requirements/srs-campaign-tang-ve-bank.md" -Role "ba"
```
