---
name: ba-change
description: Kỹ năng quản lý thay đổi — Impact Analysis, Cascading Update, Dependency Graph, Impact Scoring, Communication Plan, Version Control
---

# Kỹ Năng: Change Management

> **Shared resources:** `../ba/references/change-templates.md`, `../ba/examples/cm-examples.md`
> **Nguồn gốc:** Gộp từ Change Manager role. Benchmark: Prosci ADKAR + ITIL + BABOK KA5.

---

## 1. Impact Analysis Report

> **Kích hoạt:** Khi nhận được Change Request (CR) từ khách hàng hoặc nội bộ.

**Mục tiêu:** Xác định đầy đủ mọi tài liệu, module, và rủi ro bị ảnh hưởng.

**Output:** Impact Analysis Report đánh giá 4 layers:
- Layer 1: Requirements (PRD/SRS/User Story/AC)
- Layer 2: Design (Mockup/ADR)
- Layer 3: Technical (API spec/DB schema)
- Layer 4: Testing (Test Plan/Test Cases)

→ Template: `../ba/references/change-templates.md` §2 | Ví dụ: `../ba/examples/cm-examples.md` §1

## 2. Quy Trình Cập Nhật Chuỗi (Cascading Process)

> **Kích hoạt:** CR đã được approve, cần cập nhật tất cả tài liệu bị ảnh hưởng.

**Quy trình:**
1. Tiếp nhận CR → Ghi nhận yêu cầu thay đổi rõ ràng
2. Lập Impact Analysis (§1)
3. Xin Approve: Trình bày Impact Analysis cho PM/PO
4. Cập nhật SRS/User Story
5. Trigger Designer cập nhật UI (nếu có)
6. Trigger DEV & QA bắt đầu code và test dựa trên tài liệu đã update

→ Template checklist: `../ba/references/change-templates.md` §3

## 3. Impact Scoring Matrix

> **Kích hoạt:** Cần so sánh mức độ ảnh hưởng giữa nhiều CRs để prioritize.

**6 Dimensions:** Scope (20%) | Documents affected (20%) | Code changes (15%) | Testing effort (15%) | User impact (15%) | Risk level (15%)

**Classification:**
| Score | Level | Action |
|-------|-------|--------|
| 1.0-1.5 | 🟢 Minor | BA tự xử lý, log CR |
| 1.6-2.5 | 🟡 Moderate | Impact Analysis required |
| 2.6-3.5 | 🟠 Significant | Full impact + PM/PO review |
| 3.6-5.0 | 🔴 Major | War room + PM/PO/BA review |

→ Ví dụ scoring: `../ba/examples/cm-examples.md` §1

## 4. Change Communication Plan

> **Kích hoạt:** CR được approve và cần thông báo đến các bên liên quan.

**Output:**
- What Changed? (Before → After)
- Who Is Affected? (Table: Team/Role → Impact → Action Required → Deadline)
- Documents Updated (Table: Document → Version → Changes → Updated By)
- Timeline (Milestones → Date → Status)

→ Template: `../ba/references/change-templates.md` §4

## 5. Document Version Control

> **Kích hoạt:** Cần track phiên bản tài liệu qua nhiều change requests.

**Versioning Rules:**
- Major version (X.0): Structural change, new feature area
- Minor version (x.Y): Content update within existing structure
- Format: `v[Major].[Minor]` — ví dụ: v2.3
- Mỗi CR tạo ít nhất 1 minor version bump
- Header mỗi document PHẢI có: Version, Last Updated, CR Reference

**Output:** Document Version Registry + Version Change Log
