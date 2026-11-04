# Quality Gate Execution Reports

Thư mục này lưu trữ các báo cáo thực thi Quality Gate tự động sinh ra từ `validators/gate_runner.py` hoặc các scripts kiểm thử.

## Quy Định Báo Cáo Gate:
Mỗi báo cáo được đặt tên theo cú pháp: `QGR-[YYYYMMDD]-[Role]-[ArtifactName].md` và phải chứa:
1. Danh sách checklists và validators thực sự được chạy.
2. Kết quả kiểm tra: PASS / FAIL / NOT APPLICABLE (kèm lý do).
3. Danh sách các phát hiện vi phạm (Blocking vs Important).
4. Xác nhận trạng thái cho phép bước tiếp theo thực thi.
