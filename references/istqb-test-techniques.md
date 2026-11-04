# ISTQB Test Design Techniques — Kỹ Thuật Thiết Kế Kiểm Thử Chuẩn

> **Tổ chức:** International Software Testing Qualifications Board (ISTQB)  
> **Áp dụng cho:** QA Agent trong việc thiết kế Test Cases, kiểm tra biên và kịch bản lỗi.

---

## 1. Các Kỹ Thuật Hộp Đen Cốt Lõi (Black-Box Techniques)

1. **Phân Vùng Tương Đương (Equivalence Partitioning - EP):**
   - Chia miền giá trị đầu vào thành các phân vùng hợp lệ (Valid) và không hợp lệ (Invalid).
   - *Ví dụ Vietlott SMS:* Mua vé Mega 6/45:
     - Hợp lệ: Chọn đúng 6 số khác nhau trong khoảng [01, 45].
     - Không hợp lệ: Chọn ít hơn 6 số, chọn nhiều hơn 6 số, chọn trùng số, chọn số < 01 hoặc > 45.

2. **Phân Tích Giá Trị Biên (Boundary Value Analysis - BVA):**
   - Kiểm tra tại các điểm biên: Min, Min-1, Min+1, Max, Max-1, Max+1.
   - *Ví dụ hạn mức giao dịch:* Hạn mức nạp tiền tối thiểu 10,000 VND, tối đa 50,000,000 VND / ngày.
     - Test points: 9,999 VND (Fail), 10,000 VND (Pass), 10,001 VND (Pass), 49,999,999 VND (Pass), 50,000,000 VND (Pass), 50,000,001 VND (Fail).

3. **Bảng Quyết Định (Decision Table Testing):**
   - Áp dụng khi logic nghiệp vụ chứa nhiều điều kiện kết hợp (AND/OR).
   - *Ví dụ:* Điều kiện tự động nhận thưởng: (Tài khoản đã eKYC = TRUE) AND (Trúng giải <= 10 tỷ) AND (Số dư TKDT + Thưởng <= HMDT) -> Thực hiện chi thưởng tự động.

4. **Kiểm Thử Chuyển Đổi Trạng Thái (State Transition Testing):**
   - Kiểm thử vòng đời trạng thái của vé và giao dịch (Init -> Pending -> Success/Failed -> Refunded).
