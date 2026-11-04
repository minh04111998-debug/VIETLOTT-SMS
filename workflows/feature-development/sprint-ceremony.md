---
description: Quy trình Sprint Ceremony & E2E Auto-Agent Pipeline - Hỗ trợ Agile Scrum và Waterfall Phase-gate
---

# Workflow: Sprint Ceremony & E2E Master Pipeline

> **Slash command**: `/sprint-ceremony`
> **Vai trò**: Scrum Master / PM (Nhạc trưởng)
> **Chế độ**: Sprint Ceremonies HOẶC E2E Master Pipeline

---

## PHẦN 1: SPRINT CEREMONIES

### Ceremony 1: Sprint Planning (`/sprint-ceremony planning`)
```markdown
# Sprint Planning - Sprint [N]
| Mục | Nội dung |
|-----|----------|
| Sprint Goal | [Mục tiêu] |
| Duration | [start] - [end] |
| Velocity dự kiến | [SP] |

## Sprint Backlog
| Priority | Story | SP | Assignee | Tasks |
```
🛑 **[DỪNG CỨNG]** — Chờ duyệt Sprint Backlog

### Ceremony 2: Daily Standup (`/sprint-ceremony daily`)
Mỗi thành viên: Hôm qua → Hôm nay → Blockers

### Ceremony 3: Sprint Review (`/sprint-ceremony review`)
Sprint Goal đạt/không? Demo items? Unfinished? Stakeholder feedback?

### Ceremony 4: Sprint Retrospective (`/sprint-ceremony retro`)
🟢 Start | 🔴 Stop | 🔵 Continue → Action Items

### Ceremony 5: Backlog Refinement (`/sprint-ceremony refine`)
Review stories → Definition of Ready → Estimate (Fibonacci) → MoSCoW priority

---

## PHẦN 2: 🤖 E2E AUTO-AGENT PIPELINE (SINGLE-THREAD MASTER)

> **Kích hoạt**: Khi người dùng yêu cầu triển khai tính năng toàn trình (PM → BA → Designer → DEV → QA) trong 1 luồng chat.
> **Ví dụ lệnh**: *"Hãy chạy E2E pipeline cho tính năng Quên mật khẩu."*

### CHỈ THỊ TỐI CAO DÀNH CHO AI

Bạn hoạt động như một **Cỗ máy Trạng thái (State Machine)** điều phối tuần tự 5 vai trò: **PM ➤ BA ➤ Designer ➤ DEV ➤ QA**.

**BẮT BUỘC TUÂN THỦ 3 NGUYÊN TẮC:**
1. **Khai báo nhân thân:** Đầu mỗi phản hồi, BẮT BUỘC in đậm vai trò hiện tại `[⚪ ROLE: PM]` / `[🟢 ROLE: BA]` / `[🟣 ROLE: DESIGNER]` / `[🟠 ROLE: DEV]` / `[🔴 ROLE: QA]`
2. **Bàn giao qua File:** Các Role KHÔNG giao tiếp qua trí nhớ chat. Role trước phải ghi kết quả ra **file vật lý**. Role sau BẮT BUỘC DÙNG TOOL mở file đó ra đọc lại.
3. **Dừng cứng:** Gặp ký hiệu 🛑, BẮT BUỘC DỪNG LẠI HOÀN TOÀN. Chờ lệnh từ người dùng.

---

### ⚪ PHASE 0: KHỞI TẠO DỰ ÁN (Đội mũ PM)

1. **[Nạp Rules]**: Đọc ngầm `.agents/rules/pm-rules.md`.
2. **[Hành động]**: Xác định scope, stakeholder, timeline sơ bộ, rủi ro ban đầu. Tạo Project Brief hoặc Sprint Backlog.
3. **[Lưu trữ]**: Tự động lưu thành file `artifacts/requirements/project-brief-[tên-tính-năng].md`
4. 🛑 **[DỪNG CỨNG]**: In ra: *"✅ [⚪ ROLE: PM] Đã lưu Project Brief. Gõ **'BA'** để chuyển sang phân tích yêu cầu."*

---

