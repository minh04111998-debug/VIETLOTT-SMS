---
name: ba-review
description: Thẩm định và đánh giá chất lượng output tài liệu BA (SRS, Use Case, User Story, NFR) theo chuẩn Senior BABOK v3 và kiến trúc ngoại lệ
---

# Kỹ Năng: BA Output Review & Senior Quality Audit

## 1. Mô Tả & Kích Hoạt
Kỹ năng dùng để thẩm định chất lượng các tài liệu nghiệp vụ do BA tạo ra (SRS, Use Case, User Story, BDD Acceptance Criteria, Change Request, NFR). 
- **Thời điểm kích hoạt:** Trong bước `CRITIQUE` của quy trình phân tích yêu cầu (`workflows/requirement/`), trước khi gửi sang PO/SA/DEV/QA hoặc trước khi Human ký duyệt baseline.
- **Tiêu chuẩn đối chiếu:** BABOK® v3 (IIBA), ISO/IEC/IEEE 29148.

---

## 2. Bảng So Sánh Cấp Độ Đầu Ra BA

| Tiêu chí | Junior / Mid BA Output | Senior BA Output (Target) |
|---|---|---|
| **Tư duy yêu cầu** | Ghi chép thụ động giải pháp bề mặt của khách hàng ("cần nút màu xanh"). | Đào sâu vấn đề gốc (5 Whys), phân tách rõ Problem vs Solution, phát hiện mâu thuẫn ẩn giữa các bên. |
| **Kịch bản AC** | Chủ yếu mô tả Happy Path; Alternative sơ sài; bỏ qua lỗi hệ thống. | Đầy đủ 4 kịch bản BDD: Happy, Alternative, Exception, Edge Cases ranh giới dữ liệu. |
| **Tích hợp & Ngoại lệ** | Coi API bên thứ 3 luôn chạy tốt; không có timeout hay rollback. | Thiết kế trọn vẹn kiến trúc ngoại lệ: Timeout định lượng, Hung state, Idempotency key, Compensating reversal, Reconciliation. |
| **Độ đo NFR** | Dùng từ cảm tính ("hệ thống phản hồi nhanh", "thao tác dễ dàng"). | Định lượng hóa SLA đo được: P95 < 500ms, throughput 500 TPS, RTO < 15p, RPO = 0. |
| **Độ sẵn sàng (DoR)** | DEV phải họp nhiều lần để hỏi lại luồng; QA tự bịa kịch bản test. | Tự chứa (Self-contained): DEV estimate được ngay, QA tạo test matrix 100% bao phủ. |

---

## 3. Senior BA Output Checklist (15 Điểm Thẩm Định)

### A. Traceability & Scope (Truy vết & Phạm vi)
- [ ] **BA-CHK-01 [Traceability]**: Mọi FR và NFR đều có mã ID chuẩn (`FR-xxx`, `NFR-xxx`) và map ngược về ít nhất 1 Business Goal / User Need cụ thể.
- [ ] **BA-CHK-02 [Boundary Clarity]**: Tài liệu có mục **In-Scope** và **Out-of-Scope** danh sách đóng rõ ràng, không để khoảng trống cho scope creep.
- [ ] **BA-CHK-03 [RACI & Governance]**: Xác định rõ ai là Người phê duyệt (Approver), ai tham vấn (Consulted) theo quy tắc quản trị yêu cầu.

### B. Kịch Bản Nghiệp Vụ & BDD AC (BDD Completeness)
- [ ] **BA-CHK-04 [Scenario Diversity]**: Mỗi Use Case / User Story đều có đủ 4 tầng kịch bản:
  1. *Happy Path*: Luồng chuẩn lý tưởng mang lại kết quả mong muốn.
  2. *Alternative Path*: Nhánh rẽ hợp lệ (đổi cổng thanh toán, đổi hình thức nhận OTP).
  3. *Exception Path*: Lỗi nghiệp vụ (tài khoản không đủ số dư, nhập sai OTP quá số lần).
  4. *Edge Cases*: Giá trị biên min/max, chuỗi ký tự Unicode, số 0, khoảng trắng, số âm.
