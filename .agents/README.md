# Unified Agent & Customization Hub (`.agents/`)

Thư mục `.agents/` là trung tâm hợp nhất duy nhất (Single Source of Truth — SSOT theo DEC-004 & DEC-008) cho toàn bộ hệ thống Multi-Agent và Antigravity IDE Customization:

## 1. Tầng Điều Phối & Nhận Diện (Harness Engineering Coordination Layer)
- `.agents/personas/`: Định nghĩa 8 Personas chính thức (`pm`, `po`, `ba`, `da`, `dev`, `qa`, `designer`, `governance`).
- `.agents/definitions/`:
  - `harness-map.json`: Ánh xạ logic 14 thư mục root và `.agents/` vào 7 AI Harnesses (DEC-008).
  - `handoff-contracts.md`: Hợp đồng bàn giao artifact giữa các vai trò theo luồng Discovery → Release.
  - `agent-spec.schema.json`: JSON Schema chuẩn hóa cấu hình Agent.
  - `role-detector.md`: Bộ quy tắc tự động nhận diện vai trò dựa trên input/lệnh.
  - `role-permission-matrix.md`: Ma trận phân quyền hành động giữa Human và Agent (đồng bộ với `boundaries.md`).

## 2. Tầng Tích Hợp Antigravity IDE (IDE Customization Hub)

Toàn bộ cấu hình IDE được tập trung hóa trực tiếp tại `.agents/` (Single Source of Truth, không dùng junction hay hard link ngoài root):

| Đường dẫn nạp | Quy mô | Vai trò / Chức năng |
|---|---|---|
| `.agents/skills/<skill>/` | 30 skills | Kỹ năng nghiệp vụ, phân tích, kỹ thuật, audit checklist (tự động phát hiện bởi IDE) |
| `.agents/rules/<file>.md` | 16 rules | Bộ quy tắc hành vi, ranh giới, PII, bảo mật, từ cấm |
| `.agents/hooks.json` | 1 config | Cấu hình hook duy nhất được IDE nạp (trỏ đến script tại `hooks/agent_gate_hook.py`) |

## 3. Kiểm Tra Toàn Vẹn Hệ Thống
Chạy bộ kiểm tra bất kỳ lúc nào sau khi thêm/sửa rules, skills hoặc definitions:
```powershell
python validators/harness_integrity_checker.py
```