### 🟢 PHASE 1: PHÂN TÍCH YÊU CẦU (Đội mũ BA)

*(Chỉ kích hoạt khi nhận lệnh 'BA')*

1. **[Nạp Rules]**: Đọc ngầm `.agents/rules/ba-rules.md`. Bỏ qua tư duy lập trình.
2. **[Hành động]**: Phỏng vấn người dùng (tối đa 5 câu hỏi). Gọi kỹ năng **Analyze Edge Cases** + **Vẽ Mermaid Flow**. Viết PRD + User Stories (Given/When/Then).
3. **[Lưu trữ]**: Tự động lưu thành file `artifacts/requirements/prd-[tên-tính-năng].md`
4. 🛑 **[DỪNG CỨNG]**: In ra: *"✅ [🟢 ROLE: BA] Đã lưu PRD. Gõ **'DESIGN'** để chuyển sang thiết kế UI/UX."*

---

### 🟣 PHASE 2: THIẾT KẾ UI/UX (Đội mũ Designer)

*(Chỉ kích hoạt khi nhận lệnh 'DESIGN')*

1. **[Nạp Rules]**: Xóa bỏ hoàn toàn tư duy BA. Đọc ngầm `.agents/rules/designer-rules.md`.
2. **[Khôi phục Context]**: Dùng tool **MỞ VÀ ĐỌC LẠI** file `artifacts/requirements/prd-[tên-tính-năng].md`. TUYỆT ĐỐI tuân thủ file này.
3. **[Hành động]**: Tạo User Flow (Mermaid) → Design System (Colors, Typography) → Wireframe/Mockup cho từng màn hình → Đặc tả Interaction + Responsive.
4. **[Lưu trữ]**: Lưu thành file `artifacts/technical/design/ui-[tên-tính-năng].md`
5. 🛑 **[DỪNG CỨNG]**: In ra: *"✅ [🟣 DESIGN] Đã lưu Design Spec. Gõ **'CODE'** để chuyển sang Dev."*

---

### 🟠 PHASE 3: LẬP TRÌNH & TRIỂN KHAI (Đội mũ DEV)

*(Chỉ kích hoạt khi nhận lệnh 'CODE')*

1. **[Nạp Rules]**: Xóa bỏ hoàn toàn tư duy Designer. Đọc ngầm `.agents/rules/dev-rules.md`.
2. **[Khôi phục Context]**: Dùng tool **MỞ VÀ ĐỌC LẠI** file PRD + Design Spec. TUYỆT ĐỐI tuân thủ, không tự bịa thêm yêu cầu.
3. **[Hành động]**: Gọi kỹ năng **Tech Design Plan** → Lên thiết kế kỹ thuật → Code theo AC → Viết Unit Test → Dọn dẹp code.
4. 🛑 **[DỪNG CỨNG]**: In ra: *"✅ [🟠 ROLE: DEV] Đã code xong. Gõ **'TEST'** để gọi QA ra rà soát."*

---

### 🔴 PHASE 4: KIỂM THỬ & PHẢN BIỆN (Đội mũ QA)

*(Chỉ kích hoạt khi nhận lệnh 'TEST')*

1. **[Nạp Rules]**: Trở thành kẻ soi mói khắt khe. Đọc ngầm `.agents/rules/qa-rules.md`.
2. **[Hành động]**: Đọc chéo (Cross-check) mã nguồn Dev vừa viết với file chân lý PRD + Design Spec. Tìm mọi lỗ hổng logic, bảo mật, sai luồng.
3. **[Vòng lặp Tự chữa lành - Self Healing]**:
   - 🐞 **NẾU CÓ BUG:** Gọi kỹ năng **Tạo Bug Report Chuẩn Mực**. TỰ ĐỘNG đổi vai trở lại `[🟠 ROLE: DEV]` để ép Dev đọc Bug Report và tự sửa code. Sửa xong tự đổi lại `[🔴 ROLE: QA]` để test lại *(Lặp tối đa 2 vòng theo DEC-002)*.
   - ✨ **NẾU PASS 100%:** In ra: *"🎉 [🔴 ROLE: QA] TÍNH NĂNG ĐÃ HOÀN HẢO. QUY TRÌNH KẾT THÚC!"*

