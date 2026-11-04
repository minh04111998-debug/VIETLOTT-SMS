import os

def build_usecase_xml():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="Electron" modified="2026-08-02T10:40:00.000Z" agent="Vietlott SMS BA Agent" version="21.6.8" type="device">
  <diagram id="usecase-bank-campaign" name="2. Use Case Diagram">
    <mxGraphModel dx="1200" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="900" background="#ffffff" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- System Boundary -->
        <mxCell id="sys_bound" value="Hệ Thống Quản Lý &amp; Tự Động Tặng Vé Kênh Bank (Vietlott SMS)" style="shape=swimlane;whiteSpace=wrap;html=1;startSize=30;fillColor=#f8fafc;strokeColor=#334155;fontStyle=1;fontSize=13;fontColor=#0f172a;" vertex="1" parent="1">
          <mxGeometry x="220" y="40" width="760" height="820" as="geometry" />
        </mxCell>

        <!-- ACTORS (Left & Right) -->
        <mxCell id="actor_admin" value="Quản Trị Viên&#xa;(Admin Vietlott)" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#e2e8f0;strokeColor=#1e293b;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="50" y="150" width="45" height="90" as="geometry" />
        </mxCell>

        <mxCell id="actor_customer" value="Khách Hàng&#xa;(App Bank/Ví)" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#e2e8f0;strokeColor=#1e293b;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="50" y="450" width="45" height="90" as="geometry" />
        </mxCell>

        <mxCell id="actor_bank" value="Bank Partner API&#xa;(VPBank, Vietin...)" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#e2e8f0;strokeColor=#1e293b;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1040" y="150" width="45" height="90" as="geometry" />
        </mxCell>

        <mxCell id="actor_core" value="Core Ticketing&#xa;Vietlott SMS" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#e2e8f0;strokeColor=#1e293b;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1040" y="450" width="45" height="90" as="geometry" />
        </mxCell>

        <mxCell id="actor_noti" value="Notification Gateway&#xa;(SMS/Push Noti)" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#e2e8f0;strokeColor=#1e293b;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1040" y="680" width="45" height="90" as="geometry" />
        </mxCell>

        <!-- USE CASES inside System Boundary -->
        <mxCell id="uc1" value="UC01. Cấu hình Cụm 7 Tiêu chí Chiến dịch" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="40" y="50" width="280" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc2" value="UC02. Duyệt &amp; Kích hoạt Chiến dịch" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="40" y="140" width="280" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc10" value="UC10. Xem Dashboard Giải ngân &amp; Đối soát" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="40" y="230" width="280" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc3" value="UC03. Nhận diện Event Kích hoạt TK từ Bank" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="430" y="110" width="290" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc4" value="UC04. Realtime Validate 7 Điều kiện" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="240" y="340" width="280" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc5" value="UC05. Atomic Lock: Trừ Budget &amp; Daily Cap" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="240" y="440" width="280" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc6" value="UC06. Bảo lưu lượt tặng khi vượt Daily Cap" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="40" y="540" width="280" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc7" value="UC07. Tự động Gọi Core Cấp Vé Dự Thưởng" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="430" y="440" width="290" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc8" value="UC08. Retry Queue khi Core Timeout/Error" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="430" y="560" width="290" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc9" value="UC09. Gửi SMS / Push Noti Thông báo Vé Tặng" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="240" y="680" width="290" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc11" value="UC11. Đăng ký mở TK &amp; Tra cứu Vé Tặng" style="ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="sys_bound">
          <mxGeometry x="40" y="430" width="280" height="60" as="geometry" />
        </mxCell>

        <!-- CONNECTORS -->
        <mxCell id="e_ad1" style="edgeStyle=none;html=1;strokeColor=#000000;" edge="1" parent="1" source="actor_admin" target="uc1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e_ad2" style="edgeStyle=none;html=1;strokeColor=#000000;" edge="1" parent="1" source="actor_admin" target="uc2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e_ad3" style="edgeStyle=none;html=1;strokeColor=#000000;" edge="1" parent="1" source="actor_admin" target="uc10">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e_cust1" style="edgeStyle=none;html=1;strokeColor=#000000;" edge="1" parent="1" source="actor_customer" target="uc11">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e_bank1" style="edgeStyle=none;html=1;strokeColor=#000000;" edge="1" parent="1" source="actor_bank" target="uc3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e_core1" style="edgeStyle=none;html=1;strokeColor=#000000;" edge="1" parent="1" source="actor_core" target="uc7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e_noti1" style="edgeStyle=none;html=1;strokeColor=#000000;" edge="1" parent="1" source="actor_noti" target="uc9">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Includes & Extends -->
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
<mxfile host="Electron" modified="2026-08-02T10:40:00.000Z" agent="Vietlott SMS BA Agent" version="21.6.8" type="device">
  <diagram id="class-bank-campaign" name="3. Class Diagram">
    <mxGraphModel dx="1200" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="900" background="#ffffff" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Class 1: Campaign -->
        <mxCell id="c_campaign" value="&lt;b&gt;Campaign&lt;/b&gt;&lt;hr/&gt;+ campaignId: Long&lt;br/&gt;+ campaignCode: String&lt;br/&gt;+ campaignName: String&lt;br/&gt;+ status: CampaignStatus&lt;br/&gt;+ totalBudget: BigDecimal&lt;br/&gt;+ spentBudget: BigDecimal&lt;br/&gt;+ dailyCap: Integer&lt;br/&gt;+ issuedToday: Integer&lt;br/&gt;+ isQueueEnabled: Boolean&lt;hr/&gt;+ validateConfig(): Boolean&lt;br/&gt;+ checkBudget(): Boolean&lt;br/&gt;+ checkDailyCap(): Boolean&lt;br/&gt;+ deductQuotaAtomic(): Boolean" style="rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=top;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;spacingLeft=8;spacingTop=6;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="280" height="300" as="geometry" />
        </mxCell>

        <!-- Class 2: CampaignCondition -->
        <mxCell id="c_condition" value="&lt;b&gt;CampaignCondition&lt;/b&gt;&lt;hr/&gt;+ conditionId: Long&lt;br/&gt;+ campaignId: Long&lt;br/&gt;+ bankChannels: List&amp;lt;String&amp;gt;&lt;br/&gt;+ accountStatusReq: String&lt;br/&gt;+ tkntStatusReq: String&lt;br/&gt;+ paymentCondType: Enum&lt;br/&gt;+ minPaymentAmount: BigDecimal&lt;br/&gt;+ ticketType: String&lt;br/&gt;+ ticketValue: BigDecimal&lt;hr/&gt;+ evaluatePayload(payload): Boolean" style="rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=top;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;spacingLeft=8;spacingTop=6;" vertex="1" parent="1">
          <mxGeometry x="400" y="40" width="290" height="300" as="geometry" />
        </mxCell>

        <!-- Class 3: UserAccountEventPayload -->
        <mxCell id="c_payload" value="&lt;b&gt;UserAccountEventPayload&lt;/b&gt;&lt;hr/&gt;+ eventId: String&lt;br/&gt;+ phoneNumber: String&lt;br/&gt;+ channelCode: String&lt;br/&gt;+ accountStatus: String&lt;br/&gt;+ tkntStatus: String&lt;br/&gt;+ activatedAt: LocalDateTime&lt;hr/&gt;+ isValid(): Boolean" style="rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=top;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;spacingLeft=8;spacingTop=6;" vertex="1" parent="1">
          <mxGeometry x="770" y="40" width="280" height="230" as="geometry" />
        </mxCell>

        <!-- Class 4: GiftTicketHistory -->
        <mxCell id="c_history" value="&lt;b&gt;GiftTicketHistory&lt;/b&gt;&lt;hr/&gt;+ historyId: Long&lt;br/&gt;+ campaignId: Long&lt;br/&gt;+ phoneNumber: String&lt;br/&gt;+ channelCode: String&lt;br/&gt;+ ticketCode: String&lt;br/&gt;+ drawId: String&lt;br/&gt;+ status: IssueStatus&lt;br/&gt;+ issuedAt: LocalDateTime&lt;hr/&gt;+ markSuccess()&lt;br/&gt;+ markRetryPending()" style="rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=top;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;spacingLeft=8;spacingTop=6;" vertex="1" parent="1">
          <mxGeometry x="40" y="420" width="280" height="270" as="geometry" />
        </mxCell>

        <!-- Class 5: DailyCapQueue -->
        <mxCell id="c_queue" value="&lt;b&gt;DailyCapQueue&lt;/b&gt;&lt;hr/&gt;+ queueId: Long&lt;br/&gt;+ campaignId: Long&lt;br/&gt;+ phoneNumber: String&lt;br/&gt;+ scheduledDate: LocalDate&lt;br/&gt;+ status: QueueStatus&lt;hr/&gt;+ enqueue()&lt;br/&gt;+ processMidnightBatch()" style="rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=top;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;spacingLeft=8;spacingTop=6;" vertex="1" parent="1">
          <mxGeometry x="400" y="420" width="290" height="240" as="geometry" />
        </mxCell>

        <!-- Class 6: RealtimeRuleEngine -->
        <mxCell id="c_engine" value="&lt;b&gt;RealtimeRuleEngineService&lt;/b&gt;&lt;hr/&gt;- redisTemplate: RedisTemplate&lt;br/&gt;- coreClient: CoreTicketingClient&lt;br/&gt;- notiService: NotificationService&lt;hr/&gt;+ processAccountActivatedEvent(payload)&lt;br/&gt;+ acquireDistributedLock(campaignId)&lt;br/&gt;+ triggerRetryProtocol(request)" style="rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=top;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;spacingLeft=8;spacingTop=6;" vertex="1" parent="1">
          <mxGeometry x="770" y="420" width="310" height="240" as="geometry" />
        </mxCell>

        <!-- CONNECTORS (NO TEXT OVERLAP) -->
        <mxCell id="e_c1" value="1        1..*" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1" source="c_campaign" target="c_condition">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_c2" value="1        0..*" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" edge="1" parent="1" source="c_campaign" target="c_history">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_c3" value="1        0..*" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" edge="1" parent="1" source="c_condition" target="c_queue">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_c4" value="uses" style="edgeStyle=orthogonalEdgeStyle;dashed=1;html=1;strokeColor=#000000;fontStyle=2;fontSize=10;exitX=0.5;exitY=0;entryX=0.5;entryY=1;" edge="1" parent="1" source="c_engine" target="c_payload">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="e_c5" value="evaluates" style="edgeStyle=orthogonalEdgeStyle;dashed=1;html=1;strokeColor=#000000;fontStyle=2;fontSize=10;exitX=0;exitY=0.5;entryX=1;entryY=0.5;" edge="1" parent="1" source="c_engine" target="c_queue">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''

