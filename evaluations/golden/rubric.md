# Rubric chấm chất lượng deliverable (Golden Set)

> Thang điểm: 5 tiêu chí × 0–2 điểm = tối đa **10**. Ngưỡng golden đề xuất: **≥ 8** và không tiêu chí nào 0 điểm.
> Căn cứ tiêu chí: ISO/IEC/IEEE 29148 (đặc tính yêu cầu tốt) — xem `references/` và `.agents/rules/banned-words.md`.

| # | Tiêu chí | 0 điểm | 1 điểm | 2 điểm |
|---|---|---|---|---|
| 1 | **Đo được (Verifiable)** | Yêu cầu dùng tính từ định tính, không có con số | Một phần yêu cầu có số đo / điều kiện trigger | Mọi yêu cầu có số đo, ngưỡng hoặc danh sách đóng |
| 2 | **Truy vết (Traceable)** | Không có ID hoặc không liên kết nguồn | Có ID nhưng thiếu liên kết BR→FR→TC hoặc thiếu trích nguồn | ID đầy đủ, liên kết hai chiều, mọi thông tin nghiệp vụ trích `[Nguồn: SRC-XX]` |
| 3 | **Ngoại lệ & biên (Complete)** | Chỉ mô tả luồng thành công | Có một số luồng lỗi nhưng thiếu timeout / mất kết nối / thiếu số dư | Luồng lỗi, timeout, trạng thái trung gian và edge case đều có hành vi xác định |
| 4 | **Ranh giới Human (Governed)** | AI tự quyết KPI, scope, quy tắc pháp lý | Có đánh dấu một phần quyết định cần Human | Mọi quyết định thuộc Hard Stop đều gắn nhãn, giả định và câu hỏi mở được ghi vào `observability/` |
| 5 | **Dùng được ngay cho vai trò sau (Handoff-ready)** | Thiếu mục bắt buộc theo handoff contract | Đủ mục nhưng vai trò sau phải hỏi lại | Đủ mục bắt buộc theo `.agents/definitions/handoff-contracts.md`, vai trò sau làm tiếp được không cần hỏi lại |

**Ghi kết quả chấm:** điểm tổng vào trường `human_score` trong `manifest.json`; lý do từng tiêu chí ghi ngắn trong commit/biên bản duyệt.
