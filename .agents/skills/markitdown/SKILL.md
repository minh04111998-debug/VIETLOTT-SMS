---
name: markitdown
description: >-
  Kỹ năng chuyển đổi các định dạng tài liệu văn phòng (PDF, Word DOCX/DOC, Excel XLSX/XLS, PowerPoint PPTX, HTML, Audio, Image) sang định dạng Markdown chuẩn cấu trúc. Dùng khi cần đọc/bóc tách bất kỳ tệp tài liệu hay thư mục tài liệu nào, nạp dữ liệu cho RAG, chuẩn hóa bảng biểu đối soát, hoặc trích xuất nội dung cho các role BA, SA, QA, DA trong dự án.
---

# Kỹ Năng: Chuyển Đổi & Bóc Tách Tài Liệu Đa Năng (MarkItDown)

## Mô Tả & Mục Tiêu
Skill này cung cấp quy trình và công cụ để tự động chuyển đổi **bất kỳ tệp tài liệu** (PDF, Word, Excel, PowerPoint, CSV, HTML, Audio...) hoặc **toàn bộ một thư mục bất kỳ** sang định dạng **Markdown (`.md`)**.

Công cụ được thiết kế hoàn toàn **động (dynamic)**, không cố định đường dẫn:
- **Xử lý tệp đơn lẻ:** Tự động tạo file `.md` ngay bên cạnh file gốc hoặc lưu đến vị trí chỉ định.
- **Xử lý thư mục:** Quét đệ quy chuyển đổi toàn bộ tệp hoặc gộp tất cả nội dung vào một file Markdown tổng hợp.
- **Bảo toàn bảng biểu (Markdown Tables):** Chuyển đổi chính xác các bảng đối soát tài chính, bảng ma trận phí, bảng tham số API thành Markdown table không bị vỡ dòng.

---

## Khi Nào Kích Hoạt?
Kích hoạt skill này khi:
1. Người dùng yêu cầu đọc, phân tích, trích xuất hoặc chuyển đổi một file hoặc một folder tài liệu bất kỳ.
2. Role **BA / PO** nhận tài liệu nghiệp vụ mới cần số hóa sang Markdown để làm đầu vào viết SRS/BRD.
3. Role **SA** cần bóc tách tài liệu kiến trúc, schema API, mã lỗi tích hợp hệ thống.
4. Role **QA** cần trích xuất các bảng kịch bản và ma trận điều kiện để viết Test Cases.
5. Role **DA** cần đọc bảng tính Excel sang bảng văn bản để phân tích biến động.

---

## Hướng Dẫn Thực Thi

Script thực thi chính: [`scripts/extract_docx.py`](file:///f:/VIETLOTT-SMS/scripts/extract_docx.py)

### 1. Chuyển đổi một tệp đơn lẻ bất kỳ
```powershell
# Chuyển đổi và tự động lưu thành file .md cùng tên ngay tại thư mục đó:
python scripts/extract_docx.py "đường_dẫn_tệp_bất_kỳ.pdf"

# Chuyển đổi và chỉ định file đầu ra cụ thể:
python scripts/extract_docx.py "C:\tailieu\baocao.xlsx" -o "C:\tailieu\baocao.md"
```

### 2. Chuyển đổi từng tệp trong một thư mục bất kỳ
```powershell
# Quét thư mục và tạo file .md tương ứng cho từng tài liệu:
python scripts/extractors/extract_docx.py "đường_dẫn_thư_mục_bất_kỳ"

# Quét và xuất kết quả ra một thư mục riêng:
python scripts/extractors/extract_docx.py "C:\folder_input" -o "C:\folder_output"
```

### 3. Quét thư mục và GỘP tất cả vào 1 file Markdown duy nhất
```powershell
# Rất hữu ích khi cần tổng hợp toàn bộ tài liệu của một module vào 1 file tri thức:
python scripts/extractors/extract_docx.py "C:\path\to\folder" -m "tong_hop_kien_thuc.md"
```

### 4. Dùng trực tiếp lệnh CLI toàn cục
```powershell
markitdown "file_bất_kỳ.pdf" -o "file_bất_kỳ.md"
```

---

## Quy Chuẩn Đầu Ra (Conventions)
1. **UTF-8 Encoding:** Luôn ghi nhận kết quả dưới dạng UTF-8 để bảo toàn tiếng Việt có dấu.
2. **Loại bỏ tệp rác Office:** Tự động lọc bỏ các tệp tạm bắt đầu bằng `~$`, tệp ẩn hệ thống `.*` và `desktop.ini`.
3. **Fallback tệp cũ:** Tự động gọi COM Word để đọc các tệp `.doc` (Word 97-2003) cũ nếu có.
