# Designer Knowledge Reference — Typography, Color, Layout, Forms, Responsive

> **Nguồn:** NNGroup, Apple HIG, Material Design 3, WCAG 2.2
> **Mục đích:** Chi tiết kỹ thuật thiết kế. Lazy-load khi workflow hoặc SKILL.md gọi.

---

## Typography — Expert Level
```
Type scale có tỷ lệ (không phải tùy tiện):
- Modular scale: 1.25× hoặc 1.333× (Perfect Fourth)
- Tối đa 3 font weights trên 1 page (Regular, Medium, Bold)
- Line height: Body text 1.5-1.6em, Heading 1.1-1.2em
- Measure (line length): 45-75 characters optimal (không < 30, không > 90)
```

## Color — Expert Level
```
Color system (không chọn màu random):
- Primary: Brand color
- Secondary: Complement / accent
- Semantic: Success (green), Warning (yellow/orange), Error (red), Info (blue)
- Neutral: Grayscale cho backgrounds, borders, text

Rules:
- Test màu trong context dark/light mode
- Test contrast: WebAIM Contrast Checker
- Không chỉ dùng đỏ/xanh (colorblind users 8% nam)
- 60-30-10 rule: 60% dominant, 30% secondary, 10% accent
```

## Spacing & Layout
```
8px grid system:
- Mọi spacing = bội số 8: 8, 16, 24, 32, 40, 48, 64, 80
- Padding/margin nhất quán
- Content max-width: 720px-1200px tùy loại

Touch targets (mobile):
- Min 44×44px (HIG) hoặc 48×48px (Material)
- Spacing giữa targets ≥ 8px
- Thumb-zone optimization
```

## Forms — Critical UX
```
□ Label trên input (không placeholder-only)
□ Real-time validation
□ Error message cụ thể: "Email phải chứa '@'" ✓
□ Progress indicator cho multi-step
□ Preserve input sau error
□ Auto-complete hints
□ Tab order logical, Enter submit
□ Required vs Optional rõ ràng
```

## Responsive Design
```
Breakpoints (Mobile-First):
- xs: < 480px | sm: 480–767px | md: 768–1023px | lg: 1024–1279px | xl: ≥ 1280px

Hierarchy khi thu nhỏ:
1. Ẩn secondary content
2. Stack horizontal → vertical
3. Hamburger menu (khi necessary)
4. Tăng touch targets
5. Single-column layout
```
