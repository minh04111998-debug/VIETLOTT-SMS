# 🚫 Banned Words — Từ Cấm Trong Đặc Tả Kỹ Thuật

> **Nguồn:** ISO/IEC/IEEE 29148 — "Well-formed requirements", BABOK® v3 §4
> **Mục đích:** AI PHẢI quét output trước khi trình user. Nếu phát hiện từ cấm → thay thế hoặc gắn nhãn `[⚠️ MƠ HỒ]`.
> **Script hỗ trợ:** `validators/ambiguity_scanner.py`

---

| Từ/Cụm từ CẤM | Tại sao cấm | Thay thế bằng |
|----------------|-------------|---------------|
| nhanh chóng | Không đo lường được | Trong vòng X giây / ms |
| thân thiện | Chủ quan, không test được | Tuân thủ WCAG 2.1 AA, touch target ≥ 44px |
| dễ dàng, dễ sử dụng | Chủ quan | Hoàn thành trong ≤ N bước, không cần hướng dẫn |
| tối ưu | Không rõ tiêu chí | Đạt throughput ≥ X req/s, latency ≤ Y ms |
| tự động | Mơ hồ scope | Hệ thống tự thực hiện [hành động cụ thể] khi [điều kiện cụ thể] |
| TBD, sẽ bổ sung | Thiếu cam kết | `[❓ OPEN — cần làm rõ trước sprint X]` |
| tương tự, giống như | Thiếu truy xuất | Tuân theo spec [ID cụ thể], mục [X.Y] |
| hệ thống xử lý | Quá chung chung | [Tên module/service cụ thể] thực hiện [hành động] |
| và/hoặc | Logic mơ hồ | Tách thành 2 requirement riêng biệt |
| v.v., etc. | Mở rộng vô hạn | Liệt kê đầy đủ hoặc ghi rõ "Chỉ gồm: [danh sách]" |
| đầy đủ | Không xác định phạm vi | Bao gồm [danh sách cụ thể các mục] |
| phù hợp | Chủ quan | Thỏa mãn [tiêu chí đo lường cụ thể] |
| kịp thời | Không đo lường được | Trong vòng X phút/giờ kể từ [sự kiện trigger] |
| an toàn | Quá rộng | Tuân thủ [chuẩn bảo mật cụ thể: NĐ 2345, PCI-DSS...] |
| hiệu quả | Chủ quan | Giảm X% thời gian xử lý, tăng Y% conversion rate |
