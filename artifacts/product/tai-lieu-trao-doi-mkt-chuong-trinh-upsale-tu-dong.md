# TÀI LIỆU TRAO ĐỔI NGHIỆP VỤ VỚI MARKETING
## TÍNH NĂNG: CHIẾN DỊCH TỰ ĐỘNG TẶNG QUÀ UPSALE CHO KHÁCH HÀNG HIỆN HỮU

> **Mã tài liệu:** `BA-DISCUSS-UPSALE-MKT-01`  
> **Phiên bản:** `v1.0 (Draft)`  
> **Ngày lập:** 13/10/2026  
> **Người lập:** Senior Business Analyst (BA)  
> **Đơn vị nhận:** Bộ phận Marketing (Đầu mối: Chị Phạm Hoàng Thư - Trưởng nhóm Marketing)  
> **Căn cứ tài liệu:** Phiếu yêu cầu tính năng tại [TÍnh năng Chương trình tự động tặng quà upsale.xlsm](file:///f:/VIETLOTT-SMS/artifacts/product/TÍnh năng Chương trình tự động tặng quà upsale.xlsm)

---

## 1. MỤC ĐÍCH CUỘC HỌP & NGUYÊN TẮC THỐNG NHẤT

### 1.1. Mục đích cuộc họp
1. Thống nhất mô hình nghiệp vụ của hệ thống Upsale tự động nhằm thay thế quy trình vận hành thủ công (xuất file Excel, lọc danh sách và trao quà bằng tay).
2. Phân tích chi tiết 6 kịch bản kích cầu, làm rõ "Điểm neo kích hoạt" và cơ chế thực thi (Real-time vs Batch Scheduler).
3. Lấy ý kiến chốt (Sign-off) cho 8 câu hỏi mở (Open Questions) để hoàn thiện bản đặc tả yêu cầu phần mềm (SRS).

### 1.2. Ba nguyên tắc kiến trúc đã được thống nhất
1. **Kế thừa Concept quản trị:** Thừa hưởng toàn bộ khung vận hành đang chạy trên Production của chương trình Đăng ký mới (Vòng đời chiến dịch, Phân quyền duyệt Maker/Checker, Quản lý kho mã quà, Quản lý hạn mức ngày và ngân sách tổng, Kênh gửi tin nhắn VLT Notification).
2. **Tách riêng thành Chức năng độc lập:** Xây dựng module Web Admin riêng, cơ sở dữ liệu riêng, Background Worker riêng và Hệ thống báo cáo riêng. Không can thiệp vào code của luồng tặng quà khách hàng đăng ký mới để bảo đảm tỷ lệ lỗi phát sinh bằng 0 trên luồng hiện hữu.
3. **Mỗi Chiến dịch cấu hình 01 Kịch bản mục tiêu:** Nhằm minh bạch ngân sách, đo lường chính xác chỉ số ROI cho từng kịch bản, và bảo vệ Database Core Bán Vé không bị quá tải. Quy tắc *"Ưu tiên kịch bản giảm dần"* được giải quyết bằng trường **Mức độ ưu tiên (Priority)** khi có ≥ 2 chiến dịch cùng chạy đồng thời.

---

## 2. MA TRẬN 6 KỊCH BẢN CHI TIẾT: ĐIỂM NEO & CƠ CHẾ XỬ LÝ

| STT | Tên Kịch Bản | Điểm Neo Kích Hoạt (Trigger Anchor) | Cơ Chế Xử Lý Kỹ Thuật | Thời Điểm Xét Duyệt & Trao Quà | Tác Động Tải Database |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **KB 1A** | **Win-Back: Tặng thẳng không cần mua** | Điều kiện số ngày không mua vé: `Ngày hiện tại - Ngày mua Game X gần nhất ≥ N ngày`. | **Batch Scheduler Job** (Quét ngầm theo lịch). | 08:30 sáng hàng ngày. Quét tệp user ngủ đông, tự động gán mã quà vào ví và gửi tin nhắn VLT Notification. | Tải CPU DB < 15% do chạy khung giờ thấp điểm, phân trang 1.000 bản ghi/lô. |
| **KB 1B** | **Win-Back: Mua lại Game X mới tặng** | Sự kiện thanh toán mua vé Game X thành công (`EVENT_ORDER_SUCCESS_GAME_X`). | **Real-time Event Engine** (Sự kiện tức thời). | Tức thời ngay sau khi giao dịch mua vé hoàn tất (độ trễ ≤ 2 giây). | Nhẹ (tra cứu cờ trạng thái trong User Profile Cache). |
| **KB 2** | **Ngưỡng chi tiêu tối thiểu X đồng** | Sự kiện giao dịch mua vé làm tổng chi tiêu chạm mốc `>= X VNĐ`. | **Real-time Event Engine** (Cộng dồn gia tăng). | Tức thời ngay khi thanh toán đơn hàng đạt mốc chi tiêu. | Cực nhẹ (dùng bộ đếm gia tăng `spent_counter += order.amount`, không quét SUM). |
| **KB 3** | **Lượt vé tích lũy đạt X lượt** | Sự kiện thanh toán thành công đơn hàng chứa lượt vé thứ X. | **Real-time Event Engine** (Cộng dồn gia tăng). | Tức thời ngay khi hoàn tất lượt vé thứ X. | Cực nhẹ (tăng biến đếm `ticket_counter += 1`, không quét COUNT). |
| **KB 4A** | **Bán chéo Game 1-1: Mua Game Y mới tặng** | Sự kiện khách hàng phát sinh đơn hàng mua Game Y lần đầu tiên. | **Real-time Event Engine**. | Tức thời ngay lúc thanh toán đơn hàng Game Y đầu tiên. | Nhẹ (kiểm tra điều kiện `has_bought_game_y == false`). |
| **KB 4B** | **Bán chéo Game 1-1: Tặng thẳng chơi thử** | Khách hàng thuộc tệp `Đã mua Game X VÀ Chưa từng mua Game Y`. | **Batch Scheduler Job** (Quét ngầm theo lịch). | Chạy định kỳ đầu tuần hoặc định kỳ theo lịch chiến dịch. | Tải thấp do quét trên cơ sở dữ liệu phân tích. |
| **KB 5** | **Bán chéo 1-N: Đa dạng hóa game** | Tương tự KB 4 nhưng áp dụng khi khách hàng chỉ chơi duy nhất 1 game và mua thêm game bất kỳ khác. | **Real-time** (nếu mua) HOẶC **Batch** (nếu tặng thẳng). | Tức thời khi mua game mới, hoặc quét Batch định kỳ nếu tặng thẳng. | Kiểm soát qua cờ danh mục sản phẩm. |
| **KB 6A** | **Ngày trong tuần: Mua vé Thứ Y mới tặng** | Giao dịch mua vé thành công phát sinh vào đúng ngày Thứ Y chỉ định. | **Real-time Event Engine**. | Tức thời khi giao dịch phát sinh vào đúng ngày Thứ Y. | Cực nhẹ (kiểm tra `DAYOFWEEK(now) == Thứ Y`). |
| **KB 6B** | **Ngày trong tuần: Tặng thẳng sáng Thứ Y** | Mốc thời gian hệ thống chạm 08:00 sáng ngày Thứ Y. | **Batch Scheduler Job**. | Đúng 08:00 sáng Thứ Y, phát quà vào ví để kéo khách hàng mở app mua vé. | Tải thấp (quét tệp khách hàng quen mua các thứ khác). |
| **KB 7** | **Tái tặng quà (Re-gifting)** | Mã quà cũ rơi vào trạng thái `EXPIRED` (Hết hạn lúc 23:59:59). | **Batch Scheduler Job** (Chạy hàng ngày). | 00:05 sáng hàng ngày, quét mã hết hạn, kiểm tra số lần đã tặng lại và thời gian chờ để cấp mã mới. | Tải thấp (chạy lúc 00:05). |

---

## 3. DANH SÁCH 8 CÂU HỎI MỞ CẦN MARKETING CHỐT (OPEN QUESTIONS)

| STT | Vấn Đề Nghiệp Vụ Cần Làm Rõ | Đề Xuất Của BA | Tác Động Nếu Không Chốt | Ý Kiến Phản Hồi Của Marketing |
| :---: | :--- | :--- | :--- | :--- |
| **Q1** | **Phạm vi lịch sử (Historical Lookback Window):**<br>Điều kiện *"Chưa từng mua Game Y"* hoặc *"Đã từng mua Game X"* được quét trong mốc thời gian bao lâu? | **Phương án đề xuất:** Giới hạn tối đa **180 ngày gần nhất** (hoặc cho phép cấu hình ô nhập: 30, 60, 90, 180 ngày). Không quét toàn bộ lịch sử từ ngày tạo tài khoản. | Nếu quét toàn bộ lịch sử trên 365 ngày, thời gian chạy Job sẽ kéo dài > 4 giờ và gây nghẽn tài nguyên hệ thống. | `[Chờ MKT xác nhận]` |
| **Q2** | **Quy tắc tính Chi tiêu tối thiểu X đồng (Kịch bản 2):**<br>Tính trên **từng đơn hàng đơn lẻ** hay **cộng dồn** trong suốt thời gian diễn ra chiến dịch? | **Phương án đề xuất:** Hỗ trợ cả 2 dạng qua ô chọn Radio trên Admin:<br>- *Dạng 1:* Một đơn hàng ≥ X VNĐ.<br>- *Dạng 2:* Tổng chi tiêu tích lũy trong kỳ ≥ X VNĐ. | Tránh tranh cãi khi khách hàng thắc mắc tại sao mua ≥ 2 đơn hàng đạt tổng số tiền nhưng không được nhận quà. | `[Chờ MKT xác nhận]` |
| **Q3** | **Cơ chế phân bổ cho kịch bản "Tặng thẳng không cần mua":**<br>Khi số lượng khách hàng đạt điều kiện vượt quá Hạn mức ngày (`Daily_Cap`), hệ thống sẽ ưu tiên tặng quà cho ai? | **Phương án đề xuất:** Ưu tiên theo nguyên tắc **First-Come, First-Served** (xếp theo thời gian đăng ký tài khoản sớm hơn hoặc thời gian đạt điều kiện sớm hơn). Phần còn lại chuyển sang ngày tiếp theo. | Tránh việc khiếu nại không minh bạch khi ngân sách ngày bị hết sớm. | `[Chờ MKT xác nhận]` |
| **Q4** | **Quy tắc chống nhận trùng quà (Anti-Stacking Policy):**<br>Một khách hàng có được nhận quà từ ≥ 2 chiến dịch Upsale khác nhau trong cùng một chu kỳ thời gian không? | **Phương án đề xuất:** Trong vòng **30 ngày**, một khách hàng chỉ được nhận tối đa **01 mã quà tặng Upsale duy nhất** trên toàn hệ thống (bảo vệ quỹ khuyến mại). | Nếu cho phép nhận đồng thời, một nhóm người dùng có thể gom quà từ 3-4 kịch bản cùng lúc, làm thâm hụt ngân sách. | `[Chờ MKT xác nhận]` |
| **Q5** | **Cơ chế tài chính khi Tái tặng quà (Re-gifting):**<br>Khi một mã quà tặng bị hết hạn và hệ thống cấp lại mã mới, ngân sách sẽ được hạch toán như thế nào? | **Phương án đề xuất:**<br>- Mã quà hết hạn: Tự động hoàn tiền về ngân sách chiến dịch.<br>- Cấp mã mới: Trừ tiền theo giá trị mã mới.<br>- Giới hạn: Tối đa **1 lần tái tặng**, thời gian chờ **3 ngày** sau khi quà cũ hết hạn. | Đảm bảo số liệu kế toán giải ngân khớp đúng 100% với số lượng vé thực tế được người dùng sử dụng. | `[Chờ MKT xác nhận]` |
| **Q6** | **Thời gian đo lường chuyển đổi (Attribution Window):**<br>Báo cáo theo dõi hành vi khách hàng tự bỏ tiền mua vé sau khi dùng quà tặng trong vòng bao nhiêu ngày? | **Phương án đề xuất:** Cố định mốc **07 ngày** và **30 ngày** kể từ thời điểm khách hàng sử dụng mã quà tặng để thanh toán vé thành công. | Là căn cứ để lập trình câu lệnh tổng hợp báo cáo tỷ lệ chuyển đổi doanh thu (Conversion Report). | `[Chờ MKT xác nhận]` |
| **Q7** | **Thời gian gửi tin nhắn thông báo (Notification SLA):**<br>Khung giờ gửi tin nhắn VLT Notification thông báo nhận quà và nhắc nhở sắp hết hạn? | **Phương án đề xuất:**<br>- *Tin nhận quà tặng thẳng:* Gửi lúc **08:30 sáng**.<br>- *Tin nhắc nhở hết hạn:* Gửi lúc **09:00 sáng** trước ngày hết hạn 24 giờ.<br>- Không gửi tin nhắn sau 21:00 đêm. | Tuân thủ quy định gửi tin nhắn chăm sóc khách hàng, không làm phiền người dùng ban đêm. | `[Chờ MKT xác nhận]` |
| **Q8** | **Phân kỳ phạm vi bàn giao trước mốc 26/10/2026:**<br>Do thời hạn yêu cầu còn 13 ngày (tính từ 13/10 đến 26/10/2026), Marketing có đồng ý chia làm 2 giai đoạn không? | **Phương án đề xuất:**<br>- **Giai đoạn 1 (Ra mắt 26/10/2026):** Triển khai KB 2 (Chi tiêu), KB 3 (Lượt vé), KB 4 (Bán chéo), VLT Noti, Báo cáo giải ngân.<br>- **Giai đoạn 2 (Sau 26/10/2026):** Triển khai KB 1 (Win-back quét đêm), KB 6 (Thứ trong tuần), Re-gifting và Báo cáo ROI chuyên sâu. | Đảm bảo dự án nghiệm thu đúng hạn, không bị trễ tiến độ cam kết trong Quý 4/2026. | `[Chờ MKT xác nhận]` |

---

## 4. KẾ HOẠCH HÀNH ĐỘNG SAU CUỘC HỌP (ACTION PLAN)

```
[Cuộc họp với Marketing] ➔ [Chốt 8 Open Questions]
            │
            ▼
[Cập nhật sheet BA_phan_tich trong file Excel]
            │
            ▼
[Soạn thảo tài liệu đặc tả SRS độc lập v1.0]
            │
            ▼
[Trình PO và Tech Lead phê duyệt phạm vi Sprint]
```

* **Thời gian thực hiện đề xuất:** Sáng ngày 14/10/2026 hoàn thành trao đổi; Chiều ngày 14/10/2026 hoàn thiện bản nháp SRS v1.0.