def build_sequence_xml():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="Electron" modified="2026-08-02T10:40:00.000Z" agent="Vietlott SMS BA Agent" version="21.6.8" type="device">
  <diagram id="sequence-bank-campaign" name="4. Sequence Diagram">
    <mxGraphModel dx="1200" dy="1100" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="1000" background="#ffffff" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- PARTICIPANTS -->
        <mxCell id="p_cust" value="Khách Hàng (Bank App)" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="140" height="840" as="geometry" />
        </mxCell>

        <mxCell id="p_bank" value="Bank API Gateway" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="230" y="40" width="140" height="840" as="geometry" />
        </mxCell>

        <mxCell id="p_engine" value="Realtime Rule Engine" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="430" y="40" width="150" height="840" as="geometry" />
        </mxCell>

        <mxCell id="p_redis" value="Redis Lock Service" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="640" y="40" width="140" height="840" as="geometry" />
        </mxCell>

        <mxCell id="p_core" value="Core Ticketing API" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="840" y="40" width="140" height="840" as="geometry" />
        </mxCell>

        <mxCell id="p_noti" value="Notification Engine" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1030" y="40" width="140" height="840" as="geometry" />
        </mxCell>

        <!-- MESSAGES WITH EXPLICIT Y-COORDINATE POINTS -->
        <!-- 1. Customer registers (y=120) -->
        <mxCell id="m1" value="1. Đăng ký TK &amp; eKYC mở TK Bank" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="110" y="120" as="sourcePoint" />
            <mxPoint x="300" y="120" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- 2. Bank fires event (y=180) -->
        <mxCell id="m2" value="2. Event: ACCOUNT_ACTIVATED (phone, bank_code)" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="300" y="180" as="sourcePoint" />
            <mxPoint x="505" y="180" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- 3. Engine validates 7 criteria (y=240..270) -->
        <mxCell id="m3" value="3. Validate Cụm 7 ĐK (Kênh, TKDT, TKNT, GD)" style="html=1;verticalAlign=bottom;endArrow=block;edgeStyle=loopEdgeStyle;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="505" y="230" as="sourcePoint" />
            <mxPoint x="505" y="270" as="targetPoint" />
            <Array as="points">
              <mxPoint x="560" y="230" />
              <mxPoint x="560" y="270" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- 4. Acquire Redis Lock (y=320) -->
        <mxCell id="m4" value="4. acquireLock(campaign_id)" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="505" y="320" as="sourcePoint" />
            <mxPoint x="710" y="320" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- 5. Lock Acquired (y=370) -->
        <mxCell id="m5" value="5. Lock Acquired (Success)" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="710" y="370" as="sourcePoint" />
            <mxPoint x="505" y="370" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- 6. Deduct Quota (y=420..450) -->
        <mxCell id="m6" value="6. Atomic Deduct: Spent_Budget &amp; Issued_Today" style="html=1;verticalAlign=bottom;endArrow=block;edgeStyle=loopEdgeStyle;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="505" y="420" as="sourcePoint" />
            <mxPoint x="505" y="460" as="targetPoint" />
            <Array as="points">
              <mxPoint x="560" y="420" />
              <mxPoint x="560" y="460" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- 7. Call Core Issue Ticket (y=510) -->
        <mxCell id="m7" value="7. POST /core/ticketing/issue-promo-ticket" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="505" y="510" as="sourcePoint" />
            <mxPoint x="910" y="510" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- 8. Core Response (y=570) -->
        <mxCell id="m8" value="8. 200 OK (ticket_code, numbers, draw_date)" style="html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="910" y="570" as="sourcePoint" />
            <mxPoint x="505" y="570" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- 9. Release Lock (y=630) -->
        <mxCell id="m9" value="9. releaseLock(campaign_id)" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="505" y="630" as="sourcePoint" />
            <mxPoint x="710" y="630" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- 10. Send Noti Command (y=690) -->
        <mxCell id="m10" value="10. sendNotification(phone, ticket_details)" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="505" y="690" as="sourcePoint" />
            <mxPoint x="1100" y="690" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- 11. Send SMS / Push (y=750) -->
        <mxCell id="m11" value="11. SMS Brandname / Push Notification" style="html=1;verticalAlign=bottom;endArrow=block;strokeColor=#000000;fontStyle=1;fontSize=10;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1100" y="750" as="sourcePoint" />
            <mxPoint x="110" y="750" as="targetPoint" />
          </mxGeometry>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''

