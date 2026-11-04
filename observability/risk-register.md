# Risk Register (Sổ Theo Dõi & Quản Trị Rủi Ro Dự Án)

> **Mục tiêu:** Nhận diện sớm, đánh giá định lượng và thiết lập phương án ứng phó cho các rủi ro kỹ thuật, nghiệp vụ, pháp lý và vận hành.

---

## 1. Bảng Đăng Ký Rủi Ro

| Mã Rủi Ro | Danh mục | Mô tả rủi ro | Xác suất (1-5) | Tác động (1-5) | Điểm rủi ro (P×I) | Biện pháp ứng phó / Giảm thiểu | Người phụ trách | Trạng thái |
|---|---|---|:---:|:---:|:---:|---|---|:---:|
| **RSK-001** | Kỹ thuật | Nghẽn mạng SMS Gateway của nhà mạng viễn thông sát giờ quay thưởng (17h30 - 17h45) | 4 | 5 | **20 (Rất cao)** | Thiết lập Priority Queue cho SMS OTP và nén nội dung tin nhắn MT | Tech Lead | Đang theo dõi |
| **RSK-002** | Pháp lý | Rò rỉ dữ liệu cá nhân (PII) người chơi vi phạm Nghị định 13/2023/NĐ-CP | 2 | 5 | **10 (Cao)** | Ép buộc PII Scanner trong lifecycle hooks, mã hóa AES-256 các trường CCCD/SĐT | Governance | Đã kiểm soát |
| **RSK-003** | Nghiệp vụ | Sai lệch số dư đối soát giữa tài khoản dự thưởng và cổng thanh toán đối tác | 2 | 4 | **8 (Trung bình)** | Chạy đối soát tự động hàng đêm, có cơ chế đối soát 3 bên (Vietlott - Napas - Bank) | DA & Kế toán | Đã kiểm soát |
| **RSK-004** | Quy trình | Agent tự ý ký duyệt baseline hoặc tự quyết định NFR mà không có Human sign-off | 2 | 4 | **8 (Trung bình)** | Cưỡng chế điểm dừng 🛑 Hard Stop và kiểm tra permission matrix | Governance | Đã kiểm soát |
