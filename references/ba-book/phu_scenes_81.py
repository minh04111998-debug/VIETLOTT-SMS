# -*- coding: utf-8 -*-
"""
28 Distinct Warm-Cream Storybook Illustration Archetypes + 81 Custom Day-by-Day Configurations
for '100 ngày làm BA' — matching Mr. Phú's warm cream (#FAEFD3) + Royal Blue (#054AA3) concept.
Zero 'IT BA' / 'ITBA' text anywhere.
"""
from phu_chibi_lib import (
    INK,
    arrow_curved,
    badge_tag,
    card_box,
    draw_chibi,
    esc,
    laptop_prop,
    speech_bubble,
    sticky_note,
    svg_defs,
    wash_blob,
)


def wrap_svg(w: int, h: int, inner: str) -> str:
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">{svg_defs()}{inner}</svg>'


# ==============================================================================
# 28 DISTINCT STORYBOOK ILLUSTRATION ARCHETYPES (Warm Ink + Watercolor Palette)
# ==============================================================================

def arch_rocket_telemetry(c: dict) -> str:
    # Rocket launch + live dashboard + smiling BA
    body = f"""
    {wash_blob(430, 250, 340, 185, "skyWash", 0)}
    <!-- Rocket -->
    <g transform="translate(185,235) rotate(-18)">
      <path d="M 0,-95 C 34,-50 36,20 28,65 L -28,65 C -36,20 -34,-50 0,-95 Z" fill="#FFFDF7" stroke="{INK}" stroke-width="3.6"/>
      <path d="M 0,-95 C 18,-70 23,-45 24,-30 L -24,-30 C -23,-45 -18,-70 0,-95 Z" fill="#E05A47" stroke="{INK}" stroke-width="3.4"/>
      <circle cx="0" cy="4" r="16" fill="#8CC5F2" stroke="{INK}" stroke-width="3.2"/>
      <polygon points="-28,35 -54,72 -24,62" fill="#E05A47" stroke="{INK}" stroke-width="3.2" stroke-linejoin="round"/>
      <polygon points="28,35 54,72 24,62" fill="#E05A47" stroke="{INK}" stroke-width="3.2" stroke-linejoin="round"/>
      <path d="M -16,66 Q 0,118 16,66 Z" fill="#F6B93B" stroke="{INK}" stroke-width="3"/>
    </g>
    <!-- Dashboard Card -->
    {card_box(310, 65, 250, 155, "#FFFDF7")}
    <text x="435" y="96" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="16" fill="#054AA3">{esc(c['p1'])}</text>
    <polyline points="335,185 380,155 425,165 475,122 530,108" fill="none" stroke="#2D8A56" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="530" cy="108" r="6" fill="#2D8A56"/>
    {badge_tag(332, 195, 102, 30, c['p2'], "#DCF2E4", "#1F6E43", 13)}
    {badge_tag(446, 195, 102, 30, c['p3'], "#FDE8D7", "#A8431D", 13)}
    {draw_chibi(665, 295, 0.98, expr=c.get("expr","smile"), hair=c.get("hair","male_neat"), outfit=c.get("outfit","blue_shirt"), pose="point_up")}
    """
    return wrap_svg(860, 460, body)


def arch_crooked_house(c: dict) -> str:
    body = f"""
    {wash_blob(420, 250, 350, 185, "sandWash", 1)}
    <!-- Leaning crooked house -->
    <g transform="translate(235,245) rotate(-9)">
      <polygon points="-110,-40 110,-55 95,115 -95,115" fill="#E89D67" stroke="{INK}" stroke-width="3.8" stroke-linejoin="round"/>
      <polygon points="-128,-38 4,-128 128,-52" fill="#C9523E" stroke="{INK}" stroke-width="3.8" stroke-linejoin="round"/>
      <rect x="-65" y="-10" width="42" height="42" transform="rotate(8 -44 11)" fill="#BEE0F7" stroke="{INK}" stroke-width="3.2"/>
      <rect x="20" y="-18" width="42" height="42" transform="rotate(-12 41 3)" fill="#BEE0F7" stroke="{INK}" stroke-width="3.2"/>
      <rect x="-18" y="48" width="44" height="66" fill="#7D5338" stroke="{INK}" stroke-width="3.2"/>
      <path d="M 30,65 L 55,82 L 42,98" fill="none" stroke="{INK}" stroke-width="2.8"/>
    </g>
    {sticky_note(365, 85, 175, 82, c['p1'], c['p2'], "#FFE89E", -4)}
    {draw_chibi(645, 295, 0.98, expr="sweat", hair=c.get("hair","male_neat"), outfit="builder_vest", hat="helmet", pose="hands_head")}
    """
    return wrap_svg(860, 460, body)


def arch_shield_defense(c: dict) -> str:
    body = f"""
    {wash_blob(290, 270, 245, 200, "skyWash", 2)}
    {speech_bubble(24, 55, 235, 76, [c['p1'], c['p2']], "#FDE2DC", "#A62B2B", "right", 16)}
    <!-- Big Signed Confirmation Shield -->
    <path d="M 195,175 L 315,155 L 315,275 C 315,345 255,388 255,388 C 255,388 195,345 195,275 Z" fill="#F8C957" stroke="{INK}" stroke-width="4" stroke-linejoin="round" filter="url(#softShadow)"/>
    <path d="M 212,190 L 298,174 L 298,270 C 298,322 255,358 255,358 C 255,358 212,322 212,270 Z" fill="#FFF7DF" stroke="{INK}" stroke-width="2.8"/>
    <path d="M 234,262 L 250,280 L 280,242" fill="none" stroke="#267A48" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="255" y="218" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="14" fill="{INK}">{esc(c['p3'])}</text>
    {draw_chibi(435, 325, 0.96, expr=c.get("expr","smile"), hair=c.get("hair","male_neat"), outfit=c.get("outfit","brown_suit"), pose="point_up")}
    """
    return wrap_svg(560, 500, body)


def arch_team_compass(c: dict) -> str:
    body = f"""
    {wash_blob(430, 250, 355, 190, "sageWash", 0)}
    <!-- Left & Right Junior teammates -->
    {draw_chibi(195, 320, 0.78, expr="smile", hair="female_bob", outfit="sage_vest", glasses=False)}
    {draw_chibi(675, 320, 0.78, expr="smile", hair="male_wavy", outfit="white_tie", glasses=False)}
    <!-- Center Leader/BA -->
    {draw_chibi(435, 295, 1.0, expr=c.get("expr","smile"), hair=c.get("hair","senior_mentor"), outfit=c.get("outfit","brown_suit"), pose="point_up")}
    {badge_tag(115, 125, 175, 42, c['p1'], "#FFF5D6", INK, 15)}
    {badge_tag(342, 65, 185, 44, c['p2'], "#D9ECFF", "#054AA3", 15)}
    {badge_tag(575, 125, 175, 42, c['p3'], "#DFF2E3", "#1F6B3E", 15)}
    {arrow_curved(295, 145, 335, 110, 355, 95, "#6E5A47")}
    {arrow_curved(515, 95, 545, 110, 572, 145, "#6E5A47")}
    """
    return wrap_svg(860, 460, body)


def arch_bridge_worlds(c: dict) -> str:
    body = f"""
    {wash_blob(430, 250, 360, 185, "skyWash", 1)}
    <!-- Left Card -->
    {card_box(70, 130, 210, 150, "#E8F2FC")}
    <text x="175" y="175" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="19" fill="#054AA3">{esc(c['p1'])}</text>
    <text x="175" y="212" text-anchor="middle" font-family="Consolas, monospace" font-weight="700" font-size="16" fill="#2D4A6A">{esc(c['p2'])}</text>
    <rect x="105" y="232" width="140" height="24" rx="6" fill="#FFFDF7" stroke="{INK}" stroke-width="2.4"/>
    <!-- Right Card -->
    {card_box(580, 130, 210, 150, "#FDF1D6")}
    <text x="685" y="175" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="19" fill="#9C4A1A">{esc(c['p3'])}</text>
    <text x="685" y="212" text-anchor="middle" font-family="Segoe UI, sans-serif" font-weight="700" font-size="16" fill="#5C3D24">{esc(c['p4'])}</text>
    <rect x="615" y="232" width="140" height="24" rx="6" fill="#FFFDF7" stroke="{INK}" stroke-width="2.4"/>
    <!-- Golden Arch Bridge -->
    <path d="M 265,245 Q 430,155 595,245" fill="none" stroke="#E59A38" stroke-width="12" stroke-linecap="round"/>
    <path d="M 265,245 Q 430,155 595,245" fill="none" stroke="{INK}" stroke-width="3.6" stroke-linecap="round"/>
    {draw_chibi(430, 295, 0.96, expr=c.get("expr","smile"), hair=c.get("hair","male_neat"), outfit=c.get("outfit","blue_shirt"), pose="shrug")}
    """
    return wrap_svg(860, 460, body)


def arch_cliff_carpet(c: dict) -> str:
    body = f"""
    {wash_blob(430, 250, 350, 185, "peachWash", 2)}
    <!-- Cliff & Red Roadmap Carpet -->
    <path d="M 60,360 L 470,360 L 495,455 L 60,455 Z" fill="#D5B895" stroke="{INK}" stroke-width="3.8" stroke-linejoin="round"/>
    <path d="M 75,346 L 565,346 C 605,346 615,395 620,440" fill="none" stroke="#D9534F" stroke-width="20" stroke-linecap="round"/>
    <path d="M 75,346 L 565,346 C 605,346 615,395 620,440" fill="none" stroke="{INK}" stroke-width="3.4" stroke-dasharray="12 8"/>
    {badge_tag(120, 285, 250, 44, c['p1'], "#FDE2DC", "#A62828", 16)}
    {sticky_note(545, 95, 215, 92, c['p2'], c['p3'], "#FFF3B8", 5)}
    {draw_chibi(395, 235, 0.92, expr="shock", hair=c.get("hair","male_neat"), outfit=c.get("outfit","grey_blazer"), pose="hands_head")}
    """
    return wrap_svg(860, 460, body)


def arch_whirlwind_tickets(c: dict) -> str:
    body = f"""
    {wash_blob(280, 265, 245, 200, "sandWash", 0)}
    <!-- Swirling lines -->
    <path d="M 75,240 C 60,120 480,110 485,240" fill="none" stroke="#B89B72" stroke-width="3" stroke-dasharray="10 8"/>
    {sticky_note(42, 95, 145, 72, c['p1'], "", "#FFE699", -12)}
    {sticky_note(365, 88, 155, 72, c['p2'], "", "#FAD7CE", 11)}
    {sticky_note(38, 265, 145, 72, c['p3'], "", "#D8ECFA", 8)}
    {sticky_note(375, 265, 148, 72, c['p4'], "", "#DCF2E2", -9)}
    {draw_chibi(280, 315, 1.0, expr=c.get("expr","sweat"), hair=c.get("hair","male_wavy"), outfit=c.get("outfit","blue_shirt"), hat=c.get("hat","helmet"), pose="hands_head")}
    """
    return wrap_svg(560, 500, body)


