import os

def build_usecase_xml():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="Electron" modified="2026-08-02T10:30:00.000Z" agent="Vietlott SMS BA Agent" version="21.6.8" type="device">
  <diagram id="usecase-bank-campaign" name="Use Case Diagram">
    <mxGraphModel dx="1200" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="900" background="#ffffff" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- System Boundary -->
        <mxCell id="sys_bound" value="Hệ Thống Quản Lý &amp; Tự Động Tặng Vé Kênh Bank (Vietlott SMS)" style="shape=swimlane;whiteSpace=wrap;html=1;startSize=30;fillColor=#f8fafc;strokeColor=#334155;fontStyle=1;fontSize=13;fontColor=#0f172a;" vertex="1" parent="1">
          <mxGeometry x="240" y="40" width="720" height="800" as="geometry" />
        </mxCell>

        <!-- ACTORS (Left & Right) -->
        <!-- Actor Admin -->
        <mxCell id="actor_admin" value="Quản Trị Viên&#xa;(Admin Vietlott)" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#e2e8f0;strokeColor=#1e293b;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="60" y="150" width="45" height="90" as="geometry" />
        </mxCell>

        <!-- Actor Khách Hàng -->
        <mxCell id="actor_customer" value="Khách Hàng&#xa;(App Bank/Ví)" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#e2e8f0;strokeColor=#1e293b;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="60" y="450" width="45" height="90" as="geometry" />
        </mxCell>

        <!-- Actor Bank Partner API (Right) -->
        <mxCell id="actor_bank" value="Bank Partner API&#xa;(VPBank, Vietin...)" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#e2e8f0;strokeColor=#1e293b;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1030" y="150" width="45" height="90" as="geometry" />
        </mxCell>

        <!-- Actor Core Ticketing (Right) -->
        <mxCell id="actor_core" value="Core Ticketing&#xa;Vietlott SMS" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#e2e8f0;strokeColor=#1e293b;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1030" y="450" width="45" height="90" as="geometry" />
        </mxCell>

        <!-- Actor Noti Gateway (Right) -->
        <mxCell id="actor_noti" value="Notification Gateway&#xa;(SMS/Push Noti)" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#e2e8f0;strokeColor=#1e293b;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1030" y="680" width="45" height="90" as="geometry" />
        </mxCell>

        <!-- USE CASES inside System Boundary -->
        <mxCell id="uc1" value="UC01. Cấu hình Cụm 7 Tiêu chí Chiến dịch" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="40" y="50" width="260" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc2" value="UC02. Duyệt &amp; Kích hoạt Chiến dịch" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="40" y="140" width="260" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc10" value="UC10. Xem Dashboard Giải ngân &amp; Đối soát" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="40" y="230" width="260" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc3" value="UC03. Nhận diện Event Kích hoạt TK từ Bank" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="420" y="110" width="260" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc4" value="UC04. Realtime Validate 7 Điều kiện" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="220" y="340" width="260" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc5" value="UC05. Atomic Lock: Trừ Budget &amp; Daily Cap" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="220" y="430" width="260" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc6" value="UC06. Bảo lưu lượt tặng khi vượt Daily Cap" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="40" y="520" width="260" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc7" value="UC07. Tự động Gọi Core Cấp Vé Dự Thưởng" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="420" y="430" width="260" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc8" value="UC08. Retry Queue khi Core Timeout/Error" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="420" y="540" width="260" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc9" value="UC09. Gửi SMS / Push Noti Thông báo Vé Tặng" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="220" y="660" width="270" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc11" value="UC11. Đăng ký mở TK &amp; Tra cứu Vé Tặng" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="40" y="420" width="250" height="60" as="geometry" />
        </mxCell>

        <!-- CONNECTORS (WITH mxGeometry relative="1") -->
        <!-- Admin connections -->
        <mxCell id="e_ad1" style="edgeStyle=none;html=1;strokeColor=#000000;" edge="1" parent="1" source="actor_admin" target="uc1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e_ad2" style="edgeStyle=none;html=1;strokeColor=#000000;" edge="1" parent="1" source="actor_admin" target="uc2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e_ad3" style="edgeStyle=none;html=1;strokeColor=#000000;" edge="1" parent="1" source="actor_admin" target="uc10">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Customer connections -->
        <mxCell id="e_cust1" style="edgeStyle=none;html=1;strokeColor=#000000;" edge="1" parent="1" source="actor_customer" target="uc11">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Bank connections -->
        <mxCell id="e_bank1" style="edgeStyle=none;html=1;strokeColor=#000000;" edge="1" parent="1" source="actor_bank" target="uc3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Core connections -->
        <mxCell id="e_core1" style="edgeStyle=none;html=1;strokeColor=#000000;" edge="1" parent="1" source="actor_core" target="uc7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Noti connections -->
        <mxCell id="e_noti1" style="edgeStyle=none;html=1;strokeColor=#000000;" edge="1" parent="1" source="actor_noti" target="uc9">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Includes & Extends relationships -->
        <mxCell id="e_inc1" value="&lt;&lt;include&gt;&gt;" style="edgeStyle=orthogonalEdgeStyle;dashed=1;html=1;strokeColor=#000000;fontStyle=2;fontSize=10;" edge="1" parent="sys_bound" source="uc3" target="uc4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_inc2" value="&lt;&lt;include&gt;&gt;" style="edgeStyle=orthogonalEdgeStyle;dashed=1;html=1;strokeColor=#000000;fontStyle=2;fontSize=10;" edge="1" parent="sys_bound" source="uc4" target="uc5">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_inc3" value="&lt;&lt;include&gt;&gt;" style="edgeStyle=orthogonalEdgeStyle;dashed=1;html=1;strokeColor=#000000;fontStyle=2;fontSize=10;" edge="1" parent="sys_bound" source="uc5" target="uc7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_inc4" value="&lt;&lt;include&gt;&gt;" style="edgeStyle=orthogonalEdgeStyle;dashed=1;html=1;strokeColor=#000000;fontStyle=2;fontSize=10;" edge="1" parent="sys_bound" source="uc7" target="uc9">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_ext1" value="&lt;&lt;extend&gt;&gt;" style="edgeStyle=orthogonalEdgeStyle;dashed=1;html=1;strokeColor=#000000;fontStyle=2;fontSize=10;" edge="1" parent="sys_bound" source="uc6" target="uc5">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_ext2" value="&lt;&lt;extend&gt;&gt;" style="edgeStyle=orthogonalEdgeStyle;dashed=1;html=1;strokeColor=#000000;fontStyle=2;fontSize=10;" edge="1" parent="sys_bound" source="uc8" target="uc7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''

