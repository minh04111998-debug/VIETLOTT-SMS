# Design System Specification

> **Mục đích**: File này là "nguồn chân lý" (Single Source of Truth) cho Design System của dự án.
> AI agent **PHẢI** đọc file này trước khi thiết kế bất kỳ màn hình nào.

> **Hướng dẫn sử dụng:**
> 1. Designer copy template này sang `artifacts/technical/design/design-system-spec.md`
> 2. Điền thông tin từ Figma (Inspect panel, Tokens plugin, hoặc Dev Mode)
> 3. Cập nhật khi Design System thay đổi → chạy `/change-request` nếu cần

---

## 📋 Metadata

| Mục | Giá trị |
|-----|---------|
| **Tên dự án** | [Tên dự án] |
| **Figma Link** | [URL Figma file] |
| **Phiên bản DS** | v1.0 |
| **Ngày tạo** | [YYYY-MM-DD] |
| **Ngày cập nhật** | [YYYY-MM-DD] |
| **Designer phụ trách** | [Tên] |
| **Trạng thái** | Draft / Approved |

---

## 🎨 1. Color Palette

> Lấy từ Figma: Inspect panel → Fill/Stroke color, hoặc Figma Variables

### 1.1. Brand Colors (Màu thương hiệu)

| Token Name | Hex | RGB | Mô tả / Sử dụng |
|------------|-----|-----|-------------------|
| `--color-primary` | #[HEX] | rgb(R,G,B) | CTA buttons, links, active states |
| `--color-primary-hover` | #[HEX] | rgb(R,G,B) | Hover state của primary |
| `--color-primary-light` | #[HEX] | rgb(R,G,B) | Background nhẹ, highlight |
| `--color-secondary` | #[HEX] | rgb(R,G,B) | Secondary actions |
| `--color-secondary-hover` | #[HEX] | rgb(R,G,B) | Hover state của secondary |
| `--color-accent` | #[HEX] | rgb(R,G,B) | Điểm nhấn, badge, tag |

### 1.2. Neutral Colors (Màu trung tính)

| Token Name | Hex | Sử dụng |
|------------|-----|---------|
| `--color-neutral-900` | #[HEX] | Heading text, strongest emphasis |
| `--color-neutral-700` | #[HEX] | Body text |
| `--color-neutral-500` | #[HEX] | Secondary text, icon muted |
| `--color-neutral-300` | #[HEX] | Placeholder, disabled text |
| `--color-neutral-200` | #[HEX] | Borders, dividers |
| `--color-neutral-100` | #[HEX] | Subtle background |
| `--color-neutral-50` | #[HEX] | Page background alt |
| `--color-neutral-0` | #[HEX] | White / Main background |

### 1.3. Semantic Colors (Màu ngữ nghĩa)

| Token Name | Hex | Sử dụng |
|------------|-----|---------|
| `--color-success` | #[HEX] | Thành công, xác nhận |
| `--color-success-light` | #[HEX] | Background thành công |
| `--color-warning` | #[HEX] | Cảnh báo |
| `--color-warning-light` | #[HEX] | Background cảnh báo |
| `--color-error` | #[HEX] | Lỗi, validation fail |
| `--color-error-light` | #[HEX] | Background lỗi |
| `--color-info` | #[HEX] | Thông tin, gợi ý |
| `--color-info-light` | #[HEX] | Background thông tin |

### 1.4. Gradient (nếu có)

| Tên | Giá trị CSS | Sử dụng |
|-----|-------------|---------|
| `--gradient-primary` | `linear-gradient(...)` | [Mô tả] |

---

## 🔤 2. Typography

> Lấy từ Figma: Text Styles panel, hoặc Inspect → Typography section

### 2.1. Font Family

| Loại | Font Name | Fallback | Google Fonts Link |
|------|-----------|----------|-------------------|
| **Heading** | [Font name] | sans-serif | [URL hoặc N/A] |
| **Body** | [Font name] | sans-serif | [URL hoặc N/A] |
| **Mono** | [Font name] | monospace | [URL hoặc N/A] |

### 2.2. Type Scale

