---
name: Vietlott SMS Design System
version: "1.0"
platform: mobile-first
framework: flutter-clone
colors:
  # === Brand Primary ===
  primary: "#ED1C24"
  primary-dark: "#EB0D1E"
  primary-alt: "#EC1D25"

  # === Product Theme Colors (mỗi sản phẩm 1 màu riêng) ===
  power-655: "#ED1C24"
  mega-645: "#036AFF"
  max-3d: "#F57B21"
  max-3d-pro: "#7B2D8E"
  bingo-18: "#F57B21"
  lotto-535: "#067A3E"

  # === Semantic ===
  success: "#30B852"
  success-dark: "#129C49"
  success-darker: "#0A4429"
  warning: "#FF9500"
  warning-alt: "#FFB13B"
  error: "#FF3B30"
  error-alt: "#F23D3D"
  info: "#007AFF"
  info-alt: "#036AFF"

  # === Neutral ===
  neutral-900: "#212121"
  neutral-700: "#757575"
  neutral-600: "#7E7E7E"
  neutral-500: "#8E8E93"
  neutral-400: "#AEAEB2"
  neutral-300: "#C7C7CC"
  neutral-200: "#D6D9DB"
  neutral-100: "#E5E5EA"
  neutral-50: "#EFEFF1"
  neutral-25: "#FAFAFC"
  neutral-0: "#FDFEFF"
  black: "#000000"

  # === Accent / Special ===
  orange: "#DB5B00"
  orange-light: "#F57B21"
  gold: "#DBB25B"
  gold-light: "#FFB13B"
  green-highlight: "#CDE98C"
  blue-bg: "#F7FBFF"

typography:
  heading:
    fontFamily: "UTM Alberta"
    fallback: "sans-serif"
    source: "Custom (bundled in APK)"
  body:
    fontFamily: "Roboto"
    fallback: "sans-serif"
    source: "Google Fonts"
  countdown:
    fontFamily: "Cursed Timer ULiL"
    fallback: "monospace"
    source: "Custom (bundled in APK)"
  icon:
    fontFamily: "MaterialIcons"
    source: "Flutter built-in"

  scale:
    display:
      font: "UTM Alberta"
      weight: 800
      use: "Jackpot amount, hero numbers"
    h1:
      font: "Roboto"
      size: "24px"
      weight: 700
      use: "Page titles"
    h2:
      font: "Roboto"
      size: "20px"
      weight: 700
      use: "Section titles"
    h3:
      font: "Roboto"
      size: "16px"
      weight: 600
      use: "Sub-section titles, card headers"
    body-lg:
      font: "Roboto"
      size: "16px"
      weight: 400
      use: "Main content text"
    body:
      font: "Roboto"
      size: "14px"
      weight: 400
      use: "Default body text"
    body-sm:
      font: "Roboto"
      size: "12px"
      weight: 400
      use: "Small text, descriptions"
    caption:
      font: "Roboto"
      size: "10px"
      weight: 400
      use: "Captions, timestamps"
    timer:
      font: "Cursed Timer ULiL"
      size: "32px-48px"
      weight: 400
      use: "Countdown timer display (Bingo18, quay thưởng)"

spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "24px"
  xxl: "32px"
  section: "48px"
  grid: "8px base"

rounded:
  sm: "4px"
  md: "8px"
  lg: "12px"
  xl: "16px"
  xxl: "24px"
  full: "9999px"
---

# Vietlott SMS — Design System for Stitch

> **Mục đích:** File này dùng làm input cho Google Stitch để clone 1:1 giao diện app Vietlott-SMS (Flutter → Stitch prototype).
> **Nguồn dữ liệu:** Trích xuất trực tiếp từ APK v4.4.18.276 (DEV environment).

## Overview — Triết Lý Thiết Kế

Vietlott SMS là ứng dụng mua xổ số trực tuyến qua SMS/ví điện tử. Giao diện tuân theo phong cách:

