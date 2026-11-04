# User Story & Acceptance Criteria Specification

> **Mã Story:** US-[ID] | **Feature:** [Tên Feature]  
> **Ưu tiên:** Must Have (P0) / Should Have (P1) / Could Have (P2)  
> **Story Points ước tính:** [1 / 2 / 3 / 5 / 8] SP

---

## 1. Nội Dung User Story (Format Concurrence)

```text
As a [Chân dung người dùng / Người chơi Vietlott SMS]
I want [Thực hiện hành động hoặc tính năng cụ thể]
So that [Đạt được lợi ích, giải quyết vấn đề hoặc hoàn thành mục tiêu]
```

---

## 2. Kiểm Tra Tiêu Chuẩn INVEST
- [x] **I — Independent (Độc lập):** Không phụ thuộc chặt vào story chưa hoàn thành.
- [x] **N — Negotiable (Thương lượng được):** Chi tiết kỹ thuật có thể bàn bạc giữa BA và DEV.
- [x] **V — Valuable (Có giá trị):** Mang lại lợi ích rõ ràng cho người chơi hoặc doanh nghiệp.
- [x] **E — Estimable (Ước lượng được):** Đủ rõ ràng để DEV team cho điểm Story Points.
- [x] **S — Small (Đủ nhỏ):** Có thể hoàn thành trong 1 sprint (1-3 ngày làm việc).
- [x] **T — Testable (Kiểm thử được):** Có Acceptance Criteria rõ ràng.

---

## 3. Tiêu Chí Nghiệm Thu (Acceptance Criteria — GWT)

### Scenario 1: [Tên kịch bản thành công chính]
```gherkin
Given [Tiền điều kiện ban đầu của hệ thống và người dùng]
When [Hành động kích hoạt sự kiện được thực hiện]
Then [Kết quả mong đợi trả về]
And [Tác động phụ hoặc trạng thái cập nhật tiếp theo]
```

### Scenario 2: [Kịch bản xử lý ngoại lệ / Lỗi]
```gherkin
Given [Người dùng thực hiện giao dịch trong trạng thái lỗi (VD: Hết số dư / Mất kết nối mạng)]
When [Người dùng bấm xác nhận giao dịch]
Then [Hệ thống hiển thị thông báo lỗi rõ ràng và gợi ý giải pháp xử lý]
And [Hệ thống không trừ tiền và không sinh vé rác]
```