def build_state_machine_xml():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="Electron" modified="2026-08-02T10:40:00.000Z" agent="Vietlott SMS BA Agent" version="21.6.8" type="device">
  <diagram id="state-bank-campaign" name="5. State Machine Diagram">
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
          <mxGeometry x="360" y="40" width="160" height="50" as="geometry" />
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


        <!-- Container 2: Gift Ticket Transaction State Machine (NO TEXT OVERLAP) -->
        <mxCell id="group_tx" value="Mô Hình Trạng Thái Giao Dịch Tặng Vé (Gift Ticket Transaction State Machine)" style="shape=swimlane;whiteSpace=wrap;html=1;startSize=30;fillColor=#f8fafc;strokeColor=#334155;fontStyle=1;fontSize=12;" vertex="1" parent="1">
          <mxGeometry x="40" y="460" width="1120" height="380" as="geometry" />
        </mxCell>

        <mxCell id="st_tx_start" value="" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="group_tx">
          <mxGeometry x="30" y="160" width="30" height="30" as="geometry" />
        </mxCell>

        <!-- Row 1: Rejected -->
        <mxCell id="st_rejected" value="REJECTED&#xa;(Không đủ 7 ĐK)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_tx">
          <mxGeometry x="340" y="40" width="160" height="50" as="geometry" />
        </mxCell>

        <!-- Row 2: Happy Path -->
        <mxCell id="st_init" value="INITIATED&#xa;(Nhận Event Bank)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_tx">
          <mxGeometry x="100" y="150" width="160" height="50" as="geometry" />
        </mxCell>

        <mxCell id="st_issuing" value="ISSUING&#xa;(Gọi Core Sinh Vé)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_tx">
          <mxGeometry x="340" y="150" width="160" height="50" as="geometry" />
        </mxCell>

        <mxCell id="st_success" value="SUCCESS&#xa;(Cấp vé &amp; SMS thành công)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_tx">
          <mxGeometry x="660" y="150" width="220" height="50" as="geometry" />
        </mxCell>

        <mxCell id="st_tx_end" value="" style="ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="group_tx">
          <mxGeometry x="1050" y="160" width="30" height="30" as="geometry" />
        </mxCell>

        <!-- Row 3: Exceptions / Queue -->
        <mxCell id="st_queued" value="QUEUED_DAILY_CAP&#xa;(Bảo lưu 00:00:01)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_tx">
          <mxGeometry x="180" y="280" width="180" height="50" as="geometry" />
        </mxCell>

        <mxCell id="st_retry" value="PENDING_RETRY&#xa;(Core Timeout - Thử 3 lần)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_tx">
          <mxGeometry x="500" y="280" width="180" height="50" as="geometry" />
        </mxCell>

        <mxCell id="st_failed_manual" value="FAILED_MANUAL&#xa;(Chờ Admin xử lý)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;fontStyle=1;fontSize=11;" vertex="1" parent="group_tx">
          <mxGeometry x="760" y="280" width="160" height="50" as="geometry" />
        </mxCell>

        <!-- Transaction Transitions with clean paths -->
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
<mxfile host="Electron" modified="2026-08-02T10:40:00.000Z" agent="Vietlott SMS BA Agent" version="21.6.8" type="device">
  <diagram id="erd-bank-campaign" name="6. ERD Diagram">
    <mxGraphModel dx="1200" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="900" background="#ffffff" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Entity 1: tbl_campaign -->
        <mxCell id="e_tbl_campaign" value="&lt;b&gt;tbl_campaign (Bảng Chiến Dịch)&lt;/b&gt;&lt;hr/&gt;&lt;b&gt;PK&lt;/b&gt; | campaign_id : BIGINT&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| campaign_code : VARCHAR(50)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| campaign_name : NVARCHAR(200)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| status : VARCHAR(20)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| start_time : DATETIME&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| end_time : DATETIME&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| total_budget : DECIMAL(15,2)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| spent_budget : DECIMAL(15,2)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| daily_cap : INT&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| issued_today : INT&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| is_queue_enabled : TINYINT(1)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| created_at : DATETIME" style="rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=top;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;spacingLeft=8;spacingTop=6;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="310" height="300" as="geometry" />
        </mxCell>

        <!-- Entity 2: tbl_campaign_condition -->
        <mxCell id="e_tbl_condition" value="&lt;b&gt;tbl_campaign_condition (Cụm 7 ĐK)&lt;/b&gt;&lt;hr/&gt;&lt;b&gt;PK&lt;/b&gt; | condition_id : BIGINT&lt;br/&gt;&lt;b&gt;FK&lt;/b&gt; | campaign_id : BIGINT&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| channel_codes : JSON&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| account_status_req : VARCHAR(30)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| tknt_status_req : VARCHAR(30)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| payment_cond_type : VARCHAR(30)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| min_payment_amount : DECIMAL(15,2)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| ticket_type : VARCHAR(30)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| ticket_value : DECIMAL(15,2)" style="rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=top;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;spacingLeft=8;spacingTop=6;" vertex="1" parent="1">
          <mxGeometry x="440" y="40" width="310" height="260" as="geometry" />
        </mxCell>

        <!-- Entity 3: tbl_gift_ticket_history -->
        <mxCell id="e_tbl_history" value="&lt;b&gt;tbl_gift_ticket_history (Lịch Sử Tặng Vé)&lt;/b&gt;&lt;hr/&gt;&lt;b&gt;PK&lt;/b&gt; | history_id : BIGINT&lt;br/&gt;&lt;b&gt;FK&lt;/b&gt; | campaign_id : BIGINT&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| phone_number : VARCHAR(20)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| channel_code : VARCHAR(30)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| ticket_code : VARCHAR(50)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| draw_id : VARCHAR(50)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| ticket_value : DECIMAL(15,2)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| status : VARCHAR(30)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| issued_at : DATETIME" style="rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=top;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;spacingLeft=8;spacingTop=6;" vertex="1" parent="1">
          <mxGeometry x="40" y="420" width="310" height="260" as="geometry" />
        </mxCell>

        <!-- Entity 4: tbl_daily_cap_queue -->
        <mxCell id="e_tbl_queue" value="&lt;b&gt;tbl_daily_cap_queue (Hàng Chờ Bảo Lưu)&lt;/b&gt;&lt;hr/&gt;&lt;b&gt;PK&lt;/b&gt; | queue_id : BIGINT&lt;br/&gt;&lt;b&gt;FK&lt;/b&gt; | campaign_id : BIGINT&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| phone_number : VARCHAR(20)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| channel_code : VARCHAR(30)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| scheduled_date : DATE&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| status : VARCHAR(30)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| created_at : DATETIME" style="rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=top;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;spacingLeft=8;spacingTop=6;" vertex="1" parent="1">
          <mxGeometry x="440" y="420" width="310" height="220" as="geometry" />
        </mxCell>

        <!-- Entity 5: tbl_notification_log -->
        <mxCell id="e_tbl_noti" value="&lt;b&gt;tbl_notification_log (Log SMS/Push)&lt;/b&gt;&lt;hr/&gt;&lt;b&gt;PK&lt;/b&gt; | log_id : BIGINT&lt;br/&gt;&lt;b&gt;FK&lt;/b&gt; | history_id : BIGINT&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| phone_number : VARCHAR(20)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| noti_type : VARCHAR(30)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| message_content : NVARCHAR(500)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| send_status : VARCHAR(30)&lt;br/&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| sent_at : DATETIME" style="rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=top;fillColor=#f8fafc;strokeColor=#0f172a;fontSize=11;spacingLeft=8;spacingTop=6;" vertex="1" parent="1">
          <mxGeometry x="840" y="420" width="310" height="220" as="geometry" />
        </mxCell>

        <!-- RELATIONSHIPS WITH CLEAN ENTRY/EXIT -->
        <mxCell id="r1" value="1        1..*" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1" source="e_tbl_campaign" target="e_tbl_condition">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="r2" value="1        0..*" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" edge="1" parent="1" source="e_tbl_campaign" target="e_tbl_history">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="r3" value="1        0..*" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" edge="1" parent="1" source="e_tbl_condition" target="e_tbl_queue">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="r4" value="1        0..*" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1" source="e_tbl_history" target="e_tbl_queue">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="r5" value="1        0..*" style="edgeStyle=orthogonalEdgeStyle;html=1;strokeColor=#000000;fontStyle=1;fontSize=10;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1" source="e_tbl_queue" target="e_tbl_noti">
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
        print(f"Fixed & Re-generated: {filepath}")

    # Also update .xml copies
    for filename, xml in files_map.items():
        xml_fname = filename.replace(".drawio", ".xml")
        filepath = os.path.join(draft_dir, xml_fname)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(xml)
