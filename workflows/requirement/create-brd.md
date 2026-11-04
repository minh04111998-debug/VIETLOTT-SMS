---
description: Quy trình tạo Business Requirements Document (BRD) - Vai trò BA (Waterfall)
---

# Workflow: Tạo BRD (Business Requirements Document)

> **Slash command**: `/create-brd`
> **Vai trò**: `[🟢 ROLE: BA]`
> **Methodology**: Waterfall / Phase-gate
> **Đầu vào**: Thông tin nghiệp vụ từ stakeholder, tài liệu yêu cầu gốc
> **Đầu ra**: File BRD hoàn chỉnh tại `artifacts/requirements/brd-[tên-dự-án].md`

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo nhân thân:** Đầu mỗi phản hồi, BẮT BUỘC in `[🟢 ROLE: BA]`
- **Nạp Rules:** Đọc ngầm `.agents/rules/ba-rules.md` (Mindset: Tech-Agnostic, No Hallucination)
- **Nạp Skills:** Sẵn sàng gọi `.agents/skills/ba/SKILL.md`
- **Dừng cứng:** Gặp ký hiệu 🛑 = BẮT BUỘC DỪNG, chờ người dùng
- **Phân biệt BRD vs PRD:**
  - **BRD** = Tài liệu yêu cầu **nghiệp vụ** (Business-focused, cho Waterfall). Mô tả CÁI GÌ cần đạt từ góc nhìn kinh doanh.
  - **PRD** = Tài liệu yêu cầu **sản phẩm** (Product-focused, cho Agile). Mô tả sản phẩm cần xây dựng.

---

## Các Bước Thực Hiện

### BƯỚC 1: Thu nhập thông tin nghiệp vụ

- If has input file: Dùng tool **MỞ VÀ ĐỌC LẠI** file đó. TUYỆT ĐỐI tuân thủ.
- If not: Phỏng vấn người dùng bằng bộ câu hỏi sắc bén (**TỐI ĐA 7 CÂU HỎI**):

  **Nhóm 1 — Bối cảnh kinh doanh:**
  1. Vấn đề kinh doanh / cơ hội cần giải quyết là gì?
  2. Mục tiêu kinh doanh cụ thể (KPIs)?
  3. Ai là các bên liên quan chính (Stakeholders)?

  **Nhóm 2 — Phạm vi & Ràng buộc:**
  4. Phạm vi dự án bao gồm những gì? Loại trừ những gì?
  5. Ràng buộc: Timeline, ngân sách, pháp lý, kỹ thuật?

  **Nhóm 3 — Quy trình nghiệp vụ:**
  6. Quy trình nghiệp vụ hiện tại (As-Is) ra sao? Pain points?
  7. Quy trình mong muốn (To-Be) khác gì?

- 🛑 **[DỪNG CỨNG]** — Chờ người dùng trả lời các câu hỏi

---

### BƯỚC 2: Phân tích Gap & Mô hình hóa

- Tổng hợp câu trả lời từ Bước 1
- Gọi kỹ năng **Gap Analysis** (As-Is vs To-Be) để tạo bảng gap
- Gọi kỹ năng **Vẽ Mermaid Flow** để vẽ:
  - **Business Process Flow** (luồng nghiệp vụ tổng quan)
  - **Stakeholder Map** (ma trận Power/Interest nếu phức tạp)
- Gọi kỹ năng **Analyze Edge Cases** để quét rủi ro nghiệp vụ
- 🛑 **[DỪNG CỨNG]** — In Gap Analysis + Diagrams. Hỏi: *"Phân tích này đã chính xác chưa? Có gap nào bị thiếu không?"*

---

### BƯỚC 3: Viết BRD theo template chuẩn

Dựa trên thông tin đã chốt, viết BRD theo format sau:

