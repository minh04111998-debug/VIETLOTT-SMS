import base64
import zlib
import urllib.request
import re

mermaid_code_1 = """graph TD
    GD[Ban Giám Đốc<br><i>Quản trị & Vận hành toàn bộ công ty</i>]
    subgraph Khối Nghiệp Vụ & Kinh Doanh
        KD[Team Kinh Doanh & Sale<br><i>Business Requirements</i>]
        MKT[Team Marketing<br><i>Truyền thông & Marketing</i>]
        VHNV[Team Vận Hành Nghiệp Vụ<br><i>CSKH & Vận hành sản phẩm</i><br><b>Phó phòng: Anh Báo</b>]
    end
    subgraph Khối Kỹ Thuật & Công Nghệ
        KT_TEST[Team Kỹ Thuật & Tester<br><i>Phát triển sản phẩm</i><br><b>Trưởng phòng: Anh Thăng</b>]
        NOC1[Team Vận Hành Kỹ Thuật NOC 1<br><i>Trung tâm vận hành mạng số 1</i>]
        NOC2[Team NOC 2<br><i>Trung tâm vận hành mạng số 2</i>]
    end
    subgraph Khối Bảo Mật & Giám Sát
        BM[Team Bảo Mật<br><i>Triển khai giải pháp bảo mật</i>]
    end
    subgraph Khối Hỗ Trợ
        HCNS[Team Hành Chính Nhân Sự - HCNS<br><i>Hành chính & Nhân sự</i>]
    end
    GD --> KD
    GD --> MKT
    GD --> VHNV
    GD --> KT_TEST
    GD --> NOC1
    GD --> NOC2
    GD --> BM
    GD --> HCNS
    style GD fill:#f9f,stroke:#333,stroke-width:2px,color:#000
    style VHNV fill:#ff9,stroke:#f66,stroke-width:2px,color:#000
    style KT_TEST fill:#9f9,stroke:#33f,stroke-width:2px,color:#000
    style BM fill:#f99,stroke:#f33,stroke-width:2px,color:#000
"""

mermaid_code_2 = """sequenceDiagram
    autonumber
    actor Customer as Khách hàng
    participant KD as Team Kinh Doanh
    participant BA as Business Analyst
    participant KT as Team Kỹ Thuật (Anh Thăng)
    participant BM as Team Bảo Mật
    participant NOC as Team NOC 1/NOC 2
    participant VH as Team Vận Hành (Anh Báo)

    KD->>BA: Gửi Yêu cầu nghiệp vụ mới (Business Need)
    BA->>BA: Phân tích & Viết Đặc tả (SRS/User Story)
    BA->>KT: Chuyển giao tài liệu SRS để ước lượng (Estimation)
    KT->>BA: Phản hồi tính khả thi & giải pháp sơ bộ
    BA->>BM: Đánh giá an toàn thông tin (Security Review)
    BM-->>BA: Xác nhận phê duyệt bảo mật
    BA->>KD: Thống nhất tài liệu SRS cuối cùng
    KT->>NOC: Triển khai thử nghiệm (Staging) & Vận hành (Production)
    Customer->>VH: Gặp lỗi/khiếu nại khi sử dụng dịch vụ
    VH->>KT: Gửi ticket báo lỗi hệ thống cần sửa đổi
"""

def get_base64_data_uri(code):
    compressed = zlib.compress(code.encode('utf-8'), 9)
    encoded = base64.urlsafe_b64encode(compressed).decode('utf-8')
    url = f"https://kroki.io/mermaid/svg/{encoded}"
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            svg_data = response.read()
            b64_svg = base64.b64encode(svg_data).decode('utf-8')
            return f"data:image/svg+xml;base64,{b64_svg}"
    except Exception as e:
        print(f"Error calling kroki: {e}")
        return None

print("Rendering Diagram 1...")
b64_1 = get_base64_data_uri(mermaid_code_1)
print("Rendering Diagram 2...")
b64_2 = get_base64_data_uri(mermaid_code_2)

if b64_1 and b64_2:
    file_path = r'f:\VIETLOTT-SMS\00_Draft\company-organizational-structure.md'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Thay thế khối mã 1 bằng hình ảnh Base64
    pattern1 = r"(## 2\. Mô Hình Sơ Đồ Tổ Chức \(Organizational Structure Model\)\n\nDưới đây là sơ đồ tổ chức dạng cây phân cấp thể hiện mối quan hệ quản lý và chức năng của các phòng ban trong công ty\..*?\n\n)```mermaid.*?```"
    replacement1 = r"\1![Sơ đồ tổ chức công ty](" + b64_1 + r")"
    content = re.sub(pattern1, replacement1, content, flags=re.DOTALL)
    
    # Thay thế khối mã 2
    pattern2 = r"(## 5\. Đề Xuất Quy Trình Phối Hợp Nghiệp Vụ \(Proposed Collaboration Flow\)\n\nDưới đây là luồng thông tin cơ bản giữa các bộ phận khi phát sinh một yêu cầu nghiệp vụ mới cho sản phẩm \*\*VIETLOTT-SMS\*\*:\n\n)```mermaid.*?```"
    replacement2 = r"\1![Sơ đồ luồng nghiệp vụ](" + b64_2 + r")"
    content = re.sub(pattern2, replacement2, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Updated the markdown file with base64 embedded images.")
else:
    print("FAILED: Could not generate SVG base64 strings.")
