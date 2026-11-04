---
description: Quy trình Change Request - Tự động cập nhật cascading tài liệu dự án khi có thay đổi
---

# Workflow: Change Request & Cascading Document Update

> **Slash command**: `/ba change`
> **Vai trò**: `[🟢 ROLE: BA]`
> **Đầu vào**: Mô tả thay đổi từ người dùng (scope change, bug fix, new feature, requirement change...)
> **Đầu ra**: Tất cả tài liệu liên quan được cập nhật đồng bộ + Change Log

---

## CHỈ THỊ QUAN TRỌNG CHO AI

- **Khai báo nhân thân:** Đầu mỗi phản hồi, BẮT BUỘC in `[🟢 ROLE: BA]`
- **Nạp Rules:** Đọc ngầm `.agents/rules/ba-rules.md` (đặc biệt §7 — Change Management)
- **Dừng cứng:** Gặp ký hiệu 🛑 = BẮT BUỘC DỪNG, chờ người dùng duyệt
- **Đọc trước khi sửa:** TUYỆT ĐỐI KHÔNG sửa file nào mà chưa dùng tool MỞ VÀ ĐỌC LẠI bản hiện tại

---

## Các Bước Thực Hiện

### BƯỚC 1: Tiếp nhận & Phân loại Change Request

1. Hỏi người dùng (nếu chưa rõ):
   - **Thay đổi gì?** (Mô tả cụ thể)
   - **Lý do?** (Tại sao cần thay đổi)
   - **Phạm vi?** (Module/tính năng nào bị ảnh hưởng)
   - **Mức độ khẩn cấp?** (Bình thường / Khẩn cấp)

2. Gán mã CR: `CR-[số thứ tự]` (nếu chưa có)

3. Phân loại mức độ:
   - 🟢 **Minor**: Sửa text, format, typo → Chỉ sửa file chứa lỗi
   - 🟡 **Moderate**: Thêm/sửa flow, field, validation → SRS + Test Cases
   - 🟠 **Major**: Thay đổi scope, thêm/xóa module → BRD + SRS + Test Cases + Timeline
   - 🔴 **Critical**: Thay đổi kiến trúc, tech stack → Tất cả tài liệu

---

## BƯỚC 2: Quét tài liệu hiện tại (Document Scan)

AI **PHẢI** dùng tool đọc lại các file trong dự án để nắm trạng thái hiện tại:

1. **Quét thư mục** `artifacts/requirements/`, `artifacts/technical/design/`, `artifacts/testing/` để liệt kê tất cả tài liệu
2. **Đọc nội dung** các file có khả năng bị ảnh hưởng:
   - If CR is Minor → Chỉ đọc file liên quan trực tiếp
   - If CR is Moderate → Đọc SRS + Test Plan liên quan
   - If CR is Major/Critical → Đọc BRD + SRS + Test Plan + Architecture (nếu có)
3. **Xác định ID liên quan**: Tìm các BR-xxx, FR-xxx, UC-xxx, TC-xxx bị ảnh hưởng

---

## BƯỚC 3: Impact Analysis (Phân tích tác động)

Sinh báo cáo Impact Analysis theo format trong `ba-rules.md` §7, đánh giá **5 chiều**:

1. **Scope** — Phạm vi dự án có thay đổi không?
2. **Tài liệu** — File nào, section nào cần sửa?
3. **Timeline** — Deadline có bị ảnh hưởng không?
4. **Resource** — Cần thêm người/effort không?
5. **Rủi ro** — Có phát sinh rủi ro mới không?

**Output:** Bảng tóm tắt:

```markdown
## 📊 Tóm Tắt Impact Analysis — CR-[ID]
| Chiều | Ảnh hưởng | Chi tiết |
|-------|-----------|----------|
| Scope | Có/Không | [...] |
| Tài liệu | X file | [Danh sách file + section] |
| Timeline | Có/Không | [+Y ngày] |
| Resource | Có/Không | [...] |
| Rủi ro | Có/Không | [...] |
```

🛑 **[DỪNG CỨNG]** — Trình bày Impact Analysis cho người dùng. Hỏi:
*"Đây là phân tích tác động. Xin xác nhận để tôi tiến hành cập nhật tài liệu. Gõ **'UPDATE'** để tiếp tục, hoặc **'CANCEL'** để hủy."*

---

### BƯỚC 4: Cascading Update (Cập nhật lan truyền)

