# 📥 Source Registry — Nguồn Tài Liệu Tin Cậy

> **Mục đích:** AI CHỈ được trích dẫn từ các nguồn trong bảng này khi phân tích nghiệp vụ.
> Nếu cần thông tin ngoài danh sách → **PHẢI hỏi người dùng**, không tự suy diễn.
>
> **Cập nhật:** Human chịu trách nhiệm bổ sung/xóa nguồn. AI không tự thêm nguồn mới.

---

## Nguồn Tài Liệu Đã Đăng Ký

| ID | Nguồn | Đường dẫn | Loại | Độ tin cậy | Ghi chú |
|----|-------|-----------|------|------------|---------|
| SRC-01 | Tài liệu nghiệp vụ Vietlott SMS | `knowledge/product/vietlott-sms-overview.md SMS_ Tài liệu nghiệp vụ/` | Specs gốc | ⭐⭐⭐ Verified | Tài liệu chính thức từ Vietlott |
| SRC-02 | Tài liệu tích hợp kênh bán | `knowledge/product/vietlott-sms-overview.md SMS_Tích hợp kênh bán/` | API/Integration | ⭐⭐⭐ Verified | Specs kênh bán chính thức |
| SRC-03 | Tài liệu hệ thống VIETLOTT_SMS | `knowledge/product/vietlott-sms-overview.md` | System docs | ⭐⭐⭐ Verified | Tài liệu hệ thống gốc |
| SRC-04 | Tài liệu Xổ Số+ | `artifacts/requirements/Xổ Số+_Tài liệu nghiệp vụ/` | CTV/Agent | ⭐⭐⭐ Verified | Hệ thống CTV bán vé hộ |
| SRC-05 | Báo cáo doanh thu & TKDT | `artifacts/requirements/(2026) Báo cáo DT & TKDT*.xlsx` | Data | ⭐⭐⭐ Verified | Dữ liệu đối soát gốc |
| SRC-06 | SRS đã phê duyệt | `artifacts/requirements/srs-*.html` | Baseline SRS | ⭐⭐⭐ Verified | Specs đã sign-off |
| SRC-07 | Fintech Knowledge Base | `knowledge/product/fintech-knowledge-base.md` | Reference | ⭐⭐ AI-generated | Tổng hợp từ ~64 tài liệu, cần verify |
| SRC-08 | Project Context | `knowledge/product/project-context.md` | Project memory | ⭐⭐ Living doc | Bối cảnh dự án — cập nhật liên tục |
| SRC-09 | Template mẫu tổ chức | `templates/` | Templates | ⭐⭐⭐ Verified | BRD, SRS chuẩn tổ chức |
| SRC-10 | Biên bản họp | `artifacts/analysis/` | Meeting notes | ⭐⭐⭐ Verified | Biên bản họp với stakeholder |

---

## Quy Tắc Trích Dẫn

1. Mọi thông tin nghiệp vụ trích dẫn **PHẢI** ghi rõ: `[Nguồn: SRC-XX, mục/chương Y.Z]`
2. Nếu không tìm thấy nguồn phù hợp trong registry → gắn nhãn `[⚠️ KHÔNG CÓ NGUỒN — cần stakeholder xác nhận]`
3. Không được trích dẫn từ "kiến thức chung" hoặc "best practice ngành" mà không có reference cụ thể
