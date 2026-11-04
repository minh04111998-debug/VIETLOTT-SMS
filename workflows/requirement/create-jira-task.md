---
description: Quy trình tự động tạo Jira Task - Vai trò BA/PM
---

# Quy trình Tạo Jira Task Nhanh (Create Jira Task)

## Mục Đích
Tự động hóa quá trình tạo Task/Story/Bug trên hệ thống Jira từ câu lệnh tự nhiên của người dùng, giảm thiểu thao tác thủ công.

## Vai Trò Thực Hiện
**BA** hoặc **PM** (quyền theo `tools/tool-registry.md` §4 — tool mức 🔴 Ghi ngoài, bắt buộc Hard Stop).

## Trigger
- Lệnh `/create-jira-task`
- Hoặc câu lệnh tự nhiên: "tạo giúp tôi task trên Jira", "đẩy cái này lên Jira"...

## Các Bước Thực Hiện

### Bước 1: Thu thập thông tin (Elicitation)
Agent kiểm tra xem yêu cầu của người dùng đã có đủ 3 thông tin bắt buộc chưa:
1. **Dự án (Project)**: (VD: Xăng dầu, Hóa đơn điện tử)
2. **Tiêu đề (Summary)**: Ngắn gọn, súc tích.
3. **Mô tả (Description)**: Chi tiết yêu cầu.

*Nếu thiếu bất kỳ thông tin nào, Agent PHẢI dừng lại và hỏi người dùng để làm rõ.*

### Bước 2: Mapping Project Key
Chuyển đổi tên dự án tự nhiên sang mã Project Key tương ứng:
- Xăng dầu / Xăng dầu ATC -> `XDA`
- Phần mềm bán hàng -> `PMBH`
- Quản lý bán hàng -> `QLBH`
- Hóa đơn điện tử -> `HDDT`
- Tổng đài -> `QTA`
- Công chứng -> `CC`
*(Nếu dự án không có trong danh sách trên, Agent PHẢI hỏi người dùng mã Project Key — KHÔNG tự suy luận, vì tạo ticket sai dự án là thao tác ghi ra hệ thống bên ngoài.)*
> `[❓ OPEN — Q-008]` Danh sách mapping trên (Xăng dầu, Hóa đơn điện tử, Công chứng...) và `JIRA_URL` mặc định trong script không thuộc dự án Vietlott SMS — cần Human xác nhận Project Key của Vietlott SMS.

### Bước 3: 🛑 Hard Stop — Xác nhận trước khi tạo
Trình cho Human bảng tóm tắt: Project Key, Issue Type, Summary, Description, Assignee. Kiểm tra nội dung không chứa PII chưa mask và không chứa secret. **Chỉ thực thi Bước 4 sau khi Human xác nhận rõ ràng trong phiên làm việc.** Với yêu cầu tạo nhiều task, trình toàn bộ danh sách một lần.

### Bước 4: Thực thi Script (Execution)
Gọi công cụ dòng lệnh bằng PowerShell (từ thư mục gốc dự án):
```powershell
$env:PYTHONIOENCODING="utf-8"; python "tools/jira/create_task.py" --project "[ProjectKey]" --summary "[Tiêu đề]" --description "[Mô tả]" --assignee "[Username]"
```
Exit code: `0` = tạo thành công, `1` = lỗi (thiếu credentials, HTTP lỗi, SSL).

### Bước 5: Báo Cáo Kết Quả
- Đọc Output trả về từ Terminal.
- Trích xuất **Issue Key** và **URL**.
- In ra một thông báo Markdown đẹp mắt chứa đường dẫn trực tiếp (clickable link) để người dùng có thể bấm vào xem ngay thẻ Jira vừa tạo.

> [!TIP]
> Người dùng có thể đính kèm danh sách tính năng từ PRD và yêu cầu AI tự động chẻ nhỏ thành nhiều task Jira thông qua vòng lặp.
