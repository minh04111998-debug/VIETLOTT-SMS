# 🧠 Context Budget & Lazy Loading Strategy

> **Mục đích:** Document này định nghĩa chiến lược quản lý "bộ nhớ" (Context Window) của AI.
> Tránh việc AI phải nạp quá nhiều thông tin không cần thiết dẫn đến "loãng" ngữ cảnh, quên yêu cầu chính, hoặc sinh ảo giác (hallucination).

---

## 1. Nguyên Tắc Cốt Lõi (Core Principles)

1. **Lazy Loading (Tải Khi Cần):** KHÔNG BAO GIỜ đọc toàn bộ thư mục `.agents/` cùng lúc. Chỉ đọc file khi bước đó thực sự cần.
2. **Drop Context (Xóa Bộ Nhớ Cũ):** Chuyển từ Phase A sang Phase B (VD: từ BA sang DEV), AI nên bỏ qua (quên bớt) chi tiết thảo luận của Phase A, chỉ nạp **Artifact đầu ra đã chốt** của Phase A.
3. **Budget Limit:** System Prompt + Agent Rules nên chiếm tối đa **10-15%** Context Window. Đẩy 85% còn lại cho Source Code, User Chat, và Artifacts.

---

## 2. Phân Cấp Context (What to load when)

### 🔴 Tier 1: Core System (Luôn luôn tồn tại)
- `AGENTS.md` — Project Rules gốc.

### 🟡 Tier 2: Role & Protocol (Tải theo ngữ cảnh hiện tại)
Ví dụ user gõ *"Nạp role BA"*:
- **Load Mới:** `.agents/rules/ba-rules.md`
- **Load Mới:** `.agents/skills/ba/SKILL.md`
- **Tùy chọn:** Nếu bắt đầu Review → Load `evaluations/agents/cross-review-protocol.md`
- **Tùy chọn:** Nếu phải viết Yêu cầu phi chức năng (NFR) → Load `.agents/rules/security-checklist.md`

(*Lưu ý: System KHÔNG đọc rules của PM, DEV, QA lúc này.*)

### 🟢 Tier 3: Workflows & Project Context (Tải 1 lần để thực thi)
- Lệnh `/create-prd` → Load `workflows/product-discovery/create-prd.md` (Chỉ load đúng workflow này).
- **Tool Registry:** Khi nhận yêu cầu phức tạp (>3 bước), AI PHẢI tham chiếu `tools/tool-registry.md` để biết tool nào khả dụng.
- Đọc file `knowledge/product/project-context.md` (Project Memory — living document, khởi tạo từ template) để lấy bối cảnh dự án.

---

## 3. Workflow Chuyển Giao (Handoff Strategy)

When kết thúc 1 phase và chuyển sang role khác. Ví dụ BA → SA.

**Cách SAI (Tiết kiệm token kém):**
AI mang toàn bộ lịch sử chat dài dòng giữa PO và BA sang cho SA phân tích kiến trúc.

**Cách ĐÚNG (Tiết kiệm token hiệu quả):**
1. Gọi Role SA.
2. SA chỉ yêu cầu tải đúng 2 thứ:
   - `artifacts/requirements/srs-campaign-tang-ve-bank.md` (Kết quả Approved của BA).
   - `.agents/rules/dev-rules.md`.
3. SA bỏ qua toàn bộ những gì BA và PO đã chém gió trước đó để focus vào kiến trúc.

## 4. Tóm Tắt
1. **Chỉ đọc rules của đúng MỘT Role đang nhập vai.**
2. **Chỉ viện dẫn tài liệu chuyên sâu khi thực sự đụng đến vấn đề đó (VD: đụng bảo mật mới đọc `.agents/rules/security-checklist.md`).**
3. **Lấy File Đầu Ra (Artifact) làm phương tiện giao tiếp giữa các roles, không dùng lịch sử Chat.**