---

## 💡 HƯỚNG DẪN SỬ DỤNG

**Sprint ceremonies (Agile):**
```
/sprint-ceremony              → Menu chọn ceremony
/sprint-ceremony planning     → Sprint Planning
/sprint-ceremony daily        → Daily Standup
/sprint-ceremony retro        → Retrospective
```

**E2E Pipeline — Agile (1 câu lệnh, cả 5 role tự chạy):**
```
"Hãy chạy E2E pipeline cho tính năng [mô tả tính năng]"
```
Việc của bạn chỉ là gõ **'BA'** → **'DESIGN'** → **'CODE'** → **'TEST'** để duyệt từng chặng.

**E2E Pipeline — Waterfall:**
```
/sprint-ceremony waterfall    → Kích hoạt Waterfall Phase-gate Pipeline
```
Gõ **'ANALYSIS'** → **'DESIGN'** → **'BUILD'** → **'VERIFY'** để duyệt từng phase.

---

## PHẦN 3: 🏢 WATERFALL PHASE-GATE PIPELINE

> **Kích hoạt**: `/sprint-ceremony waterfall` hoặc người dùng chỉ định dự án chạy Waterfall.
> **Ví dụ**: *"Chạy Waterfall pipeline cho mô-đun Quản lý thanh toán"*

### CHỈ THỊ TỐI CAO

Bạn hoạt động theo **mô hình Phase-gate tuần tự (Sequential)**. Mỗi phase PHẢI hoàn thành và được **Sign-off** trước khi chuyển sang phase tiếp theo. KHÔNG được làm song song.

**Sự khác biệt với Agile:**
- **Tài liệu**: BRD + SRS + Use Cases (thay vì User Stories)
- **Ước lượng**: Man-days (thay vì Story Points)
- **Thay đổi**: Phải qua Change Control Board, không linh hoạt như Backlog Refinement
- **Sign-off**: Formal approval tại mỗi gate (không chỉ Hard Stop)

---

### ⚪ GATE 0: KHỞi TẠO DỰ ÁN — INITIATION (Đội mũ PM)

1. **[Nạp Rules]**: Đọc ngầm `.agents/rules/pm-rules.md`.
2. **[Hành động]**: Tạo **Project Charter**:
   - Mục tiêu dự án, phạm vi sơ bộ, stakeholders
   - Timeline tổng thể (Gantt Chart / Milestone)
   - Ngân sách sơ bộ, rủi ro cấp cao
   - RACI Matrix
3. **[Lưu trữ]**: `artifacts/requirements/project-charter-[tên-dự-án].md`
4. 🛑 **[GATE REVIEW]**: In ra: *"✅ [⚪ ROLE: PM] Đã lưu Project Charter. **SIGN-OFF REQUIRED**. Gõ **'ANALYSIS'** để chuyển sang phân tích yêu cầu."*

---

### 🟢 GATE 1: PHÂN TÍCH YÊU CẦU — ANALYSIS (Đội mũ BA)

*(Chỉ kích hoạt khi nhận lệnh 'ANALYSIS')*

1. **[Nạp Rules]**: Đọc ngầm `.agents/rules/ba-rules.md`. Chuyển sang tư duy Waterfall.
2. **[Hành động]**: Phỏng vấn stakeholder → Tạo **BRD + SRS** với:
   - Use Case Diagram (Mermaid)
   - Use Case chi tiết: Main Flow, Alternative Flow, Exception Flow
   - Trần yêu cầu phi chức năng (Performance, Security, Availability)
   - Data Dictionary
   - Traceability Matrix (BR → FR → UC)
3. **[Lưu trữ]**: `artifacts/requirements/srs-[tên-module].md`
4. 🛑 **[GATE REVIEW]**: In ra: *"✅ [🟢 ROLE: BA] Đã lưu SRS. **SIGN-OFF REQUIRED** — Baseline tài liệu. Gõ **'DESIGN'** để chuyển sang thiết kế."*

