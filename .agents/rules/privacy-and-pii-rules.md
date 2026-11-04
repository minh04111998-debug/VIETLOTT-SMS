# Privacy & PII Protection Rules (Quy Định Bảo Vệ Dữ Liệu Cá Nhân)

> **Căn cứ:** Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân  
> **Áp dụng:** Bắt buộc cho toàn bộ tài liệu, logs, prompt và artifacts sinh ra bởi AI.

---

## 1. Dữ Liệu Cá Nhân Nhạy Cảm (PII) Bị Cấm Tuyệt Đối Ghi Rõ (Strict Masking)

1. **Số điện thoại khách hàng (MSISDN):**
   - Chỉ được hiển thị dạng masked: `091****888` hoặc `8490****123`.
   - Tuyệt đối không ghi số điện thoại thực của người chơi vào các tài liệu PRD, SRS, Test Case hoặc Log.
2. **Số Căn cước công dân (CCCD / CMND):**
   - Bắt buộc masked: `001099******` (chỉ hiển thị 6 số đầu, ẩn các số đuôi).
3. **Số tài khoản ngân hàng / Số thẻ:**
   - Chỉ hiển thị 4 số cuối: `**** **** **** 1234`.
4. **Mã OTP và Mật khẩu / Mã PIN:**
   - **TUYỆT ĐỐI CẤM** ghi lại mã OTP thực trong bất kỳ file log hoặc báo cáo nào.

---

## 2. Quy Định Đối Với AI Agent

- Nếu phát hiện file dữ liệu đầu vào chứa thông tin nhạy cảm chưa được ẩn danh, AI **PHẢI** tự động ẩn danh hóa trước khi đưa vào các bước phân tích tiếp theo.
- Không đưa thông tin nhạy cảm của khách hàng thật vào các ví dụ minh họa hoặc file mẫu.
