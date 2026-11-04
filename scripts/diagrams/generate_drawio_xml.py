import os

def build_drawio_xml():
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="Electron" modified="2026-07-29T22:00:00.000Z" agent="Vietlott SMS BA Agent" version="21.6.8" type="device">
  <diagram id="swimlane-bank-campaign" name="Sơ đồ Luồng Tặng Vé Bank">
    <mxGraphModel dx="1200" dy="1800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1160" pageHeight="1850" background="#ffffff" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Pool Container -->
        <mxCell id="pool" value="Luồng Hoạt Động Tặng Vé Mở Tài Khoản Kênh Bank (UML Activity Swimlane)" style="swimlane;html=1;childLayout=stackLayout;horizontal=1;startSize=35;horizontalStack=1;resizeParent=1;resizeParentMax=0;horizontalStack=0;fillColor=#f8fafc;strokeColor=#000000;fontStyle=1;fontSize=14;fontColor=#0f172a;align=center;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="1080" height="1760" as="geometry" />
        </mxCell>

        <!-- Lane 1: Khách hàng & Kênh Bank -->
        <mxCell id="lane1" value="Khách hàng &amp; Kênh Bank" style="swimlane;html=1;startSize=30;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=12;fontColor=#0f172a;" vertex="1" parent="pool">
          <mxGeometry x="0" y="35" width="360" height="1725" as="geometry" />
        </mxCell>

        <!-- Lane 2: Web Admin Vietlott SMS -->
        <mxCell id="lane2" value="Web Admin Vietlott SMS" style="swimlane;html=1;startSize=30;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=12;fontColor=#0f172a;" vertex="1" parent="pool">
          <mxGeometry x="360" y="35" width="360" height="1725" as="geometry" />
        </mxCell>

        <!-- Lane 3: Realtime Rule Engine & Core Service -->
        <mxCell id="lane3" value="Hệ thống Realtime Rule Engine &amp; Core Service" style="swimlane;html=1;startSize=30;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=12;fontColor=#0f172a;" vertex="1" parent="pool">
          <mxGeometry x="720" y="35" width="360" height="1725" as="geometry" />
        </mxCell>

        <!-- ==================== LANE 1 NODES ==================== -->
        <!-- Start Node -->
        <mxCell id="node_start" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="lane1">
          <mxGeometry x="165" y="40" width="30" height="30" as="geometry" />
        </mxCell>

        <!-- Step 1 Box -->
        <mxCell id="step1" value="1. Đăng ký mở tài khoản mới qua kênh Bank" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane1">
          <mxGeometry x="40" y="100" width="280" height="50" as="geometry" />
        </mxCell>

        <!-- Step 2 Box -->
        <mxCell id="step2" value="2. Thực hiện eKYC / Active tài khoản / Thanh toán" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane1">
          <mxGeometry x="30" y="190" width="300" height="50" as="geometry" />
        </mxCell>

        <!-- Step 16b Box -->
        <mxCell id="step16b" value="16b. Nhận thông báo suất tặng vé&#xa;được bảo lưu sang 00:00:01 ngày hôm sau" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane1">
          <mxGeometry x="30" y="1120" width="300" height="50" as="geometry" />
        </mxCell>

        <!-- End Node 16b -->
        <mxCell id="end_16b" value="" style="ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="lane1">
          <mxGeometry x="165" y="1210" width="30" height="30" as="geometry" />
        </mxCell>

        <!-- Step 23 Box -->
        <mxCell id="step23" value="23. Nhận SMS / Push Noti vé tặng&#xa;&amp; Tra cứu vé dự thưởng trên App" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane1">
          <mxGeometry x="30" y="1570" width="300" height="50" as="geometry" />
        </mxCell>

        <!-- End Node 23 -->
        <mxCell id="end_23" value="" style="ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="lane1">
          <mxGeometry x="165" y="1660" width="30" height="30" as="geometry" />
        </mxCell>


        <!-- ==================== LANE 2 NODES ==================== -->
        <!-- Step 3 Box -->
        <mxCell id="step3" value="3. Admin thiết lập cụm 7 điều kiện chiến dịch" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane2">
          <mxGeometry x="40" y="100" width="280" height="50" as="geometry" />
        </mxCell>

        <!-- Step 4 Box -->
        <mxCell id="step4" value="4. Nhấn 'Lưu &amp; Kích hoạt' chiến dịch" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane2">
          <mxGeometry x="40" y="190" width="280" height="50" as="geometry" />
        </mxCell>

        <!-- Step 5 Diamond -->
        <mxCell id="step5" value="5. Kiểm tra thông tin&#xa;cấu hình hợp lệ?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=10;fontColor=#0f172a;" vertex="1" parent="lane2">
          <mxGeometry x="100" y="280" width="160" height="80" as="geometry" />
        </mxCell>

        <!-- Step 6 Box (No) -->
        <mxCell id="step6" value="6. Báo lỗi &amp; Yêu cầu nhập lại" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane2">
          <mxGeometry x="40" y="390" width="280" height="45" as="geometry" />
        </mxCell>

        <!-- Step 7 Box (Yes) -->
        <mxCell id="step7" value="7. Chuyển trạng thái chiến dịch DANG_CHAY" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane2">
          <mxGeometry x="40" y="465" width="280" height="50" as="geometry" />
        </mxCell>


        <!-- ==================== LANE 3 NODES ==================== -->
        <!-- Step 8 Box -->
        <mxCell id="step8" value="8. Lắng nghe Event: ACCOUNT_ACTIVATED từ Bank" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane3">
          <mxGeometry x="25" y="520" width="310" height="50" as="geometry" />
        </mxCell>

        <!-- Step 9 Diamond -->
        <mxCell id="step9" value="9. Kiểm tra Kênh Bank &amp;&#xa;Trạng thái TKDT/TKNT?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=10;fontColor=#0f172a;" vertex="1" parent="lane3">
          <mxGeometry x="40" y="600" width="160" height="80" as="geometry" />
        </mxCell>

        <!-- Step 10 Box (No) -->
        <mxCell id="step10" value="10. Ghi log lý do:&#xa;Không đủ điều kiện" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=10;fontColor=#0f172a;" vertex="1" parent="lane3">
          <mxGeometry x="220" y="665" width="130" height="50" as="geometry" />
        </mxCell>

        <!-- End Node 10 -->
        <mxCell id="end_10" value="" style="ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="lane3">
          <mxGeometry x="270" y="740" width="30" height="30" as="geometry" />
        </mxCell>

        <!-- Step 11 Diamond (Yes) -->
        <mxCell id="step11" value="11. Kiểm tra Total Budget&#xa;Chiến dịch?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=10;fontColor=#0f172a;" vertex="1" parent="lane3">
          <mxGeometry x="40" y="730" width="160" height="80" as="geometry" />
        </mxCell>

        <!-- Step 12 Box (Hết Budget) -->
        <mxCell id="step12" value="12. Chuyển trạng thái:&#xa;DA_HET_BUDGET" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=10;fontColor=#0f172a;" vertex="1" parent="lane3">
          <mxGeometry x="220" y="795" width="130" height="50" as="geometry" />
        </mxCell>

        <!-- End Node 12 -->
        <mxCell id="end_12" value="" style="ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="lane3">
          <mxGeometry x="270" y="870" width="30" height="30" as="geometry" />
        </mxCell>

        <!-- Step 13 Diamond (Còn Budget) -->
        <mxCell id="step13" value="13. Kiểm tra Hạn mức Ngày&#xa;(Daily Cap)?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=10;fontColor=#0f172a;" vertex="1" parent="lane3">
          <mxGeometry x="40" y="860" width="160" height="80" as="geometry" />
        </mxCell>

        <!-- Step 14 Diamond (Vượt Cap) -->
        <mxCell id="step14" value="14. Check Policy&#xa;Bảo lưu?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=10;fontColor=#0f172a;" vertex="1" parent="lane3">
          <mxGeometry x="220" y="930" width="130" height="70" as="geometry" />
        </mxCell>

        <!-- Step 16 Box (Có bảo lưu) -->
        <mxCell id="step16" value="16. Đưa vào Queue chờ&#xa;00:00:01 ngày sau" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=10;fontColor=#0f172a;" vertex="1" parent="lane3">
          <mxGeometry x="205" y="1035" width="145" height="50" as="geometry" />
        </mxCell>

        <!-- Step 17 Box (Còn Quota) -->
        <mxCell id="step17" value="17. Atomic Lock: Trừ Quota &amp; Budget" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane3">
          <mxGeometry x="25" y="1210" width="310" height="50" as="geometry" />
        </mxCell>

        <!-- Step 18 Box -->
        <mxCell id="step18" value="18. Gọi API Core Ticketing sinh vé tự động" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane3">
          <mxGeometry x="25" y="1300" width="310" height="50" as="geometry" />
        </mxCell>

        <!-- Step 19 Diamond -->
        <mxCell id="step19" value="19. Kết quả phát vé&#xa;từ Core?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=10;fontColor=#0f172a;" vertex="1" parent="lane3">
          <mxGeometry x="40" y="1380" width="160" height="80" as="geometry" />
        </mxCell>

        <!-- Step 20 Box (Fail/Timeout) -->
        <mxCell id="step20" value="20. Retry Queue (Thử 3 lần)&#xa;Log PENDING_RETRY" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=10;fontColor=#0f172a;" vertex="1" parent="lane3">
          <mxGeometry x="200" y="1445" width="145" height="50" as="geometry" />
        </mxCell>

        <!-- End Node 20 -->
        <mxCell id="end_20" value="" style="ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="lane3">
          <mxGeometry x="257" y="1520" width="30" height="30" as="geometry" />
        </mxCell>

        <!-- Step 21 Box (Thành công) -->
        <mxCell id="step21" value="21. Ghi Audit Log &amp;&#xa;Update Dashboard" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=10;fontColor=#0f172a;" vertex="1" parent="lane3">
          <mxGeometry x="25" y="1485" width="165" height="50" as="geometry" />
        </mxCell>

        <!-- Step 22 Box -->
        <mxCell id="step22" value="22. Gửi lệnh thông báo SMS / Push Notification" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;fontStyle=1;fontSize=11;fontColor=#0f172a;" vertex="1" parent="lane3">
          <mxGeometry x="25" y="1575" width="310" height="45" as="geometry" />
        </mxCell>


        <!-- ==================== EDGES / CONNECTORS (WITH mxGeometry) ==================== -->
        <!-- Start -> Step 1 -->
        <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" edge="1" parent="1" source="node_start" target="step1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 1 -> Step 2 -->
        <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" edge="1" parent="1" source="step1" target="step2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 3 -> Step 4 -->
        <mxCell id="e3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" edge="1" parent="1" source="step3" target="step4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 4 -> Step 5 -->
        <mxCell id="e4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" edge="1" parent="1" source="step4" target="step5">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 5 -> Step 6 (No) -->
        <mxCell id="e5_no" value="No" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="step5" target="step6">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 6 -> Step 3 (Loopback) -->
        <mxCell id="e6_loop" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" edge="1" parent="1" source="step6" target="step3">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="710" y="447" />
              <mxPoint x="710" y="160" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Step 5 -> Step 7 (Yes) -->
        <mxCell id="e5_yes" value="Yes" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="step5" target="step7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 2 & Step 7 -> Step 8 -->
        <mxCell id="e7_event" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;dashed=1;" edge="1" parent="1" source="step2" target="step8">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e7b_event" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" edge="1" parent="1" source="step7" target="step8">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 8 -> Step 9 -->
        <mxCell id="e8" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" edge="1" parent="1" source="step8" target="step9">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 9 -> Step 10 (No) -->
        <mxCell id="e9_no" value="No" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="step9" target="step10">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 10 -> End 10 -->
        <mxCell id="e10_end" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" edge="1" parent="1" source="step10" target="end_10">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 9 -> Step 11 (Yes) -->
        <mxCell id="e9_yes" value="Yes" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="step9" target="step11">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 11 -> Step 12 (Hết Budget) -->
        <mxCell id="e11_no" value="Hết Budget" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="step11" target="step12">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 12 -> End 12 -->
        <mxCell id="e12_end" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" edge="1" parent="1" source="step12" target="end_12">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 11 -> Step 13 (Còn Budget) -->
        <mxCell id="e11_yes" value="Còn Budget" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="step11" target="step13">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 13 -> Step 14 (Vượt Cap) -->
        <mxCell id="e13_no" value="Vượt Cap" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="step13" target="step14">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 14 -> Step 16 (Có bảo lưu) -->
        <mxCell id="e14_yes" value="Có bảo lưu" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="step14" target="step16">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 16 -> Step 16b -->
        <mxCell id="e16_to_16b" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" edge="1" parent="1" source="step16" target="step16b">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 16b -> End 16b -->
        <mxCell id="e16b_end" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" edge="1" parent="1" source="step16b" target="end_16b">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 13 -> Step 17 (Còn Quota) -->
        <mxCell id="e13_yes" value="Còn Quota" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="step13" target="step17">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 17 -> Step 18 -->
        <mxCell id="e17" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" edge="1" parent="1" source="step17" target="step18">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 18 -> Step 19 -->
        <mxCell id="e18" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" edge="1" parent="1" source="step18" target="step19">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 19 -> Step 20 (Fail/Timeout) -->
        <mxCell id="e19_no" value="Fail / Timeout" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="step19" target="step20">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 20 -> End 20 -->
        <mxCell id="e20_end" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" edge="1" parent="1" source="step20" target="end_20">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 19 -> Step 21 (Thành công) -->
        <mxCell id="e19_yes" value="Thành công" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="step19" target="step21">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 21 -> Step 22 -->
        <mxCell id="e21" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" edge="1" parent="1" source="step21" target="step22">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 22 -> Step 23 -->
        <mxCell id="e22_to_23" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" edge="1" parent="1" source="step22" target="step23">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Step 23 -> End 23 -->
        <mxCell id="e23_end" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;" edge="1" parent="1" source="step23" target="end_23">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    return xml

if __name__ == "__main__":
    xml_content = build_drawio_xml()
    
    # Save .drawio file
    drawio_file_path = r"f:\VIETLOTT-SMS\00_Draft\activity_diagram_swimlane.drawio"
    with open(drawio_file_path, "w", encoding="utf-8") as f:
        f.write(xml_content)
    print("Draw.io XML generated successfully.")

    # Save .xml file as well
    xml_file_path = r"f:\VIETLOTT-SMS\00_Draft\activity_diagram_swimlane.xml"
    with open(xml_file_path, "w", encoding="utf-8") as f:
        f.write(xml_content)
    print("XML file generated successfully.")