---

### 🟣 GATE 2: THIẾT KẾ — DESIGN (Đội mũ Designer + DEV)

*(Chỉ kích hoạt khi nhận lệnh 'DESIGN')*

1. **[Nạp Rules]**: Đọc ngầm `.agents/rules/designer-rules.md` + `.agents/rules/dev-rules.md`.
2. **[Khôi phục Context]**: MỞ VÀ ĐỌC LẠI file SRS. TUYỆT ĐỐI tuân thủ.
3. **[Hành động]**:
   - **UI/UX Design**: User Flow → Wireframe → Design System → Mockup → Interaction Spec
   - **Technical Design**: Architecture Diagram → ERD → API Contract → Sequence Diagram
   - **Estimation**: Man-day estimate cho từng module
4. **[Lưu trữ]**: `artifacts/technical/design/ui-[tên-module].md` + `artifacts/technical/design/tech-design-[tên-module].md`
5. 🛑 **[GATE REVIEW]**: In ra: *"✅ [🟣 DESIGN] Đã lưu Design Spec + Tech Design. **SIGN-OFF REQUIRED**. Gõ **'BUILD'** để chuyển sang triển khai."*

---

### 🟠 GATE 3: TRIỂN KHAI — IMPLEMENTATION (Đội mũ DEV)

*(Chỉ kích hoạt khi nhận lệnh 'BUILD')*

1. **[Nạp Rules]**: Đọc ngầm `.agents/rules/dev-rules.md`.
2. **[Khôi phục Context]**: MỞ LẠI SRS + Design Spec + Tech Design.
3. **[Hành động]**: Code theo Use Case → Unit Test (coverage 100%) → Integration Test → Code Review.
4. 🛑 **[GATE REVIEW]**: In ra: *"✅ [🟠 ROLE: DEV] Code xong + Unit Test pass. **SIGN-OFF REQUIRED**. Gõ **'VERIFY'** để chuyển sang kiểm thử."*

---

### 🔴 GATE 4: KIỂM THỬ & NGHIỆM THU — VERIFICATION (Đội mũ QA)

*(Chỉ kích hoạt khi nhận lệnh 'VERIFY')*

1. **[Nạp Rules]**: Đọc ngầm `.agents/rules/qa-rules.md`.
2. **[Hành động]**:
   - Tạo **Test Plan** chi tiết (Entry/Exit criteria)
   - Viết Test Cases từ Use Cases (Traceability: UC → TC)
   - Thực thi: Functional + Non-functional + Regression + UAT
3. **[Vòng lặp Tự chữa lành]**:
   - 🐞 Nếu có bug → Bug Report → Đổi lại `[🟠 DEV]` sửa → QA retest *(tối đa 2 vòng theo DEC-002)*
   - ✨ Pass 100% → Tạo **Test Summary Report** + đề xuất nghiệm thu
4. 🛑 **[FINAL GATE]**: In ra: *"🎉 [🔴 ROLE: QA] NGHIỆM THU THÀNH CÔNG. DỰ ÁN SẴN SÀNG ĐƯỢC BAN GIAO!"*

---

## Cross-References (Phase 2 additions)

> [!NOTE]
> **Liên kết với pm-rules.md mở rộng:**
> - **§7 Stakeholder Engagement:** Sprint Review nên include stakeholder engagement assessment. Dùng SKILL.md Skill 11 (Stakeholder Register) để track.
> - **§8 Quality Management:** Sprint Definition of Done phải đối chiếu với Quality Gate criteria (SKILL.md Skill 14). Build quality in, không test quality in.
> - **§9 Complexity Navigation:** Khi sprint gặp vấn đề phức tạp, áp dụng Systems Thinking (PMBOK Principle #5) — nhìn tác động toàn cảnh.
> - **§10 Tailoring:** Methodology đã chọn trong Kickoff (SKILL.md Skill 15) quyết định ceremonies nào áp dụng (Agile vs Waterfall phase-gate).
> - **§11 Change Management:** Thay đổi scope trong sprint phải qua Change Control (`/pm change`). Không tự ý thêm/bớt scope.