def arch_balance_scale(c: dict) -> str:
    body = f"""
    {wash_blob(430, 255, 355, 185, "sandWash", 1)}
    <!-- Golden Balance Scale -->
    <line x1="430" y1="95" x2="430" y2="395" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
    <rect x="365" y="390" width="130" height="18" rx="8" fill="#D99B38" stroke="{INK}" stroke-width="3.4"/>
    <g transform="rotate({c.get('tilt', -8)} 430 135)">
      <line x1="185" y1="135" x2="675" y2="135" stroke="#D99B38" stroke-width="10" stroke-linecap="round"/>
      <line x1="185" y1="135" x2="675" y2="135" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/>
      <!-- Left Pan -->
      <line x1="195" y1="135" x2="155" y2="235" stroke="{INK}" stroke-width="2.8"/>
      <line x1="195" y1="135" x2="235" y2="235" stroke="{INK}" stroke-width="2.8"/>
      <path d="M 125,235 Q 195,275 265,235 Z" fill="#F5C451" stroke="{INK}" stroke-width="3.4"/>
      {card_box(120, 168, 150, 62, "#E3F1FD", 10)}
      <text x="195" y="205" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="16" fill="#054AA3">{esc(c['p1'])}</text>
      <!-- Right Pan -->
      <line x1="665" y1="135" x2="625" y2="235" stroke="{INK}" stroke-width="2.8"/>
      <line x1="665" y1="135" x2="705" y2="235" stroke="{INK}" stroke-width="2.8"/>
      <path d="M 595,235 Q 665,275 735,235 Z" fill="#F5C451" stroke="{INK}" stroke-width="3.4"/>
      {card_box(590, 168, 150, 62, "#FDE6D8", 10)}
      <text x="665" y="205" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="16" fill="#A33B1C">{esc(c['p2'])}</text>
    </g>
    {draw_chibi(430, 310, 0.9, expr=c.get("expr","think"), hair=c.get("hair","male_neat"), outfit=c.get("outfit","brown_suit"), pose="think")}
    """
    return wrap_svg(860, 460, body)


def arch_keyhole_tools(c: dict) -> str:
    body = f"""
    {wash_blob(280, 265, 240, 195, "sageWash", 2)}
    <!-- Big Vault / Lock Card -->
    {card_box(60, 95, 205, 250, "#EAE2D3", 20)}
    <circle cx="162" cy="195" r="26" fill="{INK}"/>
    <polygon points="150,205 174,205 182,265 142,265" fill="{INK}"/>
    <text x="162" y="138" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="16" fill="#054AA3">{esc(c['p1'])}</text>
    <!-- Glowing Golden Key -->
    <g transform="translate(335,155) rotate(-20)">
      <circle cx="-42" cy="0" r="24" fill="#F7C948" stroke="{INK}" stroke-width="3.6"/>
      <circle cx="-42" cy="0" r="9" fill="#FAEFD3" stroke="{INK}" stroke-width="3"/>
      <rect x="-18" y="-7" width="82" height="14" rx="4" fill="#F7C948" stroke="{INK}" stroke-width="3.4"/>
      <rect x="36" y="7" width="10" height="16" fill="#F7C948" stroke="{INK}" stroke-width="3"/>
      <rect x="52" y="7" width="10" height="12" fill="#F7C948" stroke="{INK}" stroke-width="3"/>
    </g>
    {badge_tag(290, 68, 225, 40, c['p2'], "#FFF3C4", INK, 15)}
    {draw_chibi(395, 325, 0.96, expr=c.get("expr","detective"), hair=c.get("hair","female_bob"), outfit=c.get("outfit","sage_vest"), pose="point_up")}
    """
    return wrap_svg(560, 500, body)


def arch_square_wheel_cart(c: dict) -> str:
    body = f"""
    {wash_blob(430, 255, 355, 185, "peachWash", 0)}
    <!-- Cart with Square Wheels -->
    <rect x="115" y="185" width="275" height="125" rx="12" fill="#E9B872" stroke="{INK}" stroke-width="3.8"/>
    <text x="252" y="238" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="19" fill="{INK}">{esc(c['p1'])}</text>
    <text x="252" y="268" text-anchor="middle" font-family="Segoe UI, sans-serif" font-weight="700" font-size="15" fill="#7A2E1D">{esc(c['p2'])}</text>
    <!-- Square wheels! -->
    <rect x="145" y="295" width="66" height="66" transform="rotate(12 178 328)" fill="#6E7680" stroke="{INK}" stroke-width="3.8"/>
    <rect x="295" y="295" width="66" height="66" transform="rotate(-8 328 328)" fill="#6E7680" stroke="{INK}" stroke-width="3.8"/>
    {speech_bubble(435, 68, 315, 74, [c['p3']], "#FFFDF7", "#A62828", "down", 17)}
    {draw_chibi(615, 295, 0.96, expr=c.get("expr","sweat"), hair=c.get("hair","male_neat"), outfit=c.get("outfit","blue_shirt"), pose="shrug")}
    """
    return wrap_svg(860, 460, body)


def arch_railway_switch(c: dict) -> str:
    body = f"""
    {wash_blob(430, 255, 360, 185, "sageWash", 1)}
    <!-- Railway Tracks branching -->
    <path d="M 70,350 L 340,350 Q 460,350 580,225 L 780,225" fill="none" stroke="#5A6572" stroke-width="10" stroke-linecap="round"/>
    <path d="M 340,350 Q 460,350 595,385 L 775,385" fill="none" stroke="#C8B9A6" stroke-width="8" stroke-dasharray="12 10"/>
    <!-- Obstacle on old track -->
    {badge_tag(605, 362, 165, 42, c['p2'], "#FAD7CE", "#9E2A2A", 14)}
    <!-- Clean Finish Flag on switched track -->
    {badge_tag(585, 152, 195, 46, c['p1'], "#D7F2DF", "#1B6B3A", 15)}
    {sticky_note(110, 125, 205, 84, c['p3'], c.get('p4',''), "#FFF2B2", -4)}
    {draw_chibi(405, 275, 0.94, expr="detective", hair=c.get("hair","male_neat"), outfit=c.get("outfit","orange_cardigan"), pose="point_up")}
    """
    return wrap_svg(860, 460, body)


def arch_debate_table(c: dict) -> str:
    body = f"""
    {wash_blob(430, 260, 360, 185, "peachWash", 2)}
    <!-- Left Person (Angry/Stubborn) -->
    {speech_bubble(65, 58, 255, 72, [c['p1']], "#FAD8CE", "#9E2424", "down", 16)}
    {draw_chibi(195, 295, 0.92, expr="shock", hair="boss_slick", outfit="grey_blazer", glasses=False, pose="arms_crossed")}
    <!-- Center Evidence Board -->
    {card_box(332, 150, 196, 145, "#FFFDF7")}
    <text x="430" y="185" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="16" fill="#054AA3">{esc(c['p2'])}</text>
    <rect x="355" y="205" width="150" height="22" rx="6" fill="#DCF2E3"/>
    <rect x="355" y="238" width="115" height="22" rx="6" fill="#DCEBFB"/>
    <text x="430" y="280" text-anchor="middle" font-family="Segoe UI, sans-serif" font-weight="700" font-size="14" fill="#4A5568">{esc(c['p3'])}</text>
    <!-- Right Calm BA -->
    {speech_bubble(545, 58, 255, 72, [c.get('p4','Dữ liệu & Logic')], "#DCF2E4", "#1B6B3A", "down", 16)}
    {draw_chibi(665, 295, 0.92, expr="smile", hair=c.get("hair","male_neat"), outfit=c.get("outfit","blue_shirt"), pose="point_up")}
    """
    return wrap_svg(860, 460, body)


def arch_iceberg_depth(c: dict) -> str:
    body = f"""
    {wash_blob(280, 265, 245, 200, "skyWash", 0)}
    <!-- Waterline -->
    <path d="M 25,215 Q 150,202 280,215 T 535,215 L 535,465 L 25,465 Z" fill="#CBE3F5" opacity="0.72"/>
    <line x1="25" y1="215" x2="535" y2="215" stroke="#2D6DA3" stroke-width="3.5" stroke-dasharray="10 6"/>
    <!-- Tip of Iceberg -->
    <polygon points="155,215 215,118 275,215" fill="#FFFFFF" stroke="{INK}" stroke-width="3.6" stroke-linejoin="round"/>
    <text x="215" y="192" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="14" fill="#054AA3">{esc(c['p1'])}</text>
    <!-- Giant Underwater Iceberg -->
    <polygon points="135,218 295,218 335,335 255,435 145,420 95,320" fill="#89BBE0" stroke="{INK}" stroke-width="3.6" stroke-linejoin="round"/>
    <text x="215" y="285" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="16" fill="{INK}">{esc(c['p2'])}</text>
    <text x="215" y="320" text-anchor="middle" font-family="Segoe UI, sans-serif" font-weight="700" font-size="15" fill="#1A365D">{esc(c['p3'])}</text>
    <text x="215" y="352" text-anchor="middle" font-family="Segoe UI, sans-serif" font-weight="700" font-size="15" fill="#1A365D">{esc(c.get('p4',''))}</text>
    {draw_chibi(435, 315, 0.92, expr=c.get("expr","detective"), hair=c.get("hair","male_neat"), outfit=c.get("outfit","brown_suit"), pose="point_up")}
    """
    return wrap_svg(560, 500, body)


def arch_system_tree_roots(c: dict) -> str:
    body = f"""
    {wash_blob(430, 250, 355, 190, "sageWash", 1)}
    <!-- Ground line -->
    <line x1="80" y1="295" x2="560" y2="295" stroke="#7D5A3C" stroke-width="4" stroke-linecap="round"/>
    <!-- Tree Crown -->
    <circle cx="315" cy="145" r="78" fill="#7BC47F" stroke="{INK}" stroke-width="3.6"/>
    <circle cx="255" cy="168" r="52" fill="#8FD18E" stroke="{INK}" stroke-width="3.4"/>
    <circle cx="375" cy="168" r="52" fill="#8FD18E" stroke="{INK}" stroke-width="3.4"/>
    <text x="315" y="152" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="17" fill="{INK}">{esc(c['p1'])}</text>
    <!-- Trunk & Deep Roots -->
    <path d="M 295,215 L 290,295 M 335,215 L 340,295" stroke="#8C583A" stroke-width="18" stroke-linecap="round"/>
    <path d="M 315,295 C 285,345 215,375 165,405 M 315,295 L 315,415 M 315,295 C 345,345 415,375 465,405" fill="none" stroke="#8C583A" stroke-width="8" stroke-linecap="round"/>
    {badge_tag(105, 385, 135, 36, c['p2'], "#FFF3C4", INK, 14)}
    {badge_tag(252, 395, 135, 36, c['p3'], "#D8ECFA", "#054AA3", 14)}
    {badge_tag(400, 385, 135, 36, c.get('p4','State & Rule'), "#FADBD2", "#9C2B2B", 14)}
    {draw_chibi(675, 295, 0.96, expr=c.get("expr","smile"), hair=c.get("hair","male_neat"), outfit=c.get("outfit","sage_vest"), pose="point_up")}
    """
    return wrap_svg(860, 460, body)


