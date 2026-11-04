---
name: da-visualization
description: Dashboard design, data cleaning, Google Sheets→BI migration, PowerBI MCP integration
---

# Kỹ Năng: Dashboard Design & Data Tools

---

## 1. Kỹ Thuật Trực Quan Hóa (Dashboard Design)

**3 cấp layout:**
- **Cấp 1 (High-Level KPIs):** Trên cùng. Tổng doanh thu, Tổng user mới, Tổng vé bán ra + % biến động (Xanh/Đỏ).
- **Cấp 2 (Trend & Distribution):** Giữa. Line chart (xu hướng), Pie chart (cơ cấu sản phẩm).
- **Cấp 3 (Detailed Data):** Dưới cùng. Bảng số liệu chi tiết cho deep-dive.

## 2. Xử Lý Google Sheets to Dashboard

- Cấu trúc bảng dữ liệu phẳng (Flat table) để kết nối BI tools
- Làm sạch: Bỏ merge cells, chuẩn hóa ngày tháng, fill missing values
- Gợi ý kết nối: Google Data Studio / Looker Studio / PowerBI

## 3. Tích Hợp PowerBI Modeling (MCP Server)

Khi dự án có mô hình PowerBI (`.pbip`, `*.SemanticModel`):
- **MCP Server:** `powerbi-modeling` (truy cập qua `call_mcp_tool`)
- **Năng lực:**
  - Chạy DAX queries (`dax_query_operations`)
  - Đọc/tối ưu Measures, Calculated Columns (`measure_operations`, `column_operations`)
  - Khám phá Table Relationships và Schema (`table_operations`, `relationship_operations`)
- **Quy tắc:** Kiểm tra tính chính xác công thức trước khi xuất báo cáo
