---
name: ba-analysis
description: Kỹ năng phân tích nghiệp vụ nâng cao — Gap Analysis, Edge Cases, 5 Whys, SWOT, BABOK KA5 techniques
---

# Kỹ Năng: Phân Tích Nghiệp Vụ Nâng Cao

> **Shared resources:** `../ba/references/analysis-frameworks.md`, `../ba/references/babok-knowledge-areas.md`

---

## 1. Gap Analysis

> **Kích hoạt:** Cần so sánh quy trình hiện tại (As-Is) với mong muốn (To-Be).

Output: Gap Matrix + Đề Xuất Lộ Trình (Phase 1/2/3)
→ Template: `../ba/templates/document-templates.md` §2

## 2. Phân Tích Ngoại Lệ & Rủi Ro (Edge Case Analyzer)

> **Kích hoạt:** Cần rà soát lỗ hổng logic hoặc viết AC phần Unhappy Path.

Quét 8 nhóm: 🔲 Empty States | 🔴 Error States | 📏 Limits | 🔐 Permissions | ⚡ Concurrency | ⏱️ Timeout & Latency | 🔄 Retry & Recovery | 🔗 Integration Failure
→ `../ba/references/analysis-frameworks.md` §2 + §2b (Timeout & Hung State Protocol)

## 3. Phân Tích Dữ Liệu & Tài Liệu

> **Kích hoạt:** User cung cấp file Excel cũ, file log, hoặc bản Word mô tả quy trình lộn xộn.

Phân tích As-Is Data → Khai phá Business Rule → Phát hiện Anomaly
→ `../ba/references/analysis-frameworks.md` §5

## 4. Wireframe Dạng Text (Low-Fidelity ASCII)

> **Kích hoạt:** Cần chốt luồng thao tác nhanh trước khi Designer vẽ UI/UX.

Dùng ASCII block mô tả Content + Call-to-Action, KHÔNG quan tâm cái đẹp.
→ `../ba/references/analysis-frameworks.md` §6

## 5. Phân Tích Nguyên Nhân Gốc Rễ (5 Whys)

> **Kích hoạt:** Stakeholder yêu cầu "Giải pháp" thay vì đưa ra "Vấn đề nghiệp vụ".

Áp dụng 5 Whys để lột bỏ lớp vỏ giải pháp bề mặt. BA KHÔNG lập tức viết Use Case cho yêu cầu dạng này.
→ `../ba/references/analysis-frameworks.md` §7

## 6. Solution Options Analysis (BABOK KA5)

> **Kích hoạt:** Có nhiều phương án giải pháp nghiệp vụ, cần trình stakeholder chọn.
> **Lưu ý:** BA đề xuất giải pháp **nghiệp vụ** (Business Solution), KHÔNG phải giải pháp kỹ thuật.

Output: Bảng so sánh 2-3 options với Pros/Cons/Effort/Risk + BA recommendation kèm rationale.
→ Template: `../ba/templates/document-templates.md` §13
→ Nguồn: [BABOK® v3, KA5 Task 6.5](https://www.iiba.org/standards-and-resources/babok/)

## 7. Value Analysis (BABOK KA5)

> **Kích hoạt:** Bắt đầu phân tích module mới, cần đánh giá "có đáng làm không?" TRƯỚC khi tốn effort.

**Quy trình:** Problem → Proposed Solution → Target Users → Expected Benefit → Success KPI → Cost → Risk → GO/NO-GO
→ `../ba/references/babok-knowledge-areas.md` KA5

## 8. Balanced Scorecard

> **Kích hoạt:** Cần đánh giá strategy alignment từ 4 góc nhìn cân bằng.

4 Perspectives: Financial | Customer | Internal Process | Learning & Growth
→ Nguồn: [Balanced Scorecard — Kaplan & Norton, 1992](https://hbr.org/1992/01/the-balanced-scorecard-measures-that-drive-performance-2)

## 9. Business Capability Analysis

> **Kích hoạt:** Cần hiểu tổ chức CÓ THỂ LÀM GÌ (capabilities) trước khi xác định requirements.

Liệt kê capabilities → Đánh giá maturity (1-5) → Xác định gaps → Map requirements vào capabilities cần nâng cấp
→ Nguồn: [BABOK® v3, Technique #6](https://www.iiba.org/standards-and-resources/babok/)

## 10. Business Cases

> **Kích hoạt:** Cần justify đầu tư cho dự án/feature — trình ban lãnh đạo.

Output: Problem Statement → Proposed Solution → Cost-Benefit Analysis → Risk → Recommendation → Timeline
→ `../ba/references/analysis-frameworks.md` §11

## 11. Collaborative Games

> **Kích hoạt:** Cần prioritize features với stakeholder một cách interactive.
> ⚠️ AI hỗ trợ chuẩn bị, KHÔNG trực tiếp chạy game.

Games: Buy a Feature | Prune the Product Tree | Speed Boat
→ Nguồn: [Innovation Games — Luke Hohmann](https://www.innovationgames.com/)

## 12. Financial Analysis

> **Kích hoạt:** Cần phân tích tài chính cho Business Case hoặc solution evaluation.

Phương pháp: ROI | Payback Period | NPV | TCO
→ Nguồn: [BABOK® v3, Technique #20](https://www.iiba.org/standards-and-resources/babok/)

## 13. SWOT Analysis

> **Kích hoạt:** Cần đánh giá chiến lược cho dự án/solution.

4 góc: Strengths (nội bộ) | Weaknesses (nội bộ) | Opportunities (bên ngoài) | Threats (bên ngoài)
→ Nguồn: [SWOT Analysis — Albert Humphrey, Stanford Research Institute](https://en.wikipedia.org/wiki/SWOT_analysis)

## 14. Vendor Assessment

> **Kích hoạt:** Cần đánh giá nhà cung cấp / quyết định Build vs Buy vs Partner.

Output: Weighted scoring table (7 dimensions) + Recommendation.
→ Nguồn: [BABOK® v3, Technique #49](https://www.iiba.org/standards-and-resources/babok/)

## 15. Lessons Learned

> **Kích hoạt:** Kết thúc dự án/release/sprint, cần tổng kết bài học.

Output: What went well / What didn't / What to do differently + BA Process Metrics.
→ Template: `../ba/templates/document-templates.md` §12