def arch_fistbump_alliance(c: dict) -> str:
    body = f"""
    {wash_blob(430, 255, 350, 185, "skyWash", 2)}
    <!-- Spark Star in Center -->
    <polygon points="430,115 444,152 484,152 452,175 464,212 430,188 396,212 408,175 376,152 416,152" fill="#F7C948" stroke="{INK}" stroke-width="3.2" stroke-linejoin="round"/>
    {badge_tag(345, 58, 170, 40, c['p1'], "#FFF4C7", INK, 15)}
    <!-- Left BA -->
    {draw_chibi(235, 295, 0.95, expr="smile", hair="male_neat", outfit="blue_shirt", pose="point_up")}
    {badge_tag(150, 118, 150, 38, c['p2'], "#DCEBFB", "#054AA3", 15)}
    <!-- Right DEV / QA -->
    {draw_chibi(625, 295, 0.95, expr="smile", hair="male_wavy", outfit="dark_hoodie", glasses=False, hat=c.get("hat2","headphones"))}
    {badge_tag(560, 118, 150, 38, c['p3'], "#DCF2E4", "#1B6B3A", 15)}
    """
    return wrap_svg(860, 460, body)


def arch_git_whiteboard(c: dict) -> str:
    body = f"""
    {wash_blob(430, 255, 360, 185, "sandWash", 0)}
    <!-- Warm Cork/Whiteboard -->
    {card_box(85, 70, 445, 305, "#FFFDF8", 16)}
    <rect x="85" y="70" width="445" height="42" rx="14" fill="#054AA3"/>
    <text x="307" y="97" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="17" fill="#FFFFFF">{esc(c['p1'])}</text>
    <!-- Git Branch Graph -->
    <line x1="130" y1="175" x2="485" y2="175" stroke="#054AA3" stroke-width="6" stroke-linecap="round"/>
    <path d="M 195,175 C 225,175 235,255 265,255 L 365,255 C 395,255 405,175 435,175" fill="none" stroke="#E06D44" stroke-width="6" stroke-linecap="round"/>
    <circle cx="155" cy="175" r="11" fill="#FFF" stroke="#054AA3" stroke-width="5"/>
    <circle cx="195" cy="175" r="11" fill="#FFF" stroke="#054AA3" stroke-width="5"/>
    <circle cx="275" cy="255" r="11" fill="#FFF" stroke="#E06D44" stroke-width="5"/>
    <circle cx="355" cy="255" r="11" fill="#FFF" stroke="#E06D44" stroke-width="5"/>
    <circle cx="435" cy="175" r="12" fill="#2D8A56" stroke="{INK}" stroke-width="3.5"/>
    {badge_tag(120, 126, 95, 30, c['p2'], "#DCEBFB", "#054AA3", 13)}
    {badge_tag(255, 282, 125, 30, c['p3'], "#FDE5D8", "#A33B1C", 13)}
    {badge_tag(390, 126, 115, 30, c.get('p4','Merge / Tag'), "#DCF2E4", "#1B6B3A", 13)}
    {draw_chibi(665, 295, 0.96, expr=c.get("expr","explain"), hair=c.get("hair","male_neat"), outfit=c.get("outfit","orange_cardigan"), pose="point_up")}
    """
    return wrap_svg(860, 460, body)


def arch_open_book_pop(c: dict) -> str:
    body = f"""
    {wash_blob(280, 265, 240, 195, "sandWash", 1)}
    <!-- Open Storybook -->
    <path d="M 65,335 Q 170,305 275,335 Q 380,305 485,335 L 495,415 Q 380,388 275,415 Q 170,388 55,415 Z" fill="#FFFDF7" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>
    <line x1="275" y1="335" x2="275" y2="415" stroke="{INK}" stroke-width="3.6"/>
    <!-- Popping Knowledge Cards -->
    {sticky_note(55, 115, 155, 86, c['p1'], c['p2'], "#D8ECFA", -8)}
    {sticky_note(345, 115, 160, 86, c['p3'], c.get('p4',''), "#FFE89E", 8)}
    {draw_chibi(275, 215, 0.88, expr=c.get("expr","smile"), hair=c.get("hair","female_ponytail"), outfit=c.get("outfit","sage_vest"), pose="point_up")}
    """
    return wrap_svg(560, 500, body)


def arch_speedboat_game(c: dict) -> str:
    body = f"""
    {wash_blob(430, 250, 360, 190, "skyWash", 2)}
    <!-- Sea Waves -->
    <path d="M 60,285 Q 150,265 240,285 T 420,285 T 600,285 T 790,285 L 790,435 L 60,435 Z" fill="#9AC7EB" opacity="0.65"/>
    <!-- Speedboat -->
    <polygon points="225,245 555,245 615,195 515,288 255,288" fill="#E05A47" stroke="{INK}" stroke-width="3.8" stroke-linejoin="round"/>
    <polygon points="335,245 455,245 425,195 355,195" fill="#FFFDF7" stroke="{INK}" stroke-width="3.4"/>
    <!-- Wind Boost -->
    {badge_tag(95, 145, 175, 42, c['p1'], "#DCF2E4", "#1B6B3A", 15)}
    <path d="M 278,165 L 335,165 M 265,182 L 320,182" stroke="#1B6B3A" stroke-width="4" stroke-linecap="round"/>
    <!-- Heavy Underwater Anchors -->
    <line x1="330" y1="288" x2="330" y2="375" stroke="{INK}" stroke-width="3.6" stroke-dasharray="6 5"/>
    <circle cx="330" cy="392" r="20" fill="#5A6572" stroke="{INK}" stroke-width="3.4"/>
    {badge_tag(368, 368, 195, 40, c['p2'], "#FAD8CE", "#9E2424", 15)}
    {draw_chibi(695, 295, 0.9, expr="explain", hair="male_neat", outfit="blue_shirt", pose="point_up")}
    """
    return wrap_svg(860, 460, body)


def arch_mobile_thumb(c: dict) -> str:
    body = f"""
    {wash_blob(280, 260, 240, 200, "peachWash", 0)}
    <!-- Big Smartphone -->
    <rect x="85" y="65" width="195" height="355" rx="28" fill="#3B4252" stroke="{INK}" stroke-width="4"/>
    <rect x="99" y="92" width="167" height="298" rx="14" fill="#FFFDF7" stroke="{INK}" stroke-width="2.6"/>
    <!-- Thumb Zone Arcs -->
    <path d="M 266,390 A 155,155 0 0,0 111,235 L 266,390 Z" fill="#8AD499" opacity="0.75"/>
    <path d="M 266,235 A 155,155 0 0,0 99,145 L 99,235 Z" fill="#F9D56E" opacity="0.65"/>
    <rect x="115" y="108" width="135" height="34" rx="8" fill="#F5B7B1"/>
    <text x="182" y="130" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="13" fill="#922B21">{esc(c['p1'])}</text>
    <text x="200" y="348" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="15" fill="#1B6B3A">{esc(c['p2'])}</text>
    {draw_chibi(415, 315, 0.94, expr=c.get("expr","smile"), hair=c.get("hair","female_bob"), outfit=c.get("outfit","orange_cardigan"), pose="point_up")}
    """
    return wrap_svg(560, 500, body)


def arch_flashlight_fog(c: dict) -> str:
    body = f"""
    {wash_blob(430, 255, 360, 185, "sandWash", 1)}
    <!-- Fog / Grey Zone Cloud on Right -->
    <ellipse cx="615" cy="225" rx="165" ry="115" fill="#CBD5E0" opacity="0.85" stroke="{INK}" stroke-width="3" stroke-dasharray="10 6"/>
    <!-- Bright Golden Spotlight Cone cutting through fog -->
    <polygon points="275,265 665,105 685,345" fill="#FFF3B0" opacity="0.86"/>
    {badge_tag(485, 145, 195, 42, c['p1'], "#FFFDF7", "#054AA3", 15)}
    {badge_tag(505, 205, 195, 42, c['p2'], "#DCF2E4", "#1B6B3A", 15)}
    {badge_tag(485, 265, 195, 42, c['p3'], "#FDE5D8", "#9E2A2A", 15)}
    {draw_chibi(195, 295, 0.98, expr=c.get("expr","detective"), hair=c.get("hair","male_neat"), outfit=c.get("outfit","brown_suit"), hat=c.get("hat","explorer"), pose="point_up")}
    """
    return wrap_svg(860, 460, body)


def arch_three_specimens(c: dict) -> str:
    body = f"""
    {wash_blob(430, 255, 365, 185, "skyWash", 2)}
    <!-- 3 Distinct Illustrated Specimen Cards + Chibi BA -->
    {card_box(65, 105, 175, 210, "#FDE8E4", 18)}
    <circle cx="152" cy="165" r="28" fill="#E05A47" stroke="{INK}" stroke-width="3.2"/>
    <text x="152" y="173" text-anchor="middle" font-size="24">1</text>
    <text x="152" y="232" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="16" fill="{INK}">{esc(c['p1'])}</text>
    <text x="152" y="262" text-anchor="middle" font-family="Segoe UI, sans-serif" font-weight="700" font-size="13" fill="#6E3B3B">{esc(c.get('s1',''))}</text>

    {card_box(262, 85, 175, 210, "#FFF4CE", 18)}
    <circle cx="350" cy="145" r="28" fill="#F5B82E" stroke="{INK}" stroke-width="3.2"/>
    <text x="350" y="153" text-anchor="middle" font-size="24">2</text>
    <text x="350" y="212" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="16" fill="{INK}">{esc(c['p2'])}</text>
    <text x="350" y="242" text-anchor="middle" font-family="Segoe UI, sans-serif" font-weight="700" font-size="13" fill="#6B5322">{esc(c.get('s2',''))}</text>

    {card_box(460, 105, 175, 210, "#E1F3E6", 18)}
    <circle cx="547" cy="165" r="28" fill="#48A868" stroke="{INK}" stroke-width="3.2"/>
    <text x="547" y="173" text-anchor="middle" font-size="24">3</text>
    <text x="547" y="232" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="16" fill="{INK}">{esc(c['p3'])}</text>
    <text x="547" y="262" text-anchor="middle" font-family="Segoe UI, sans-serif" font-weight="700" font-size="13" fill="#235D3A">{esc(c.get('s3',''))}</text>

    {draw_chibi(730, 295, 0.92, expr=c.get("expr","explain"), hair=c.get("hair","male_neat"), outfit=c.get("outfit","blue_shirt"), pose="point_up")}
    """
    return wrap_svg(860, 460, body)