def build_class_xml():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="Electron" modified="2026-08-02T10:30:00.000Z" agent="Vietlott SMS BA Agent" version="21.6.8" type="device">
  <diagram id="class-bank-campaign" name="Class Diagram">
    <mxGraphModel dx="1200" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="900" background="#ffffff" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Class 1: Campaign -->
        <mxCell id="c_campaign" value="Campaign&#xa;--&#xa;+ campaignId: Long&#xa;+ campaignCode: String&#xa;+ campaignName: String&#xa;+ status: CampaignStatus&#xa;+ totalBudget: BigDecimal&#xa;+ spentBudget: BigDecimal&#xa;+ dailyCap: Integer&#xa;+ issuedToday: Integer&#xa;+ isQueueEnabled: Boolean&#xa;--&#xa;+ validateConfig(): Boolean&#xa;+ checkBudget(): Boolean&#xa;+ checkDailyCap(): Boolean&#xa;+ deductQuotaAtomic(): Boolean" style="swipe;shape=swimlane;whiteSpace=wrap;html=1;fontStyle=1;align=center;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="40" y="60" width="250" height="240" as="geometry" />
        </mxCell>

        <!-- Class 2: CampaignCondition -->
        <mxCell id="c_condition" value="CampaignCondition&#xa;--&#xa;+ conditionId: Long&#xa;+ campaignId: Long&#xa;+ bankChannels: List&lt;String&gt;&#xa;+ accountStatusReq: String&#xa;+ tkntStatusReq: String&#xa;+ paymentCondType: Enum&#xa;+ minPaymentAmount: BigDecimal&#xa;+ ticketType: String&#xa;+ ticketValue: BigDecimal&#xa;--&#xa;+ evaluatePayload(payload): Boolean" style="swipe;shape=swimlane;whiteSpace=wrap;html=1;fontStyle=1;align=center;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="360" y="60" width="250" height="240" as="geometry" />
        </mxCell>

        <!-- Class 3: UserAccountEventPayload -->
        <mxCell id="c_payload" value="UserAccountEventPayload&#xa;--&#xa;+ eventId: String&#xa;+ phoneNumber: String&#xa;+ channelCode: String&#xa;+ accountStatus: String&#xa;+ tkntStatus: String&#xa;+ activatedAt: LocalDateTime&#xa;--&#xa;+ isValid(): Boolean" style="swipe;shape=swimlane;whiteSpace=wrap;html=1;fontStyle=1;align=center;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="680" y="60" width="240" height="180" as="geometry" />
        </mxCell>

        <!-- Class 4: GiftTicketHistory -->
        <mxCell id="c_history" value="GiftTicketHistory&#xa;--&#xa;+ historyId: Long&#xa;+ campaignId: Long&#xa;+ phoneNumber: String&#xa;+ channelCode: String&#xa;+ ticketCode: String&#xa;+ drawId: String&#xa;+ status: IssueStatus&#xa;+ issuedAt: LocalDateTime&#xa;--&#xa;+ markSuccess()&#xa;+ markRetryPending()" style="swipe;shape=swimlane;whiteSpace=wrap;html=1;fontStyle=1;align=center;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="40" y="380" width="250" height="220" as="geometry" />
        </mxCell>

        <!-- Class 5: DailyCapQueue -->
        <mxCell id="c_queue" value="DailyCapQueue&#xa;--&#xa;+ queueId: Long&#xa;+ campaignId: Long&#xa;+ phoneNumber: String&#xa;+ scheduledDate: LocalDate&#xa;+ status: QueueStatus&#xa;--&#xa;+ enqueue()&#xa;+ processMidnightBatch()" style="swipe;shape=swimlane;whiteSpace=wrap;html=1;fontStyle=1;align=center;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="360" y="380" width="250" height="190" as="geometry" />
        </mxCell>

        <!-- Class 6: RealtimeRuleEngine -->
        <mxCell id="c_engine" value="RealtimeRuleEngineService&#xa;--&#xa;- redisTemplate: RedisTemplate&#xa;- coreClient: CoreTicketingClient&#xa;- notiService: NotificationService&#xa;--&#xa;+ processAccountActivatedEvent(payload)&#xa;+ acquireDistributedLock(campaignId)&#xa;+ triggerRetryProtocol(request)" style="swipe;shape=swimlane;whiteSpace=wrap;html=1;fontStyle=1;align=center;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="680" y="380" width="270" height="190" as="geometry" />
        </mxCell>

        <!-- CONNECTORS (WITH mxGeometry relative="1") -->
        <!-- Campaign 1 -- * CampaignCondition -->
        <mxCell id="e_c1" value="1        1..*" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="c_campaign" target="c_condition">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Campaign 1 -- * GiftTicketHistory -->
        <mxCell id="e_c2" value="1        0..*" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="c_campaign" target="c_history">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Campaign 1 -- * DailyCapQueue -->
        <mxCell id="e_c3" value="1        0..*" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="c_campaign" target="c_queue">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- RealtimeRuleEngine uses UserAccountEventPayload -->
        <mxCell id="e_c4" value="uses" style="edgeStyle=orthogonalEdgeStyle;dashed=1;html=1;strokeColor=#000000;fontStyle=2;fontSize=10;" edge="1" parent="1" source="c_engine" target="c_payload">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- RealtimeRuleEngine manages Campaign -->
        <mxCell id="e_c5" value="evaluates" style="edgeStyle=orthogonalEdgeStyle;dashed=1;html=1;strokeColor=#000000;fontStyle=2;fontSize=10;" edge="1" parent="1" source="c_engine" target="c_condition">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''

