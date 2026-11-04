# Ví Dụ Thực Tế Sử Dụng MarkItDown Trong Dự Án VIETLOTT-SMS

Tài liệu này cung cấp các ví dụ thực chiến khi áp dụng kỹ năng **MarkItDown** cho các bài toán cụ thể trong dự án Vietlott SMS.

---

## 1. Ví Dụ: Trích xuất bảng đối soát tài chính từ Excel

Khi cần kiểm tra công thức và dữ liệu đối soát nạp/rút tiền giữa Vietlott và các ví điện tử (ZaloPay, Mobifone Money, VNPT Money):

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert(r"f:\VIETLOTT-SMS\knowledge\product\sources\Mau_Doi_Soat_2026.xlsx")

# Kết quả sinh ra bảng Markdown chuẩn:
# | Ngày GD | Mã Đơn Hàng | Số Thuê Bao | Số Tiền | Kênh Thanh Toán | Trạng Thái |
# |---|---|---|---|---|---|
# | 2026-03-01 | VT1234567 | 0987654321 | 50.000 | ZaloPay | Thành Công |
```

Ưu điểm: Agent có thể dùng ngay bảng này để viết công thức tính toán hoặc verify số liệu mà không bị lệch cột như plain text.

---

## 2. Ví Dụ: Đọc tài liệu đặc tả tích hợp API kênh bán (Word DOCX)

Trích xuất tài liệu kết nối kỹ thuật để cung cấp đầu vào cho Solution Architect (SA):

```powershell
markitdown "f:\VIETLOTT-SMS\knowledge\product\sources\Tai_lieu_tich_hop_ZaloPay_v2.docx" -o "f:\VIETLOTT-SMS\artifacts\technical\ZaloPay_Integration_Spec.md"
```

Sau khi chạy lệnh trên:
- Các đề mục `# 1. Quy trình thanh toán`, `## 1.1 Khởi tạo đơn hàng` được giữ nguyên.
- Danh sách tham số request/response JSON và bảng mã lỗi HTTP được định dạng rõ ràng trong Markdown, giúp SA dễ dàng lập Architecture Decision Record (ADR).

---

## 3. Ví Dụ: Tự động hóa Pipeline cập nhật Knowledge Base cho Agent

Khi đối tác gửi tài liệu bản cập nhật mới, chỉ cần chạy:

```powershell
python f:\VIETLOTT-SMS\scripts\extract_docs_markitdown.py
```

Toàn bộ các tài liệu trong `knowledge/product/sources/` sẽ được số hóa thành các tệp tri thức cập nhật mới nhất, sẵn sàng phục vụ cho các role BA, SA, QA tham chiếu.