def arch_bullseye_outcome(c: dict) -> str:
    body = f"""
    {wash_blob(430, 255, 355, 185, "peachWash", 0)}
    <!-- Busy Output Stack on Left -->
    {sticky_note(80, 155, 165, 95, c['p1'], c['p2'], "#E8E4DC", -5)}
    {arrow_curved(260, 205, 325, 175, 385, 195, "#054AA3")}
    <!-- Giant Bullseye Target -->
    <circle cx="485" cy="225" r="108" fill="#E05A47" stroke="{INK}" stroke-width="3.8"/>
    <circle cx="485" cy="225" r="76" fill="#FFFDF7" stroke="{INK}" stroke-width="3.4"/>
    <circle cx="485" cy="225" r="44" fill="#E05A47" stroke="{INK}" stroke-width="3.4"/>
    <circle cx="485" cy="225" r="18" fill="#F7C948" stroke="{INK}" stroke-width="3.2"/>
    <!-- Golden Arrow hitting center -->
    <line x1="365" y1="125" x2="482" y2="222" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
    {badge_tag(390, 355, 195, 42, c['p3'], "#DCF2E4", "#1B6B3A", 16)}
    {draw_chibi(710, 295, 0.94, expr=c.get("expr","smile"), hair=c.get("hair","male_neat"), outfit=c.get("outfit","brown_suit"), pose="point_up")}
    """
    return wrap_svg(860, 460, body)


def arch_staircase_growth(c: dict) -> str:
    body = f"""
    {wash_blob(280, 265, 240, 195, "sageWash", 1)}
    <!-- Ascending Warm Wooden Stairs -->
    <polygon points="45,425 145,425 145,345 255,345 255,265 365,265 365,185 495,185 495,455 45,455" fill="#E5BA73" stroke="{INK}" stroke-width="3.8" stroke-linejoin="round"/>
    {badge_tag(50, 368, 92, 34, c['p1'], "#FFFDF7", INK, 13)}
    {badge_tag(155, 288, 96, 34, c['p2'], "#DCEBFB", "#054AA3", 13)}
    {badge_tag(265, 208, 98, 34, c['p3'], "#DCF2E4", "#1B6B3A", 13)}
    <!-- Trophy / Star at Top -->
    <polygon points="435,95 447,125 480,125 453,144 463,175 435,156 407,175 417,144 390,125 423,125" fill="#F7C948" stroke="{INK}" stroke-width="3.2"/>
    {draw_chibi(210, 195, 0.82, expr=c.get("expr","smile"), hair=c.get("hair","male_neat"), outfit=c.get("outfit","blue_shirt"), hat=c.get("hat",""), pose="point_up")}
    """
    return wrap_svg(560, 500, body)


def arch_battery_energy(c: dict) -> str:
    body = f"""
    {wash_blob(280, 265, 240, 195, "peachWash", 2)}
    <!-- Big Battery Icon -->
    <rect x="65" y="135" width="165" height="92" rx="16" fill="#FFFDF7" stroke="{INK}" stroke-width="4"/>
    <rect x="230" y="162" width="14" height="38" rx="5" fill="{INK}"/>
    <rect x="77" y="147" width="{c.get('charge_w', 42)}" height="68" rx="10" fill="{c.get('charge_c', '#E05A47')}"/>
    <text x="147" y="190" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="22" fill="{INK}">{esc(c['p1'])}</text>
    {speech_bubble(55, 260, 205, 75, [c['p2'], c.get('p3','')], "#FFF6D6", INK, "right", 15)}
    {draw_chibi(395, 315, 0.96, expr=c.get("expr","cry"), hair=c.get("hair","male_wavy"), outfit=c.get("outfit","grey_blazer"), pose=c.get("pose","hands_head"))}
    """
    return wrap_svg(560, 500, body)


def arch_scooter_delivery(c: dict) -> str:
    body = f"""
    {wash_blob(430, 255, 360, 185, "sageWash", 0)}
    <!-- Route Map Curve -->
    <path d="M 95,355 Q 260,185 450,295 T 765,175" fill="none" stroke="#3B82F6" stroke-width="7" stroke-dasharray="14 8" stroke-linecap="round"/>
    <circle cx="95" cy="355" r="14" fill="#E05A47" stroke="{INK}" stroke-width="3.4"/>
    <circle cx="450" cy="295" r="14" fill="#F5B82E" stroke="{INK}" stroke-width="3.4"/>
    <circle cx="765" cy="175" r="16" fill="#2D8A56" stroke="{INK}" stroke-width="3.4"/>
    {badge_tag(65, 275, 165, 40, c['p1'], "#FFFDF7", INK, 15)}
    {badge_tag(575, 98, 195, 42, c['p2'], "#DCF2E4", "#1B6B3A", 15)}
    <!-- Cute Delivery Parcel Box + Chibi -->
    {card_box(275, 105, 165, 88, "#F5CBA7", 12)}
    <text x="357" y="156" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="16" fill="{INK}">{esc(c['p3'])}</text>
    {draw_chibi(525, 305, 0.92, expr="smile", hair="male_neat", outfit="builder_vest", hat="helmet", pose="point_up")}
    """
    return wrap_svg(860, 460, body)


def arch_pipeline_castles(c: dict) -> str:
    body = f"""
    {wash_blob(430, 255, 360, 185, "skyWash", 1)}
    <!-- System A -->
    {card_box(75, 135, 175, 175, "#DCEBFB", 16)}
    <text x="162" y="195" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="18" fill="#054AA3">{esc(c['p1'])}</text>
    <rect x="105" y="220" width="115" height="55" rx="8" fill="#FFFDF7" stroke="{INK}" stroke-width="2.8"/>
    <!-- Resilient Pipe -->
    <rect x="250" y="202" width="245" height="36" fill="#F5C451" stroke="{INK}" stroke-width="3.6"/>
    {badge_tag(285, 128, 175, 42, c['p2'], "#DCF2E4", "#1B6B3A", 15)}
    {badge_tag(285, 268, 175, 42, c['p3'], "#FFF4C7", INK, 15)}
    <!-- System B -->
    {card_box(495, 135, 175, 175, "#E1F3E6", 16)}
    <text x="582" y="195" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="18" fill="#1B6B3A">{esc(c.get('p4','System B'))}</text>
    <rect x="525" y="220" width="115" height="55" rx="8" fill="#FFFDF7" stroke="{INK}" stroke-width="2.8"/>
    {draw_chibi(755, 295, 0.88, expr="smile", hair="male_neat", outfit="blue_shirt", pose="point_up")}
    """
    return wrap_svg(860, 460, body)


def arch_three_pillars(c: dict) -> str:
    body = f"""
    {wash_blob(430, 250, 365, 190, "sandWash", 2)}
    <!-- Temple Roof & Base -->
    <polygon points="85,125 345,48 605,125" fill="#F3D186" stroke="{INK}" stroke-width="3.8" stroke-linejoin="round"/>
    <rect x="95" y="125" width="500" height="22" rx="6" fill="#E5BA68" stroke="{INK}" stroke-width="3.4"/>
    <rect x="85" y="365" width="520" height="28" rx="8" fill="#D9B37C" stroke="{INK}" stroke-width="3.6"/>
    <!-- 3 Pillars -->
    <rect x="135" y="147" width="95" height="218" fill="#FFFDF7" stroke="{INK}" stroke-width="3.4"/>
    <text x="182" y="262" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="16" fill="#054AA3">{esc(c['p1'])}</text>
    <rect x="297" y="147" width="95" height="218" fill="#FFFDF7" stroke="{INK}" stroke-width="3.4"/>
    <text x="344" y="262" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="16" fill="#1B6B3A">{esc(c['p2'])}</text>
    <rect x="460" y="147" width="95" height="218" fill="#FFFDF7" stroke="{INK}" stroke-width="3.4"/>
    <text x="507" y="262" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="16" fill="#A33B1C">{esc(c['p3'])}</text>
    {draw_chibi(715, 295, 0.96, expr=c.get("expr","zen"), hair="senior_mentor", outfit="brown_suit", hat=c.get("hat",""), pose="point_up")}
    """
    return wrap_svg(860, 460, body)


def arch_laptop_bubbles(c: dict) -> str:
    body = f"""
    {wash_blob(280, 265, 240, 195, "skyWash", 0)}
    {speech_bubble(28, 72, 205, 66, [c['p1']], "#FAD8CE", "#9E2424", "down", 15)}
    {speech_bubble(315, 65, 215, 66, [c['p2']], "#FFF4C7", INK, "down", 15)}
    {speech_bubble(35, 175, 185, 62, [c['p3']], "#DCEBFB", "#054AA3", "right", 15)}
    {draw_chibi(335, 285, 0.94, expr=c.get("expr","sweat"), hair=c.get("hair","male_neat"), outfit=c.get("outfit","blue_shirt"), pose=c.get("pose","normal"))}
    {laptop_prop(265, 425, 0.95, c.get("lap","BA"))}
    """
    return wrap_svg(560, 500, body)


def arch_quadrant_wheel(c: dict) -> str:
    body = f"""
    {wash_blob(430, 255, 360, 185, "sageWash", 1)}
    <!-- 2x2 Strategic Canvas / Wheel -->
    {card_box(95, 78, 215, 145, "#DCEBFB", 14)}
    <text x="202" y="158" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="18" fill="#054AA3">{esc(c['p1'])}</text>
    {card_box(325, 78, 215, 145, "#DCF2E4", 14)}
    <text x="432" y="158" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="18" fill="#1B6B3A">{esc(c['p2'])}</text>
    {card_box(95, 238, 215, 145, "#FFF4C7", 14)}
    <text x="202" y="318" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="18" fill="#8C5418">{esc(c['p3'])}</text>
    {card_box(325, 238, 215, 145, "#FDE5D8", 14)}
    <text x="432" y="318" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="18" fill="#9E2A2A">{esc(c['p4'])}</text>
    <circle cx="317" cy="230" r="28" fill="#F7C948" stroke="{INK}" stroke-width="3.6"/>
    <text x="317" y="236" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="900" font-size="15" fill="{INK}">{esc(c.get('center','BA'))}</text>
    {draw_chibi(695, 295, 0.96, expr=c.get("expr","explain"), hair=c.get("hair","senior_mentor"), outfit=c.get("outfit","brown_suit"), pose="point_up")}
    """
    return wrap_svg(860, 460, body)


def arch_moscow_funnel(c: dict) -> str:
    body = f"""
    {wash_blob(280, 265, 240, 200, "sandWash", 0)}
    {sticky_note(38, 52, 130, 58, c['p1'], "", "#FAD8CE", -10)}
    {sticky_note(188, 42, 135, 58, c['p2'], "", "#FFE699", 8)}
    <!-- Golden MoSCoW Filter Funnel -->
    <polygon points="75,135 285,135 215,245 145,245" fill="#F5C451" stroke="{INK}" stroke-width="3.8" stroke-linejoin="round"/>
    <rect x="145" y="245" width="70" height="42" rx="6" fill="#E59A38" stroke="{INK}" stroke-width="3.4"/>
    <text x="180" y="188" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="900" font-size="18" fill="{INK}">MoSCoW</text>
    {badge_tag(75, 310, 210, 42, c['p3'], "#DCF2E4", "#1B6B3A", 15)}
    {draw_chibi(415, 315, 0.96, expr="smile", hair="male_neat", outfit="blue_shirt", pose="point_up")}
    """
    return wrap_svg(560, 500, body)


