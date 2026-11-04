# -*- coding: utf-8 -*-
"""
Warm Cream Storybook / Chibi Illustration Primitives matching Mr. Phú's signature aesthetic:
- Espresso-brown hand-drawn ink outlines (#3B2518)
- Soft watercolor background washes (#EFE0BC, #DCE8F2, #DFECE0, #F5DFD4)
- Expressive chibi BA characters (diverse poses, expressions, hairstyles, outfits, glasses)
- Crisp, warm gouache props (whiteboards, sticky notes, laptops, shields, scales, trees, etc.)
"""
import html

INK = "#3B2518"
BLUE_TITLE = "#054AA3"
SKIN = "#FAD9BE"
SKIN_SHADOW = "#F0C19C"
CHEEK = "#F2A294"


def esc(t: str) -> str:
    return html.escape(str(t))


def svg_defs() -> str:
    return """
  <defs>
    <filter id="softShadow" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#8C6D46" flood-opacity="0.16"/>
    </filter>
    <linearGradient id="skyWash" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#DCE8F4" stop-opacity="0.78"/>
      <stop offset="100%" stop-color="#EBF1E6" stop-opacity="0.55"/>
    </linearGradient>
    <linearGradient id="sandWash" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F1DFB6" stop-opacity="0.82"/>
      <stop offset="100%" stop-color="#F6E9CB" stop-opacity="0.5"/>
    </linearGradient>
    <linearGradient id="sageWash" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#DCECE0" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#F1E6C8" stop-opacity="0.55"/>
    </linearGradient>
    <linearGradient id="peachWash" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F6DDD2" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#F3E4C2" stop-opacity="0.55"/>
    </linearGradient>
  </defs>
"""


def wash_blob(cx: float, cy: float, rx: float, ry: float, grad: str = "sandWash", seed: int = 0) -> str:
    """Organic layered watercolor wash behind the scene."""
    if seed % 3 == 0:
        p1 = f"M {cx-rx},{cy+ry*0.1} C {cx-rx*0.95},{cy-ry*0.85} {cx-rx*0.2},{cy-ry*1.05} {cx+rx*0.35},{cy-ry*0.9} C {cx+rx*0.95},{cy-ry*0.75} {cx+rx*1.08},{cy+ry*0.15} {cx+rx*0.75},{cy+ry*0.78} C {cx+rx*0.35},{cy+ry*1.08} {cx-rx*0.65},{cy+ry*1.02} {cx-rx},{cy+ry*0.1} Z"
    elif seed % 3 == 1:
        p1 = f"M {cx-rx*0.92},{cy-ry*0.15} C {cx-rx*0.75},{cy-ry*0.95} {cx+rx*0.25},{cy-ry*1.02} {cx+rx*0.85},{cy-ry*0.45} C {cx+rx*1.1},{cy+ry*0.2} {cx+rx*0.65},{cy+ry*0.95} {cx-rx*0.1},{cy+ry*0.98} C {cx-rx*0.8},{cy+ry*0.95} {cx-rx*1.05},{cy+ry*0.4} {cx-rx*0.92},{cy-ry*0.15} Z"
    else:
        p1 = f"M {cx-rx},{cy} C {cx-rx*0.88},{cy-ry*0.92} {cx+rx*0.1},{cy-ry*0.98} {cx+rx*0.78},{cy-ry*0.65} C {cx+rx*1.05},{cy-ry*0.1} {cx+rx*0.92},{cy+ry*0.82} {cx+rx*0.2},{cy+ry*0.95} C {cx-rx*0.55},{cy+ry*1.02} {cx-rx*1.04},{cy+ry*0.55} {cx-rx},{cy} Z"
    return f'<path d="{p1}" fill="url(#{grad})" />'


