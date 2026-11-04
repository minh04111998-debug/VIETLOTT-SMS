# -*- coding: utf-8 -*-
"""
SVG graphic generators for each specific topic in 100 ngày làm BA.
"""

def svg_rocket_monitoring():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- Live Monitoring Dashboard with Rocket Launch -->
      <rect x="40" y="30" width="340" height="200" rx="16" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <rect x="55" y="45" width="310" height="30" rx="6" fill="#0f172a"/>
      <circle cx="75" cy="60" r="5" fill="#ef4444"/>
      <circle cx="92" cy="60" r="5" fill="#f59e0b"/>
      <circle cx="109" cy="60" r="5" fill="#10b981"/>
      <text x="210" y="65" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">PROD TELEMETRY · LIVE</text>
      
      <!-- Metrics bars -->
      <rect x="65" y="95" width="70" height="110" rx="8" fill="#0f172a" stroke="#334155"/>
      <rect x="75" y="145" width="50" height="50" rx="4" fill="#10b981"/>
      <text x="100" y="115" text-anchor="middle" fill="#94a3b8" font-size="11">Active User</text>
      <text x="100" y="135" text-anchor="middle" fill="#34d399" font-size="14" font-weight="bold">98.4%</text>

      <rect x="150" y="95" width="105" height="110" rx="8" fill="#0f172a" stroke="#334155"/>
      <polyline points="160,175 180,165 200,180 220,140 240,150" fill="none" stroke="#38bdf8" stroke-width="3"/>
      <text x="202" y="115" text-anchor="middle" fill="#94a3b8" font-size="11">Funnel Drop</text>
      <text x="202" y="135" text-anchor="middle" fill="#38bdf8" font-size="14" font-weight="bold">-4.2% (Pass)</text>

      <rect x="270" y="95" width="95" height="110" rx="8" fill="#0f172a" stroke="#334155"/>
      <circle cx="317" cy="155" r="28" fill="none" stroke="#f59e0b" stroke-width="6" stroke-dasharray="140, 40"/>
      <text x="317" y="115" text-anchor="middle" fill="#94a3b8" font-size="11">CSKH Ticket</text>
      <text x="317" y="160" text-anchor="middle" fill="#fbbf24" font-size="13" font-weight="bold">0 Bug</text>

      <!-- Rocket launching -->
      <g transform="translate(420, 20)">
        <!-- Booster flame -->
        <polygon points="100,160 85,210 100,195 115,210" fill="#f97316"/>
        <polygon points="100,165 92,200 100,190 108,200" fill="#fde047"/>
        <!-- Rocket Body -->
        <path d="M100,30 C85,60 75,110 75,160 L125,160 C125,110 115,60 100,30 Z" fill="#f8fafc" stroke="#0f172a" stroke-width="3"/>
        <path d="M100,30 C92,45 85,70 85,85 L115,85 C115,70 108,45 100,30 Z" fill="#ef4444"/>
        <!-- Wings -->
        <polygon points="75,130 50,165 75,160" fill="#3b82f6"/>
        <polygon points="125,130 150,165 125,160" fill="#3b82f6"/>
        <!-- Window -->
        <circle cx="100" cy="110" r="14" fill="#38bdf8" stroke="#0f172a" stroke-width="2.5"/>
        <circle cx="100" cy="110" r="10" fill="#e0f2fe"/>
      </g>
    </svg>
    """

def svg_ba_manager_clock():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- 4 Stages of BA Manager day -->
      <g transform="translate(30, 40)">
        <rect x="0" y="0" width="130" height="170" rx="14" fill="#292524" stroke="#eab308" stroke-width="2"/>
        <text x="65" y="32" text-anchor="middle" fill="#fef08a" font-size="14" font-weight="bold">☀️ SÁNG</text>
        <line x1="20" y1="46" x2="110" y2="46" stroke="#44403c"/>
        <circle cx="65" cy="80" r="22" fill="#44403c"/>
        <text x="65" y="86" text-anchor="middle" fill="#fde047" font-size="18">💬</text>
        <text x="65" y="125" text-anchor="middle" fill="#e7e5e4" font-size="11">Đỡ tin nhắn khuya</text>
        <text x="65" y="145" text-anchor="middle" fill="#a8a29e" font-size="10">Join họp gỡ rối</text>
      </g>
      <g transform="translate(180, 40)">
        <rect x="0" y="0" width="130" height="170" rx="14" fill="#292524" stroke="#ca8a04" stroke-width="2"/>
        <text x="65" y="32" text-anchor="middle" fill="#fef08a" font-size="14" font-weight="bold">📖 TRƯA</text>
        <line x1="20" y1="46" x2="110" y2="46" stroke="#44403c"/>
        <circle cx="65" cy="80" r="22" fill="#44403c"/>
        <text x="65" y="86" text-anchor="middle" fill="#60a5fa" font-size="18">🗺️</text>
        <text x="65" y="125" text-anchor="middle" fill="#e7e5e4" font-size="11">Rà soát 3 dự án</text>
        <text x="65" y="145" text-anchor="middle" fill="#a8a29e" font-size="10">Vẽ lại bản đồ</text>
      </g>
      <g transform="translate(330, 40)">
        <rect x="0" y="0" width="130" height="170" rx="14" fill="#292524" stroke="#ca8a04" stroke-width="2"/>
        <text x="65" y="32" text-anchor="middle" fill="#fef08a" font-size="14" font-weight="bold">💼 CHIỀU</text>
        <line x1="20" y1="46" x2="110" y2="46" stroke="#44403c"/>
        <circle cx="65" cy="80" r="22" fill="#44403c"/>
        <text x="65" y="86" text-anchor="middle" fill="#4ade80" font-size="18">👂</text>
        <text x="65" y="125" text-anchor="middle" fill="#e7e5e4" font-size="11">Đồng hành Junior</text>
        <text x="65" y="145" text-anchor="middle" fill="#a8a29e" font-size="10">Lắng nghe & gỡ</text>
      </g>
      <g transform="translate(480, 40)">
        <rect x="0" y="0" width="130" height="170" rx="14" fill="#292524" stroke="#eab308" stroke-width="2"/>
        <text x="65" y="32" text-anchor="middle" fill="#fef08a" font-size="14" font-weight="bold">🌙 TỐI</text>
        <line x1="20" y1="46" x2="110" y2="46" stroke="#44403c"/>
        <circle cx="65" cy="80" r="22" fill="#44403c"/>
        <text x="65" y="86" text-anchor="middle" fill="#c084fc" font-size="18">✍️</text>
        <text x="65" y="125" text-anchor="middle" fill="#e7e5e4" font-size="11">Viết 100 ngày BA</text>
        <text x="65" y="145" text-anchor="middle" fill="#a8a29e" font-size="10">Truyền lửa nghề</text>
      </g>
    </svg>
    """

