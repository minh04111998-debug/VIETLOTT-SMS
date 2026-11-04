import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def build_perfect_excel(output_path):
    wb = openpyxl.Workbook()
    wb.remove(wb.active)  # Remove default blank sheet

    # ARGB Color Palette (100% Solid Opacity with FF prefix)
    c_banner_fill = "FFD9E1F2"    # Ice Blue for Top Banner
    c_banner_text = "FF002060"    # Deep Navy for Title
    c_hdr_fill = "FF1F4E78"       # Steel Navy for Table Headers
    c_hdr_text = "FFFFFFFF"       # Solid White for Table Headers
    c_hdr_alt_fill = "FF2F5597"   # Secondary Blue for Tables
    c_row_alt = "FFF2F4F8"        # Very light clean gray/blue for alternating rows
    c_white = "FFFFFFFF"          # Solid White
    c_text_dark = "FF000000"      # Pure Black for maximum contrast
    c_border = "FFB0C4DE"         # Steel Border

    # Fonts
    font_banner = Font(name="Segoe UI", size=14, bold=True, color=c_banner_text)
    font_tbl_hdr = Font(name="Segoe UI", size=11, bold=True, color=c_hdr_text)
    font_row_bold = Font(name="Segoe UI", size=10, bold=True, color=c_text_dark)
    font_row_regular = Font(name="Segoe UI", size=10, color=c_text_dark)

    # Fills
    fill_banner = PatternFill(start_color=c_banner_fill, end_color=c_banner_fill, fill_type="solid")
    fill_tbl_hdr = PatternFill(start_color=c_hdr_fill, end_color=c_hdr_fill, fill_type="solid")
    fill_tbl_hdr_alt = PatternFill(start_color=c_hdr_alt_fill, end_color=c_hdr_alt_fill, fill_type="solid")
    fill_alt = PatternFill(start_color=c_row_alt, end_color=c_row_alt, fill_type="solid")
    fill_white = PatternFill(start_color=c_white, end_color=c_white, fill_type="solid")

    # Borders
    border_side = Side(border_style="thin", color=c_border)
    border_all = Border(left=border_side, right=border_side, top=border_side, bottom=border_side)
    border_banner = Border(
        left=border_side, right=border_side,
        top=Side(border_style="medium", color=c_banner_text),
        bottom=Side(border_style="medium", color=c_banner_text)
    )

    align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
    align_left = Alignment(horizontal="left", vertical="center", wrap_text=True)
    align_top_left = Alignment(horizontal="left", vertical="top", wrap_text=True)
    align_top_center = Alignment(horizontal="center", vertical="top", wrap_text=True)

    # ====================================================
    # SHEET 1: TỔNG QUAN KHÓA HỌC
    # ====================================================
    ws1 = wb.create_sheet(title="1. Tong_Quan_Khoa_Hoc")
    ws1.views.sheetView[0].showGridLines = True
    ws1.freeze_panes = "A4"

    # Dòng 1: Tiêu đề Sheet (Banner)
    ws1.merge_cells("A1:D1")
    t1 = ws1["A1"]
    t1.value = "THÔNG TIN KHÓA HỌC: AI AGENT ENGINEERING (MENTORA x PROTONX)"
    t1.font = font_banner
    t1.fill = fill_banner
    t1.alignment = align_center
    t1.border = border_banner
    ws1.row_dimensions[1].height = 36

    # Dòng 2: Phân cách
    ws1.row_dimensions[2].height = 8

    # Dòng 3: Dòng tiêu đề các cột của Bảng
    ws1.cell(row=3, column=1, value="HẠNG MỤC THÔNG TIN").font = font_tbl_hdr
    ws1.cell(row=3, column=1).fill = fill_tbl_hdr
    ws1.cell(row=3, column=1).alignment = align_center
    ws1.cell(row=3, column=1).border = border_all

    ws1.cell(row=3, column=2, value="NỘI DUNG CHI TIẾT").font = font_tbl_hdr
    ws1.cell(row=3, column=2).fill = fill_tbl_hdr
    ws1.cell(row=3, column=2).alignment = align_left
    ws1.cell(row=3, column=2).border = border_all
    ws1.merge_cells("B3:D3")
    ws1.row_dimensions[3].height = 28

    overview_data = [
        ("Tên khóa học", "AI Agent Engineering"),
        ("Đơn vị tổ chức", "Mentora (Trực thuộc Công ty TNHH VTI Education)"),
        ("Giảng viên / Mentor", "Nguyễn Bá Ngọc — Founder & CEO ProtonX, Google Developer Expert (GDE) Machine Learning đầu tiên tại Việt Nam"),
        ("Mô hình trọng tâm", "Mô hình 7 AI Harnesses (Context, Tool, Orchestration, Evaluation, Security, Governance, AgentOps)"),
        ("Thời lượng đào tạo", "14 buổi trực tiếp (~28 giờ học)"),
        ("Lịch học dự kiến", "Thứ 4 & Thứ 6 (19h30 - 21h30)"),
        ("Khai giảng", "04/11/2026"),
        ("Học phí niêm yết", "5.000.000 VNĐ (Chính sách ưu đãi theo gói hội viên Mentora Plus)"),
        ("Đối tượng mục tiêu", "AI Engineers, Solution Architects, Data Professionals, Tech Leads, AI Product Owners, Technical BAs"),
        ("Yêu cầu đầu vào", "Biết một ngôn ngữ lập trình cơ bản hoặc có kỹ năng 'Vibe Coding' (sử dụng AI coding assistants như Claude Code, Cursor)"),
        ("Mục tiêu đầu ra", "Tự tin thiết kế, phát triển, đánh giá, bảo mật và vận hành hệ thống Enterprise AI Agent Platform sẵn sàng cho môi trường Production ở quy mô lớn.")
    ]

    curr_row = 4
    for idx, (cat, val) in enumerate(overview_data):
        c1 = ws1.cell(row=curr_row, column=1, value=cat)
        c2 = ws1.cell(row=curr_row, column=2, value=val)
        ws1.merge_cells(start_row=curr_row, start_column=2, end_row=curr_row, end_column=4)
        
        c1.font = font_row_bold
        c2.font = font_row_regular
        c1.alignment = align_top_left
        c2.alignment = align_top_left
        
        row_fill = fill_alt if idx % 2 == 1 else fill_white
        c1.fill = row_fill
        c2.fill = row_fill
        
        for col_idx in range(1, 5):
            ws1.cell(row=curr_row, column=col_idx).border = border_all
            
        ws1.row_dimensions[curr_row].height = 28 if len(val) < 80 else 46
        curr_row += 1

    ws1.column_dimensions["A"].width = 25
    ws1.column_dimensions["B"].width = 35
    ws1.column_dimensions["C"].width = 35
    ws1.column_dimensions["D"].width = 35

    # ====================================================
    # SHEET 2: CHI TIẾT 14 BUỔI HỌC (SYLLABUS)
    # ====================================================
    ws2 = wb.create_sheet(title="2. Chi_Tiet_14_Buoi_Hoc")
    ws2.views.sheetView[0].showGridLines = True
    ws2.freeze_panes = "A4"

    # Dòng 1: Tiêu đề Sheet (Banner)
    ws2.merge_cells("A1:G1")
    t2 = ws2["A1"]
    t2.value = "KHUNG CHƯƠNG TRÌNH CHI TIẾT 14 BUỔI HỌC — AI AGENT ENGINEERING"
    t2.font = font_banner
    t2.fill = fill_banner
    t2.alignment = align_center
    t2.border = border_banner
    ws2.row_dimensions[1].height = 36

    # Dòng 2: Phân cách
    ws2.row_dimensions[2].height = 8

    # Dòng 3: Dòng Tiêu đề các Cột của Bảng
    headers_ws2 = [
        ("STT", 8),
        ("Tên Buổi Học", 32),
        ("Trụ Cột Harness", 22),
        ("Nội Dung Chi Tiết (Topics)", 46),
        ("Bài Lab / Thực Hành", 30),
        ("Tech Stack / Công Cụ", 25),
        ("Góc Nhìn Ứng Dụng Cho BA / PO", 45)
    ]

    for col_idx, (hdr, width) in enumerate(headers_ws2, start=1):
        cell = ws2.cell(row=3, column=col_idx, value=hdr)
        cell.font = font_tbl_hdr
        cell.fill = fill_tbl_hdr
        cell.alignment = align_center
        cell.border = border_all
        ws2.column_dimensions[get_column_letter(col_idx)].width = width
    ws2.row_dimensions[3].height = 32

    sessions = [
        (
            1,
            "Buổi 1: Nền tảng Agentic AI + Framework Harness",
            "Foundation & Overview",
            "• LLM Fundamentals\n• Transformer & Attention Mechanism\n• Prompt Engineering nâng cao\n• Khái niệm Tool Calling\n• MCP (Model Context Protocol)\n• Tổng quan AI Agent Landscape",
            "Ví dụ điển hình về Agentic: Claude Code",
            "LLMs, MCP, Claude Code, Anthropic Tools",
            "Hiểu hệ sinh thái Agentic AI, nguyên lý Tool Calling & giao thức MCP để chuẩn bị thiết kế hệ thống tương tác giữa AI và phần mềm doanh nghiệp."
        ),
        (
            2,
            "Buổi 2: Context Harness - Nền tảng RAG",
            "Context Harness",
            "• Context Harness Overview\n• RAG Architecture chuẩn Enterprise\n• Chunking Strategies (kỹ thuật phân mảnh dữ liệu)\n• Embedding Models\n• Reranking tối ưu độ chính xác\n• Hybrid Search (kết hợp Dense & Sparse)\n• Agent Memory (Short-term & Long-term)\n• Context Compression & Long Context Optimization",
            "• Xây dựng Enterprise RAG\n• Multi-source Knowledge Base (tích hợp đa nguồn)",
            "Vector Database, Embedding Models, Reranker, Hybrid Search",
            "Đặc tả kiến trúc tri thức (Knowledge Architecture Spec): Phân loại nguồn tài liệu, quy định chiến lược chunking theo nghiệp vụ, cấu hình Agent Memory tránh tràn ngữ cảnh."
        ),
        (
            3,
            "Buổi 3: [Bổ trợ] Docker + Cloud",
            "Infrastructure & DevOps",
            "• Khái niệm Docker & ảo hóa container\n• Phân biệt Docker Image và Container\n• Hướng dẫn cài đặt Docker\n• Xây dựng Docker Image và chạy Docker Container\n• Kiến trúc triển khai trên môi trường Cloud",
            "Thực hành đóng gói hệ thống Agent vào Docker Container và triển khai Cloud",
            "Docker, Containerization, Cloud Providers (AWS/GCP)",
            "Hiểu quy trình đóng gói phần mềm và môi trường vận hành hạ tầng; phối hợp hiệu quả với DevOps/Infra team khi triển khai giải pháp Agent vào production."
        ),
        (
            4,
            "Buổi 4: [Live] Context Harness - Thực hành lập trình",
            "Context & Agent Core",
            "• Lập trình reasoning (cơ chế suy luận đa bước)\n• Lập trình gọi tools (tool invocation)\n• Lập trình truy xuất memory (đọc/ghi bộ nhớ ngữ cảnh)",
            "Thực hành lập trình hoàn chỉnh 1 Agent tự trị có memory và công cụ",
            "Python, LLM Function Calling, Memory Stores",
            "Đọc hiểu luồng dữ liệu (Data Flow) thực thi của Agent; thẩm định tính khả thi kỹ thuật của các kịch bản nghiệp vụ phức tạp."
        ),
        (
            5,
            "Buổi 5: Tool Harness",
            "Tool Harness",
            "• Bản chất Tool Harness trong doanh nghiệp\n• Function Calling & Schema Definitions\n• Xây dựng MCP Servers\n• API Privilege Design (phân quyền API)\n• Retry Mechanisms (cơ chế thử lại khi lỗi)\n• Error Recovery (tự phục hồi lỗi)\n• Audit Logging Integration\n• Tool Registry & Least Privilege (quyền tối thiểu)",
            "• CRM Agent\n• ERP Agent\n• Database Agent",
            "MCP Protocol, REST APIs, SQL/NoSQL Connectors, Audit Logs",
            "Thiết kế Danh mục công cụ (Tool Registry) & Interface Specs: Quy định API nào Agent được gọi, gán nhãn rủi ro (Read vs Write/Delete), thiết lập cơ chế kiểm toán và quyền tối thiểu."
        ),
        (
            6,
            "Buổi 6: Bài tập lớn 1 - Lập trình Drive Agent",
            "Tool & Data Integration",
            "• Chi tiết yêu cầu bài tập lớn 1\n• Hướng dẫn kết nối Google Drive API\n• Thiết kế schema cho thao tác tệp (tìm kiếm, đọc, tạo, phân quyền)",
            "Lập trình Drive Agent tự động quản lý và tra cứu tài liệu trên Google Drive",
            "Google Drive API, OAuth2 / Service Account, Tool Calling",
            "Thực hành đóng vai PO kiểm thử nghiệm thu (UAT) một Agent tích hợp dịch vụ lưu trữ bên thứ ba; viết User Stories và kịch bản tương tác tệp tin."
        ),
        (
            7,
            "Buổi 7: Orchestration Harness",
            "Orchestration Harness",
            "• Tổng quan Orchestration Harness\n• Agent Planning & Decomposition\n• DAG Workflows (đồ thị có hướng không chu trình)\n• State Machines (máy trạng thái)\n• Framework LangGraph\n• Multi-Agent Systems & Handoff Protocols\n• Routing Strategies (chiến lược điều phối)\n• Fallback Models & Parallel Execution",
            "• Research Agent (Tác nhân nghiên cứu)\n• Customer Service Agent (Tác nhân CSKH)",
            "LangGraph, State Graph, Multi-Agent Handoff, Fallback Routing",
            "Thiết kế luồng phối hợp đa tác nhân (Multi-Agent Blueprints): Xây dựng sơ đồ State Machine, phân định vai trò từng Agent, quy tắc định tuyến (Routing) và kịch bản dự phòng khi AI bị kẹt."
        ),
        (
            8,
            "Buổi 8: Evaluation Harness",
            "Evaluation Harness",
            "• Khái niệm Evaluation Harness\n• Xây dựng Golden Datasets (bộ kiểm thử chuẩn)\n• Phương pháp LLM-as-a-Judge\n• Tích hợp Human Feedback\n• A/B Testing cho mô hình AI\n• Regression Testing (kiểm thử hồi quy tự động)\n• RAG Evaluation (đo lường độ chính xác RAG)\n• Hallucination Detection (phát hiện ảo giác)",
            "Xây dựng Evaluation Pipeline tự động chấm điểm chất lượng Agent",
            "Golden Datasets, LLM-as-a-Judge, Ragas, DeepEval, Regression Suites",
            "Acceptance Criteria (AC) thế hệ mới: Thiết lập bộ dữ liệu chuẩn (Golden Dataset), tiêu chí đánh giá (Rubric) về ảo giác và độ chính xác để nghiệm thu hệ thống trước khi Go-live."
        ),
        (
            9,
            "Buổi 9: Security Harness",
            "Security Harness",
            "• Rủi ro an toàn trong hệ thống AI Agent\n• Kỹ thuật tấn công Prompt Injection\n• Cơ chế phòng thủ Jailbreak Defense\n• Data Leakage Prevention (chống lộ dữ liệu)\n• PII Protection (bảo vệ thông tin định danh)\n• Access Control & Credential Management\n• Secure Tool Access",
            "Thực hành Attack & Defend (Tấn công và thiết lập phòng thủ cho AI Agent)",
            "Security Guardrails, PII Filters (NĐ 13), Secret Scanners, OWASP Top 10",
            "Viết Yêu cầu phi chức năng (NFR) về bảo mật và tuân thủ: Chống rò rỉ dữ liệu cá nhân (CCCD, SĐT, tài khoản ngân hàng), cơ chế phân quyền truy cập và kiểm soát rủi ro bảo mật."
        ),
        (
            10,
            "Buổi 10: Governance Harness",
            "Governance Harness",
            "• Khung quản trị Governance Harness\n• Audit Trail (ghi vết kiểm toán đầy đủ)\n• Explainability (tính giải trình quyết định của AI)\n• Approval Workflows (luồng phê duyệt)\n• Human-in-the-loop (con người can thiệp)\n• AI Policies & Risk Management\n• Compliance Frameworks",
            "Xây dựng AI Governance Dashboard giám sát tuân thủ",
            "Audit Logging, Approval Gateways, Human-in-the-loop UI, Compliance Matrix",
            "Thiết kế Ma trận phê duyệt & Điểm chặn (Human-in-the-loop): Xác định hành động AI được tự quyết, hành động BẮT BUỘC con người ký duyệt (Hard Stop) và lưu vết pháp lý."
        ),
        (
            11,
            "Buổi 11: AgentOps Harness",
            "AgentOps Harness",
            "• Vận hành AgentOps trong doanh nghiệp\n• Monitoring (giám sát trạng thái hoạt động)\n• Tracing (truy vết từng bước suy luận / tool call)\n• Cost Tracking (theo dõi chi phí token theo request)\n• Latency Optimization (tối ưu độ trễ)\n• Accuracy Metrics theo thời gian\n• Drift Detection (phát hiện độ lệch chất lượng)\n• Giới thiệu Observability Tools",
            "Cài đặt và cấu hình công cụ giám sát, tracing Agent (LangSmith, Phoenix)",
            "LangSmith, OpenTelemetry, Arize Phoenix, Datadog",
            "Quản trị hiệu quả kinh tế (Unit Economics): Theo dõi chi phí token trên từng transaction, độ trễ SLA, phát hiện suy giảm chất lượng câu trả lời để tính toán bài toán ROI sản phẩm."
        ),
        (
            12,
            "Buổi 12: Project cuối khóa - Enterprise Platform",
            "Capstone Project (Architecture)",
            "• Thiết kế kiến trúc hoàn chỉnh cho Enterprise AI Agent Platform:\n  1. Knowledge Base\n  2. RAG Pipeline\n  3. AI Agents\n  4. Tool Calling\n  5. Workflow Engine\n  6. Evaluation System\n  7. Security Layer\n  8. Governance Layer\n  9. Monitoring Layer",
            "Khởi tạo kiến trúc đồ án tích hợp đầy đủ 7 Harnesses",
            "Enterprise Multi-Agent Architecture, Full-stack Harness Integration",
            "Đóng vai trò Product Lead / Solution Architect: Tổng hợp toàn bộ tài liệu PRD/SRS kiến trúc hệ thống, phân rã backlog và điều phối phạm vi dự án."
        ),
        (
            13,
            "Buổi 13: Dự án cuối khóa - Implementation",
            "Capstone Project (Implementation)",
            "• Chi tiết hướng dẫn bài tập lớn và đồ án\n• Phân tích các dự án mẫu (tham khảo)\n• Mentor giải đáp thắc mắc, tháo gỡ lỗi kỹ thuật\n• Tích hợp các lớp bảo vệ và đo lường",
            "Hoàn thiện code, kết nối dữ liệu thực tế và chạy kiểm thử toàn diện đồ án",
            "End-to-end Testing, System Hardening, Evaluation Run",
            "Nghiệm thu tính năng (UAT), chạy bộ Golden Dataset kiểm thử hồi quy hệ thống và chuẩn bị tài liệu báo cáo sản phẩm."
        ),
        (
            14,
            "Buổi 14: Trình diễn dự án cuối khóa",
            "Capstone Defense & Review",
            "• Trình diễn hệ thống thực tế (Live Demo)\n• Báo cáo kết quả đánh giá (Evaluation Report)\n• Bảo vệ giải pháp kiến trúc trước Mentor và Hội đồng chuyên gia\n• Nhận phản hồi chuyên môn và định hướng phát triển",
            "Thuyết trình và bảo vệ đồ án Enterprise AI Agent Platform",
            "Live Presentation, Executive Demo, Defense Rubric",
            "Kỹ năng Product Pitching & Executive Presentation: Thuyết trình giá trị kinh doanh, kiến trúc giải pháp, ranh giới an toàn và bài toán ROI trước các bên liên quan (Stakeholders)."
        )
    ]

    for sess in sessions:
        stt, name, harness, topics, lab, tech, bapo = sess
        r = ws2.max_row + 1
        ws2.row_dimensions[r].height = 90
        
        c_stt = ws2.cell(row=r, column=1, value=stt)
        c_name = ws2.cell(row=r, column=2, value=name)
        c_harness = ws2.cell(row=r, column=3, value=harness)
        c_topics = ws2.cell(row=r, column=4, value=topics)
        c_lab = ws2.cell(row=r, column=5, value=lab)
        c_tech = ws2.cell(row=r, column=6, value=tech)
        c_bapo = ws2.cell(row=r, column=7, value=bapo)

        c_stt.alignment = align_top_center
        c_stt.font = font_row_bold
        c_name.alignment = align_top_left
        c_name.font = font_row_bold
        c_harness.alignment = align_top_left
        c_harness.font = font_row_bold
        c_topics.alignment = align_top_left
        c_topics.font = font_row_regular
        c_lab.alignment = align_top_left
        c_lab.font = font_row_regular
        c_tech.alignment = align_top_left
        c_tech.font = font_row_regular
        c_bapo.alignment = align_top_left
        c_bapo.font = font_row_regular

        row_fill = fill_alt if stt % 2 == 0 else fill_white
        for col_idx in range(1, 8):
            cell = ws2.cell(row=r, column=col_idx)
            cell.fill = row_fill
            cell.border = border_all

    # ====================================================
    # SHEET 3: MÔ HÌNH 7 AI HARNESSES & VAI TRÒ BA/PO
    # ====================================================
    ws3 = wb.create_sheet(title="3. Mo_Hinh_7_AI_Harnesses")
    ws3.views.sheetView[0].showGridLines = True
    ws3.freeze_panes = "A4"

    # Dòng 1: Tiêu đề Sheet (Banner)
    ws3.merge_cells("A1:E1")
    t3 = ws3["A1"]
    t3.value = "MÔ HÌNH 7 AI HARNESSES — NHIỆM VỤ KỸ THUẬT & TRÁCH NHIỆM CỦA BA / PO"
    t3.font = font_banner
    t3.fill = fill_banner
    t3.alignment = align_center
    t3.border = border_banner
    ws3.row_dimensions[1].height = 36

    # Dòng 2: Phân cách
    ws3.row_dimensions[2].height = 8

    # Dòng 3: Dòng Tiêu đề các Cột
    headers_ws3 = [
        ("Trụ Cột Harness", 22),
        ("Định Nghĩa & Trách Nhiệm Kỹ Thuật", 38),
        ("Nhiệm Vụ Trọng Tâm Của BA / PO", 38),
        ("Deliverables (Sản Phẩm Đầu Ra) Của BA / PO", 35),
        ("Rủi Ro Nếu Bỏ Quên", 30)
    ]

    for col_idx, (hdr, width) in enumerate(headers_ws3, start=1):
        cell = ws3.cell(row=3, column=col_idx, value=hdr)
        cell.font = font_tbl_hdr
        cell.fill = fill_tbl_hdr_alt
        cell.alignment = align_center
        cell.border = border_all
        ws3.column_dimensions[get_column_letter(col_idx)].width = width
    ws3.row_dimensions[3].height = 32

    harness_rows = [
        (
            "1. Context Harness",
            "Quản lý, nạp và trích xuất tri thức phù hợp cho Agent thông qua Enterprise RAG, Chunking, Hybrid Search, Reranking và cơ chế bộ nhớ (Memory).",
            "Phân loại nguồn dữ liệu nghiệp vụ; xác định quy tắc làm sạch và phân vùng tri thức; định nghĩa độ tươi của dữ liệu (Data freshness).",
            "• Knowledge Architecture Spec\n• Chunking & Indexing Guidelines\n• Context Scope & Boundary Rules",
            "AI trả lời lạc đề, ảo giác thông tin sai sự thật, hoặc lộ thông tin mật giữa các phòng ban."
        ),
        (
            "2. Tool Harness",
            "Kết nối Agent với hệ sinh thái công cụ, API doanh nghiệp, cơ sở dữ liệu qua giao thức chuẩn (MCP, Function Calling), kèm cơ chế tự phục hồi và retry.",
            "Thiết kế danh mục chức năng; định nghĩa tham số đầu vào/đầu ra (API Schemas); phân loại hành động an toàn vs hành động rủi ro cao.",
            "• Tool Registry & Action Catalog\n• Tool Interface Specs (OpenAPI/MCP)\n• Error Recovery & Fallback Rules",
            "Agent tự ý gọi nhầm API phá hỏng dữ liệu, spam hệ thống hoặc thất bại mà không biết cách tự xử lý."
        ),
        (
            "3. Orchestration Harness",
            "Thiết kế đồ thị công việc (DAG), máy trạng thái (State Machine), định tuyến (Routing) và cơ chế chuyển giao (Handoff) trong hệ thống Multi-Agent.",
            "Mô hình hóa quy trình kinh doanh thành các trạng thái; phân định vai trò trách nhiệm của từng Agent; thiết kế luồng rẽ nhánh và dự phòng.",
            "• Multi-Agent Workflow Blueprint\n• State Machine & Decision Tables\n• Agent Handoff Matrix",
            "Các Agent đùn đẩy hoặc lặp vô tận (Infinite loop), xung đột logic và làm gián đoạn quy trình kinh doanh."
        ),
        (
            "4. Evaluation Harness",
            "Xây dựng đường ống đo lường tự động (Evaluation Pipeline) chất lượng, độ chính xác, tỷ lệ ảo giác bằng Golden Datasets và LLM-as-a-Judge.",
            "Xây dựng bộ dữ liệu đề thi chuẩn (Ground Truth); định nghĩa bộ tiêu chí chấm điểm (Rubric); thiết lập ngưỡng chấp nhận để ký duyệt release.",
            "• Golden Dataset (200-500 test cases)\n• Evaluation Rubric & Metrics Definition\n• UAT / Regression Test Report",
            "Đưa AI vào vận hành theo cảm tính, không đo lường được tỷ lệ sai sót thực tế, mất niềm tin của người dùng."
        ),
        (
            "5. Security Harness",
            "Bảo vệ hệ thống trước tấn công Prompt Injection, Jailbreak, rò rỉ bí mật (Secrets) và tuân thủ bảo vệ dữ liệu cá nhân (PII Protection).",
            "Xác định danh mục dữ liệu nhạy cảm theo pháp luật (PII); thiết kế chính sách che chắn dữ liệu; viết yêu cầu bảo mật phi chức năng (NFR).",
            "• PII Protection & Data Privacy Policy\n• Security NFRs (OWASP Top 10)\n• Prompt Injection Threat Scenarios",
            "Rò rỉ thông tin cá nhân khách hàng, vi phạm Nghị định 13/2023/NĐ-CP, bị tin tặc chiếm quyền điều khiển Agent."
        ),
        (
            "6. Governance Harness",
            "Đảm bảo tính giải trình (Explainability), lưu vết kiểm toán (Audit Trail), quản trị rủi ro và các điểm chặn con người duyệt (Human-in-the-loop).",
            "Thiết kế ma trận quyền hạn; xác định ngưỡng ranh giới (Threshold) hành động nào cần phê duyệt; đảm bảo dữ liệu ghi vết đủ điều kiện kiểm toán.",
            "• Human-in-the-loop (HITL) Matrix\n• Audit Logging Specification\n• AI Compliance & Policy Guideline",
            "Mất kiểm soát hoàn toàn; khi có sự cố pháp lý hoặc tài chính, không giải trình được tại sao AI đưa ra quyết định đó."
        ),
        (
            "7. AgentOps Harness",
            "Giám sát hiệu năng (Observability), đo lường độ trễ (Latency), chi phí token (Cost Tracking) và phát hiện suy giảm chất lượng (Drift Detection).",
            "Theo dõi bài toán kinh tế (Unit Economics); tính toán ROI của giải pháp AI; giám sát cam kết chất lượng dịch vụ (SLA/SLO).",
            "• Product Unit Economics & ROI Model\n• SLA / SLO & Latency Specifications\n• AgentOps KPI Monitoring Dashboard Spec",
            "Chi phí token tăng vọt làm lỗ sản phẩm; hệ thống phản hồi quá chậm khiến người dùng quay lưng."
        )
    ]

    for idx, row_data in enumerate(harness_rows, start=1):
        r = ws3.max_row + 1
        ws3.row_dimensions[r].height = 70
        for col_idx, val in enumerate(row_data, start=1):
            cell = ws3.cell(row=r, column=col_idx, value=val)
            cell.alignment = align_top_left
            cell.font = font_row_bold if col_idx == 1 else font_row_regular
            cell.fill = fill_alt if idx % 2 == 0 else fill_white
            cell.border = border_all

    # ====================================================
    # SHEET 4: MA TRẬN CHUYỂN ĐỔI KỸ NĂNG BA/PO
    # ====================================================
    ws4 = wb.create_sheet(title="4. Chuyen_Doi_Nang_Luc_BA_PO")
    ws4.views.sheetView[0].showGridLines = True
    ws4.freeze_panes = "A4"

    # Dòng 1: Tiêu đề Sheet (Banner)
    ws4.merge_cells("A1:D1")
    t4 = ws4["A1"]
    t4.value = "MA TRẬN CHUYỂN DỊCH NĂNG LỰC: TRADITIONAL BA/PO  ➔  AI AGENT PRODUCT OWNER"
    t4.font = font_banner
    t4.fill = fill_banner
    t4.alignment = align_center
    t4.border = border_banner
    ws4.row_dimensions[1].height = 36

    # Dòng 2: Phân cách
    ws4.row_dimensions[2].height = 8

    # Dòng 3: Dòng Tiêu đề các Cột
    headers_ws4 = [
        ("Khía Cạnh Công Việc", 24),
        ("Traditional BA / PO (Cách Làm Cũ)", 38),
        ("AI Agent Product Owner / Solution BA (Chuẩn Mới)", 42),
        ("Mô-đun Trong Khóa Học Bổ Trợ", 28)
    ]

    for col_idx, (hdr, width) in enumerate(headers_ws4, start=1):
        cell = ws4.cell(row=3, column=col_idx, value=hdr)
        cell.font = font_tbl_hdr
        cell.fill = fill_tbl_hdr
        cell.alignment = align_center
        cell.border = border_all
        ws4.column_dimensions[get_column_letter(col_idx)].width = width
    ws4.row_dimensions[3].height = 32

    comparison_data = [
        (
            "1. Bản chất hệ thống",
            "Tất định (Deterministic): Cùng một Input + Logic sẽ luôn cho ra đúng 100% cùng một Output.",
            "Phi tất định (Probabilistic): Cùng một Input, AI có thể sinh các câu trả lời khác nhau; chấp nhận xác suất sai sót.",
            "Buổi 1, 8 (Nền tảng & Evals)"
        ),
        (
            "2. Yêu cầu & Tiêu chí nghiệm thu (AC)",
            "User Stories & Given-When-Then tĩnh: Kiểm thử bằng kịch bản chức năng đúng/sai rõ ràng.",
            "Golden Datasets & Rubric: Nghiệm thu bằng bộ đề thi chuẩn, đo lường tỷ lệ ảo giác, độ chính xác ngữ nghĩa và kiểm thử hồi quy.",
            "Buổi 8 (Evaluation Harness)"
        ),
        (
            "3. Thiết kế luồng quy trình",
            "BPMN, Flowchart với các nhánh điều kiện If/Else cứng cố định.",
            "DAG Workflows & State Machines: AI tự lập kế hoạch (Planning), định tuyến động và chuyển giao giữa nhiều Agent.",
            "Buổi 7 (Orchestration Harness)"
        ),
        (
            "4. Quản lý dữ liệu & Tri thức",
            "Thiết kế Database Schema (ERD), bảng biểu quan hệ SQL.",
            "Knowledge Architecture: Thiết kế RAG, phân mảnh ngữ cảnh (Chunking), làm sạch dữ liệu nội bộ và tối ưu hóa bộ nhớ Agent.",
            "Buổi 2, 4 (Context Harness)"
        ),
        (
            "5. Phân quyền & Tương tác hệ thống",
            "Phân quyền người dùng (Role-based Access Control - RBAC) trên giao diện màn hình.",
            "Tool Registry & Privilege Design: Phân quyền API cho AI, kiểm soát hành động tự trị vs hành động bắt buộc người duyệt (HITL).",
            "Buổi 5, 10 (Tool & Governance)"
        ),
        (
            "6. Bảo mật & Tuân thủ",
            "Bảo mật ứng dụng web truyền thống (SQL Injection, XSS, Authen/Author).",
            "AI Safety: Chống Prompt Injection, Jailbreak, bảo vệ rò rỉ dữ liệu PII và lưu vết kiểm toán phục vụ giải trình pháp lý.",
            "Buổi 9, 10 (Security & Governance)"
        ),
        (
            "7. Bài toán kinh tế sản phẩm",
            "Ước lượng chi phí Server cố định hàng tháng (Hosting/Cloud VM).",
            "Unit Economics: Tối ưu chi phí token trên từng transaction, cân bằng giữa Cost - Latency - Accuracy để đảm bảo ROI dương.",
            "Buổi 11 (AgentOps Harness)"
        )
    ]

    for idx, comp in enumerate(comparison_data, start=1):
        r = ws4.max_row + 1
        ws4.row_dimensions[r].height = 55
        for col_idx, val in enumerate(comp, start=1):
            cell = ws4.cell(row=r, column=col_idx, value=val)
            cell.alignment = align_top_left
            cell.font = font_row_bold if col_idx in [1, 4] else font_row_regular
            cell.fill = fill_alt if idx % 2 == 0 else fill_white
            cell.border = border_all

    # Save to both requested destinations
    wb.save(output_path)
    print(f"Saved successfully to: {output_path}")

if __name__ == "__main__":
    import os
    # Try save to Curriculum
    f1 = r"f:\VIETLOTT-SMS\AI_Agent_Engineering_Curriculum.xlsx"
    f2 = r"f:\VIETLOTT-SMS\Khoa_Hoc_AI_Agent_Engineering.xlsx"
    
    for f in [f1, f2]:
        try:
            build_perfect_excel(f)
        except Exception as e:
            print(f"Could not save to {f}: {e}")