def arch_fortress_gate_logic(c: dict) -> str:
    body = f"""
    {wash_blob(430, 255, 360, 185, "sageWash", 2)}
    <!-- Warm Stone Fortress Wall blocking bugs -->
    <path d="M 95,380 L 95,145 L 135,145 L 135,175 L 185,175 L 185,145 L 235,145 L 235,175 L 285,175 L 285,145 L 335,145 L 335,380 Z" fill="#E2C499" stroke="{INK}" stroke-width="3.8" stroke-linejoin="round"/>
    <path d="M 165,380 L 165,265 C 165,225 265,225 265,265 L 265,380 Z" fill="#7D5338" stroke="{INK}" stroke-width="3.6"/>
    {badge_tag(365, 118, 205, 42, c['p1'], "#DCEBFB", "#054AA3", 15)}
    {badge_tag(385, 182, 205, 42, c['p2'], "#FFF4C7", INK, 15)}
    {badge_tag(365, 246, 205, 42, c['p3'], "#DCF2E4", "#1B6B3A", 15)}
    {draw_chibi(695, 295, 0.96, expr="detective", hair="male_neat", outfit="brown_suit", pose="point_up")}
    """
    return wrap_svg(860, 460, body)


def arch_kpi_gauge_ruler(c: dict) -> str:
    body = f"""
    {wash_blob(280, 265, 240, 195, "skyWash", 1)}
    <!-- Big Semi-circle KPI Meter -->
    <path d="M 55,265 A 135,135 0 0,1 325,265 Z" fill="#FFFDF7" stroke="{INK}" stroke-width="4"/>
    <path d="M 78,265 A 112,112 0 0,1 190,153 L 190,265 Z" fill="#FAD8CE"/>
    <path d="M 190,153 A 112,112 0 0,1 302,265 L 190,265 Z" fill="#9AE0B0"/>
    <line x1="190" y1="265" x2="265" y2="178" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
    <circle cx="190" cy="265" r="12" fill="#F5B82E" stroke="{INK}" stroke-width="3.4"/>
    {badge_tag(65, 85, 245, 42, c['p1'], "#DCEBFB", "#054AA3", 15)}
    {badge_tag(65, 295, 245, 42, c['p2'], "#DCF2E4", "#1B6B3A", 15)}
    {draw_chibi(420, 315, 0.94, expr="smile", hair="female_bob", outfit="sage_vest", pose="point_up")}
    """
    return wrap_svg(560, 500, body)


def arch_ui_handoff_trap(c: dict) -> str:
    body = f"""
    {wash_blob(430, 255, 360, 185, "peachWash", 0)}
    <!-- Pretty UI Wireframe on Left with broken gears inside -->
    {card_box(85, 88, 255, 255, "#FFFDF7", 18)}
    <rect x="85" y="88" width="255" height="42" rx="14" fill="#8CC5F2" stroke="{INK}" stroke-width="3.2"/>
    <circle cx="112" cy="109" r="6" fill="#E05A47"/>
    <circle cx="132" cy="109" r="6" fill="#F5B82E"/>
    <rect x="112" y="152" width="200" height="42" rx="8" fill="#E8F2FC" stroke="{INK}" stroke-width="2.6"/>
    <text x="212" y="179" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="15" fill="#054AA3">{esc(c['p1'])}</text>
    {badge_tag(112, 215, 200, 40, c['p2'], "#FAD8CE", "#9E2424", 14)}
    {badge_tag(112, 270, 200, 40, c['p3'], "#FFF4C7", "#8C5418", 14)}
    {speech_bubble(375, 68, 245, 72, ["Check lại hộ anh nhé!"], "#FAD8CE", "#9E2424", "down", 16)}
    {draw_chibi(665, 295, 0.96, expr="shock", hair="male_neat", outfit="orange_cardigan", pose="hands_head")}
    """
    return wrap_svg(860, 460, body)


def arch_nodding_question_bomb(c: dict) -> str:
    body = f"""
    {wash_blob(280, 265, 240, 195, "peachWash", 2)}
    <!-- Thought Cloud full of ??? -->
    <ellipse cx="195" cy="145" rx="135" ry="78" fill="#FFFDF7" stroke="{INK}" stroke-width="3.6"/>
    <circle cx="285" cy="228" r="14" fill="#FFFDF7" stroke="{INK}" stroke-width="3.2"/>
    <circle cx="318" cy="258" r="8" fill="#FFFDF7" stroke="{INK}" stroke-width="3"/>
    <text x="195" y="138" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="900" font-size="28" fill="#E05A47">? ? ?</text>
    <text x="195" y="175" text-anchor="middle" font-family="Segoe UI, sans-serif" font-weight="800" font-size="16" fill="{INK}">{esc(c['p1'])}</text>
    {speech_bubble(55, 275, 195, 64, [c['p2']], "#DCF2E4", "#1B6B3A", "right", 16)}
    {draw_chibi(395, 320, 0.96, expr="sweat", hair="male_wavy", outfit="blue_shirt", pose="shrug")}
    """
    return wrap_svg(560, 500, body)


def arch_entity_erd_board(c: dict) -> str:
    body = f"""
    {wash_blob(430, 255, 365, 185, "skyWash", 1)}
    <!-- 3 Connected Data Object Boxes -->
    {card_box(75, 95, 185, 115, "#DCEBFB", 14)}
    <text x="167" y="138" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="17" fill="#054AA3">{esc(c['p1'])}</text>
    <text x="167" y="172" text-anchor="middle" font-family="Segoe UI, sans-serif" font-weight="700" font-size="14" fill="{INK}">ID · Trạng thái</text>

    {card_box(335, 95, 185, 115, "#FFF4C7", 14)}
    <text x="427" y="138" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="17" fill="#8C5418">{esc(c['p2'])}</text>
    <text x="427" y="172" text-anchor="middle" font-family="Segoe UI, sans-serif" font-weight="700" font-size="14" fill="{INK}">Quan hệ 1 — N</text>

    {card_box(205, 265, 195, 115, "#DCF2E4", 14)}
    <text x="302" y="308" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="800" font-size="17" fill="#1B6B3A">{esc(c['p3'])}</text>
    <text x="302" y="342" text-anchor="middle" font-family="Segoe UI, sans-serif" font-weight="700" font-size="14" fill="{INK}">Vòng đời dữ liệu</text>

    <line x1="260" y1="152" x2="335" y2="152" stroke="{INK}" stroke-width="4"/>
    <line x1="185" y1="210" x2="255" y2="265" stroke="{INK}" stroke-width="4"/>
    <line x1="410" y1="210" x2="345" y2="265" stroke="{INK}" stroke-width="4"/>
    {draw_chibi(685, 295, 0.96, expr="smile", hair="male_neat", outfit="brown_suit", pose="point_up")}
    """
    return wrap_svg(860, 460, body)


def arch_calendar_clock_overload(c: dict) -> str:
    body = f"""
    {wash_blob(280, 265, 240, 195, "peachWash", 0)}
    <!-- Big Wall Clock showing 6 hours of meetings -->
    <circle cx="175" cy="195" r="105" fill="#FFFDF7" stroke="{INK}" stroke-width="4.2"/>
    <path d="M 175,195 L 175,102 A 93,93 0 1,1 92,238 Z" fill="#F5A99B" opacity="0.82"/>
    <line x1="175" y1="195" x2="175" y2="118" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
    <line x1="175" y1="195" x2="235" y2="225" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
    <circle cx="175" cy="195" r="8" fill="{INK}"/>
    {badge_tag(65, 322, 220, 42, c['p1'], "#FAD8CE", "#9E2424", 15)}
    {badge_tag(295, 78, 215, 42, c['p2'], "#DCEBFB", "#054AA3", 15)}
    {draw_chibi(405, 320, 0.95, expr="cry", hair="female_ponytail", outfit="grey_blazer", pose="hands_head")}
    """
    return wrap_svg(560, 500, body)


def arch_domino_one_field(c: dict) -> str:
    body = f"""
    {wash_blob(430, 255, 365, 185, "sandWash", 1)}
    <!-- Falling Domino Chain from 1 tiny input to 3 big teams -->
    <rect x="92" y="265" width="44" height="105" rx="8" transform="rotate(14 114 317)" fill="#DCEBFB" stroke="{INK}" stroke-width="3.6"/>
    <rect x="195" y="215" width="62" height="155" rx="10" transform="rotate(22 226 292)" fill="#FFE699" stroke="{INK}" stroke-width="3.6"/>
    <rect x="325" y="165" width="78" height="205" rx="12" transform="rotate(30 364 267)" fill="#F7B299" stroke="{INK}" stroke-width="3.8"/>
    <rect x="475" y="125" width="92" height="245" rx="12" transform="rotate(38 521 247)" fill="#E05A47" stroke="{INK}" stroke-width="3.8"/>
    {badge_tag(55, 185, 155, 38, c['p1'], "#FFFDF7", "#054AA3", 14)}
    {badge_tag(295, 78, 255, 42, c['p2'], "#FAD8CE", "#9E2424", 15)}
    {draw_chibi(715, 295, 0.94, expr="shock", hair="male_neat", outfit="blue_shirt", pose="hands_head")}
    """
    return wrap_svg(860, 460, body)


def arch_magnifying_hidden_rule(c: dict) -> str:
    body = f"""
    {wash_blob(280, 265, 240, 195, "sandWash", 2)}
    <!-- Spec Document + Giant Brass Magnifying Glass revealing hidden rule -->
    {card_box(55, 85, 235, 295, "#FFFDF7", 14)}
    <line x1="85" y1="135" x2="255" y2="135" stroke="#CBD5E0" stroke-width="8" stroke-linecap="round"/>
    <line x1="85" y1="168" x2="235" y2="168" stroke="#CBD5E0" stroke-width="8" stroke-linecap="round"/>
    <!-- Magnifying Glass Lens -->
    <circle cx="195" cy="255" r="74" fill="#FFF3B8" stroke="#C98A2C" stroke-width="10"/>
    <circle cx="195" cy="255" r="74" fill="none" stroke="{INK}" stroke-width="3.6"/>
    <line x1="248" y1="308" x2="308" y2="368" stroke="#8C583A" stroke-width="16" stroke-linecap="round"/>
    <text x="195" y="248" text-anchor="middle" font-family="Montserrat, Segoe UI, sans-serif" font-weight="900" font-size="16" fill="#A62828">{esc(c['p1'])}</text>
    <text x="195" y="274" text-anchor="middle" font-family="Segoe UI, sans-serif" font-weight="800" font-size="14" fill="{INK}">{esc(c['p2'])}</text>
    {draw_chibi(420, 315, 0.96, expr="detective", hair="male_neat", outfit="sage_vest", hat="explorer", pose="point_up")}
    """
    return wrap_svg(560, 500, body)