def svg_hacker_edge_case():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- Happy Path vs Destructive Edge Case -->
      <g transform="translate(40, 30)">
        <rect x="0" y="0" width="260" height="195" rx="16" fill="#064e3b" stroke="#10b981" stroke-width="2.5"/>
        <text x="130" y="35" text-anchor="middle" fill="#6ee7b7" font-size="15" font-weight="bold">HAPPY PATH (User thường)</text>
        <rect x="30" y="55" width="200" height="35" rx="8" fill="#022c22"/>
        <text x="130" y="78" text-anchor="middle" fill="#a7f3d0" font-size="12">1. Điền form đúng chuẩn</text>
        <rect x="30" y="100" width="200" height="35" rx="8" fill="#022c22"/>
        <text x="130" y="123" text-anchor="middle" fill="#a7f3d0" font-size="12">2. Nhấn nút 1 lần</text>
        <rect x="30" y="145" width="200" height="35" rx="8" fill="#022c22"/>
        <text x="130" y="168" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">✅ Giao dịch thành công</text>
      </g>
      <text x="320" y="135" text-anchor="middle" fill="#f87171" font-size="28" font-weight="bold">VS</text>
      <g transform="translate(340, 30)">
        <rect x="0" y="0" width="260" height="195" rx="16" fill="#450a0a" stroke="#ef4444" stroke-width="2.5"/>
        <text x="130" y="35" text-anchor="middle" fill="#fca5a5" font-size="15" font-weight="bold">EDGE CASE (Thằng... Phá)</text>
        <rect x="30" y="55" width="200" height="35" rx="8" fill="#1c1917"/>
        <text x="130" y="78" text-anchor="middle" fill="#fecdd3" font-size="12">1. Spam click 10 lần liên tục</text>
        <rect x="30" y="100" width="200" height="35" rx="8" fill="#1c1917"/>
        <text x="130" y="123" text-anchor="middle" fill="#fecdd3" font-size="12">2. Đổi URL token, tắt wifi</text>
        <rect x="30" y="145" width="200" height="35" rx="8" fill="#1c1917"/>
        <text x="130" y="168" text-anchor="middle" fill="#f87171" font-size="12" font-weight="bold">🛡️ Idempotency &amp; Fallback</text>
      </g>
    </svg>
    """

def svg_git_tree():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- Main Branch Line -->
      <line x1="50" y1="180" x2="590" y2="180" stroke="#38bdf8" stroke-width="4"/>
      <circle cx="90" cy="180" r="14" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
      <circle cx="210" cy="180" r="14" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
      <circle cx="390" cy="180" r="14" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
      <circle cx="530" cy="180" r="16" fill="#10b981" stroke="#34d399" stroke-width="3.5"/>
      <text x="50" y="215" fill="#38bdf8" font-size="13" font-weight="bold">main (prod)</text>
      
      <!-- Feature Branch Curve -->
      <path d="M 210,180 C 260,180 260,80 310,80 L 430,80 C 470,80 480,180 530,180" fill="none" stroke="#f59e0b" stroke-width="3.5" stroke-dasharray="6,4"/>
      <circle cx="330" cy="80" r="14" fill="#0f172a" stroke="#f59e0b" stroke-width="3"/>
      <circle cx="430" cy="80" r="14" fill="#0f172a" stroke="#f59e0b" stroke-width="3"/>
      <text x="380" y="55" fill="#fbbf24" font-size="13" font-weight="bold">feature/cart-checkout</text>
      
      <!-- PR Badge -->
      <rect x="460" y="105" width="110" height="32" rx="8" fill="#10b981" stroke="#064e3b" stroke-width="1.5"/>
      <text x="515" y="126" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">✓ PR Merged</text>
    </svg>
    """

