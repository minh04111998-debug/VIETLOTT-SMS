# Self-Correction & Critique Loop Rules

> **Mục tiêu:** Định nghĩa quy chuẩn thống nhất cho vòng lặp kiểm tra chất lượng và tự sửa chữa của AI Agent, giải quyết triệt để sự mâu thuẫn giữa các tài liệu trước đây.

---

## 1. Giới Hạn Vòng Lặp Chuẩn (Canonical Limit: Max 2 Rounds)

Quy trình tự sửa chữa trong bước CRITIQUE tuân thủ nghiêm ngặt giới hạn: **Tối đa 2 vòng sửa sau bản thảo đầu tiên (Initial Draft + Max 2 Critique Fixes)**:

```text
[DRAFT BAN ĐẦU] ──> [CRITIQUE VÒNG 1] ──FAIL──> [SỬA LẦN 1] ──> [CRITIQUE VÒNG 2] ──FAIL──> [SỬA LẦN 2] ──> [CRITIQUE VÒNG 3]
                                                                                                                   │
                                                                                                                  FAIL
                                                                                                                   │
                                                                                                                   ▼
                                                                                                       🛑 DEADLOCK ESCALATION
```

---

## 2. Giao Thức Leo Thang Bế Tắc (Deadlock Escalation Protocol)

Nếu sau **2 vòng sửa** (tức là bước CRITIQUE thất bại lần thứ 2 liên tiếp), hệ thống **BẮT BUỘC**:

1. **Dừng Ngay Lập Tức (`🛑 Hard Stop`):** Không cố gắng tạo vòng sửa thứ 3 trong vô vọng để tránh cạn kiệt Context Window và Hallucination.
2. **Lập Hồ Sơ Bất Đồng (Critique Conflict Dossier):** Ghi nhận chi tiết vào `observability/critique-conflicts/CC-[date]-[feature].md`.
3. **Báo Cáo Phân Xử Cho Human:**
   - Trình bày rõ: Lý do kiểm tra thất bại, 2 quan điểm trái chiều giữa các bên (ví dụ: BA muốn thêm nhiều trường validation, DEV cảnh báo ảnh hưởng latency p95).
   - Đưa ra 2 lựa chọn cụ thể để Human phê duyệt.
