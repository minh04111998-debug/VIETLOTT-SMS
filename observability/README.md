# Observability Layer — Hệ Thống Giám Sát Toàn Diện

> **Mục tiêu:** Đảm bảo 100% tính minh bạch trong mọi hoạt động của AI Agent, ngăn chặn ảo giác (Anti-Hallucination), ghi nhận mọi quyết định và rủi ro.

---

## Các Thành Phần Giám Sát Cốt Lõi:

1. `assumptions-log.md`: Sổ đăng ký mọi giả định nghiệp vụ phát sinh trong quá trình phân tích.
2. `open-questions.md`: Danh mục câu hỏi mở phân loại rõ ràng theo mức độ chặn đường (Blocking vs Non-blocking).
3. `decisions-log.md`: Sổ đăng ký các quyết định đã được phê duyệt chính thức bởi Human.
4. `risk-register.md`: Sổ quản trị rủi ro dự án định lượng theo xác suất và tác động.
5. `critique-conflicts/`: Nơi lưu trữ các hồ sơ bế tắc khi vòng lặp CRITIQUE thất bại > 2 lần (Deadlock Escalation).
6. `gate-reports/`: Nơi lưu trữ báo cáo tự động từ các công cụ kiểm tra chất lượng (Quality Gate Reports).
7. `observation-protocol.md`: Quy trình và chuẩn mực ghi nhật ký quan sát của hệ thống.