def svg_speed_boat():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- Water surface -->
      <path d="M 20,180 Q 80,165 140,180 T 260,180 T 380,180 T 500,180 T 620,180" fill="none" stroke="#38bdf8" stroke-width="3"/>
      <path d="M 20,200 Q 80,185 140,200 T 260,200 T 380,200 T 500,200 T 620,200" fill="none" stroke="#0284c7" stroke-width="2" opacity="0.6"/>

      <!-- Island / Goal -->
      <path d="M 520,180 C 530,140 590,140 600,180 Z" fill="#eab308"/>
      <line x1="560" y1="140" x2="560" y2="90" stroke="#fef08a" stroke-width="3"/>
      <polygon points="560,90 605,105 560,120" fill="#ef4444"/>
      <text x="560" y="80" text-anchor="middle" fill="#fef08a" font-size="13" font-weight="bold">GOAL / GO-LIVE</text>

      <!-- Speed Boat -->
      <g transform="translate(180, 70)">
        <!-- Boat Hull -->
        <path d="M 20,105 L 170,105 L 195,80 L 0,80 Z" fill="#f8fafc" stroke="#0f172a" stroke-width="3"/>
        <!-- Cabin -->
        <rect x="50" y="55" width="60" height="25" rx="4" fill="#38bdf8"/>
        <!-- Mast & Sails (Drivers / Gió đẩy) -->
        <line x1="120" y1="80" x2="120" y2="10" stroke="#f8fafc" stroke-width="3"/>
        <path d="M 120,15 Q 165,45 120,75 Z" fill="#38bdf8" opacity="0.85"/>
        <text x="70" y="30" fill="#67e8f9" font-size="12" font-weight="bold">💨 Động lực (Wind)</text>
        
        <!-- Anchors (Blockers / Rào cản kéo tụt) -->
        <line x1="40" y1="105" x2="20" y2="160" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4,3"/>
        <circle cx="20" cy="165" r="9" fill="#ef4444"/>
        <text x="20" y="170" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">⚓</text>
        <line x1="90" y1="105" x2="80" y2="155" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4,3"/>
        <circle cx="80" cy="160" r="9" fill="#ef4444"/>
        <text x="80" y="165" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">⚓</text>
        <text x="120" y="170" fill="#f87171" font-size="12" font-weight="bold">⚓ Rào cản ngầm (Anchors)</text>
      </g>
    </svg>
    """

def svg_polc_four():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- 4 Quadrants of P.O.L.C -->
      <g transform="translate(60, 25)">
        <rect x="0" y="0" width="245" height="95" rx="12" fill="#292524" stroke="#eab308" stroke-width="2.5"/>
        <text x="20" y="32" fill="#fef08a" font-size="16" font-weight="bold">1. PLANNING (Kế hoạch)</text>
        <text x="20" y="58" fill="#d6d3d1" font-size="12">• Lộ trình phân tích by sprint</text>
        <text x="20" y="78" fill="#a8a29e" font-size="11">• Backup nhân sự &amp; timeline</text>
      </g>
      <g transform="translate(335, 25)">
        <rect x="0" y="0" width="245" height="95" rx="12" fill="#292524" stroke="#38bdf8" stroke-width="2.5"/>
        <text x="20" y="32" fill="#7dd3fc" font-size="16" font-weight="bold">2. ORGANIZING (Tổ chức)</text>
        <text x="20" y="58" fill="#d6d3d1" font-size="12">• Xây template, checklist chuẩn</text>
        <text x="20" y="78" fill="#a8a29e" font-size="11">• Phân chia module &amp; trace CR</text>
      </g>
      <g transform="translate(60, 135)">
        <rect x="0" y="0" width="245" height="95" rx="12" fill="#292524" stroke="#f43f5e" stroke-width="2.5"/>
        <text x="20" y="32" fill="#fda4af" font-size="16" font-weight="bold">3. LEADING (Dẫn dắt)</text>
        <text x="20" y="58" fill="#d6d3d1" font-size="12">• Gợi mở tư duy, không soi vặt</text>
        <text x="20" y="78" fill="#a8a29e" font-size="11">• Bảo vệ team trước vô lý</text>
      </g>
      <g transform="translate(335, 135)">
        <rect x="0" y="0" width="245" height="95" rx="12" fill="#292524" stroke="#10b981" stroke-width="2.5"/>
        <text x="20" y="32" fill="#6ee7b7" font-size="16" font-weight="bold">4. CONTROLLING (Kiểm soát)</text>
        <text x="20" y="58" fill="#d6d3d1" font-size="12">• Quản lý chất lượng &amp; logic</text>
        <text x="20" y="78" fill="#a8a29e" font-size="11">• Đo reject rate &amp; UAT pass</text>
      </g>
    </svg>
    """