# ==============================================================================
# ALL 81 BESPOKE DAY CONFIGURATIONS (Hand-crafted headlines + distinct scenes)
# ==============================================================================

BESPOKE_DAYS = {
    1:  ("top_center", ["BA nên làm gì sau khi", "tính năng được Release?"], arch_rocket_telemetry, {"p1": "Sau Go-Live", "p2": "Đo KPI", "p3": "Feedback", "expr": "smile", "outfit": "blue_shirt"}),
    2:  ("top_center", ["BA không tư duy hệ thống =", "Người xây nhà không có bản vẽ"], arch_crooked_house, {"p1": "Thiếu bản vẽ!", "p2": "Đập đi xây lại"}),
    3:  ("split_left", ["3 kỹ thuật BABOK", "giúp BA không bị đổ lỗi", "“Tôi chưa nói thế bao giờ”"], arch_shield_defense, {"p1": "Tôi chưa chốt", "p2": "thế bao giờ!", "p3": "BIÊN BẢN CHỐT", "outfit": "brown_suit"}),
    4:  ("split_left", ["3 kỹ thuật BABOK", "xử lý yêu cầu gấp", "mà không vỡ tiến độ"], arch_moscow_funnel, {"p1": "Gấp lắm!", "p2": "Phải có ngay!", "p3": "Ưu tiên đúng Sprint"}),
    5:  ("top_center", ["3 kỹ thuật BABOK giúp BA tư duy lỗi:", "Viết logic chặt chẽ, không lọt Case"], arch_fortress_gate_logic, {"p1": "1. Exception Flow", "p2": "2. Risk Analysis", "p3": "3. Timeout & Retry"}),
    6:  ("top_center", ["Một ngày làm", "BA Manager của tôi"], arch_team_compass, {"p1": "Coaching 1-1", "p2": "Giữ nhịp dự án", "p3": "Gỡ vướng Team", "hair": "senior_mentor", "outfit": "brown_suit"}),
    7:  ("split_right", ["3 kỹ thuật BABOK", "giúp BA đo lường", "hiệu quả tính năng"], arch_kpi_gauge_ruler, {"p1": "Tỷ lệ sử dụng thật", "p2": "Đo giá trị sau Go-Live"}),
    8:  ("split_left", ["Học gì để lên Senior BA?", "Làm đúng và học đúng", "thứ cần học"], arch_staircase_growth, {"p1": "Vững kỹ thuật", "p2": "Tư duy Hệ thống", "p3": "Hiểu Kinh doanh", "expr": "smile", "outfit": "brown_suit"}),
    9:  ("split_right", ["3 kỹ thuật BABOK tránh viết", "Requirement rồi toang", "vì Constraint"], arch_iceberg_depth, {"p1": "Tính năng đẹp", "p2": "Giới hạn hạ tầng", "p3": "Ràng buộc pháp lý", "p4": "Ngân sách & Thời gian", "expr": "detective", "outfit": "sage_vest"}),
    10: ("top_center", ["PO tự vẽ UI/UX rồi bảo BA “check hộ”:", "Trò chơi đổ lỗi bắt đầu?"], arch_ui_handoff_trap, {"p1": "Giao diện lung linh", "p2": "Chưa chốt Business Rule!", "p3": "Thiếu luồng ngoại lệ!"}),
    11: ("split_right", ["Khi BA gật đầu", "vì ngại hỏi lại"], arch_nodding_question_bomb, {"p1": "Ngại hỏi = Mìn nổ chậm", "p2": "Dạ em hiểu rồi ạ..."}),
    12: ("top_center", ["BA có cần biết code không?"], arch_bridge_worlds, {"p1": "TECH / DEV", "p2": "API · SQL · JSON", "p3": "BUSINESS", "p4": "Quy trình · Giá trị", "expr": "smile", "outfit": "blue_shirt"}),
    13: ("top_center", ["Data Object – Bí kíp", "phân tích nghiệp vụ của tôi"], arch_entity_erd_board, {"p1": "Khách hàng", "p2": "Đơn hàng", "p3": "Thanh toán"}),
    14: ("split_left", ["3 dạng comment dễ khiến", "BA rơi vào bẫy", "tưởng đã DONE rồi"], arch_laptop_bubbles, {"p1": "“Cơ bản ok rồi em”", "p2": "“Tạm duyệt UI nhé”", "p3": "Khoan! Chốt biên đã!", "expr": "detective", "outfit": "orange_cardigan"}),
    15: ("top_center", ["BA không biết “gốc”, chỉ chăm chăm “ngọn”", "thì sớm muộn cũng toang"], arch_system_tree_roots, {"p1": "Yêu cầu bề nổi (Ngọn)", "p2": "Bài toán gốc", "p3": "Luồng dữ liệu", "p4": "Quy tắc vận hành", "outfit": "sage_vest"}),
    16: ("split_right", ["Bạn chỉ viết flow cho người dùng?", "Vậy ai viết cho", "thằng... Phá?"], arch_shield_defense, {"p1": "Spam bấm 10 lần!", "p2": "Sửa request ngầm!", "p3": "CHẶN EDGE CASE", "expr": "detective", "outfit": "dark_hoodie"}),
    17: ("top_center", ["Roadmap dài như kỳ vọng,", "nhưng ngắn như sự hiểu khách hàng"], arch_cliff_carpet, {"p1": "ROADMAP 20 Tính năng", "p2": "Khách thực sự", "p3": "cần gì???"}),
    18: ("top_center", ["Buổi Retro cuối Sprint: Không phải để", "bẻ lái tội lỗi, mà để bẻ lái cách làm"], arch_team_compass, {"p1": "Không đổ lỗi", "p2": "Nhìn thẳng quy trình", "p3": "Cải tiến Sprint tới", "hair": "male_neat", "outfit": "blue_shirt"}),
    19: ("split_left", ["Một ngày họp 6 tiếng –", "Còn đâu thời gian", "để phân tích?"], arch_calendar_clock_overload, {"p1": "6 Tiếng họp kín lịch!", "p2": "Giữ khung Deep Work"}),
    20: ("top_center", ["Không xem kỹ hệ thống hiện tại đã có gì", "là viết yêu cầu như chưa từng có hệ thống"], arch_pipeline_castles, {"p1": "Hệ thống AS-IS", "p2": "Khảo sát hiện trạng", "p3": "Tránh đập đi xây lại", "p4": "Luồng TO-BE khớp"}),
    21: ("top_center", ["BA kiêm PM – Tưởng được nâng tầm,", "ai ngờ nâng luôn cục nợ"], arch_balance_scale, {"p1": "Phân tích sâu (BA)", "p2": "Đòi tiến độ & Họp (PM)", "tilt": 14, "expr": "sweat", "outfit": "grey_blazer"}),
    22: ("top_center", ["Tính năng “chỉ thêm 1 dòng thôi mà”", "rồi tốn cả 3 team xử lý"], arch_domino_one_field, {"p1": "Thêm 1 ô Input", "p2": "CRM · Marketing · CSKH rối!"}),
    23: ("top_center", ["Domain-Driven Design (DDD) là gì?", "Và tại sao BA nên biết sớm?"], arch_quadrant_wheel, {"p1": "Bounded Context", "p2": "Ubiquitous Language", "p3": "Core Domain", "p4": "Ranh giới rõ ràng", "center": "DDD", "expr": "smile"}),
    24: ("top_center", ["Khi nội bộ chia bè – BA chỉ còn 2 lựa chọn:", "Dẫn dắt hoặc làm bia đỡ đạn"], arch_debate_table, {"p1": "Phòng A đòi kiểu này!", "p2": "Mục tiêu chung", "p3": "Số liệu khách quan", "p4": "Phòng B đòi kiểu kia!"}),
    25: ("split_right", ["Hidden Requirement:", "Khi “quy tắc ngầm”", "làm hệ thống lệch hướng"], arch_magnifying_hidden_rule, {"p1": "QUY TẮC NGẦM!", "p2": "Ai cũng ngầm hiểu trừ BA"}),

    26: ("split_left", ["Đầu tháng, bạn là BA mới toanh", "Chào mừng đến với chiến trường!"], arch_whirlwind_tickets, {"p1": "SRS gấp!", "p2": "Họp khách!", "p3": "CR mới!", "p4": "Dev hỏi!", "hat": "helmet", "expr": "sweat"}),
    27: ("top_center", ["Bạn có đang làm đúng việc", "nhưng vẫn thấy chông chênh?"], arch_balance_scale, {"p1": "Xong 100 Task", "p2": "Định hướng nghề?", "tilt": 10, "expr": "think", "outfit": "sage_vest"}),
    28: ("split_right", ["Elicitation dùng sai kỹ thuật", "là tự đẩy mình vào thế bí"], arch_keyhole_tools, {"p1": "Nhu cầu thật", "p2": "Chọn đúng kỹ thuật", "expr": "detective", "hair": "female_bob"}),
    29: ("top_center", ["Ngụy biện của kẻ lười:", "“Em làm theo yêu cầu mà”"], arch_square_wheel_cart, {"p1": "Tính năng vô dụng", "p2": "(Đúng y lời khách dặn)", "p3": "Em làm đúng yêu cầu mà!", "expr": "sweat"}),
    30: ("top_center", ["Cách tôi xử lý CR đổi logic giữa đường", "mà vẫn kịp deadline"], arch_railway_switch, {"p1": "Kịp Go-Live Phase 1", "p2": "Vỡ tiến độ", "p3": "Đánh giá Impact", "p4": "Tách Scope khéo"}),
    31: ("top_center", ["“Em đang cãi anh à?”", "Bài học nhớ đời về tư duy phản biện"], arch_debate_table, {"p1": "Em đang cãi anh à?!", "p2": "Option A vs B", "p3": "Rủi ro & Số liệu", "p4": "Em bảo vệ dự án!"}),
    32: ("split_left", ["Dấu hiệu nhận biết", "dự án sắp toang", "từ góc nhìn BA"], arch_iceberg_depth, {"p1": "Báo cáo Xanh", "p2": "Scope nở ngầm", "p3": "Họp im lặng", "p4": "UAT dời lịch", "expr": "shock"}),
    33: ("split_right", ["Feedback không giết bạn,", "phản ứng dở mới giết bạn"], arch_shield_defense, {"p1": "Tài liệu chỗ này", "p2": "chưa ổn em nhé!", "p3": "CẦU THỊ & SỬA", "expr": "smile", "outfit": "sage_vest"}),
    34: ("top_center", ["Tôi đang nối liền...", "Hay đang chia rẽ dự án?"], arch_bridge_worlds, {"p1": "STAKEHOLDER", "p2": "Kỳ vọng kinh doanh", "p3": "TECH TEAM", "p4": "Kiến trúc kỹ thuật", "expr": "think", "outfit": "orange_cardigan"}),
    35: ("top_center", ["Tư duy hệ thống:", "Nền móng sống còn của BA thực thụ"], arch_system_tree_roots, {"p1": "Giao diện UI", "p2": "Data Flow", "p3": "Integration", "p4": "State & Rule"}),
    36: ("top_center", ["BA và DEV:", "Đồng minh hay đối đầu?"], arch_fistbump_alliance, {"p1": "ĐỒNG MINH!", "p2": "BA rõ nghiệp vụ", "p3": "DEV vững giải pháp"}),
    37: ("split_left", ["Sai lầm lớn nhất của BA:", "Học kỹ thuật... nhưng quên", "học sự thấu hiểu"], arch_open_book_pop, {"p1": "UML · BPMN", "p2": "SQL · API", "p3": "Nỗi đau thật", "p4": "của User ❤️", "hair": "female_ponytail", "expr": "think"}),
    38: ("split_right", ["Sếp đổi ý xoành xoạch –", "BA cần làm gì?"], arch_whirlwind_tickets, {"p1": "Sáng chốt A", "p2": "Trưa đổi B", "p3": "Chiều quay C", "p4": "Decision Log!", "expr": "sweat", "outfit": "brown_suit", "hat": ""}),
    39: ("split_left", ["Task dần biến khỏi tay bạn", "không vì bạn dở, mà vì", "người ta hết dám tin"], arch_battery_energy, {"p1": "Niềm tin 15%", "p2": "Trễ hẹn nhỏ,", "p3": "mất uy tín lớn", "charge_w": 36, "charge_c": "#E05A47", "expr": "sad", "pose": "shrug"}),
    40: ("split_right", ["5 câu hỏi sống còn", "trước khi phân tích", "bất kỳ hệ thống nào"], arch_keyhole_tools, {"p1": "5 Câu hỏi gốc", "p2": "Why · Who · Impact", "expr": "smile", "hair": "male_neat", "outfit": "blue_shirt"}),

    41: ("top_center", ["Làm BA hệ tích hợp:", "Thiết kế để không ai phải hỏi", "“Nếu lỗi thì sao?”"], arch_pipeline_castles, {"p1": "Core System", "p2": "Retry & Queue", "p3": "Đối soát & Log", "p4": "Partner API"}),
    42: ("top_center", ["Gỡ xung đột khi DEV từ chối", "implement logic BA phân tích"], arch_debate_table, {"p1": "Logic này không làm!", "p2": "Trade-off Matrix", "p3": "Chi phí vs Giá trị", "p4": "Cùng tìm phương án!"}),
    43: ("top_center", ["Tư duy Business Goals:", "Requirement không tự nhiên sinh ra"], arch_bullseye_outcome, {"p1": "Tính năng rời rạc", "p2": "Làm cho có", "p3": "Mục tiêu Kinh doanh"}),
    44: ("top_center", ["Ở một công ty nọ –", "Người BA mang chữ C trên ngực áo"], arch_team_compass, {"p1": "Clarity (Rõ ràng)", "p2": "Connector (Kết nối)", "p3": "Courage (Bản lĩnh)", "hair": "male_neat", "outfit": "blue_shirt"}),
    45: ("top_center", ["Bị ném vào giữa dự án hỗn loạn:", "Đây là cách để không lạc hướng"], arch_flashlight_fog, {"p1": "1. Nắm bài toán gốc", "p2": "2. Vẽ lại luồng chính", "p3": "3. Khoanh vùng rủi ro", "hat": "explorer"}),
    46: ("split_left", ["Sếp quá kỹ tính:", "Làm sao không bị cuốn theo", "từng comment vụn?"], arch_laptop_bubbles, {"p1": "Sửa màu nút đi!", "p2": "Lệch 2 pixel kìa!", "p3": "Chốt luồng lớn trước!", "expr": "detective", "outfit": "grey_blazer"}),
    47: ("top_center", ["Branch, Merge, Pull Request, Tag...", "Giải thích Git dễ hiểu cho BA"], arch_git_whiteboard, {"p1": "GIT DÀNH CHO BA", "p2": "main", "p3": "feature-branch", "p4": "Pull Request"}),
    48: ("top_center", ["Tester hỏi lại yêu cầu “rõ ràng rồi”:", "BA nên phản ứng ra sao?"], arch_fistbump_alliance, {"p1": "CÙNG BẮT LỖI SỚM", "p2": "BA làm rõ biên", "p3": "QA soi góc khuất", "hat2": ""}),
    49: ("top_center", ["Kẹt giữa rừng xà nu kế toán:", "BA có nên đi học kế toán không?"], arch_balance_scale, {"p1": "NỢ (Debit)", "p2": "CÓ (Credit)", "tilt": 0, "expr": "detective", "outfit": "brown_suit"}),
    50: ("split_right", ["Review sách hay cho BA:", "“UX for Beginners”"], arch_open_book_pop, {"p1": "UX thực chiến", "p2": "Hành vi User", "p3": "Đơn giản hóa", "p4": "trải nghiệm", "hair": "male_neat", "outfit": "orange_cardigan"}),

    51: ("top_center", ["Tính năng “làm tạm thôi”", "nhưng sống dai, chết đau"], arch_square_wheel_cart, {"p1": "Giải pháp “Tạm thời”", "p2": "Tồn tại suốt 4 năm!", "p3": "Phải ghi dấu vết & hạn gỡ!", "expr": "shock"}),
    52: ("top_center", ["Làm SaaS mà khách nào cũng đòi", "“Làm theo cách nhà anh”?"], arch_bridge_worlds, {"p1": "SAAS CORE", "p2": "Chuẩn hóa · Cấu hình", "p3": "KHÁCH RIÊNG", "p4": "Đòi sửa luồng gốc!", "expr": "sweat", "outfit": "grey_blazer"}),
    53: ("top_center", ["Nếu cứ hỏi “Tính năng này cần không?”", "Thì mẹ bạn cũng sẽ gật đầu!"], arch_debate_table, {"p1": "Cái gì anh cũng cần!", "p2": "Ngân sách có hạn", "p3": "Chọn 1 bỏ 2", "p4": "Anh đánh đổi gì?"}),
    54: ("top_center", ["Làm quản lý không phải làm sếp,", "mà là đổi góc nhìn"], arch_team_compass, {"p1": "Trao quyền", "p2": "Nhìn toàn cục", "p3": "Xây đội ngũ", "hair": "senior_mentor", "outfit": "sage_vest"}),
    55: ("split_left", ["“Deadline gấp lắm!”", "Nhưng chưa chắc", "đã cần BA làm ẩu"], arch_laptop_bubbles, {"p1": "Gấp lắm em ơi!", "p2": "Mai code luôn nhé!", "p3": "Khoan! Gốc ở đâu?", "expr": "detective", "outfit": "brown_suit"}),
    56: ("split_right", ["“Sếp ơi, em mệt rồi...”"], arch_battery_energy, {"p1": "Pin còn 8%", "p2": "Quá tải kỳ vọng,", "p3": "cần được lắng nghe", "charge_w": 24, "charge_c": "#E05A47", "expr": "cry", "pose": "hands_head"}),
    57: ("split_left", ["Phỏng vấn BA Mid & Senior:", "Đừng chỉ kể bạn làm gì,", "hãy chứng minh độ sâu tư duy"], arch_iceberg_depth, {"p1": "Kể tên dự án", "p2": "Vì sao chọn PA đó?", "p3": "Đánh đổi gì?", "p4": "Tác động hệ thống", "expr": "smile", "outfit": "brown_suit"}),
    58: ("split_right", ["Cách xây dựng khung năng lực", "và đánh giá Level team BA"], arch_staircase_growth, {"p1": "Junior", "p2": "Middle", "p3": "Senior / Lead", "expr": "smile", "outfit": "brown_suit"}),
    59: ("split_left", ["Dành thời gian một mình", "để suy nghĩ sâu,", "không phải để né team"], arch_open_book_pop, {"p1": "Deep Work", "p2": "Tắt nhiễu", "p3": "Nối các mảnh", "p4": "nghiệp vụ khó", "expr": "zen", "hair": "male_neat", "outfit": "sage_vest"}),
    60: ("split_right", ["Estimate task cho BA:", "Không đếm số màn hình,", "mà đo độ xoắn tư duy"], arch_iceberg_depth, {"p1": "Chỉ 2 màn hình", "p2": "18 Business Rules", "p3": "5 Hệ thống tích hợp", "p4": "Xử lý bất đồng bộ", "expr": "think", "outfit": "blue_shirt"}),

    61: ("top_center", ["Sao hôm qua đi chỉ 50k,", "mà hôm nay lại 65k?"], arch_balance_scale, {"p1": "Cầu tăng vọt (Mưa)", "p2": "Cung thiếu tài xế", "tilt": -12, "expr": "explain", "outfit": "orange_cardigan"}),
    62: ("top_center", ["Khi dự án chỉ có Deadline", "và 1 câu nói mơ hồ: BA làm gì đầu tiên?"], arch_flashlight_fog, {"p1": "Chốt mục tiêu cốt lõi", "p2": "Khoanh MVP khả thi", "p3": "Nêu giả định & rủi ro", "hat": ""}),
    63: ("top_center", ["Làm sản phẩm...", "nhưng không ai được quyền quyết định"], arch_quadrant_wheel, {"p1": "Hỏi anh A?", "p2": "Chờ chị B?", "p3": "Đợi sếp C?", "p4": "Cần chốt RACI!", "center": "AI?", "expr": "sweat"}),
    64: ("top_center", ["Cây KPI: Giao thế nào", "cho đúng và hiệu quả?"], arch_system_tree_roots, {"p1": "North Star KPI", "p2": "Tỷ lệ chuyển đổi", "p3": "Tần suất dùng", "p4": "Giảm lỗi vận hành", "outfit": "brown_suit"}),
    65: ("split_left", ["Chuyên mục", "“Anh ơi...” nơi công sở"], arch_laptop_bubbles, {"p1": "Anh ơi flow này...", "p2": "Anh ơi API đâu?", "p3": "Anh ơi khách hỏi!", "expr": "sweat", "outfit": "blue_shirt"}),
    66: ("top_center", ["BA chọn công ty Startup:", "Hãy nhìn như một nhà đầu tư"], arch_three_specimens, {"p1": "Mô hình kiếm tiền", "s1": "Tiền từ đâu ra?", "p2": "Bài toán thực tế", "s2": "Khách có trả phí?", "p3": "Đội ngũ sáng lập", "s3": "Thực thi tới cùng", "expr": "detective", "outfit": "brown_suit"}),
    67: ("top_center", ["Áp dụng CI/CD: BA không viết code", "nhưng vẫn có thể gây lỗi Production!"], arch_pipeline_castles, {"p1": "Spec thiếu biên", "p2": "Feature Flag", "p3": "Backward Compat", "p4": "Production!"}),
    68: ("split_right", ["Scope đã note rõ", "mà vẫn ăn bug oan –", "Vì khách không đọc hay vì ta?"], arch_shield_defense, {"p1": "Ủa tưởng có luôn", "p2": "tính năng này?!", "p3": "OUT-OF-SCOPE RÕ", "expr": "think", "outfit": "orange_cardigan"}),
    69: ("split_left", ["Khi người dùng chỉ thao tác", "bằng một tay – Bài học", "Design Thinking cho BA"], arch_mobile_thumb, {"p1": "Khó với tới", "p2": "Vùng ngón cái ✓", "hair": "female_bob", "outfit": "orange_cardigan"}),
    70: ("top_center", ["Đào lại lỗi cũ –", "Đúc ra chuẩn mới cho team BA"], arch_three_specimens, {"p1": "Mổ xẻ sự cố cũ", "s1": "Không đổ lỗi", "p2": "Tìm lỗ hổng quy trình", "s2": "Vì sao lọt lỗi?", "p3": "Chuẩn hóa Checklist", "s3": "Cả team mạnh lên", "expr": "smile"}),

    71: ("split_right", ["Họ vẫn đi họp, vẫn nhận task,", "nhưng tâm trí đã rời đi từ lâu"], arch_battery_energy, {"p1": "Mất lửa 0%", "p2": "Im lặng gật đầu,", "p3": "ngừng phản biện", "charge_w": 12, "charge_c": "#94A3B8", "expr": "zen", "pose": "normal"}),
    72: ("top_center", ["BA Toolkit – Collaborative Game:", "Speed Boat khơi thông dự án"], arch_speedboat_game, {"p1": "Gió đẩy dự án", "p2": "Mỏ neo kìm hãm"}),
    73: ("split_left", ["Một runner giỏi không tăng tốc sớm", "mà giữ nhịp bền bỉ đến phút cuối"], arch_staircase_growth, {"p1": "Giữ sức", "p2": "Đều nhịp", "p3": "Về đích bền", "expr": "zen", "outfit": "sage_vest"}),
    74: ("top_center", ["Bạn viết tài liệu nhưng người khác điều phối,", "còn DEV thì không thèm đọc"], arch_git_whiteboard, {"p1": "TRỰC QUAN HÓA LUỒNG", "p2": "Bỏ văn sớ dài", "p3": "Vẽ sơ đồ rõ", "p4": "Chủ động dẫn dắt", "expr": "explain", "outfit": "blue_shirt"}),
    75: ("split_right", ["Viết tài liệu rất rõ ràng,", "nhưng sao vẫn bị sếp chê thiếu?"], arch_keyhole_tools, {"p1": "Thiếu chữ WHY!", "p2": "Tác động Kinh doanh", "expr": "think", "hair": "female_ponytail", "outfit": "grey_blazer"}),
    76: ("top_center", ["Các thông số Non-Functional", "mà BA thực chiến phải nắm"], arch_quadrant_wheel, {"p1": "Latency (Tốc độ)", "p2": "TPS (Chịu tải)", "p3": "Availability 99.9%", "p4": "Security & PII", "center": "NFR", "expr": "detective"}),
    77: ("split_left", ["Làm BA cho Mobile App:", "Đừng tưởng giống Web là đủ!"], arch_mobile_thumb, {"p1": "Mất mạng · Push", "p2": "App Store · OS", "hair": "male_neat", "outfit": "blue_shirt"}),
    78: ("top_center", ["Câu chuyện một buổi Offboarding", "và bài học quản trị ngoài Handbook"], arch_team_compass, {"p1": "Tôn trọng", "p2": "Lắng nghe thật lòng", "p3": "Bàn giao tử tế", "hair": "senior_mentor", "outfit": "sage_vest"}),
    79: ("top_center", ["Vì sao cần hiểu Business Model Canvas", "trước khi viết bất kỳ flow nào?"], arch_quadrant_wheel, {"p1": "Giá trị cốt lõi", "p2": "Phân khúc khách", "p3": "Dòng doanh thu", "p4": "Cấu trúc chi phí", "center": "BMC", "expr": "smile"}),
    80: ("top_center", ["Phân biệt 3 loại lỗi trong dự án", "để DEV, QA và User không trách nhầm"], arch_three_specimens, {"p1": "Bug kỹ thuật", "s1": "Code sai đặc tả", "p2": "Hổng nghiệp vụ", "s2": "BA thiếu kịch bản", "p3": "Lệch kỳ vọng UX", "s3": "Khó thao tác thật", "expr": "explain"}),

    81: ("top_center", ["Sprint vẫn trễ dù đã Agile Scrum:", "Kế hoạch sai hay sống sai với Agile?"], arch_square_wheel_cart, {"p1": "Vỏ Agile, Ruột Thác Nước", "p2": "Nhồi việc · Ngại cắt Scope", "p3": "Sao Sprint nào cũng trễ?!", "expr": "sweat"}),
    82: ("top_center", ["“Nối cuốc” – Tính năng nhỏ, hiệu quả lớn", "trong bài toán tối ưu Ride-Hailing"], arch_scooter_delivery, {"p1": "Trả khách điểm A", "p2": "Đón ngay điểm B", "p3": "Giảm xe chạy rỗng"}),
    83: ("top_center", ["Làm BA trong “Tây Du Ký Corp”:", "Không chỉ phân tích, mà còn đọc vị lòng người"], arch_quadrant_wheel, {"p1": "Người quyết liệt", "p2": "Người cầu toàn", "p3": "Người ngại đổi thay", "p4": "Người giữ tầm nhìn", "center": "ĐỌC VỊ", "expr": "smile"}),
    84: ("top_center", ["Khách hàng đột ngột đổi người đại diện:", "BA xử lý bàn giao thế nào?"], arch_bridge_worlds, {"p1": "ĐẠI DIỆN CŨ", "p2": "Lịch sử quyết định", "p3": "ĐẠI DIỆN MỚI", "p4": "Onboarding & Baseline", "expr": "smile", "outfit": "brown_suit"}),
    85: ("top_center", ["Ranh giới của BA: Không rõ thì dễ toang,", "mà rõ quá lại bị nói... chảnh"], arch_balance_scale, {"p1": "Ôm hết việc người", "p2": "Hỗ trợ đúng vai", "tilt": 0, "expr": "smile", "outfit": "sage_vest"}),
    86: ("top_center", ["Reverse-Engineer: Kỹ năng sống còn", "khi BA bước vào hệ thống cũ"], arch_flashlight_fog, {"p1": "Đọc DB & API Log", "p2": "Dựng lại luồng sống", "p3": "Kiểm chứng với User", "hat": "explorer"}),
    87: ("top_center", ["Góp ý mà không làm người khác nản lòng:", "Nghệ thuật quản trị ít ai dạy bạn"], arch_fistbump_alliance, {"p1": "GÓP Ý XÂY DỰNG", "p2": "Nói vào công việc", "p3": "Giữ trọn tự trọng", "hat2": ""}),
    88: ("top_center", ["Trong team có người “nói nhiều hơn làm”:", "Xử lý thế nào cho ra chất quản lý?"], arch_debate_table, {"p1": "Để em lo hết cho!", "p2": "Đo bằng Output", "p3": "Mốc kiểm tra rõ", "p4": "Chốt kết quả cụ thể nhé"}),
    89: ("top_center", ["Mad Unicorn – Khởi nghiệp giao hàng", "& những câu hỏi BA không thể trốn"], arch_scooter_delivery, {"p1": "Định giá & Tuyến", "p2": "Đối soát COD chuẩn", "p3": "Vận hành thực chiến"}),
    90: ("top_center", ["P.O.L.C dành cho BA Lead"], arch_quadrant_wheel, {"p1": "Planning", "p2": "Organizing", "p3": "Leading", "p4": "Controlling", "center": "P.O.L.C", "expr": "smile"}),

    91: ("top_center", ["Ngôn ngữ khách hàng:", "Thứ tiếng BA buộc phải hiểu như bản xứ"], arch_bridge_worlds, {"p1": "LỜI KHÁCH NÓI", "p2": "“Làm nút thông minh”", "p3": "NGÔN NGỮ HỆ THỐNG", "p4": "Rule · Data · Trigger", "expr": "explain", "outfit": "orange_cardigan"}),
    92: ("top_center", ["Câu chuyện Tái Ông Thất Mã", "và triết lý điềm tĩnh trong nghề BA"], arch_balance_scale, {"p1": "Sự cố bất ngờ", "p2": "Bài học nâng tầm", "tilt": 0, "expr": "zen", "outfit": "sage_vest"}),
    93: ("split_right", ["Top 5 lỗi mà Senior BA", "và BA Lead thường mắc phải"], arch_whirlwind_tickets, {"p1": "Ôm việc!", "p2": "Chủ quan!", "p3": "Xa rời Biz!", "p4": "Áp đặt team!", "hat": "crown", "expr": "sweat", "outfit": "brown_suit"}),
    94: ("top_center", ["Ký hợp đồng chốt khung,", "phân tích chi tiết thì Scope nở bung"], arch_railway_switch, {"p1": "Giữ khung + CR có phí", "p2": "Lỗ nặng dự án", "p3": "Hợp đồng khung", "p4": "Quản trị thay đổi"}),
    95: ("top_center", ["Vùng xám trong khảo sát yêu cầu –", "Cái bẫy âm thầm giết chết dự án"], arch_flashlight_fog, {"p1": "Ai xử lý ngoại lệ?", "p2": "Dữ liệu rỗng thì sao?", "p3": "Quyền hạn tới đâu?", "hat": ""}),
    96: ("top_center", ["Tư duy Fail Fast:", "Cứu dự án ngay từ giai đoạn phân tích"], arch_crooked_house, {"p1": "Test Prototype sớm!", "p2": "Sai trên giấy rẻ gấp 100x"}),
    97: ("split_left", ["10 sai lầm của BA Leader", "làm tụt năng lượng đội ngũ"], arch_battery_energy, {"p1": "Năng lượng ↑", "p2": "Bỏ vi quản lý,", "p3": "trao niềm tin thật", "charge_w": 125, "charge_c": "#48A868", "expr": "smile", "pose": "point_up"}),
    98: ("top_center", ["Phân biệt Auto-Suggest, Auto-Complete", "và ML-Based Recommendation"], arch_three_specimens, {"p1": "Auto-Suggest", "s1": "Gợi ý danh sách", "p2": "Auto-Complete", "s2": "Điền nốt từ khóa", "p3": "ML Recommend", "s3": "Cá nhân hóa thông minh", "expr": "explain"}),
    99: ("top_center", ["Outcome và Output:", "Đừng nhầm giữa “bận rộn” và “hiệu quả”"], arch_bullseye_outcome, {"p1": "Output: 50 trang", "p2": "Bận tối mắt", "p3": "Outcome: Giá trị thật!"}),
    100: ("top_center", ["10 năm làm nghề – Tôi giữ lại 3 thứ:", "Mindset, Hệ thống và Bản lĩnh"], arch_three_pillars, {"p1": "Mindset", "p2": "Hệ thống", "p3": "Bản lĩnh", "expr": "smile", "hat": "crown"}),
}
