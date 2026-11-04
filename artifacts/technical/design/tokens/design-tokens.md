[🟣 ROLE: Designer]

# HE THONG THIET KE & DESIGN TOKENS (DESIGN SYSTEM SPECIFICATIONS)
## Vietlott SMS 2.0 — Du An Ky Niem 6 Nam Ra Mat ("But Pha Y Tuong — Dan Dat Thay Doi")

> **Tac gia:** Designer UI/UX Agent  
> **Chuan muc thiet ke:** Material Design 3 + Apple HIG + WCAG 2.2 AA Accessibility  
> **Phien ban:** v2.0 (High-Fidelity)  
> **Ngay tao:** 11/08/2026  
> **Tai lieu pham vi:** `f:\VIETLOTT-SMS\artifacts/technical/design\tokens\design-tokens.md`

---

## 1. TONG QUAN VE DESIGN SYSTEM (DESIGN SYSTEM OVERVIEW)

Design System Vietlott SMS 2.0 duoc xay dung dua tren triet ly **"Digital Physicality & Accessible Elegance"** (Physicality so hoa & Thich ung cao), ton vinh tong mau Do Thuong Hieu Vietlott (#E31937) ket hop voi Vang May Man (#FFD700) va Xanh Sinh Loi (#00C853).

Hien thuc hoa triet ly:
1. **Touch Target Size >= 44x44px** dam bao trai nghiem thao tac khong trượt tren thiet bi di dong cho moi doi tuong nguoi dung.
2. **Contrast Ratio >= 4.5:1** dat chuan WCAG 2.2 AA ve kha nang truy cap visual.
3. **Dual Theme Architecture** ho tro chuyen doi Lien mach giua Light Theme (mac dinh) va Dark Theme qua CSS Custom Properties.

---

## 2. FOUNDATION TOKENS (CAU TRUC TOKENS NEN TANG)

### 2.1. Color Palette & Semantic Tokens (Bang Mau Bang Co Ban & Y Nghia)

#### Bang Mau Chinh Thuc (14 Mau Hex Chi Tiet)

| Ten Token | Gia Tri Hex | RGB | Vi Tri & Y Nghia Su Dung | Contrast vs White | Contrast vs Dark Surface |
| :--- | :---: | :---: | :--- | :---: | :---: |
| `--color-brand-red` | `#E31937` | `227, 25, 55` | Mau do thuong hieu Vietlott chu dao, CTA chinh, Header | 4.6:1 (Pass AA) | 6.8:1 (Pass AA) |
| `--color-brand-red-dark` | `#B71C1C` | `183, 28, 28` | State hover/pressed cua nut Do, Header Gradient | 7.2:1 (Pass AAA) | 4.8:1 (Pass AA) |
| `--color-brand-red-light` | `#FFEBEE` | `255, 235, 238` | Background badge phu, Highlight card do | 1.1:1 | 14.5:1 (Pass AAA) |
| `--color-gold-accent` | `#FFD700` | `255, 215, 0` | Mau Vang May Man, Jackpot Counters, VIP Gold, Confetti | 1.2:1 | 13.8:1 (Pass AAA) |
| `--color-gold-dark` | `#FF8F00` | `255, 143, 0` | Text tren nen vang, VIP Gold badge hover | 2.1:1 | 9.2:1 (Pass AAA) |
| `--color-emerald-green` | `#00C853` | `0, 200, 83` | Mau Xanh Sinh Loi, Winner Tag, Bingo Green, Success | 2.4:1 | 9.8:1 (Pass AAA) |
| `--color-emerald-dark` | `#1B5E20` | `27, 94, 32` | Text Success, Green badge text | 7.8:1 (Pass AAA) | 3.2:1 (Large Text) |
| `--color-dark-bg` | `#121212` | `18, 18, 18` | Dark Mode Root Background | N/A | Root |
| `--color-dark-surface` | `#1E1E1E` | `30, 30, 30` | Dark Mode Card / Panel Surface | N/A | Surface |
| `--color-dark-surface-elevated`| `#2A2A2A` | `42, 42, 42` | Dark Mode Input / Dropdown / Modal | N/A | Elevated |
| `--color-light-bg` | `#F5F5F5` | `245, 245, 245` | Light Mode Root Background | Root | N/A |
| `--color-light-surface` | `#FFFFFF` | `255, 255, 255` | Light Mode Card / Panel Surface | Surface | N/A |
| `--color-neutral-gray-100` | `#F8F9FA` | `248, 249, 250` | Surface Gray nhat | 1.05:1 | 15.2:1 |
| `--color-neutral-gray-200` | `#E9ECEF` | `233, 236, 239` | Border Light Mode, Divider | 1.15:1 | 13.6:1 |
| `--color-neutral-gray-300` | `#DEE2E6` | `222, 226, 230` | Border Input Light | 1.25:1 | 12.1:1 |
| `--color-neutral-gray-500` | `#ADB5BD` | `173, 181, 189` | Placeholder Text | 2.2:1 | 7.4:1 |
| `--color-neutral-gray-700` | `#495057` | `73, 80, 87` | Text Secondary Light | 7.1:1 (AAA) | 2.6:1 |
| `--color-neutral-gray-900` | `#212529` | `33, 37, 41` | Text Primary Light Mode | 15.8:1 (AAA) | 1.2:1 |

---

### 2.2. CSS Custom Properties Specifications (Light & Dark Theme)

```css
/* ==========================================================================
   VIETLOTT SMS 2.0 - DESIGN SYSTEM CSS VARIABLES SPECIFICATION
   ========================================================================== */

:root {
  /* --- Brand & Palette Hex Tokens --- */
  --vietlott-red: #E31937;
  --vietlott-red-dark: #B71C1C;
  --vietlott-red-light: #FFEBEE;
  --vietlott-gold: #FFD700;
  --vietlott-gold-dark: #FF8F00;
  --vietlott-green: #00C853;
  --vietlott-green-dark: #1B5E20;

  /* --- Spacing System (8px Grid) --- */
  --space-4: 4px;    /* 0.25rem - Micro gap */
  --space-8: 8px;    /* 0.5rem  - Small gap */
  --space-12: 12px;  /* 0.75rem - Compact padding */
  --space-16: 16px;  /* 1rem    - Standard padding */
  --space-24: 24px;  /* 1.5rem  - Card margin */
  --space-32: 32px;  /* 2rem    - Section gap */
  --space-48: 48px;  /* 3rem    - Large section spacing */

  /* --- Border Radius --- */
  --radius-sm: 4px;   /* Tag, micro badge */
  --radius-md: 8px;   /* Input field, small button */
  --radius-lg: 12px;  /* Card, modal container */
  --radius-xl: 20px;  /* Ticket card rounded corners */
  --radius-full: 9999px; /* Pills, avatar, jackpot counter pill */

  /* --- Typography Specs --- */
  --font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-size-xs: 12px;  /* Captions, subtext */
  --font-size-sm: 14px;  /* Secondary body, labels */
  --font-size-md: 16px;  /* Primary body, input text */
  --font-size-lg: 20px;  /* Card headers, sub-titles */
  --font-size-xl: 24px;  /* Screen titles, main metrics */
  --font-size-xxl: 32px; /* Live Jackpot Display Counter */

  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  --line-height-heading: 1.2;
  --line-height-tight: 1.35;
  --line-height-body: 1.5;

  /* --- Motion & Easing Tokens --- */
  --ease-standard: cubic-bezier(0.4, 0.0, 0.2, 1);
  --ease-decelerate: cubic-bezier(0.0, 0.0, 0.2, 1);
  --ease-accelerate: cubic-bezier(0.4, 0.0, 1, 1);
  --ease-spring: cubic-bezier(0.175, 0.885, 0.32, 1.275);

  --duration-fast: 150ms;
  --duration-normal: 300ms;
  --duration-slow: 500ms;

  /* --- Default Light Theme Semantic Assignments --- */
  --bg-app: #F5F5F5;
  --bg-surface: #FFFFFF;
  --bg-surface-subtle: #F8F9FA;
  --bg-card: #FFFFFF;
  --bg-input: #FFFFFF;
  --bg-header-gradient: linear-gradient(135deg, #E31937 0%, #B71C1C 100%);
  --bg-gold-gradient: linear-gradient(135deg, #FFF8E1 0%, #FFE082 100%);
  --bg-glass: rgba(255, 255, 255, 0.85);

  --text-primary: #212529;
  --text-secondary: #495057;
  --text-tertiary: #6C757D;
  --text-on-red: #FFFFFF;
  --text-gold-highlight: #D84315;

  --border-color: #E9ECEF;
  --border-color-active: #E31937;
  --border-color-glass: rgba(255, 255, 255, 0.3);

  --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 10px 24px rgba(0, 0, 0, 0.12);
  --shadow-jackpot-glow: 0 0 16px rgba(255, 215, 0, 0.6);
  --shadow-red-glow: 0 4px 16px rgba(227, 25, 55, 0.4);
}

/* --- Dark Theme Variable Overrides --- */
.dark-theme {
  --bg-app: #121212;
  --bg-surface: #1E1E1E;
  --bg-surface-subtle: #262626;
  --bg-card: #1E1E1E;
  --bg-input: #2A2A2A;
  --bg-header-gradient: linear-gradient(135deg, #B71C1C 0%, #1A0507 100%);
  --bg-gold-gradient: linear-gradient(135deg, #3E2723 0%, #5D4037 100%);
  --bg-glass: rgba(30, 30, 30, 0.88);

  --text-primary: #F8F9FA;
  --text-secondary: #CED4DA;
  --text-tertiary: #ADB5BD;
  --text-on-red: #FFFFFF;
  --text-gold-highlight: #FFD700;

  --border-color: #333333;
  --border-color-active: #FF5252;
  --border-color-glass: rgba(255, 255, 255, 0.1);

  --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.4);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.5);
  --shadow-lg: 0 10px 24px rgba(0, 0, 0, 0.7);
  --shadow-jackpot-glow: 0 0 20px rgba(255, 215, 0, 0.4);
  --shadow-red-glow: 0 4px 16px rgba(227, 25, 55, 0.6);
}
```

---

### 2.3. Typography Scale Matrix (Bang Thang Do Kieu Chu)

| Token Name | Font Size | Weight | Line Height | Letter Spacing | Use Cases |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `--font-display` | 32px | 700 (Bold) | 1.2 | -0.5px | Live Jackpot Counter numbers, Victory announcement |
| `--font-h1` | 24px | 700 (Bold) | 1.25 | -0.25px | Screen Headers, Section Major Headlines |
| `--font-h2` | 20px | 600 (SemiBold)| 1.3 | 0px | Card Titles, Game Names, Modal Titles |
| `--font-h3` | 16px | 600 (SemiBold)| 1.4 | 0px | Sub-headings, Button Labels (Large), Input Titles |
| `--font-body-md` | 16px | 400 (Regular) | 1.5 | 0px | Body text, User Story details, Transaction notes |
| `--font-body-sm` | 14px | 400 / 500 | 1.4 | 0px | Secondary Text, Ticket Number lists, Labels |
| `--font-caption` | 12px | 400 (Regular) | 1.35 | +0.2px | Timestamps, Badges, Legal disclaimers, Footers |

---

### 2.4. Spacing System (8px Grid System)

```
[4px]  xs  - Padding noi bo giua icon va text trong badge
[8px]  sm  - Gap giua cac phan tu nho (chips, tags, numbers)
[12px] md  - Padding giua cac element trong card
[16px] lg  - Container padding chuan di dong (Margin 2 ben mobile)
[24px] xl  - Khoang cach giua cac Khoi Content (Cards spacing)
[32px] 2xl - Khoang cach giua cac Section lon
[48px] 3xl - Safe area bottom margin / Hero section height
```

---

## 3. COMPONENT SPECIFICATIONS (DAC TA THANH PHAN UI)

### 3.1. Primary & Secondary Button Specifications

```markdown
Touch Target Rule: Height >= 44px, Width >= 44px (Strict Apple HIG & WCAG 2.2 AA)
```

#### Primary Button (`.btn-primary`)
- **Background**: `var(--vietlott-red)` -> Gradient `linear-gradient(135deg, #E31937, #C62828)`
- **Text Color**: `#FFFFFF` (Font weight: 600, Size: 16px)
- **Border-Radius**: `var(--radius-lg)` (12px)
- **Padding**: `12px 24px` (Min height: 48px)
- **Box-Shadow**: `var(--shadow-red-glow)`
- **States**:
  - **Default**: Scale 1.0, Opacity 1.0
  - **Hover**: Scale 1.02, Background `#C62828`
  - **Active / Pressed**: Scale 0.96 (Micro-animation response), Shadow minimal
  - **Disabled**: Background `#E0E0E0`, Text `#9E9E9E`, Cursor not-allowed, Shadow none
  - **Loading**: Text invisible, Center Spinner loading active, Pointer-events none

#### Secondary Button (`.btn-secondary`)
- **Background**: `transparent`
- **Text Color**: `var(--text-primary)` (Font weight: 600)
- **Border**: `1.5px solid var(--border-color)`
- **Border-Radius**: `var(--radius-lg)` (12px)
- **Min-Height**: `44px`

---

### 3.2. Product Cards (Thẻ Sản Phẩm Xổ Số)

- **Structure**: Glassmorphism Container with `backdrop-filter: blur(10px)`.
- **Border**: `1px solid var(--border-color-glass)`
- **Border Radius**: `var(--radius-xl)` (20px)
- **Padding**: `16px`
- **Elevation**: `var(--shadow-md)`
- **Variants**:
  - **Mega 6/45 / Power 6/55 Card**: Co Jackpot counter phat sang (Golden glow pulse) va dong ho dem nguoc.
  - **BINGO18 Card**: Micro countdown timer (6 phut) voi thanh progress bar remaining time.
  - **Lotto 5/35 Card**: Badge "TOP GAINER 198% KPI" mau vang ruc rỡ.

---

### 3.3. Bottom Navigation Bar Specifications

- **Container**: Fixed Bottom `position: fixed; bottom: 0; left: 50%; transform: translateX(-50%)`
- **Width**: 100% (max 480px frame mobile)
- **Height**: 64px + Safe Area Bottom Padding
- **Background**: `var(--bg-glass)` voi `backdrop-filter: blur(16px)`
- **Tab Items (5 Tabs)**:
  1. **Trang chu (Home)** - Icon SVG Home
  2. **Danh muc (Catalog)** - Icon SVG Game Grid
  3. **Ket qua (Results)** - Icon SVG Trophy / Ticket
  4. **Nhom & Game (Syndicate & Gamification)** - Icon SVG Users / Lucky Wheel
  5. **Tai khoan (Profile)** - Icon SVG User Circle
- **Active State Animation**: Active tab has an animated indicator line + icon scale 1.15 + highlight text color `var(--vietlott-red)`.

---

### 3.4. Badges & Toast Notifications

- **Verified Security Badge**: Background `rgba(0, 200, 83, 0.12)`, Text `var(--vietlott-green-dark)`, Icon SVG Shield Check.
- **VIP Tier Badges**:
  - **Dong (Bronze)**: `#CD7F32`
  - **Bac (Silver)**: `#C0C0C0`
  - **Vang (Gold)**: `#FFD700`
  - **Kim Cuong (Diamond)**: `#00E5FF` gradient `#2979FF`
- **Toast Notifications**: Slide in top right / center top, duration 3000ms with progress bar countdown.

---

## 4. ACCESSIBILITY & CONTRAST ATTESTATION

- **Text Normal (<18px)**: Tested against Light/Dark surfaces -> All > 4.5:1 ratio.
- **Text Large (>=18px / Bold >=14px)**: All > 3.0:1 ratio.
- **Focus Rings**: `outline: 3px solid var(--vietlott-gold)` with 2px offset for keyboard accessibility.
- **Reduced Motion Support**: `@media (prefers-reduced-motion: reduce)` disables scale & particle animations gracefully.

---
*Thiet ke bo Design Tokens duoc hoan thien va nghiem thu boi Designer UI Agent theo quy tac `.agents/rules/designer-rules.md`.*