def svg_three_pillars():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- 3 Foundation Pillars for 10 Years as BA -->
      <g transform="translate(50, 40)">
        <rect x="0" y="0" width="160" height="170" rx="14" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2.5"/>
        <text x="80" y="38" text-anchor="middle" fill="#93c5fd" font-size="16" font-weight="bold">🧠 MINDSET</text>
        <line x1="25" y1="52" x2="135" y2="52" stroke="#3b82f6"/>
        <text x="80" y="85" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">Tư duy hệ thống</text>
        <text x="80" y="115" text-anchor="middle" fill="#bfdbfe" font-size="11">Luôn hỏi gốc rễ</text>
        <text x="80" y="135" text-anchor="middle" fill="#bfdbfe" font-size="11">Không chạy theo lời</text>
        <text x="80" y="155" text-anchor="middle" fill="#93c5fd" font-size="10">Vấn đề cốt lõi là gì?</text>
      </g>
      <g transform="translate(240, 40)">
        <rect x="0" y="0" width="160" height="170" rx="14" fill="#065f46" stroke="#34d399" stroke-width="2.5"/>
        <text x="80" y="38" text-anchor="middle" fill="#6ee7b7" font-size="16" font-weight="bold">⚙️ HỆ THỐNG</text>
        <line x1="25" y1="52" x2="135" y2="52" stroke="#10b981"/>
        <text x="80" y="85" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">Chuẩn hóa reuse</text>
        <text x="80" y="115" text-anchor="middle" fill="#a7f3d0" font-size="11">Template &amp; checklist</text>
        <text x="80" y="135" text-anchor="middle" fill="#a7f3d0" font-size="11">Không bắt đầu số 0</text>
        <text x="80" y="155" text-anchor="middle" fill="#6ee7b7" font-size="10">Giữ team vững vàng</text>
      </g>
      <g transform="translate(430, 40)">
        <rect x="0" y="0" width="160" height="170" rx="14" fill="#831843" stroke="#f472b6" stroke-width="2.5"/>
        <text x="80" y="38" text-anchor="middle" fill="#fbcfe8" font-size="16" font-weight="bold">🛡️ BẢN LĨNH</text>
        <line x1="25" y1="52" x2="135" y2="52" stroke="#ec4899"/>
        <text x="80" y="85" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">Dám nói điều đúng</text>
        <text x="80" y="115" text-anchor="middle" fill="#fce7f3" font-size="11">Lập luận có dữ liệu</text>
        <text x="80" y="135" text-anchor="middle" fill="#fce7f3" font-size="11">Không gân cổ cãi</text>
        <text x="80" y="155" text-anchor="middle" fill="#fbcfe8" font-size="10">Giữ vững chuẩn nghề</text>
      </g>
    </svg>
    """

def svg_mobile_thumb_zone():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- Smartphone mockup with Thumb Zone -->
      <g transform="translate(80, 20)">
        <rect x="0" y="0" width="130" height="220" rx="20" fill="#0f172a" stroke="#64748b" stroke-width="3"/>
        <rect x="8" y="12" width="114" height="196" rx="12" fill="#1e293b"/>
        <!-- Notch -->
        <rect x="45" y="16" width="40" height="10" rx="5" fill="#0f172a"/>
        <!-- Thumb Zones -->
        <!-- Hard to reach (top red) -->
        <path d="M 8,22 L 122,22 L 122,70 C 90,65 40,65 8,70 Z" fill="#ef4444" opacity="0.35"/>
        <text x="65" y="48" text-anchor="middle" fill="#fca5a5" font-size="10" font-weight="bold">Vùng với (Khó chạm)</text>
        <!-- Stretch zone (middle yellow) -->
        <path d="M 8,70 C 40,65 90,65 122,70 L 122,120 C 80,125 40,140 8,150 Z" fill="#f59e0b" opacity="0.35"/>
        <text x="65" y="105" text-anchor="middle" fill="#fde047" font-size="10" font-weight="bold">Vùng rướn</text>
        <!-- Natural Thumb zone (bottom green) -->
        <path d="M 8,150 C 40,140 80,125 122,120 L 122,208 L 8,208 Z" fill="#10b981" opacity="0.45"/>
        <text x="65" y="175" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">VÙNG THAO TÁC 1 TAY</text>
      </g>
      <!-- Explanation cards on right -->
      <g transform="translate(250, 40)">
        <rect x="0" y="0" width="340" height="50" rx="10" fill="#2e1065" stroke="#a855f7" stroke-width="1.5"/>
        <text x="20" y="30" fill="#e9d5ff" font-size="13" font-weight="bold">🟢 Nút bấm chính (CTA): Đặt sát đáy màn hình</text>
        
        <rect x="0" y="65" width="340" height="50" rx="10" fill="#2e1065" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="20" y="95" fill="#fde047" font-size="13" font-weight="bold">🟡 Bộ lọc / Tìm kiếm: Cần kéo xuống tầm tay</text>

        <rect x="0" y="130" width="340" height="50" rx="10" fill="#2e1065" stroke="#ef4444" stroke-width="1.5"/>
        <text x="20" y="160" fill="#fca5a5" font-size="13" font-weight="bold">🔴 Góc trên cùng: Chỉ để thông tin, cấm nút quan trọng</text>
      </g>
    </svg>
    """

def svg_accounting_ledger():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- Double-entry T-Account Balance -->
      <g transform="translate(40, 30)">
        <rect x="0" y="0" width="260" height="195" rx="14" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="130" y="32" text-anchor="middle" fill="#a7f3d0" font-size="14" font-weight="bold">TÀI KHOẢN NỢ (DEBIT)</text>
        <line x1="20" y1="46" x2="240" y2="46" stroke="#059669"/>
        <text x="30" y="75" fill="#ecfdf5" font-size="12">1. Doanh thu bán hàng</text>
        <text x="210" y="75" fill="#34d399" font-size="12" font-weight="bold">+10M</text>
        <text x="30" y="110" fill="#ecfdf5" font-size="12">2. Tiền gửi ngân hàng</text>
        <text x="210" y="110" fill="#34d399" font-size="12" font-weight="bold">+15M</text>
        <text x="30" y="145" fill="#ecfdf5" font-size="12">3. Hàng tồn kho nhập</text>
        <text x="210" y="145" fill="#34d399" font-size="12" font-weight="bold">+5M</text>
      </g>
      <text x="320" y="135" text-anchor="middle" fill="#f59e0b" font-size="32" font-weight="bold">=</text>
      <g transform="translate(340, 30)">
        <rect x="0" y="0" width="260" height="195" rx="14" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="130" y="32" text-anchor="middle" fill="#a7f3d0" font-size="14" font-weight="bold">TÀI KHOẢN CÓ (CREDIT)</text>
        <line x1="20" y1="46" x2="240" y2="46" stroke="#059669"/>
        <text x="30" y="75" fill="#ecfdf5" font-size="12">1. Thuế GTGT đầu ra (VAT)</text>
        <text x="215" y="75" fill="#fde047" font-size="12" font-weight="bold">-1M</text>
        <text x="30" y="110" fill="#ecfdf5" font-size="12">2. Chiết khấu thương mại</text>
        <text x="215" y="110" fill="#fde047" font-size="12" font-weight="bold">-500K</text>
        <text x="30" y="145" fill="#ecfdf5" font-size="12">3. Phải trả nhà cung cấp</text>
        <text x="215" y="145" fill="#fde047" font-size="12" font-weight="bold">-4.5M</text>
      </g>
    </svg>
    """

def svg_reverse_gears():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- Old Legacy Blackbox -> Reverse Engineer -> Clean Schema -->
      <g transform="translate(40, 45)">
        <rect x="0" y="0" width="160" height="160" rx="16" fill="#27272a" stroke="#71717a" stroke-width="2.5"/>
        <text x="80" y="35" text-anchor="middle" fill="#a1a1aa" font-size="13" font-weight="bold">LEGACY SYSTEM</text>
        <circle cx="80" cy="95" r="38" fill="none" stroke="#eab308" stroke-width="8" stroke-dasharray="8,6"/>
        <circle cx="80" cy="95" r="14" fill="#eab308"/>
        <text x="80" y="150" text-anchor="middle" fill="#71717a" font-size="11">Không tài liệu / Dev nghỉ</text>
      </g>
      <!-- Transition arrow -->
      <g transform="translate(225, 110)">
        <line x1="0" y1="15" x2="60" y2="15" stroke="#38bdf8" stroke-width="4"/>
        <polygon points="60,5 80,15 60,25" fill="#38bdf8"/>
        <text x="40" y="-5" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">BÓC TÁCH</text>
      </g>
      <g transform="translate(330, 35)">
        <rect x="0" y="0" width="270" height="180" rx="16" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5"/>
        <text x="135" y="32" text-anchor="middle" fill="#38bdf8" font-size="14" font-weight="bold">REVERSE-ENGINEERED MODEL</text>
        <rect x="20" y="50" width="105" height="48" rx="8" fill="#1e293b" stroke="#334155"/>
        <text x="72" y="72" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="bold">1. Trace DB Log</text>
        <text x="72" y="88" text-anchor="middle" fill="#94a3b8" font-size="10">Quan sát data biến thiên</text>
        <rect x="145" y="50" width="105" height="48" rx="8" fill="#1e293b" stroke="#334155"/>
        <text x="197" y="72" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="bold">2. Trigger Edge</text>
        <text x="197" y="88" text-anchor="middle" fill="#94a3b8" font-size="10">Thao tác ép lỗi UI</text>
        <rect x="20" y="112" width="230" height="50" rx="8" fill="#1e293b" stroke="#10b981"/>
        <text x="135" y="134" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">3. Dựng lại Logic Matrix &amp; ERD</text>
        <text x="135" y="152" text-anchor="middle" fill="#a7f3d0" font-size="10">Khôi phục 100% luật ngầm</text>
      </g>
    </svg>
    """

