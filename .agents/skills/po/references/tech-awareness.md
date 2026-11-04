# Technology Awareness for PO

> Tham chiếu từ: `.agents/skills/po/SKILL.md` — Section POA-D1.4 (Apply Foundational Concepts)
> **Mục đích:** PO không cần code — nhưng cần hiểu đủ để ra quyết định đúng về timeline, feasibility, và trade-off.

---

## Những gì PO cần biết (không cần code được)

### Frontend / Backend / API
```
Frontend: Cái người dùng nhìn thấy và tương tác (React, Vue, Mobile app)
Backend: Logic xử lý ở server (API, Business logic, Auth)
API: Cầu nối giữa Frontend và Backend (REST/GraphQL)
Database: Nơi lưu trữ dữ liệu

→ PO cần hiểu: Thay đổi UI ≠ thay đổi Backend (có thể làm riêng lẻ)
→ PO cần hiểu: API integration với 3rd party có thể limit feature
```

### Tech Debt
```
Tech debt = "Nợ kỹ thuật" tích lũy do code nhanh, cut corners
Ảnh hưởng: Tốc độ dev chậm lại, bug nhiều, khó thêm feature mới
PO cần làm: Dành ~20% sprint capacity cho tech debt repayment
Không để dev nợ tích lũy > 30% tổng effort → breaking point
```

### Câu hỏi PO nên hỏi Dev (thay vì "bao lâu xong?")
```
"Rủi ro kỹ thuật lớn nhất của feature này là gì?"
"Dependency nào với hệ thống khác? Có thể làm song song không?"
"Nếu scale lên 10x user, approach này có hold không?"
"Tech debt nào đang block feature này? Ta có nên address trước không?"
"Build vs Buy: Có library/service nào giải được không? Chi phí so với tự build?"
"Phần nào có thể release independent (tránh big bang release)?"
```

### Build vs Buy vs Partner
```
Build: Khi đây là core competitive advantage
Buy: Khi đây là commodity feature, có vendor tốt
Partner: Khi cần speed-to-market, có thể switch vendor sau

Ví dụ: Authentication → Buy (Auth0/Firebase). Search → Build nếu là core value, Buy nếu commodity.
```

---

## Cloud & SaaS Basics

> **Tại sao PO cần biết:** Quyết định infrastructure ảnh hưởng trực tiếp đến cost, scalability, và release strategy.

```
SaaS: Software as a Service — User dùng qua browser, không cài đặt
      VD: Google Workspace, Slack, Jira
      PO impact: Có thể release liên tục, user luôn dùng bản mới nhất

PaaS: Platform as a Service — Dev deploy code, platform lo hạ tầng
      VD: Heroku, Google App Engine, Azure App Service
      PO impact: Dev focus vào feature thay vì quản lý server

IaaS: Infrastructure as a Service — Thuê máy chủ ảo, tự quản lý
      VD: AWS EC2, Azure VM, Google Compute Engine
      PO impact: Linh hoạt nhất nhưng cần DevOps team mạnh

Câu hỏi PO nên hỏi:
- "Hosting cost hàng tháng ước lượng bao nhiêu? Scale lên 10x thì sao?"
- "Có vendor lock-in không? Nếu cần chuyển provider thì effort bao nhiêu?"
- "Data lưu ở đâu? Có comply với quy định lưu trữ trong nước không?"
```

---

## Data Privacy & Compliance

> **Tại sao PO cần biết:** Feature vi phạm quy định → phạt, mất uy tín, phải rework.

```
PDPA (Việt Nam — NĐ 13/2023): Nghị định bảo vệ dữ liệu cá nhân
GDPR (EU): General Data Protection Regulation
PCI-DSS: Chuẩn bảo mật thanh toán thẻ

Câu hỏi PO PHẢI hỏi trước khi ship feature có personal data:
1. "Feature này collect dữ liệu cá nhân gì? Có cần consent không?"
2. "User có thể request xóa data (Right to be Forgotten) không?"
3. "Data lưu bao lâu? Có retention policy chưa?"
4. "Có transfer data ra nước ngoài không? (Cross-border transfer)"
5. "Payment feature có cần PCI-DSS compliance không?"

→ PO không cần biết implement thế nào — nhưng PHẢI biết feature có cần compliance check không,
  và PHẢI tag SA/DevOps review trước khi commit vào roadmap.
```

> **Nguồn:** [Nghị định 13/2023/NĐ-CP](https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Nghi-dinh-13-2023-ND-CP-bao-ve-du-lieu-ca-nhan-357191.aspx)

---

## AI/ML Basics cho PO

> **Tại sao PO cần biết:** Ngày càng nhiều feature có AI — PO cần biết khi nào AI hợp lý, khi nào là overkill.

```
Khi nào dùng AI/ML:
✅ Pattern phức tạp, human khó detect (fraud, recommendation, sentiment)
✅ Có đủ data lịch sử (>10k samples cho supervised learning)
✅ Accuracy 80-90% đã acceptable (không cần 100%)

Khi nào KHÔNG dùng AI:
❌ Logic rõ ràng, if-else đủ → Rule-based engine rẻ hơn, nhanh hơn
❌ Data < 1000 samples → Underfitting, model kém
❌ Cần 100% accuracy (y tế, pháp lý) → AI không guarantee

Câu hỏi PO nên hỏi:
- "Feature này cần AI thật hay rule-based đủ?"
- "Data training từ đâu? Có đủ lượng và chất lượng không?"
- "Accuracy target bao nhiêu? 80%? 95%? Có acceptable không?"
- "Model cần retrain bao thường xuyên? Cost retrain bao nhiêu?"
- "Nếu AI sai, fallback plan cho user là gì?"
```

---

## Microservices vs Monolith

> **Tại sao PO cần biết:** Kiến trúc ảnh hưởng đến release strategy, team structure, và feature coupling.

```
Monolith: 1 codebase, 1 deployment
  ✅ Đơn giản, nhanh bắt đầu, team nhỏ (< 10 devs)
  ❌ Deploy 1 feature = deploy cả hệ thống, high risk
  → PO: Release lớn, ít thường xuyên, regression risk cao

Microservices: Nhiều service nhỏ, deploy độc lập
  ✅ Team lớn, release independent, scale từng phần
  ❌ Phức tạp, cần DevOps mạnh, debugging khó hơn
  → PO: Release nhỏ, thường xuyên, feature toggle dễ

Câu hỏi PO nên hỏi:
- "Feature mới ảnh hưởng bao nhiêu service?"
- "Deploy feature này có cần deploy thêm service khác không?"
- "Nếu service X down, feature Y có bị ảnh hưởng không?"
```

> **Nguồn:** [Inspired — Marty Cagan, Chapter 11](https://www.svpg.com/inspired-how-to-create-products-customers-love/), [Building Microservices — Sam Newman](https://samnewman.io/books/building_microservices_2nd_edition/)
