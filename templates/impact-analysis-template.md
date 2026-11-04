# Change Request Impact Analysis — [Tên Yêu Cầu Thay Đổi]

> **Mã CR:** CR-[CODE] | **Mã phân tích:** IA-[CODE]  
> **Người thực hiện:** Business Analyst (BA) | **Ngày phân tích:** YYYY-MM-DD  
> **Mức độ tác động:** [Thấp / Trung bình / Cao / Khẩn cấp]

---

## 1. Mô Tả Yêu Cầu Thay Đổi (Change Description)
- **Nguồn gốc đề xuất:** [Khách hàng / Stakeholder / Đối tác Ngân hàng / Pháp lý]
- **Yêu cầu hiện tại (As-Is):** ...
- **Yêu cầu thay đổi (To-Be):** ...
- **Lý do cần thay đổi:** ...

---

## 2. Ma Trận Đánh Giá Tác Động (Impact Matrix)

| Lĩnh vực tác động | Mức độ (1-5) | Chi tiết hệ thống / Tài liệu bị ảnh hưởng | Hành động cần thiết |
|---|:---:|---|---|
| **Business Logic** | ... | Quy tắc tính thưởng, hạn mức giao dịch | Cập nhật `knowledge/business-rules/` |
| **API & Database** | ... | Schema bảng giao dịch, thêm trường `bank_code` | DEV migration DB & cập nhật API spec |
| **UI/UX App** | ... | Màn hình chọn phương thức thanh toán | Designer cập nhật Figma & UI spec |
| **Testing & QA** | ... | Cần cập nhật 15 test cases liên quan | QA cập nhật Test Plan & Regression suite |
| **Hệ thống ngoại vi** | ... | Cổng thanh toán Napas / SMS Gateway | Gửi thông báo đối tác và test sandbox |

---

## 3. Điểm Đánh Giá Tác Động Tổng Thể (Impact Score)
- **Công thức:** `Impact Score = (Phạm vi × 0.3) + (Kỹ thuật × 0.3) + (Rủi ro × 0.4)`
- **Điểm số:** `X / 5.0`
- **Kết luận:** [Thay đổi nhỏ (Minor) / Thay đổi lớn (Major) cần họp CAB]

---

## 4. Kế Hoạch Đồng Bộ Xuyên Suốt (Cascading Update Plan)
- [ ] Bước 1: Cập nhật tài liệu SRS tại `artifacts/requirements/`
- [ ] Bước 2: Thông báo DEV review tính khả thi kỹ thuật
- [ ] Bước 3: Cập nhật kịch bản kiểm thử tại `artifacts/testing/`
- [ ] Bước 4: Trình Human phê duyệt tại điểm 🛑 Hard Stop