def svg_mad_unicorn():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- Unicorn Express Delivery Logistics Network -->
      <g transform="translate(60, 40)">
        <circle cx="80" cy="80" r="60" fill="#3b0764" stroke="#c084fc" stroke-width="2.5"/>
        <text x="80" y="65" text-anchor="middle" fill="#e9d5ff" font-size="32">🦄</text>
        <text x="80" y="105" text-anchor="middle" fill="#f0abfc" font-size="12" font-weight="bold">MAD UNICORN</text>
        <text x="80" y="122" text-anchor="middle" fill="#d8b4fe" font-size="10">Express Logistics</text>
      </g>
      <!-- Delivery route nodes -->
      <g transform="translate(230, 40)">
        <rect x="0" y="0" width="370" height="170" rx="14" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
        <circle cx="50" cy="50" r="18" fill="#4338ca"/>
        <text x="50" y="55" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">HUB</text>
        <line x1="68" y1="50" x2="160" y2="50" stroke="#f472b6" stroke-width="3" stroke-dasharray="6,4"/>
        <circle cx="180" cy="50" r="18" fill="#be185d"/>
        <text x="180" y="55" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">SORT</text>
        <line x1="198" y1="50" x2="290" y2="50" stroke="#f472b6" stroke-width="3" stroke-dasharray="6,4"/>
        <circle cx="310" cy="50" r="18" fill="#047857"/>
        <text x="310" y="55" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">USER</text>
        
        <!-- BA Key Questions -->
        <rect x="25" y="90" width="320" height="60" rx="8" fill="#2e1065"/>
        <text x="40" y="112" fill="#fde047" font-size="11" font-weight="bold">❓ Nếu shipper hỏng xe giữa đường?</text>
        <text x="40" y="132" fill="#fbcfe8" font-size="11" font-weight="bold">❓ Khách hẹn lại giờ giao 3 lần?</text>
      </g>
    </svg>
    """

def svg_dynamic_pricing():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- Surge Pricing Curve (50k -> 65k) -->
      <g transform="translate(50, 30)">
        <rect x="0" y="0" width="540" height="195" rx="16" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <!-- Chart axes -->
        <line x1="60" y1="155" x2="480" y2="155" stroke="#334155" stroke-width="2"/>
        <line x1="60" y1="30" x2="60" y2="155" stroke="#334155" stroke-width="2"/>
        <text x="40" y="158" fill="#94a3b8" font-size="11">50k</text>
        <text x="40" y="65" fill="#f59e0b" font-size="11" font-weight="bold">65k</text>
        <!-- Baseline price line -->
        <line x1="60" y1="130" x2="240" y2="130" stroke="#10b981" stroke-width="3"/>
        <circle cx="150" cy="130" r="8" fill="#10b981"/>
        <text x="150" y="115" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">Bình thường: 50K</text>
        
        <!-- Surge Curve -->
        <path d="M 240,130 C 290,130 310,60 380,60 L 480,60" fill="none" stroke="#f59e0b" stroke-width="4"/>
        <circle cx="380" cy="60" r="9" fill="#ef4444"/>
        <text x="380" y="42" text-anchor="middle" fill="#f87171" font-size="13" font-weight="bold">Mưa lớn + Giờ cao điểm: 65K</text>
        
        <!-- Multiplier factors -->
        <text x="120" y="180" fill="#94a3b8" font-size="11">Base Supply = Demand</text>
        <text x="350" y="180" fill="#fbbf24" font-size="11" font-weight="bold">Surge Multiplier x1.3 (Nhu cầu tăng 300%)</text>
      </g>
    </svg>
    """

