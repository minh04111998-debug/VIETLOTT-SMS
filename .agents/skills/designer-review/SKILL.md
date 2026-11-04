---
name: designer-review
description: UX audit, design review, handoff checklist, WCAG compliance, user research toolkit
---

# Kỹ Năng: UX Audit & Design Review

---

## 1. UX Audit

> **Kích hoạt:** Đánh giá UX hiện tại, tìm pain points.

**Framework:** Nielsen's 10 Heuristics
**Output:** UX Audit Report — Heuristic | Issue | Severity | Screenshot | Recommendation
**Scoring:** 0 (No issue) → 4 (Catastrophe)

## 2. Design Review

> **Kích hoạt:** Review design trước khi chuyển sang DEV.

**Checklist:**
- [ ] Consistent with design system?
- [ ] Edge states handled? (empty, error, loading, success)
- [ ] Accessibility: contrast ratio ≥ 4.5:1, focus states, alt text
- [ ] Responsive: all breakpoints covered?
- [ ] Interaction: hover, active, disabled states defined?
- [ ] Copy: clear, concise, actionable?

## 3. Design Handoff Checklist

> **Kích hoạt:** Bàn giao design cho DEV.

- [ ] All screens finalized + approved by PO
- [ ] Design specs annotated (spacing, colors, font sizes)
- [ ] Assets exported (SVG icons, images)
- [ ] Interaction specs documented (animation, transitions)
- [ ] Responsive behavior documented
- [ ] Component mapping: Design component → Code component

## 4. WCAG 2.2 Compliance Checker

**Level AA Requirements:**
- [ ] Color contrast ≥ 4.5:1 (normal text), ≥ 3:1 (large text)
- [ ] Focus indicators visible
- [ ] Touch targets ≥ 24×24px
- [ ] Text resizable to 200%
- [ ] Alt text for all images
- [ ] Keyboard navigable
- [ ] Motion: reduce-motion media query supported

## 5. User Research Toolkit

### Persona Template
**Cấu trúc:** Name | Photo | Demographics | Goals | Frustrations | Tech Savviness | Quote
**Nguyên tắc:** Persona từ data thật (interview, analytics), KHÔNG tưởng tượng.

### Usability Testing Guide
**5-user rule:** 5 users phát hiện ~85% usability issues
**Script:** Intro (5min) → Warm-up (3min) → Tasks (20min) → Debrief (5min)
**Metrics:** Task success rate | Time on task | Error rate | SUS score