| Token / Style Name | Font | Size | Weight | Line Height | Letter Spacing | Sử dụng |
|--------------------|------|------|--------|-------------|----------------|---------|
| `--text-display` | [Font] | [px] | [wt] | [value] | [value] | Hero section, landing |
| `--text-h1` | [Font] | [px] | [wt] | [value] | [value] | Tiêu đề trang |
| `--text-h2` | [Font] | [px] | [wt] | [value] | [value] | Tiêu đề section |
| `--text-h3` | [Font] | [px] | [wt] | [value] | [value] | Tiêu đề sub-section |
| `--text-h4` | [Font] | [px] | [wt] | [value] | [value] | Tiêu đề nhỏ |
| `--text-body-lg` | [Font] | [px] | [wt] | [value] | [value] | Body text lớn |
| `--text-body` | [Font] | [px] | [wt] | [value] | [value] | Body text mặc định |
| `--text-body-sm` | [Font] | [px] | [wt] | [value] | [value] | Small text |
| `--text-caption` | [Font] | [px] | [wt] | [value] | [value] | Captions, labels |
| `--text-overline` | [Font] | [px] | [wt] | [value] | [value] | Overline/Eyebrow text |

---

## 📐 3. Spacing & Layout

> Lấy từ Figma: Auto Layout → Padding, Gap values

### 3.1. Spacing Scale

| Token | Value | Sử dụng |
|-------|-------|---------|
| `--space-0` | 0px | Reset |
| `--space-1` | [val]px | Micro gap (icon-text) |
| `--space-2` | [val]px | Tight spacing |
| `--space-3` | [val]px | Default inner padding |
| `--space-4` | [val]px | Standard gap |
| `--space-5` | [val]px | Section inner padding |
| `--space-6` | [val]px | Section gap |
| `--space-8` | [val]px | Large section gap |
| `--space-10` | [val]px | Page-level spacing |

> **Ghi chú hệ thống**: Ghi rõ nếu dùng 4px grid, 8px grid, hoặc custom: `_________________`

### 3.2. Grid System

| Property | Desktop (≥1024) | Tablet (768-1023) | Mobile (<768) |
|----------|-----------------|-------------------|---------------|
| Columns | [số] | [số] | [số] |
| Gutter | [val]px | [val]px | [val]px |
| Margin | [val]px | [val]px | [val]px |
| Max Width | [val]px | 100% | 100% |

### 3.3. Breakpoints

| Tên | Min Width | Ghi chú |
|-----|-----------|---------|
| `mobile` | 0px | Default mobile-first |
| `tablet` | [val]px | |
| `desktop` | [val]px | |
| `wide` | [val]px | Optional |

---

## 🔲 4. Border & Shape

> Lấy từ Figma: Inspect → Border Radius, Stroke

### 4.1. Border Radius

| Token | Value | Sử dụng |
|-------|-------|---------|
| `--radius-none` | 0px | Sharp corners |
| `--radius-sm` | [val]px | Small elements (badge, tag) |
| `--radius-md` | [val]px | Buttons, inputs, cards |
| `--radius-lg` | [val]px | Modals, panels |
| `--radius-xl` | [val]px | Large containers |
| `--radius-full` | 9999px | Pills, avatars |

### 4.2. Border Width

| Token | Value | Sử dụng |
|-------|-------|---------|
| `--border-thin` | [val]px | Default border |
| `--border-medium` | [val]px | Emphasized border |
| `--border-thick` | [val]px | Active/Focus state |

---

## 🌑 5. Shadows & Elevation

> Lấy từ Figma: Inspect → Drop Shadow, Inner Shadow

| Token | Value (CSS) | Sử dụng |
|-------|-------------|---------|
| `--shadow-xs` | `[box-shadow value]` | Subtle elevation |
| `--shadow-sm` | `[box-shadow value]` | Cards ở rest |
| `--shadow-md` | `[box-shadow value]` | Cards hover, dropdown |
| `--shadow-lg` | `[box-shadow value]` | Modals, overlays |
| `--shadow-xl` | `[box-shadow value]` | Sticky elements |

---

## 🧩 6. Component Library (Thư Viện Component)

> Liệt kê các component có sẵn trong Figma. AI phải dùng đúng tên và variant.

### 6.1. Danh Sách Component