def svg_kpi_tree():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- 3-Tier KPI Hierarchy Tree -->
      <!-- Tier 1: North Star Metric -->
      <g transform="translate(220, 20)">
        <rect x="0" y="0" width="200" height="50" rx="10" fill="#1e1b4b" stroke="#f59e0b" stroke-width="2.5"/>
        <text x="100" y="24" text-anchor="middle" fill="#fef08a" font-size="12" font-weight="bold">NORTH STAR METRIC</text>
        <text x="100" y="42" text-anchor="middle" fill="#ffffff" font-size="11">Doanh thu gộp (GMV)</text>
      </g>
      <!-- Connector lines -->
      <line x1="320" y1="70" x2="320" y2="95" stroke="#f59e0b" stroke-width="2"/>
      <line x1="160" y1="95" x2="480" y2="95" stroke="#f59e0b" stroke-width="2"/>
      <line x1="160" y1="95" x2="160" y2="115" stroke="#f59e0b" stroke-width="2"/>
      <line x1="480" y1="95" x2="480" y2="115" stroke="#f59e0b" stroke-width="2"/>
      
      <!-- Tier 2: Driver Metrics -->
      <g transform="translate(60, 115)">
        <rect x="0" y="0" width="200" height="50" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <text x="100" y="24" text-anchor="middle" fill="#7dd3fc" font-size="11" font-weight="bold">LƯỢNG GIAO DỊCH</text>
        <text x="100" y="42" text-anchor="middle" fill="#e2e8f0" font-size="11">Số đơn hàng hoàn tất</text>
      </g>
      <g transform="translate(380, 115)">
        <rect x="0" y="0" width="200" height="50" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
        <text x="100" y="24" text-anchor="middle" fill="#6ee7b7" font-size="11" font-weight="bold">GIÁ TRỊ TRUNG BÌNH (AOV)</text>
        <text x="100" y="42" text-anchor="middle" fill="#e2e8f0" font-size="11">Giá trị trên mỗi đơn</text>
      </g>
      
      <!-- Tier 3: BA Feature Metrics -->
      <g transform="translate(80, 185)">
        <rect x="0" y="0" width="160" height="40" rx="8" fill="#1e293b"/>
        <text x="80" y="25" text-anchor="middle" fill="#93c5fd" font-size="11">Tối ưu Checkout Flow</text>
      </g>
      <g transform="translate(400, 185)">
        <rect x="0" y="0" width="160" height="40" rx="8" fill="#1e293b"/>
        <text x="80" y="25" text-anchor="middle" fill="#a7f3d0" font-size="11">Gợi ý Cross-sell Combo</text>
      </g>
    </svg>
    """

def svg_nfr_tiles():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- 4 Non-Functional Requirements Tiles -->
      <g transform="translate(40, 30)">
        <rect x="0" y="0" width="260" height="90" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <text x="25" y="32" fill="#38bdf8" font-size="14" font-weight="bold">⚡ PERFORMANCE / LATENCY</text>
        <text x="25" y="58" fill="#f8fafc" font-size="12">Thời gian phản hồi API &lt; 200ms</text>
        <text x="25" y="76" fill="#94a3b8" font-size="11">Tại tải đỉnh 95th percentile</text>
      </g>
      <g transform="translate(340, 30)">
        <rect x="0" y="0" width="260" height="90" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
        <text x="25" y="32" fill="#34d399" font-size="14" font-weight="bold">🛡️ AVAILABILITY / SLA</text>
        <text x="25" y="58" fill="#f8fafc" font-size="12">Độ sẵn sàng hệ thống 99.9%</text>
        <text x="25" y="76" fill="#94a3b8" font-size="11">Downtime tối đa &lt; 43 phút / tháng</text>
      </g>
      <g transform="translate(40, 140)">
        <rect x="0" y="0" width="260" height="90" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
        <text x="25" y="32" fill="#fbbf24" font-size="14" font-weight="bold">📈 CONCURRENCY / TPS</text>
        <text x="25" y="58" fill="#f8fafc" font-size="12">Chịu tải 5,000 giao dịch / giây</text>
        <text x="25" y="76" fill="#94a3b8" font-size="11">Tự động auto-scale khi vượt 80%</text>
      </g>
      <g transform="translate(340, 140)">
        <rect x="0" y="0" width="260" height="90" rx="12" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
        <text x="25" y="32" fill="#f472b6" font-size="14" font-weight="bold">🔒 SECURITY &amp; DATA PRIVACY</text>
        <text x="25" y="58" fill="#f8fafc" font-size="12">Mã hóa PII chuẩn AES-256</text>
        <text x="25" y="76" fill="#94a3b8" font-size="11">Tuân thủ Nghị định 13/2023/NĐ-CP</text>
      </g>
    </svg>
    """