def build_sequence_xml():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="Electron" modified="2026-08-02T10:30:00.000Z" agent="Vietlott SMS BA Agent" version="21.6.8" type="device">
  <diagram id="sequence-bank-campaign" name="Sequence Diagram">
    <mxGraphModel dx="1200" dy="1100" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="1000" background="#ffffff" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- PARTICIPANTS -->
        <mxCell id="p_cust" value="Khách Hàng (Bank App)" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="130" height="840" as="geometry" />
        </mxCell>

        <mxCell id="p_bank" value="Bank API Gateway" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="220" y="40" width="130" height="840" as="geometry" />
        </mxCell>

        <mxCell id="p_engine" value="Realtime Rule Engine" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="400" y="40" width="140" height="840" as="geometry" />
        </mxCell>

        <mxCell id="p_redis" value="Redis Lock Service" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="590" y="40" width="130" height="840" as="geometry" />
        </mxCell>

        <mxCell id="p_core" value="Core Ticketing API" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="770" y="40" width="130" height="840" as="geometry" />
        </mxCell>

        <mxCell id="p_noti" value="Notification Engine" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="950" y="40" width="130" height="840" as="geometry" />
        </mxCell>

        <!-- MESSAGES & CALLS -->
        <!-- 1. Customer registers -->
        <mxCell id="m1" value="1. Đăng ký TK &amp; eKYC mở TK Bank" style="edgeStyle=none;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="p_cust" target="p_bank">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="105" y="120" as="sourcePoint" />
            <mxPoint x="285" y="120" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- 2. Bank fires event -->
        <mxCell id="m2" value="2. Event: ACCOUNT_ACTIVATED (phone, bank_code)" style="edgeStyle=none;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="p_bank" target="p_engine">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="285" y="170" as="sourcePoint" />
            <mxPoint x="470" y="170" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- 3. Engine validates 7 criteria -->
        <mxCell id="m3" value="3. Validate Cụm 7 ĐK (Kênh, TKDT, TKNT, GD)" style="edgeStyle=loopEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="p_engine" target="p_engine">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="470" y="220" as="sourcePoint" />
            <mxPoint x="520" y="250" as="targetPoint" />
            <Array as="points">
              <mxPoint x="520" y="220" />
              <mxPoint x="520" y="260" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- 4. Acquire Redis Lock -->
        <mxCell id="m4" value="4. acquireLock(campaign_id)" style="edgeStyle=none;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="p_engine" target="p_redis">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="470" y="300" as="sourcePoint" />
            <mxPoint x="655" y="300" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- 5. Lock Acquired -->
        <mxCell id="m5" value="5. Lock Acquired (Success)" style="edgeStyle=none;dashed=1;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="p_redis" target="p_engine">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="655" y="340" as="sourcePoint" />
            <mxPoint x="470" y="340" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- 6. Deduct Quota -->
        <mxCell id="m6" value="6. Atomic Deduct: Spent_Budget &amp; Issued_Today" style="edgeStyle=loopEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="p_engine" target="p_engine">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="470" y="380" as="sourcePoint" />
            <mxPoint x="520" y="410" as="targetPoint" />
            <Array as="points">
              <mxPoint x="520" y="380" />
              <mxPoint x="520" y="420" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- 7. Call Core Issue Ticket -->
        <mxCell id="m7" value="7. POST /core/ticketing/issue-promo-ticket" style="edgeStyle=none;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="p_engine" target="p_core">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="470" y="460" as="sourcePoint" />
            <mxPoint x="835" y="460" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- 8. Core Response -->
        <mxCell id="m8" value="8. 200 OK (ticket_code, numbers, draw_date)" style="edgeStyle=none;dashed=1;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="p_core" target="p_engine">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="835" y="510" as="sourcePoint" />
            <mxPoint x="470" y="510" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- 9. Release Lock -->
        <mxCell id="m9" value="9. releaseLock(campaign_id)" style="edgeStyle=none;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="p_engine" target="p_redis">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="470" y="560" as="sourcePoint" />
            <mxPoint x="655" y="560" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- 10. Send Noti Command -->
        <mxCell id="m10" value="10. sendNotification(phone, ticket_details)" style="edgeStyle=none;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="p_engine" target="p_noti">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="470" y="620" as="sourcePoint" />
            <mxPoint x="1015" y="620" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- 11. Send SMS / Push -->
        <mxCell id="m11" value="11. SMS Brandname / Push Notification" style="edgeStyle=none;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="p_noti" target="p_cust">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1015" y="680" as="sourcePoint" />
            <mxPoint x="105" y="680" as="targetPoint" />
          </mxGeometry>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''

