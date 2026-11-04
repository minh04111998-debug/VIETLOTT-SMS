---
name: da-review
description: Thẩm định và đánh giá output Data Analyst (Báo cáo kinh doanh, Executive Dashboard, Insights) theo chuẩn Senior Decision Intelligence và Minto Pyramid
---

# Kỹ Năng: DA Output Review & Senior Analytics Audit

## 1. Mô Tả & Kích Hoạt
Kỹ năng dùng để thẩm định chất lượng các báo cáo phân tích dữ liệu và dashboard do Data Analyst tạo ra (Weekly Business Report, Cohort Analysis, Anomaly Detection, PowerBI/Sheet Dashboard).
- **Thời điểm kích hoạt:** Trong bước `CRITIQUE` của quy trình phân tích dữ liệu (`workflows/data-analysis/`), trước khi xuất trình báo cáo cho Giám đốc kinh doanh / Ban Lãnh đạo hoặc trước khi đưa Dashboard vào sử dụng định kỳ.
- **Tiêu chuẩn đối chiếu:** Decision Intelligence, Barbara Minto (Pyramid Principle), Stephen Few (Information Dashboard Design).

---

## 2. Bảng So Sánh Cấp Độ Đầu Ra DA

| Tiêu chí | Junior / Mid DA Output | Senior DA Output (Target) |
|---|---|---|
| **Cấp độ phân tích** | Dừng lại ở mô tả (Descriptive): "Doanh thu tuần này tăng 5% so với tuần trước". | Đạt mức chẩn đoán (Diagnostic) và đề xuất (Prescriptive): "Tại sao tăng? Khách hàng nào thúc đẩy? Cần làm gì tiếp theo?". |
| **Cấu trúc trình bày** | Đổ toàn bộ bảng số liệu thô dày đặc, biểu đồ lộn xộn khiến sếp khó tìm ý chính. | Cấu trúc Kim tự tháp Minto (Top-down): Kết luận/Khuyến nghị đưa lên đầu, sau đó mới đến số liệu chứng minh. |
| **Khuyến nghị hành động**| Không có khuyến nghị, hoặc khuyến nghị chung chung ("Cần đẩy mạnh marketing"). | Đưa ra ít nhất 3 Actionable Recommendations có chủ thể thực hiện, việc cần làm và tác động dự kiến. |
| **Độ tin cậy dữ liệu** | Lấy dữ liệu chưa làm sạch; kết luận vội vã từ cỡ mẫu quá nhỏ hoặc bị lệch bởi ngoại lai. | Kiểm định độ tin cậy thống kê (Statistical Significance), lọc sạch duplicate, cô lập và giải thích outliers. |
| **Thiết kế Dashboard** | Bảng màu sặc sỡ, thiếu ngữ cảnh so sánh (chỉ thấy con số tuyệt đối, không biết tốt hay xấu). | Cấu trúc 3 tầng chuẩn mực (KPI Cards $\to$ Trend/Breakdown $\to$ Granular Table); đầy đủ so sánh WoW/MoM/YoY. |

---

## 3. Senior DA Output Checklist (15 Điểm Thẩm Định)

### A. Độ Toàn Vẹn & Tính Chuẩn Xác Dữ Liệu (Data Integrity & Rigor)
- [ ] **DA-CHK-01 [Data Hygiene Verification]**: Dữ liệu thô đã được làm sạch, kiểm tra trùng lặp (de-duplication), xử lý giá trị khuyết thiếu (missing values) và chuẩn hóa kiểu dữ liệu trước khi tính toán.
- [ ] **DA-CHK-02 [Outlier Isolation]**: Các giá trị dị biệt (outliers) đã được phát hiện, giải thích rõ nguyên nhân (ví dụ: giao dịch thử nghiệm nội bộ, ngày khuyến mãi đặc biệt) và không làm sai lệch bức tranh tổng thể.
- [ ] **DA-CHK-03 [Statistical Significance]**: Kết luận phân tích không dựa trên cỡ mẫu quá nhỏ hoặc biến động ngẫu nhiên; có lưu ý về mức độ tin cậy nếu dữ liệu hạn chế.

### B. Độ Sâu Phân Tích Chẩn Đoán (Diagnostic Analytics Depth)
- [ ] **DA-CHK-04 [Root Cause Decomposition]**: Khi có biến động tăng/giảm, báo cáo phân rã ít nhất 2–3 tầng nguyên nhân:
  - *Theo kênh thanh toán*: Ngân hàng nào hay ví nào tăng/giảm?
  - *Theo nhóm người dùng*: Người dùng mới (New Users) hay người dùng cũ (Retained Buyers)?
  - *Theo sản phẩm*: Dòng game xổ số nào (Power 6/55, Mega 6/45, Keno) đóng góp chính?
- [ ] **DA-CHK-05 [Funnel & Cohort Analysis]**: Báo cáo có phân tích phễu chuyển đổi (Conversion Funnel Drop-off) hoặc phân tích chu kỳ giữ chân người dùng (Cohort Retention) thay vì chỉ nhìn vào một lát cắt tĩnh.