| Component Name (Figma) | Variants | Sizes | States | Ghi chú |
|-------------------------|----------|-------|--------|---------|
| `Button` | Primary, Secondary, Ghost, Danger | sm, md, lg | default, hover, active, focus, disabled | [Ghi chú] |
| `Input` | Text, Password, Search, Textarea | sm, md | default, focus, error, disabled | [Ghi chú] |
| `Select` | Single, Multi | sm, md | default, open, error, disabled | |
| `Checkbox` | Default | md | unchecked, checked, indeterminate, disabled | |
| `Radio` | Default | md | unselected, selected, disabled | |
| `Toggle` | Default | sm, md | off, on, disabled | |
| `Card` | [Variants] | [Sizes] | [States] | |
| `Modal / Dialog` | [Variants] | [Sizes] | [States] | |
| `Toast / Notification` | Success, Error, Warning, Info | md | visible, dismissing | |
| `Badge` | [Variants] | sm, md | [States] | |
| `Avatar` | Image, Initial, Icon | sm, md, lg, xl | [States] | |
| `Table` | [Variants] | [Sizes] | [States] | |
| `Tab` | [Variants] | [Sizes] | default, active, disabled | |
| `Navigation` | [Variants] | [Sizes] | [States] | |
| `Pagination` | [Variants] | [Sizes] | [States] | |
| `Tooltip` | [Variants] | [Sizes] | [States] | |
| `Breadcrumb` | [Variants] | [Sizes] | [States] | |
| `Sidebar` | [Variants] | [Sizes] | expanded, collapsed | |

> **Thêm component khác**: Nếu Figma library có component không có trong list trên, thêm row mới.

### 6.2. Component Chi Tiết (Tùy Chọn)

> Nếu một component có quy tắc phức tạp, mô tả chi tiết tại đây.

#### Button
```
Padding:    [horizontal]px [vertical]px
Min Width:  [val]px
Icon Size:  [val]px (khi có icon)
Gap:        [val]px (giữa icon và text)
Font:       [style name từ Type Scale]
```

#### Input
```
Height:     [val]px (md), [val]px (sm)
Padding:    [horizontal]px [vertical]px
Border:     [val]px solid [color token]
Label:      [font style], [spacing từ input]
Helper:     [font style], [spacing từ input]
```

---

## 🎭 7. Iconography

| Property | Giá trị |
|----------|---------|
| **Icon Library** | [Tên: Phosphor, Lucide, Material, Heroicons, Custom...] |
| **Style** | [Outline / Filled / Duotone / Mixed] |
| **Sizes** | [val]px (sm), [val]px (md), [val]px (lg) |
| **Stroke Width** | [val]px |
| **Color** | [Token name: --color-neutral-700] |
| **Naming Convention** | [VD: `ic-[name]` hoặc `[name]-icon`] |

---

## 🎬 8. Motion & Animation

| Property | Giá trị |
|----------|---------|
| **Easing** | [VD: ease-in-out, cubic-bezier(0.4, 0, 0.2, 1)] |
| **Duration - Micro** | [val]ms (hover, toggle) |
| **Duration - Standard** | [val]ms (expand, slide) |
| **Duration - Complex** | [val]ms (page transition, modal) |

---

## 🚫 9. Do's & Don'ts

> Quy tắc thiết kế quan trọng mà Designer muốn enforce. AI **PHẢI** tuân thủ.

### ✅ Do's (NÊN làm)
- [VD: Luôn dùng Primary button cho CTA chính duy nhất trên mỗi màn hình]
- [VD: Icon phải luôn đi kèm text label trên mobile]
- [VD: Form phải có inline validation]
- [...]

### ❌ Don'ts (KHÔNG ĐƯỢC làm)
- [VD: Không dùng quá 3 màu brand trên cùng 1 màn hình]
- [VD: Không dùng placeholder thay label cho input]
- [VD: Không sử dụng shadow-lg cho card trong list view]
- [...]

---

## 📝 10. Ghi Chú Bổ Sung

> Bất kỳ quy tắc hoặc thông tin nào không nằm trong các section trên.

- [Ghi chú 1]
- [Ghi chú 2]

---

> **⚠️ FILE NÀY LÀ NGUỒN CHÂN LÝ (SINGLE SOURCE OF TRUTH)**
> AI agent PHẢI đọc file `artifacts/technical/design/design-system-spec.md` (bản đã điền) trước khi thiết kế.
> Mọi đề xuất UI PHẢI tuân thủ giá trị trong file này.
> Nếu cần thay đổi Design System → liên hệ Designer → cập nhật file → chạy `/change-request`.
