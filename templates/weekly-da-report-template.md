# Báo Cáo Định Kỳ Số Liệu Kinh Doanh Vietlott SMS — Tuần [SỐ] / Năm [NĂM]

> **Tác giả:** Data Analyst (DA) | **Thời gian phân tích:** YYYY-MM-DD đến YYYY-MM-DD  
> **Nguồn dữ liệu:** PowerBI Model, Core Reporting DB, Báo cáo đối soát Telco

---

## 1. Tóm Tắt Chỉ Số Hoạt Động Cốt Lõi (Executive KPI Dashboard)

| Chỉ số (KPI) | Thực tế kỳ này | Kỳ trước (WoW) | Cùng kỳ năm trước (YoY) | Đánh giá xu hướng |
|---|---|---|---|:---:|
| **Tổng Doanh Thu (VND)** | ... tỷ | +...% | +...% | 🟢 Tăng trưởng |
| **Số Lượng Vé Bán Ra** | ... vé | +...% | +...% | 🟢 Tăng trưởng |
| **Người Dùng Hoạt Động (WAU)** | ... user | -...% | +...% | 🟡 Cảnh báo giảm nhẹ |
| **Giá Trị Đơn Trung Bình (AOV)** | ... VND | +...% | +...% | 🟢 Ổn định |

---

## 2. Phân Tích Biến Động Theo Dòng Sản Phẩm (Product Variance Analysis)
- **Mega 6/45 & Power 6/55:** Tác động của giá trị giải Jackpot lên số lượng người chơi mới.
- **Keno & Bingo18:** Tỷ lệ duy trì (Retention) của nhóm người chơi quay nhanh trong các khung giờ vàng (11h30-13h00 và 19h00-21h00).

---

## 3. Phân Tích Kênh Thanh Toán & Nạp Tiền
- Tỷ trọng doanh thu theo từng kênh: VNPT Money (...%), Viettel Money (...%), ZaloPay (...%), App Ngân Hàng (...%).
- Tỷ lệ giao dịch lỗi / timeout tại cổng ngân hàng.

---

## 4. Key Insights & Khuyến Nghị Hành Động (Data Storytelling)
1. **Insight 1:** Người chơi có xu hướng tăng mua vé Keno vào ngày Chủ Nhật khi không có kỳ quay Power 6/55.
   - *Khuyến nghị cho PO/Marketing:* Tung chương trình khuyến mại tặng vé Keno vào khung giờ trưa Chủ Nhật.
2. **Insight 2:** Tỷ lệ drop-off tại bước thanh toán qua Bank Gateway tăng 3% do chậm trễ nhận SMS OTP.
   - *Khuyến nghị cho DEV/Ops:* Kiểm tra latency kết nối mạng viễn thông.