*(Chỉ kích hoạt khi nhận lệnh 'UPDATE')*

Thực hiện cập nhật **TUẦN TỰ** theo chuỗi cascade:

#### 4.1. Cập nhật BRD (nếu scope thay đổi)
- Mở và đọc lại file BRD hiện tại
- Thêm/sửa/xóa `BR-xxx` phù hợp
- Cập nhật "Phạm Vi" (In Scope / Out of Scope)
- Tăng version + ghi Change Log

#### 4.2. Cập nhật SRS
- Mở và đọc lại file SRS hiện tại
- Thêm/sửa/xóa `FR-xxx` hoặc `UC-xxx`
- Cập nhật Acceptance Criteria (Given/When/Then)
- Cập nhật Interface Specification table (nếu có thay đổi UI)
- Tăng version + ghi Change Log

#### 4.3. Cập nhật Test Plan / Test Cases
- Mở và đọc lại file Test Plan hiện tại
- Thêm `TC-xxx` mới cho requirement mới
- Sửa expected result cho requirement đã sửa
- Đánh dấu `[DEPRECATED]` cho test case của requirement đã xóa
- Tăng version + ghi Change Log

#### 4.4. Cập nhật Architecture Document (nếu có và nếu cần)
- Cập nhật component diagram
- Cập nhật API spec
- Cập nhật data model

#### 4.5. Cập nhật Timeline (nếu cần)
- Điều chỉnh milestone
- Ghi chú lý do

---

### BƯỚC 5: Cập nhật Traceability Matrix

- Cập nhật ma trận trace: `BR → FR → UC → TC`
- Đánh dấu các dòng mới thêm / đã sửa / đã xóa
- Đảm bảo KHÔNG CÒN mục nào bị "mồ côi" (orphaned) — tức có BR nhưng không có FR/TC tương ứng

---

### BƯỚC 6: Tổng kết & Lưu trữ

1. **Cập nhật Change Log tổng hợp** tại `artifacts/requirements/change-log.md` (tạo mới nếu chưa có):

```markdown
| CR ID | Ngày | Phân loại | Mô tả | Tài liệu đã cập nhật | Trạng thái |
|-------|------|-----------|-------|----------------------|------------|
| CR-XXX | [DD/MM/YYYY] | [Mức độ] | [Mô tả] | [Danh sách file đã sửa + version mới] | ✅ Hoàn thành |
```

2. **Tổng kết cho người dùng:**

```markdown
## ✅ Change Request CR-[ID] đã hoàn tất

### Tài liệu đã cập nhật:
| # | Tài liệu | File | Version cũ → mới | Thay đổi chính |
|---|----------|------|-------------------|----------------|
| 1 | BRD | brd-xxx.md | 1.0 → 1.1 | Thêm BR-005 |
| 2 | SRS | srs-xxx.md | 1.2 → 1.3 | Thêm UC-10, FR-015 |
| 3 | Test Plan | test-plan-xxx.md | 1.0 → 1.1 | Thêm TC-020~025 |
```

🛑 **[DỪNG CỨNG]** — In ra:
*"✅ [🟢 ROLE: BA] Change Request CR-[ID] đã hoàn tất. Tất cả tài liệu đã được cập nhật đồng bộ. Xin kiểm tra các file đã sửa."*

---

## 💡 HƯỚNG DẪN SỬ DỤNG

### Cách 1: Lệnh trực tiếp
```
/ba change
```
AI sẽ hỏi bạn mô tả thay đổi.

### Cách 2: Kèm mô tả
```
/ba change Thêm tính năng thanh toán QR vào module Bán hàng
```
AI sẽ bắt đầu phân tích ngay.

### Cách 3: Kèm context
```
/ba change
- Thay đổi: Bỏ tính năng Chat, thay bằng Chatbot AI
- Lý do: Khách hàng yêu cầu
- Module: CSKH
- Khẩn cấp: Không
```

### Lệnh điều khiển
| Lệnh | Hành động |
|-------|-----------|
| `UPDATE` | Xác nhận và bắt đầu cập nhật tài liệu |
| `CANCEL` | Hủy Change Request |
| `SKIP [loại tài liệu]` | Bỏ qua cập nhật 1 loại tài liệu cụ thể |
| `ROLLBACK CR-[ID]` | Hoàn tác Change Request đã thực hiện |