def build_state_machine_xml():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="Electron" modified="2026-08-02T10:30:00.000Z" agent="Vietlott SMS BA Agent" version="21.6.8" type="device">
  <diagram id="state-bank-campaign" name="State Machine Diagram">
    <mxGraphModel dx="1200" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="900" background="#ffffff" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Container 1: Campaign LifeCycle State Machine -->
        <mxCell id="group_campaign" value="Mô Hình Trạng Thái Chiến Dịch (Campaign State Machine)" style="shape=swimlane;whiteSpace=wrap;html=1;startSize=30;fillColor=#f8fafc;strokeColor=#334155;fontStyle=1;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="1120" height="380" as="geometry" />
        </mxCell>

        <mxCell id="st_c_start" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="group_campaign">
          <mxGeometry x="40" y="160" width="30" height="30" as="geometry" />
        </mxCell>

        <mxCell id="st_draft" value="DRAFT&#xa;(Nháp)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_campaign">
          <mxGeometry x="130" y="150" width="130" height="50" as="geometry" />
        </mxCell>

        <mxCell id="st_running" value="DANG_CHAY&#xa;(Kích hoạt tự động)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_campaign">
          <mxGeometry x="360" y="150" width="160" height="50" as="geometry" />
        </mxCell>

        <mxCell id="st_paused" value="TAM_DUNG&#xa;(Pause thủ công)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_campaign">
          <mxGeometry x="360" y="50" width="160" height="50" as="geometry" />
        </mxCell>

        <mxCell id="st_exhausted" value="DA_HET_BUDGET&#xa;(Dừng do hết tiền)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_campaign">
          <mxGeometry x="640" y="150" width="160" height="50" as="geometry" />
        </mxCell>

        <mxCell id="st_finished" value="KET_THUC&#xa;(Hết hạn / Closed)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_campaign">
          <mxGeometry x="880" y="150" width="150" height="50" as="geometry" />
        </mxCell>

        <mxCell id="st_c_end" value="" style="ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="group_campaign">
          <mxGeometry x="1060" y="160" width="30" height="30" as="geometry" />
        </mxCell>

        <!-- Campaign Transitions -->
        <mxCell id="e_st1" value="Admin Save" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontSize=10;" edge="1" parent="group_campaign" source="st_c_start" target="st_draft">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_st2" value="Admin Kích Hoạt" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="group_campaign" source="st_draft" target="st_running">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_st3" value="Pause" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontSize=10;" edge="1" parent="group_campaign" source="st_running" target="st_paused">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_st4" value="Resume" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontSize=10;" edge="1" parent="group_campaign" source="st_paused" target="st_running">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_st5" value="Spent &gt;= Budget" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="group_campaign" source="st_running" target="st_exhausted">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_st6" value="Hết Hạn / Admin Close" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontSize=10;" edge="1" parent="group_campaign" source="st_running" target="st_finished">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="440" y="250" />
              <mxPoint x="955" y="250" />
            </Array>
          </mxGeometry>
        </mxCell>

        <mxCell id="e_st7" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;" edge="1" parent="group_campaign" source="st_exhausted" target="st_finished">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_st8" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;" edge="1" parent="group_campaign" source="st_finished" target="st_c_end">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Container 2: Gift Ticket Transaction State Machine -->
        <mxCell id="group_tx" value="Mô Hình Trạng Thái Giao Dịch Tặng Vé (Gift Ticket Transaction State Machine)" style="shape=swimlane;whiteSpace=wrap;html=1;startSize=30;fillColor=#f8fafc;strokeColor=#334155;fontStyle=1;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="40" y="460" width="1120" height="380" as="geometry" />
        </mxCell>

        <mxCell id="st_tx_start" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="group_tx">
          <mxGeometry x="40" y="160" width="30" height="30" as="geometry" />
        </mxCell>

        <mxCell id="st_init" value="INITIATED&#xa;(Nhận Event Bank)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_tx">
          <mxGeometry x="120" y="150" width="140" height="50" as="geometry" />
        </mxCell>

        <mxCell id="st_rejected" value="REJECTED&#xa;(Không đủ 7 ĐK)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_tx">
          <mxGeometry x="340" y="50" width="140" height="50" as="geometry" />
        </mxCell>

        <mxCell id="st_queued" value="QUEUED_DAILY_CAP&#xa;(Bảo lưu 00:00:01)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_tx">
          <mxGeometry x="340" y="270" width="150" height="50" as="geometry" />
        </mxCell>

        <mxCell id="st_issuing" value="ISSUING&#xa;(Gọi Core Sinh Vé)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_tx">
          <mxGeometry x="340" y="150" width="140" height="50" as="geometry" />
        </mxCell>

        <mxCell id="st_retry" value="PENDING_RETRY&#xa;(Core Timeout - Thử 3 lần)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_tx">
          <mxGeometry x="580" y="270" width="180" height="50" as="geometry" />
        </mxCell>

        <mxCell id="st_success" value="SUCCESS&#xa;(Cấp vé &amp; Gửi SMS thành công)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_tx">
          <mxGeometry x="580" y="150" width="200" height="50" as="geometry" />
        </mxCell>

        <mxCell id="st_failed_manual" value="FAILED_MANUAL&#xa;(Chờ Admin xử lý)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_tx">
          <mxGeometry x="840" y="270" width="160" height="50" as="geometry" />
        </mxCell>

        <mxCell id="st_tx_end" value="" style="ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="group_tx">
          <mxGeometry x="1050" y="160" width="30" height="30" as="geometry" />
        </mxCell>

        <!-- Transaction Transitions -->
        <mxCell id="e_tx1" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;" edge="1" parent="group_tx" source="st_tx_start" target="st_init">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_tx2" value="Đủ ĐK &amp; Còn Quota" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="group_tx" source="st_init" target="st_issuing">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_tx3" value="Không đủ ĐK" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontSize=10;" edge="1" parent="group_tx" source="st_init" target="st_rejected">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_tx4" value="Vượt Daily Cap" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontSize=10;" edge="1" parent="group_tx" source="st_init" target="st_queued">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_tx5" value="00:00:01 Quét Job" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontSize=10;" edge="1" parent="group_tx" source="st_queued" target="st_issuing">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_tx6" value="Core Success" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="group_tx" source="st_issuing" target="st_success">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_tx7" value="Core Timeout/Error" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontSize=10;" edge="1" parent="group_tx" source="st_issuing" target="st_retry">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_tx8" value="Retry 1-3 Success" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontSize=10;" edge="1" parent="group_tx" source="st_retry" target="st_success">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_tx9" value="Thất bại 3 lần" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontSize=10;" edge="1" parent="group_tx" source="st_retry" target="st_failed_manual">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_tx10" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;" edge="1" parent="group_tx" source="st_success" target="st_tx_end">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''

