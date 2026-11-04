---
name: po-review
description: Thẩm định và đánh giá output Product Owner (Product Discovery, PRD, Backlog, RICE, MVP) theo chuẩn Senior IIBA POA và SVPG
---

# Kỹ Năng: PO Output Review & Senior Product Audit

## 1. Mô Tả & Kích Hoạt
Kỹ năng dùng để thẩm định chất lượng các sản phẩm đầu ra của Product Owner (Product Discovery, PRD, Product Backlog, Story Mapping, RICE Scoring, MVP Definition).
- **Thời điểm kích hoạt:** Trong bước `CRITIQUE` của quy trình phát triển sản phẩm (`workflows/product-discovery/`), trước khi đưa User Story vào Sprint Planning hoặc trước khi trình duyệt PRD lên Ban Lãnh đạo.
- **Tiêu chuẩn đối chiếu:** IIBA Guide to Product Ownership Analysis (POA), Marty Cagan (Inspired / SVPG), Teresa Torres (Continuous Discovery Habits).

---

## 2. Bảng So Sánh Cấp Độ Đầu Ra PO

| Tiêu chí | Junior / Mid PO Output | Senior PO Output (Target) |
|---|---|---|
| **Mục tiêu sản phẩm** | Tập trung vào số lượng tính năng ("Feature Factory"), đo bằng Velocity hoàn thành. | Tập trung vào giá trị (Outcome over Output), đo bằng North Star Metric & tác động doanh thu/người dùng. |
| **Quản trị rủi ro** | Đợi code xong mới biết người dùng có thích hay không; bỏ qua rủi ro pháp lý/kỹ thuật. | Triệt tiêu 4 rủi ro sản phẩm (Value, Usability, Feasibility, Viability) ngay từ bước Discovery. |
| **Phân bổ ưu tiên** | Backlog xếp theo cảm tính, theo ai nói to nhất (HiPPO) hoặc ai giục nhiều nhất. | Ưu tiên dựa trên dữ liệu (RICE, WSJF, Cost of Delay) kết hợp mục tiêu chiến lược tổ chức. |
| **Cắt lát MVP** | Cắt theo chiều ngang kỹ thuật (Sprint 1 làm DB, Sprint 2 làm UI); MVP quá cồng kềnh. | Cắt lát mỏng theo Walking Skeleton (luồng end-to-end mỏng nhất mang lại giá trị trọn vẹn). |
| **Thử nghiệm & Học hỏi**| Coi tính năng là cam kết cố định; tính năng thất bại thì âm thầm bỏ qua. | Đặt tính năng dưới dạng giả thuyết kiểm chứng (Hypothesis-driven), có MCS và tiêu chí Pivot/Kill rõ ràng. |

---

## 3. Senior PO Output Checklist (15 Điểm Thẩm Định)

### A. Định Hướng Giá Trị & Mục Tiêu (Outcome & Alignment)
- [ ] **PO-CHK-01 [Outcome Linkage]**: Mỗi sáng kiến / Epic / Feature đều gắn liền với một **North Star Metric** hoặc **Key Result (OKR)** cụ thể có thể đo đạc bằng số liệu.
- [ ] **PO-CHK-02 [Problem vs Solution]**: Tài liệu làm rõ triệt để Vấn đề của người dùng (Customer Problem) trước khi đề xuất Giải pháp (Solution). Trả lời được: *"Nếu chúng ta không làm tính năng này, tổn thất cụ thể là gì?"*
- [ ] **PO-CHK-03 [Target Persona Precision]**: Định danh rõ ràng phân khúc người dùng mục tiêu (Persona) chịu ảnh hưởng, không nói chung chung "người dùng".

