---
name: ba-diagrams
description: Kỹ năng vẽ luồng nghiệp vụ bằng Mermaid — Activity, State, BPMN, Context, Decision Table/Tree, Dependency Graph
---

# Kỹ Năng: Diagrams & Visual Modeling

> **Shared resources:** `../ba/templates/diagram-templates.md`, `../ba/references/`

---

## 1. Activity Diagram

> **Kích hoạt:** Cần trực quan hóa luồng xử lý tuần tự của một chức năng.

Dùng `flowchart TD` với hình thoi cho decision, viên thuốc cho start/end.
→ Mẫu: `../ba/templates/diagram-templates.md` §1

## 2. Vẽ Luồng Nghiệp Vụ (Business Flow)

> **Kích hoạt:** Cần trực quan hóa quy trình, luồng dữ liệu hoặc hành trình người dùng.

**Quy tắc:** `flowchart TD`, hình thoi cho decision, label trên mũi tên, viên thuốc cho start/end.
→ `../ba/templates/diagram-templates.md` §3

## 3. Decision Table / Decision Tree

> **Kích hoạt:** Business logic có nhiều nhánh if-else, nhiều điều kiện kết hợp.

- **Decision Table:** Nhiều điều kiện ngang nhau → bảng combinations
- **Decision Tree:** Logic phân cấp → Mermaid graph TD
→ `../ba/templates/diagram-templates.md` §4

## 4. State Diagram (Mô Hình Trạng Thái)

> **Kích hoạt:** Đối tượng có nhiều trạng thái (order, ticket, approval) cần mô tả transitions.

Liệt kê states → Xác định events/triggers → Guards/conditions → Terminal states → Vẽ Mermaid stateDiagram
→ `../ba/templates/diagram-templates.md` §5

## 5. BPMN Process Modeling

> **Kích hoạt:** Quy trình nghiệp vụ cross-department, cần swimlane.

Dùng Mermaid flowchart với subgraph (simulated swimlane), mỗi subgraph = 1 department/role.
→ `../ba/templates/diagram-templates.md` §6

## 6. Context Diagram (Scope Modeling)

> **Kích hoạt:** Bắt đầu phân tích hệ thống mới, cần xác định ranh giới.

Output: Context Diagram (Mermaid) — hệ thống ở giữa, external entities xung quanh.
→ `../ba/templates/diagram-templates.md` §7

## 7. Dependency Graph Builder

> **Kích hoạt:** Cần visualize mối quan hệ giữa các tài liệu/components trước khi thay đổi.

**Quy trình:**
1. Xác định **điểm bắt đầu** của change (node nào bị thay đổi?)
2. Trace **downstream** — tất cả nodes phụ thuộc vào nó
3. Mỗi downstream node = 1 item trong Cascading Checklist
4. Ưu tiên update từ **upstream → downstream** (BRD trước, TC sau)

**Output:** Mermaid `graph TD` với color-coded nodes + Dependency Table (Source → Depends On → Depended By → 🔴/🟡/🟢)

## 8. Functional Decomposition

> **Kích hoạt:** Cần phân rã hệ thống/module lớn thành các chức năng nhỏ hơn để ước lượng và phân công.

**Quy trình:** Xác định module cấp cao → Phân rã 2-4 cấp → Mỗi leaf = 1 potential User Story → Vẽ Mermaid graph TD
→ Nguồn: [BABOK® v3, Technique #22](https://www.iiba.org/standards-and-resources/babok/)

## 9. Concept Modelling

> **Kích hoạt:** Cần mô hình hóa các khái niệm nghiệp vụ và mối quan hệ giữa chúng.

Output: Concept Map (Mermaid graph) — mỗi node = 1 business concept, mỗi edge = relationship.
→ Nguồn: [BABOK® v3, Technique #11](https://www.iiba.org/standards-and-resources/babok/)

## 10. Organizational Modelling

> **Kích hoạt:** Cần hiểu cấu trúc tổ chức, đơn vị nào liên quan đến dự án.

Output: Organization Chart (Mermaid) + Stakeholder mapping per department.
→ Nguồn: [BABOK® v3, Technique #32](https://www.iiba.org/standards-and-resources/babok/)

## 11. Mind Mapping

> **Kích hoạt:** Giai đoạn diverge ý tưởng, cần brainstorm tự do.

AI có thể tạo Mermaid mindmap (experimental) để tổng hợp kết quả sau brainstorm.
Hướng dẫn: Sử dụng Miro/FigJam/XMind → AI cấu trúc output thành requirements.
→ Nguồn: [BABOK® v3, Technique #29](https://www.iiba.org/standards-and-resources/babok/)