- **Vibrant & Energetic**: Mỗi sản phẩm xổ số có màu theme riêng biệt, tạo cảm giác đa dạng và sôi động
- **Trust & Official**: Tông đỏ chủ đạo (brand Vietlott #ED1C24) truyền tải sự chính thức, uy tín
- **Gamification**: Heavy sử dụng animation (Lottie), mascot "Thần Tài", hiệu ứng pháo hoa/confetti
- **Mobile-First**: Toàn bộ thiết kế tối ưu cho mobile (Flutter framework)

## Colors — Cách Sử Dụng

### Brand Primary (#ED1C24 — Đỏ Vietlott)
- **BẮT BUỘC** dùng cho: Logo, CTA button chính (Mua vé), Tab bar active state, Header chính
- Variant `#EB0D1E` dùng cho pressed/active state
- **KHÔNG** dùng đỏ brand cho text body hoặc background lớn

### Product Theme Colors — MỖI SẢN PHẨM 1 MÀU
Đây là điểm thiết kế đặc trưng nhất của app. Mỗi sản phẩm xổ số có màu riêng, apply cho:
- Navigation background (`nav_bg_*.png`)
- Product card gradient
- Ball/number highlight
- Section header

| Sản phẩm | Màu | Navigation BG file |
|-----------|-----|--------------------|
| **Power 6/55** | 🔴 `#ED1C24` (Red) | `home/nav_bg_red.png` |
| **Mega 6/45** | 🔵 `#036AFF` (Blue) | `home/nav_bg_blue.png` |
| **Max 3D** | 🟠 `#F57B21` (Orange) | `home/nav_bg_orange.png` |
| **Max 3D Pro** | 🟣 `#7B2D8E` (Purple) | `home/nav_bg_purple_max3d_pro.png` |
| **Bingo18** | 🟡 `#FFB13B` (Yellow/Gold) | `home/nav_bg_yellow.png` |
| **Lotto 5/35** | 🟢 `#067A3E` (Green) | `home/nav_bg_green.png` |

### Neutral Colors
- Body text: `#212121` (gần đen, dễ đọc)
- Secondary text: `#757575`
- Disabled/muted: `#8E8E93`
- Borders/dividers: `#C7C7CC` hoặc `#D6D9DB`
- Background cards: `#FDFEFF` (gần trắng)
- Page background: `#EFEFF1` hoặc `#FAFAFC`

## Typography — Quy Tắc

### Font "UTM Alberta Heavy" — CHỈ dùng cho:
- Số tiền Jackpot (display size)
- Tiêu đề sản phẩm nổi bật
- **KHÔNG** dùng cho body text

### Font "Roboto" — Font mặc định toàn app:
- Đầy đủ 12 weights (Thin → Black, kèm Italic)
- Heading: Bold (700) hoặc Medium (500)
- Body: Regular (400)
- Caption: Light (300) hoặc Regular (400)

### Font "Cursed Timer ULiL" — CHỈ dùng cho:
- Đồng hồ đếm ngược quay thưởng
- Countdown Bingo18 (6 phút/kỳ)
- **KHÔNG** dùng cho bất kỳ nội dung nào khác

## Components — Danh Sách Từ APK

### Bottom Tab Bar (5 tabs)
| Tab | Icon (SVG) | Label |
|-----|-----------|-------|
| Trang chủ | `tabbar_home.svg` | Trang chủ |
| Kết quả | `tabbar_result.svg` | Kết quả |
| Lịch sử | `tabbar_history.svg` | Lịch sử |
| Tiện ích | `tabbar_utility.svg` | Tiện ích |
| Cá nhân | `tabbar_personal.svg` | Cá nhân |

- Active state: fill `#ED1C24` (đỏ brand)
- Inactive state: fill `#8E8E93` (neutral-500)

### Buttons
- **Primary CTA (Mua vé)**: Background `#ED1C24`, text white, border-radius `8px`
- **Secondary**: Border `#ED1C24`, text `#ED1C24`, background transparent
- **Ghost**: Text-only, no border

### Number Ball (Quả bóng số)
- SVG base: `ball_flat.svg`
- Color variants theo sản phẩm (Power = đỏ, Mega = xanh dương...)
- Active/selected state: fill đậm + shadow
- Inactive: fill nhạt hoặc outlined

### Product Cards (Home)
- Mỗi card có gradient background theo product color
- Logo sản phẩm nằm bên trái
- Jackpot amount (UTM Alberta font) nằm bên phải
- Chevron arrow (`power_chevron.png`, `mega_chevron.png`) để navigate

### Wallet Logos (Thanh toán)
| Ví | File |
|----|------|
| Momo | `wallet/Momo.png` |
| ZaloPay | `wallet/ZaloPay.png` |
| VNPay | `wallet/VNPay.png` |
| ViettelMoney | `wallet/ViettelMoney.png` |
| VNPTPay | `wallet/VNPTPay.png` |
| VNPTMoney | `wallet/VNPTMoney1.png` |
| Moca | `wallet/Moca.png` |

### Bingo18 Special Components
- **Dice (xúc xắc)**: `bingo18/dice0-5.png` (6 mặt, numbered 0-5)
- **Chip betting**: `bingo18/bingo_chip1-4.png` (4 mức cược)
- **God of Wealth (Thần Tài)**: 5 color variants
- **Aura effects**: 6 color variants (blue, green, purple, red, white, yellow)
- **Countdown timer**: Font Cursed Timer + background animation

### Lottie Animations (Interactive)
| Animation | File | Trigger |
|-----------|------|---------|
| Thần Tài login | `lottie/than_tai_login.json` | Màn hình login |
| Thần Tài mascot | `lottie/ic_than_tai.json` | Trang sản phẩm |
| Xúc xắc quay | `lottie/dice1-3.json` | Bingo18 kết quả |
| Confetti trúng | `lottie/confetti.json` | Popup trúng thưởng |
| Pháo hoa | `lottie/firework_*.json` | Celebration |
| Loading spinner | `lottie/loading.json` | Loading state |
| Red dot live | `lottie/ic_red_dot_live.json` | Indicator quay live |

## Do's and Don'ts

### ✅ DO
- Luôn dùng đúng product theme color cho mỗi sản phẩm xổ số
- Dùng Roboto làm font chính, UTM Alberta CHỈ cho display numbers
- Giữ bottom tab bar cố định 5 tabs
- Dùng mascot "Thần Tài" ở các điểm engagement (login, trúng thưởng)
- Hiển thị giá trị Jackpot bằng UTM Alberta + product color
- Dùng rounded corners 8-12px cho cards và buttons

### ❌ DON'T
- KHÔNG trộn product colors (ví dụ: dùng màu Power trên trang Mega)
- KHÔNG dùng Cursed Timer font ngoài countdown
- KHÔNG bỏ Lottie animations — chúng là phần core UX
- KHÔNG thay đổi thứ tự tab bar
- KHÔNG dùng flat white background cho product pages — luôn có gradient theo theme
- KHÔNG hiển thị full-uppercase cho body text tiếng Việt

## Asset Paths Reference

Tất cả assets đã được extract tại:
```
f:\VIETLOTT-SMS\scripts\apk-extracted\contents\assets\flutter_assets\
├── assets/
│   ├── png/          # 567 PNG files (logos, backgrounds, icons, game assets)
│   ├── svg/          # 331 SVG files (icons, illustrations, UI elements)
│   ├── lottie/       # 24 Lottie JSON animations
│   ├── gif/          # 3 GIF animations
│   ├── sound/        # Sound effects (bingo18, lotto535)
│   └── vid/          # Video files
├── fonts/            # 15 font files (Roboto, UTM Alberta, Cursed Timer, MaterialIcons)
└── packages/         # Flutter packages (toast, webview, youtube player)
```
