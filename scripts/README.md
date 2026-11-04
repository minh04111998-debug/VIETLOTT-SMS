# Utility Scripts — Vietlott SMS

Thư mục này chứa toàn bộ các kịch bản tự động hóa (PowerShell & Python 3) phục vụ quy trình phát triển, kiểm thử, phân tích dữ liệu và trích xuất tài liệu.

---

## 1. Nhóm Chuyển Đổi & Bóc Tách Văn Bản (Document Conversion)

| Script | Ngôn ngữ | Chức năng | Cách chạy |
|---|---|---|---|
| `export_docx.ps1` | PowerShell | Chuyển đổi Markdown sang DOCX chuyên nghiệp (dùng Pandoc) | `.\scripts\export_docx.ps1 -InputFile file.md` |
| `read_excel.ps1` | PowerShell | Đọc và hiển thị nội dung file bảng tính XLSX | `.\scripts\read_excel.ps1 -Path data.xlsx` |
| `convert_word_to_md.py` | Python 3 | Chuyển đổi tài liệu DOCX sang Markdown chuẩn cấu trúc | `python scripts/convert_word_to_md.py` |
| `convert_md_to_html.py` | Python 3 | Chuyển đổi file Markdown sang giao diện HTML có style hiện đại | `python scripts/convert_md_to_html.py` |
| `convert_md_to_html_full.py` | Python 3 | Chuyển đổi Markdown sang HTML đầy đủ mục lục và giao diện responsive | `python scripts/convert_md_to_html_full.py` |
| `convert_standalone.py` | Python 3 | Đóng gói HTML thành file độc lập (nhúng css/js inline) | `python scripts/convert_standalone.py` |
| `extract_all.py` / `extract_docx.py` | Python 3 | Trích xuất toàn bộ văn bản và bảng biểu từ tài liệu Word gốc | `python scripts/extract_docx.py` |
| `extract_strings.py` | Python 3 | Trích xuất chuỗi ký tự và metadata văn bản | `python scripts/extract_strings.py` |
| `merge_docx.py` / `merge_markdown.py` | Python 3 | Hợp nhất nhiều file docx hoặc markdown thành một tài liệu duy nhất | `python scripts/merge_markdown.py` |
| `run_recursive_extract.py` | Python 3 | Trích xuất tài liệu đệ quy từ thư mục dữ liệu | `python scripts/run_recursive_extract.py` |

---

## 2. Nhóm Sinh Sơ Đồ Kiến Trúc & Xử Lý Layout (Diagram Generation & Layout)

| Script | Chức năng | Đầu ra |
|---|---|---|
| `generate_all_diagrams.py` | Tự động sinh toàn bộ sơ đồ Draw.io từ đặc tả luồng | File `.drawio` và `.xml` |
| `generate_bpmn_diagram.py` | Sinh sơ đồ quy trình nghiệp vụ BPMN 2.0 | `knowledge/architecture/diagrams/` |
| `generate_drawio_xml.py` | Sinh mã XML cho biểu đồ Draw.io từ mô hình dữ liệu | File XML |
| `generate_svg_swimlane.py` | Sinh sơ đồ làn bơi (Swimlane diagram) định dạng SVG vector | File `.svg` |
| `generate_svg_b64.py` | Mã hóa sơ đồ SVG sang định dạng Base64 phục vụ nhúng HTML | Chuỗi Base64 |
| `generate_mapping.py` | Sinh ma trận ánh xạ nghiệp vụ giữa các thành phần | File JSON/Markdown |
| `combine_all_diagrams.py` | Hợp nhất nhiều sơ đồ thành một bản vẽ tổng hợp | File diagram tổng hợp |
| `fix_all_diagram_layouts.py` | Cân chỉnh layout tự động cho hệ thống diagram | Diagram đã định dạng |
| `fix_all_diagram_overlaps.py` | Tự động cân chỉnh vị trí node để không bị đè chữ trong Draw.io | File `.drawio` đã căn lề |
| `fix_svg_overlap.py` | Xử lý đè chữ và chồng lấn trong file vector SVG | File SVG đã chuẩn hóa |

---

## 3. Nhóm Kế Hoạch Phát Triển (Roadmap)

| Script | Chức năng dự kiến | Trạng thái |
|---|---|---|
| `apk_runtime_analyzer.py` | Phân tích file APK release, bóc tách AndroidManifest, permissions, API endpoints | *(Kế hoạch phát triển)* |
| `vietlott_proxy_logger.py` | Proxy logger ghi nhận traffic API giữa mobile app và server backend | *(Kế hoạch phát triển)* |
| `fetch_reviews.py` | Thu thập đánh giá người dùng Vietlott SMS trên Google Play / App Store | *(Kế hoạch phát triển)* |
| `setup_adb_environment.ps1` | Thiết lập môi trường Android Debug Bridge (ADB) để debug thiết bị thật | *(Kế hoạch phát triển)* |

---

## 4. Thư Mục Phân Nhóm Chức Năng (Organized Subdirectories)

- `scripts/diagrams/`: Chứa 10 scripts tự động sinh sơ đồ Draw.io, BPMN 2.0, SVG swimlane và căn chỉnh layout.
- `scripts/converters/`: Chứa 5 scripts chuyển đổi định dạng (Markdown sang HTML, Word sang Markdown, đóng gói standalone).
- `scripts/extractors/`: Chứa 5 scripts trích xuất đệ quy văn bản, chuỗi ký tự và bảng biểu từ dữ liệu gốc.
- `scripts/archive/`: Chứa các script one-off từ các đợt refactor link/tài liệu trước đây.
- `scripts/migration/`: Chứa các script PowerShell phục vụ đợt di chuyển cấu trúc sang mô hình 20 thành phần.
- `scripts/screenshots/`: Thư mục lưu trữ ảnh chụp màn hình tự động từ thiết bị di động.

