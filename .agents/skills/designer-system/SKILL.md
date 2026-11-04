---
name: designer-system
description: Design system setup, design tokens, Figma import, responsive design patterns, component architecture
---

# Kỹ Năng: Design System & Components

---

## 1. Design System Setup
**Cấu trúc:** Foundations (colors, typography, spacing) → Atoms → Molecules → Organisms → Templates → Pages
**Nguyên tắc:** Single source of truth | Consistent naming | Version controlled

## 2. Design Token System
**Categories:**
- **Color tokens:** Primary, Secondary, Neutral, Semantic (success/warning/error/info)
- **Typography tokens:** Font family, size scale, weight, line-height
- **Spacing tokens:** 4px grid (4, 8, 12, 16, 24, 32, 48, 64)
- **Elevation tokens:** Shadow levels (sm, md, lg, xl)
- **Border tokens:** Radius, width, style

## 3. Import Design System (Figma)
**Quy trình:**
1. Export tokens từ Figma (plugin: Tokens Studio)
2. Convert to CSS variables / Flutter theme
3. Map Figma components → Code components
4. Setup Storybook / Widget catalog

## 4. Responsive Design Patterns
**Breakpoints:** Mobile (360px) | Tablet (768px) | Desktop (1024px) | Wide (1440px)
**Patterns:** Stack (mobile) → Grid (tablet) → Multi-column (desktop)
**Touch targets:** Min 44×44px (iOS), 48×48dp (Android)

## 5. Component Architecture
**Atomic Design:** Atom (Button, Input) → Molecule (Search Bar) → Organism (Header) → Template → Page
**Naming:** `[category]-[name]-[variant]` (VD: `btn-primary-lg`)

## 6. Information Architecture Blueprint
**Card Sorting:** Open sort (users create categories) | Closed sort (predefined categories)
**Output:** Site map + Navigation structure + Label taxonomy