### C. Khuyến Nghị Hành Động Rõ Ràng (Actionable & Prescriptive Insights)
- [ ] **DA-CHK-06 [The "So What?" Test]**: Mỗi insight tìm thấy đều trả lời được câu hỏi: *"Điều này có ý nghĩa gì đối với mục tiêu kinh doanh của công ty?"*
- [ ] **DA-CHK-07 [Actionable Recommendations]**: Báo cáo kết thúc bằng **Top 3 Khuyến nghị cụ thể**, đáp ứng công thức 3 thành phần:
  1. *Chủ thể hành động* (Ví dụ: Đội ngũ CSKH / Đội ngũ Marketing / Đội ngũ Kỹ thuật).
  2. *Hành động cụ thể* (Ví dụ: Gửi tin nhắn SMS kích hoạt lại nhóm khách hàng không mua vé 14 ngày qua).
  3. *Tác động dự kiến* (Ví dụ: Dự kiến phục hồi 5–8% lượng Active Buyers trong đợt quay thưởng tới).
- [ ] **DA-CHK-08 [Priority Labeling]**: Khuyến nghị được phân cấp mức độ ưu tiên rõ ràng (**P1 - Khẩn cấp / Impact cao**, **P2 - Trung hạn**).

### D. Kể Chuyện Bằng Dữ Liệu Cho Lãnh Đạo (Executive Data Storytelling)
- [ ] **DA-CHK-09 [Minto Pyramid Structure]**: Cấu trúc báo cáo tuân thủ nguyên tắc Kim tự tháp:
  - *Phần đầu (30 giây)*: Executive Summary & Key Takeaways (3–5 gạch đầu dòng quan trọng nhất).
  - *Phần giữa (5 phút)*: Các phân tích chuyên sâu kèm biểu đồ xu hướng.
  - *Phần cuối (Chi tiết)*: Bảng số liệu chi tiết và phương pháp tính toán.
- [ ] **DA-CHK-10 [No Fluff & Jargon]**: Ngôn ngữ súc tích, chuyển hóa thuật ngữ kỹ thuật dữ liệu thành ngôn ngữ kinh doanh (Business Impact).

### E. Thiết Kế Trực Quan Hóa (Executive Dashboard UX)
- [ ] **DA-CHK-11 [3-Tier Layout Principle]**: Dashboard được tổ chức chuẩn 3 tầng từ trên xuống dưới:
  1. *Top Tier*: Thẻ tóm tắt chỉ số chính (KPI Cards: Doanh thu, Lượng vé, Active Buyers, Tỷ lệ lỗi).
  2. *Middle Tier*: Biểu đồ trực quan (Xu hướng theo thời gian, tỷ trọng game, phễu chuyển đổi).
  3. *Bottom Tier*: Bảng dữ liệu phân rã chi tiết hoặc đối soát.
- [ ] **DA-CHK-12 [Comparative Context]**: Mọi chỉ số chính đều có ngữ cảnh so sánh rõ ràng: Tuần trước (**WoW**), Tháng trước (**MoM**), hoặc Cùng kỳ năm trước (**YoY**).
- [ ] **DA-CHK-13 [Visual Accessibility & Color Logic]**: Màu sắc có tính quy ước nhất quán: Xanh lá (Tăng trưởng tốt), Đỏ (Báo động suy giảm), Xám/Xanh dương (Trung tính). Không dùng quá 5 màu trên một dashboard.
- [ ] **DA-CHK-14 [Data Freshness Notice]**: Thể hiện rõ mốc thời gian cập nhật dữ liệu (Timestamp: `Dữ liệu cập nhật đến 23:59 ngày DD/MM/YYYY`).
- [ ] **DA-CHK-15 [PII Masking Enforcement]**: Báo cáo tuyệt đối không hiển thị SĐT đầy đủ hoặc thông tin cá nhân của khách hàng trúng thưởng/mua vé (tuân thủ Nghị định 13/2023/NĐ-CP).

---

## 4. Hướng Dẫn Sửa Lỗi Nhanh Khi Bị Đánh Rớt (Actionable Fix Guide)

1. **Lỗi báo cáo chỉ có số liệu mà không có Insight:**
   - Đặt câu hỏi "Tại sao?" ít nhất 3 lần cho con số biến động lớn nhất và ghi câu trả lời thành 1 bullet point Insight.
2. **Lỗi thiếu hành động (Actionable Output):**
   - Áp dụng mẫu: `[Bộ phận] cần [Hành động] trước [Thời hạn] để đạt [Mục tiêu số liệu]`.
3. **Lỗi biểu đồ rối mắt, quá nhiều thông tin:**
   - Giảm số lượng series trên 1 chart xuống tối đa 4 đường/cột; gom các nhóm nhỏ hơn 5% vào nhóm "Khác" (Others).