def build_erd_xml():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="Electron" modified="2026-08-02T10:30:00.000Z" agent="Vietlott SMS BA Agent" version="21.6.8" type="device">
  <diagram id="erd-bank-campaign" name="ERD Diagram">
    <mxGraphModel dx="1200" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="900" background="#ffffff" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Entity 1: tbl_campaign -->
        <mxCell id="e_tbl_campaign" value="tbl_campaign (Bảng Chiến Dịch)&#xa;--&#xa;PK | campaign_id : BIGINT&#xa;     | campaign_code : VARCHAR(50)&#xa;     | campaign_name : NVARCHAR(200)&#xa;     | status : VARCHAR(20)&#xa;     | start_time : DATETIME&#xa;     | end_time : DATETIME&#xa;     | total_budget : DECIMAL(15,2)&#xa;     | spent_budget : DECIMAL(15,2)&#xa;     | daily_cap : INT&#xa;     | issued_today : INT&#xa;     | is_queue_enabled : TINYINT(1)&#xa;     | created_at : DATETIME" style="swipe;shape=swimlane;whiteSpace=wrap;html=1;fontStyle=1;align=left;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="280" height="260" as="geometry" />
        </mxCell>

        <!-- Entity 2: tbl_campaign_condition -->
        <mxCell id="e_tbl_condition" value="tbl_campaign_condition (Cụm 7 ĐK)&#xa;--&#xa;PK | condition_id : BIGINT&#xa;FK | campaign_id : BIGINT&#xa;     | channel_codes : JSON&#xa;     | account_status_req : VARCHAR(30)&#xa;     | tknt_status_req : VARCHAR(30)&#xa;     | payment_cond_type : VARCHAR(30)&#xa;     | min_payment_amount : DECIMAL(15,2)&#xa;     | ticket_type : VARCHAR(30)&#xa;     | ticket_value : DECIMAL(15,2)" style="swipe;shape=swimlane;whiteSpace=wrap;html=1;fontStyle=1;align=left;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="420" y="40" width="290" height="220" as="geometry" />
        </mxCell>

        <!-- Entity 3: tbl_gift_ticket_history -->
        <mxCell id="e_tbl_history" value="tbl_gift_ticket_history (Lịch Sử Tặng Vé)&#xa;--&#xa;PK | history_id : BIGINT&#xa;FK | campaign_id : BIGINT&#xa;     | phone_number : VARCHAR(20)&#xa;     | channel_code : VARCHAR(30)&#xa;     | ticket_code : VARCHAR(50)&#xa;     | draw_id : VARCHAR(50)&#xa;     | ticket_value : DECIMAL(15,2)&#xa;     | status : VARCHAR(30)&#xa;     | issued_at : DATETIME" style="swipe;shape=swimlane;whiteSpace=wrap;html=1;fontStyle=1;align=left;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="40" y="400" width="280" height="220" as="geometry" />
        </mxCell>

        <!-- Entity 4: tbl_daily_cap_queue -->
        <mxCell id="e_tbl_queue" value="tbl_daily_cap_queue (Hàng Chờ Bảo Lưu)&#xa;--&#xa;PK | queue_id : BIGINT&#xa;FK | campaign_id : BIGINT&#xa;     | phone_number : VARCHAR(20)&#xa;     | channel_code : VARCHAR(30)&#xa;     | scheduled_date : DATE&#xa;     | status : VARCHAR(30)&#xa;     | created_at : DATETIME" style="swipe;shape=swimlane;whiteSpace=wrap;html=1;fontStyle=1;align=left;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="420" y="400" width="290" height="190" as="geometry" />
        </mxCell>

        <!-- Entity 5: tbl_notification_log -->
        <mxCell id="e_tbl_noti" value="tbl_notification_log (Log SMS/Push)&#xa;--&#xa;PK | log_id : BIGINT&#xa;FK | history_id : BIGINT&#xa;     | phone_number : VARCHAR(20)&#xa;     | noti_type : VARCHAR(30)&#xa;     | message_content : NVARCHAR(500)&#xa;     | send_status : VARCHAR(30)&#xa;     | sent_at : DATETIME" style="swipe;shape=swimlane;whiteSpace=wrap;html=1;fontStyle=1;align=left;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="800" y="400" width="290" height="190" as="geometry" />
        </mxCell>

        <!-- RELATIONSHIPS (WITH mxGeometry relative="1") -->
        <!-- tbl_campaign 1 -- * tbl_campaign_condition -->
        <mxCell id="r1" value="1        1..*" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="e_tbl_campaign" target="e_tbl_condition">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- tbl_campaign 1 -- * tbl_gift_ticket_history -->
        <mxCell id="r2" value="1        0..*" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="e_tbl_campaign" target="e_tbl_history">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- tbl_campaign 1 -- * tbl_daily_cap_queue -->
        <mxCell id="r3" value="1        0..*" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="e_tbl_campaign" target="e_tbl_queue">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- tbl_gift_ticket_history 1 -- * tbl_notification_log -->
        <mxCell id="r4" value="1        0..*" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1" source="e_tbl_history" target="e_tbl_noti">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''

if __name__ == "__main__":
    draft_dir = r"f:\VIETLOTT-SMS\00_Draft"
    
    files_map = {
        "usecase_diagram.drawio": build_usecase_xml(),
        "class_diagram.drawio": build_class_xml(),
        "sequence_diagram.drawio": build_sequence_xml(),
        "state_machine_diagram.drawio": build_state_machine_xml(),
        "erd_diagram.drawio": build_erd_xml(),
    }
    
    for filename, xml in files_map.items():
        filepath = os.path.join(draft_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(xml)
        print(f"Generated: {filepath}")