### B. Triệt Tiêu 4 Rủi Ro Sản Phẩm (Four Product Risks — Marty Cagan)
- [ ] **PO-CHK-04 [Value Risk Validation]**: Có bằng chứng chứng minh khách hàng thực sự có nhu cầu và sẵn sàng sử dụng/mua (phỏng vấn $\ge 5$ khách hàng, dữ liệu phân tích hành vi, hoặc khảo sát định lượng).
- [ ] **PO-CHK-05 [Usability Risk Assessment]**: Đã kiểm tra tính khả dụng của luồng trải nghiệm (User Flow/Wireframe được đánh giá không gây bối rối hay tắc nghẽn thao tác).
- [ ] **PO-CHK-06 [Feasibility Alignment]**: Đã tham vấn Tech Lead / Solution Architect về tính khả thi công nghệ và giới hạn hạ tầng trước khi cam kết scope.
- [ ] **PO-CHK-07 [Viability & Compliance]**: Đã thẩm định tính phù hợp về pháp lý, quy chế kinh doanh, an toàn tài chính (đặc biệt trong Fintech/Xổ số: hạn mức nạp/rút, chống gian lận, thuế TNCN).

### C. Cắt Lát MVP & Story Mapping (Lean Delivery)
- [ ] **PO-CHK-08 [Walking Skeleton]**: Bản đồ câu chuyện (User Story Map) thể hiện rõ khung xương sống (Backbone) xuyên suốt hành trình khách hàng.
- [ ] **PO-CHK-09 [Thin-Slice MVP]**: Phiên bản phát hành đầu tiên (MVP) được cắt lát mỏng nhất có thể chạy thông luồng end-to-end, loại bỏ toàn bộ các tính năng "trang trí" (nice-to-have).
- [ ] **PO-CHK-10 [Clear Release Horizons]**: Lộ trình sản phẩm được phân định theo 3 tầng tầm nhìn thực tế: **NOW** (Sprint hiện tại), **NEXT** (1–2 tháng tới), **LATER** (Tương lai/Đang nghiên cứu).

### D. Ưu Tiên Hóa Dựa Trên Dữ Liệu (Evidence-based Prioritization)
- [ ] **PO-CHK-11 [RICE / WSJF Scoring]**: Mọi item trong Backlog đều được chấm điểm định lượng (Reach, Impact, Confidence, Effort). Không để backlog tồn đọng hàng trăm item vô danh.
- [ ] **PO-CHK-12 [Say No by Default]**: Có luận điểm rõ ràng để giải thích lý do từ chối hoặc hoãn lại các yêu cầu phát sinh không phục vụ mục tiêu quý.

### E. Giả Thuyết & Vòng Lặp Học Hỏi (Experimentation & Learning Loops)
- [ ] **PO-CHK-13 [Hypothesis Definition]**: Feature được viết dưới dạng giả thuyết kiểm chứng: *"Chúng tôi tin rằng [tính năng X] sẽ giúp [đối tượng Y] đạt được [kết quả Z]. Chúng tôi biết mình đúng khi [chỉ số W tăng K%]"*.
- [ ] **PO-CHK-14 [Minimum Criteria for Success (MCS)]**: Thiết lập trước ngưỡng đạt kỳ vọng (ví dụ: Tỷ lệ hoàn tất mua vé đạt $\ge 75\%$ sau 2 tuần mở bán).
- [ ] **PO-CHK-15 [Pivot / Kill Triggers]**: Quy định rõ điều kiện dừng hoặc chuyển hướng nếu số liệu thực tế không đạt sau thời gian thử nghiệm.

---

## 4. Hướng Dẫn Sửa Lỗi Nhanh Khi Bị Đánh Rớt (Actionable Fix Guide)

1. **Lỗi yêu cầu mang tính "Feature Factory":**
   - Chuyển đổi định dạng: Từ "Xây dựng tính năng nhắc mua vé" $\to$ "Tăng tỷ lệ người dùng mua vé định kỳ ngày quay thưởng từ 12% lên 20% thông qua thông báo thông minh".
2. **Lỗi MVP quá lớn / cồng kềnh:**
   - Dùng kỹ thuật *Story Slicing*: Tách theo luồng dữ liệu đơn giản nhất (ví dụ: chỉ hỗ trợ 1 phương thức thanh toán phổ biến nhất trong đợt đầu thay vì tích hợp cả 4 cổng cùng lúc).
3. **Lỗi thiếu căn cứ ưu tiên:**
   - Lập bảng ma trận RICE chấm điểm minh bạch và công khai cho các bên liên quan.