def draw_chibi(
    cx: float,
    cy: float,
    scale: float = 1.0,
    expr: str = "smile",
    hair: str = "male_neat",
    outfit: str = "blue_shirt",
    glasses: bool = True,
    pose: str = "normal",
    hat: str = "",
) -> str:
    """
    Draws an expressive chibi character centered at head (cx, cy).
    Head radius ~56*scale; torso extends to cy + 165*scale.
    """
    outfits = {
        "blue_shirt": ("#8AB4DF", "#FFFFFF", "#2B5B9E"),
        "brown_suit": ("#7A6352", "#F7F2E8", "#A64B38"),
        "grey_blazer": ("#6D7682", "#FFFFFF", "#3B6EA8"),
        "sage_vest": ("#7DA882", "#FBF7EE", "#4C7553"),
        "orange_cardigan": ("#D9824B", "#FFF9EE", "#8C4A27"),
        "white_tie": ("#F5EFE4", "#FFFFFF", "#1E56A0"),
        "dark_hoodie": ("#434A54", "#656D78", "#E67E22"),
        "builder_vest": ("#E6A832", "#7AB0D9", "#C95B2B"),
    }
    coat_c, shirt_c, tie_c = outfits.get(outfit, outfits["blue_shirt"])

    hair_c = "#3D281D" if hair not in ("female_bob", "senior_mentor") else ("#4E3324" if hair == "female_bob" else "#33241D")

    parts = [f'<g transform="translate({cx},{cy}) scale({scale})">']

    # Back hair for female styles
    if hair == "female_bob":
        parts.append(f'<path d="M -64,-10 C -72,45 -62,72 -44,74 L 44,74 C 62,72 72,45 64,-10 Z" fill="{hair_c}" stroke="{INK}" stroke-width="3.6" stroke-linejoin="round"/>')
    elif hair == "female_ponytail":
        parts.append(f'<path d="M 52,-18 C 84,-28 96,12 78,42 C 66,34 56,16 50,-4 Z" fill="{hair_c}" stroke="{INK}" stroke-width="3.6" stroke-linejoin="round"/>')

    # Neck & Torso
    parts.append(f'<rect x="-14" y="48" width="28" height="22" rx="8" fill="{SKIN_SHADOW}" stroke="{INK}" stroke-width="3.2"/>')
    parts.append(f'<path d="M -56,162 C -54,96 -38,66 0,66 C 38,66 54,96 56,162 Z" fill="{coat_c}" stroke="{INK}" stroke-width="3.8" stroke-linejoin="round"/>')

    if outfit == "dark_hoodie":
        parts.append(f'<path d="M -26,68 Q 0,92 26,68" fill="none" stroke="{INK}" stroke-width="3.4"/>')
        parts.append(f'<line x1="-10" y1="80" x2="-12" y2="112" stroke="#F5EFE4" stroke-width="3" stroke-linecap="round"/>')
        parts.append(f'<line x1="10" y1="80" x2="12" y2="112" stroke="#F5EFE4" stroke-width="3" stroke-linecap="round"/>')
    else:
        # Shirt V-collar & tie
        parts.append(f'<polygon points="-20,67 0,115 20,67" fill="{shirt_c}" stroke="{INK}" stroke-width="3.2" stroke-linejoin="round"/>')
        parts.append(f'<polygon points="-5,74 5,74 8,112 0,124 -8,112" fill="{tie_c}" stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"/>')
        # Collar flaps
        parts.append(f'<polygon points="-24,66 -4,76 -15,88" fill="#FFFFFF" stroke="{INK}" stroke-width="2.8" stroke-linejoin="round"/>')
        parts.append(f'<polygon points="24,66 4,76 15,88" fill="#FFFFFF" stroke="{INK}" stroke-width="2.8" stroke-linejoin="round"/>')

    # Arms by pose
    if pose == "point_up":
        parts.append(f'<path d="M -50,92 C -72,115 -68,142 -48,156" fill="none" stroke="{coat_c}" stroke-width="20" stroke-linecap="round"/>')
        parts.append(f'<path d="M -50,92 C -72,115 -68,142 -48,156" fill="none" stroke="{INK}" stroke-width="3.6" stroke-linecap="round"/>')
        parts.append(f'<path d="M 48,94 C 76,82 88,54 84,26" fill="none" stroke="{coat_c}" stroke-width="20" stroke-linecap="round"/>')
        parts.append(f'<path d="M 48,94 C 76,82 88,54 84,26" fill="none" stroke="{INK}" stroke-width="3.6" stroke-linecap="round"/>')
        parts.append(f'<circle cx="84" cy="20" r="11" fill="{SKIN}" stroke="{INK}" stroke-width="3.2"/>')
        parts.append(f'<line x1="84" y1="10" x2="84" y2="-4" stroke="{SKIN}" stroke-width="8" stroke-linecap="round"/>')
        parts.append(f'<line x1="84" y1="10" x2="84" y2="-4" stroke="{INK}" stroke-width="3.2" stroke-linecap="round"/>')
    elif pose == "hands_head":
        for s in (-1, 1):
            parts.append(f'<path d="M {s*46},90 C {s*84},62 {s*82},10 {s*56},-18" fill="none" stroke="{coat_c}" stroke-width="19" stroke-linecap="round"/>')
            parts.append(f'<path d="M {s*46},90 C {s*84},62 {s*82},10 {s*56},-18" fill="none" stroke="{INK}" stroke-width="3.6" stroke-linecap="round"/>')
            parts.append(f'<circle cx="{s*55}" cy="-20" r="10" fill="{SKIN}" stroke="{INK}" stroke-width="3.2"/>')
    elif pose == "shrug":
        for s in (-1, 1):
            parts.append(f'<path d="M {s*48},94 C {s*74},104 {s*88},84 {s*96},64" fill="none" stroke="{coat_c}" stroke-width="19" stroke-linecap="round"/>')
            parts.append(f'<path d="M {s*48},94 C {s*74},104 {s*88},84 {s*96},64" fill="none" stroke="{INK}" stroke-width="3.6" stroke-linecap="round"/>')
            parts.append(f'<circle cx="{s*98}" cy="60" r="11" fill="{SKIN}" stroke="{INK}" stroke-width="3.2"/>')
    elif pose == "think":
        parts.append(f'<path d="M 46,96 C 68,88 52,58 24,48" fill="none" stroke="{coat_c}" stroke-width="18" stroke-linecap="round"/>')
        parts.append(f'<path d="M 46,96 C 68,88 52,58 24,48" fill="none" stroke="{INK}" stroke-width="3.6" stroke-linecap="round"/>')
        parts.append(f'<circle cx="20" cy="46" r="10" fill="{SKIN}" stroke="{INK}" stroke-width="3.2"/>')
    elif pose == "arms_crossed":
        parts.append(f'<path d="M -46,108 Q 0,124 46,108" fill="none" stroke="{coat_c}" stroke-width="22" stroke-linecap="round"/>')
        parts.append(f'<path d="M -46,108 Q 0,124 46,108" fill="none" stroke="{INK}" stroke-width="3.6" stroke-linecap="round"/>')
    else:
        for s in (-1, 1):
            parts.append(f'<path d="M {s*48},92 C {s*64},118 {s*60},142 {s*48},158" fill="none" stroke="{coat_c}" stroke-width="18" stroke-linecap="round"/>')
            parts.append(f'<path d="M {s*48},92 C {s*64},118 {s*60},142 {s*48},158" fill="none" stroke="{INK}" stroke-width="3.6" stroke-linecap="round"/>')

    # Ears
    parts.append(f'<circle cx="-56" cy="4" r="12" fill="{SKIN}" stroke="{INK}" stroke-width="3.4"/>')
    parts.append(f'<circle cx="56" cy="4" r="12" fill="{SKIN}" stroke="{INK}" stroke-width="3.4"/>')

    # Head
    parts.append(f'<rect x="-56" y="-52" width="112" height="108" rx="48" fill="{SKIN}" stroke="{INK}" stroke-width="3.8"/>')

    # Rosy cheeks
    parts.append(f'<ellipse cx="-34" cy="18" rx="10" ry="6" fill="{CHEEK}" opacity="0.55"/>')
    parts.append(f'<ellipse cx="34" cy="18" rx="10" ry="6" fill="{CHEEK}" opacity="0.55"/>')

    # Hair front
    if hair == "male_wavy":
        parts.append(f'<path d="M -58,-10 C -64,-52 -28,-72 6,-68 C 42,-66 64,-44 58,-8 C 46,-26 28,-32 8,-26 C -8,-36 -26,-30 -40,-22 C -48,-20 -54,-14 -58,-10 Z" fill="{hair_c}" stroke="{INK}" stroke-width="3.6" stroke-linejoin="round"/>')
    elif hair == "female_bob" or hair == "female_ponytail":
        parts.append(f'<path d="M -58,-6 C -60,-52 -30,-68 0,-68 C 30,-68 60,-52 58,-6 C 44,-28 22,-34 0,-28 C -22,-34 -44,-28 -58,-6 Z" fill="{hair_c}" stroke="{INK}" stroke-width="3.6" stroke-linejoin="round"/>')
    elif hair == "boss_slick":
        parts.append(f'<path d="M -56,-12 C -58,-56 -20,-68 18,-64 C 48,-60 60,-38 56,-12 C 42,-34 10,-40 -26,-34 C -42,-30 -50,-22 -56,-12 Z" fill="#2C221E" stroke="{INK}" stroke-width="3.6" stroke-linejoin="round"/>')
    else:
        # Classic PhuNB neat side-part hair
        parts.append(f'<path d="M -57,-8 C -62,-50 -32,-68 4,-67 C 38,-66 62,-46 57,-8 C 48,-26 30,-35 8,-33 C -6,-24 -22,-22 -36,-28 C -46,-24 -52,-16 -57,-8 Z" fill="{hair_c}" stroke="{INK}" stroke-width="3.6" stroke-linejoin="round"/>')

    # Optional Hat / Headphones
    if hat == "helmet":
        parts.append(f'<path d="M -62,-26 C -58,-72 58,-72 62,-26 Z" fill="#F5B82E" stroke="{INK}" stroke-width="3.6" stroke-linejoin="round"/>')
        parts.append(f'<rect x="-68" y="-30" width="136" height="10" rx="5" fill="#E09B1B" stroke="{INK}" stroke-width="3.2"/>')
    elif hat == "explorer":
        parts.append(f'<ellipse cx="0" cy="-32" rx="74" ry="12" fill="#D9B37C" stroke="{INK}" stroke-width="3.4"/>')
        parts.append(f'<path d="M -46,-32 C -42,-70 42,-70 46,-32 Z" fill="#E6C594" stroke="{INK}" stroke-width="3.4"/>')
        parts.append(f'<rect x="-45" y="-40" width="90" height="8" fill="#8C583A"/>')
    elif hat == "crown":
        parts.append(f'<polygon points="-28,-62 -20,-86 -6,-70 0,-90 6,-70 20,-86 28,-62" fill="#F6C438" stroke="{INK}" stroke-width="3.2" stroke-linejoin="round"/>')
    elif hat == "headphones":
        parts.append(f'<path d="M -60,2 C -64,-58 64,-58 60,2" fill="none" stroke="#2D3748" stroke-width="8" stroke-linecap="round"/>')
        parts.append(f'<rect x="-68" y="-12" width="14" height="28" rx="6" fill="#4A90E2" stroke="{INK}" stroke-width="3"/>')
        parts.append(f'<rect x="54" y="-12" width="14" height="28" rx="6" fill="#4A90E2" stroke="{INK}" stroke-width="3"/>')

    # Expressions (Brows, Eyes, Mouth, Extras)
    if expr in ("sweat", "panic"):
        parts.append(f'<path d="M -34,-18 L -14,-12" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>')
        parts.append(f'<path d="M 34,-18 L 14,-12" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>')
        parts.append(f'<circle cx="-22" cy="0" r="5.5" fill="{INK}"/>')
        parts.append(f'<circle cx="22" cy="0" r="5.5" fill="{INK}"/>')
        parts.append(f'<path d="M -14,28 Q -7,22 0,28 T 14,28" fill="none" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>')
        # Sweat drop
        parts.append(f'<path d="M 46,-26 C 52,-14 54,-6 46,-4 C 38,-6 40,-14 46,-26 Z" fill="#7CC4F8" stroke="{INK}" stroke-width="2.6"/>')
    elif expr == "cry":
        parts.append(f'<path d="M -34,-12 L -14,-18" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>')
        parts.append(f'<path d="M 34,-12 L 14,-18" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>')
        parts.append(f'<path d="M -30,0 Q -22,-6 -14,0" fill="none" stroke="{INK}" stroke-width="3.6" stroke-linecap="round"/>')
        parts.append(f'<path d="M 14,0 Q 22,-6 30,0" fill="none" stroke="{INK}" stroke-width="3.6" stroke-linecap="round"/>')
        # Tear streams
        parts.append(f'<path d="M -24,4 L -28,42" stroke="#85CCF7" stroke-width="7" stroke-linecap="round" opacity="0.8"/>')
        parts.append(f'<path d="M 24,4 L 28,42" stroke="#85CCF7" stroke-width="7" stroke-linecap="round" opacity="0.8"/>')
        parts.append(f'<path d="M -15,32 Q 0,18 15,32" fill="#D96B6B" stroke="{INK}" stroke-width="3.2"/>')
    elif expr == "detective":
        parts.append(f'<path d="M -34,-14 L -12,-10" stroke="{INK}" stroke-width="3.8" stroke-linecap="round"/>')
        parts.append(f'<path d="M 34,-14 L 12,-10" stroke="{INK}" stroke-width="3.8" stroke-linecap="round"/>')
        parts.append(f'<circle cx="-22" cy="1" r="5" fill="{INK}"/>')
        parts.append(f'<circle cx="22" cy="1" r="5" fill="{INK}"/>')
        parts.append(f'<path d="M -10,27 Q 2,31 12,25" fill="none" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>')
    elif expr == "explain":
        parts.append(f'<path d="M -32,-16 Q -22,-22 -12,-16" fill="none" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>')
        parts.append(f'<path d="M 12,-16 Q 22,-22 32,-16" fill="none" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>')
        parts.append(f'<circle cx="-22" cy="0" r="5.2" fill="{INK}"/>')
        parts.append(f'<circle cx="22" cy="0" r="5.2" fill="{INK}"/>')
        parts.append(f'<ellipse cx="0" cy="28" rx="10" ry="8" fill="#D96B6B" stroke="{INK}" stroke-width="3.2"/>')
    elif expr == "shock":
        parts.append(f'<path d="M -32,-22 Q -22,-28 -12,-22" fill="none" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>')
        parts.append(f'<path d="M 12,-22 Q 22,-28 32,-22" fill="none" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>')
        parts.append(f'<circle cx="-22" cy="0" r="6.5" fill="#FFFFFF" stroke="{INK}" stroke-width="3"/>')
        parts.append(f'<circle cx="-22" cy="0" r="2.8" fill="{INK}"/>')
        parts.append(f'<circle cx="22" cy="0" r="6.5" fill="#FFFFFF" stroke="{INK}" stroke-width="3"/>')
        parts.append(f'<circle cx="22" cy="0" r="2.8" fill="{INK}"/>')
        parts.append(f'<ellipse cx="0" cy="29" rx="9" ry="11" fill="#D96B6B" stroke="{INK}" stroke-width="3.2"/>')
    elif expr == "zen":
        parts.append(f'<path d="M -30,-14 Q -22,-18 -14,-14" fill="none" stroke="{INK}" stroke-width="3.2" stroke-linecap="round"/>')
        parts.append(f'<path d="M 14,-14 Q 22,-18 30,-14" fill="none" stroke="{INK}" stroke-width="3.2" stroke-linecap="round"/>')
        parts.append(f'<path d="M -30,2 Q -22,8 -14,2" fill="none" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>')
        parts.append(f'<path d="M 14,2 Q 22,8 30,2" fill="none" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>')
        parts.append(f'<path d="M -12,25 Q 0,34 12,25" fill="none" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>')
    elif expr == "think":
        parts.append(f'<path d="M -32,-14 L -12,-14" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>')
        parts.append(f'<path d="M 12,-20 Q 22,-25 32,-18" fill="none" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>')
        parts.append(f'<circle cx="-20" cy="-1" r="5" fill="{INK}"/>')
        parts.append(f'<circle cx="24" cy="-2" r="5" fill="{INK}"/>')
        parts.append(f'<path d="M -8,27 L 10,25" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>')
    else:
        # Warm confident smile
        parts.append(f'<path d="M -32,-15 Q -22,-20 -12,-15" fill="none" stroke="{INK}" stroke-width="3.2" stroke-linecap="round"/>')
        parts.append(f'<path d="M 12,-15 Q 22,-20 32,-15" fill="none" stroke="{INK}" stroke-width="3.2" stroke-linecap="round"/>')
        parts.append(f'<circle cx="-22" cy="0" r="5.2" fill="{INK}"/>')
        parts.append(f'<circle cx="-20" cy="-2" r="1.8" fill="#FFFFFF"/>')
        parts.append(f'<circle cx="22" cy="0" r="5.2" fill="{INK}"/>')
        parts.append(f'<circle cx="24" cy="-2" r="1.8" fill="#FFFFFF"/>')
        parts.append(f'<path d="M -13,24 Q 0,35 13,24" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>')

    # Signature Glasses
    if glasses:
        parts.append(f'<rect x="-39" y="-11" width="32" height="23" rx="6" fill="#FFFFFF" fill-opacity="0.22" stroke="{INK}" stroke-width="3.4"/>')
        parts.append(f'<rect x="7" y="-11" width="32" height="23" rx="6" fill="#FFFFFF" fill-opacity="0.22" stroke="{INK}" stroke-width="3.4"/>')
        parts.append(f'<line x1="-7" y1="0" x2="7" y2="0" stroke="{INK}" stroke-width="3.4"/>')
        parts.append(f'<line x1="-55" y1="-2" x2="-39" y2="-1" stroke="{INK}" stroke-width="3"/>')
        parts.append(f'<line x1="39" y1="-1" x2="55" y2="-2" stroke="{INK}" stroke-width="3"/>')

    parts.append("</g>")
    return "\n".join(parts)


