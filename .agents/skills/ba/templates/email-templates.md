# Mẫu Email Giao Tiếp Stakeholder (BA)

> Tham chiếu từ: `.agents/skills/ba/SKILL.md` — Section 9: Giao Tiếp Stakeholder

---

## 1. Email Yêu Cầu Xác Nhận (Confirmation Request)

```markdown
**Subject:** [Tên dự án] — Xin xác nhận yêu cầu: [Chủ đề cụ thể]

Kính gửi [Tên Stakeholder],

Sau buổi họp ngày [DD/MM/YYYY], tôi xin tổng hợp lại các yêu cầu đã thảo luận để anh/chị xác nhận:

**1. Yêu cầu đã thống nhất:**
- [BR-001]: [Mô tả]
- [BR-002]: [Mô tả]

**2. Điểm còn chờ xác nhận:**
- [ ] [Câu hỏi 1]
- [ ] [Câu hỏi 2]

**3. Hành động tiếp theo:**
| Hành động | Người phụ trách | Deadline |
|-----------|----------------|----------|

Xin anh/chị phản hồi trước **[DD/MM/YYYY]** để chúng tôi tiếp tục triển khai.

Trân trọng,
[Tên BA]
```

---

## 2. Email Escalation

```markdown
**Subject:** [URGENT] [Tên dự án] — Cần quyết định: [Chủ đề]

Kính gửi [Tên Leader/Sponsor],

Tôi xin báo cáo một vấn đề cần quyết định gấp trong dự án [Tên dự án]:

**Vấn đề:**
[Mô tả ngắn gọn, 2-3 câu]

**Tác động nếu không xử lý:**
- Timeline: [Trễ X ngày/sprint]
- Scope: [Ảnh hưởng module Y]
- Chi phí: [Tăng Z%]

**Các phương án:**
| # | Phương án | Ưu điểm | Nhược điểm | Effort |
|---|----------|---------|-----------|--------|
| A | [PA 1] | ... | ... | ... |
| B | [PA 2] | ... | ... | ... |

**Đề xuất:** Phương án [X] vì [lý do].

Kính mong anh/chị phản hồi trước **[DD/MM/YYYY HH:MM]**.

Trân trọng,
[Tên BA]
```

---

## 3. Meeting Request / Agenda

```markdown
**Subject:** [Tên dự án] — Mời họp: [Chủ đề] | [DD/MM/YYYY HH:MM]

**Mục đích:** [1 câu mô tả mục tiêu cuộc họp]
**Thời gian:** [DD/MM/YYYY] [HH:MM - HH:MM] ([X] phút)
**Địa điểm / Link:** [Phòng họp / Google Meet / Teams]
**Người tham gia:** [Danh sách tên + vai trò]

### Agenda
| # | Nội dung | Thời lượng | Người trình bày | Mục tiêu |
|---|---------|------------|----------------|----------|
| 1 | [Chủ đề 1] | [X phút] | [Tên] | Thông tin / Thảo luận / Quyết định |
| 2 | [Chủ đề 2] | [X phút] | [Tên] | ... |

### Chuẩn bị trước
- [ ] [Tài liệu cần đọc]
- [ ] [Câu hỏi cần chuẩn bị]
```

---

## 4. Status Update (Cho Stakeholder không kỹ thuật)

```markdown
## 📊 Cập Nhật Tiến Độ — [Tên dự án] | Tuần [N]

### Trạng thái: 🟢 Đúng tiến độ / 🟡 Cần chú ý / 🔴 Trễ

**Tóm tắt 1 câu:** [Mô tả ngắn gọn tình hình]

### ✅ Đã hoàn thành tuần này
- [Thành tựu 1 — diễn đạt theo ngôn ngữ nghiệp vụ, KHÔNG nói "code xong API"]
- [Thành tựu 2]

### 🔜 Kế hoạch tuần tới
- [Kế hoạch 1]

### ⚠️ Cần anh/chị hỗ trợ
- [Quyết định cần đưa ra — nếu có]
- [Thông tin cần cung cấp — nếu có]
```

---

## Nguyên Tắc Giao Tiếp

- **Ngôn ngữ nghiệp vụ**: Không dùng thuật ngữ kỹ thuật với stakeholder non-tech
- **1 email = 1 chủ đề**: Không trộn lẫn nhiều vấn đề
- **Action-oriented**: Mọi email phải có Call-to-Action rõ ràng (xác nhận, phản hồi, quyết định)
- **Deadline cụ thể**: Không viết "sớm nhất có thể" — ghi ngày giờ cụ thể