```markdown
# Tài Liệu Yêu Cầu Nghiệp Vụ (BRD)

## 1. Thông Tin Chung
| Mục | Nội dung |
|-----|----------|
| Tên dự án | [Tên] |
| Mã dự án | [Mã] |
| Phiên bản | 1.0 |
| Ngày tạo | [DD/MM/YYYY] |
| Tác giả | [Tên BA] |
| Trạng thái | Nháp |

## 2. Tóm Tắt Điều Hành (Executive Summary)
[1-2 đoạn tóm tắt vấn đề, giải pháp, và giá trị mong đợi]

## 3. Mục Tiêu Nghiệp Vụ
| # | Mục tiêu | KPI đo lường | Giá trị mục tiêu |
|---|----------|--------------|-------------------|

## 4. Phạm Vi
| Khía cạnh | Phạm vi chi tiết |
|-----------|------------------|
| **Trong phạm vi (In Scope)** | [Chi tiết] |
| **Ngoài phạm vi (Out of Scope)** | [Chi tiết] |
| **Giả định (Assumptions)** | [Chi tiết] |
| **Ràng buộc (Constraints)** | [Chi tiết] |

## 5. Các Bên Liên Quan (Stakeholders)
| Tên | Vai trò | Mức độ ảnh hưởng (Power) | Mức quan tâm (Interest) | Kỳ vọng |
|-----|---------|--------------------------|-------------------------|---------|

## 6. Yêu Cầu Nghiệp Vụ Chi Tiết
### BR-001: [Tên yêu cầu]
- **Mô tả**: [Chi tiết]
- **Lý do nghiệp vụ**: [Tại sao cần - Business justification]
- **Độ ưu tiên**: Must have / Should have / Could have / Won't have
- **Tiêu chí thành công**: [Cách đo lường]
- **Quy tắc nghiệp vụ liên quan**: [BRU-xxx nếu có]
- **Tài liệu tham chiếu**: [Link/nguồn]

## 7. Quy Tắc Nghiệp Vụ (Business Rules)
| ID | Quy tắc | Mô tả chi tiết | Ảnh hưởng | Nguồn |
|----|---------|----------------|-----------|-------|

## 8. Phân Tích Gap (As-Is vs To-Be)
| # | Khía cạnh | As-Is (Hiện tại) | To-Be (Mong muốn) | Gap | Giải pháp đề xuất |
|---|----------|-------------------|-------------------|-----|-------------------|

## 9. Luồng Nghiệp Vụ (Business Process Flow)
[Mermaid diagrams]

## 10. Yêu Cầu Phi Chức Năng (High-level)
### 10.1. Hiệu năng
### 10.2. Bảo mật & Tuân thủ
### 10.3. Khả dụng
### 10.4. Tích hợp

## 11. Rủi Ro & Biện Pháp Giảm Thiểu
| ID | Rủi ro | Xác suất | Tác động | Mức độ | Biện pháp |
|----|--------|----------|----------|--------|-----------|

## 12. Timeline & Milestone (Sơ bộ)
| Phase | Milestone | Thời gian dự kiến | Deliverable |
|-------|-----------|-------------------|-------------|

## 13. Ngân Sách Sơ Bộ (nếu có)

## 14. Phê Duyệt
| Vai trò | Tên | Chữ ký | Ngày |
|---------|-----|--------|------|

## 15. Lịch Sử Thay Đổi
| Phiên bản | Ngày | Người thay đổi | Mô tả thay đổi |
|-----------|------|----------------|-----------------|
| 1.0 | [DD/MM/YYYY] | [Tên] | Tạo mới |
```

- **Mỗi BR-xxx** PHẢI có Business Justification (lý do nghiệp vụ)
- **Mỗi BR-xxx** PHẢI map được với ít nhất 1 Business Rule (BRU) hoặc KPI
- 🛑 **[DỪNG CỨNG]** — Trình bày BRD draft để review

---

### BƯỚC 4: Tạo Traceability Matrix sơ bộ

- Liên kết: BR → (sẽ map FR/UC khi làm SRS)
- Đảm bảo mọi mục tiêu nghiệp vụ đều được cover bởi ít nhất 1 BR

```markdown
| Mục tiêu KV | BR ID | Trạng thái | Ghi chú |
|-------------|-------|------------|---------|
| [KPI 1] | BR-001, BR-002 | ✅ Covered | |
| [KPI 2] | BR-003 | ⚠️ Partial | Cần bổ sung |
```

---

### BƯỚC 5: Lưu trữ & Baseline

- Lưu file BRD **nháp** tại `artifacts/requirements/brd-[tên-dự-án].md`
- Ghi nhận lịch sử thay đổi
- 🛑 **[DỪNG CỨNG]** — In ra: *"✅ [🟢 ROLE: BA] BRD nháp đã lưu tại `artifacts/requirements/`. Phê duyệt để tôi chuyển sang `artifacts/requirements/` và baseline?"*
- Sau khi được phê duyệt → **Chuyển file** từ `artifacts/requirements/` sang `artifacts/requirements/brd-[tên-dự-án].md`
- Thông báo: *"BRD đã baseline. Bước tiếp theo: chạy `/create-srs` để viết SRS chi tiết từ BRD này."*

---

## 💡 SỰ KHÁC BIỆT VS `/create-prd`

| Tiêu chí | `/create-brd` (Waterfall) | `/create-prd` (Agile) |
|----------|--------------------------|----------------------|
| **Góc nhìn** | Nghiệp vụ (Business) | Sản phẩm (Product) |
| **Đối tượng đọc** | Ban lãnh đạo, Sponsor, PMO | Dev Team, PO |
| **Nội dung chính** | BR-xxx, Business Rules, Gap Analysis | User Stories, Acceptance Criteria |
| **Ước lượng** | Man-days, ngân sách | Story Points |
| **Thay đổi** | Change Control Board | Backlog Refinement |
| **Output tiếp theo** | → SRS (`/create-srs`) | → Code (`/code-review`) hoặc Design (`/create-ui-design`) |