def card_box(x: float, y: float, w: float, h: float, fill: str = "#FFFDF7", rx: float = 14) -> str:
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{INK}" stroke-width="3.4" filter="url(#softShadow)"/>'


def speech_bubble(x: float, y: float, w: float, h: float, text_lines: list, fill: str = "#FFFDF7", text_color: str = INK, tail_dir: str = "down", font_size: int = 18) -> str:
    cx = x + w / 2
    if tail_dir == "down":
        tail = f'<polygon points="{cx-12},{y+h-2} {cx+12},{y+h-2} {cx-4},{y+h+18}" fill="{fill}" stroke="{INK}" stroke-width="3.2" stroke-linejoin="round"/>'
        cover = f'<line x1="{cx-10}" y1="{y+h}" x2="{cx+10}" y2="{y+h}" stroke="{fill}" stroke-width="5"/>'
    elif tail_dir == "left":
        tail = f'<polygon points="{x+2},{y+h*0.5-10} {x+2},{y+h*0.5+10} {x-18},{y+h*0.5+6}" fill="{fill}" stroke="{INK}" stroke-width="3.2" stroke-linejoin="round"/>'
        cover = f'<line x1="{x}" y1="{y+h*0.5-8}" x2="{x}" y2="{y+h*0.5+8}" stroke="{fill}" stroke-width="5"/>'
    else:
        tail = f'<polygon points="{x+w-2},{y+h*0.5-10} {x+w-2},{y+h*0.5+10} {x+w+18},{y+h*0.5+6}" fill="{fill}" stroke="{INK}" stroke-width="3.2" stroke-linejoin="round"/>'
        cover = f'<line x1="{x+w}" y1="{y+h*0.5-8}" x2="{x+w}" y2="{y+h*0.5+8}" stroke="{fill}" stroke-width="5"/>'

    rect = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="{INK}" stroke-width="3.2" filter="url(#softShadow)"/>'
    start_y = y + (h - (len(text_lines) - 1) * (font_size + 6)) / 2 + font_size * 0.34
    t_elems = []
    for i, line in enumerate(text_lines):
        t_elems.append(f'<text x="{cx}" y="{start_y + i*(font_size+6)}" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="{font_size}" fill="{text_color}">{esc(line)}</text>')
    return "\n".join([tail, rect, cover] + t_elems)


def sticky_note(x: float, y: float, w: float, h: float, title: str, sub: str = "", fill: str = "#FFE999", rot: float = 0) -> str:
    cx, cy = x + w / 2, y + h / 2
    s = [f'<g transform="rotate({rot} {cx} {cy})">']
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{INK}" stroke-width="3.2" filter="url(#softShadow)"/>')
    s.append(f'<rect x="{cx-18}" y="{y-7}" width="36" height="14" rx="3" fill="#E8C266" opacity="0.85"/>')
    ty = cy - 6 if sub else cy + 6
    s.append(f'<text x="{cx}" y="{ty}" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="17" fill="{INK}">{esc(title)}</text>')
    if sub:
        s.append(f'<text x="{cx}" y="{ty+22}" text-anchor="middle" font-family="Segoe UI, sans-serif" font-weight="700" font-size="14" fill="#5C402B">{esc(sub)}</text>')
    s.append("</g>")
    return "\n".join(s)


def badge_tag(x: float, y: float, w: float, h: float, label: str, fill: str = "#D7E8FA", color: str = "#0B4DA2", font_size: int = 16) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{fill}" stroke="{INK}" stroke-width="3"/>'
        f'<text x="{x+w/2}" y="{y+h/2+font_size*0.35}" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="{font_size}" fill="{color}">{esc(label)}</text>'
    )


def arrow_curved(x1: float, y1: float, cx: float, cy: float, x2: float, y2: float, color: str = INK) -> str:
    # Draw curve + small arrowhead at (x2, y2)
    import math
    ang = math.atan2(y2 - cy, x2 - cx)
    a1 = ang + 2.6
    a2 = ang - 2.6
    r = 12
    p1x, p1y = x2 + r * math.cos(a1), y2 + r * math.sin(a1)
    p2x, p2y = x2 + r * math.cos(a2), y2 + r * math.sin(a2)
    return (
        f'<path d="M {x1},{y1} Q {cx},{cy} {x2},{y2}" fill="none" stroke="{color}" stroke-width="3.6" stroke-linecap="round"/>'
        f'<path d="M {p1x:.1f},{p1y:.1f} L {x2},{y2} L {p2x:.1f},{p2y:.1f}" fill="none" stroke="{color}" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/>'
    )


def laptop_prop(cx: float, cy: float, scale: float = 1.0, label: str = "BA") -> str:
    return f"""
    <g transform="translate({cx},{cy}) scale({scale})">
      <polygon points="-68,-44 68,-44 58,34 -58,34" fill="#7D8794" stroke="{INK}" stroke-width="3.6" stroke-linejoin="round"/>
      <polygon points="-60,-36 60,-36 52,28 -52,28" fill="#9BB3C9" stroke="{INK}" stroke-width="2.4"/>
      <circle cx="0" cy="-4" r="16" fill="#EDF3F8" stroke="{INK}" stroke-width="2.6"/>
      <text x="0" y="2" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="13" fill="{INK}">{esc(label)}</text>
      <rect x="-82" y="34" width="164" height="12" rx="6" fill="#B5BDC7" stroke="{INK}" stroke-width="3.6"/>
    </g>
    """
