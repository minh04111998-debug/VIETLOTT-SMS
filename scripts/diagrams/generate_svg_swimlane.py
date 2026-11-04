import os
import re

def build_inline_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 1920" width="100%" height="auto" style="background-color: #ffffff; font-family: 'Inter', sans-serif;">
  <defs>
    <!-- Graph Paper Grid Pattern -->
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#e2e8f0" stroke-width="0.8"/>
    </pattern>
    <!-- Arrow Marker -->
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000"/>
    </marker>
  </defs>

  <!-- Background Grid -->
  <rect width="1100" height="1920" fill="url(#grid)" />

  <!-- Top Title Header -->
  <rect x="0" y="0" width="1100" height="40" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
  <text x="550" y="26" font-weight="bold" font-size="15" text-anchor="middle" fill="#000000">Luồng Hoạt Động Tặng Vé Mở Tài Khoản Kênh Bank (UML Swimlane Diagram)</text>

  <!-- Column Headers -->
  <g font-weight="bold" font-size="14" text-anchor="middle">
    <!-- Header 1 -->
    <rect x="0" y="40" width="360" height="40" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
    <text x="180" y="65">Khách hàng &amp; Kênh Bank</text>

    <!-- Header 2 -->
    <rect x="360" y="40" width="370" height="40" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
    <text x="545" y="65">Web Admin Vietlott SMS</text>

    <!-- Header 3 -->
    <rect x="730" y="40" width="370" height="40" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
    <text x="915" y="65">Hệ thống Realtime Rule Engine &amp; Core Service</text>
  </g>

  <!-- Swimlane Vertical Dividers -->
  <line x1="360" y1="40" x2="360" y2="1920" stroke="#000000" stroke-width="1.5"/>
  <line x1="730" y1="40" x2="730" y2="1920" stroke="#000000" stroke-width="1.5"/>

  <!-- ==================== COLUMN 1: KHÁCH HÀNG & KÊNH BANK ==================== -->
  <!-- Start Node -->
  <circle cx="180" cy="110" r="12" fill="#000000"/>

  <!-- Arrow Start -> Step 1 -->
  <line x1="180" y1="122" x2="180" y2="150" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Step 1 Box -->
  <rect x="50" y="150" width="260" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="180" y="180" font-size="12" font-weight="600" text-anchor="middle">1. Đăng ký mở tài khoản mới qua kênh Bank</text>

  <!-- Arrow Step 1 -> Step 2 -->
  <line x1="180" y1="200" x2="180" y2="240" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Step 2 Box -->
  <rect x="40" y="240" width="280" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="180" y="270" font-size="12" font-weight="600" text-anchor="middle">2. Thực hiện eKYC / Active tài khoản / Thanh toán</text>


  <!-- ==================== COLUMN 2: WEB ADMIN VIETLOTT SMS ==================== -->
  <!-- Step 3 Box -->
  <rect x="415" y="150" width="260" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="545" y="180" font-size="12" font-weight="600" text-anchor="middle">3. Admin thiết lập cụm 7 điều kiện chiến dịch</text>

  <!-- Arrow Step 3 -> Step 4 -->
  <line x1="545" y1="200" x2="545" y2="240" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Step 4 Box -->
  <rect x="415" y="240" width="260" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="545" y="270" font-size="12" font-weight="600" text-anchor="middle">4. Nhấn 'Lưu &amp; Kích hoạt' chiến dịch</text>

  <!-- Arrow Step 4 -> Step 5 Diamond -->
  <line x1="545" y1="290" x2="545" y2="330" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Step 5 Decision Diamond -->
  <polygon points="545,330 655,370 545,410 435,370" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="545" y="365" font-size="11" font-weight="600" text-anchor="middle">5. Kiểm tra thông tin</text>
  <text x="545" y="380" font-size="11" font-weight="600" text-anchor="middle">cấu hình hợp lệ?</text>

  <!-- Branch No: Step 5 -> Step 6 -->
  <line x1="435" y1="370" x2="390" y2="370" stroke="#000000" stroke-width="1.2"/>
  <line x1="390" y1="370" x2="390" y2="450" stroke="#000000" stroke-width="1.2"/>
  <line x1="390" y1="450" x2="415" y2="450" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="410" y="362" font-size="10" font-weight="bold" fill="#000">No</text>

  <!-- Step 6 Box (Báo lỗi) -->
  <rect x="415" y="425" width="260" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="545" y="455" font-size="12" font-weight="600" text-anchor="middle">6. Báo lỗi &amp; Yêu cầu nhập lại</text>

  <!-- Loopback Step 6 -> Step 3 -->
  <path d="M 675 450 L 700 450 L 700 175 L 675 175" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Branch Yes: Step 5 -> Step 7 -->
  <line x1="545" y1="410" x2="545" y2="510" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="555" y="430" font-size="10" font-weight="bold" fill="#000">Yes</text>

  <!-- Step 7 Box -->
  <rect x="405" y="510" width="280" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="545" y="540" font-size="12" font-weight="600" text-anchor="middle">7. Chuyển trạng thái chiến dịch DANG_CHAY</text>


  <!-- ==================== COLUMN 3: REALTIME RULE ENGINE & CORE SERVICE ==================== -->
  <!-- Event Arrow Step 2 & Step 7 -> Step 8 -->
  <path d="M 180 290 L 180 595 L 755 595" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,4"/>
  <path d="M 545 560 L 545 595 L 755 595" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Step 8 Box -->
  <rect x="755" y="570" width="320" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="915" y="600" font-size="12" font-weight="600" text-anchor="middle">8. Lắng nghe Event: ACCOUNT_ACTIVATED từ Bank</text>

  <!-- Arrow Step 8 -> Step 9 Diamond -->
  <line x1="915" y1="620" x2="915" y2="660" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Step 9 Decision Diamond -->
  <polygon points="915,660 1040,705 915,750 790,705" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="915" y="698" font-size="11" font-weight="600" text-anchor="middle">9. Kiểm tra Kênh Bank &amp;</text>
  <text x="915" y="714" font-size="11" font-weight="600" text-anchor="middle">Trạng thái TKDT/TKNT?</text>

  <!-- Branch No: Step 9 -> Step 10 -->
  <line x1="1040" y1="705" x2="1060" y2="705" stroke="#000000" stroke-width="1.2"/>
  <line x1="1060" y1="705" x2="1060" y2="790" stroke="#000000" stroke-width="1.2"/>
  <line x1="1060" y1="790" x2="1040" y2="790" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="1045" y="695" font-size="10" font-weight="bold" fill="#000">No</text>

  <!-- Step 10 Box -->
  <rect x="765" y="765" width="270" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="900" y="795" font-size="12" font-weight="600" text-anchor="middle">10. Ghi log lý do: Không đủ điều kiện</text>

  <!-- End Node Step 10 -->
  <line x1="900" y1="815" x2="900" y2="840" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <circle cx="900" cy="855" r="12" fill="#none" stroke="#000000" stroke-width="1.5"/>
  <circle cx="900" cy="855" r="7" fill="#000000"/>

  <!-- Branch Yes: Step 9 -> Step 11 Diamond -->
  <line x1="915" y1="750" x2="915" y2="890" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="925" y="770" font-size="10" font-weight="bold" fill="#000">Yes</text>

  <!-- Step 11 Decision Diamond -->
  <polygon points="915,890 1040,935 915,980 790,935" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="915" y="930" font-size="11" font-weight="600" text-anchor="middle">11. Kiểm tra Total Budget</text>
  <text x="915" y="945" font-size="11" font-weight="600" text-anchor="middle">Chiến dịch?</text>

  <!-- Branch Hết Budget: Step 11 -> Step 12 -->
  <line x1="1040" y1="935" x2="1060" y2="935" stroke="#000000" stroke-width="1.2"/>
  <line x1="1060" y1="935" x2="1060" y2="1020" stroke="#000000" stroke-width="1.2"/>
  <line x1="1060" y1="1020" x2="1040" y2="1020" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="1045" y="925" font-size="10" font-weight="bold" fill="#000">Hết Budget</text>

  <!-- Step 12 Box -->
  <rect x="765" y="995" width="270" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="900" y="1025" font-size="12" font-weight="600" text-anchor="middle">12. Chuyển trạng thái: DA_HET_BUDGET</text>

  <!-- End Node Step 12 -->
  <line x1="900" y1="1045" x2="900" y2="1070" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <circle cx="900" cy="1085" r="12" fill="#none" stroke="#000000" stroke-width="1.5"/>
  <circle cx="900" cy="1085" r="7" fill="#000000"/>

  <!-- Branch Còn Budget: Step 11 -> Step 13 Diamond -->
  <line x1="915" y1="980" x2="915" y2="1120" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="925" y="1000" font-size="10" font-weight="bold" fill="#000">Còn Budget</text>

  <!-- Step 13 Decision Diamond -->
  <polygon points="915,1120 1040,1165 915,1210 790,1165" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="915" y="1160" font-size="11" font-weight="600" text-anchor="middle">13. Kiểm tra Hạn mức Ngày</text>
  <text x="915" y="1175" font-size="11" font-weight="600" text-anchor="middle">(Daily Cap)?</text>

  <!-- Branch Vượt Daily Cap: Step 13 -> Step 14 Diamond -->
  <line x1="1040" y1="1165" x2="1065" y2="1165" stroke="#000000" stroke-width="1.2"/>
  <line x1="1065" y1="1165" x2="1065" y2="1240" stroke="#000000" stroke-width="1.2"/>
  <line x1="1065" y1="1240" x2="1040" y2="1240" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="1042" y="1155" font-size="10" font-weight="bold" fill="#000">Vượt Cap</text>

  <!-- Step 14 Decision Diamond (Check Policy) -->
  <polygon points="915,1220 1040,1255 915,1290 790,1255" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="915" y="1259" font-size="11" font-weight="600" text-anchor="middle">14. Check Policy Bảo lưu?</text>

  <!-- Option A: Có bảo lưu -> Step 16 Queue Box -->
  <line x1="915" y1="1290" x2="915" y2="1330" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="925" y="1305" font-size="10" font-weight="bold" fill="#000">Có bảo lưu</text>

  <!-- Step 16 Box -->
  <rect x="755" y="1330" width="320" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="915" y="1360" font-size="12" font-weight="600" text-anchor="middle">16. Đưa vào Queue chờ 00:00:01 ngày sau</text>

  <!-- Arrow Step 16 -> Step 11b (Column 1) -->
  <path d="M 755 1355 L 180 1355 L 180 1410" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Step 11b Box (Col 1) -->
  <rect x="30" y="1410" width="300" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="180" y="1433" font-size="11" font-weight="600" text-anchor="middle">11b. Nhận thông báo suất tặng vé</text>
  <text x="180" y="1448" font-size="11" font-weight="600" text-anchor="middle">được bảo lưu sang ngày sau</text>

  <!-- End Node Step 11b -->
  <line x1="180" y1="1460" x2="180" y2="1490" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <circle cx="180" cy="1505" r="12" fill="#none" stroke="#000000" stroke-width="1.5"/>
  <circle cx="180" cy="1505" r="7" fill="#000000"/>

  <!-- Branch Còn Quota Ngày: Step 13 -> Step 17 Box -->
  <line x1="790" y1="1165" x2="745" y2="1165" stroke="#000000" stroke-width="1.2"/>
  <line x1="745" y1="1165" x2="745" y2="1525" stroke="#000000" stroke-width="1.2"/>
  <line x1="745" y1="1525" x2="765" y2="1525" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="740" y="1155" font-size="10" font-weight="bold" fill="#000">Còn Quota</text>

  <!-- Step 17 Box -->
  <rect x="765" y="1500" width="310" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="920" y="1530" font-size="12" font-weight="600" text-anchor="middle">17. Atomic Lock: Trừ Quota &amp; Budget</text>

  <!-- Arrow Step 17 -> Step 18 -->
  <line x1="920" y1="1550" x2="920" y2="1590" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Step 18 Box -->
  <rect x="765" y="1590" width="310" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="920" y="1620" font-size="12" font-weight="600" text-anchor="middle">18. Gọi API Core Ticketing sinh vé tự động</text>

  <!-- Arrow Step 18 -> Step 19 Diamond -->
  <line x1="920" y1="1640" x2="920" y2="1670" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Step 19 Decision Diamond -->
  <polygon points="920,1670 1045,1705 920,1740 795,1705" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="920" y="1700" font-size="11" font-weight="600" text-anchor="middle">19. Kết quả phát vé</text>
  <text x="920" y="1715" font-size="11" font-weight="600" text-anchor="middle">từ Core?</text>

  <!-- Branch Thành công: Step 19 -> Step 21 -->
  <line x1="920" y1="1740" x2="920" y2="1780" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="930" y="1758" font-size="10" font-weight="bold" fill="#000">Thành công</text>

  <!-- Step 21 Box -->
  <rect x="765" y="1780" width="310" height="45" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="920" y="1807" font-size="12" font-weight="600" text-anchor="middle">21. Ghi Audit Log &amp; Update Dashboard</text>

  <!-- Arrow Step 21 -> Step 22 -->
  <line x1="920" y1="1825" x2="920" y2="1855" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Step 22 Box -->
  <rect x="765" y="1855" width="310" height="45" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="920" y="1882" font-size="12" font-weight="600" text-anchor="middle">22. Gửi lệnh thông báo SMS / Push Notification</text>

  <!-- Arrow Step 22 -> Step 9 (Col 1) -->
  <path d="M 765 1877 L 180 1877 L 180 1675" fill="none" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Step 9 Box (Col 1) -->
  <rect x="30" y="1625" width="300" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2"/>
  <text x="180" y="1648" font-size="11" font-weight="600" text-anchor="middle">9. Nhận SMS / Push Noti vé tặng</text>
  <text x="180" y="1663" font-size="11" font-weight="600" text-anchor="middle">&amp; Tra cứu vé trên App</text>

  <!-- End Node Step 9 -->
  <line x1="180" y1="1625" x2="180" y2="1590" stroke="#000000" stroke-width="1.2"/>
  <line x1="180" y1="1590" x2="180" y2="1575" stroke="#000000" stroke-width="1.2" marker-end="url(#arrow)"/>
  <circle cx="180" cy="1560" r="12" fill="#none" stroke="#000000" stroke-width="1.5"/>
  <circle cx="180" cy="1560" r="7" fill="#000000"/>
</svg>'''
    return svg

if __name__ == "__main__":
    svg_content = build_inline_svg()
    
    # Write SVG to standalone file 00_Draft/activity_diagram_swimlane.svg
    svg_file_path = r"f:\VIETLOTT-SMS\00_Draft\activity_diagram_swimlane.svg"
    with open(svg_file_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Standalone SVG generated successfully.")
