---
name: ba-requirements
description: Kỹ thuật thu thập, tài liệu hóa yêu cầu phần mềm — SRS, BRD, Use Case, NFR, Scope, Glossary, Traceability
---

# Kỹ Năng: Thu Thập & Tài Liệu Hóa Yêu Cầu

> **Shared resources:** `../ba/templates/`, `../ba/references/`, `../ba/examples/`

---

## 1. Kỹ Thuật Thu Thập Yêu Cầu

> **Kích hoạt:** Bắt đầu dự án mới hoặc thu thập yêu cầu cho module mới.

- **Phỏng vấn Stakeholder:** Chuẩn bị câu hỏi As-Is / To-Be / Ràng buộc → `../ba/references/analysis-frameworks.md` §1
- **Workshop Facilitation:** Brainstorming, Affinity Mapping, Dot Voting (5-8 người, gửi agenda trước 2-3 ngày)

## 2. Tạo SRS Document

> **Kích hoạt:** Cần tài liệu hóa yêu cầu chức năng và phi chức năng.

**Quy trình:** Xác định phạm vi → Vẽ Use Case → Viết Use Case chi tiết → Xác định NFR → Review & Sign-off
→ Template: `../ba/templates/document-templates.md` §1

## 3. Data Dictionary

> **Kích hoạt:** Cần mô tả cấu trúc dữ liệu entity.

Output: Bảng mô tả trường, kiểu, ràng buộc, mối quan hệ.
→ Template: `../ba/templates/document-templates.md` §3

## 4. Traceability Matrix

> **Kích hoạt:** Cần truy vết từ Business Rule → FR → Use Case → User Story → Test Case.

**PHẢI** duy trì truy vết xuyên suốt.
→ Template: `../ba/templates/document-templates.md` §4

## 5. NFR Analysis (FURPS+ Framework)

> **Kích hoạt:** Cần viết đặc tả yêu cầu phi chức năng. TUYỆT ĐỐI không bỏ qua.

5 khía cạnh: Performance | Reliability | Usability | Security | Supportability
→ Template: `../ba/templates/document-templates.md` §5

## 6. Interface Analysis

> **Kích hoạt:** Tích hợp 3rd party hoặc nhiều module internal cần giao tiếp.

Đặc tả: Loại interface, Data Contract, Error Handling, SLA
→ Template: `../ba/templates/document-templates.md` §6

## 7. Scope Modeling (Context Diagram)

> **Kích hoạt:** Bắt đầu phân tích hệ thống mới, cần xác định ranh giới.

Output: Context Diagram (Mermaid) + Scope Statement (In/Out Scope, Assumptions, Constraints)
→ Template: `../ba/templates/document-templates.md` §7 + `../ba/templates/diagram-templates.md` §7

## 8. Business Glossary

> **Kích hoạt:** Stakeholder và DEV hiểu cùng 1 thuật ngữ theo nghĩa khác nhau.

Glossary là **living document**. Mỗi thuật ngữ có **1 định nghĩa duy nhất** + cột "Không phải là".
→ Template: `../ba/templates/document-templates.md` §8

## 9. Requirements Lifecycle Management

> **Kích hoạt:** Cần track trạng thái requirements, duy trì traceability, hoặc handle change request.

Output: Requirements Status Dashboard + Traceability Matrix + Change Log
→ Template: `../ba/templates/document-templates.md` §9

## 10. Meeting Notes → Structured AC

> **Kích hoạt:** User paste meeting notes lộn xộn, cần cấu trúc lại thành AC.

**Quy trình:** Parse → Extract Business Rules Ẩn → Draft AC (Given/When/Then) → Cross-Review → Highlight Open Items
→ `../ba/references/analysis-frameworks.md` §3

## 11. User Story Mapping (Jeff Patton)

> **Kích hoạt:** Cần tổ chức requirements theo trải nghiệm người dùng, xác định release scope, hoặc tìm Walking Skeleton cho MVP.

**Quy trình:** Identify Activities (backbone) → Break into Tasks → Prioritize vertically → Draw release lines
**Walking Skeleton:** Bộ tối thiểu stories xuyên suốt backbone để demo end-to-end.
→ Nguồn: [User Story Mapping — Jeff Patton, O'Reilly 2014](https://www.oreilly.com/library/view/user-story-mapping/9781491904893/)

## 12. Tự Động Tạo Jira Task

> **Kích hoạt:** User yêu cầu "tạo task", "đẩy lên Jira".

Thu thập: Project Key + Summary + Description → Gọi script Python
→ `../ba/references/analysis-frameworks.md` §8

## 13. Roles & Permissions Matrix

> **Kích hoạt:** Cần đặc tả phân quyền cho hệ thống — ai được làm gì.

Output: Bảng CRUD per role per function.
→ Template: `../ba/templates/document-templates.md` §11
→ Nguồn: [BABOK® v3, Technique #39](https://www.iiba.org/standards-and-resources/babok/)

## 14. Giao Tiếp Stakeholder

> **Kích hoạt:** Cần soạn email, meeting request, báo cáo tiến độ, hoặc escalation.

4 mẫu: Confirmation Request | Escalation | Meeting Agenda | Status Update
→ Templates: `../ba/templates/email-templates.md`
**Nguyên tắc:** Ngôn ngữ nghiệp vụ | 1 email = 1 chủ đề | Action-oriented | Deadline cụ thể