def svg_three_bugs():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- 3 Types of Errors: Logic Bug, Dev Bug, User Expectation Gap -->
      <g transform="translate(40, 35)">
        <rect x="0" y="0" width="170" height="180" rx="14" fill="#450a0a" stroke="#ef4444" stroke-width="2.5"/>
        <circle cx="85" cy="50" r="22" fill="#7f1d1d"/>
        <text x="85" y="57" text-anchor="middle" fill="#ffffff" font-size="20">🐛</text>
        <text x="85" y="95" text-anchor="middle" fill="#fca5a5" font-size="13" font-weight="bold">1. BUG KỸ THUẬT</text>
        <text x="85" y="125" text-anchor="middle" fill="#fecdd3" font-size="11">Crash, Null Pointer</text>
        <text x="85" y="145" text-anchor="middle" fill="#fecdd3" font-size="11">500 Server Error</text>
        <text x="85" y="165" text-anchor="middle" fill="#f87171" font-size="10">DEV Fix Code</text>
      </g>
      <g transform="translate(235, 35)">
        <rect x="0" y="0" width="170" height="180" rx="14" fill="#431407" stroke="#f59e0b" stroke-width="2.5"/>
        <circle cx="85" cy="50" r="22" fill="#78350f"/>
        <text x="85" y="57" text-anchor="middle" fill="#ffffff" font-size="20">📐</text>
        <text x="85" y="95" text-anchor="middle" fill="#fde047" font-size="13" font-weight="bold">2. BUG LOGIC NGHIỆP VỤ</text>
        <text x="85" y="125" text-anchor="middle" fill="#fef3c7" font-size="11">Thiếu case ngoại lệ</text>
        <text x="85" y="145" text-anchor="middle" fill="#fef3c7" font-size="11">Tính sai chiết khấu</text>
        <text x="85" y="165" text-anchor="middle" fill="#fbbf24" font-size="10">BA Fix SRS / Flow</text>
      </g>
      <g transform="translate(430, 35)">
        <rect x="0" y="0" width="170" height="180" rx="14" fill="#1e1b4b" stroke="#38bdf8" stroke-width="2.5"/>
        <circle cx="85" cy="50" r="22" fill="#312e81"/>
        <text x="85" y="57" text-anchor="middle" fill="#ffffff" font-size="20">💡</text>
        <text x="85" y="95" text-anchor="middle" fill="#7dd3fc" font-size="13" font-weight="bold">3. GAP KỲ VỌNG</text>
        <text x="85" y="125" text-anchor="middle" fill="#e0f2fe" font-size="11">Hệ thống làm đúng spec</text>
        <text x="85" y="145" text-anchor="middle" fill="#e0f2fe" font-size="11">Nhưng User thấy khó</text>
        <text x="85" y="165" text-anchor="middle" fill="#38bdf8" font-size="10">PO / BA Cải tiến UX</text>
      </g>
    </svg>
    """

def svg_ride_stitch():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- Ride Hailing Route Stitching (Nối cuốc) -->
      <g transform="translate(40, 30)">
        <rect x="0" y="0" width="560" height="195" rx="16" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
        <!-- Map Grid Lines -->
        <line x1="40" y1="50" x2="520" y2="50" stroke="#1e293b" stroke-width="1.5"/>
        <line x1="40" y1="100" x2="520" y2="100" stroke="#1e293b" stroke-width="1.5"/>
        <line x1="40" y1="150" x2="520" y2="150" stroke="#1e293b" stroke-width="1.5"/>
        <line x1="140" y1="20" x2="140" y2="180" stroke="#1e293b" stroke-width="1.5"/>
        <line x1="280" y1="20" x2="280" y2="180" stroke="#1e293b" stroke-width="1.5"/>
        <line x1="420" y1="20" x2="420" y2="180" stroke="#1e293b" stroke-width="1.5"/>

        <!-- Trip 1: Blue line ending at Dropoff A -->
        <path d="M 80,130 C 120,70 180,80 230,80" fill="none" stroke="#38bdf8" stroke-width="4"/>
        <circle cx="80" cy="130" r="10" fill="#38bdf8"/>
        <circle cx="230" cy="80" r="12" fill="#ef4444"/>
        <text x="230" y="60" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="bold">Điểm trả Khách 1</text>
        
        <!-- Seamless Stitching connector -->
        <line x1="230" y1="80" x2="310" y2="120" stroke="#f59e0b" stroke-width="3" stroke-dasharray="6,4"/>
        <text x="270" y="115" text-anchor="middle" fill="#fde047" font-size="11" font-weight="bold">NỐI CUỐC (300m)</text>
        
        <!-- Trip 2: Green line starting at Pickup B -->
        <circle cx="310" cy="120" r="12" fill="#10b981"/>
        <text x="310" y="145" text-anchor="middle" fill="#6ee7b7" font-size="11" font-weight="bold">Điểm đón Khách 2</text>
        <path d="M 310,120 C 370,120 420,70 480,90" fill="none" stroke="#10b981" stroke-width="4"/>
        <circle cx="480" cy="90" r="10" fill="#10b981"/>

        <!-- Impact Badge -->
        <rect x="150" y="160" width="260" height="26" rx="6" fill="#064e3b" stroke="#34d399"/>
        <text x="280" y="178" text-anchor="middle" fill="#a7f3d0" font-size="11" font-weight="bold">Giảm 70% thời gian xe chạy rỗng</text>
      </g>
    </svg>
    """

