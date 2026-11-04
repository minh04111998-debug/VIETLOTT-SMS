import os

def generate_perfect_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 1820" width="100%" height="auto" style="background-color: #ffffff; font-family: 'Inter', sans-serif;">
  <defs>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#e2e8f0" stroke-width="0.8"/>
    </pattern>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000"/>
    </marker>
  </defs>

  <!-- Background Grid -->
  <rect width="1100" height="1820" fill="url(#grid)" />

  <!-- Top Title Header -->
  <rect x="0" y="0" width="1100" height="40" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="550" y="26" font-weight="bold" font-size="15" text-anchor="middle" fill="#000000">Luồng Hoạt Động Tặng Vé Mở Tài Khoản Kênh Bank (UML Swimlane Diagram)</text>

  <!-- Column Headers -->
  <g font-weight="bold" font-size="14" text-anchor="middle">
    <rect x="0" y="40" width="360" height="40" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
    <text x="180" y="65">Khách hàng &amp; Kênh Bank</text>

    <rect x="360" y="40" width="370" height="40" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
    <text x="545" y="65">Web Admin Vietlott SMS</text>

    <rect x="730" y="40" width="370" height="40" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
    <text x="915" y="65">Hệ thống Realtime Rule Engine &amp; Core Service</text>
  </g>

  <!-- Swimlane Vertical Dividers -->
  <line x1="360" y1="40" x2="360" y2="1820" stroke="#000000" stroke-width="1.5"/>
  <line x1="730" y1="40" x2="730" y2="1820" stroke="#000000" stroke-width="1.5"/>

  <!-- ==================== COLUMN 1: KHÁCH HÀNG & KÊNH BANK ==================== -->
  <circle cx="180" cy="105" r="12" fill="#000000"/>

  <line x1="180" y1="117" x2="180" y2="145" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <rect x="50" y="145" width="260" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="180" y="175" font-size="12" font-weight="600" text-anchor="middle">1. Đăng ký mở tài khoản mới qua kênh Bank</text>

  <line x1="180" y1="195" x2="180" y2="235" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <rect x="40" y="235" width="280" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="180" y="265" font-size="12" font-weight="600" text-anchor="middle">2. Thực hiện eKYC / Active tài khoản / Thanh toán</text>

  <!-- Step 16b Box -->
  <rect x="30" y="1135" width="300" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="180" y="1158" font-size="11" font-weight="600" text-anchor="middle">16b. Nhận thông báo suất tặng vé</text>
  <text x="180" y="1173" font-size="11" font-weight="600" text-anchor="middle">được bảo lưu sang 00:00:01 ngày sau</text>

  <line x1="180" y1="1185" x2="180" y2="1215" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <circle cx="180" cy="1230" r="12" fill="none" stroke="#000000" stroke-width="1.5"/>
  <circle cx="180" cy="1230" r="7" fill="#000000"/>

  <!-- Step 23 Box -->
  <rect x="30" y="1695" width="300" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="180" y="1718" font-size="11" font-weight="600" text-anchor="middle">23. Nhận SMS / Push Noti vé tặng</text>
  <text x="180" y="1733" font-size="11" font-weight="600" text-anchor="middle">&amp; Tra cứu vé trên App</text>

  <line x1="180" y1="1745" x2="180" y2="1770" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <circle cx="180" cy="1785" r="12" fill="none" stroke="#000000" stroke-width="1.5"/>
  <circle cx="180" cy="1785" r="7" fill="#000000"/>


  <!-- ==================== COLUMN 2: WEB ADMIN VIETLOTT SMS ==================== -->
  <rect x="415" y="145" width="260" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="545" y="175" font-size="12" font-weight="600" text-anchor="middle">3. Admin thiết lập cụm 7 điều kiện chiến dịch</text>

  <line x1="545" y1="195" x2="545" y2="235" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <rect x="415" y="235" width="260" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="545" y="265" font-size="12" font-weight="600" text-anchor="middle">4. Nhấn 'Lưu &amp; Kích hoạt' chiến dịch</text>

  <line x1="545" y1="285" x2="545" y2="325" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <polygon points="545,325 655,365 545,405 435,365" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="545" y="360" font-size="11" font-weight="600" text-anchor="middle">5. Kiểm tra thông tin</text>
  <text x="545" y="375" font-size="11" font-weight="600" text-anchor="middle">cấu hình hợp lệ?</text>

  <!-- Branch No: Step 5 -> Step 6 (Off to Side Left X=380..475) -->
  <line x1="435" y1="365" x2="425" y2="365" stroke="#000000" stroke-width="1.2"/>
  <line x1="425" y1="365" x2="425" y2="410" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="430" y="357" font-size="10" font-weight="bold" fill="#000">No</text>

  <!-- Step 6 Box (On Left Branch X=370..480, Y=410) -->
  <rect x="375" y="410" width="105" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="427" y="432" font-size="10" font-weight="600" text-anchor="middle">6. Báo lỗi &amp;</text>
  <text x="427" y="447" font-size="10" font-weight="600" text-anchor="middle">Yêu cầu nhập lại</text>

  <!-- Loopback Step 6 -> Step 3 -->
  <path d="M 375 435 L 365 435 L 365 170 L 415 170" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Branch Yes: Step 5 -> Step 7 (Straight Down X=545) -->
  <line x1="545" y1="405" x2="545" y2="495" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="555" y="425" font-size="10" font-weight="bold" fill="#000">Yes</text>

  <rect x="405" y="495" width="280" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="545" y="525" font-size="12" font-weight="600" text-anchor="middle">7. Chuyển trạng thái chiến dịch DANG_CHAY</text>


  <!-- ==================== COLUMN 3: REALTIME RULE ENGINE & CORE SERVICE ==================== -->
  <path d="M 180 285 L 180 570 L 745 570" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,4"/>
  <path d="M 545 545 L 545 570 L 745 570" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <rect x="745" y="545" width="330" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="910" y="575" font-size="12" font-weight="600" text-anchor="middle">8. Lắng nghe Event: ACCOUNT_ACTIVATED từ Bank</text>

  <line x1="840" y1="595" x2="840" y2="630" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <polygon points="840,630 940,670 840,710 740,670" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="840" y="663" font-size="11" font-weight="600" text-anchor="middle">9. Kiểm tra Kênh Bank &amp;</text>
  <text x="840" y="678" font-size="11" font-weight="600" text-anchor="middle">Trạng thái TKDT/TKNT?</text>

  <!-- Branch No: Step 9 -> Step 10 Box -->
  <line x1="940" y1="670" x2="970" y2="670" stroke="#000000" stroke-width="1.2"/>
  <line x1="970" y1="670" x2="970" y2="700" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="948" y="660" font-size="10" font-weight="bold" fill="#000">No</text>

  <rect x="940" y="700" width="150" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="1015" y="722" font-size="11" font-weight="600" text-anchor="middle">10. Ghi log lý do:</text>
  <text x="1015" y="737" font-size="11" font-weight="600" text-anchor="middle">Không đủ điều kiện</text>

  <line x1="1015" y1="750" x2="1015" y2="775" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <circle cx="1015" cy="790" r="12" fill="none" stroke="#000000" stroke-width="1.5"/>
  <circle cx="1015" cy="790" r="7" fill="#000000"/>

  <!-- Branch Yes: Step 9 -> Step 11 -->
  <line x1="840" y1="710" x2="840" y2="780" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="850" y="730" font-size="10" font-weight="bold" fill="#000">Yes</text>

  <polygon points="840,780 940,820 840,860 740,820" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="840" y="813" font-size="11" font-weight="600" text-anchor="middle">11. Kiểm tra Total Budget</text>
  <text x="840" y="828" font-size="11" font-weight="600" text-anchor="middle">Chiến dịch?</text>

  <!-- Branch Hết Budget: Step 11 -> Step 12 -->
  <line x1="940" y1="820" x2="970" y2="820" stroke="#000000" stroke-width="1.2"/>
  <line x1="970" y1="820" x2="970" y2="850" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="942" y="810" font-size="10" font-weight="bold" fill="#000">Hết Budget</text>

  <rect x="940" y="850" width="150" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="1015" y="872" font-size="11" font-weight="600" text-anchor="middle">12. Chuyển trạng thái:</text>
  <text x="1015" y="887" font-size="11" font-weight="600" text-anchor="middle">DA_HET_BUDGET</text>

  <line x1="1015" y1="900" x2="1015" y2="925" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <circle cx="1015" cy="940" r="12" fill="none" stroke="#000000" stroke-width="1.5"/>
  <circle cx="1015" cy="940" r="7" fill="#000000"/>

  <!-- Branch Còn Budget: Step 11 -> Step 13 -->
  <line x1="840" y1="860" x2="840" y2="930" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="850" y="880" font-size="10" font-weight="bold" fill="#000">Còn Budget</text>

  <polygon points="840,930 940,970 840,1010 740,970" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="840" y="963" font-size="11" font-weight="600" text-anchor="middle">13. Kiểm tra Hạn mức Ngày</text>
  <text x="840" y="978" font-size="11" font-weight="600" text-anchor="middle">(Daily Cap)?</text>

  <!-- Branch Vượt Daily Cap: Step 13 -> Step 14 (Off to Side X=1015) -->
  <line x1="940" y1="970" x2="1015" y2="970" stroke="#000000" stroke-width="1.2"/>
  <line x1="1015" y1="970" x2="1015" y2="1000" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="948" y="960" font-size="10" font-weight="bold" fill="#000">Vượt Cap</text>

  <!-- Step 14 Diamond -->
  <polygon points="1015,1000 1085,1035 1015,1070 945,1035" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="1015" y="1038" font-size="10" font-weight="600" text-anchor="middle">14. Check Policy?</text>

  <!-- Option A: Có bảo lưu -> Step 16 Box (Placed at X=930..1080, Y=1110 OFF THE MAIN AXIS!) -->
  <line x1="1015" y1="1070" x2="1015" y2="1110" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="1025" y="1085" font-size="10" font-weight="bold" fill="#000">Có bảo lưu</text>

  <!-- Step 16 Box (OFF MAIN AXIS, Placed at X=920..1080) -->
  <rect x="925" y="1110" width="160" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="1005" y="1132" font-size="10" font-weight="600" text-anchor="middle">16. Đưa vào Queue chờ</text>
  <text x="1005" y="1147" font-size="10" font-weight="bold" fill="#000">00:00:01 ngày sau</text>

  <!-- Arrow Step 16 -> Step 16b (Column 1) across horizontal line Y=1160 -->
  <path d="M 925 1160 L 330 1160" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Branch Còn Quota Ngày: Step 13 -> Step 17 (Straight Down Main Axis X=840 from Y=1010 to Y=1270, ZERO OBSTRUCTION!) -->
  <line x1="840" y1="1010" x2="840" y2="1270" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="850" y="1030" font-size="10" font-weight="bold" fill="#000">Còn Quota</text>

  <!-- Step 17 Box (Main Axis) -->
  <rect x="745" y="1270" width="330" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="910" y="1300" font-size="12" font-weight="600" text-anchor="middle">17. Atomic Lock: Trừ Quota &amp; Budget</text>

  <line x1="910" y1="1320" x2="910" y2="1360" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <rect x="745" y="1360" width="330" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="910" y="1390" font-size="12" font-weight="600" text-anchor="middle">18. Gọi API Core Ticketing sinh vé tự động</text>

  <line x1="840" y1="1410" x2="840" y2="1440" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <polygon points="840,1440 940,1480 840,1520 740,1480" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="840" y="1473" font-size="11" font-weight="600" text-anchor="middle">19. Kết quả phát vé</text>
  <text x="840" y="1488" font-size="11" font-weight="600" text-anchor="middle">từ Core?</text>

  <!-- Branch Fail / Timeout: Step 19 -> Step 20 Box (Off to Side X=1015, Y=1455..1505) -->
  <line x1="940" y1="1480" x2="970" y2="1480" stroke="#000000" stroke-width="1.2"/>
  <line x1="970" y1="1480" x2="970" y2="1510" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="942" y="1470" font-size="10" font-weight="bold" fill="#000">Fail / Timeout</text>

  <!-- Step 20 Box (Off Side X=930..1080) -->
  <rect x="930" y="1510" width="150" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="1005" y="1532" font-size="10" font-weight="600" text-anchor="middle">20. Retry Queue (Thử 3 lần)</text>
  <text x="1005" y="1547" font-size="10" font-weight="600" text-anchor="middle">Log PENDING_RETRY</text>

  <line x1="1005" y1="1560" x2="1005" y2="1585" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <circle cx="1005" cy="1600" r="12" fill="none" stroke="#000000" stroke-width="1.5"/>
  <circle cx="1005" cy="1600" r="7" fill="#000000"/>

  <!-- Branch Thành công: Step 19 -> Step 21 (Straight Down Main Axis X=840 from Y=1520 to Y=1560) -->
  <line x1="840" y1="1520" x2="840" y2="1560" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="850" y="1538" font-size="10" font-weight="bold" fill="#000">Thành công</text>

  <!-- Step 21 Box (Main Axis Y=1560) -->
  <rect x="745" y="1560" width="330" height="45" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="910" y="1587" font-size="12" font-weight="600" text-anchor="middle">21. Ghi Audit Log &amp; Update Dashboard</text>

  <line x1="840" y1="1605" x2="840" y2="1640" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Step 22 Box (Main Axis Y=1640) -->
  <rect x="745" y="1640" width="330" height="45" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="910" y="1667" font-size="12" font-weight="600" text-anchor="middle">22. Gửi lệnh thông báo SMS / Push Notification</text>

  <!-- Clean Horizontal Line from Step 22 (Col 3 Y=1662) -> Step 23 (Col 1 Y=1720) -->
  <path d="M 745 1662 L 180 1662 L 180 1695" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
</svg>'''
    return svg

if __name__ == "__main__":
    svg_data = generate_perfect_svg()
    
    # Update standalone SVG file
    svg_path = r"f:\VIETLOTT-SMS\00_Draft\activity_diagram_swimlane.svg"
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_data)
    print("Perfect SVG written successfully.")
