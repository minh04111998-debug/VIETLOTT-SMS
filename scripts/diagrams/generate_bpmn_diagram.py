import os
import re

def build_bpmn_xml():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="Electron" modified="2026-08-02T10:45:00.000Z" agent="Vietlott SMS BA Agent" version="21.6.8" type="device">
  <diagram id="bpmn-bank-campaign" name="7. BPMN 2.0 Process Diagram">
    <mxGraphModel dx="1200" dy="1200" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1300" pageHeight="950" background="#ffffff" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Pool Container -->
        <mxCell id="pool_bpmn" value="Quy Trình Nghiệp Vụ Tặng Vé Tự Động Kênh Bank (BPMN 2.0 Process Model)" style="swimlane;html=1;childLayout=stackLayout;horizontal=1;startSize=35;horizontalStack=1;resizeParent=1;resizeParentMax=0;horizontalStack=0;fillColor=#f8fafc;strokeColor=#0f172a;fontStyle=1;fontSize=14;fontColor=#0f172a;align=center;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="1220" height="850" as="geometry" />
        </mxCell>

        <!-- Lane 1: Khách hàng & Bank App -->
        <mxCell id="bpmn_lane1" value="Khách Hàng &amp; Bank App" style="swimlane;html=1;startSize=30;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=12;fontColor=#0f172a;" vertex="1" parent="pool_bpmn">
          <mxGeometry x="0" y="35" width="1220" height="230" as="geometry" />
        </mxCell>

        <!-- Lane 2: Web Admin Vietlott SMS -->
        <mxCell id="bpmn_lane2" value="Web Admin Vietlott SMS" style="swimlane;html=1;startSize=30;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=12;fontColor=#0f172a;" vertex="1" parent="pool_bpmn">
          <mxGeometry x="0" y="265" width="1220" height="240" as="geometry" />
        </mxCell>

        <!-- Lane 3: Realtime Rule Engine & Core Service -->
        <mxCell id="bpmn_lane3" value="Realtime Rule Engine &amp; Core Service" style="swimlane;html=1;startSize=30;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=12;fontColor=#0f172a;" vertex="1" parent="pool_bpmn">
          <mxGeometry x="0" y="505" width="1220" height="345" as="geometry" />
        </mxCell>

        <!-- ==================== LANE 1 NODES ==================== -->
        <!-- BPMN Start Event -->
        <mxCell id="bpmn_start" value="Mở TK Bank&#xa;thành công" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#dcfce7;strokeColor=#16a34a;strokeWidth=2;fontStyle=1;fontSize=10;" vertex="1" parent="bpmn_lane1">
          <mxGeometry x="50" y="85" width="50" height="50" as="geometry" />
        </mxCell>

        <!-- User Task 1 -->
        <mxCell id="t1" value="1. Đăng ký &amp; eKYC tài khoản mới" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1d4ed8;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="bpmn_lane1">
          <mxGeometry x="140" y="80" width="200" height="60" as="geometry" />
        </mxCell>

        <!-- User Task 2 -->
        <mxCell id="t2" value="2. Nạp tiền / Mua vé đầu tiên (nếu yêu cầu)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1d4ed8;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="bpmn_lane1">
          <mxGeometry x="380" y="80" width="220" height="60" as="geometry" />
        </mxCell>

        <!-- Send/Receive Task 3 -->
        <mxCell id="t3" value="3. Nhận SMS / Push Noti vé tặng &amp; Tra cứu App" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fef3c7;strokeColor=#d97706;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="bpmn_lane1">
          <mxGeometry x="880" y="80" width="220" height="60" as="geometry" />
        </mxCell>

        <!-- BPMN End Event -->
        <mxCell id="bpmn_end_success" value="Nhận vé&#xa;thành công" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#fee2e2;strokeColor=#dc2626;strokeWidth=3;fontStyle=1;fontSize=10;" vertex="1" parent="bpmn_lane1">
          <mxGeometry x="1140" y="85" width="50" height="50" as="geometry" />
        </mxCell>


        <!-- ==================== LANE 2 NODES ==================== -->
        <!-- User Task 4 -->
        <mxCell id="t4" value="4. Thiết lập Cụm 7 tiêu chí chiến dịch" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1d4ed8;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="bpmn_lane2">
          <mxGeometry x="50" y="80" width="220" height="60" as="geometry" />
        </mxCell>

        <!-- User Task 5 -->
        <mxCell id="t5" value="5. Trình duyệt &amp; Kích hoạt chiến dịch" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1d4ed8;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="bpmn_lane2">
          <mxGeometry x="310" y="80" width="220" height="60" as="geometry" />
        </mxCell>

        <!-- BPMN Exclusive Gateway 1 -->
        <mxCell id="g1" value="X&#xa;Hợp lệ?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fef08a;strokeColor=#ca8a04;fontStyle=1;fontSize=10;" vertex="1" parent="bpmn_lane2">
          <mxGeometry x="570" y="70" width="70" height="70" as="geometry" />
        </mxCell>

        <!-- User Task 6 (Error) -->
        <mxCell id="t6" value="6. Báo lỗi &amp; Yêu cầu chỉnh sửa" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fee2e2;strokeColor=#dc2626;fontStyle=1;fontSize=10;" vertex="1" parent="bpmn_lane2">
          <mxGeometry x="515" y="170" width="180" height="45" as="geometry" />
        </mxCell>

        <!-- Service Task 7 -->
        <mxCell id="t7" value="7. Chuyển trạng thái chiến dịch DANG_CHAY" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#16a34a;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="bpmn_lane2">
          <mxGeometry x="700" y="80" width="240" height="60" as="geometry" />
        </mxCell>


        <!-- ==================== LANE 3 NODES ==================== -->
        <!-- Intermediate Message Catch Event -->
        <mxCell id="e_msg" value="Event: ACCOUNT_ACTIVATED" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#e0f2fe;strokeColor=#0284c7;strokeWidth=2;fontStyle=1;fontSize=10;" vertex="1" parent="bpmn_lane3">
          <mxGeometry x="50" y="80" width="55" height="55" as="geometry" />
        </mxCell>

        <!-- Business Rule Task 8 -->
        <mxCell id="t8" value="8. Realtime Validate Cụm 7 ĐK" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#16a34a;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="bpmn_lane3">
          <mxGeometry x="140" y="77.5" width="200" height="60" as="geometry" />
        </mxCell>

        <!-- BPMN Exclusive Gateway 2 -->
        <mxCell id="g2" value="X&#xa;Đủ 7 ĐK?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fef08a;strokeColor=#ca8a04;fontStyle=1;fontSize=10;" vertex="1" parent="bpmn_lane3">
          <mxGeometry x="375" y="72.5" width="70" height="70" as="geometry" />
        </mxCell>

        <!-- End Event (Reject) -->
        <mxCell id="end_reject" value="Log từ chối" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#fee2e2;strokeColor=#dc2626;strokeWidth=3;fontStyle=1;fontSize=9;" vertex="1" parent="bpmn_lane3">
          <mxGeometry x="387.5" y="5" width="45" height="45" as="geometry" />
        </mxCell>

        <!-- BPMN Exclusive Gateway 3 -->
        <mxCell id="g3" value="X&#xa;Còn Budget?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fef08a;strokeColor=#ca8a04;fontStyle=1;fontSize=10;" vertex="1" parent="bpmn_lane3">
          <mxGeometry x="480" y="72.5" width="70" height="70" as="geometry" />
        </mxCell>

        <!-- End Event (Exhausted) -->
        <mxCell id="end_budget" value="Đóng Campaign" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#fee2e2;strokeColor=#dc2626;strokeWidth=3;fontStyle=1;fontSize=9;" vertex="1" parent="bpmn_lane3">
          <mxGeometry x="492.5" y="5" width="45" height="45" as="geometry" />
        </mxCell>

        <!-- BPMN Exclusive Gateway 4 -->
        <mxCell id="g4" value="X&#xa;Trong Cap?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fef08a;strokeColor=#ca8a04;fontStyle=1;fontSize=10;" vertex="1" parent="bpmn_lane3">
          <mxGeometry x="585" y="72.5" width="70" height="70" as="geometry" />
        </mxCell>

        <!-- Service Task (Queue) -->
        <mxCell id="t_queue" value="Bảo lưu Queue sang 00:00:01" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#faf5ff;strokeColor=#9333ea;fontStyle=1;fontSize=10;" vertex="1" parent="bpmn_lane3">
          <mxGeometry x="535" y="180" width="170" height="50" as="geometry" />
        </mxCell>

        <!-- Service Task 10 -->
        <mxCell id="t10" value="10. Atomic Lock: Trừ Budget &amp; Cap" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#16a34a;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="bpmn_lane3">
          <mxGeometry x="690" y="77.5" width="210" height="60" as="geometry" />
        </mxCell>

        <!-- Service Task 11 -->
        <mxCell id="t11" value="11. Gọi API Core Ticketing Cấp vé" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#16a34a;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="bpmn_lane3">
          <mxGeometry x="690" y="175" width="210" height="60" as="geometry" />
        </mxCell>

        <!-- Exclusive Gateway 5 (Core) -->
        <mxCell id="g5" value="X&#xa;Core OK?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fef08a;strokeColor=#ca8a04;fontStyle=1;fontSize=10;" vertex="1" parent="bpmn_lane3">
          <mxGeometry x="935" y="170" width="70" height="70" as="geometry" />
        </mxCell>

        <!-- Service Task 12 (Retry) -->
        <mxCell id="t12" value="12. Retry Queue (Thử 3 lần)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fee2e2;strokeColor=#dc2626;fontStyle=1;fontSize=10;" vertex="1" parent="bpmn_lane3">
          <mxGeometry x="895" y="270" width="150" height="45" as="geometry" />
        </mxCell>

        <!-- Service Task 13 (Noti) -->
        <mxCell id="t13" value="13. Trigger Notification Engine" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#16a34a;strokeWidth=1.5;fontStyle=1;fontSize=11;" vertex="1" parent="bpmn_lane3">
          <mxGeometry x="930" y="77.5" width="200" height="60" as="geometry" />
        </mxCell>


        <!-- CONNECTORS (WITH EXPLICIT mxGeometry relative="1") -->
        <!-- Lane 1 Sequence Flows -->
        <mxCell id="bf1" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;" edge="1" parent="bpmn_lane1" source="bpmn_start" target="t1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bf2" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;" edge="1" parent="bpmn_lane1" source="t1" target="t2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bf3" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;" edge="1" parent="bpmn_lane1" source="t3" target="bpmn_end_success">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Lane 2 Sequence Flows -->
        <mxCell id="bf4" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;" edge="1" parent="bpmn_lane2" source="t4" target="t5">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bf5" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;" edge="1" parent="bpmn_lane2" source="t5" target="g1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bf_g1_no" value="No" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="bpmn_lane2" source="g1" target="t6">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bf_t6_loop" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;" edge="1" parent="bpmn_lane2" source="t6" target="t4">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="160" y="192" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="bf_g1_yes" value="Yes" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="bpmn_lane2" source="g1" target="t7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Lane 3 Sequence Flows -->
        <mxCell id="bf6" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;" edge="1" parent="bpmn_lane3" source="e_msg" target="t8">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bf7" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;" edge="1" parent="bpmn_lane3" source="t8" target="g2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bf_g2_no" value="No" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="bpmn_lane3" source="g2" target="end_reject">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bf_g2_yes" value="Yes" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="bpmn_lane3" source="g2" target="g3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bf_g3_no" value="No" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="bpmn_lane3" source="g3" target="end_budget">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bf_g3_yes" value="Yes" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="bpmn_lane3" source="g3" target="g4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bf_g4_no" value="Vượt Cap" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="bpmn_lane3" source="g4" target="t_queue">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bf_g4_yes" value="Còn Cap" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="bpmn_lane3" source="g4" target="t10">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bf8" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;" edge="1" parent="bpmn_lane3" source="t10" target="t11">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bf9" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;" edge="1" parent="bpmn_lane3" source="t11" target="g5">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bf_g5_no" value="Fail/Timeout" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="bpmn_lane3" source="g5" target="t12">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="bf_g5_yes" value="Success" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="bpmn_lane3" source="g5" target="t13">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Message Flows between Swimlanes (Dashed) -->
        <mxCell id="mf1" value="Event ACCOUNT_ACTIVATED" style="edgeStyle=orthogonalEdgeStyle;dashed=1;html=1;strokeColor=#0284c7;fontStyle=1;fontSize=10;" edge="1" parent="pool_bpmn" source="t2" target="e_msg">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="mf2" value="SMS / Push Command" style="edgeStyle=orthogonalEdgeStyle;dashed=1;html=1;strokeColor=#d97706;fontStyle=1;fontSize=10;" edge="1" parent="pool_bpmn" source="t13" target="t3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''

if __name__ == "__main__":
    draft_dir = r"f:\VIETLOTT-SMS\00_Draft"
    xml = build_bpmn_xml()
    
    # Save bpmn_diagram.drawio
    bpmn_path = os.path.join(draft_dir, "bpmn_diagram.drawio")
    with open(bpmn_path, "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"Generated BPMN 2.0 diagram: {bpmn_path}")

    # Save bpmn_diagram.xml
    bpmn_xml_path = os.path.join(draft_dir, "bpmn_diagram.xml")
    with open(bpmn_xml_path, "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"Generated BPMN XML: {bpmn_xml_path}")