def svg_search_trio():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- 3 Search Features Comparison -->
      <g transform="translate(40, 25)">
        <rect x="0" y="0" width="170" height="200" rx="12" fill="#1e1b4b" stroke="#38bdf8" stroke-width="2"/>
        <text x="85" y="30" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="bold">AUTO-COMPLETE</text>
        <rect x="15" y="45" width="140" height="28" rx="6" fill="#0f172a" stroke="#334155"/>
        <text x="25" y="64" fill="#f8fafc" font-size="11">ipho| <tspan fill="#64748b">ne 16</tspan></text>
        <text x="85" y="105" text-anchor="middle" fill="#cbd5e1" font-size="11">Điền nốt từ khóa</text>
        <text x="85" y="125" text-anchor="middle" fill="#94a3b8" font-size="10">Dựa trên Prefix Matching</text>
        <rect x="25" y="150" width="120" height="28" rx="4" fill="#312e81"/>
        <text x="85" y="168" text-anchor="middle" fill="#7dd3fc" font-size="10" font-weight="bold">Search bar</text>
      </g>
      <g transform="translate(235, 25)">
        <rect x="0" y="0" width="170" height="200" rx="12" fill="#1e1b4b" stroke="#f59e0b" stroke-width="2"/>
        <text x="85" y="30" text-anchor="middle" fill="#fde047" font-size="13" font-weight="bold">AUTO-SUGGEST</text>
        <rect x="15" y="45" width="140" height="28" rx="6" fill="#0f172a" stroke="#334155"/>
        <text x="25" y="64" fill="#f8fafc" font-size="11">áo len...</text>
        <rect x="15" y="78" width="140" height="60" rx="4" fill="#0f172a"/>
        <text x="25" y="96" fill="#94a3b8" font-size="10">• áo len nam cổ lọ</text>
        <text x="25" y="114" fill="#94a3b8" font-size="10">• áo len nữ oversize</text>
        <text x="25" y="132" fill="#94a3b8" font-size="10">• áo len cardigan</text>
        <rect x="25" y="150" width="120" height="28" rx="4" fill="#78350f"/>
        <text x="85" y="168" text-anchor="middle" fill="#fef08a" font-size="10" font-weight="bold">Query Popularity</text>
      </g>
      <g transform="translate(430, 25)">
        <rect x="0" y="0" width="170" height="200" rx="12" fill="#1e1b4b" stroke="#10b981" stroke-width="2"/>
        <text x="85" y="30" text-anchor="middle" fill="#6ee7b7" font-size="13" font-weight="bold">ML RECOMMEND</text>
        <rect x="15" y="45" width="140" height="28" rx="6" fill="#0f172a" stroke="#334155"/>
        <text x="25" y="64" fill="#f8fafc" font-size="11">Dành riêng cho bạn</text>
        <text x="85" y="105" text-anchor="middle" fill="#cbd5e1" font-size="11">Cá nhân hóa theo User</text>
        <text x="85" y="125" text-anchor="middle" fill="#94a3b8" font-size="10">Lịch sử xem &amp; mua sắm</text>
        <rect x="25" y="150" width="120" height="28" rx="4" fill="#064e3b"/>
        <text x="85" y="168" text-anchor="middle" fill="#a7f3d0" font-size="10" font-weight="bold">User Embedding</text>
      </g>
    </svg>
    """

def svg_outcome_bullseye():
    return """
    <svg width="640" height="260" viewBox="0 0 640 260">
      <!-- Output (busy conveyor belt) vs Outcome (Target Bullseye) -->
      <g transform="translate(40, 30)">
        <rect x="0" y="0" width="250" height="195" rx="14" fill="#27272a" stroke="#71717a" stroke-width="2"/>
        <text x="125" y="32" text-anchor="middle" fill="#e4e4e7" font-size="14" font-weight="bold">OUTPUT (Số lượng việc)</text>
        <rect x="25" y="55" width="200" height="35" rx="6" fill="#18181b"/>
        <text x="125" y="77" text-anchor="middle" fill="#a1a1aa" font-size="11">Hoàn thành 50 màn hình</text>
        <rect x="25" y="98" width="200" height="35" rx="6" fill="#18181b"/>
        <text x="125" y="120" text-anchor="middle" fill="#a1a1aa" font-size="11">Đóng 120 task Jira</text>
        <rect x="25" y="141" width="200" height="35" rx="6" fill="#18181b"/>
        <text x="125" y="163" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">⚠️ Bận rộn nhưng không hiệu quả</text>
      </g>
      <text x="320" y="135" text-anchor="middle" fill="#f59e0b" font-size="28" font-weight="bold">→</text>
      <g transform="translate(350, 30)">
        <rect x="0" y="0" width="250" height="195" rx="14" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
        <text x="125" y="32" text-anchor="middle" fill="#a7f3d0" font-size="14" font-weight="bold">OUTCOME (Giá trị tạo ra)</text>
        <circle cx="125" cy="100" r="50" fill="#065f46" stroke="#34d399" stroke-width="2"/>
        <circle cx="125" cy="100" r="32" fill="#047857" stroke="#34d399" stroke-width="2"/>
        <circle cx="125" cy="100" r="14" fill="#ef4444"/>
        <text x="125" y="175" text-anchor="middle" fill="#6ee7b7" font-size="12" font-weight="bold">🎯 Tăng 25% tỷ lệ chuyển đổi đơn</text>
      </g>
    </svg>
    """

def svg_generic_scene(icon: str, title1: str, desc1: str, title2: str, desc2: str, title3: str, desc3: str, color1: str, color2: str):
    return f"""
    <svg width="640" height="260" viewBox="0 0 640 260">
      <g transform="translate(40, 30)">
        <rect x="0" y="0" width="170" height="195" rx="14" fill="#0f172a" stroke="{color1}" stroke-width="2"/>
        <circle cx="85" cy="45" r="22" fill="#1e293b"/>
        <text x="85" y="52" text-anchor="middle" fill="#ffffff" font-size="20">{icon}</text>
        <text x="85" y="90" text-anchor="middle" fill="{color1}" font-size="13" font-weight="bold">{title1}</text>
        <rect x="15" y="110" width="140" height="65" rx="6" fill="#1e293b"/>
        <text x="85" y="135" text-anchor="middle" fill="#cbd5e1" font-size="11">{desc1[:22]}</text>
        <text x="85" y="155" text-anchor="middle" fill="#94a3b8" font-size="10">{desc1[22:46]}</text>
      </g>
      <text x="235" y="135" text-anchor="middle" fill="#64748b" font-size="24" font-weight="bold">→</text>
      <g transform="translate(255, 30)">
        <rect x="0" y="0" width="170" height="195" rx="14" fill="#0f172a" stroke="{color2}" stroke-width="2"/>
        <circle cx="85" cy="45" r="22" fill="#1e293b"/>
        <text x="85" y="52" text-anchor="middle" fill="#ffffff" font-size="20">⚡</text>
        <text x="85" y="90" text-anchor="middle" fill="{color2}" font-size="13" font-weight="bold">{title2}</text>
        <rect x="15" y="110" width="140" height="65" rx="6" fill="#1e293b"/>
        <text x="85" y="135" text-anchor="middle" fill="#cbd5e1" font-size="11">{desc2[:22]}</text>
        <text x="85" y="155" text-anchor="middle" fill="#94a3b8" font-size="10">{desc2[22:46]}</text>
      </g>
      <text x="450" y="135" text-anchor="middle" fill="#64748b" font-size="24" font-weight="bold">→</text>
      <g transform="translate(470, 30)">
        <rect x="0" y="0" width="140" height="195" rx="14" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
        <circle cx="70" cy="45" r="22" fill="#1e293b"/>
        <text x="70" y="52" text-anchor="middle" fill="#ffffff" font-size="20">🎯</text>
        <text x="70" y="90" text-anchor="middle" fill="#34d399" font-size="13" font-weight="bold">{title3}</text>
        <rect x="15" y="110" width="110" height="65" rx="6" fill="#1e293b"/>
        <text x="70" y="135" text-anchor="middle" fill="#a7f3d0" font-size="11">{desc3[:18]}</text>
        <text x="70" y="155" text-anchor="middle" fill="#6ee7b7" font-size="10">{desc3[18:38]}</text>
      </g>
    </svg>
    """