- [ ] **BA-CHK-05 [BDD Format]**: Tiêu chí nghiệm thu viết chuẩn cú pháp `Given - When - Then`, tránh mô tả hành động kỹ thuật bên dưới.
- [ ] **BA-CHK-06 [INVEST Quality]**: Mọi User Story đều độc lập (Independent), đàm phán được (Negotiable), có giá trị (Valuable), ước lượng được (Estimable), kích thước vừa vặn trong sprint (Small), và kiểm thử được (Testable).

### C. Kiến Trúc Ngoại Lệ & Giao Dịch Treo (Exception & Hung State)
- [ ] **BA-CHK-07 [Timeout Quantification]**: Mọi điểm tích hợp external (Telco SMS, Payment Gateway, Ngân hàng) đều có thời gian Timeout định lượng cụ thể (ví dụ: 30 giây, 60 giây).
- [ ] **BA-CHK-08 [Hung State Recovery]**: Luồng giao dịch có trạng thái treo (Pending/Processing) bắt buộc phải chỉ rõ: Ai/Cơ chế nào phát hiện (polling, webhook, heartbeat) và ai xử lý (cronjob tự động hay vận hành can thiệp)?
- [ ] **BA-CHK-09 [Idempotency & Reversal]**: Có quy định rõ ràng về **Idempotency Key** khi retry (tránh duplicate giao dịch trừ tiền) và hành động bù trừ (**Compensating Action / Reversal**) khi giao dịch đứt quãng giữa chừng.
- [ ] **BA-CHK-10 [Reconciliation Link]**: Mọi trạng thái giao dịch bất thường đều được quy định đưa vào luồng đối soát tự động ngày T+1.

### D. Đo Lường & Chuẩn Hóa Ngôn Ngữ (Language & NFR Rigor)
- [ ] **BA-CHK-11 [No Ambiguity]**: Không chứa bất kỳ từ cấm mơ hồ nào theo ISO 29148 (*"nhanh chóng", "thân thiện", "tối ưu", "dễ dùng", "v.v.", "TBD"*).
- [ ] **BA-CHK-12 [Quantified NFR]**: Các yêu cầu phi chức năng có đầy đủ chỉ số kỹ thuật: Thời gian phản hồi (P95/P99 latency), tải đồng thời (Concurrent users/TPS), độ khả dụng (Uptime 99.9x%), và an toàn dữ liệu (RTO/RPO).
- [ ] **BA-CHK-13 [Data Privacy & PII]**: Không chứa dữ liệu thật của khách hàng (SĐT, CCCD, số thẻ, số tài khoản phải được che theo Nghị định 13/2023/NĐ-CP).

### E. Tính Khả Thi Triển Khai (Implementation Readiness)
- [ ] **BA-CHK-14 [DEV Hand-off Feasibility]**: DEV Lead đọc xong tài liệu có thể hình dung được Data Model, State Machine và chia nhỏ task kỹ thuật mà không cần hỏi lại câu hỏi căn bản.
- [ ] **BA-CHK-15 [QA Testability]**: QA Lead đọc xong có thể dựng được Test Matrix và truy vết 1:1 từ AC sang Test Cases.

---

## 4. Hướng Dẫn Sửa Lỗi Nhanh Khi Bị Đánh Rớt (Actionable Fix Guide)

1. **Lỗi thiếu Edge Cases / Exception:**
   - Bổ sung ngay bảng *Exception Analysis Matrix* theo mẫu:
     `| Bước | Trigger | Loại lỗi | Phản hồi người dùng | Timeout | Retry Policy | Hành động rollback |`
2. **Lỗi từ cấm mơ hồ:**
   - Thay "Hệ thống phản hồi nhanh chóng" $\to$ "Thời gian trả lời API $\le 500\text{ms}$ tại mức tải $200\text{ TPS}$".
   - Thay "Giao diện thân thiện, dễ thao tác" $\to$ "Người dùng hoàn tất quy trình mua vé trong tối đa 3 bước với thời gian thao tác trung bình $\le 60\text{ giây}$".
3. **Lỗi thiếu Traceability:**
   - Bổ sung bảng *Requirements Traceability Matrix (RTM)* liên kết từ `Goal-ID` $\to$ `FR-ID` $\to$ `TC-ID`.
