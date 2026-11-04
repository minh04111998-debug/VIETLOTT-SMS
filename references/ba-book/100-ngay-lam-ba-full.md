# 100 Ngày Làm BA — ITBA Mentor (Bản Số Hóa Đầy Đủ)

> Tổng hợp 100 bài viết thực chiến Business Analyst (Trang 4–237).


---

## DAY 1/100 — BA NÊN LÀM GÌ SAU KHI TÍNH NĂNG ĐƯỢC RELEASE?

*Trang 4*

Nhiều bạn BA nghĩ:
Xong tài liệu → DEV code xong → TEST pass → Release, là hết việc. **Sai nha!** Release không phải là điểm kết thúc, mà là lúc BA chứng minh giá trị của mình.
Dưới đây là 5 việc bạn nên làm ngay sau khi sản phẩm được release:

1. **Kiểm tra thực tế trên Production**
- Đăng nhập như người dùng thật, thao tác từng bước.
- Check kỹ những thứ nhỏ nhất: nút bấm, flow xử lý, dữ liệu hiển thị...

Lưu ý: Đừng tin QA 100%. Hãy tự mình trải nghiệm thật.

2. **Ghi nhận phản hồi người dùng**
- Hỏi stakeholder, user nội bộ: “Bạn dùng thấy sao?”, “Có gì khó hiểu không?”
- Những feedback đời thực thường khác hẳn với lúc họp bàn ban đầu.

3. **Theo dõi chỉ số sử dụng (nếu có)**
- Tính năng có được dùng không? Bao nhiêu user? Rớt ở bước nào?
- Data sẽ nói thật thay cho lời khen xã giao.

4. **Hỗ trợ team sau release**
- Tester phát hiện bug? → Hỗ trợ xác minh
- DEV hỏi lại flow? → Cung cấp lại tài liệu
- CSKH cần hướng dẫn? → Chuẩn bị quick guide

Ghi nhớ: BA chủ động = BA được yêu thương.

5. **Tổng kết & cải tiến**
- Ghi lại bài học: viết thiếu gì, flow nào lủng, user chưa hiểu đoạn nào.
- Tự hỏi: "Nếu làm lại, mình sẽ làm gì khác?"

Mỗi lần tổng kết = 1 lần nâng cấp.
Tóm lại: BA giỏi không dừng lại ở viết tài liệu, mà ở chỗ: Quan sát, phản hồi, cải tiến sau khi tính năng lên sóng. Còn bạn thì sao?
- Từng “ngủ quên sau release” và bị sếp gọi hỏi bug?
- Hay từng cứu cả team nhờ việc support sau release?

**Hãy chia sẻ để cùng học hỏi nhé!**


---

## DAY 2/100 — BA KHÔNG TƯ DUY HỆ THỐNG = NGƯỜI XÂY NHÀ KHÔNG CÓ BẢN VẼ

*Trang 5–7*

Bạn có thể hoàn thành task. Bạn có thể “hoàn thành SRS đúng deadline”. Nhưng nếu bạn chỉ làm theo từng yêu cầu mà không hình dung toàn cảnh, thì hệ thống bạn xây sẽ rối như tơ vò sau vài tháng.

✦ **Một ví dụ có thật 100%:**
- Giai đoạn 1: Làm tính năng tạo đơn hàng → theo luồng của bộ phận Sales.
- Giai đoạn 2: Gắn với hệ thống kế toán → mới phát hiện thiếu thông tin doanh thu, không tách được thuế và chiết khấu.
- Giai đoạn 3: Tích hợp kho → không kiểm soát được tồn thực tế vs dự kiến, dẫn tới mất cân đối

Kết quả?
● 3 module không ăn nhập
● Dữ liệu đứt đoạn
● Càng làm càng phải chỉnh
👤 Tại sao?
Vì BA chỉ xử lý từng phần riêng lẻ, không nghĩ rằng hệ thống cần phát triển lâu dài, có khả năng mở rộng & kết nối.

▲ 3 sai lầm nghiêm trọng khi BA không tư duy hệ thống:
◆ 1. Xây từng mảnh – không kết nối
Bạn hỏi “nghiệp vụ này cần gì”,
→ Nhưng không hỏi:
- Nó ảnh hưởng đến phần nào khác?
- Dữ liệu sẽ được dùng tiếp ở đâu?
- Nếu quy trình đổi, sửa có dễ không?

💣 Kết quả: Làm đúng yêu cầu nhưng hệ thống lại... không dùng được!

◆ 2. Càng làm càng lệ thuộc DEV
Viết từng tính năng rời rạc
→ Không biết mảnh nào ảnh hưởng tới đâu
→ Không dám đề xuất, chỉ chờ DEV phân tích ngược
Lúc đó bạn không còn là người phân tích hệ thống, → bạn thành người... “giao nộp và chạy”.

◆ 3. Sản phẩm thiếu nhất quán, cực khó bảo trì
- Cùng là duyệt đơn → module A có 2 cấp, module B làm tay
- Cùng là cập nhật trạng thái → chỗ dùng API, chỗ tải Excel

● Không phải DEV cẩu thả.
■ Mà vì BA không thiết kế logic tổng thể ngay từ đầu.

● Kết luận
Bạn không cần biết viết code.
Nhưng phải biết tư duy cấu trúc – như người thiết kế ngôi nhà.
Một người xây nhà giỏi sẽ không chỉ hỏi:
“Phòng khách anh muốn to bao nhiêu?”
Mà sẽ hỏi thêm:
- “Sau này có muốn thêm tầng không?”
- “Mặt bằng chịu lực ổn không?”
- “Đường điện – nước chạy ra sao?”

BA cũng vậy.
Đừng chỉ làm tính năng.
**Hãy xây hệ thống.**

## CHECKLIST ĐÁNH GIÁ LUỒNG NGHIỆP VỤ CÓ KHẢ NĂNG MỞ RỘNG

1. **Dữ liệu có dùng được cho các bước sau không?**
- Dữ liệu đầu vào có đủ cho các bước nghiệp vụ kế tiếp?
- Có lặp lại thông tin đã có ở hệ thống khác?
- Có trùng định nghĩa hay dùng sai tên gọi giữa các bộ phận?

2. **Flow có dễ tích hợp không?**
- Luồng này có phụ thuộc hệ thống khác không?
- Nếu sau này cần gọi API / tích hợp – có sẵn điểm nối chưa?
- Có tách rõ phần xử lý nghiệp vụ – phần xử lý kỹ thuật không?

3. **Có tách được logic & giao diện không?**
- Nếu muốn đổi UI/UX, flow có cần sửa lại logic không?
- Có chôn điều kiện xử lý vào giao diện không?

4. **Có xử lý tình huống mở rộng chưa?**
- Luồng hiện tại xử lý được mấy case chính?
- Có để chừa đường cho case ngoại lệ, mở rộng nghiệp vụ, thay đổi quy trình?

5. **Có kiểm tra khả năng tái sử dụng không?**
- Flow hoặc đoạn xử lý này có thể áp dụng lại ở module khác không?
- Có bị viết lại logic giống nhau ở nhiều nơi không?

6. **Đặt ngược lại: Nếu hệ thống tăng gấp đôi user / thao tác / data – flow có chịu được không?**
- Gọi API có bị nghẽn không?
- Dữ liệu lưu có đủ cột / định danh để mở rộng không?
- Có cần refactor toàn bộ nếu thêm bước nhỏ?


---

## DAY 3/100 — 3 KỸ THUẬT BABOK GIÚP BẠN KHÔNG BỊ ĐỔ LỖI KHI KHÁCH NÓI: "TÔI CHƯA NÓI THẾ BAO GIỜ"

*Trang 8–9*

Câu nói tưởng nhẹ, nhưng có thể thổi bay cả sprint và đạp BA xuống hố.

✎ **Chuyện có thật 100%:**
Khách từng bảo trong họp: “Không cần kiểm tra tồn kho đâu, cứ tạo đơn rồi xử lý sau.”
Tôi gật đầu. DEV làm theo. 3 tuần sau UAT, khách quay lại:

> “Ủa? Không có bước kiểm tra tồn à? Tôi đâu có nói bỏ cái đó?”

● Tôi đứng hình.
👤 DEV chửi.
✎ TEST sửa.
■ PM dời release.
💊 Và tôi? Im lặng chờ bị phán xử.

✖ Vấn đề không phải do khách quay xe.
■ Mà là do BA không xác minh đủ chặt.
Và đó là lúc tôi biết mình vừa bỏ qua **3 kỹ thuật cơ bản trong BABOK** những thứ tưởng lý thuyết, nhưng cực kỳ giải cứu thực chiến.

▲ **Kỹ thuật 1: Confirm Elicitation Results**
▼ **Tôi đã làm gì sai?**
- Nghe miệng → hiểu miệng → code luôn
- Không recap lại
- Không flow, không exception

🔧 **Đáng ra phải làm:** “Luồng tạo đơn KHÔNG có bước kiểm tra tồn kho. Đơn vẫn tạo được nếu sản phẩm hết hàng. Anh/chị xác nhận giúp em trước 17/3 để DEV triển khai đúng.”
👉 Không gửi = không có bằng chứng = bạn mất quyền bảo vệ chính mình.

▲ **Kỹ thuật 2: Validate Requirements (BABOK 7.3)**
📌 **Sai lầm của tôi:**
- Tự suy đoán: "Chắc khách đã kiểm tra tồn kho ở chỗ khác rồi.”
- Nghĩ là hợp lý → không hỏi thêm, không xác minh

🔧 **Đáng ra phải làm:**
“Giả định: Hiện khách đang kiểm kho thủ công qua Excel, nên giai đoạn 1 không cần kiểm tra tồn kho trong hệ thống. Sẽ xác nhận lại khi tích hợp kho ở giai đoạn 2.”
👉 Giả định mà không xác minh = mìn chôn sẵn dưới hệ thống.

● BABOK nhấn mạnh Validate Requirements là quá trình bảo đảm yêu cầu hỗ trợ mục tiêu kinh doanh và không mâu thuẫn với các mục tiêu khác nghĩa là BA phải làm rõ mọi logic, giả định ngầm.

▲ **Kỹ thuật 3: Approve Requirements (BABOK 5.5)**
📌 **Sai lầm của tôi:**
- Ai nói cũng tưởng là người có quyền chốt
- Không ghi rõ ai xác nhận, lúc nào, qua kênh nào

🔧 **Đáng ra phải làm:** “Nội dung này được chị Lan Trưởng phòng Vận hành xác nhận qua Zalo lúc 15:23 ngày 10/3. Screenshot đính kèm.”
👉 Không có xác nhận chính thức = bạn không có tư cách chứng minh điều gì.

● BABOK định nghĩa Approve Requirements là hoạt động đảm bảo rằng các stakeholder có thẩm quyền đã xem xét và đồng ý với yêu cầu trước khi chuyển sang bước tiếp theo.


---

## DAY 4/100 — 3 KỸ THUẬT BABOK GIÚP BẠN XỬ LÝ YÊU CẦU GẤP MÀ KHÔNG VỠ TIẾN ĐỘ

*Trang 10–11*

"Quan trọng lắm!", "Phải có ngay!", "Còn chờ gì nữa?"
Bạn không sai khi làm đúng yêu cầu.
Nhưng nếu bạn không quản trị được kỳ vọng và ưu tiên, thì:
- Backlog sẽ ngày càng phình to
- Sprint nào cũng vỡ plan
- Và người bị truy trách nhiệm đầu tiên: chính là bạn – BA của dự án

● **3 kỹ thuật từ BABOK giúp bạn đứng vững trước áp lực yêu cầu gấp**

■ **1. MoSCoW – Ưu tiên không phải vì khách nói gấp**
Dùng khi:
Bạn bị yêu cầu xử lý 5 task “must have” trong cùng 1 sprint
✖ Sai:
- Dán nhãn “ưu tiên cao” vì... nghe có vẻ quan trọng
- Không kiểm tra xem task đó ảnh hưởng gì nếu chưa làm

■ Đúng:
- Hỏi thẳng: "Không làm cái này, hệ thống có chạy được không?"
- Ưu tiên theo: ảnh hưởng đến KPI, tần suất sử dụng, rủi ro nếu lỗi
- Phân loại rõ: Must – Should – Could – Won’t

📌 Ví dụ:
Khách muốn “thêm bộ lọc nâng cao”
→ Không ảnh hưởng tính năng chính
→ Could Have, không phải Must

■ 2. Stakeholder Analysis – Ưu tiên người quyết định, không phải người nói to
Dùng khi:
Bạn nhận yêu cầu từ 3 bộ phận khác nhau – không biết bên nào cần xử lý trước
✖ Sai:
- Ưu tiên theo cấp bậc hoặc “bên nào gắt hơn”
- Không phân loại người dùng vs người duyệt

■ Đúng:
- Chia stakeholder thành: Người dùng – Người quản lý dữ liệu – Người có quyền chốt
- Gán trọng số ưu tiên theo vai trò & ảnh hưởng

📌 Ví dụ:
Trưởng phòng Kinh doanh đòi thêm “trường sở thích khách hàng”
→ CRM bảo không ai điền
→ Không phải người thao tác, không chịu trách nhiệm
→ Lùi

■ **3. Expectation Management – Vẽ đường kỳ vọng, đừng để khách tưởng sprint là cái túi thần kỳ**
Dùng khi:
Sprint đang chạy, khách muốn thêm task
✖ Sai:
- Gật đầu nhồi thêm task, không nói rõ hệ lụy
- Mỗi lần “thêm chút xíu” là backlog bung như dây thun đứt

■ Đúng:
- Truyền thông rõ ràng: gì làm được, gì phải trade-off
- Giữ tính minh bạch & log lại quyết định

📌 Ví dụ:
Khách đòi thêm popup cảnh báo
→ Nếu không nói trước ảnh hưởng đến task chính
→ Cả sprint trượt deadline
→ Blame đổ đầu BA


---

## DAY 5/100 — 3 KỸ THUẬT BABOK GIÚP BA TƯ DUY LỖI – VIẾT LOGIC CHẶT CHẼ, KHÔNG BỊ LỌT CASE

*Trang 12–13*

BA giỏi không phải người nghĩ được nhiều tính năng,
Mà là người đủ tỉnh để hỏi:
👉 “Nếu sai thì sao?”
👉 “Nếu người dùng thao tác ngược thì sao?”
👉 “Nếu server lag, mất kết nối thì sao?”

● **1. Exception Flow – Tư duy lỗi = tư duy sống sót**
■ BABOK Technique: Scenario & Use Case, Exception Handling
- Input: Tập hợp yêu cầu chức năng từ stakeholder
- Process: Vẽ flow, xác định điểm có thể phát sinh lỗi
- Output: Luồng chính + luồng phụ (Exception Flow)

▲ Sai thường thấy:
- Chỉ mô tả “đúng thì làm gì”, không nói “sai thì sao”
- Coi exception là việc “dev tự xử lý”

■ Phải thấm:
BA không viết code, nhưng phải vẽ được bức tranh toàn cảnh, kể cả lúc mọi thứ đổ bể.

● **2. Risk Analysis – Tính trước điểm đứt gãy**
■ BABOK Technique: Risk Analysis and Management
- Input: Thông tin hệ thống hiện tại + yêu cầu mở rộng
- Process: Phân tích điều gì có thể sai lệch: dữ liệu – user – kết nối – tích hợp
- Output: Danh sách rủi ro & đề xuất xử lý

🧪 Ví dụ:
- Người dùng nhấn “Xác nhận” 2 lần → Giao dịch bị nhân đôi
- API chậm → Giao diện loading mãi → Người dùng tưởng lỗi, thoát ra

■ Nhớ:
BA không thể loại bỏ rủi ro,
Nhưng phải nhìn thấy nó trước,
Để đội kỹ thuật kịp gia cố móng nhà.

● **3. Non-functional Scenarios – Không có nhưng vắng là chết**
■ BABOK Technique: Non-Functional Requirements Analysis
- Input: Functional spec hiện có
- Process: Đặt câu hỏi: hiệu năng? bảo mật? trải nghiệm nếu quá tải?
- Output: Yêu cầu không chức năng để phòng bug logic – trải nghiệm

✖ Sai thường gặp:
- Không mô tả timeout
- Không định nghĩa trạng thái hệ thống khi lỗi xảy ra

■ Output tốt phải trả lời được:
- Nếu mất kết nối thì sao?
- Có cần retry không?
- Báo lỗi bằng gì?

💬 Một chuyện thật:
Mình từng làm một dự án, vẽ diagram và spec cực kỳ chi tiết –
nhưng không có dòng nào nói:
“Nếu người dùng chọn option A rồi back lại thì sao?”
Kết quả:
→ DEV không xử lý → PROD lỗi → rollback.
→ BA bị gọi lên nhận lỗi.
→ Cả team mệt.
Vì Exception không được viết ra, nên hệ thống tự đổ gãy.

💬 Kết
Tổ tiên giữ nước vì biết lo trước khi có giặc.
BA giữ hệ thống vững vì biết đặt câu hỏi trước khi lỗi xảy ra.


---

## DAY 6/100 — MỘT NGÀY LÀM BA MANAGER CỦA TÔI

*Trang 14–15*

Tôi không còn là người viết đặc tả từng dòng SRS. Tôi cũng không còn là người ngồi daily với Dev mỗi sáng. Nhưng tôi là người mà cả team BA sẽ gọi... khi mọi thứ bắt đầu rối.

**Tôi không còn làm BA như trước.**
Giờ tôi làm người đứng sau. Không để kiểm soát. Mà để giữ cho từng người trong team có thể tiếp tục đi mà không thấy đơn độc.

☀️ **Buổi sáng**
Không mở task, chỉ mở đoạn tin nhắn gửi lúc khuya. "Anh ơi, luồng này em chưa chắc chốt được logic theo hướng nào..." Tôi không sửa tài liệu giùm. Tôi không nói: “Cái này em phải biết rồi chứ.” Tôi chỉ nhắn: “Em set họp với đầu mối đi. Có gì anh join cùng.
Mình làm nghề này không để gồng cho giỏi, mà để hiểu cho kỹ.” Làm BA Manager – nhiều khi không cần nói nhiều, chỉ cần có mặt đúng lúc.

📖 **Buổi trưa**
Rà lại dự án – không phải để theo dõi, mà để không ai bị bỏ lại 3 dự án. 3 team. 3 câu chuyện khác nhau:
- Một team bị chậm vì thay đổi yêu cầu phút chót
- Một team chuẩn bị go-live nhưng nghiệp vụ chưa thông end-to-end
- Một bạn BA thì đang loay hoay do chưa chốt đầu bài nghiệp vụ

Tôi không ôm hết. Tôi không cầm tay chỉ việc. Tôi chỉ vẽ lại bản đồ để từng người nhìn thấy mình đang ở đâu, và sắp tới cần vượt qua đoạn nào.

💬 **Buổi chiều**
Ngồi nghe – không phải để đánh giá, mà để đồng hàn. Bạn BA junior trình bày trước Business. Khi bị hỏi: “Luồng này dựa trên hành vi thực tế nào của garage?” – bạn ấy hơi khựng. Tôi không ngắt lời. Chỉ nhắn một dòng: “Gợi lại case thực tế hôm khảo sát đi em.” Bạn nói lại, lần này gắn vào một ví dụ cụ thể. Business gật. Tôi không nói gì thêm. Không phải để chứng minh vị trí. Mà để bạn ấy biết có người đang lắng nghe, và sẵn sàng đỡ nếu cần.

💼 **Cuối giờ**
Phỏng vấn một bạn BA trẻ hơn tôi 10 tuổi, Bạn hỏi: “Team anh có ai hướng dẫn không?”
Tôi chỉ cười. Không hứa mentor. Không khoe coaching. Tôi chỉ biết:
- Mình vẫn đang rep tin nhắn khuya
- Vẫn ở lại sau giờ làm để cùng team OT
- Vẫn gõ comment SRS từng đoạn vì không muốn bạn nào bị gọi tên trước mặt Dev

🌙 **Tối**
Một mình một màn hình và lời hứa viết nốt 100 ngày. Tôi viết tiếp bài thứ 06 – 07 – 08. Không cần người khen hay. Không cần đếm like. Chỉ cần nhớ: Mình từng ở vị trí đó loay hoay, ngợp tài liệu, áp lực go-live. Và nếu có ai đang giống mình ngày trước, thì ít nhất họ đọc được một bài... để thấy rằng mình không lẻ loi.


---

## DAY 7/100 — 3 KỸ THUẬT BABOK GIÚP BA ĐO LƯỜNG HIỆU QUẢ TÍNH NĂNG.

*Trang 16–17*

Bạn từng đề xuất một tính năng, tự tin lắm, tâm huyết lắm. Nhưng sau khi release:
Không ai dùng. Không ai đoái hoài. Không tạo impact.
- Không phải do DEV code sai.
- Không phải do UI xấu.
- Mà vì ngay từ đầu bạn không nghĩ đến chuyện đo lường.

“Viết tính năng mà không đo được hiệu quả thì không phải là làm BA – đó là đoán mò.”
Muốn tránh cảnh đó, đây là 3 kỹ thuật trích từ BABOK, cộng với một "nắm hành" từ thực chiến

● **1. Gắn chỉ số ngay từ khâu đề xuất (Theo BABOK – Solution Evaluation)**
Mỗi tính năng đều phải trả lời rõ ràng:
“Tính năng này giúp business tăng cái gì / giảm cái gì?”
Nếu không trả lời được – bỏ.
Ví dụ:
- Bạn đề xuất chatbot khuyến mãi → nghĩ là tăng tương tác.
- Push xong, KH không bấm vì đã tắt thông báo từ lâu.
- Sếp hỏi: “Có thống kê bao nhiêu người click không?”

Bạn im. Không tracking. Không KPI. Không gì cả.

■ **2. Tư duy số liệu khi viết yêu cầu (Theo BABOK – Measurement Criteria)**
Viết xong mà không tracking được, không báo cáo được thì bạn đang "cầu nguyện", chứ không làm sản phẩm.
Ví dụ:
- Bạn đề xuất tính năng lọc phụ tùng theo hãng xe.
- Release xong – KH vẫn nhắn Zalo hỏi phụ tùng, không ai dùng filter.

Dev bảo: “Tốn 3 ngày làm cái không ai dùng.”
Sếp hỏi: “Tính năng này để làm gì vậy em?”. Bạn không trả lời được. Bạn không chứng minh được giá trị. Bạn mất tiếng nói.

🧪 **3. Viết acceptance criteria sao cho test & đo được (Theo BABOK – Requirements Validation)**
Đừng viết kiểu chung chung: “Cho phép khách đánh giá sau khi sửa xe.”
→ Câu này tưởng đúng nhưng không đo được gì, không giúp ra quyết định.

Viết chuẩn nên là:
“Sau mỗi lượt sửa xe, hiển thị form đánh giá gồm: chấm điểm từng dịch vụ (rửa xe, thay nhớt, sửa phanh...), thời gian phản hồi dưới 2s, tỷ lệ KH hoàn thành khảo sát tối thiểu 30%.”

Vì sao cần viết rõ vậy? Vì nếu không, bạn sẽ rơi vào tình huống “form đánh giá tưởng xịn nhưng flop” như sau: Ví dụ: Bạn đề xuất: “Sau khi xe sửa xong, gửi form đánh giá cho khách để đo chất lượng garage.”
Nghe hay, ai cũng gật đầu.
- Dev làm xong, push lên app.
- KH thấy form → bấm đại 5 sao cho xong, hoặc bấm tắt.
- Bạn không biết KH đang hài lòng thật hay... muốn thoát nhanh.

Bạn cũng không phân loại theo từng dịch vụ (chăm sóc xe, thay dầu, rửa xe...),
nên không biết phần nào tốt, phần nào cần cải thiện.
Kết quả:
- Có vài ngàn lượt đánh giá 5 sao... nhưng không ra insight gì hết
- Không giúp nâng cấp dịch vụ
- Không hỗ trợ ra quyết định nào cho quản lý garage

BA tưởng đang “đo chất lượng”, nhưng thực ra chỉ đang gom data vô nghĩa. Điều khác biệt giữa BA thường thường và BA đỉnh cao:
- BA thường viết xong là xong.
- BA đỉnh thì viết, theo dõi, phân tích và cải tiến.

Tính năng không ai dùng = phí công cả team. Không đo được hiệu quả = tự bắn vào chân mình.
**3 việc BA cần làm ngay hôm nay:**
- Đừng đề xuất nếu không gắn được chỉ số cụ thể.
- Viết tiêu chí rõ để team test được và bạn đo được.
- Chủ động tracking – đừng đợi bị hỏi mới cuống.


---

## DAY 8/100 — HỌC GÌ ĐỂ LÊN SENIOR BA? KHÔNG PHẢI CỨ LÀM LÂU LÀ TIẾN XA. TIẾN XA LÀ NHỜ LÀM ĐÚNG VÀ HỌC ĐÚNG THỨ CẦN HỌC.

*Trang 18–19*

"Tôi làm BA 4 năm rồi, sao vẫn chưa được tin tưởng giao vai trò cao hơn?" Không hiếm người đặt câu hỏi này. Nhưng phần lớn đều vướng ở một điểm: Chưa trang bị đúng kỹ năng để xử lý bài toán lớn hơn.
→ Viết tài liệu? Ổn.
→ Ghi nhận yêu cầu? Không còn bỡ ngỡ.
→ Vẽ flow? Làm được.

Nhưng...BA cấp độ cao hơn là người:
→ Nhìn thấy rủi ro trước khi hệ thống được xây dựng
→ Biết chọn đúng yêu cầu cần triển khai
→ Gắn kết team khi dự án gặp vấn đề

Một tình huống thật: Khách hàng yêu cầu cho phép người dùng chỉnh sửa số điện thoại. BA chỉ thấy đó là 1 field nhỏ – không phân tích gì thêm. Dev làm nhanh, test OK, go-live. 1 tuần sau:
- Gần 2000 đơn hàng không tìm được người nhận vì số mới không khớp với thông tin giao vận đã tạo
- Call center không gọi được user vì ticket chăm sóc vẫn dùng số cũ
- Dữ liệu thống kê bị lệch vì hệ thống tracking theo số điện thoại đầu tiên

Lỗi nằm ở BA không xác định số điện thoại là dữ liệu định danh, gắn với nhiều hệ thống liên quan (vận đơn, CSKH, phân tích dữ liệu).

Theo BABOK: lỗi ở Impact Analysis và Data Dependency Mapping – không bóc được, là mở cửa cho hệ thống gãy dây chuyền. Vậy học gì để không lặp lại những sai lầm như vậy?
- Không phải thêm template.
- Không ôn lại lý thuyết cũ.

Mà là học để:
→ Lập kế hoạch BA bài bản
→ Phỏng vấn & workshop hiệu quả
→ Phân tích tác động & thay đổi đa chiều

Truyền đạt yêu cầu rõ – từ lúc nói miệng đến lúc chạy ổn định


---

## DAY 9/100 — 3 KỸ THUẬT BABOK GIÚP BẠN TRÁNH VIẾT REQUIREMENT ĐỂ RỒI TOANG VÌ CONSTRAINT

*Trang 20–21*

**Bạn từng bị sếp mắng... chỉ vì làm đúng yêu cầu chưa?**
Tôi từng dính cú đó. Làm feature điểm danh theo đúng lời sếp. Viết đủ flow, mô tả rõ ràng, test pass. 3 ngày sau: bị gọi lên và gỡ app.
**Sếp bảo:**
“Làm app điểm danh đi, cho nhân viên tự check-in bằng điện thoại. Vân tay lỗi thời rồi.”

Nghe hợp lý và có vẻ dễ! Tôi viết tài liệu, mô tả chức năng, giao cho dev. QC test pass. Go-live.

**3 ngày sau, sếp gọi lên gắt gỏng:**
"Nhân viên check-in từ quán cafe à? App kiểu gì khuyến khích gian lận vậy? Gỡ liền!"
Tôi cứng họng. Vì tôi không sai chỉ là chưa bóc constraint.

**Sai lầm của BA non kinh nghiệm là:**
- Nghe yêu cầu tưởng rõ rồi
- Không phân tích constraint
- Không verify khả thi
- Không lường trước rủi ro

Kết quả:
- Feature đúng specs → không dùng được
- Dev tốn công
- Sếp mất niềm tin → rollback → xóa app

**3 kỹ thuật BABOK giúp BA thoát phốt**

**Constraint Analysis**
Nói nghe hay lắm, nhưng constraint không cho làm thì khác gì mơ giữa ban ngày.
**Business:** Dữ liệu chấm công ảnh hưởng tính lương → phải chính xác
**Technical:** App chưa có GPS, chưa xác minh người dùng
**Operational:** Không có người duyệt lại check-in

**Verify Requirements**
Yêu cầu tưởng rõ mà chưa chắc làm được. Yêu cầu viết vào tài liệu: “Tự động ghi nhận giờ làm việc khi nhân viên bấm check-in.” Nhưng BA không verify xem:
- Có rule nào để xác định ca sáng/chiều không?
- Nhân viên đi sớm 30 phút có được tính không?
- Nếu check-in lúc 2h sáng thì sao?
- Giờ nghỉ trưa có tự tách được không?

Không verify → dev phải đoán → tính năng ra đời với 1001 câu hỏi chưa ai trả lời.

**Risk Analysis**
Làm được không quan trọng bằng: làm xong có bị lạm dụng không ?
**Tình huống:**
Bạn triển khai xong tính năng check-in tự do. Không giới hạn địa điểm. Không giới hạn thời gian.
**Rủi ro:**
- Nhân viên ngồi quán cafe cũng chấm công được
- Có người check-in 2h sáng để... đủ giờ
- Dữ liệu sai → HR không dám dùng → rollback hệ thống

BA không phân tích risk → tính năng thành bằng chứng thất bại của “chuyển đổi số”

■ **Checklist 5 câu hỏi sống còn của BA thực chiến**
✔ Có ràng buộc nào khiến yêu cầu này không triển khai được không?
✔ Nếu làm xong mà không dùng được, vì cái gì?
✔ Có giả định nào mình đang tin mà chưa verify không?
✔ Dev có đủ công cụ, dữ liệu để làm tính năng này không?
✔ Người dùng có thực sự vận hành được không?


---

## DAY 10/100 — PO TỰ VẼ UI/UX RỒI BẢO BA "CHECK LẠI HỘ" TRÒ CHƠI ĐỔ LỖI BẮT ĐẦU?

*Trang 22–23*

**Câu chuyện có thật:** Tuần trước, một bạn BA nhắn tôi, giọng đầy bức xúc: “Em nghỉ phép mấy hôm. Quay lại thì PO đã confirm hết UI với designer rồi. Em chỉ còn mỗi việc soi chính tả và check logic. Mà cái logic thì sai be bét... Giờ ai chịu trách nhiệm?”

**Quen không?**
- PO bảo “anh duyệt rồi”
- Designer bảo “PO đồng ý mà”
- Còn BA thì thành người ngồi ngoài flow – bị giao trách nhiệm nhưng không có quyền

**Kết quả:**
- Giao diện nhìn đẹp
- Luồng logic thì toang
- Cả team phải làm lại
- Deadline vỡ
- Căng thẳng nổ

● Sai từ đâu?
Sai từ vai trò
- PO nghĩ: "Mình hiểu người dùng nhất → confirm luôn UI"
- Designer: "PO duyệt là xong"
- BA không được involve từ đầu → vào sau để vá lỗi

👉 Và thế là:
- Giao diện nhìn xịn nhưng không thể chạy
- DEV còng lưng sửa
- Tester kêu trời
- BA ôm lỗi không hiểu vì sao

■ **Gỡ bằng kỹ thuật chuẩn BABOK - BA không phải người đến sau**
Muốn tránh cảnh này, BA cần áp dụng 3 kỹ thuật đơn giản nhưng hiệu quả:

🛠️ **1. Stakeholder Analysis**
Ai làm gì? Ai duyệt gì? Ngay từ đầu dự án, cần phân rõ:
- PO: Người chia sẻ insight từ khách hàng
- BA: Người dẫn dắt logic nghiệp vụ
- UI/UX: Người lên giao diện từ flow đã được thống nhất

**Không rõ vai → ai cũng làm → mà không ai chịu trách nhiệm**

💬 **2. Collaborative Modeling**
UI không chỉ để đẹp. Phải đúng. Trước khi vẽ, nên:
- Ngồi chung: PO – BA – UI/UX
- BA chia logic + rule
- UI/UX dựng giao diện dựa trên nghiệp vụ
- PO feedback trải nghiệm

→ **Giao diện sẽ chạy được, chứ không chỉ nhìn được**

■ **3. Review Session**
Vẽ đến đâu check đến đó. Đừng để “vẽ xong hết rồi mới hỏi BA đâu?”. Mỗi lần xong 1 flow:
- BA review logic
- PO xác nhận trải nghiệm
- UI mới được finalize

**Làm sớm, sửa sớm → khỏi toang muộn**


---

## DAY 11/100 — KHI BA GẬT ĐẦU VÌ NGẠI HỎI LẠI

*Trang 24–25*

Mất 2 phút đọc – nhưng nếu bạn là BA mới, đây có thể là 2 phút đáng nhất tuần này.

Sếp: “Màn này làm giống bên XYZ nhé, flow bên đó tối ưu rồi. Em nắm rồi làm luôn nha.”
Tôi gật đầu. Và tôi biết... hình như có điều gì đó chưa ổn. Nhưng tôi vẫn gật. Lúc đó tôi là một BA mới. Không ai ép tôi làm sai. Chỉ là... tôi không dám hỏi lại. Tôi nghĩ:
“Chắc là đúng rồi.”
“Mình hỏi thì kỳ lắm.”
- Tôi nhìn vài ảnh chụp UI, tưởng mình hiểu
- Tôi tự vẽ lại luồng theo suy diễn
- Tôi viết tài liệu theo logic trong đầu
- DEV làm
- TEST chạy

Mọi người đều tưởng là xong.
■ Cho đến khi người dùng thật bắt đầu sử dụng:
- Một bước xử lý bị thiếu
- Một trường hợp ngoại lệ không được đề cập
- Một logic ngầm không ai viết ra – và tôi cũng không hỏi tới

✖ Tôi không hỏi không phải vì không biết. Mà vì... tôi ngại.
- Sợ làm phiền người khác
- Sợ bị đánh giá
- Sợ bị xem là “chưa hiểu gì à?”
- Sợ làm trái ý sếp

Tôi đã cảm thấy có gì đó không ổn. Nhưng tôi im. Và chính khoảnh khắc đó không sai vì non, Mà sai vì im lặng.

● **3 kỹ thuật BABOK giúp BA phân tích khi sếp bảo làm giống bên XYZ**

**Benchmarking – So sánh có chiều sâu**
Đừng chỉ nhìn UI hay ảnh chụp.
Hãy hỏi: hệ thống kia hoạt động thế nào?
Có gì khác với bên mình?

**Risk Analysis – Dự đoán trước khi người dùng vướng lỗi**
Nếu thao tác sai thì sao?
Nếu thiếu dữ liệu thì xử lý thế nào?
Nếu hiểu nhầm flow – có hậu quả gì?

**Stakeholder Needs – Hiểu đúng người, đúng nhu cầu**
Sếp muốn nhanh, gọn.
Người dùng muốn rõ, đúng.
Tính năng tốt là thứ cân bằng được cả hai.

■ **Checklist trước khi bạn “làm giống bên kia”**
- Tính năng này đang giải quyết vấn đề gì – và vấn đề đó có thật ở hệ thống của bạn không?
- Dữ liệu đầu vào và đầu ra bên bạn có đủ như hệ thống mẫu không?
- Quy trình xử lý có khác biệt theo vai trò, khách hàng, phân hệ?
- Có trường hợp ngoại lệ hoặc nghiệp vụ đặc thù nào không thể bê nguyên xi?
- Sau khi triển khai, ai là người sử dụng và họ cần hỗ trợ gì để sử dụng tốt?

▲ Nếu bạn đọc tới đây mà vẫn nghĩ: “Lại là BA đổ lỗi à...”. Thì có lẽ bạn chưa từng là người phải ngồi giữa flow mơ hồ, deadline sát nút, và một team đang đợi đặc tả để kịp sprint. Tôi không viết bài này để chứng minh BA là nạn nhân. Tôi viết để nhắc những người mới – hoặc sắp làm BA:
❗ Làm BA không phải để đoán ý sếp.
Mà là để hỏi lại – khi cả team tưởng là hiểu rồi.


---

## DAY 12/100 — BA CÓ CẦN BIẾT CODE KHÔNG?

*Trang 26–27*

**Câu hỏi tưởng cũ, nhưng mỗi lần nghe lại là một lần muốn kể chuyện**

Chiều qua, mình có dịp quay lại FPT Polytechnic để chia sẻ về nghề BA cho các bạn sinh viên IT. Và đúng như dự đoán, câu hỏi xuất hiện ở gần cuối buổi:
“Anh ơi, BA có cần biết code không ạ?”
Mình bật cười – không phải vì câu hỏi ngây ngô. Mà vì... mình cũng từng là người hỏi y chang như vậy cách đây vài năm. Rất nhiều người nghĩ:
- “Phải biết viết code thì mới làm được BA kỹ thuật”
- “Không học công nghệ thì khỏi mơ làm BA”

**Hoặc:**
- “Chỉ cần giao tiếp tốt là làm được BA rồi, kỹ thuật để Dev lo!”

**Và kết quả là:**
- Người thì tự loại mình ra khỏi nghề vì sợ kỹ thuật
- Người thì làm BA kiểu “ghi chép viên”, không nắm được hệ thống đang vận hành ra sao

■ **Thật ra... BA không cần biết code – nhưng nên hiểu hệ thống chạy ra sao**
Mình không nghĩ BA phải viết được code. Không ai đòi bạn thành Dev. Nhưng nếu làm BA, thì ít nhất bạn nên hiểu:
- Khi người dùng bấm nút “Gửi” – đằng sau hệ thống làm gì?
- Dữ liệu đi từ đâu – qua đâu – ai xử lý – lưu ở đâu?
- Khi có lỗi xảy ra – là do hệ thống, do logic sai, hay do thiếu xử lý?

**Hiểu những điều này không phải để lấn sân kỹ thuật. Mà để bạn:**
- Viết yêu cầu rõ ràng hơn
- Làm việc với Dev mạch lạc hơn
- Và không hoang mang khi hệ thống chạy sai với kỳ vọng

**Cá nhân mình thấy:** Hiểu cách hệ thống vận hành là nền tảng quan trọng nhất để BA trưởng thành.

👤 Mình nhớ có lần nói chuyện với một chị CTO...Một người chị mình rất nể, làm sản phẩm hơn 10 năm, từng nói với mình một câu rất thật:
“Em có thể train BA viết tài liệu, lên flow, push Dev...Nhưng cái khó nhất là làm sao để các bạn có được tư duy hệ thống.”

Và mình cũng hiểu vì sao nhiều bạn BA – dù cố gắng – vẫn chật vật trong dự án:
- Thiếu nền tảng kỹ thuật → sợ khi nghe đến API
- Không rõ backend xử lý gì, frontend làm gì
- Không biết dữ liệu đi đâu, logic nằm ở đâu → viết tài liệu thiếu trước hụt sau
- Và quan trọng nhất: không đủ tự tin đứng trước Dev hay QA vì sợ hỏi sai

🎓 Vì vậy, mình có làm một mini course: Technical for BA
Chia sẻ những điều căn bản nhưng thực tế nhất mà một BA nên hiểu khi bước vào làm việc với hệ thống. Đây không phải khóa học thần kỳ. Không giúp bạn “biến hình” thành Technical BA chỉ sau vài giờ học. Nhưng nếu bạn:
- Chưa từng vọc API
- Thấy JSON là muốn lùi
- Hay bối rối khi Dev hỏi

Thì mình tin course này sẽ giúp bạn bắt đầu hiểu được cách hệ thống vận hành – để từ đó làm BA tự tin hơn một chút mỗi ngày.


---

## DAY 13/100 — DATA OBJECT BÍ KÍP PHÂN TÍCH NGHIỆP VỤ CỦA TÔI

*Trang 28–29*

Một câu hỏi rất quen khi làm với các bạn BA mới vào nghề:
"Làm sao để biết hệ thống cần lưu những thông tin gì?
Em nên bắt đầu dựng data object từ đâu khi chưa có bảng DB?"

Tôi không ngạc nhiên. Vì trước đây, tôi cũng từng loay hoay như vậy.
- Không biết trường nào bắt buộc
- Không chắc validate ra sao
- Không rõ object cần những trạng thái nào, liên quan gì đến màn hình, báo cáo hay hành vi người dùng

Và từ sự rối đó, tôi dần hình thành một cách làm:
👉 **Dựng data object từ hành vi nghiệp vụ**

🧩 **Bước 1 – Xác định object từ hành vi nghiệp vụ**
Tôi không bắt đầu từ ERD. Tôi không chờ hệ thống chạy mới lần ngược lại. Tôi bắt đầu từ một câu hỏi: "Người dùng đang tạo, duyệt, chỉnh sửa cái gì?". Thứ đó chính là data object. Ví dụ:
- Garage thao tác với một phiếu xuất kho → Tôi có Phiếu Xuất Kho
- Người dùng đăng ký tài khoản → Tôi có Hồ sơ Khách Hàng
- Nhân viên xác nhận đơn hàng → Tôi có Đơn Giao Dịch

🧩 **Bước 2 – Gom hành vi xoay quanh object**
Với mỗi object, tôi làm rõ:
- Ai tạo ra nó?
- Nó đi qua những trạng thái gì?
- Dữ liệu đó hiển thị ở đâu?
- Có xuất hiện trong báo cáo không?
- Có là input cho chức năng khác không?

Làm rõ những câu hỏi này giúp tôi đảm bảo object không bị rời rạc. Mọi thứ đều nằm trong một dòng chảy nghiệp vụ mạch lạc.

🧩 **Bước 3 – Mô tả rõ cấu trúc bên trong object**
Tôi xác định từng trường dữ liệu:
- Trường nào là bắt buộc theo nghiệp vụ?
- Có ràng buộc dữ liệu gì cần làm rõ không? (độ dài, định dạng, không trùng...)
- Có giá trị mặc định không?
- Có cần phân loại theo enum không?
- Có logic nào phụ thuộc theo trạng thái object?

Ví dụ với Phiếu Xuất Kho:
- MaPhieu: sinh tự động, không trùng, độ dài từ 5 đến 20 ký tự
- NgayXuat: mặc định là ngày hiện tại, không được vượt quá ngày hôm nay
- TrangThai: enum gồm "Khởi tạo", "Đã duyệt", "Đã huỷ"
- GhiChu: không bắt buộc, tối đa 255 ký tự

Tôi ghi toàn bộ logic này trong tài liệu Excel.

💬 Cách làm này dựa vào tư duy:
- Phân tích luồng nghiệp vụ → object → field
- Mapping chặt giữa object – use case – màn hình

🎁 Một chút chia sẻ nhỏ:
- Tôi có một file Excel mẫu dùng để dựng data object cho dự án thật.
- Không lý thuyết, không format nặng – chỉ có cấu trúc rõ ràng và dễ áp dụng.
- Tôi sẵn sàng chia sẻ file này – chỉ cần bạn để lại một bình luận và chia sẻ bài viết để nhận thông tin nhé.
- Xem như một ly cà phê sáng để bắt đầu ngày mới với cách làm bài bản hơn cho nghề BA


---

## DAY 14/100 — 3 DẠNG COMMENT DỄ KHIẾN BA RƠI VÀO BẪY TƯỞNG ĐÃ DONE RỒI

*Trang 30–31*

Không phải bug, không phải logic sai, không phải thiếu tài liệu.
Nhiều pha toang trong dự án bắt đầu chỉ từ... **một câu comment tưởng vô hại.**

▲ **1. Những comment tưởng vô hại, nhưng khiến BA “đóng task” trong vô thức**
- “Tạm ổn rồi, mai check nốt”
- “Cái này để release sau nhé”
- “Không tái hiện được bug”

Dev nói vậy, Test gật đầu, và bạn... nghĩ là done. Nhưng thật ra:
- “Tạm ổn” là... chưa xong
- “Để sau” = không có task chính thức
- “Không tái hiện được bug” = chưa hiểu gốc rễ chứ không phải bug biến mất

📌 **Sai lầm BA gặp:**
- Bạn bỏ qua bước Verify Requirements (BABOK 7.2)
- Bạn cũng không Confirm Transition Requirements (BABOK 7.6)
- → Tưởng đã xong, nhưng thật ra mới xong... 80%

■ **Cách làm đúng:**
- Yêu cầu Dev/Test đưa ra bằng chứng: log, API, kết quả test rõ ràng
- Walkthrough lại với Test các case edge
- “Để sau” thì phải có task riêng, log rõ, assign người xử lý

▲ **2. “Khách bảo bỏ rồi” – Nhưng không ai log lại**
Nghe từ PM. Nghe từ PO. Nghe từ Dev. Bạn không thấy task update, nhưng vì “nghe chắc rồi” → bạn tự gỡ khỏi flow. Không cập nhật tài liệu. Không hỏi lại. Không có gì để backup. Hai tuần sau khách hỏi:
“Ủa, sao phần đổi mã giảm giá không thấy đâu?”
“Chị có bảo bỏ hả? Không nhớ vậy nha...”

📌 **Sai lầm BA gặp:**
- Không Maintain Requirements (BABOK 5.3)
- Không Trace Requirements (BABOK 4.2)
- Không xác nhận chính thức

■ **Cách làm đúng:**
- Mọi thay đổi cần có email, task, comment rõ ràng
- Không update tài liệu nếu chưa có xác nhận
- Ghi lại tất cả lời nói miệng vào Sổ Ghi Lời Rì Rầm

▲ **3. “Bug này chắc user không gặp đâu” – Tự an ủi, tự loại khỏi backlog**
Bug không rõ nguyên nhân. Dev/Test bảo “hiếm lắm”. Bạn tin. Bạn lờ. Bạn bỏ qua. Đến lúc user gặp thật → hệ thống xử lý sai → thiệt hại thật

📌 **Sai lầm BA gặp:**
- Không Assess Risks (BABOK 10.3)
- Không Business Rules Analysis (BABOK 10.4)
- Không trace bug ngược về requirement gốc

■ **Cách làm đúng:**
- Không bỏ qua bug nào nếu chưa rõ nguyên nhân
- Trace lại rule → có hở không? case nào chưa xử lý?
- Dùng dữ liệu thật để test lại thay vì giả định “chắc không sao đâu”

**Thật ra:**
- BA không sai vì tin người khác nói
- BA chỉ sai khi dừng lại ở đó

**Nghe là 1 chuyện.**
Xác nhận, xác minh, log lại — mới là phần BA cần làm đến cùng.


---

## DAY 15/100 — BA KHÔNG BIẾT “GỐC” CHỈ CHĂM CHĂM “NGỌN” THÌ SỚM MUỘN CŨNG TOANG

*Trang 32–33*

Có những hôm đi làm sớm như hôm nay, ngồi ung dung làm cốc trà đá, mình tự hỏi:
**Hồi mới làm BA, mình đã từng ngây thơ tới mức nào?**

Hồi đó, sếp bảo mình: “Em thêm cái nút ‘Đăng ký tư vấn’ lên trang chủ nhé, càng to càng tốt.”
Mình không hỏi gì. Chỉ note lại, vẽ mockup, viết SRS, đẩy Dev làm ngay.
Làm xong, sếp feedback: “Ủa sao có khách đăng ký rồi mà không ai gọi? Sao form này không gửi về CRM?”.

Mình toang. Vì mình chỉ làm cái ngọn – cái nút. Mà mình không hỏi cái gốc:
- Dữ liệu form gửi về đâu?
- Có cần phân loại không?
- Ai xử lý, trong bao lâu?
- Có đo lường được hiệu quả không?

Cả team Marketing chạy chiến dịch kéo về cái form đó... Mà hệ thống chẳng ai xử lý.
Cơ hội thì có – nhưng trôi đi trong im lặng. Sếp thì tức, mình thì đuối, còn khách hàng thì... biến mất. Giờ nghĩ lại, thấy mình sai từ gốc. Sai vì tin rằng làm đúng yêu cầu là đủ.

Nhưng BA đâu phải là người gõ Word theo lời người khác. Câu chuyện này mình hay kể cho học viên BA mới vào nghề. Mình bảo: "Stakeholder không sai khi yêu cầu thứ linh tinh, sai là ở BA không đào tới gốc để biết thứ nào đáng làm."
Nếu bạn từng:
- Làm xong chức năng rồi bị nói “chưa đúng ý”
- Giao diện xong xuôi mà không ai thèm dùng
- Làm theo yêu cầu rồi vẫn bị đổ lỗi

Thì có lẽ, bạn cũng đang bị ngọn cuốn mất gốc.

■ **BABOK nhấn mạnh rõ trong Strategy Analysis:**
- “Việc xác định đúng nhu cầu là nền tảng.
- Nếu xác định sai, mọi thứ còn lại chỉ là phỏng đoán.”

📌 Tháng tới, mình có một buổi mini course
“Kỹ thuật đo lường & tư duy hệ thống cho BA thực chiến”
⏰ 1 buổi – học cách hỏi đúng, đào sâu, và thiết kế đúng từ gốc.


---

## DAY 16/100 — BẠN CHỈ VIẾT FLOW CHO NGƯỜI DÙNG? VẬY AI VIẾT CHO THẰNG... PHÁ?

*Trang 34–35*

“Flow này rõ ràng mà, test gì nữa?”
Tôi một BA trẩu tre đã từng chém thế. Và sáng hôm sau, cái hệ thống “rõ ràng” đó... **gãy.**

Tôi từng mô tả flow tự động **“Tặng voucher sau 7 ngày”**. Yêu cầu trong tài liệu vỏn vẹn một dòng:
“Sau 7 ngày kể từ giao dịch thành công, hệ thống sẽ tặng 1 voucher 50K.”

Nghe thì suôn, nhưng tester test là hệ thống **rụng từng khúc:**
- Giao dịch lúc 23h59 Thứ Hai, hệ thống lại gửi voucher 00h00 Thứ Ba tuần sau → lệch 1 phút → Tester báo: trễ deadline
- Giao dịch lúc 10h tại Nhật (GMT+9), người dùng ở Việt Nam (GMT+7) → hệ thống không tặng gì vì so sai timezone
- Và đỉnh cao là: có 1 user phá – mỗi ngày giao dịch 1 đơn đúng 9h sáng → đến ngày thứ 7, hệ thống tặng 7 voucher cùng lúc. Vì BA không chặn duplicate, không lọc theo user – chỉ check “giao dịch + 7 ngày”

- Sếp thét: “Sao user được tặng cả đống quà?”
- DEV nói: “Đúng theo định nghĩa mà.”
- Tester thở dài: “Tôi test đúng logic, hệ thống toang là phải.”

**Còn BA? Đơ toàn tập vì flow không viết một dòng nào xử lý hành vi phá.**

✖ **Sai lầm phổ biến mà rất nhiều BA dính:**
- Viết mốc thời gian mà không định nghĩa rõ: 7 ngày tính từ khi nào? Server giờ nào?
- Không xử lý trường hợp người dùng phá: spam giao dịch, chỉnh múi giờ, loop để trigger tặng
- Không có logic chặn hành vi lợi dụng hệ thống

🧠 **3 kỹ thuật BABOK giúp bạn không còn ngây thơ:**

1. **Exception Flow – Luồng gãy mới là luồng cần viết nhất**
- Đừng chỉ mô tả “đủ 7 ngày thì tặng”
- Hãy viết: nếu sai lệch thì sao, nếu duplicate thì sao, nếu lệch giờ thì sao?

2. **Business Rule – Rõ luật, hệ thống mới không bị “chơi”**
- Luật tặng chỉ áp dụng mỗi user 1 lần
- Chỉ xét giao dịch đầu tiên
- Chỉ chạy trong khoảng 9h đến 21h server time
Vân vân và vân vân

3. **State Modelling – Giao dịch đang “chờ xử lý” thì đã được tặng chưa?**
- Không định nghĩa rõ trạng thái →
- Hệ thống lặp tặng hoặc quên tặng là chuyện thường

"Viết flow cho người dùng thì dễ. Viết flow sống sót trước kẻ phá mới là BA thật sự."

🖊️ Combo không thể không làm:
Đăng ký ngay record mini course "TƯ DUY TESTER DÀNH CHO BA"
🎯 Học cách viết tư duy của tester, không bị tester hỏi xoáy


---

## DAY 17/100 — TÔI TỪNG LÀM Ở MỘT CÔNG TY NỌ NƠI ROADMAP DÀI NHƯ KỲ VỌNG, NHƯNG NGẮN NHƯ SỰ HIỂU KHÁCH HÀNG

*Trang 36–38*

Lúc mới vào, tôi nghĩ: “Đây là nơi nghiêm túc làm sản phẩm.”. Team đông, vai trò rõ ràng, backlog cập nhật từng giờ, stakeholder góp ý đều đều. Nhưng càng làm, tôi càng nhận ra...Thứ chúng tôi đang tạo ra không phải là sản phẩm, mà là một chiếc máy chạy tính năng.Và rồi, tôi đọc INSPIRED của Marty Cagan – và thấy... Từng phần trong sách, chính là từng vết nứt trong công ty nọ – vết nứt đã luôn ở đó, chỉ là tôi chưa dám gọi tên.

🧩 **1. Lessons from Top Tech Companies - Những điều họ làm khác ta**
“Most product failures come not from bad engineering, but from building the wrong thing.”
📍 Ở công ty nọ: Tôi từng tham gia dự án tặng voucher cho khách hàng thân thiết. Tính năng rất hoành tráng, nhiều rule – phân loại theo mức chi tiêu, tần suất ghé, ưu đãi sinh nhật...Ba tháng sau launch:
- 1% khách dùng
- Gần 80% rule không chạy lần nào
Marketing quay sang hỏi: “Ủa có gì mới không em, để tụi anh chạy chiến dịch khác?”
✖ Không phải vì hệ thống sai. Mà vì **không ai từng xác minh xem khách hàng có cần, có hiểu, có mong chờ không.**

🧩 **2. The Right People - Không có team sản phẩm, chỉ có team giao hàng**
“We need teams of missionaries, not teams of mercenaries.”
📍 Ở công ty nọ:
- PM nói: “Mình phải làm xong trong quý này vì đã hứa với sếp.”
- Dev nói: “Miễn có API là anh code.”
- BA như tôi ngồi giữa – nhận mọi yêu cầu, hợp thức hóa thành backlog.
Không ai thực sự muốn giải quyết vấn đề. Chỉ muốn hoàn thành task.
■ Chúng tôi không được giao quyền.
Chúng tôi được giao kỳ vọng và deadline.

🧩 **3. The Right Product - Một roadmap có thật, nhưng không có hướng đi**
“Product roadmaps are not commitments. They are guesses.”
📍 Ở công ty nọ: Roadmap là danh sách tính năng từ các phòng ban. Mỗi mục có owner – có deadline – có mô tả business value ước lượng (tạm thời).
- Không có đo lường sau release
- Không có review lại sau 1 tháng
- Không có một chỉ số nào cho thấy “nó có đáng được build không”

Mỗi quý, chúng tôi chỉ được hỏi: “Xong chưa?”
Không ai hỏi: “Giá trị gì?”

🧩 **4. The Right Process - Không ai test trước, chỉ biết test sau khi fail**
“Discovery is about learning fast, not building fast.”
📍 Ở công ty nọ:
- Không prototype
- Không A/B test
- Không khảo sát người dùng thật
Mọi thứ đều được đóng gói trong format: “Em confirm với sếp rồi, làm đi.”. Và thế là một tính năng 300 giờ dev effort ra đời... mà không ai có ý định dùng.

🧩 **5. The Right Culture - Sản phẩm không sai, văn hóa mới là thứ khiến mọi thứ lệch**
“The culture of the company will determine the quality of the product.”
📍 Ở công ty nọ:
Mọi thứ đều được justify bằng: “Chúng ta đang tăng trưởng.” Tăng trưởng ở đây là:
- Số lượng dòng Word SRS
- Số lượng feature deploy
- Số lượng phòng ban được chiều lòng
Nhưng:
- Không ai đo retention
- Không ai hỏi lại khách hàng
- Không ai biết lý do vì sao hệ thống càng lúc càng... không ai muốn dùng

💬 Và rồi tôi nhận ra...
INSPIRED không dạy bạn làm sản phẩm giỏi.
Nó dạy bạn: làm sao để không phí sức đội ngũ cho những thứ vô nghĩa.

🧠 Từ đó tôi nghĩ tôi cần thay đổi:
- Không thêm tính năng vào roadmap nếu chưa test 1 vòng
- Không nhận yêu cầu “gấp” nếu chưa xác định rõ problem
- Không chạy KPI theo số feature – mà theo giá trị mang lại

📣 Bạn từng ở “công ty nọ” – nơi ai cũng bận, ai cũng chăm, mà user vẫn lặng im?
Kể tôi nghe – để cùng tìm hướng làm khác.


---

## DAY 18/100 — BUỔI RETRO CUỐI SPRINT KHÔNG PHẢI LÀ ĐỂ BẺ LÁI TỘI LỖI, MÀ ĐỂ BẺ LÁI CÁCH LÀM

*Trang 39–40*

**Cuối tuần rồi chắc thể nào cũng có team vừa retro xong**
Một buổi Retro sprint. UAT gãy. Bug nổ. Tính năng không chạy như kỳ vọng. Và rồi ánh mắt bắt đầu hướng về phía BA...
- “BA không confirm lại với user à?”
- “Cái flow đó có ghi rõ đâu?”
- “Lại thiếu logic trong tài liệu BA...”
Nghe thì nhẹ, nhưng nếu bạn làm BA đủ lâu, bạn biết nó sâu như dao cạo.
- Không ai mắng.
- Không ai chửi.
Nhưng chính bạn cũng biết lỗi này từng có thể tránh được nếu mình setup cách làm rõ ràng hơn ngay từ đầu. Là BA, bạn không cần phải luôn đúng. Nhưng bạn phải là người đầu tiên gọi tên cái sai, rồi khóa nó lại để nó không quay lại sprint sau.

🔧 **Dưới đây là 3 việc một BA từ mid-level trở lên nên làm để team mình không “ăn lại bug cũ” nữa**
Nếu bạn đang là junior, hãy đọc để chuẩn bị mindset. Còn nếu đã có tiếng nói trong team bạn hoàn toàn có thể đề xuất điều này từ ngày mai.

1. **Truy gốc - Không truy người (Root Cause Analysis)**
Khi PM hỏi: “BA không confirm lại với user à?”
Bạn nên nói (thẳng mà không gắt): “Lỗi này em không recap rõ sau buổi họp. Sprint sau, em đề xuất rule: mọi yêu cầu mới đều phải có recap chính thức trong vòng 24h nếu không, coi như chưa đủ cơ sở để triển khai.”
- Rule này không phải để đẩy trách nhiệm
- Mà là để tất cả cùng thống nhất ngưỡng rõ ràng, tránh “nghe vậy tưởng vậy” rồi toang

2. **Ghi lại để không lặp lại (Lessons Learned)**
Khi ai đó bảo: “Khách bảo chưa từng nói vậy – BA ghi sai à?”
Bạn nên nói (cứng rắn mà không đổ thừa):
“Lần này không có log xác nhận là do em chủ quan. Em sẽ tạo file Lessons Learned cho dự án – mỗi thay đổi hoặc khác biệt từ user đều phải có log hoặc recap, tránh tình trạng sau này không ai truy được.”
- Việc này không phải để đổ lỗi lại cho khách
- Mà là để bảo vệ cho cả BA và team, không phải nhớ mơ hồ – mà làm việc có dấu vết

3. **Xác minh trước - để không ai hiểu sai (Verify Requirements)**
Khi bug xảy ra, và bạn nghe câu: “Cứ mỗi lần có bug là thấy thiếu mô tả trong tài liệu BA.”
Bạn nên nói (chốt nhẹ, không bật): “Tài liệu lần này có thể chưa đủ rõ. Sprint sau, em đề xuất mỗi tính năng lớn đều có 15 phút walkthrough giữa BA–DEV–QC. Em sẽ hỏi kỹ xem mọi người hiểu giống tài liệu chưa – nếu có lệch thì sửa ngay trước khi vào dev.”
- Walkthrough không phải để “cứu vớt lỗi BA” – mà là nghi thức kiểm tra hệ thống giao tiếp của cả team

📌 BA là người viết, nhưng cũng là người phải lắng nghe
📌 BA không phải thầy bói, nhưng cũng không nên để ai tự đoán ý mình
Một tài liệu rõ không phải do viết nhiều dòng
Mà là do được xác minh đúng cách – đúng người – đúng thời điểm


---

## DAY 19/100 — MỘT NGÀY HỌP 6 TIẾNG CÒN ĐÂU THỜI GIAN ĐỂ PHÂN TÍCH?

*Trang 41–42*

■ **Thứ Hai – ngày đầu tuần, mở máy đã thấy 6 cái meeting chờ sẵn**
- Sáng 8h30: họp kick-off
- 10h: họp với team DEV để giải thích requirement
- 11h15: join họp với khách confirm lại rule
- Chiều 13h30: họp chỉnh sửa giao diện
- 15h: họp với test
- 17h: họp cập nhật tiến độ
**Kết thúc một ngày → file tài liệu vẫn trắng tinh**

**Tối về, sếp hỏi:**
- “Tài liệu đâu?”
- “Em đi họp suốt còn gì anh?”
- “Thế em họp xong mà không viết ra thì họp để làm gì?”
● Cay. Nhưng đúng.

✖ **Làm sai:**
Họp càng nhiều, càng bận rộn → càng có cảm giác đang làm việc
Nhưng thật ra chỉ đang di chuyển – không tiến về đâu cả

■ **Làm đúng:**
Một BA giỏi không phải là người đi họp “nhiệt tình nhất phòng”,
mà là người biết mình họp để làm gì – và có deliverable sau mỗi cuộc họp

● **BABOK gợi ý:**
- **Prepare for Elicitation:** Họp gì cũng cần mục tiêu rõ ràng, chứ không phải vào để “xem người ta nói gì”
- **Business Analysis Planning:** BA có quyền đề xuất không họp, nếu một email là đủ
- **Stakeholder Collaboration:** Lên tiếng khi thấy lịch họp dày đặc mà không hiệu quả

■ **Checklist sống sót giữa tuần họp chết chóc:**
Trước khi click “Join Meeting”, hãy tự hỏi:
- Mình vào họp với vai trò gì? → Listener? Ghi biên bản? Là người dẫn dắt thảo luận?
- Sau họp mình cần có cái gì? → Tài liệu, xác nhận, hay chỉ... stress?
- Có cách nào thay thế không? → Email recap? Gửi bảng câu hỏi? Offline 1:1? Slack?
📣 Bạn thì sao? Tuần này có bao nhiêu cái họp mà bạn biết mình đang làm gì?

💬 **Tặng bạn bài thơ vui sáng thứ Hai**
Thứ Hai vừa mở máy ra,
Lịch họp đập tới, xỉu ba bốn lần.
Google Meet réo vang dần,
Teams thì nhảy note: “Vào sân họp liền!”
DEV kêu: “Luồng gãy triền miên!”
TEST thì réo rắt: “Flow đâu rồi?”
Sếp vào hỏi gắt: “Xong chưa?”
Dạ... em đang họp từ trưa tới chiều...
Phân tích chưa kịp làm ra,
Cả ngày đi họp... chẳng qua được dòng.
Họp nhiều mà rỗng như không,
Khác gì ăn phở... mà không có bò ●


---

## DAY 20/100 — KHÔNG XEM KỸ HỆ THỐNG HIỆN TẠI ĐÃ CÓ GÌ LÀ VIẾT YÊU CẦU NHƯ CHƯA TỪNG CÓ HỆ THỐNG

*Trang 43–44*

■ **Chuyện có thật ở một công ty bán trà sữa...**
Công ty XYZ có hệ thống TeaBoss đã chạy 3 năm. Nó giúp quản lý đơn hàng, tính điểm thưởng cho nhân viên, và tổng hợp doanh thu từng ca. Một ngày đẹp trời, sếp giao task:
“Viết lại TeaBoss bản mới, UI xịn hơn, API mở rộng, có thể scale toàn quốc.”

Phú – một bạn BA trẻ, nhanh nhẹn, flow vẽ đẹp như sách giáo khoa – được chọn.
Nhưng Phú viết requirement như chưa từng có cái hệ thống nào tồn tại:
- Tính năng tạo đơn hàng: không còn logic tự động chia điểm thưởng cho nhân viên
- Báo cáo doanh thu: gọn gàng, nhiều biểu đồ, nhưng... mất luôn phần tổng hợp theo ca – thứ mà kế toán dùng hằng ngày
Vì sao? Vì Phú không login hệ thống cũ, không phỏng vấn user, không hỏi cái gì đang chạy ổn.

Và rồi ngày review tới...
- “Ủa cái này hồi giờ vẫn có mà?”
- “Tại sao bỏ phần quan trọng vậy?”
- “Mới mà lại thiếu, vậy nâng cấp chỗ nào?”
Team DEV lắc đầu. User thì cạch mặt. Còn Phú... đứng hình mất 5 giây.

■ **Lẽ ra, Phú phải làm thế này. Và đây là kỹ thuật BABOK giúp bạn không viết trong mơ**

1. **As-Is Process Modeling - Nhìn tận mắt hệ thống cũ đang vận hành thế nào**
Phú phải login vào TeaBoss cũ, đi theo một ca vận hành thật:
- Nhân viên thao tác gì?
- Tự động cộng điểm hoạt động ở bước nào?
- Báo cáo doanh thu cần những field nào để tổng hợp đúng theo ca?
📌 Không làm được bước này, mọi yêu cầu bạn viết chỉ là tưởng tượng.

2. **Gap Analysis - Soi sự khác biệt để không viết thừa, không bỏ thiếu**
Phú cần đối chiếu:
- Tính năng nào đang hoạt động tốt → giữ lại
- Tính năng nào gây đau cho user → cải tiến
- Logic nào là workaround → thay bằng rule chuẩn
📌 Viết lại 100% không sai – nhưng phải có cơ sở, chứ không phải vì... chưa đọc hệ thống cũ.

3. **Stakeholder Collaboration - Đào sâu thứ mà tài liệu cũ không bao giờ ghi lại**
Phú cần nói chuyện với user thật:
- Kế toán bảo: “Chị chỉ cần tổng theo ca thôi, dashboard màu mè không cần.”
- Nhân viên cửa hàng nói: “POS delay tụi em hay in lại bằng tay – app mới có nút đó không?”
📌 Không hỏi – không biết
📌 Không biết – là viết sai
📌 Viết sai – cả team sửa giùm bạn

🧠 Còn những kỹ thuật khác như Interface Analysis, Data Mapping, Migration Strategy, mình xin giữ lại, vì đó là bài học mình sẽ mổ thật sâu trong buổi chia sẻ mini: “BA thực chiến: Viết yêu cầu không toang”. Sẽ mở nếu có hơn 20 bạn comment “em muốn học” bên dưới nha.


---

## DAY 21/100 — BA KIÊM PM TƯỞNG ĐƯỢC NÂNG TẦM, AI NGỜ NÂNG LUÔN CỤC NỢ

*Trang 45–46*

**“Dự án này không có PM đâu – em follow luôn cả team nhé.”**
Không phải câu nói lịch sử, nhưng rất nhiều BA từng nghe phiên bản na ná như vậy.
Lúc đầu còn vui: “Thử sức tí, biết đâu lại lên tay.” Ba tuần sau: Mắt thâm – Jira đỏ – Dev giận – Test khóc – tài liệu lỗi. Và đau nhất là... bạn tự mất khả năng nhìn rõ toàn cảnh.

● **Khi BA ôm luôn vai PM – dễ dính 4 cú "gãy":**
→ Gãy nghiệp vụ: vì không còn thời gian ngồi phân tích cho sâu
→ Gãy chất lượng: vì vừa viết – vừa duyệt – vừa đẩy task
→ Gãy kết nối: vì bận chase deadline, quên mất phải align với business
→ Gãy chính mình: vì đầu luôn căng – việc lúc nào cũng dồn

🧠 **3 kỹ thuật BABOK cứu bạn khỏi "gãy gánh giữa đường":**
1. **Stakeholder Analysis**
→ Làm rõ mình đang đóng vai gì trong từng thời điểm
→ Sáng phân tích – chiều họp team. Không nhồi tất cả vào một cuộc call

2. **Scope Modelling**
→ Giữ cả team không trượt khỏi phạm vi ban đầu
→ Dám nói: “Cái này nằm ngoài scope – cần CR nhé”

3. **Risk Analysis**
→ Tự check định kỳ: deadline ổn không? bug có quá tải? mình còn tỉnh không?
→ Nếu thấy vượt ngưỡng – phải lên tiếng trước khi quá muộn

■ **5 điều cần làm nếu buộc phải gánh cả đôi vai:**
- Biết mình đang ở vai nào – và phải chuyển vai khi nào
- Giữ 30 phút mỗi ngày chỉ để kiểm tra logic hệ thống
- Giao lại task nào có thể giao
- Mỗi tuần, đọc lại spec như một người không quen biết
- Cảnh báo khi thấy rủi ro chứ đừng cố "chịu thêm chút nữa"

■ **Nhưng nếu làm đúng – BA kiêm PM có thể là bước chuyển mình**
**Vậy khi nào nên kiêm?**
- Khi dự án nhỏ, thời gian ngắn, team gọn
- Khi bạn có tiếng nói nội bộ, đủ kỹ năng quản task và đàm phán
- Khi bạn sẵn sàng hi sinh độ sâu phân tích để đổi lấy tốc độ delivery
- Và quan trọng nhất: phải biết mình đang trade-off cái gì

● **Nói cho vuông:**
Ôm thêm việc không làm bạn giỏi hơn
Chỉ khi ôm đúng lúc, bạn mới lớn lên thật sự


---

## DAY 22/100 — TÍNH NĂNG “CHỈ THÊM 1 DÒNG THÔI MÀ” RỒI TỐN 3 TEAM XỬ LÝ

*Trang 47–48*

■ **3 lời hứa quen thuộc trước khi dự án mệt mỏi:**
→ “Anh thấy field này nhỏ thôi, thêm vào cho chuyên nghiệp.”
→ “Mình chưa cần logic phức tạp, lưu tạm cũng được.”
→ “Có xíu thôi mà – không ảnh hưởng gì đâu em.”
Bạn BA trẻ gật đầu. Form có thêm ô nhập mã giới thiệu.

✖ **4 hậu quả ai cũng thấy sau 1 tuần chạy thật:**
→ Dữ liệu nhập lung tung, không xác thực → CRM không dám dùng report
→ Không ai định nghĩa “giới thiệu” là gì → Marketing không biết xử lý hoa hồng
→ Khách nhập sai, gọi hotline đòi sửa → CSKH phải sửa tay từng trường hợp
→ Dữ liệu không dùng được, nhưng hệ thống vẫn phải bảo trì → tốn effort vô hình

? **5 câu BA nên hỏi trước khi gật đầu thêm field:**
- Mã này từ đâu? Ai tạo? Có hạn dùng không?
- Nếu nhập sai thì sao? Có báo lỗi không?
- Nếu để trống thì sao? Có bắt buộc không?
- Dữ liệu này được dùng ở đâu? Có liên quan report, thưởng không?
- Có cần mapping giữa người giới thiệu và người được giới thiệu không?

■ **Làm BA, đừng chỉ “vẽ thêm” – hãy thiết kế như người chịu trách nhiệm hệ thống**

✔ **Requirement viết lại đúng chuẩn:**
- Người dùng có thể nhập mã giới thiệu (nếu có).
- Hệ thống sẽ kiểm tra theo danh sách hợp lệ.
- Nếu đúng: ghi nhận. Nếu sai: hiển thị lỗi.

✔ **Data Flow rõ ràng:**
- Nhập mã → Validate → Mapping → Ghi nhận → Hiển thị trên CRM
- Không có mã → Bỏ qua, không ảnh hưởng

✔ **Xử lý ngoại lệ chi tiết:**
- Mã không tồn tại → báo lỗi
- Mã không đúng quyền giới thiệu → từ chối
- Nhập sai → cho phép cập nhật trong 24h (nếu config)

🧠 **3 kỹ thuật BABOK BA phải dùng khi xử lý dạng này:**
- Business Rules Analysis – Làm rõ rule: tạo mã, phân quyền, hạn dùng
- Requirements Validation – Review cả UI + hành vi khi dữ liệu được nhập
- Data Modeling – Xác định mã giới thiệu là gì trong hệ thống: entity riêng hay quan hệ?

● **Một dòng input không rõ logic là điểm bắt đầu cho 10 bug, 4 cuộc họp, và một đống dữ liệu không ai dám động vào.**


---

## DAY 23/100 — DOMAIN DRIVEN DESIGN (DDD) LÀ GÌ? VÀ TẠI SAO BA NÊN BIẾT SỚM?

*Trang 49–51*

✦ **Chuyện thật:**
Một hệ thống đặt lịch sửa xe. BA vẽ flow đơn giản: khách đặt → garage xác nhận → sửa xong. 3 tuần sau:
- Sale cần thống kê tỷ lệ bùng
- Admin muốn tách lịch xác nhận với lịch chờ
- Sếp hỏi conversion từ booking → sửa thật
- Cả hệ thống toang.
Vì object Booking gánh luôn 7 logic. Không có ranh giới. Không có trạng thái. Không đại diện cho nghiệp vụ thật.

🧠 **Domain-Driven Design (DDD) là gì?**
Là cách thiết kế hệ thống xoay quanh logic nghiệp vụ thật sự, không xoay quanh UI, wireframe hay “bên kia làm vậy rồi”.

📌 **Nếu tư duy DDD, bạn đã:**
❶ Tách object đúng với thực tế:
- BookingRequest: khách mới đặt
- Appointment: đã xác nhận
- WorkOrder: xe vào xưởng
- NoShow: khách bùng

❷ Nhận diện đúng Aggregate:
→ Appointment là trung tâm điều phối: khách, xe, lịch, trạng thái
→ Muốn thay đổi? Phải qua Appointment để đảm bảo logic nghiệp vụ không bị phá

🔍 **Trong ví dụ Booking, DDD thể hiện ở đâu?**
- Entity: Appointment, BookingRequest, WorkOrder – có ID, trạng thái, sống độc lập
- Value Object: TimeSlot, GarageAddress, CustomerNote – dữ liệu đi kèm, không cần track riêng
- Aggregate: Appointment – mọi thao tác logic phải đi qua đây
- Domain Service: “Kiểm tra trùng lịch” – không thuộc riêng object nào → tách riêng
- Sub-domain: Customer Interaction, Garage Operation, Service Execution
- Bounded Context: BookingRequest khác context với WorkOrder → chia nhóm, chia trách nhiệm rõ ràng

📌 **Ghi nhớ: DDD chia theo logic nghiệp vụ – không nhất thiết mỗi Entity là 1 bảng DB.**

■ **Vậy BA biết DDD thì được gì?**
1. **Hiểu Entity – tránh viết tài liệu theo UI**
→ Thay vì “đặt lịch” là 1 step trong flow, bạn nhận ra Appointment là một thực thể nghiệp vụ có trạng thái riêng
→ Viết requirement gắn với trạng thái sống thật: Pending, Approved, NoShow, Completed
→ Kết quả: Dev dễ model – Test dễ viết case – Logic sống được

2. **Biết chia Aggregate – không nhồi 7 nghiệp vụ vào 1 object**
→ Bạn không gọi tất cả là Booking, mà tách: BookingRequest, Appointment, WorkOrder
→ Và hiểu: chỉ được cập nhật thông tin quan trọng qua đúng Aggregate để giữ logic nghiệp vụ nhất quán
→ Kết quả: Hệ thống ít bug logic – Dev không phải “code chống lại tài liệu”

3. **Dùng Value Object đúng – không biến mọi thứ thành bảng riêng**
→ Thay vì tạo table cho “Địa chỉ garage”, “Khung giờ”, “Yêu cầu đặc biệt của khách”...
→ Bạn hiểu đây là dữ liệu đi kèm, không cần danh tính riêng → gộp vào Entity chính dưới dạng Value Object
→ Kết quả: Thiết kế DB đơn giản – Dễ test – Dễ maintain

4. **Hiểu Domain Service – tách logic phức tạp khỏi use case tào lao**
→ Logic “Kiểm tra trùng lịch”, “Tự động chuyển trạng thái” không nằm trong UI flow hay một form nào cả
→ Bạn tách nó thành Domain Service độc lập, giúp dev xử lý nghiệp vụ đúng nơi – đúng lúc
→ Kết quả: BA không viết yêu cầu “dựa vào may mắn dev hiểu đúng” → mà có logic nghiệp vụ rõ ràng

5. **Biết vẽ Bounded Context – không viết tài liệu loang toàn hệ thống**
→ Bạn xác định đâu là phạm vi của Garage, đâu là Customer, đâu là Service Execution
→ Không gom 1 Use Case ảnh hưởng 4 module – mà chia rõ, mô tả đúng từng context
→ Kết quả: Tài liệu không bị loang – Dev dễ chia module – Dự án dễ scale

🔥 **Nói gọn lại:**
DDD không làm bạn "code giỏi" nhưng giúp bạn "chia đúng, viết đúng, scale đúng."
🔔 **Lưu ý:**
Không phải hệ thống nào cũng nên áp DDD.
→ Với CRUD nhỏ, ít nghiệp vụ – DDD có thể overkill.
Nhưng với hệ thống nhiều logic, nhiều nhóm dev, dễ scale...
→ DDD là thứ BA cần hiểu nếu không muốn dự án mình viết tài liệu – gãy sau 2 release.


---

## DAY 24/100 — KHI NỘI BỘ CHIA BÈ BA CHỈ CÒN 2 LỰA CHỌN: DẪN DẮT HOẶC LÀM BIA ĐỠ ĐẠN

*Trang 52–54*

Nghĩ làm BA trung lập là an toàn? Sai rồi. Trong môi trường bè phái đấu đá, **BA không dẫn dắt được thì chỉ còn nước làm bia đỡ đạn.**

🎭 Một ngày chết đứng của BA trẻ:
Thanh – một BA mới toe nhận dự án xây hệ thống Tuyển dụng cho công ty. Buổi họp gather requirement đầu tiên, Thanh bị kéo căng giữa hai làn đạn:
- HR Recruiter sốt ruột: “Form ứng tuyển càng nhanh càng tốt, chỉ cần tên, số điện thoại, email. Lead đang thiếu nghiêm trọng.”
- Tech Lead lạnh lùng: “Không. Phải khai đủ kỹ năng frameworks, project từng làm. Không thì phỏng vấn phí thời gian chết.”
Thanh không biết dẫn dắt. Chỉ lặng lẽ gõ biên bản họp.
- Không phân nhóm user
- Không phân nhánh flow
- Không xác định mục tiêu ưu tiên
- Không truy ngược OKR dự án
👉 “Cứ ghi hết đã, miễn ai cũng vui.” – Thanh nghĩ.

■ Kết quả: Một bản wireframe tả tơi, Thanh dựng bản wireframe đầu tiên. Nhưng nó chỉ là bản tổng hợp mâu thuẫn giữa hai phe:
- Một màn nhập cực kỳ ngắn theo ý HR
- Một màn chi tiết kỹ thuật theo ý Tech Lead
- Không tách luồng – không phân nhóm – không ưu tiên
Buổi review wireframe, mọi thứ sụp đổ:
- HR Recruiter cau có: “Form dài lê thê thế này? Ai nộp lead nổi?”
- Tech Lead đập bàn: “Form này không đủ khai kỹ năng chi tiết.”
- Manager lạnh giọng: “Thanh, em dẫn luồng form điền cho anh coi thử.”
● Thanh đứng chết lặng. Không nói nổi. Không phải vì thiếu file. Mà vì ngay từ đầu, Thanh đã từ chối dẫn dắt nghiệp vụ.

🔥 **Cốt lõi nỗi đau**
Cái chết của BA không bắt đầu ở wireframe. Cái chết bắt đầu ngay khi BA từ chối dẫn dắt buổi họp đầu tiên.
- Không phân stakeholder
- Không bóc tách luồng
- Không truy ngược mục tiêu
- Không ép các bên chốt priority
Wireframe chỉ là nơi cái sai bùng phát thành hình.Tài liệu chỉ là nơi cái sai bị phơi bày.
**“Một BA chết không phải vì thiếu file.**
**Một BA chết vì để mất quyền điều phối ngay từ buổi họp đầu tiên.”**

● **3 kỹ thuật BABOK cứu BA thoát chết giữa chiến trường**

1. **Stakeholder Analysis – Phân tích đúng người quyết requirement**
✖ **Sai:**
- Ghi hết yêu cầu ai cũng như ai
- Không rõ ai là Owner
■ **Đúng:**
- Sau họp, dựng RACI Matrix:
  - HR Recruiter: Responsible + Consulted
  - Tech Lead: Accountable
  - Manager: Informed
- Ghi rõ Owner từng phần wireframe
📌 Nếu Tech Lead là Accountable → Form kỹ năng phải theo Tech Lead.

2. **Prioritization – Ưu tiên theo đúng mục tiêu dự án**
✖ **Sai:**
- Ghi hết, không lọc, không nhóm
■ **Đúng:**
- Hỏi ngay: “Mục tiêu là gì? Tăng số lượng lead hay tuyển đúng kỹ năng?”
📌 Nếu ưu tiên chất lượng → Phải giữ form chi tiết, không cắt bừa.

3. **Facilitation – Dẫn dắt flow nghiệp vụ**
✖ **Sai:**
- Để các bên cãi tay đôi, BA ngồi ghi
■ **Đúng:**
- Gom nhóm yêu cầu
- Tách luồng nếu cần
📌 **Ví dụ:**
- Flow 1: Form đơn giản (lead phổ thông) – theo HR
- Flow 2: Form chi tiết (ứng viên kỹ thuật) – theo Tech Lead

📣 Bạn từng thấy BA nào chết đứng ngay buổi họp đầu tiên chưa?
Hay chính bạn đã từng lúng túng khi bị hỏi ngược về luồng nghiệp vụ?
■ Comment chia sẻ chiến trường thật bạn đã gặp.
Để đừng ai “chết” vì chỉ biết ghi – mà không dám dẫn.


---

## DAY 25/100 — HIDDEN REQUIREMENT – KHI “QUY TẮC NGẦM” LÀM HỆ THỐNG LỆCH HƯỚNG

*Trang 55–56*

✦ **Những thứ nguy hiểm nhất thường không nằm trên giấy**
Không phải yêu cầu nào cũng được chia sẻ ngay từ đầu. Có những quy tắc vận hành bất thành văn – tồn tại cả chục năm – nhưng không ai đưa vào tài liệu. Chỉ khi hệ thống đi vào vận hành, những lệch lạc mới lộ ra từng chút một.
👉 **Hidden requirement không nằm đâu xa, nó ẩn ngay trong hành vi thường ngày.**

■ **Một bài học thực tế – Khi nghỉ phép hóa thành phép thử**
Dự án HRM, Use Case tưởng chừng đơn giản:
"Quy trình duyệt nghỉ phép nhân sự."
Nhưng thực tế thì...
Nhiều phòng ban có thói quen "giữ chỗ" ngày nghỉ:
- Ngày 1/5: Nhân viên A nộp đơn nghỉ cho ngày 5/5
- Sáng 5/5: A quyết định... đi làm vì dự án gấp

✖ **Tuy nhiên:**
- Hệ thống đã tự động trừ phép, báo cáo sai công, tính sai lương.
- Vì hidden requirement chưa được xử lý đúng: Việc xác nhận lại trước ngày nghỉ không được capture trong flow.
✦ **Tất cả bắt nguồn từ một thứ: Quy tắc ngầm.**

💡 **3 kỹ thuật BABOK giúp bóc hidden requirement ra ánh sáng**
1. **Observation – Quan sát thực tế**
✖ Sai lầm thường gặp:
- Chỉ tin vào lời kể hoặc tài liệu
■ Cách làm đúng:
- Ngồi trực tiếp quan sát tại phòng HR
- So sánh quy trình trên giấy với hành vi thật
📌 Ví dụ: BA nếu ngồi 1 buổi sáng ở phòng nhân sự sẽ thấy:
Có người xin nghỉ nhưng... vẫn đi làm.

2. **Stakeholder Analysis – Phỏng vấn đa chiều**
✖ Sai lầm thường gặp:
- Chỉ hỏi HR hoặc Manager
■ Cách làm đúng:
- Phỏng vấn nhiều bên: Nhân viên – HR – Admin – Payroll
- So sánh câu trả lời để tìm chỗ lệch
📌 Chính lệch nhỏ trong thói quen từng nhóm sẽ bóc ra hidden rule.

3. **Business Rules Analysis – Formal hóa quy tắc miệng**
✖ Sai lầm thường gặp:
- Bỏ qua thói quen “miệng” vì nghĩ không cần thiết
■ Cách làm đúng:
- Bất kỳ hành vi ngoài hệ thống → formal thành rule
📌 Ví dụ:
“Đơn nghỉ chỉ có hiệu lực khi được xác nhận lại vào sáng ngày nghỉ. Nếu không → tự động hủy.”

🔍 **Tóm lại:**
Hidden requirement không giấu đâu xa, nó chỉ giấu trong... thói quen mà ta tưởng là “chuyện thường”.
“Một BA giỏi không chỉ nghe – mà còn nhìn, cảm, và formal hóa được cái chưa ai viết ra.”

💬 Bạn từng gặp hidden requirement nào chưa?
Comment chia sẻ một lần bạn “toang” vì quy tắc ngầm nhé.
Biết đâu lại cứu được một dự án khác khỏi lệch đường ●


---

## DAY 26/100 — ĐẦU THÁNG, BẠN LÀ BA MỚI TOANH. VÀ CHÀO MỪNG BẠN ĐẾN VỚI CHIẾN TRƯỜNG.

*Trang 57–59*

Vừa vào công ty. Mở mail chưa đầy 10 phút, sếp đã nhắn:
"Dự án này cần gấp BA, em join luôn nha."
- Không intro.
- Không lịch bàn giao.
- Không bản đồ hệ thống.
Chỉ có 1 chữ: GẤP.
Và bạn – được kỳ vọng là: Hiểu nhanh – bắt nhịp nhanh – confirm nhanh – viết nhanh.
Nhưng hệ thống thì chẳng "nhanh" lại với bạn.

🔥 **Case 1: Dự án mới – Không có gì để tham khảo**
Lần đầu gặp khách, họ nói: "Chị muốn 1 ứng dụng quản lý học sinh thông minh. Không dùng Excel nữa."
Bạn hỏi: "Cần chức năng gì?"
Họ trả lời: "Chị cũng chưa chắc."
Bạn ghi lại hết – rồi gửi DEV.
DEV hỏi: "Đây là flow hay là wishlist?"
Bạn ngơ ngác. Vì bạn chưa phân biệt được:
- Cái gì là phải có
- Cái gì là có cũng được
Bạn tưởng mình đã ghi kỹ. Nhưng càng ghi – càng loạn. DEV thì không thể code từ 1 bản danh sách ước mơ.
▲ Làm sao sống sót?
■ Dùng BABOK:
- 6.3 Business Needs – Làm rõ động cơ kinh doanh
- 10.17 Process Modelling – Vẽ flow TO-BE dù còn thiếu
- 6.5 Scope Modelling – Xác định MVP rõ ràng

🔥 **Case 2: Dự án đang chạy – nhìn như lành, hóa ra toàn sẹo**
Bạn tưởng chỉ cần viết thêm vài task. Nhưng không ai kể rằng:
- Module A từng thiếu case khách hủy đơn sau thanh toán → hóa đơn vẫn xuất → kế toán phải xoá tay
- Module B fix bug phân quyền bằng cách... ẩn nút
- Module C do 1 DEV kỳ cựu viết → ai cũng né
Bạn viết yêu cầu mới – tưởng là cải tiến. Nhưng sửa chỗ này → chỗ khác lệch. Thêm logic mới → lộ ra lỗi cũ. Bạn nhận ra: Không có hệ thống nào đang chạy mà "sạch sẽ" cả. Chỉ là... người ta không kể với bạn.
▲ Làm sao sống sót?
■ Dùng BABOK:
- 5.2 Trace Requirements – Rà lại yêu cầu cũ
- 7.2 Validate Requirements – Xác minh logic “đang chạy”
- 4.5 Communicate Requirements – Giao tiếp lại, không copy tài liệu cũ như cái máy

🔥 **Case 3: Data Migration – tưởng copy dữ liệu, ai ngờ sai cả báo cáo**
Bạn chuyển dữ liệu khách hàng từ hệ thống cũ sang hệ thống mới. Bạn thấy field giống nhau: “ngày tạo”, “trạng thái”, “loại tương tác” → bạn nối.
Kết quả:
- Lịch sử chăm sóc biến mất
- Khách đang theo dõi → bị đánh dấu là đã nghỉ
- Báo cáo tụt hẳn số khách tiềm năng
Vì sao? Vì “ngày tạo” ở hệ thống cũ = ngày bắt đầu tư vấn. Còn ở hệ thống mới = ngày tạo tài khoản. Chênh vài ngày – sai hoàn toàn báo cáo.
▲ Làm sao sống sót?
■ Dùng BABOK:
- 10.1 Data Modelling – Vẽ source → target
- 10.3 Business Rules – Làm rõ rule convert
- 6.1 Acceptance Criteria – Gắn tiêu chí pass/fail rõ ràng

🔥 **Case 4: API Integration – đọc Swagger thôi là chưa đủ**
Bạn viết tài liệu cho API gửi đơn hàng cho đối tác. Swagger đầy đủ: tên, sđt, địa chỉ → bạn map đúng. Ngày go-live: Khách trả tiền → không ai giao hàng. Vì gì? SĐT có khoảng trắng → hệ thống đối tác... im lặng bỏ qua. Bạn không hỏi:
- Có chấp nhận khoảng trắng không?
- SĐT có cần chuẩn hóa không?
- Có bước nào validate không?
Vì bạn nghĩ Swagger = nghiệp vụ. Nhưng không.
▲ Làm sao sống sót?
■ Dùng BABOK:
- 10.13 Interface Analysis – Làm rõ cách giao tiếp
- 10.16 Non-Functional Requirements – Xác định các ràng buộc
- 10.12 Use Case Modelling – API phải đúng vị trí trong flow nghiệp vụ
● Tổng kết: Làm BA không chỉ là viết tài liệu. Mà là:
Gỡ từng mảng mù mờ – cả cũ lẫn mới. Dự án nào cũng có lỗi. Chỉ là... người ta không cảnh báo trước. Bạn chỉ mới bắt đầu. Không cần giỏi ngay. Chỉ cần biết dừng lại để hỏi kỹ hơn – đã là khác biệt rồi.


---

## DAY 27/100 — BẠN CÓ ĐANG LÀM ĐÚNG VIỆC NHƯNG VẪN THẤY CHÔNG CHÊNH?

*Trang 60–61*

Vẫn đi họp đều. Vẫn viết tài liệu đầy đủ. DEV hiểu. QA test pass.Feedback không tệ. Mọi thứ... ổn. Nhưng giữa một ngày làm việc, bạn chợt nghĩ: “Mình đang giúp team gỡ điều gì? Hay chỉ đang làm cho xong task?” Không có gì sai. Chỉ là... hơi lưng chừng.

🎓 Bạn chủ động học thêm:
- Một khóa viết tài liệu
- Một mini course elicitation
- Một buổi UML
Nhưng có thể thứ bạn thiếu...Không nằm ở kỹ thuật. Mà nằm ở tư duy gỡ việc
📍 Thứ đó gọi là:
👉 Kỹ năng giải quyết vấn đề – bài bản, có tư duy, không cảm tính.

■ **Gợi ý sách nên đọc: Bulletproof Problem Solving**
Không phải sách dạy BA viết tài liệu. Mà là sách giúp bạn nghĩ được – gỡ được – kể lại được.
🧠 **7 bước giải quyết vấn đề – dành cho BA đã từng làm đúng mà vẫn thấy sai**

◆ **1. Xác định đúng bài toán – thay vì chạy theo yêu cầu**
✖ Sai: Hỏi “Chị cần gì?” rồi ghi chức năng
■ Đúng: Hỏi “Vấn đề anh/chị đang gặp là gì? Làm xong thì thay đổi điều gì?”

◆ **2. Chẻ nhỏ bài toán – thay vì vẽ flow liền tay**
✖ Sai: Vẽ flow theo lời kể → rối, chồng chéo
■ Đúng: Vẽ logic tree → bóc từng nhánh → chọn điểm đào đúng

◆ **3. Ưu tiên điểm nghẽn – thay vì mô tả đều tay**
✖ Sai: Mô tả chi tiết field đơn giản, nhưng phần duyệt lương thì sơ sài
■ Đúng: Tập trung effort vào chỗ có rủi ro cao, logic rẽ nhánh nhiều

◆ **4. Làm việc theo giả thuyết – thay vì hỏi người khác muốn gì**
✖ Sai: Hỏi “Anh/chị muốn gì tiếp theo?”
■ Đúng: Đặt giả thuyết trước: “Tôi nghĩ loyalty nên dựa theo chi tiêu đúng không?”

◆ **5. Phân tích đúng mức – không cảm tính, không trình diễn số**
✖ Sai: “Em thấy mức 20tr là hợp lý để duyệt”
■ Đúng: “Theo số liệu, >20tr là ngưỡng vượt trung bình → nên yêu cầu duyệt thêm”

◆ **6. Tổng hợp sắc gọn – không tường thuật lại tất cả**
✖ Sai: Gửi file dài 30 trang
■ Đúng: Tóm 1 slide: “3 vấn đề – 1 hướng gỡ – 1 hành động đề xuất”

◆ **7. Truyền đạt đúng người – đúng lúc – đúng cách**
✖ Sai: Gửi insight cho sai người hoặc sai thời điểm
■ Đúng: Chọn đúng stakeholder, đúng lúc cần ra quyết định, đúng cách kể chuyện

🔥 Và điều tuyệt nhất?
Bạn không còn viết tài liệu trong vô thức nữa. Bạn dẫn team đi qua được mớ hỗn độn – thay vì đứng yên nhìn deadline lao tới.
👇 Muốn nhận cuốn sách này? Điền form mình để dưới comment nhé. Mình gửi liền.
Đọc 15 phút – thấm dài lâu.
💬 Làm BA không phải để ghi lại những gì người ta nói. Mà là để dẫn ra điều mà chính họ chưa thấy được. Cuối tuần đọc nhẹ, Thứ Hai bật mode gỡ việc.


---

## DAY 28/100 — ELICITATION TECHNIQUES DÙNG SAI KỸ THUẬT LÀ TỰ ĐẨY MÌNH VÀO THẾ BÍ

*Trang 62–63*

Kỹ thuật không sai. Nhưng nếu chọn sai kỹ thuật, sai người, sai thời điểm – bạn không chỉ mất dữ liệu, mà còn mất niềm tin của cả team.
▲ **Một pha fail kinh điển – tưởng đúng mà sai**
Dự án xây hệ thống quản lý sửa xe. BA mới vào, muốn làm bài bản → tổ chức workshop thu thập nghiệp vụ: xử lý xe lỗi, đặt lịch sửa, xác nhận phụ tùng.
Workshop có:
- 5 kỹ thuật viên (đang thiếu người, đi làm ca)
- 1 quản lý (vừa họp với sếp xong, còn bực)
- 1 bạn kho (mới chuyển phòng, chưa nắm quy trình)
👉 Kết quả:
- Kỹ thuật viên im lặng hoặc né tránh
- Quản lý thì lấn át: “Cứ làm giống bên XYZ đi.”
- Bạn kho... gật gù vì không biết gì
BA vẫn ghi chép đầy đủ – nhưng:
- DEV đọc không hiểu
- Flow sai
- Stakeholder chê: “Không phải cái tôi cần.”

✖ **Vấn đề không nằm ở workshop – mà ở chỗ... chọn nhầm kỹ thuật**
Theo BABOK v3 – Task 4.2: Plan Elicitation, khi chọn kỹ thuật cần cân nhắc:
1. Mục tiêu là gì? → Khám phá mới? Kiểm tra giả định? Hay xác nhận lại?
2. Ai sẽ tham gia? → Người quyết định? Người thực thi? Hay chỉ là người cung cấp thông tin?
3. Ngữ cảnh có phù hợp? → Có đủ thời gian? Có đồng thuận? Có dữ liệu nền chưa?
BA trong case trên không trả lời được 3 câu đó.
→ Workshop chỉ là phản xạ quen tay. Và nó phản lại luôn.

■ **Cũng là tình huống đó – nhưng nếu làm đúng:**
- Observation: Shadow kỹ thuật viên trong 1 ca sửa → hiểu thao tác thật, biết điểm nghẽn
- Structured Interview: Hẹn riêng quản lý lúc tỉnh táo → nắm logic vận hành & KPI
- Prototyping + Review: Vẽ prototype → gửi từng người góp ý → refine logic đúng thực tế
3 bước – 3 kỹ thuật – 3 người phù hợp.
→ Kết quả: logic rõ hơn, DEV hiểu hơn, stakeholder gật gù hơn.

● **BA không thiếu kỹ thuật. Nhưng chọn sai kỹ thuật cho sai người – thì càng làm càng rối.**
✦ Nếu bạn từng:
- Tổ chức buổi workshop mà... không ai nói gì
- Gặp stakeholder kiểu “gật cho xong”
- Lúng túng không biết dùng kỹ thuật nào lúc nào

Thì sáng Chủ Nhật, 11/05/2025, mình sẽ tổ chức một buổi học đặc biệt:
📌 Elicitation & Collaboration Techniques – Phiên bản thực chiến
● 8h – 12h | Online
■ Nội dung:
- Chọn kỹ thuật đúng theo từng kiểu stakeholder
- Dựng nhịp thu thập theo tiến trình dự án
- Case study workshop toang, phỏng vấn fail, survey mất hút – và cách gỡ
📌 Không slide màu mè. Không định nghĩa.
Chỉ có kinh nghiệm thật – lỗi thật – cách làm đúng thật.
◆ Phí tham gia nhẹ nhàng – đủ cà phê sáng và vài cú "vỡ não" bạn sẽ không tìm thấy trong sách.


---

## DAY 29/100 — NGỤY BIỆN CỦA KẺ LƯỜI: “EM LÀM THEO YÊU CẦU MÀ”

*Trang 64–66*

“Em làm theo yêu cầu mà!”
Câu nói tưởng vô hại... nhưng thực ra đang âm thầm giết chết cả hệ thống – và cả uy tín nghề BA của bạn.

■ **App đặt cơm trưa – và cú điểm danh nhẹ cho tư duy BA "nghe lời quá mức"**
Công ty có hơn 100 nhân viên. Trước đây, mọi người nhắn Zalo cho chị admin để đặt cơm: gà, cá, thịt – mỗi món giới hạn 30 phần. Nếu món nào hết, chị sẽ gọi lại để đổi món. Hơi thủ công, nhưng chạy được.
Một ngày đẹp trời, sếp bảo:
“Làm app đặt cơm đi em. Chọn món, đặt trước 10h30 là được. Món nào hết thì admin gọi lại như mọi khi.”
Bạn BA trẻ gật đầu làm ngay:
- Giao diện chọn 3 món ■
- Nút gửi đơn ■
- Chặn sau 10h30 ■

Deploy xong, tưởng êm. UAT cũng test cho đủ quy trình. Không ai nghĩ đến chuyện: 42 người cùng chọn cơm gà.
✦ Và rồi... NGÀY ĐẦU DÙNG APP:
- 42 người chọn cơm gà
- 25 người chọn cá
- 33 người chọn thịt

● Mỗi món chỉ có 30 phần → Có 15 đơn vượt quota.
Chị admin phải gọi lại từng người như ngày xưa. Có người không nghe máy. Có người giao nhầm. Cả văn phòng bắt đầu cà khịa:
“Làm app chi mà vẫn phải gọi?”
“Nhắn Zalo còn nhanh hơn...”
Sếp hỏi:
“Sao không chặn đặt khi hết suất?”
Bạn BA trả lời: “Dạ... em làm đúng theo yêu cầu mà. Sếp bảo vẫn giữ quy trình gọi lại còn gì ạ...”

✖ **Và đó là khoảnh khắc bạn tự phá sập vai trò BA của mình**
Bạn đang làm hệ thống – hay số hoá lỗi sai cũ?
Khách mô tả quy trình
→ BA phải là người phân tích lỗ hổng, đặt câu hỏi, đề xuất giải pháp.
Làm y chang lời khách = chuyển phát nhanh yêu cầu
→ Không phải chuyên môn, mà là lười phản biện.

✖ **Sai 1: Không Verify Requirements**
Bạn nghe: “Admin vẫn gọi lại như mọi khi”
→ Bạn hiểu y chang. Không kiểm tra giới hạn suất. Không cảnh báo.
📌 Lẽ ra phải hỏi:
- Mỗi món có bao nhiêu suất?
- Khi hết thì hiển thị gì?
- Người dùng có được chọn nữa không?
- Làm vậy để giúp admin hay chỉ để đẹp?

■ Ví dụ đúng:
Người thứ 31 chọn món gà → hệ thống báo: “Món này đã hết suất. Vui lòng chọn món khác.”

✖ **Sai 2: Không Trace Requirements**
Bạn làm đúng giao diện → nhưng sai mục tiêu.
📌 Bạn quên hỏi:
- App này giúp ai tiết kiệm thao tác?
- Làm xong mà admin vẫn gọi → có cải tiến gì không?

■ Ví dụ đúng:
Trace từ yêu cầu “chặn sau 10h30”
→ ra mục tiêu: “giảm sai sót & tiết kiệm thao tác admin”
→ Thiết kế chặn suất, hiện báo cáo từng món, không cần gọi thủ công.

✖ **Sai 3: Không Define Assumptions**
Bạn nghĩ: “Thôi để sau, làm chạy đã.”
Không ghi gì. Đến lúc toang, ai cũng hỏi:
“Tại sao hệ thống không báo trước?”

■ Làm đúng thì phải:
– Ghi rõ trong release note:
“Chưa kiểm soát giới hạn suất – admin xử lý thủ công. Sẽ nâng cấp ở bản sau.”
→ Người thứ 40 vẫn đặt món cá → admin gọi lại
→ Không ai đổ lỗi, vì đã được cảnh báo.

💬 **“Nghe lời không sai. Nhưng không hỏi lại – thì sai đậm.”**

🔍 **Tổng kết**
“Em làm theo yêu cầu mà”
= Ngụy biện của người không dám phản biện
= Chiêu thoát thân khi không verify – không trace – không phân tích
Khách mô tả yêu cầu = góc nhìn chủ quan
BA hiện thực hóa giải pháp = trách nhiệm nghề nghiệp
→ Nếu chỉ copy lời khách
→ Bạn đang phản bội chính vai trò của mình

💬 **Nghề BA của bạn đang vướng gì?**
Mỗi ngày mình viết 1 bài – nhưng để viết trúng nỗi đau, mình cần nghe cái bạn đang mắc:
- Khách nói 1 đằng – DEV hiểu 1 nẻo?
- Bị nhét vai PM – toang deadline nhưng vẫn phải cười?
- Vào dự án mới mà không biết bắt đầu từ đâu?
- Cứ viết tài liệu xong là bị hỏi lại: “Cái này ở đâu?”

📥 Hãy comment hoặc inbox – mình sẽ viết tiếp, cho đúng những người đang cần.


---

## DAY 30/100 — CÁCH TÔI XỬ LÝ CR ĐỔI LOGIC GIỮA ĐƯỜNG MÀ VẪN KỊP DEADLINE

*Trang 67–68*

● 9h tối. Cả team DEV – QA – BA vẫn đang OT, căng mắt fix nốt bug cuối để kịp Golive sáng mai.
Tôi cũng đang cùng OT với anh em. Và đúng lúc đó, điện thoại tôi sáng lên:
“Em ơi, anh Phú CEO có góp ý vụ chấm công hơi cứng.
Mấy bạn có đi muộn nhưng vẫn làm đủ 8 tiếng mà vẫn bị trừ công. Mình nên sửa lại trước khi Golive sáng mai nha. Không để vậy được đâu!” Người gửi: chị HR.
⏳ Còn 12 tiếng nữa là Golive hệ thống chấm công.
Tôi đứng lặng 3 giây. Không phải vì bất ngờ. Mà vì quá quen với tình huống CR phút chót – vẫn luôn đến khi cả team đang cạn pin. Tôi hít vào một hơi. Không được cuống. Không được nhún.

💬 Nếu bạn làm BA mà gặp CR phút 90 – đừng phạm 3 lỗi này:
✖ Nghe là làm: Vội vàng bảo DEV sửa rule, chưa trace hệ quả
✖ Không hỏi kỹ: “Linh hoạt là tới bao nhiêu? Bù mấy phút?”
✖ Không recap rõ: Đến lúc số liệu sai thì stakeholder bảo: “Chị đâu có nói vậy...”

**1. Bình tĩnh trace lại logic – xác định rõ rủi ro**
Tôi hỏi thẳng chị HR: “Nếu bạn vào 10h, về 19h vẫn tính đủ công đúng không chị?”
Chị cười chữa cháy: “Không không, chỉ trễ chút xíu – tối đa 9h30 thôi. Miễn là có bù giờ.”
■ Tôi xác định lại business rule mới:
- 9:00–9:30 được coi là “linh hoạt”
- Tổng thời gian làm ≥ 8 tiếng → tính đủ công
- Hiển thị trạng thái mới: "Đi muộn có bù"

■ Tôi lập impact table, và thấy rõ nếu đổi rule bừa:
- Báo cáo chấm công mất chuẩn phân loại
- Tính lương sai nếu nhân viên lách luật
- KPI mất chỉ số đúng giờ → không đánh giá được ý thức
- Niềm tin vào hệ thống sụt giảm, văn hóa công ty nhão ra

**2. Dùng "Scope Shield" – đàm phán bằng trade-off rõ ràng**
Tôi đưa 2 lựa chọn cho chị HR:
👉 Phương án 1 – Giữ deadline
- Thêm rule mới “Đi muộn có bù”
- Không sửa báo cáo, không gỡ logic cũ
- Hiển thị trạng thái mới rõ ràng
- ■ Golive đúng hạn

👉 Phương án 2 – Sửa toàn hệ thống
- Tính công theo tổng giờ
- Viết lại báo cáo, KPI, dashboard
- ● Delay ít nhất 1 tuần

■ Kết quả: Chị HR chọn phương án 1.
Không cần BA cãi – chỉ cần BA đưa ra lựa chọn và hậu quả rõ ràng.

**3. Recap văn bản – khóa cửa “quay xe”**
Tôi gửi recap ngay trong nhóm chat + email:
- 9:00–9:30, về ≥ 18:30, làm đủ 8h → tính đủ công
- Trạng thái mới: “Đi muộn có bù”
- Không ảnh hưởng tới logic báo cáo, KPI
- Áp dụng từ ngày 6/5
- Đã đồng thuận: HR, DEV, QA, PM

■ Có chữ. Có log. Có nhân chứng. Không ai chối được.
■ Checklist “sống sót” khi CR phút 90
- Trace được toàn bộ hệ thống dính líu
- Ép stakeholder định nghĩa rõ “linh hoạt”
- Đưa ra lựa chọn + hậu quả cụ thể
- Recap có dấu thời gian – bảo vệ team

💬 “Chấp nhận đổi flow không khó – khó là không để nó kéo cả hệ thống lệch theo.”


---

## DAY 31/100 — “EM ĐANG CÃI ANH À?” – VÀ BÀI HỌC TÔI KHÔNG BAO GIỜ QUÊN VỀ TƯ DUY PHẢN BIỆN

*Trang 69–70*

Phòng họp hôm đó, tôi không nói thêm một từ nào. Sếp nhìn tôi, ánh mắt đanh lại: “Em đang cãi anh à?”
Không. Tôi không cãi. Tôi chỉ đang hỏi những câu mà... không ai dám hỏi.

🧩 **Câu chuyện bắt đầu như này**
Sếp bảo: “Khách mua đủ 100k thì tặng voucher. Làm đơn giản, đừng lằng nhằng nữa.”
Tôi gật đầu. Rồi hỏi:
- Nếu khách trả hàng thì điểm sao xử lý?
- Voucher gửi rồi có thu hồi được không?

Cả phòng quay sang nhìn tôi như thể tôi vừa phá mood họp. Sếp cắt luôn: “Đừng phức tạp hóa. Bên A làm vậy có ai kêu ca gì đâu.” Tôi ngồi im. Không phải vì tôi sợ. Mà vì... tôi đã từng thắng tranh luận – rồi... thua trên production.

✖ **Tôi từng mắc sai lầm lớn – tưởng mình viết đúng**
Hai tháng trước, tôi cũng từng nghĩ mình viết logic rất chặt. Checklist đủ. Flow chi tiết. Rule rõ ràng. Nhưng rồi: hệ thống live → toang.
Vì tôi viết đúng dựa trên một giả định sai mà chưa bao giờ kiểm tra. Tôi không sai logic. Tôi sai vì quá tin vào điều mình "nghĩ là đúng".

📘 **Cuốn sách khiến tôi ngồi thẫn thờ cả buổi:**
“Critical Thinking, Logic & Problem Solving” Tôi không đọc để học thêm kỹ năng. Tôi đọc để... gỡ lại cách mình tư duy – từ gốc.

**3 câu quote đập thẳng vào mặt tôi – và vào nghề BA:**
■ “Every argument makes an assumption.”
Mọi lập luận đều chứa một giả định.
✦ Tôi từng xây cả hệ thống dựa trên giả định chưa từng được chất vấn.

■ “Arrogance shuts down learning.”
Ngạo mạn là thứ giết chết tư duy phản biện.
✦ Tôi từng tin mình giỏi đến mức bỏ qua những điều căn bản.

■ “Logic without framing is structured confidence.”
Logic mà không có khung tư duy – chỉ là sự tự tin có cấu trúc.
✦ Và tôi từng rất tự tin – cho đến khi khách hàng vạch ra điều tôi chưa từng nghĩ tới.

**Checklist 3 câu hỏi phản biện nên hỏi cho mọi yêu cầu:**
- Chúng ta đang mặc định điều gì là đúng?
- Có góc nhìn nào bị bỏ quên không?
- Mình đang phân tích – hay chỉ đang tự an ủi logic của mình?

Tư duy phản biện không phải để thắng lý – mà để không chết chung với một yêu cầu "nghe có vẻ đúng".

📌 Nếu bạn là BA, PM, hay người viết giải pháp mỗi ngày. Đừng vội gật đầu khi yêu cầu có vẻ hợp lý. Vì cái “có vẻ” đó – có thể là lý do khiến cả hệ thống toang.

📘 Mình để link sách ở comment.
Còn nếu bạn cũng từng sai như tôi từng sai – hãy chia sẻ bài viết này, để ít nhất có thêm 1 người tránh được lỗi đó.


---

## DAY 32/100 — DẤU HIỆU NHẬN BIẾT DỰ ÁN SẮP TOANG TỪ GÓC NHÌN BA

*Trang 71–74*

✦ Dự án không nổ vì bug. Nó rò rỉ từng chút vì những tín hiệu nhỏ bị BA bỏ qua. Một sáng đẹp trời, bạn mở máy chưa kịp uống cà phê thì...
- DEV vẫn chưa update task dù đã hứa "xong hôm nay" từ... hôm kia
- QA hỏi về một flow bạn chưa từng viết
- Stakeholder nhắn riêng: “Ơ, chị tưởng em hiểu rồi nên không nói lại...”
- PM seen tin nhắn nhưng đặc biệt im lặng

Và bạn người đang giữ requirement, flow, kỳ vọng – tim run nhẹ một nhịp: "Chết rồi. Có mùi... toang."
💬 **Một BA giỏi không phải người viết tài liệu đẹp.**
BA giỏi là người đánh hơi được mùi toang – trước cả khi bug xuất hiện. Dưới đây là 5 dấu hiệu sắp toang mà tôi từng gặp. Kèm cách chữa cháy kiểu thực chiến – để bạn không gục giữa đường sprint.

🚨 **DẤU HIỆU #1 – DEV hiểu mỗi người một kiểu**
“Anh bảo click vào thì hiện popup mà? Đâu nói validate.”
“Flow này có case back à? Em tưởng đi một chiều.”
“Phải lưu lịch sử? Em hiểu là update thôi.”
🔥 **Lý do:**
- Spec bạn chưa đủ chặt
- Chưa walkthrough
- Đang sống bằng assumption

🧨 **Thực tế:**
Bạn viết “nhấn Gửi → hiện popup xác nhận”
→ DEV 1 hiểu là xác nhận xong mới lưu
→ DEV 2 hiểu là lưu xong mới hiện
→ DEV 3 không hiện gì, chỉ toast
💊 **Cách chữa:**
- Gọi mini-sync: cho DEV nói lại họ hiểu gì
- Soi lại spec, update tài liệu
- Gửi bản final, chốt hiểu đúng

■ BABOK: Verify Requirements

🚨 **DẤU HIỆU #2 – QA hỏi điều đáng ra phải rõ từ đầu**
“Nếu bỏ trống trường A thì sao?”
“Back từ bước 3 về bước 1 có giữ data không?”
“Sai định dạng thì báo lỗi kiểu gì?”
🔥 Lý do:
Exception Flow chưa viết
🧨 Thực tế:
QA hỏi: “Chọn rồi bỏ chọn hết checkbox thì sao?”
→ Bạn chưa viết → DEV làm thiếu → QA đoán → bug trồi UAT
💊 Cách chữa:
- Update Use Case với Alternate + Exception Flow
- Highlight chỗ mới update
- Gửi lại + sync cách xử lý

■ BABOK: Scenarios & Exception Handling

🚨 **DẤU HIỆU #3 – Stakeholder bắt đầu “khai thật”**
“Thật ra chị cũng chưa chắc nhu cầu này.”
“Sếp mới đổi ý, mai em update giúp nhé?”
“Thêm phần này cho đẹp hơn, nhỏ thôi.”
🔥 Lý do:
Scope lệch – timeline sắp gãy
🧨 Thực tế:
Sắp xong màn hình tạo đơn, stakeholder bảo:
“Chị muốn thêm đính kèm nhiều file như Drive.”
→ Nhẹ nhàng thôi mà: kéo theo update UI, gọi API, xử lý storage, test lại flow
💊 Cách chữa:
- Log thành Change Request
- Phân tích impact: UI, backend, testing
- Trình bày rõ: “Cái này ảnh hưởng đến kế hoạch cũ như thế nào?”
- Không ừ đại. Đề xuất post-release nếu cần

■ BABOK: Change Control + Needs Assessment

🚨 **DẤU HIỆU #4 – Chat nhóm im lặng bất thường**
- Jira trống
- Git không có commit
- Standup không ai hỏi
- Ai cũng “giả vờ bận”

🔥 Đây là giai đoạn "bình yên trước bug bão"
- DEV đang stuck mà không dám nói
- QA chờ flow chính
- PM nghi ngờ nhưng chưa nói
- Bạn thì... thấy “sai sai”

🧨 Thực tế:
Task “Xử lý tạo tài khoản KH doanh nghiệp” → 3 ngày không push
💊 Cách chữa:
- Hỏi trực tiếp: “Em đang vướng gì?”
- Mở mini-review
- Kèm 1 DEV + 1 QA rà task critical

→ Đừng đợi bug mới họp. Họp để bug không có cơ hội nảy mầm
■ BABOK: Monitor Solution Performance

🚨 **DẤU HIỆU #5 – Có hơn 2 “fix tạm” trong 1 sprint**
- “Hardcode tạm chiết khấu”
- “Dùng token demo login”
- “Tạm bỏ validate – demo trước đã”

🔥 Nghe thì ổn
- Fix tạm 1 cái → 1 bug ẩn
- Fix tạm 3 cái → staging toang
- Fix tạm 5 cái → PROD ngáp ngáp

🧨 Thực tế:
DEV hardcode token → tới UAT fail → "quên xóa"
💊 Cách chữa:
- Log danh sách fix tạm + gán người chịu trách nhiệm
- Gửi log cho PM + DEV + QA
- Đặt deadline clear hết trước staging

→ Mọi thứ “tạm” đều phải ghi ra. Không ghi = không fix
■ BABOK: Risk Register + Technical Debt Management

● **BABOK tổng kết**
✔ Risk Analysis:
Mọi sự im lặng, mọi dòng hardcode, mọi flow chưa test = 1 quả mìn chờ nổ
✔ Verify Requirements:
Không verify đủ → team hiểu lệch → bug là điều chắc chắn

💣 Dự án không nổ vì 1 quả bom – nó rò rỉ từng exception không viết, từng task không update, từng lần ‘cứ hardcode đi đã’ mà bạn không biết.

💬 Bạn từng ngửi thấy mùi bug từ ánh mắt DEV, câu hỏi của QA, hay 1 dòng nhắn của stakeholder – nhưng không ai tin cho đến khi PROD toang?

👉 Kể lại 1 pha “ngửi mùi toang đúng đét nhưng bị phớt lờ” để cộng đồng cùng học cách sống sót trước bug.


---

## DAY 33/100 — FEEDBACK KHÔNG GIẾT BẠN PHẢN ỨNG NGU MỚI GIẾT BẠN

*Trang 75–76*

Feedback không phải là cú đấm nhưng phản ứng ngu sẽ khiến bạn knockout. Hôm đó, trong một buổi họp nội bộ, tôi tự tin trình bày flow tính năng mới. Có wireframe. Có logic. Tưởng ngon. Nhưng vừa dứt slide đầu tiên... feedback tới tấp:
- UX này khó dùng lắm em ơi
- Flow chưa nghĩ tới nhóm người dùng B
- Cái logic duyệt này mâu thuẫn với chính business rule bên dashboard...

Và tôi một BA chưa “trầy da tróc vảy” đủ lâu – đã phản ứng như sau:
✖ Cãi tay đôi với DEV: “Flow này hôm trước duyệt rồi mà!”
✖ Cứng họng khi QC hỏi, vì... đúng là chưa nghĩ tới.
✖ Trả lời sếp: “Em tưởng...” – và mở ra một dây chuyền toang chưa từng có.

● **3 phản ứng sai lầm khi bị feedback chê thẳng mặt:**
1. Phản xạ phòng vệ ngay lập tức: Tưởng là đang “bảo vệ chính kiến” → Thật ra là đang tạo căng thẳng và mất uy tín.
2. Giả vờ không nghe gì: Nghe nhưng không note. Không sửa. Và y như rằng bug lại lặp lại ở bản sau.
3. Đổ sụp vì một lời chê:
“Tôi không hợp làm BA?”
“Sao làm gì cũng bị bắt lỗi?”
→ Và tự mình gục trước khi kịp giỏi.

💬 **BA giỏi không phải là người không bị feedback. Mà là người biết chuyển feedback thành năng lượng để nâng cấp.**

● **3 kỹ thuật BABOK giúp BA xử lý feedback GẮT mà không GỤC**

📌 **1. Assess Stakeholder Feedback**
Sai thường gặp: Nghe góp ý là phản ứng ngay hoặc im luôn.
Làm đúng:
- Ghi nhận đủ. Không ngắt lời.
- Sau họp: tổng hợp, phân loại feedback → phản hồi lại từng ý.

Tư duy cần có: Feedback là dữ liệu không phải đòn công kích. Phản ứng thông minh hơn cảm xúc.

📌 **2. Monitor Business Analysis Performance**
Sai thường gặp: Bị chê đâu → sửa đúng chỗ đó → lần sau lại dính y chang.
Làm đúng:
- Dừng lại soi cả hệ thống checklist/template/process.
- Nếu 1 lỗi lặp lại 3 lần → cần refactor cách bạn làm việc.

Tư duy cần có: Feedback là cơ hội nhìn thấy lỗ hổng của chính mình – để vá lại trước khi đi xa hơn.

📌 **3. Communicate Business Analysis Information**
Sai thường gặp: Gửi mỗi file tài liệu → không hướng dẫn, không deadline phản hồi.
Làm đúng:
- Gửi tài liệu kèm hướng dẫn: Ai cần đọc gì, phản hồi gì, trước khi nào.
- Gợi ý format trả lời để giảm thời gian lòng vòng.

Tư duy cần có: “Gửi file” chưa bao giờ là “giao tiếp”. Giao tiếp = Dẫn dắt người ta hiểu đúng điều bạn mong muốn.
💬 "Feedback không giết bạn. Phản ứng ngu mới giết bạn."
💬 Còn bạn thì sao? Bạn từng bị feedback “chém thẳng mặt” là khi nào? Phản ứng lúc đó là gì: bật lại, né tránh, hay tỉnh ra và sửa cho đến nơi đến chốn?
👉 Comment chia sẻ cú feedback khiến bạn từ “ảo tưởng ổn” → “thật sự giỏi lên” nhé.


---

## DAY 34/100 — TÔI ĐANG NỐI LIỀN... HAY CHIA RẼ DỰ ÁN?

*Trang 77*

(Dành cho những BA Manager – khi thấy dự án vận hành mà vẫn không an lòng)

🌙 Chủ Nhật. Không task. Không họp. Chat cũng im. Tôi ngồi lại, không phải vì mệt. Mà vì có gì đó... không thông. Không phải bug. Không phải task chưa xong. Mà là cảm giác dự án đang vận hành... mà thiếu mạch.
📌 Cả tuần qua... ai cũng làm đúng phần việc của mình.
- Tài liệu có.
- Yêu cầu rõ.
- Kết luận đầy đủ.

Nhưng giữa những mảnh ghép đó, tôi không chắc đã có ai... đứng ở giữa để nối.
- Không phải bug.
- Không phải lỗ hổng rõ ràng.
- Chỉ là những đoạn chuyển tiếp không ai gọi tên.

Một vài flow không có người giữ mạch. Một vài tình huống mà cả hai bên đều nghĩ:
→ “Chắc phía kia sẽ xử lý tiếp.”

💬 Tôi từng nghĩ: Chỉ cần team nào làm đúng phần team đó, thì hệ thống sẽ ổn. Nhưng càng làm lâu, tôi càng nhận ra một sự thật đôi khi, ai cũng đúng mà tổng thể vẫn lệch.

● Và tôi hiểu ra: BA không chỉ là người confirm yêu cầu. Cũng không chỉ là người giao tiếp giữa các nhóm. Mà là người giữ cho dự án liền mạch.

💬 Tối nay tôi không làm gì cả. Không chạy deadline. Chỉ ngồi lại và nhìn lại. Một tuần vừa rồi, mỗi team đều làm đúng phần của mình. Mọi thứ đều “done”. Nhưng trong đầu tôi vẫn còn một cảm giác: Các đoạn flow vẫn đang chạy...Nhưng hình như mỗi bên đang chạy theo một nhịp riêng. Tôi không trách ai vì tôi hiểu: Không ai có trách nhiệm nhìn toàn hệ thống ngoại trừ chính tôi. Và đó là vai của một BA Manager. Không phải vì tôi giỏi hơn. Mà vì tôi là người duy nhất phải giữ được góc nhìn đủ rộng... để thấy mạch đang rời ra.
📘 Tôi viết lại cảm giác này nặng như treo đá, nhưng nếu không viết, tôi sẽ quên mất. Cảm giác của một người thấy dự án vẫn trôi, nhưng không chắc nó đang đi tới đâu.


---

## DAY 35/100 — TƯ DUY HỆ THỐNG NỀN MÓNG SỐNG CÒN CỦA MỘT BA THỰC THỤ

*Trang 78–79*

● **Rất nhiều bạn BA nghĩ:**
“Em viết đầy đủ flow rồi mà, sao hệ thống vẫn lỗi?”
“Em confirm lại với user rồi, họ bảo đúng logic.”
“Em đâu có sai, DEV làm chưa đúng thôi.”
→ Bạn không sai về flow.
→ Bạn không sai về quy trình.
→ Nhưng bạn sai vì không thấy được hệ thống toàn cảnh.

📌 **Bạn làm đúng theo yêu cầu nhưng không nhận ra:**
- Yêu cầu đó đẩy lỗi sang hệ thống khác mà bạn không kiểm soát.
- Flow bạn viết không tính đến lệch nhịp dữ liệu giữa các module.
- “Logic đúng” bạn xác nhận với user chỉ đúng trong phạm vi góc nhìn của họ.

✦ Sai lầm không nằm ở từng task. Sai lầm nằm ở góc nhìn thiếu hệ thống.

● **Điểm mấu chốt**
Tư duy hệ thống không phải là tư duy vẽ hệ thống. Mà là khả năng nhìn thấy tác động qua lại giữa các thành phần, và đánh giá ảnh hưởng trước khi nó bung ra thành lỗi.

✖ **Một BA thiếu tư duy hệ thống sẽ:**
- Không dự đoán được hậu quả của yêu cầu.
- Không thấy được data chảy qua đâu, log ghi thế nào, exception có fallback không.
- Không phân biệt được lỗi hệ thống vs lỗi nghiệp vụ vs lỗi tích hợp.

📘 **3 KỸ THUẬT GIÚP HÌNH THÀNH TƯ DUY HỆ THỐNG**
◆ Ví dụ chung: Công ty muốn làm app nội bộ để nhân viên đặt cơm mỗi ngày. Yêu cầu từ user: “Tạo màn hình chọn món, xác nhận, vậy là xong.”
Một BA non tay sẽ nghĩ ngay đến UI. Một BA có tư duy hệ thống sẽ dùng 3 kỹ thuật sau:

**1. System Thinking – Tư duy toàn cảnh & dòng chảy dữ liệu**
Câu hỏi cần đặt:
- Danh sách món mỗi ngày lấy từ đâu?
- Sau khi đặt xong, dữ liệu đi đâu?
- Ai tiếp nhận? Nhà bếp, admin hay auto export file?
- Có ràng buộc ngân sách theo chi nhánh?
- Có xử lý nếu nhân viên huỷ sau thời gian cutoff?

■ Lợi ích:
→ Map được toàn bộ các thành phần liên kết:
User – Hệ thống – Bộ phận liên quan – Dữ liệu đầu ra.
→ Tránh được lỗi kiểu “viết xong flow – backend không xử lý được – kitchen không nhận đơn”.

**2. Scope Modeling – Phân biệt ranh giới hệ thống**
Câu hỏi cần làm rõ:
- Việc cập nhật menu là do ai? Dùng hệ thống nào?
- App đặt cơm có duyệt ngân sách luôn không, hay chỉ gửi sang hệ thống kế toán?

■ Giải pháp:
→ BA xác định rõ phạm vi xử lý:
- App chỉ cho đặt món, huỷ món, tracking suất ăn theo user.
- Xuất file tổng cho nhà bếp.
- Không xử lý phê duyệt ngân sách → gửi báo cáo sang hệ thống khác.

■ Lợi ích:
→ Không ôm requirement vượt quyền → tránh tự đẩy mình vào thế chết.

**3. Interface Analysis – Phân tích điểm kết nối hệ thống**
Câu hỏi BA cần làm rõ:
- Dữ liệu món ăn được nhập tay, import Excel hay call API?
- Sau khi đặt món, đơn được gửi đi qua đâu? Email? API? Zalo?
- Có API xuất đơn tổng không? Có retry khi lỗi mạng? Có log không?

■ Lợi ích:
→ Giúp thiết kế requirement đúng theo khả năng giao tiếp của hệ thống.
→ Không bị “vẽ flow xịn nhưng không ai nhận đơn”.


---

## DAY 36/100 — BA VÀ DEV – ĐỒNG MINH HAY ĐỐI ĐẦU?

*Trang 80–82*

“Em gửi task rõ ràng mà DEV vẫn làm sai.”
“DEV làm ẩu, không đọc SRS, em mệt mỏi sửa logic hoài.”
“BA toàn vẽ hươu vẽ vượn, DEV tụi tôi code khổ vc.”
✦ Đây không chỉ là câu chuyện của bạn – mà là nỗi đau muôn thuở giữa BA và DEV.

● **Sự thật phũ:**
Cả hai không sai... nhưng đang không cùng chiến tuyến.
- BA nghĩ: “Tôi phân tích nghiệp vụ, tôi đúng.”
- DEV nghĩ: “Tôi code đúng mô tả, tôi cũng đúng.”

→ Và cả hai không hiểu:
Mỗi lần hiểu lệch nhau 1cm – hệ thống lệch 10km khi vận hành. Dự án không chết vì bug to. Dự án chết vì:
- Task hiểu sai mà không ai phát hiện.
- Luồng nghiệp vụ gãy mà không ai chịu trách nhiệm.
- Feedback tới lui hoài mà không sửa tận gốc.

▲ **3 kiểu “đối đầu thụ động” đang giết chết dự án:**
**1. Cãi ngầm bằng im lặng**
“Tôi làm đúng rồi.” – “Tôi cũng làm đúng rồi.”, nhưng hệ thống vẫn lỗi. Vì không ai soát lại, không ai nhìn hệ thống tổng thể.
**2. Không dám hỏi**
- DEV không dám hỏi lại vì sợ bị chê kém.
- BA không dám nói không biết vì sợ lộ dốt.

→ Kết quả: cả hai cùng đoán – và đoán sai.
**3. Ném task như ném hàng**
- BA gửi task xong mất hút con mẹ hàng lươn
- DEV đọc không hiểu cũng không hỏi, cứ thế mà code.

→ Đến lúc lỗi thì cả team chỉ tay vào nhau.

■ **Giải pháp: Đừng chia việc – hãy chia góc nhìn**
Đây không phải là:
👉 “Bạn làm phần của bạn – tôi làm phần của tôi.”
Mà là:
👉 “Chúng ta cùng nhau sống sót qua deadline.”

💬 **3 kỹ thuật giúp BA và DEV cùng nhau thắng**
**1. Walkthrough Task**
✖ Đừng nói suông “task rõ ràng rồi nhé”
Task không bao giờ hoàn thành chỉ bằng text. Mỗi task phức tạp cần 5 phút ngồi lại:
- BA trình bày logic + edge case
- DEV diễn giải lại bằng ngôn ngữ kỹ thuật

→ Nếu chưa hiểu giống nhau → **KHÔNG ĐƯỢC CODE**
📌 Giao task mà không confirm hiểu giống nhau = cài mìn đợi nổ

**2. Rule phải logic và tròn luồng**
Không để DEV & QC tự suy diễn vặn vẹo
✖ BA viết:
“Người dùng không được hủy đơn sau khi thanh toán.”
→ Nghe tưởng đủ. Nhưng rồi DEV sẽ hỏi:
- Admin có được hủy không?
- Nếu chưa chuyển hàng thì sao?

📌 Nếu BA không chốt luôn ngoại lệ trong UC → Team sẽ tự fill logic theo trí tưởng tượng → Và toang là điều tất yếu.
■ Viết rule thì phải:
- Nêu rõ khi nào áp dụng
- Có ngoại lệ không?
- Nếu có, xử lý ở đâu?

**3. BA không xác định đúng điểm thực thi**
→ DEV build đúng mà vẫn... sai
✖ BA viết:
“Khi tạo đơn hàng, hệ thống kiểm tra tồn kho. Nếu hết hàng thì không cho tạo.”
DEV:
- Hiểu đúng
- Code đúng

Nhưng check tồn kho lại đặt ở lúc mở form, không phải khi nhấn ‘Tạo đơn’.
→ Trong lúc user nhập, hàng đã bị người khác mua mất
→ Hệ thống vẫn tạo đơn → Đơn lỗi → User chửi → Team đơ
■ BA cần chốt rõ:
- Rule chạy lúc nào?
- Dữ liệu nào là data chuẩn?
- Có cần re-validate trước khi xác nhận hành động không?

● **Kết luận**
- BA không sai nghiệp vụ
- DEV không sai kỹ thuật
- Nhưng lệch nhau ở ranh giới thực thi

→ Hệ thống gãy mà không ai chịu trách nhiệm.

● **Nếu bạn là BA:**
- Đừng giao task kiểu ném qua tường.
- Ngồi review cùng DEV → confirm từng case.
- Khi DEV hỏi: “Field này để làm gì?”

→ Nếu bạn không trả lời được → quay lại hỏi stakeholder.

💬 **Câu hỏi cho bạn:**
Bạn từng “toang” với DEV vì hiểu sai task chưa? Hãy comment một lần bạn nhớ đời để BA khác đọc mà né kịp ●


---

## DAY 37/100 — SAI LẦM LỚN NHẤT CỦA BA: HỌC KỸ THUẬT... NHƯNG QUÊN HỌC SỰ THẤU HIỂU

*Trang 83–85*

● Bối cảnh:
Kỳ review 6 tháng và một hệ thống được build đúng tới từng field. Công ty triển khai kỳ đánh giá hiệu suất 6 tháng đầu năm, gắn với:
- KPI / OKR
- Xếp loại A-B-C theo kết quả đánh giá
- Xét tăng lương

HR yêu cầu hệ thống:
- Cho phép nhân viên tự đánh giá theo OKR
- Line Manager đánh giá lại
- Hệ thống tính điểm trung bình theo trọng số
- Export kết quả → làm căn cứ tăng lương, xét thưởng

BA bắt tay vào làm: Tạo kỳ đánh giá → Gán từng nhân viên → Nhập điểm → Tổng hợp → Xuất báo cáo
- SRS đầy đủ
- Triển khai đúng deadline

Nhưng sau kỳ review:
◆ Nhân viên thì chán
◆ Quản lý thì nản
◆ HR thì... im lặng

💣 **Sự thật không có trong tài liệu**
Tôi hỏi lại team thì được những câu trả lời thế này:
- “Em không dám tự đánh giá cao, sợ sếp bảo ảo tưởng.”
- “Sếp chấm như máy – cảm giác copy paste.”
- “Không có chỗ nào để ghi nhận xét, chỉ có nhập số.”
- “Có OKR mà cả kỳ chẳng ai nhắc tới – giờ review thì lấy gì mà nhớ?”

📌 Hệ thống đúng kỹ thuật – nhưng sai cảm xúc.

✖ **Sai lầm của BA nằm ở đâu?**
Bạn làm đúng những gì HR yêu cầu. Nhưng sai cái người dùng thật sự cần mà không nói ra. Bạn nghĩ mình đang làm phần mềm review. Thật ra bạn đang thiết kế một trải nghiệm chạm vào lòng tự trọng, danh dự và... tiền lương.
✦ Một hệ thống review là nơi:
- Tiền bạc được quyết định (tăng lương hay không)
- Danh dự được xếp hạng (A–B–C)
- Tâm lý bị khui ra (nỗi ấm ức bị đè nén)

→ Nhưng bạn lại build như một form nhập liệu nội bộ.
- Giao diện lạnh
- Flow đơn chiều
- Không tạo cảm giác được lắng nghe – chỉ thấy bị xét xử

💬 **Nếu BA hiểu thấu hơn, lẽ ra đã...**
■ **1. Thêm phần nhận xét cá nhân hóa**
Trước khi chấm điểm, gợi ý quản lý viết vài dòng như:
“Anh đánh giá cao cách em gánh team trong chiến dịch golive tháng 4.”
→ Nhân viên có cảm giác được nhìn thấy – không bị xử lý như máy móc.

■ **2. Thiết kế tính năng "Ghi chú hiệu suất theo tháng"**
Review không còn là trò chơi trí nhớ.
Nhiều quản lý đến kỳ review mới cuống cuồng hỏi:
“Ủa, bạn này... 6 tháng rồi làm gì nhỉ?”
→ Không nhớ → chấm đại → cả hệ thống trở thành một trò đùa.
📌 Giải pháp:
- Thêm UC “Ghi chú hiệu suất”
- Cho phép tag theo mục tiêu OKR
- Hàng tháng, hệ thống nhắc nhẹ:

“Tháng này team bạn có gì nổi bật không? Ghi lại 1 dòng nhé.”
▲ Tính năng này không cứu kỳ review hiện tại – mà cứu những kỳ sau.

■ 3. Chia báo cáo cho BOD theo nhóm năng lực – không chỉ là bảng điểm
BOD không cần cột điểm từ cao đến thấp. Họ cần biết:
- Ai đang nổi bật → giữ chân
- Ai đang ổn → phát triển
- Ai đang trượt → coaching gấp

📌 Gợi ý phân nhóm, đừng chỉ export một cái bảng vô hồn.
💬 "Người ta không nhớ mình được chấm mấy điểm, nhưng nhớ rất lâu cảm giác sau kỳ đánh giá."

● BA giỏi không chỉ hiểu nghiệp vụ – mà phải hiểu cảm xúc người dùng
- Bạn làm đúng field → Nhưng người ta ngại mở form
- Bạn làm đúng rule → Nhưng rule đó gây áp lực thầm lặng
- Bạn tưởng đang hỗ trợ HR → Nhưng bạn đang chạm vào lòng tự trọng của người lao động

→ Là BA, bạn không chỉ build flow.
→ Bạn định hình cách tổ chức trưởng thành và giữ người.

🎙 Và nếu bài viết này đạt 100 lượt comment + share, tôi sẽ tổ chức 1 buổi webinar hoàn toàn miễn phí, chia sẻ:
- Cách phát hiện cảm xúc người dùng ẩn sau flow nội bộ
- Kỹ thuật Empathy Mapping cho BA
- Những lỗi phổ biến khiến hệ thống “đúng kỹ thuật mà vẫn thất bại”

⏱ Một buổi thật – không màu mè, không hô hào nghề – chỉ nói đúng việc người dùng thật đang cảm thấy gì mà bạn không viết vào SRS.
👉 Comment “Tôi cần học” + share bài nếu bạn muốn tham gia.


---

## DAY 38/100 — SẾP ĐỔI Ý XOÀNH XOẠCH – BA CẦN LÀM GÌ?

*Trang 86–87*

“Làm lại cái này cho anh nhé.”
“Đưa tính năng kia lên gấp, mấy cái khác tính sau.”
“Sao còn chưa xong? Anh nói từ hôm trước rồi mà?”
Nếu bạn từng khựng lại vì một câu nói từ sếp – không phải vì sợ, mà vì biết:
👉 Chỉ một dòng chỉ đạo, có thể kéo theo cả hệ thống chệch hướng.

● **Bối cảnh có thật:**
BA vừa sign-off bản SRS với khách hàng. Chiều hôm đó, sếp nhắn riêng:
“Mai anh đi họp, em sửa luồng kia theo ý anh nhé. Gấp.”
BA trả lời:
“Sếp ơi, flow đó ảnh hưởng tới 2 phần khác, và dev đã làm được 70% rồi ạ.”
Sếp seen, không trả lời. Sáng hôm sau, cả team... **làm lại từ đầu.**

✖ **3 sai lầm phổ biến của BA khi bị ép đổi ý:**
1. Coi lời sếp là mệnh lệnh tuyệt đối → Ngại bị đánh giá là không linh hoạt
2. Không hỏi lại lý do đổi → Nghĩ rằng hỏi lại là thiếu tôn trọng
3. Không ghi lại thay đổi, không phân tích tác động → Khi rủi ro xảy ra, không có gì để bảo vệ mình

💣 **3 Case thực chiến – và cách BA phản ứng an toàn mà vẫn “gắt”:**

**Case 1: Sếp bảo làm gấp, không cần hỏi**
“Anh bảo làm là làm. Gấp.”
📌 Cách xử lý:
Nhắn lại thật lịch sự: “Dạ, để em ghi nhận lại yêu cầu đổi. Em gửi sếp bảng tác động để mình xử lý đúng, hạn chế rủi ro về sau ạ.”
👉 Bạn không phản đối. Bạn đưa ra bức tranh hệ quả để sếp tự cân nhắc.
● Đây là lúc BA phải dẫn dắt sếp bằng logic, không bằng lời.

**Case 2: Sếp muốn làm ngay – khỏi cần phân tích**
“Khỏi phân tích. Làm như anh nói đi.”
📌 Cách xử lý:
Ghi nhận bằng văn bản/email.
Tài liệu ghi rõ: “Tạm thời chỉnh theo yêu cầu trực tiếp – chưa đánh giá đầy đủ.”
● BA giỏi không ngăn được tất cả thay đổi, nhưng luôn để lại dấu vết để bảo vệ team và chính mình.

**Case 3: Sếp không muốn nghe phân tích**
“Lúc nào cũng phân tích! Cứ làm đi.”
📌 Cách xử lý:
Không tranh luận.
Làm prototype/mockup thật nhanh, gửi sếp duyệt.
Đính kèm lời nhắn:
“Nếu đi theo hướng này, timeline có thể lùi 1 tuần, dev cần chỉnh 30% phần đã làm.
App cũng mất tính năng X. Anh cân nhắc giúp em nhé.”
● Không phải sếp nào cũng thích nghe BA nói. Nhưng sếp nào cũng ngại bị sai khi hệ quả đã hiện hình.

💬 Một sự thật đắng nhưng đúng:
Bạn không thể dạy sếp.
Nhưng bạn có thể dẫn dắt sếp bằng dữ kiện, bằng logic, và bằng nghệ thuật sinh tồn của một BA.

📢 Cần template "Change Request" log để tự vệ trước những lần đổi ý bất ngờ?
Comment "TÔI CẦN" để tôi gửi bạn mẫu nhé.


---

## DAY 39/100 — TASK SẼ DẦN BIẾN KHỎI TAY BẠN KHÔNG VÌ BẠN DỞ, MÀ VÌ NGƯỜI TA KHÔNG CÒN DÁM TIN

*Trang 88–90*

📍 **Câu chuyện thật – Khởi đầu của sự mất niềm tin**
Ở công ty cũ, tôi từng lead một team dev nhỏ. Làm cùng với một anh BA. Giai đoạn đầu? Ổn.
- Tài liệu ok.
- Họp khách bài bản.
- Flow vẽ đủ bước.

Tôi còn nghĩ: “Cho ảnh handle luôn mấy feature chính cũng được.” Cho đến khi...

✖ Một flow tưởng đã confirm với khách.
Dev code xong, khách phản hồi: “Ai bảo xử lý kiểu này?”
Cả team nhìn nhau. Anh BA như chưa từng tồn tại.

✖ Buổi họp khác, khách hỏi: “Tính năng này bên em làm được không?”
Ảnh gật đầu. Không hỏi dev. Không check backend.
Về mới lòi ra: còn vướng nhiều vấn đề, team thì thiếu BE.

Không toang hệ thống.
Không drama.
Nhưng... đủ để tôi hiểu: Không thể để ảnh cầm feature chính thêm lần nào nữa. Tôi không inbox. Không blame. Tôi chỉ... âm thầm rút toàn bộ task nghiệp vụ khỏi tay ảnh.
**Tự xử lại hết.**

📖 “Người ta chỉ thật sự tin bạn khi bạn có 4 thứ: Chính trực – Ý định – Năng lực – Kết quả.”
— Stephen M.R. Covey

**1. ● CHÍNH TRỰC – Nói được thì làm được**
Chính trực là sống nhất quán giữa lời nói và hành động – ngay cả khi không có ai nhìn.
— Covey

Tôi từng chứng kiến nhiều BA:
- Báo rằng khách “chốt rồi” → nhưng chưa hề confirm
- Họp xong bảo “cuối ngày gửi recap” → 3 hôm sau mới nhớ
- Trễ deadline nhưng im như chưa từng mở miệng

Không ai trách liền. Nhưng từ đó... không ai tin nữa.
📌 Muốn rèn?
- Trước khi nói, tự hỏi: “Mình chắc chưa?”
- Không chắc? Nói thẳng: “Cái này em cần check lại.”
- Trễ thì báo. Không báo = tự phá uy tín.

**2. ● Ý ĐỊNH – Làm vì đúng, hay làm cho yên?**
Ý định là thứ người khác cảm được – không phải thứ bạn tự nhận.
— Covey
Tôi từng thấy BA:
- Biết giải pháp sai nhưng vẫn gật vì “sếp nói rồi”
- Không phản biện, không dám lắc đầu – sợ mất lòng
- Giao task cho dev mà trong bụng vẫn thấy “có gì đó sai sai”

Người ta không cần bạn ngoan. Người ta cần bạn đứng về thứ đúng – kể cả khi không ai nói ra.
📌 Muốn rèn?
- Nhận task → tự hỏi: “Mình làm vì lý do gì?”
- Nếu không rõ mục tiêu → đi hỏi.
- Nếu thấy sai → phân tích hậu quả, chứ đừng gân cổ cãi.
- Tin là đúng? Giữ lập trường – đừng gật đại cho yên chuyện.

**3. 🛠 NĂNG LỰC – Làm được hay không, nhìn lúc hệ thống rối mới biết**
Năng lực không phải thứ để trưng. Là thứ bạn dùng để thực thi.
— Covey

Tôi đã thấy BA:
- Gặp tình huống lạ là đứng hình
- Gặp dev hỏi khó là né
- Có bug thì đổ cho “khách nói vậy”, chứ không dám soi lại chính mình

Lúc bình thường ai cũng nói được. Lúc hệ thống bắt đầu lệch... mới biết ai thiệt sự hiểu.
📌 Muốn rèn?
- Đừng khoe mình biết. Hỏi: “Mình có xử lý được khi hệ thống lệch 1 nhịp không?”
- Gặp lỗi → đào ngược lại: “Mình thiếu kỹ năng gì?”
- Họp xong → tự hỏi: “Mình hiểu bản chất hay chỉ copy lời khách?”

**4. ■ KẾT QUẢ – Làm được việc. Làm ra chuyện. Làm tới nơi.**
Năng lực mà không ra kết quả → vẫn chỉ là lý thuyết.
— Covey
Tôi không quan tâm bạn học mấy khoá BA. Tôi chỉ hỏi:
- Bạn từng phân tích xong trọn vẹn 1 flow phức tạp nào chưa?
- Có lần nào dev/tester khen: “Spec lần này chuẩn đấy!”
- Có lần nào khách bảo: “Team này dễ làm việc ghê” nhờ bạn xử lý?

Nếu không có – thì sorry, nói mấy cũng không ai tin.
📌 Muốn rèn?
- Ghi lại từng task làm xong → đo bằng thứ người khác thấy
- Tự hỏi mỗi tuần: “Mình để lại gì đáng kể?”
- Làm một việc thật chỉn chu → lấy làm bằng chứng sống cho lần sau

■ KẾT
Bạn không mất niềm tin vì một cú fail. Bạn mất vì từng chút một – team phải lo hộ bạn mà bạn không biết. Niềm tin không nổ tung. Nó rút đi lặng lẽ. Và bạn chỉ biết khi:
- Task quan trọng không còn đến tay bạn
- Chat vẫn hoạt động, nhưng chẳng ai tag tên bạn nữa


---

## DAY 40/100 — 5 CÂU HỎI SỐNG CÒN TRƯỚC KHI PHÂN TÍCH HỆ THỐNG

*Trang 91–94*

“Em làm nhanh cái hệ thống ABC nhé.”
Và thế là BA bắt đầu đi phân tích hệ thống – nhưng thật ra không hiểu:
- Hệ thống này để làm gì?
- Giải quyết nỗi đau nào?
- Ảnh hưởng tới ai?
- Chạm tới tầng nào trong quy trình vận hành?

● Đó là cách hàng loạt dự án "làm đúng nhưng vẫn toang".
**Một BA cứng không lao vào viết tài liệu, vẽ diagram, mà lùi lại một bước để nhìn tổng thể cuộc chơi.**

💬 **Họ bắt đầu bằng 5 câu hỏi sống còn dưới đây – nghe tưởng đơn giản, nhưng nếu bạn chưa hỏi đến nơi đến chốn, một lúc nào đó dự án sẽ gặp khó khăn.**

■ **Câu 1: “Tụi mình đang muốn giải quyết vấn đề gì – thật sự?”**
Câu này để xác định:
→ Thay đổi bạn sắp phân tích là chuyện nhỏ trong thao tác,
→ Hay là thay đổi cả quy trình vận hành?
● Một BA giỏi không vội vẽ hệ thống, mà phân tầng bài toán để biết mức độ ảnh hưởng, rủi ro, và cách thiết kế phù hợp.
📌 Chỉ đơn giản giúp thao tác nhanh hơn? Thì chỉ cần chỉnh UI, bổ sung tính năng nhỏ – không ảnh hưởng đến hệ thống chung.
Ví dụ: gộp 2 màn hình thành 1, thêm ô tìm kiếm để đỡ cuộn.
📌 Hay thay đổi cả quy trình của nhiều bộ phận? Thì phải phân tích kỹ các vai trò liên quan, cập nhật lại hướng dẫn vận hành, và có kế hoạch chuyển đổi quy trình.
Ví dụ: sửa lại flow duyệt hợp đồng → đụng cả team pháp lý, kế toán.

✦ Nhiều BA thấy tên yêu cầu nghe quen – tưởng là thay đổi đơn giản.
Nhưng nếu không hỏi kỹ, có thể bạn đang đụng tới:
→ Quy trình giao nhận
→ Phân quyền duyệt giá
→ Logic chia hoa hồng
→ KPI giao hàng
... mà không hề hay biết.
💬 Nếu bạn không làm rõ ngay từ đầu → bạn sẽ thiết kế hệ thống quá giới hạn hoặc quá sơ sài, không đáp ứng được yêu cầu thật sự.

■ **Câu 2: “Ai sẽ là người vui – và ai có thể ‘phá’ nếu không được tham gia?”**
Một BA giỏi không chỉ hỏi người đưa yêu cầu. Họ sẽ truy ngược xem: ai khác cũng bị ảnh hưởng bởi thay đổi này – dù không được nhắc tên.
● Trong công ty, luôn có những vai như sau:
◆ Sếp khởi xướng dự án: rất hào hứng, muốn đẩy nhanh tiến độ
→ Bạn nên liên tục cập nhật để giữ nhịp triển khai
◆ Kế toán – người đang quen nhập số liệu theo cách cũ
→ Nếu không được hỏi sớm, có thể sẽ phản đối vì “không phù hợp quy trình tài chính”
→ Bạn cần mời họ vào validate luồng từ đầu
◆ Nhân viên vận hành – người đang làm việc thủ công
→ Có thể lo hệ thống mới sẽ “lấy mất việc của mình”
→ Bạn cần giúp họ thấy vai trò mới, không né tránh
◆ Những người ghét thay đổi
→ Thường không nói gì nhưng rollout là... không dùng
→ Bạn nên tạo cơ hội để họ góp ý, để có cảm giác "mình là một phần của thay đổi"
✦ Nếu bạn bỏ sót những vai này:
→ Hệ thống làm xong dễ bị chặn, bị làm khó, hoặc golive rồi... lặng như tờ.
📌 BA cấp cao không “dự đoán theo cảm tính” – mà vẽ ra bản đồ ảnh hưởng, rồi quyết định:
→ Ai cần hỏi trước?
→ Ai nên mời góp ý?
→ Ai cần update thường xuyên?
→ Ai cần nói chuyện riêng?

■ **Câu 3: “Hiện tại mọi người đang xử lý ra sao – và vì sao cách đó vẫn sống được?”**
Trước khi đập đi làm lại, BA cần biết:
→ Cái hệ thống cũ kia – dù “cùi” – nhưng sao vẫn chạy được suốt mấy năm qua?
● Có nhiều thứ tưởng là tạm bợ, nhưng thực ra đang giữ cả quy trình sống sót:
Team sale dùng file Excel phức tạp để tổng hợp doanh thu cuối ngày.
→ Trong đó có công thức riêng, mã hóa màu, shortcut tắt mà chỉ họ hiểu.
→ Nếu bạn làm hệ thống mới mà không thay được logic đó → họ sẽ... dùng lại file cũ.
Bên vận hành xử lý lỗi bằng Zalo, chụp màn, gửi tay, check với kho rồi nhập.
→ Nghe thủ công, nhưng giúp họ xử lý linh hoạt hơn bất kỳ flow cứng nhắc nào bạn vẽ ra.
Kế toán đang “lách” nghiệp vụ bằng cách nhập tạm mã rồi sửa sau để chạy kịp deadline
→ Nếu hệ thống mới bắt nhập đúng từ đầu mà không cho phép sửa sau → họ sẽ phản ứng hoặc không dùng.
✦ Nếu bạn không hỏi – không quan sát – không phân tích:
→ Bạn sẽ “tự tin xóa cái cũ” rồi nhận ra hệ thống mới đẹp... nhưng không sống nổi.

📌 Một BA giỏi không chỉ biết quy trình chính thức, mà còn hiểu cả phần “lách luật”, “chống cháy” và “sáng tạo ngầm” của người dùng – để thiết kế giải pháp thật sự thay thế được thói quen cũ.

■ Câu 4: “Làm xong rồi thì... thế nào gọi là thành công?”
Hệ thống làm xong, chạy được, không lỗi – chưa chắc đã thành công.
● Câu hỏi này giúp BA bóc ra:
- Thành công là gì theo góc nhìn sếp?
- Người dùng muốn thấy gì thay đổi?
- Có chỉ số nào đo được kết quả không?

📌 Vì nếu không có tiêu chí rõ ràng, bạn sẽ rơi vào tình huống:
- “Tôi không thấy hệ thống này cải thiện gì cả.”
- “Vẫn phải làm tay như cũ.”
- “Chạy rồi, nhưng tốn thời gian hơn.”

■ **Câu 5: “Đã ai từng làm cái này chưa – và... gãy ở đâu?”**
Một BA giỏi không chỉ phân tích thứ mình thấy.
Họ đi đào những thứ từng được làm – và từng thất bại.
● Vì hệ thống bạn sắp phân tích có thể:
- Đã từng được team khác làm rồi
- Từng fail vì thiếu 1 logic nhỏ
- Từng làm tốt, nhưng không sống nổi khi rollout
📌 Nếu không hỏi – bạn sẽ đâm đầu vào đúng cái hố mà người khác từng rơi.
🔍 Ví dụ thật:
- Hệ thống theo dõi hiệu suất kỹ thuật viên từng được triển khai.
→ Nhưng gãy vì... nhân viên không chịu chấm công → không đủ dữ liệu → dashboard đẹp nhưng toàn số 0
→ BA mới không tìm hiểu → build lại hệ thống khác, rồi cũng... fail
- Có team từng làm hệ thống nhập đơn hàng
→ Nhưng khách hàng phản hồi sai số liên tục → do dữ liệu đầu vào không được kiểm tra định dạng kỹ
→ BA mới build lại giao diện đẹp hơn... nhưng không sửa luật nhập liệu → gãy tiếp vòng 2
✦ Nếu bạn bỏ qua lịch sử: Bạn sẽ tốn công lặp lại đúng sai lầm – mà tưởng mình đang làm mới.
📌 Một BA cứng sẽ luôn hỏi:
- Hệ thống cũ đâu? Ai từng làm? Có tài liệu không?
- Có ai đang dùng workaround để sống sót thay vì hệ thống?
- Có đối thủ hay bên khác đang làm tương tự để mình học?
Không để bị tự tin quá sớm → rồi lặp lại thất bại mà đáng lẽ có thể né được.

💬 “Đọc đến đây chắc sẽ có bạn làm BA outsource hơi chạnh lòng vì bạn không được quyền hỏi quá nhiều, bạn có thể không quyết được hệ thống sẽ đi đâu – nhưng nếu tư duy đúng, bạn vẫn là người giữ nó không toang trên đường đi.”
🧠 Nếu bạn từng bị dí vào một dự án, đầu chưa kịp hiểu bài toán – tay đã phải vẽ flow...
Nếu bạn từng viết xong tài liệu mới nhận ra: “Ơ, hóa ra mình đang thiết kế sai tầng logic?”
Hãy bookmark lại 5 câu hỏi này – và đừng bao giờ phân tích khi chưa hỏi đủ.


---

## DAY 41/100 — LÀM BA HỆ TÍCH HỢP – ĐỪNG HỎI "NẾU LỖI THÌ SAO?", HÃY THIẾT KẾ ĐỂ KHÔNG AI CÒN PHẢI HỎI

*Trang 95–96*

● **Bối cảnh:**
Mỗi khi khách mua hàng tại cửa hàng → điểm sẽ được cộng vào tài khoản loyalty trên app khách hàng. Luồng tưởng như đơn giản:
- POS bắn data sang loyalty
- Loyalty cập nhật điểm
- CRM ghi nhận hành vi mua hàng
Nhưng khi chạy thật:
- Nhiều cửa hàng mạng yếu → POS bắn chậm hoặc bắn lỗi
- Loyalty không nhận được → khách không thấy điểm
- CRM vẫn ghi nhận là đã mua → tạo dữ liệu bất nhất giữa 3 hệ thống
🔥 Kết quả?
- Khách gọi hotline: “Tôi mua rồi mà điểm đâu?”
- Nhân viên cửa hàng bị trách oan dù không rõ nguyên nhân
- CRM báo báo cáo tăng nhưng loyalty thì không
- Ban lãnh đạo ra quyết định sai vì báo cáo dựa trên dữ liệu đã lệch

💣 **Và đây là lúc một BA senior không còn hỏi kiểu:**
“Nếu POS fail thì sao?”
“Nếu loyalty chưa nhận thì rollback được không?”
✖ Những câu hỏi đó là quá muộn.
■ Một BA thực chiến sẽ dựng framework ngay từ đầu.

● **Đẳng cấp senior là gì?**
Không hỏi “Nếu... thì sao?”, mà chủ động dựng cơ chế chịu lỗi, trace lỗi, và quản lý lỗi như một phần của thiết kế.
1. **Define flow chịu lỗi ở cấp hệ thống**
Ngay khi vẽ luồng App → POS → Loyalty → CRM, BA đã xác định:
- Nếu POS gửi sang Loyalty thất bại → lưu tạm data local, tự retry sau 1h
- Nếu Loyalty xử lý lỗi → hệ thống bắn cảnh báo cho BA / Vận hành / CSKH
- Có email cảnh báo nội bộ khi có 3 lần retry liên tiếp thất bại để xử lý thủ công

2. **Tách sync thành 2 giai đoạn: Gửi – và xác nhận đã nhận**
Không coi việc gửi xong là xong. Cần thiết kế:
- Sau khi gửi, Loyalty phải phản hồi “ACK” để xác nhận đã nhận
- Nếu không có ACK → chuyển bản ghi vào hàng đợi retry + log cảnh báo
- Có thêm API để support kiểm tra trạng thái sync từng đơn
→ “Đơn #1234 được POS gửi lúc 10:00. Loyalty không ACK → chuyển hàng đợi retry → cảnh báo bật đỏ trên dashboard theo dõi.”

3. **Thiết kế hệ thống audit log trung lập**
Mọi hệ thống đều đẩy log chuẩn về 1 nơi, để trace bất kỳ vấn đề nào. Khách khiếu nại không thấy điểm. Gõ ID khách vào loghub:
- POS gửi 10:03
- Loyalty nhận 10:03:01
- Xử lý lỗi format → điểm không ghi
- Cảnh báo lúc 10:03:05

4. **Thiết lập SLA dữ liệu chéo hệ thống**
Mỗi hệ thống phải xử lý đúng hạn – nếu chậm phải có cảnh báo, có dashboard theo dõi.
→ “SLA đặt: POS gửi → Loyalty xử lý trong 2 phút.
- Nếu quá 2 phút → dashboard highlight đỏ → báo lỗi.
- Nếu quá 5% đơn bị chậm/ngày → loyalty phải giải trình.

5. **Vẽ contract giữa các hệ thống**
Không ai được gửi field lung tung hoặc thay đổi format không báo trước.
→ “Trường customer_id bắt buộc là UUID v4.
Nếu POS gửi sai → Loyalty reject.
POS chịu trách nhiệm validate trước.
Mọi thay đổi field cần thông báo trước 5 ngày và cập nhật version API contract.”

📌 Một câu để đời dành cho BA: “Tôi không thiết kế hệ thống để chạy đúng – tôi thiết kế nó để không bao giờ gãy khi có một ai đó làm sai.”
📢 Còn bạn?
Bạn đang tích hợp bao nhiêu hệ thống?


---

## DAY 42/100 — GỠ CASE CONFLICT: KHI DEV TỪ CHỐI IMPLEMENT LOGIC BA PHÂN TÍCH

*Trang 97–98*

● **Bối cảnh: Module xin nghỉ – chấm công trong hệ thống nội bộ**
Junior BA đề xuất một logic đơn giản:
- Nếu user xin nghỉ nửa ngày
- Nhưng chưa có chấm công buổi sáng
→ Hiển thị cảnh báo nhẹ để kiểm tra lại (không chặn, không huỷ)
DEV phản hồi:
- Tốn effort
- Không cần thiết
- Trường hợp này người dùng cần tự kiểm soát
Cả phòng im. Junior BA nhìn xuống tài liệu. PM nhìn sang tôi.

🧠 Tôi không tranh luận đúng sai. Tôi chỉ hỏi:
“Nếu không có cảnh báo, hệ thống đang để chuyện gì xảy ra mà không ai nhìn thấy?”

■ **1. Phân tích hậu quả ở tầng vận hành – không nói cảm xúc, chỉ nhìn vào hệ quả**
“User quên check-in, xin nghỉ chiều → bị tính nghỉ cả ngày. Tháng đó có 17 tình huống tương tự. HR phải xử lý thủ công, truy log, điều chỉnh bảng lương.”
→ Hậu quả không chỉ nằm ở thao tác người dùng
→ Mà lan đến bộ phận vận hành và độ tin cậy của hệ thống.

■ **2. Hệ thống không phải là bảo mẫu**
Nhưng nếu để mặc user sai mà không cảnh báo. Thì hệ thống đang bỏ trống một trách nhiệm cơ bản. Tôi nói với DEV: “Không ai mong hệ thống làm thay user. Nhưng hệ thống cần đưa đủ thông tin – để user không vô tình gây lỗi.”
“Chỉ cần hiển thị: ‘Bạn chưa có chấm công sáng – vui lòng kiểm tra trước khi gửi đơn nghỉ.’
Không chặn luồng, không thay đổi logic – nhưng giảm được phần lớn lỗi nghiệp vụ.”

■ **3. Tôi không hỏi “làm được không” – tôi hỏi: “nếu không làm, phần này để ai gánh?”**
Tôi nói nhẹ: “Khi người dùng bị trừ lương do thiếu cảnh báo – có ai đứng ra nói đây là vấn đề thiết kế không? Hay tất cả đều im – rồi HR xử lý lại, còn người dùng thì tự hiểu là ‘chắc do lỗi của mình’?”
Tôi không cần câu trả lời. Cả phòng đều hiểu, nếu logic này không có ai đứng ra nhận thì hệ thống đang vận hành với một vùng trách nhiệm bị bỏ ngỏ.

💬 Tôi không phải người giỏi nhất trong phòng họp. Nhưng khi mọi người bắt đầu im khi các bên né tránh phần khó. Tôi biết: nếu không ai lên tiếng, hệ thống sẽ tiếp tục cho phép lỗi xảy ra như một điều bình thường. Tôi cũng từng nghĩ: “Ghi nhận rồi để đó.”

Nhưng rồi tôi nhớ đến một câu nói tôi từng đọc – của Harry Truman, Tổng thống Mỹ
Người đặt tấm bảng trên bàn làm việc suốt nhiệm kỳ với dòng chữ:
“The buck stops here.”
(Câu này hay có ở phòng CTSV FPT Polytechnic hồi tôi còn là SV)
Ông ấy không phải người viết phần mềm. Nhưng ông hiểu một điều quan trọng:
Khi không ai chịu trách nhiệm, sẽ cần một người đứng ra – để mọi thứ không tiếp tục trôi đi trong im lặng. Và tôi chọn dừng nó lại ở tôi. Không phải vì tôi luôn đúng mà vì tôi biết: Nếu BA không giữ hệ thống, thì không ai giữ giúp mình đâu.


---

## DAY 43/100 — TƯ DUY BUSINESS GOALS – REQUIREMENT KHÔNG PHẢI TỰ SINH RA

*Trang 99–100*

**Nếu bạn vẫn nghĩ BA đi phân tích yêu cầu là để làm tính năng, thì bạn đang hiểu sai bản chất nghề này ngay từ bước đầu.**

● **Không ai thật sự “cần” tính năng**
Người dùng không thật sự cần một tính năng. Họ cần kết quả mà tính năng đó mang lại.
- Khi họ nói “cần lọc danh sách” → họ đang cố gắng tìm ra nhóm khách để hành động.
- Khi họ nói “cần dashboard” → họ muốn quản lý được tình hình để ra quyết định.
- Khi họ nói “cần gửi thông báo” → họ đang muốn gắn kết với người dùng và giữ chân khách hàng.
Còn BA – nếu không đào tới tầng “họ muốn đạt được gì”, mà chỉ dừng ở việc “họ nói cần gì” → là đang làm ở tầng bề mặt.
Tổ chức cũng vậy.
- Họ không thật sự cần “form nhập liệu đầy đủ”, “lọc nâng cao” hay “tính năng mới mỗi sprint”
- Họ cần những hành động rõ ràng giúp cải thiện hiệu quả về doanh thu, chi phí, vận hành, con người.
Nếu requirement bạn viết ra không dẫn tới hành động cụ thể nào tạo giá trị thì đó không phải requirement mà là chi tiết thừa đang ngốn effort của cả team.

🧠 **Requirement là kết quả cuối cùng của một chuỗi tư duy logic 4 tầng**
Nó không phải điểm xuất phát. Nó là đầu ra sau khi BA đi hết một vòng truy vấn:
“Tổ chức muốn gì → Đang mắc gì → Có cách nào gỡ → Hệ thống cần làm gì”
**Business Goal**
→ Mục tiêu tổ chức cần đạt: tăng doanh thu, giữ chân khách, tối ưu chi phí...
**Vấn đề đang cản trở**
→ Những điểm nghẽn trong quy trình hiện tại khiến mục tiêu chưa đạt.
**Giải pháp khả thi / giả thuyết hành động**
→ Những hướng đi có khả năng gỡ nút thắt, dựa vào insight hoặc dữ liệu.

**Requirement**
→ Hệ thống cần làm gì để giúp người dùng hiện thực hoá giải pháp đó.
Nếu bạn nhảy thẳng từ "ý kiến người dùng" → "viết tài liệu" mà không truy ngược 3 tầng trên bạn đang phân tích theo phản xạ – không phải theo chiến lược.

🧩 **Tình huống: Người dùng bảo “cần lọc nâng cao danh sách khách hàng”**
BA non tay sẽ:
- Ghi lại các trường cần lọc
- Vẽ form chi tiết, chỉnh UI
- Giao DEV code
→ Làm đúng. Nhưng sai hướng. Vì người dùng không thật sự cần nó.
BA hiểu tư duy mục tiêu sẽ:
- Hỏi: “Sau khi lọc xong, bạn định làm gì tiếp theo?”
- Tìm ra mục tiêu thật: phân bổ danh sách khách chưa được gọi để tăng hiệu suất telesales
- Đề xuất giải pháp: Tự động gợi ý danh sách khách chưa đủ số lần gọi, phân nhóm theo khu vực
→ Tính năng gắn trực tiếp với hành vi tạo giá trị.

▲ **Sai lầm lớn nhất của BA không phải là viết thiếu field**
mà là viết ra những yêu cầu không có liên kết với mục tiêu tổ chức. Và những gì không gắn với mục tiêu sớm muộn cũng sẽ bị loại bỏ.

🛠️ **Hãy luôn tự hỏi:**
■ Tổ chức đang cố đạt được điều gì?
■ Đâu là rào cản khiến họ chưa đạt?
■ Người dùng đang kỳ vọng điều gì sẽ thay đổi sau khi có tính năng này?
■ Nếu không có yêu cầu này, chỉ số nào sẽ bị ảnh hưởng?
Chỉ khi bạn trả lời được hết mới nên đặt tay viết requirement.
🧠 **Ghi nhớ:**
Bạn không phải người ghi lời. Bạn là người kết nối mục tiêu với hành động. Nếu requirement của bạn không giúp ai đạt được điều gì
→ nó chỉ là dòng mô tả trôi giữa hệ thống mà không ai nhìn lại.


---

## DAY 44/100 — Ở MỘT CÔNG TY NỌ – CÓ NGƯỜI BA MANG CHỮ C TRÊN NGỰC ÁO

*Trang 101–102*

Ở một công ty nọ, có những dự án bắt đầu bằng cụm từ “rất gấp”, nhưng rồi trôi vào im lặng cũng bằng chính cụm từ ấy: “Giờ ưu tiên cái khác trước nhé.” Người BA bước vào dự án với niềm tin: Chỉ cần mình làm đủ tốt, đủ kỹ, đủ trách nhiệm thì hệ thống sẽ đi tới đích.
Nhưng rồi:
- Họ viết ra một tài liệu dày 600 trang, không ai mở
- Họ vẽ flow rõ như lòng bàn tay, nhưng DEV bảo cái này làm khó lắm, gọt bớt đi
- Họ hỏi user 5 lần, vẫn không ai chắc mình cần gì
- Họ cố gắng giữ timeline, rồi bị dí ngược: “Tại sao lại chưa làm xong?”
Và tệ nhất, là cảm giác bị đứng giữa nhưng không thuộc về đâu cả.
- DEV coi bạn là “người ngoài” không hiểu kỹ thuật
- Bên kinh doanh thì nói bạn “không nắm rõ nghiệp vụ”
- Còn PM thì bảo: “Em chỉ cần làm tài liệu thôi, mấy chuyện ưu tiên đã có anh lo”
Giữa những khoảng cách đó chỉ còn một thứ duy nhất khiến người BA vẫn tiếp tục:
**Chữ C trên ngực**

👕 Nhưng chữ C đó...không chỉ nằm trên ngực. Nó còn là băng đội trưởng – như trong bóng đá, không ai trao, không có buổi họp công nhận. Chỉ là một ngày, khi mọi người im lặng, deadline nhạt dần và hệ thống như chờ để bị bỏ lại, bạn siết tay lại và tự nói thầm: “Để tôi dẫn tiếp”

Bạn không phải người ghi bàn, không có commit code, không lên báo cáo thành tích. Nhưng bạn là người kéo đội hình không bị gãy, người bảo vệ logic không bị bóp méo. Người giữ sản phẩm không bị mất hồn. Và nếu bạn gục, cả hệ thống sẽ gục theo

🔎 **C là gì?**
C là ‘Cam kết’ – Commitment. Không phải với sếp, không phải với deadline. Mà là cam kết với người dùng mà bạn đã từng nói chuyện, với hệ thống mà bạn đặt cả logic và tâm huyết vào. Bạn không có quyền force ai làm. Bạn không có quyền duyệt ngân sách. Bạn không có quyền yêu cầu user phải hiểu mình. Nhưng bạn vẫn mở backlog

Vẫn dọn lại task, vẫn gửi từng câu hỏi nhẹ nhàng cho DEV:
“Nếu mình đổi hướng chỗ này, có khả thi hơn không?”
Bạn vẫn gọi lại cho stakeholder dù đã bị "seen" 3 lần
Bạn vẫn đi họp đều đặn, dù biết sẽ lại là một buổi “nói mà không có ai lắng nghe thật sự”

▲ **Và mỗi ngày như vậy – không ai biết**
mỗi lần gõ bàn phím viết tài liệu là một lần bạn tự hỏi:
“Mình còn nên tin vào sản phẩm này không?”
“Nếu mình buông, có ai làm tiếp không?”
“Nếu hệ thống không ra đời, người dùng kia sẽ ra sao?”

🧠 **Người BA mang chữ C – không phải là người giỏi nhất**
Họ chỉ là người kiên định đến mức dại khờ. Tin rằng nếu đã hiểu được một nỗi đau thật sự, thì không thể nào làm ngơ

💬 Nếu bạn từng cố gắng nói một lần cuối để bảo vệ một logic đang bị lược bỏ
Nếu bạn từng nhìn DEV lắc đầu, PM lảng tránh, User không phản hồi nhưng bạn vẫn nghĩ:“Mình còn làm được gì để cứu hệ thống này không?”
Thì bạn – chính bạn – là một người đang mang chữ C mà không cần ai phong tặng
Và nếu bạn từng giữ chữ C ấy trong thầm lặng – tôi chỉ muốn nói một câu thật nhẹ:
Cảm ơn bạn – vì đã không bỏ cuộc. Dù chẳng ai nhận ra – nhưng tôi biết, hệ thống đó còn sống... là vì có bạn


---

## DAY 45/100 — NẾU BẠN BỊ NÉM VÀO GIỮA MỘT DỰ ÁN HỖN LOẠN ĐÂY LÀ CÁCH ĐỂ KHÔNG LẠC HƯỚNG

*Trang 103–104*

Bạn vừa được “đẩy” vào một dự án đang chạy. Không onboarding, không hệ thống tài liệu, không ai nói cho bạn biết chuyện gì đang xảy ra.
- Dev thì bận build tính năng.
- QC thì nhìn bạn đầy ái ngại.
- Còn PM thì chỉ nói một câu quen thuộc: “Em cứ làm theo tài liệu cũ nhé, có gì anh confirm sau.”
Và rồi bạn... ngồi đó. Mở Figma. Mở Jira. Lướt. Không biết nên hỏi gì trước, nên bắt đầu từ đâu. Mỗi ngày trôi qua, bạn thấy mình đang "có mặt" trong dự án, nhưng không thực sự hiểu dự án.
Nếu bạn đang ở trong cảm giác ấy – tôi đã từng ở đó. Và nếu bạn không muốn tiếp tục mông lung, thì đây là cách tôi sẽ chỉ bạn dựng lại nền từ đầu.

● **Trước hết, đừng vội nhận task. Dừng lại.**
Tôi không đùa. Tắt Jira, tắt Figma. Lấy một tờ giấy ra, và trả lời 3 câu này:
1. **Hệ thống này đang giải quyết vấn đề gì?**
- Là hệ thống lõi vận hành? Hay chỉ là công cụ hỗ trợ?
- Nếu nó ngừng chạy, phòng ban nào sẽ bị ảnh hưởng đầu tiên?
- Câu trả lời này sẽ cho bạn biết đâu là phần quan trọng cần nắm, đâu là phần có thể học sau.
2. **Ai là người dùng thật sự?**
- Họ dùng mỗi ngày để làm gì?
- Chỉ nhập dữ liệu, xử lý công việc, hay kiểm tra và phê duyệt?
- Mỗi nhóm người dùng có kỳ vọng khác nhau – và bạn cần biết họ đang cố đạt được điều gì khi dùng hệ thống.
3. **Dữ liệu đang chảy theo cách nào?**
- Dữ liệu tạo ra từ đâu – ai là người nhập – có bị sửa không?
- Có đi qua các bước trung gian? Có được kiểm soát, đối chiếu?
- Dữ liệu là máu của hệ thống. BA không nhìn thấy dòng chảy dữ liệu thì không phân tích được gì.
■ Nếu chưa trả lời được 3 câu này, bạn chưa nên đụng vào bất kỳ task nào.

Sau đó, tôi sẽ chỉ bạn 4 việc tôi luôn làm – luôn hiệu quả:
1. **Vẽ lại hệ thống bằng cách hiểu của bạn**
Không cần UML. Không cần đúng 100%.
Chỉ cần:
- Module nào làm gì?
- Ai tương tác với ai?
- Dữ liệu đi qua đâu?
- Trạng thái thay đổi ở điểm nào?
Vẽ sai cũng được. Nhưng sau 3 lần chỉnh, bạn sẽ hiểu hệ thống hơn bất kỳ ai không đụng tay. BA không cần bản vẽ đẹp. BA cần nhìn được mạch sống hệ thống.
2. **Tạo bảng excel “Hiểu – Cần xác nhận – Chưa rõ”**
Dừng việc hỏi “cái này là gì vậy anh?”
Tạo 3 mục rõ ràng:
■ Đã nắm chắc
❓ Cần xác nhận lại
● Chưa hiểu, hoặc còn thiếu dữ liệu
Mỗi buổi họp, mỗi cuộc trao đổi, bạn đem bảng này ra “chốt điểm mù”. Khi bạn hỏi để xác nhận logic, bạn không còn là người mới. Bạn đang dẫn dắt lại tiến trình hiểu hệ thống.
3. **Quan sát trước khi hỏi**
Trong tuần đầu tiên, đừng lao vào hỏi loạn lên. Hãy quan sát ai là người:
- Hay được tag vào confirm logic
- Thường đưa ra câu hỏi khó
- Được nhờ “check hộ” khi mọi người rối
Đó là những người đang thực sự nắm logic. Tiếp cận họ sau khi bạn đã có bản vẽ sơ bộ, đã ghi chú nghiêm túc – họ sẽ tôn trọng bạn. Đừng tìm người giỏi nhất. Tìm người làm thật nhất. Họ là người sẽ mở khóa hệ thống cho bạn.
4. **Tự xây Knowledge Base cá nhân**
Tài liệu nội bộ luôn thiếu. Bạn hãy tự ghi lại mọi thứ:
- Luồng xử lý chính
- Luật nghiệp vụ
- Từ vựng đặc thù hệ thống
- Những điểm team làm theo thói quen, không ghi trong spec
Sau vài tuần, bạn sẽ có một kho dữ liệu sống – giúp bạn (và cả người khác) không bao giờ bắt đầu lại từ số 0.


---

## DAY 46/100 — DỰ ÁN CÓ SẾP QUÁ KỸ TÍNH LÀM SAO KHÔNG BỊ CUỐN THEO TỪNG COMMENT VỤN

*Trang 105–106*

Có những dự án không thiếu người, không thiếu tiền. Sếp cũng rất tâm huyết, luôn theo sát từng bước. Chỉ là... quá kỹ tính.
Không kỹ về nghiệp vụ – mà kỹ về... từng dấu chấm, từng dòng text, từng icon.
- “Chỗ này sao em dùng từ ‘xuất hiện’? Nghe hơi cứng.”
- “Dòng này nên tách ra, anh đọc thấy hơi nặng mắt.”
- “Cái flow em vẽ... nhìn chưa mượt.”
Bạn là BA, bạn vào dự án với tâm thế: mình sẽ phân tích nghiệp vụ thật chắc, viết logic thật gọn, flow thật chuẩn.
Nhưng rồi từng buổi review, từng file SRS bị xé nhỏ thành hàng chục comment không liên quan đến hệ thống. Và đến một lúc, bạn bắt đầu không còn thấy bản thân trong chính tài liệu mình viết.

● **Những nỗi đau thầm lặng trong dự án có sếp “kỹ tính”**
- Không có lỗi lớn – nhưng comment thì không dứt
- Tài liệu không sai – chỉ là... “chưa đủ mượt”
- Không ai hỏi: “User cần gì?” – chỉ nghe: “Câu này nên viết lại.”
- Bạn chỉnh wording đến lần thứ 4 – vẫn không đúng cảm giác sếp mong muốn

🧠 **3 bước thực chiến để BA sống sót khi sếp quá kỹ**
■ **1. Làm rõ đâu là phần cần chốt trước – đâu là phần có thể chỉnh sau**
Trước khi gửi bản tài liệu cho sếp, hãy hỏi thẳng mình:
- Cái gì là business logic cốt lõi, nếu sai thì hệ thống gãy?
- Cái gì là hình thức, nếu chưa chỉnh thì vẫn dùng được?
- Nếu phải sửa – thứ gì bắt buộc phải làm trước, thứ gì có thể dời sau?
● Mục đích: Phân tầng ưu tiên để khi comment đến, bạn không bị “vỡ trận”.

■ **2. Trong lúc review – chủ động phân loại và định hướng**
Khi sếp bắt đầu “soi từng chữ”, đừng cãi – cũng đừng sửa ngay. Thay vào đó, nói như một Senior BA: “Em xin phép tách góp ý thành 2 nhóm:
- Nhóm A: Các ý ảnh hưởng đến logic → em sẽ ưu tiên xử lý trong vòng này
- Nhóm B: Các ý về diễn đạt, trình bày → em sẽ ghi nhận và cập nhật sau khi logic đã chốt, để tránh sửa qua sửa lại nhiều vòng và ảnh hưởng DEV.”
Bạn không chống lại feedback – bạn chia nhóm để xử lý. Và bạn là người đưa ra đề xuất.

■ **3. Sau khi chốt logic – đóng file đúng cách, chặn vòng feedback vô hạn**
Khi bạn đã xử lý xong phần nghiệp vụ → đừng im lặng. Phải gửi thông báo đóng vòng review nội dung chính: “Phần nghiệp vụ hiện đã ổn định để DEV bắt đầu triển khai. Em xin phép đóng phần nội dung logic, và chuyển sang xử lý các phần trình bày theo checklist góp ý. Mọi góp ý mới nếu có, em xin phép sẽ tổng hợp vào bản cập nhật tiếp theo.”
● Câu này giúp bạn giữ timeline, chốt version, và tránh bị lôi đi comment tiếp sau mỗi lần “sếp đọc lại lần nữa”.

📌 Bạn không thể thay đổi việc sếp kỹ. Nhưng bạn phải giữ được giá trị nghề nghiệp của mình. Một BA giỏi không nằm ở việc “sửa câu cho mượt”, mà nằm ở việc giữ vững hệ thống – và dẫn dắt cả team vượt qua vòng lặp chỉnh sửa không hồi kết.


---

## DAY 47/100 — BRANCH, MERGE, PULL REQUEST, TAG... GIẢI THÍCH LẠI GIT ĐỂ BA KHÔNG NGỒI HỌP NHƯ NGƯỜI NGOÀI HÀNH TINH

*Trang 107–109*

🗣️ **Một ngày bình thường và một loạt từ ngữ kỳ lạ ập đến**
- DEV bảo: “Tôi đang checkout nhánh hotfix.”
- Tester nói: “Commit này có được cherry-pick lên PROD không chị?”
- PM hỏi: “Tính năng A đã merge chưa, có nằm trong bản tag v2.3.0 không?”
**Bạn không cần vào Git để kiểm tra, nhưng bạn phải hiểu họ đang nói gì để trả lời đúng, không ngơ ngác, và không đổ lỗi sai người.**

🧠 **Vậy Git là gì – kể cho BA nghe cho dễ hiểu?**
Git là hệ thống quản lý phiên bản mã nguồn giống như “lịch sử chỉnh sửa tài liệu” dành cho lập trình viên. Git giúp DEV:
- Làm việc song song trên nhiều branch
- Lưu lại từng thay đổi bằng commit
- Hợp nhất lại bằng merge
- Và xác định mốc release bằng tag version
BA không dùng Git, nhưng các khái niệm này ảnh hưởng trực tiếp đến tiến độ và chất lượng sản phẩm mà BA đang theo sát.

💡 **Dòng chảy thực tế của 1 tính năng**
1. **DEV tạo nhánh riêng để code**
Tính năng “Đăng nhập bằng số điện thoại” sẽ được DEV thực hiện trên một branch riêng (ví dụ: feature/login-by-phone) Nhánh main là bản chính thức, đang chạy ngoài production.
🚩 BA không cần vào Git, nhưng phải biết nhánh nào đang dev, để hiểu rõ trạng thái: “Tính năng này đang được làm, chưa ảnh hưởng hệ thống chính.”

2. **Test ở môi trường DEV**
Sau khi DEV push code, hệ thống CI/CD sẽ tự động deploy lên môi trường DEV. Tester test, báo bug, DEV sửa → commit tiếp → tự cập nhật.

🚩 BA cần hiểu:
“Giai đoạn này đang test ở DEV, chưa nghiệm thu.”
→ Báo cáo đúng trạng thái với PM, tránh nhầm với UAT.

3. **DEV tạo Pull Request để merge vào UAT**
Khi tính năng xong, DEV tạo Pull Request (PR) để xin merge vào nhánh uat. PR là nơi DEV khác có thể review code và BA có thể được tag vào nếu cần review logic hoặc validate lại yêu cầu.
🚩 BA không cần vào PR, nhưng phải nắm quy trình: Có PR mới → mới được merge lên UAT Merge rồi → mới được nghiệm thu

4. **Nghiệm thu tại UAT → Chốt Release**
Sau khi merge PR, hệ thống deploy bản test lên môi trường UAT. BA cùng QA kiểm tra lần cuối. Nếu đạt yêu cầu → BA nghiệm thu.
🚩 BA sẽ biết: “Tính năng A đã đủ điều kiện release, đã pass UAT.”

5. **Merge lên main → Gắn tag version → Release ra PROD**
DEV merge vào nhánh main, gắn tag (vd: v2.3.0) để xác định bản release. Hệ thống CI/CD đưa bản đó ra môi trường production.
🚩 BA không cần xem tag trong Git, nhưng phải được DEV/PM thông báo: “Bản release hôm nay là v2.3.0, bao gồm các tính năng A, B, C.”
→ Để update changelog, truyền thông nội bộ, hướng dẫn người dùng, v.v.

6. **Tình huống đặc biệt: Cherry-pick**
Một lỗi khẩn được sửa trong một commit nhỏ → DEV không muốn merge nguyên nhánh lớn đang còn test dở. Họ dùng cherry-pick chỉ lấy đúng commit cần thiết để đưa ra PROD.
🚩 BA không cần biết cherry-pick hoạt động thế nào, nhưng cần hỏi kỹ: “Lần release này chỉ có fix bug hay có cả tính năng A?”
→ Tránh truyền thông sai, báo khách "đã có" trong khi thực tế chưa merge toàn bộ.

✖ **Nếu BA không hiểu Git – hậu quả thực tế:**
**Tình huống 1:**
DEV bảo:
“Em ơi, nhánh này đang bị conflict nên anh chưa merge được.”
Bạn gật đầu nhưng không hiểu "conflict" là gì, không biết ảnh hưởng thế nào. Bạn vẫn báo lên PM rằng tính năng đã test xong, sẵn sàng lên UAT.
→ Rủi ro: Báo sai trạng thái. Cả team QA ngồi chờ code chưa bao giờ được merge.

**Tình huống 2:**
DEV nói: "Em chỉ cherry-pick đúng 1 commit fix bug vào PROD."
Bạn không hiểu "cherry-pick" là gì, tưởng là "đã merge toàn bộ tính năng". Bạn báo khách: “Dạ bản này có luôn phần tính năng A chị yêu cầu.”
→ Rủi ro: Khách kiểm tra không thấy, mất niềm tin. Bạn bị quy là báo sai, thiếu trách nhiệm.

📌 Mỗi team làm Git một kiểu, mỗi DEV dùng Git một cách. Còn BA thì thường đứng giữa, không biết nên hiểu đến đâu là đủ.

Bạn từng gặp tình huống nào dở khóc dở cười vì không hiểu Git chưa? Hoặc nếu bạn đã từng "bị kẹt" giữa DEV – QA – PM trong buổi họp release vì không rành merge, tag, PR,... thì chia sẻ thử vài câu chuyện bên dưới nhé.
Biết đâu mình cùng nhau rút được mấy tips sống sót nghề BA mà không cần chạm vào Git.


---

## DAY 48/100 — TESTER HỎI LẠI YÊU CẦU “RÕ RÀNG RỒI” BA NÊN PHẢN ỨNG RA SAO?

*Trang 110–112*

Một trong những thời điểm thể hiện rõ đẳng cấp của BA – không nằm ở lúc viết requirement, mà là khi bị hỏi lại... yêu cầu tưởng như đã “chắc cú”.

📌 **Bối cảnh thật:**
BA vừa viết xong đặc tả. Duyệt nội bộ xong, DEV đang code. Tester bắt đầu test, rồi một câu hỏi nhẹ nhàng bay tới: “Phần này chưa rõ lắm – người dùng nhập thế nào thì được tính hợp lệ?”
Bạn giật mình. Ủa rõ ràng ghi rồi mà? Sao lại hỏi?
Câu trả lời thường thấy:
✖ “Có ghi mà, bạn coi lại chỗ ABC đi.”
✖ “Ủa rõ ràng quá trời mà còn hỏi gì nữa...”
Sai. Rất sai.

✖ **Sai lầm của nhiều BA:**
Coi việc Tester hỏi lại là phiền, là bị làm phiền, thậm chí là tự ái. Họ quên mất rằng:
- Tester hỏi lại = Dấu hiệu cảnh báo sớm tài liệu có vấn đề.
- Bạn không sửa – thì lỗi đó sẽ ra production.
- Người dùng hỏi lại – và lần này không có cơ hội sửa nữa.

■ **Tư duy đúng:**
Câu hỏi của Tester chính là bài test ngược lại độ rõ ràng và logic của yêu cầu. Nếu một người chuyên phân tích test case mà còn “chưa hình dung được flow” thì chắc chắn yêu cầu đó có rủi ro hiểu sai, viết sai hoặc test thiếu.

🛠️ **3 kỹ thuật giúp BA phản hồi đúng cách khi bị hỏi lại:**
1. **Confirm lại yêu cầu bằng cách soát lỗi logic và diễn đạt**
📍 Gợi ý phản ứng đúng: Mở lại đoạn mô tả, đọc như người ngoài ngành. Tự hỏi:
- Có đang dùng từ mơ hồ?
- Có thiếu “nếu... thì...”?
- Có assumption nào chưa được viết ra?
📌 Ví dụ thực tế:
Yêu cầu ghi: “Nếu người dùng chọn thanh toán online, hệ thống chuyển sang màn hình OTP.”
Tester hỏi: “Trường hợp chọn online nhưng chưa nhập số điện thoại thì sao?”
👉 Bạn chợt nhận ra: quên nêu điều kiện tiền đề là phải có số điện thoại hợp lệ.
→ Cần bổ sung logic kiểm tra số trước khi chuyển OTP.
● Ghi nhớ: Diễn đạt sai = yêu cầu sai, dù ý đúng.

2. **Soát lại tính “test được” của yêu cầu**
📍 Gợi ý phản ứng đúng:
Giả sử mình là Tester – đọc tài liệu, bạn có thể viết test case ngay không?
📌 Ví dụ thực tế:
Yêu cầu ghi: “Nếu người dùng nhập sai định dạng email, hệ thống cảnh báo lỗi.”
Tester hỏi lại: “Sai định dạng là sao? Có check đuôi .com không? Có giới hạn ký tự đặc biệt không?”
👉 Lúc đó mới nhận ra: bạn chưa viết rõ quy tắc validate.
Tester không rõ test cái gì → DEV cũng không biết phải code theo logic nào.
■ Cần bổ sung:
- Định dạng hợp lệ
- Regex (nếu có)
- Mẫu lỗi hiển thị (text, màu, vị trí cảnh báo)
● Ghi nhớ: Tài liệu không test được → coi như chưa viết.

3. **Chuẩn hóa từ ngữ & định nghĩa rõ ràng**
📍 Gợi ý phản ứng đúng:
Nếu người đọc hiểu một thuật ngữ khác bạn →
không phải do họ ngây thơ, mà do bạn viết chưa đủ rõ.

📌 Ví dụ thực tế:
Yêu cầu ghi:
“Hệ thống cho phép nhân viên tạo yêu cầu ‘Tạm ứng’ nếu đã hoàn thành ‘Đào tạo bắt buộc’.”
Tester hỏi lại:
“‘Đào tạo bắt buộc’ là khoá nào? Onboarding hay training kỹ năng? Có mấy loại vậy?”
👉 Bạn chợt nhận ra:
trong hệ thống có 3 khoá đào tạo khác nhau,
nhưng bạn đang dùng cụm “đào tạo bắt buộc” mà không định nghĩa cụ thể.
■ Cần bổ sung:
- Danh sách cụ thể các khoá được coi là “bắt buộc”
- Mã code hoặc ID nếu có
- Điều kiện để được tính là “hoàn thành”
- Link đến bảng glossary / rule table nếu dài
● Ghi nhớ:
Một từ bạn nghĩ “ai cũng hiểu” – chính là chỗ dễ toang nhất.

✦ “Tester không phải người lười đọc – mà là người giúp bạn soi lỗi diễn đạt.”
Còn bạn là người quyết định xem lỗi đó được sửa... hay chờ ngày bung bét ở UAT.
Nếu từng rơi vào cảnh “ghi rõ rồi mà Tester vẫn hỏi lại” –
thì bạn đã biết cảm giác đó khó chịu và nguy hiểm thế nào.
Đừng để lỗi logic âm ỉ phá toang deadline –
học cách nhìn xa, nghĩ sâu, và chặn bug từ gốc trước cả khi vẽ flow.


---

## DAY 49/100 — KẸT GIỮA RỪNG XÀ NU KẾ TOÁN BA CÓ NÊN ĐI HỌC LUÔN KẾ TOÁN KHÔNG?

*Trang 113–115*

“Em đang làm dự án có tích hợp kế toán anh ạ, mà đọc tới chỗ kế toán em muốn nghỉ việc.
Một rừng thuật ngữ: Công nợ – Bút toán – Tài khoản cấp 1/2/3 – Hạch toán – Định khoản – đối ứng...”
● Em bắt đầu thấy mình kém cỏi, lú luôn với loạt thuật ngữ, muốn đi học khóa kế toán cho rồi
🧠 Nhưng với kinh nghiệm của một BA lâu năm, anh không chọn cách đi học kế toán như một kế toán.
Anh chọn cách hiểu kế toán vừa đủ để đặt câu hỏi đúng, thiết kế hệ thống không toang, và kết nối chuẩn logic với bên tài chính.

1. **Gom thuật ngữ kế toán thành nhóm chức năng – để hệ thống hóa rừng xà nu**
Thay vì học vẹt từng khái niệm kế toán, anh chọn cách gom lại theo chức năng nghiệp vụ – tức là gom theo việc hệ thống xử lý gì, không phải theo chương sách kế toán.
Vì sao phải gom?
→ Vì kế toán không vận hành kiểu "thuật ngữ đơn lẻ", mà theo nghiệp vụ thực tế gắn liền hệ thống: ghi nhận doanh thu, đối chiếu công nợ, sinh bút toán khi trả lương, lập báo cáo...Anh không cố nhớ “Tài khoản 111 là gì” – anh hỏi:
“Khi người dùng tạo phiếu thu, hệ thống ghi nhận gì – dữ liệu chạy qua đâu – sinh ra gì?”
● Anh thường chia thành 5 nhóm chức năng chính:
- Ghi nhận doanh thu – chi phí
- Quản lý công nợ
- Dòng tiền & thanh toán
- Liên kết phân hệ khác (bán hàng, lương, tài sản...)
- Cấu hình định khoản và mapping tài khoản
Hiểu được nhóm → trace được flow → biết hỏi đúng → thiết kế đúng logic, không sai.

🔍 Có cần định nghĩa từng thuật ngữ không?
→ Có. Nhưng theo kiểu BA, không theo kiểu kế toán viên.
Anh không cần biết cách định khoản chi tiết, anh chỉ cần hiểu:
- "Bút toán" là thứ DEV phải sinh đúng lúc.
- "Định khoản" là điều QC phải test đúng logic.
- "Công nợ" là dòng tiền phải được cập nhật chuẩn sau khi khách trả.
→ Vậy là đủ để sống sót rồi.
Hiểu để phân tích và thiết kế, không phải để lên bảng cân đối kế toán.

2. **Luôn nhớ 3 câu hỏi gốc rễ mà mọi hệ thống kế toán cần trả lời**
Trước khi viết đặc tả, trước khi vẽ flow, em phải trả lời được 3 câu hỏi sau:
❓ Tiền đi đâu?
→ Chi cho việc gì? Hệ thống ghi vào tài khoản nào? Có chia theo bộ phận, dự án không?
❓ Tiền đến từ đâu?
→ Từ khách nào? Đơn hàng nào? Có tự động trừ công nợ không? Phân biệt tiền mặt – chuyển khoản chứ?
❓ Ghi nhận đã đúng theo chuẩn kế toán chưa?
→ Có sinh đúng bút toán không? Có đủ thông tin reference không?
Có log ai sửa – sửa gì – lúc nào không?
💡 Trong kế toán, “tiền” là cách nói tắt – thực ra là giá trị tài sản/nợ/chi phí/doanh thu được ghi nhận.

3. **Không làm kế toán nhưng cần tư như kế toán**
Luôn làm rõ:
- Sự kiện nào sinh bút toán?
- Dữ liệu lấy từ đâu?
- Mapping tài khoản ai cấu hình?
- Trường hợp nào ngoại lệ?
- Có cần lock dữ liệu sau khi chốt sổ không?
❗ Đừng coi module kế toán là CRUD.
Nó là hệ thống có logic – có ràng buộc – có trách nhiệm pháp lý.

4. **Thuật ngữ sống còn – hiểu theo cách của BA**
Hạch toán = ghi nhận nghiệp vụ tài chính
Định khoản = chọn đúng tài khoản Nợ/Có
Tài khoản kế toán = mã đại diện cho tài sản/nợ phải trả
Công nợ = khoản phải thu hoặc phải trả
Bút toán = dòng ghi tài chính, có Nợ – Có – Số tiền – Mô tả – Ngày

**KẾT:**
Là BA, em không cần giỏi kế toán, nhưng phải hiểu hệ thống kế toán đang vận hành ra sao. Hiểu để không bị hỏi ngược. Hiểu để thiết kế đúng – trước khi lỗi hệ thống gọi tên em.


---

## DAY 50/100 — REVIEW SÁCH DÀNH CHO BA “UX FOR BEGINNERS”

*Trang 116–118*

**“UX là việc của designer chứ liên quan gì đến BA?”**
Câu hỏi mà mình từng nghĩ trong năm đầu làm BA. Cho đến khi:
- Flow mình phân tích khiến người dùng... không muốn dùng,
- UI team phải quay lại hỏi: “Ủa Phú muốn trải nghiệm gì ở bước này?”
Và mình nhận ra: Lỗi nằm ở mình – người viết requirement thiếu tư duy trải nghiệm.

● **Cuốn “UX for Beginners” có gì đáng đọc với BA?**
Tác giả Joel Marsh chia UX thành 100 bài học cực ngắn, mỗi bài chỉ 1–2 trang, nhưng “đấm thẳng” vào nhiều ngộ nhận phổ biến. Và quan trọng hơn: BA đọc là ứng dụng được ngay.

💡 **Bài học 1: UX ≠ Giao diện đẹp – UX = Giúp người dùng làm được việc**
Trích sách:
“The goal of a UX designer is to make users effective.”
(Lesson 1 – What is UX?)
● BA đừng dừng lại ở việc mô tả chức năng.
Phải hỏi: người dùng thực sự muốn làm gì?
Giao diện có đẹp mà không dùng được, thì vẫn là UX... tệ.
BA mà không nhận ra điều này, dễ toang từ lúc viết flow.

💡 **Bài học 2: 5 yếu tố tạo nên UX – BA thường chỉ làm 2**
Trích sách:
“UX = Psychology, Usability, Design, Copywriting, and Analysis.”
(Lesson 2 – The Five Main Ingredients of UX)
🧠 BA thường chăm phần logic + usability (tức “dùng được”), nhưng:
- Bỏ qua Copywriting: Nút bấm ghi gì? Form ghi thế nào để user không lo lắng?
- Bỏ quên đo lường:
  - Tính năng mình phân tích có hiệu quả không?
  - Bao nhiêu người dùng xong bước 3 thì out?
👉 Làm BA giỏi không chỉ là “viết hay”, mà phải hiểu rõ hành vi người dùng và đo được hiệu quả.

💡 **Bài học 3: Bạn biết quá nhiều – người dùng thì không**
Trích sách:
“You want things that don’t matter to users.
You know things that don’t matter to users.”
(Lesson 3 – Your Perspective)
🔍 BA hay mang kiến thức nội bộ áp lên user.
“Tôi biết danh mục này chia như thế là đúng”, nhưng người dùng không hiểu – và không quan tâm.

✦ Giải pháp:
- Bỏ tư duy “dễ với tôi là được”
- Test giả định của mình bằng cách cho người khác dùng thử flow trước khi duyệt UI

💡 **Bài học 4: UX là cả hành trình – đừng coi đó là 1 bước duyệt mockup**
Trích sách:
“A UX designer is not ‘the person who does the UX part’.
That’s like saying the water is just the wet part of your drink.”
(Lesson 8 – UX is a Process)
● BA mà tới giai đoạn UI mới nghĩ tới UX là... trễ.
Ngay từ lúc phân tích requirement, bạn đã là người “thiết kế trải nghiệm” rồi – dù không vẽ.
→ Viết flow có logic?
→ Có điều hướng rõ ràng?
→ Có xử lý lỗi hợp lý không?

💡 **Bài học 5: Requirement rõ ràng chưa chắc dùng được**
Trích sách:
“If the user doesn’t read the fine print, does it still work/make sense?”
(Lesson 2 – Usability checklist)
▲ BA hay lầm tưởng “ghi rõ rồi là xong”.
Nhưng người dùng không đọc hết đâu.
→ Viết mô tả kỹ chưa đủ – phải diễn giải bằng trải nghiệm.
Ví dụ:
- Hệ thống báo lỗi ngay khi nhập sai → tốt
- Báo lỗi ở bước cuối sau khi nhập 6 bước → toang

🧠 **Tư duy BA khi đọc sách này là gì? Đọc không phải để làm designer.**
Mà để:
- Viết flow mượt mà, tối ưu thao tác người dùng.
- Biết đặt câu hỏi cho UI/UX team đúng chỗ.
- Biết feedback UI không phải “cho đẹp lên” mà là “cho dùng được”.

📥 Muốn bản ebook để lại email dưới comment nha.


---

## DAY 51/100 — TÍNH NĂNG “LÀM TẠM THÔI” NHƯNG SỐNG DAI, CHẾT ĐAU, NẾU BA KHÔNG ĐỂ LẠI DẤU VẾT

*Trang 119–120*

Nhiều tính năng bắt đầu bằng một câu rất quen:
- “Làm nhanh để kịp demo chiều nay nhé.”
- “Tạm thời thêm tính năng gửi mail, mai chạy campaign.”
Không họp phân tích. Không đặc tả. Không gì cả – ngoài một task gắn tên bạn với deadline: ngay hôm nay!!!

Có những lúc team buộc phải đi “đường tắt” – để test insight, để show investor, để MKT kịp chiến dịch. Tính năng chưa được họp phân tích, chưa chốt requirement, chưa có use case – nhưng vẫn phải làm.
Là BA, bạn không thể nói “đợi em phân tích đã”. Nhưng cũng không thể làm kiểu “giao gì làm nấy” mà không để lại dấu vết.

💡 **Sự khác biệt giữa BA non và BA cứng**
Không nằm ở việc viết SRS,
→ Mà ở chỗ kiểm soát rủi ro khi mọi thứ chưa rõ ràng.
Trong tình huống kiểu "làm gấp – chưa kịp đánh giá", một BA cứng sẽ hành xử như sau:
✔ OK, không cần đặc tả chính thức – nhưng vẫn viết tài liệu kiểm soát, để cả team có chung một hiểu biết tạm thời.
✔ OK, không có flow chi tiết – nhưng vẫn mô tả hành vi xử lý, để QC còn biết test cái gì, DEV không phải đoán.
✔ OK, làm gấp – nhưng vẫn để lại dấu vết:
- Ai giao,
- Giao lúc nào,
- Mục đích là gì,
- Sẽ gỡ khi nào,
- Có ảnh hưởng tới flow nào không?
👉 Vì nếu không làm vậy, bạn tưởng là xong – nhưng rắc rối chỉ mới bắt đầu.

● **Khi hệ thống xảy ra sự cố, người ta sẽ tìm đến bạn – để hỏi:**
- “Chức năng này từ đâu ra?”
- “Ai chốt logic?”
- “Có ai review chưa?”
Nếu bạn không để lại bất kỳ thông tin nào,
→ Bạn không chỉ mất quyền giải thích,
→ Mà còn mất cả uy tín kiểm soát – thứ mà một BA sống còn nhờ nó.

💡 **3 điều BA cần làm khi đối mặt với “tính năng tạm thời”:**
1. **Ghi rõ mục đích và ngữ cảnh**
- “Chức năng này dùng để thử nghiệm hành vi người dùng với mục tiêu [XYZ].
- Không phải chức năng chính thức.
- Có thể gỡ sau [3 tuần / campaign kết thúc].”
2. **Mô tả hành vi hệ thống đơn giản nhưng rõ**
- Ai thao tác?
- Nhập gì?
- Hệ thống phản hồi gì?
- Có xử lý gì đặc biệt?

3. **Cảnh báo rủi ro**
“Nếu muốn giữ lại tính năng này trong hệ thống chính thức, cần đánh giá lại và viết UC chuẩn trước khi go-live.”

🧠 Thành công của BA không nằm ở việc từ chối làm nhanh. Nó nằm ở chỗ: Vẫn làm – nhưng làm có kiểm soát. Vì bạn không thể chọn lúc nào dự án ổn định. Nhưng bạn có thể chọn cách mình phản ứng – khi nó bất ổn. Làm tạm không có nghĩa là làm mù.
Tạm thời – vẫn cần được viết ra một cách có trách nhiệm.


---

## DAY 52/100 — LÀM SAAS MÀ KHÁCH NÀO CŨNG ĐÒI "LÀM THEO CÁCH NHÀ ANH"?

*Trang 121–123*

🍻 **Mở đầu từ quán bia hơi Hà Nội:**
Bạn làm phần mềm SaaS cho chuỗi quán bia.
Hệ thống core đã có: Gọi món – quản lý bàn – in bếp – tính tiền – báo cáo doanh thu.
Rồi một quán yêu cầu:
“Bên chị bán cả bia lon, bia chai, tháp bia – muốn tính điểm thưởng riêng cho từng loại, tặng thẻ tích điểm theo từng bàn.”
Quán khác yêu cầu:
“Bên chị cần gợi ý món theo lịch sử từng khách quen.”
Một bên nữa lại đề nghị:
“Cần báo cáo riêng theo tổ phục vụ, chia theo ca – logic không giống báo cáo mặc định.”

Nghe thì tưởng nhỏ – nhưng nếu bạn gật hết:
👉 SaaS của bạn không còn là sản phẩm để scale, mà là sân sau của từng khách hàng.
❗ **Vấn đề không nằm ở từng yêu cầu – mà ở chỗ BA không có khung tư duy để phân loại, dẫn hướng và ra quyết định.**

■ **Một BA thực sự giỏi khi làm SaaS cần tư duy ở 3 tầng:**
1. **Tầng sản phẩm – Phục vụ ai, và trong phạm vi nào?**
- Bạn phải dám trả lời: hệ thống này sinh ra để phục vụ loại hình khách hàng nào? Quán nhỏ? Chuỗi? Tập đoàn lớn?
- Giới hạn trải nghiệm đến đâu thì dừng lại?
- Cho phép khách tự cấu hình combo? → Có thể.
- Tự sinh logic chia tua, tính KPI theo tổ? → Không.
Nếu BA không xác định được giới hạn sản phẩm – hệ thống sẽ thành một nồi lẩu custom không ai còn kiểm soát nổi.

2. **Tầng kiến trúc – Cái gì đưa vào lõi hệ thống, cái gì tách mô-đun, cái gì loại bỏ?**
- Tính năng phổ biến, ai cũng cần → đưa vào core.
- Tính năng nhiều khách lớn yêu cầu → tách mô-đun, tính phí nếu cần.
- Tính năng chỉ 1 khách cần, logic riêng biệt, phá vỡ cấu trúc → loại bỏ.
BA không phải người hỏi “dev có làm được không?”
Mà là người dám nói:
“Nếu làm cái này, 3 sprint tới sẽ chỉ chạy regression.”

3. **Tầng vận hành – Giữ hệ thống sạch nhưng vẫn linh hoạt cấu hình**
- Linh hoạt không có nghĩa là chiều.
- Linh hoạt là: thiết kế được vùng cấu hình an toàn – không phá vỡ logic gốc.
Cụ thể:
- Luồng nghiệp vụ dùng chung → quy tắc hệ thống
- Những gì khách tự cấu hình được: như bật/tắt tính năng theo gói (cờ chức năng), tự cấu hình menu, tạo combo linh hoạt
- Những gì “khách đòi riêng” mà đụng sâu vào core → đẩy về gói Enterprise, có chi phí và cam kết bảo trì

🧠 **Khi nhận một yêu cầu “tuỳ chỉnh riêng”, BA cần xử lý như thế nào?**
1. Xác định khách thuộc nhóm nào – phổ thông hay enterprise? → Điều này quyết định mức độ ưu tiên xử lý.
2. Đánh giá: yêu cầu này là độc quyền hay là mẫu số chung? → Nếu nhiều khách cùng hỏi, có thể nên đưa vào roadmap.
3. Hỏi ngược lại:
- “Yêu cầu này có thể giải quyết bằng cấu hình không?”
- Nếu xử lý được bằng feature flag, menu builder, combo creator – đừng đụng codebase.
4. Đánh giá rủi ro kỹ thuật:
- Yêu cầu này có phá vỡ logic hệ thống không?
- Nếu có, cần dừng hoặc tách riêng thành module.
5. Tư vấn lại cho khách:
- “Cái này mình có thể làm dưới dạng addon/gói riêng – bên em gửi proposal nhé.”
- Giữ được kiến trúc sạch, lại mở thêm dòng doanh thu.

💡 **Và để hệ thống tồn tại lâu dài – bạn cần thêm 4 chiến lược xử lý:**
1. **Thiết kế kiến trúc cho phép cấu hình (Configuration thay vì Customization)**
Áp dụng:
- Trường dữ liệu linh hoạt (Dynamic Field)
- Cờ chức năng (Feature Flag)
- Phân quyền linh hoạt (Role/Permission)
→ Vừa tạo cảm giác “được tuỳ chỉnh”, vừa giữ được lõi code chung.

2. **Xác định rõ ranh giới "tuỳ chỉnh được – và không"**
Soạn một SaaS Customization Policy gồm 3 nhóm:
■ Những gì có thể cấu hình
▲ Những gì có thể cân nhắc
✖ Những gì không hỗ trợ
→ Giảm thời gian đàm phán – tránh kỳ vọng sai từ khách hàng và sales.

3. **Dùng chiến lược phân tầng sản phẩm (Product Tiering)**
- Khách hàng phổ thông dùng core
- Khách hàng enterprise muốn tuỳ chỉnh → nâng cấp lên gói riêng hoặc triển khai private instance
→ Có ngân sách để làm đúng – không phá hệ thống

4. **Nhận diện yêu cầu lặp lại để mở rộng sản phẩm**
- Một khách đòi báo cáo chia vùng = ý kiến cá nhân
- Năm khách cùng đòi = tín hiệu thị trường
→ Cập nhật roadmap


---

## DAY 53/100 — NẾU BẠN CỨ HỎI “TÍNH NĂNG NÀY CÓ CẦN KHÔNG?” – THÌ MẸ BẠN CŨNG SẼ GẬT ĐẦU

*Trang 124–126*

Bạn vừa họp xong với khách hàng. Hỏi nhanh: “Nếu có bộ lọc thời gian thì tiện hơn không anh?”
Khách gật đầu: “Tiện quá em. Làm luôn đi.”
Bạn note lại, đưa vào backlog. DEV build, QC test, PM báo done. Sản phẩm ra mắt không ai dùng. Tính năng gần như mất tích. Không lỗi. Không bug. Nhưng không có nhu cầu.

💬 **Lý do?**
Bạn hỏi sai. Nhưng tưởng mình hỏi đúng.
Bạn hỏi xem họ “muốn gì” – chứ không hỏi họ “đã từng làm gì”.
Bạn hỏi về “tương lai” – chứ không kiểm tra “quá khứ”.
Bạn hỏi một cách khiến... đến mẹ bạn cũng sẽ không dám chê.

📘 **Đó là lý do cuốn sách The Mom Test ra đời**
The Mom Test là một quy tắc đơn giản: Nếu bạn hỏi mẹ mình về ý tưởng sản phẩm – và bà ấy cũng không thể chê được – thì bạn đã hỏi sai.
Vì người ta lịch sự. Người ta yêu quý bạn. Người ta muốn nói điều tử tế. Nhưng điều tử tế không phải là insight. Cuốn sách này chỉ bạn cách đặt câu hỏi để tìm ra sự thật, ngay cả khi người đối diện không muốn làm bạn buồn.

🖊️ **Mọi người xây sản phẩm bằng... lời khen**
“Ý tưởng em hay đấy!”
“Tính năng này cần thiết mà.”
“Cái này chắc chắn người dùng thích.”
Nghe quen không?
Toàn là lời hoa mỹ. Nhưng toàn là... vàng giả.
“Compliments are the fool’s gold of customer learning.”
Lời khen là vàng giả trong việc học từ khách hàng.

■ Thay vào đó, bạn cần 3 nguyên tắc hỏi của The Mom Test:
- Hỏi về chuyện đã xảy ra → “Gần đây anh có từng lọc danh sách theo thời gian không?”
- Hỏi về cách họ tự xử lý vấn đề → “Anh thường lọc bằng cách nào? Có file riêng không?”
- Không dẫn dắt, không giải thích tính năng của bạn → Bạn đang nghe, không phải bán hàng.

“You aren’t allowed to tell them what their problem is, and in return, they aren’t allowed to tell you what to build.”
Bạn không được gợi ý vấn đề của họ – và họ cũng không được bảo bạn nên build gì.

🔍 **Một ví dụ thật mà tôi từng gặp**
Hệ thống nội bộ. Stakeholder bảo: “Phải có bộ lọc theo thời gian thì mới dễ dùng.”
Tôi hỏi lại theo kiểu The Mom Test:
- “Lần gần nhất anh cần lọc là khi nào?”
- “Nếu không lọc được, anh xử lý thế nào?”
- “Sai sót từ việc lọc nhầm có gây hậu quả gì không?”

👉 Và phát hiện ra:
- Một năm họ lọc đúng 1 lần – vào kỳ tổng kết
- Còn lại họ mở file Excel
- Không ai gặp lỗi gì nghiêm trọng

→ Thay vì build bộ lọc UI to đùng, tôi đề xuất để trong export. Nhẹ hơn, nhanh hơn, đúng nhu cầu.

💬 **BA/PO hỏi đúng xong thì làm gì?**
Câu trả lời: **Không phải ghi lại là xong.**
Bạn cần truy ra 3 thứ để biết sản phẩm mình có đúng market-fit không:
1. Có nỗi đau thật không?
- Nếu họ chưa từng tự tìm cách giải quyết,
- Họ cũng chẳng mua tool bạn làm.
2. Nỗi đau đó đủ lớn để họ thay đổi thói quen không?
- Nếu không, họ sẽ vẫn làm kiểu cũ – và bạn chỉ build cho vui.
3. Giải pháp của bạn có “đáng tiền” với họ không?
- Nếu có, họ sẽ hào hứng.
- Nếu không, họ sẽ im lặng sau buổi demo.

🧩 Hỏi đúng = tiết kiệm cả team 3 tháng phát triển vô nghĩa
Bạn không cần học:
- “kỹ thuật hỏi sâu”,
- “tư duy chiến lược”,
- “sát thương tâm lý”.

Bạn chỉ cần:
■ Dừng việc hỏi “Tính năng này có cần không?”
■ Bắt đầu hỏi “Anh từng gặp chuyện đó bao giờ chưa?”
■ Và nhìn xem:
Họ thật sự xử lý ra sao, chứ không phải họ tưởng tượng ra sao.


---

## DAY 54/100 — LÀM QUẢN LÝ KHÔNG PHẢI LÀM SẾP MÀ LÀ ĐỔI GÓC NHÌN

*Trang 127–128*

Sau 1 năm ở vai trò quản lý, tôi hiểu:
Làm sếp là một danh xưng
Làm quản lý là một hành trình đổi cách nhìn người, nhìn việc và nhìn chính mình.
Ngày trước, tôi nghĩ: “LÀM SẾP là ra quyết định và dẫn dắt team”
Họp hành, phân công, duyệt task, đưa ra chỉ đạo...

Tôi nghĩ vậy là đúng vai. Nhưng dần dần tôi nhận ra: Team không cần một người chỉ tay. Team cần một người hiểu và hỗ trợ.
📌 Làm quản lý = Đổi góc nhìn
- Trước kia, tôi chỉ cần làm tốt việc của mình
- Giờ đây, tôi phải làm sao để nhiều người cùng làm tốt

Không còn là người giỏi nhất team – mà là người giúp team ngày càng giỏi
Tôi bắt đầu học cách:
- ■ Đặt câu hỏi thay vì chỉ đạo
- 👀 Quan sát thay vì xen vào
- 💪 Hỗ trợ thay vì làm thay

**3 điều tôi học được sau 1 năm làm quản lý**
💬 **1 – Giúp người khác làm tốt, chứ không phải làm thay**
- Bạn càng làm thay, team càng chậm trưởng thành
- Bạn càng kiên nhẫn hỗ trợ, team càng chủ động về sau

Tư duy cá nhân hóa thì làm được việc.
Tư duy nhân bản hóa thì xây được đội.

💬 **2 – Uy tín đến từ hành động nhất quán**
Không cần nói nhiều. Chỉ cần:
- Nói gì làm nấy
- Làm gương trước khi nhắc người khác
- Dám nhận lỗi, dám sửa sai

Được gọi là “lead” là một điều may mắn.
Được tin tưởng là một điều bạn phải vun đắp từng ngày.

📘 **3 – Không phải làm ít việc hơn, mà là thấy nhiều thứ hơn**
Bạn sẽ là người:
- 🤝 Kết nối team với team
- ⚡ Xử lý các xung đột thầm lặng
- 🧭 Suy nghĩ xa hơn: về năng lực đội ngũ, về định hướng lâu dài – không chỉ là task hiện tại

Làm quản lý là học cách “thấy nhiều hơn” – và “nâng người khác lên cùng mình”.

■ Nếu chỉ nhớ 1 điều sau bài này:
Làm quản lý không phải “lên sếp” – mà là “lùi lại đúng lúc để người khác bước lên”.
Là đổi từ tư duy “mình làm tốt” → thành “cả đội cùng tốt”.


---

## DAY 55/100 — “DEADLINE GẤP LẮM” NHƯNG CHƯA CHẮC ĐÃ CẦN BA GẤP

*Trang 129–130*

Nghe chữ “gấp”, BA non tay sẽ lao vào làm ngay. BA cứng thì tỉnh lại, nhìn bản đồ dự án, rồi mới ra tay. Sếp nhắn: “Em ơi gấp lắm. Làm tài liệu giúp anh ngay nhé.”
BA mở máy, viết. Gõ xong spec, dựng flow, gửi bản vẽ wireframe. Rồi...
- 1 tuần sau, DEV chưa làm.
- 2 tuần sau, đổi logic.
- 3 tuần sau, spec bạn viết bị bỏ.

Bạn thấy mình có tâm, còn hệ thống thì đổ sông đổ biển. Vấn đề không nằm ở bạn làm chậm hay nhanh, mà là bạn làm khi chưa tới lượt. Một BA cứng sẽ chọn:
◆ **Không làm ngay, nếu chưa có quyết định rõ.**
Tính năng “tặng điểm thưởng” mà:
- Chưa biết tặng ai
- Dùng ở đâu
- Reset thế nào?

→ BA cứng sẽ dừng lại 30 phút hỏi gốc rễ, thay vì viết liều 3 ngày rồi sửa cả tuần.
◆ **Không làm hết, nếu team mới cần một phần.**
- DEV BE đang cần API khởi tạo đơn hàng → Viết đúng phần đó trước
- UI chưa rõ → Để sau

Làm vừa đủ để hệ thống tiến, không ôm hết rồi chết giữa chừng.
◆ **Không làm cho có, nếu không ai cam kết sẽ dùng**
Sếp nói: “Viết trước cho chắc” – nhưng khách chưa duyệt ngân sách?
→ BA cứng đề xuất bản draft sơ bộ, Và chốt thẳng: “Khi nào có quyết định chính thức, em hoàn thiện tiếp.”

**Senior BA làm gì?**
■ Họ không phản ứng theo cảm xúc. Mà phân loại tình huống:
- Gấp vì đang chờ BA → Vào ngay
- Gấp vì sếp sốt ruột → Giải thích lại luồng
- Gấp nhưng chưa tới lượt → Dẫn lại tiến trình

■ **Họ chia timeline thành điểm rơi logic:**
- DEV cần gì đầu tiên?
- Phần nào có thể làm trước mà không bị toang nếu thay đổi?
- Ai sẽ dùng đầu ra của tôi – và vào lúc nào?

Từ đó, họ chọn cách ra tay đúng lúc – đúng điểm chạm.
“Gấp không phải là lúc để BA làm.
Gấp là lúc để BA tỉnh.”

**Muốn trưởng thành**
BA phải thoát khỏi phản xạ “nghe gấp là làm”.
Mà phải học cách nhìn dòng chảy hệ thống và đặt câu hỏi:
- “Nếu tôi làm bây giờ – ai dùng?
- Khi nào dùng?
- Có chắc sẽ dùng không?”

**Nếu không có câu trả lời rõ ràng,**
→ Lùi lại một nhịp.
→ Dẫn nhịp cho team.
→ Và xuất hiện đúng lúc – như một mắt xích không thể thiếu.


---

## DAY 56/100 — “SẾP ƠI, EM MỆT RỒI”

*Trang 131–132*

4h50 chiều, thứ Sáu. Tin nhắn hiện lên trên màn hình: “Sếp ơi, em mệt rồi. Em thấy mình không còn vui khi làm việc nữa.”
Tôi ngồi nhìn dòng đó. Không gõ trả lời. Không phản xạ gì. Chỉ thấy một cảm giác hơi trống, như vừa để rơi mất một thứ gì đó mà chính mình làm vỡ. Người gửi tin nhắn đó là 1 BA cứng team tôi. Bạn ấy không bao giờ than.
- Lúc người khác trễ deadline, bạn ấy làm thay.
- Lúc cả team căng, bạn ấy vẫn cười và bảo: “Để em xử lý.”

Tôi từng nghĩ: “Bạn này ổn mà. Giỏi như thế, chắc làm nhanh thôi.”
Nhưng tôi quên mất một điều: Người làm được việc nhất thường là người dễ bị lạm dụng vô thức nhất. Và sự mệt mỏi không bao giờ đến đột ngột.
- 3 tháng trước: bạn nhận thêm việc người khác bỏ lại.
- 2 tháng trước: nghỉ phép vẫn bị gọi xử lý “gấp”.
- 1 tháng trước: bạn đề xuất cải tiến – tôi từ chối với một câu: “Giờ chưa phải lúc, tập trung làm xong cái đang chạy đi.”

Mỗi lần như thế, tôi nghĩ bạn ấy sẽ hiểu. Mỗi lần như thế, tôi tự nhủ bạn ấy chịu được.

Đến khi bạn nói “Em mệt rồi”, tôi mới hiểu: Không phải vì việc quá nhiều. Mà vì bạn không còn thấy mình có ý nghĩa gì trong team nữa.

Tôi không trả lời tin nhắn. Tôi hẹn bạn... đi cà phê. Không phải để hỏi:
“Mệt vì task nào?”
Mà để tạo một không gian –Nơi bạn ấy không cần gồng nữa.

💬 **Buổi cà phê hôm đó không có slide, không có KPI.**
Chỉ có tôi, bạn ấy, và một câu hỏi rất chậm: “Nếu có quyền chọn lại, em có còn muốn ở lại team mình không?” Và nếu câu trả lời là “không”, thì vì điều gì?
Bạn không trả lời ngay. Chỉ nhìn ra cửa kính một lúc rồi nói:
- “Sếp có nhớ lần em nhận 2 task không ai làm không?
- Có lần em nghỉ phép vẫn nhận điện thoại?
- Có lần em viết tài liệu góp ý, nhưng bị cắt ngang là ‘thừa’?
Lúc đó em không trách gì. Nhưng em bắt đầu nghĩ: Chắc mình... chỉ là cái máy làm việc.”

Tôi nghe – không phản biện. Không giải thích. Không bào chữa. Vì tôi biết:
Một người đang mất lửa, không cần được “thuyết phục”. Họ cần được “thấy mình vẫn có giá trị.”

**Và sau buổi đó, tôi đã làm 3 việc:**
**1. Tôi gỡ điểm thắt.**
- Ngay chiều hôm đó, tôi rút lại phần việc đang overload của bạn.
- Giao lại cho người khác, dù biết sẽ chậm hơn.

Tôi nhắn riêng: “Tạm thời em chỉ làm 1 task. Anh không cần em chứng minh gì nữa cả. Chỉ cần em thấy vui trở lại khi làm việc.”

**2. Tôi công khai lại luật chơi trong team.**
Tôi gọi cả team vào họp, nói rõ ràng: “Từ nay, ai làm nhanh – không có nghĩa sẽ làm nhiều. Giao task sẽ theo 3 yếu tố: Kỹ năng – Năng lượng – và Sự công bằng.”
Tôi biết có người không thích. Nhưng tôi cũng biết: Một team bền không được xây bằng sự hi sinh âm thầm của người giỏi.

**3. Tôi thiết kế lại cách chia việc – theo biểu đồ năng lượng.**
Tôi chia task không chỉ theo skill, Mà còn theo trạng thái tâm lý: Tôi bắt đầu quan sát kỹ hơn từng người:
- Ai đang máu lửa: giao task mới, nhiều ownership → Cho họ cảm giác chinh phục.
- Ai đang ổn định: giữ nhịp vận hành → Để team không gãy.
- Ai đang cạn lửa: cho reset → Không phải nghỉ ngơi, mà là nạp lại ý nghĩa công việc.

Tôi không chia task theo “ai thích gì”, Mà chia theo sức kéo thực tế như một đội đạp xe:
- Người khoẻ kéo đầu.
- Người hụt hơi núp gió một đoạn.
- Nhưng tất cả cùng đạp – và về đích cùng nhau.

Đó không phải chiều cảm xúc. Đó là quản trị nhịp độ.
📌 “Em mệt rồi” – không phải một câu than. Mà là một cú chạm cuối cùng – nếu bạn còn muốn cứu. Người ta không rời đi vì lương thấp hay task nặng. Người ta rời đi khi thấy...
Mình chẳng còn được nhìn thấy.


---

## DAY 57/100 — PHỎNG VẤN BA MID & SENIOR ĐỪNG KỂ BẠN TỪNG LÀM GÌ. HÃY CHỨNG MINH: BẠN TƯ DUY ĐƯỢC TỚI ĐÂU.

*Trang 133–136*

“Cùng 4-5 năm kinh nghiệm, có người là senior, có người mãi là mid. Khác biệt không nằm ở độ dài CV. Mà nằm ở chiều sâu phản xạ trong từng câu trả lời.”

💬 **Lưu ý: Bài viết là quan điểm tổng hợp từ góc nhìn người tuyển dụng thực chiến trong ngành. Không đại diện cho tất cả nhà tuyển dụng – hãy tham khảo có chọn lọc, không áp đặt như khuôn mẫu cứng nhắc.**

👀 **Nhà tuyển dụng đánh giá BA Mid như thế nào?**
Không phỏng vấn để nghe ứng viên kể:
✖ “Em từng làm hệ thống ABC...”
Mà để xác định:
■ Ứng viên đang dừng ở mức hoàn thành đầu việc
hay
■ Đã tư duy như người giữ logic và dòng chảy hệ thống?

💬 **1. Quan sát phản xạ khi bị vặn ngược yêu cầu**
Câu hỏi duy nhất: “Nếu user thao tác sai liên tục 5 lần – hệ thống nên phản ứng thế nào để tránh bị lạm dụng?”
- Junior: “Hệ thống báo lỗi.”
- BA có tư duy hệ thống:
  - Theo dõi số lần nhập sai
  - Cảnh báo cấp độ sau lần 3, khóa tạm sau lần 5
  - Phân biệt sai vô tình vs cố ý (abuse)
  - Ghi log truy vết hành vi bất thường
  - Tránh làm khó người dùng thật

→ Chỉ với một câu hỏi tưởng đơn giản, đã phân loại được tư duy tầng giao diện vs tầng hệ thống.

🧩 **2. Gài bẫy bằng yêu cầu không rõ ràng**
Câu hỏi: “Khách yêu cầu thêm nút Tạm hoãn ở màn phê duyệt. Viết UC kiểu gì?”
- Junior: viết luôn.
- Mid thực thụ: hỏi lại 👇
  - “Phê duyệt có deadline không?”
  - “Tạm hoãn thì giữ trạng thái ở đâu?”
  - “Logic business cho ‘tạm hoãn’ là gì?”
- Không hỏi gì → chưa đạt
- Hỏi nhầm → chưa đủ tư duy
- Hỏi đúng → đủ tiềm năng mở form offer

📓 **3. Quan sát sổ ghi chép và cách noted logic**
Ứng viên không giỏi ăn nói – vẫn có thể là BA tốt nếu:
- Sổ ghi chú rõ từng case, flow, logic, issue, risk
- Có phân loại, gom nhóm, dự đoán nguy cơ

→ Có tư duy phòng lỗi. Không để dự án toang vì “lơ mơ”.

● **4. Quan sát cấu trúc trả lời**
BA Mid thực thụ: Context → Problem → Impact → Option → Decision
- Không vòng vo
- Không “dạ vâng”, né tránh, giấu dốt
- Có lúc dừng lại 2 giây... rồi trả lời gọn – chính xác

→ Người đó đang kiểm soát được tư duy của chính mình.

⚖️ **5. Quan sát sự chủ động khi bị dồn**
Mid đúng nghĩa là người:
- Khi không biết → hỏi lại
- Khi bị ép → phân tích rủi ro
- Khi mơ hồ → dựng lại sơ đồ
- Không đợi giao mới làm
- Không né khi sai

→ Không để dự án chết vì câu: “Em tưởng thế là đúng.”

🔥 **Với BA Senior – Cách phỏng vấn hoàn toàn khác**
Senior là người:
- Giữ được logic khi cả team bắt đầu mất bình tĩnh
- Cân được politics
- Bảo vệ chất lượng sản phẩm khi khách đổi ý, dev lật mặt, sếp thiếu hiểu

💣 **1. Ép thời gian – test phản ứng**
Câu hỏi:
“Khách yêu cầu thêm 3 chức năng trong 1 tuần. Sếp bảo cứ viết tài liệu đi, chưa rõ nhưng làm trước. Xử lý sao?”
- Ứng viên thường: “Em làm bản nháp... hỏi thêm...”
- Senior:
  - Ưu tiên làm outline
  - Ghi rõ phần pending
  - Cảnh báo effort nếu sai → 3 ngày
  - Không fake sự chắc chắn
  - Trình bày sự mơ hồ = đẳng cấp

🥊 **2. Vặn case mâu thuẫn – test game nội bộ**
Case: “DEV bảo KH đổi scope. KH bảo BA viết sai. TEST thì không test được vì flow chưa rõ. Làm gì?”
- Ứng viên non: “Họp 3 bên, ghi nhận...”
- Senior:
  - Dựng lại toàn bộ data flow
  - Check bản release – mapping commit
  - Trích dẫn UC, yêu cầu, timestamp
  - Lập văn bản “logic đã thống nhất”

→ Bảo vệ logic – giữ team không tan.

📘 **3. Thử leadership style**
Tình huống:
“Team junior đi sai hướng, hiểu sai requirement. Làm gì?”
- Junior: “Em góp ý nhẹ nhàng...”
- Senior:

Senior:
- Không sửa giúp ngay
- Cho trace lại flow
- Hướng dẫn viết lại
- Note lại điểm sai
- Sửa mindset – không chỉ sửa task

■ **Một BA Mid/Senior cần chứng minh:**
- Hiểu mình đang làm gì trong tổng thể hệ thống
- Không nhầm giữa “làm việc chăm chỉ” và “làm việc đúng”
- Có tư duy kiểm lỗi từ đầu – không đợi fail
- Có khả năng chịu trách nhiệm khi mọi thứ lệch hướng
- Dám nói “Không nên làm vậy” khi cả team đang hưng phấn mà sai hướng

● **Chúc bạn bước vào phỏng vấn với:**
- Tư duy rõ ràng
- Phản xạ tỉnh táo
- Và đủ bản lĩnh để nói:
“Tôi không chỉ làm đúng – tôi giữ được hệ thống không gãy.”

■ Gặp nhau ở vòng offer nhé.
Nếu bạn thấy bài viết hữu ích – đừng quên để lại bình luận hoặc chia sẻ cho người đang chuẩn bị phỏng vấn.


---

## DAY 58/100 — CÁCH XÂY DỰNG KHUNG NĂNG LỰC VÀ ĐÁNH GIÁ LEVEL TEAM BA

*Trang 137–139*

Trước khi đăng bài này, tôi đã sửa – rồi xoá – rồi viết lại... không dưới 5 lần.
Vì đây là chủ đề dễ chạm tới nhiều bạn đang là BA, và cũng ảnh hưởng đến cách các BA Lead – Manager – HR đánh giá và phân cấp đội ngũ.
Bài viết không nhằm dạy ai – mà chia sẻ một góc nhìn thực chiến, từng bước một – khi tiếp quản lại một team BA cũ, giữa nhiều mâu thuẫn ngầm, nhãn mác cũ – và kỳ vọng mới.
Nếu bạn đang trên hành trình đó – hy vọng những chia sẻ này sẽ giúp bạn đỡ đơn độc hơn một chút.

✖ **Khi tiếp quản lại một team BA – đừng vội "gắn nhãn"**
Cách dễ nhất nhưng cũng dễ “phản tác dụng” nhất:
- Lập bảng competency, chấm điểm từng người từ 1–5
- Rồi đối chiếu với BABOK, gọi đó là Junior, Mid, Senior.

Nghe thì hợp lý. Nhưng:
- Người cũ thấy mình đang bị “xét lại hồ sơ”
- Người mới không hiểu đang bị đánh giá vì tiêu chí gì
- Cả team rơi vào trạng thái tự vệ ngầm: làm nhưng không mở lòng, hợp tác kiểu “chống trôi”

■ **Cách đúng hơn – và đủ tinh tế:**
Không vội đánh giá → mà dẫn dắt team tự soi lại chính mình.
◆ Bước 1: Quan sát – không ghi điểm 3 tuần đầu tiên, bạn đừng lập bảng chấm điểm hay bảng phân cấp. Hãy chỉ tập trung vào 3 hoạt động:
- Dự đủ các buổi họp transfer, họp yêu cầu với DEV, QC, stakeholder
- Đọc lại các tài liệu Use Case, SRS, BRD cũ
- Ghi chú những tình huống phản xạ nghiệp vụ thực tế

Hãy quan sát:
- Ai có thói quen hỏi lại khi yêu cầu chưa rõ?
- Ai trace logic từ màn hình → API → DB mà không bị đứt đoạn?
- Ai nhạy bén với lỗi logic trước cả DEV?
- Ai giải thích lại cho DEV hiểu – mà vẫn giữ được không khí hợp tác?

👉 Mục tiêu không phải là để phán xét.
Mà là để nhận diện từng mảnh năng lực tiềm ẩn – trước khi cùng họ phát triển.

◆ **Bước 2: Gợi mở – không xếp loại**
Đừng dùng từ “đánh giá” hay “xếp hạng”. Bạn hãy tạo một buổi sharing nhẹ nhàng:
"Mỗi người chia sẻ một project mình thấy tự tin nhất. Làm gì? Gặp gì? Giải ra sao?"
Sau mỗi phần trình bày, hãy hỏi: “Trong phần đó, kỹ năng nào là thứ quyết định để xử lý được tình huống?” Không cần Junior hay Senior gì cả. Chính họ sẽ tự thấy – mình đang mạnh ở đâu – yếu ở đâu – cần phát triển gì.

◆ **Bước 3: Dẫn dắt phát triển cá nhân – không bảng điểm**
Sau sharing, hãy hẹn từng người 1–1 và hỏi 3 câu:
1. Em thấy mình mạnh nhất ở nhóm kỹ năng nào?
2. Có phần nào em muốn thử nhưng chưa từng được giao không?
3. Có nhóm nào thấy yếu mà không biết bắt đầu từ đâu?

Từ đó, xây một plan đơn giản:
- Giao một project thử sức – đúng tầm
- Có buddy nếu cần
- Giao KPI tháng đầu, review lại vào tháng sau

→ Mỗi người có lộ trình riêng. Không ai bị so sánh. Nhưng vẫn có chỉ dấu để phát triển rõ ràng.

● **Phân cấp Junior – Mid – Senior thế nào?**
Không dùng cảm tính. Bạn hãy dùng hành vi thực tế, có dẫn chứng. Ví dụ:
- Ai từng trace Exception Flow và được DEV áp dụng luôn?
- Ai từng dẫn dắt buổi họp yêu cầu với stakeholder khó tính?
- Ai từng phát hiện bug logic trước cả DEV?
- Ai từng giúp người khác trace nghiệp vụ?

Checklist hành vi này chia thành 6 nhóm năng lực:
- Giao tiếp & Elicitation
- Viết & trace yêu cầu
- Thiết kế logic & wireframe
- Quản lý vòng đời yêu cầu
- Phân tích chiến lược & stakeholder
- Đánh giá giải pháp

→ Với mỗi nhóm, tôi mô tả rõ hành vi & ví dụ cụ thể.

Ví dụ:
Senior – Communication:
- Từng dẫn 3 buổi họp với stakeholder khó trong 2 quý gần nhất
- Có feedback tốt từ stakeholder về khả năng dẫn dắt

→ Không có flow mẫu? → chưa Mid
→ Chưa từng hỏi khách đúng trọng tâm? → Junior ở nhóm giao tiếp
→ Có kỹ năng Senior nhưng không chia sẻ lại cho team? → Chưa là Senior toàn diện

💬 **Kết quả thực tế sau 3 tháng:**
- Bạn Junior từng im lặng trong họp → nay xử lý trọn vẹn 1 module nghiệp vụ
- Bạn Mid từng viết tài liệu thụ động → nay dám phản biện khi thấy yêu cầu chưa rõ
- Người từng “ẩn mình” → nổi bật vì giúp team trace bug trước UAT

Không cần gắn nhãn. Họ tự chứng minh.

● **Một vài điểm tôi rút ra sau khi áp dụng:**
1. Liên kết với lương – thưởng:
- Việc phân cấp theo hành vi là nền để review lương theo kỳ (tháng, quý, 6 tháng) –
- không dùng để ép lương hay giảm bậc ngay tức thì.
2. Checklist hành vi nên có mẫu rõ ràng:
- Càng mô tả chi tiết (VD: “Từng detect 2 lỗi logic critical trước DEV trong 3 tháng gần nhất”) thì càng công bằng.
3. Phản hồi 360 độ:
- Tôi bổ sung thêm phản hồi từ đồng đội trong kỳ review.
- Đôi khi sự công nhận không đến từ sếp, mà đến từ tập thể.

📌 **Tổng kết**
Nếu bạn cũng đang tiếp quản một team BA:
- Đừng vội đánh giá – hãy quan sát
- Đừng gắn nhãn – hãy gợi mở
- Đừng áp bảng điểm – hãy dẫn dắt phát triển

Và khi cần phân cấp – hãy dùng:
→ Hành vi cụ thể, có dẫn chứng, có phản hồi 360.


---

## DAY 59/100 — DÀNH THỜI GIAN MỘT MÌNH ĐỂ SUY NGHĨ KHÔNG PHẢI ĐỂ NÉ TEAM

*Trang 140–141*

Một người lãnh đạo không chết chìm vì dự án khó, mà chết vì không còn nổi một tiếng để suy nghĩ cho ra trò.”
Có một kiểu mệt rất đặc biệt – chỉ những người đang làm BA Lead mới hiểu. Nó không phải kiểu “căng deadline”, không phải kiểu “bị khách hàng dí”...Mà là kiểu mệt lử vì ngày nào cũng đầy việc, nhưng tối về vẫn thấy bản thân... đang bị trôi.
- Không có một dòng nào để viết ra định hướng.
- Không đủ tỉnh táo để rà lại toàn bộ flow.
- Không có nổi 15 phút để tự hỏi: “Team mình đang làm cái quái gì thế này?”

🌀 **Vòng xoáy quen thuộc: bạn bị kéo xuống... từ từ mà rất chắc**
❗ Cuộc họp nào cũng mời bạn vào, vì “có lead thì mới chốt được”
Một buổi họp nhỏ giữa dev với tester – nhưng vẫn ping bạn “join cho chắc ăn”.
→ Dần dà, bạn biến thành cái ‘thẻ đảm bảo’ cho mọi buổi họp.
❗ Mỗi lần junior lăn tăn – lại forward cho bạn xử lý
“Anh/chị ơi, đoạn này em chưa chắc nên không dám chốt. Anh confirm giúp.”
→ Và bạn lại làm nốt phần tư duy mà lẽ ra họ cần luyện.
❗ Tất cả bug, sai lệch, hiểu nhầm – đều đẩy bạn vào làm “người hòa giải”
→ Cả team quên mất: BA Lead không phải là trung tâm hỗ trợ nghiệp vụ 24/7.

🔥 Và rồi bạn biến thành gì?
- Một người cực kỳ bận rộn.
- Một người luôn có mặt – nhưng không dẫn được ai.
- Một người xử lý rất giỏi – nhưng không còn dư thời gian để nhìn toàn hệ thống.
- Một người... đang gánh cả team trên vai, nhưng càng gánh, team càng dựa.

Bạn không nhận ra mình đang bị dẫn bởi guồng quay, cho tới khi thấy... chính mình không còn thời gian để nghĩ.

💭 Và đây là sự thật phũ phàng:
Làm lãnh đạo mà không còn được suy nghĩ thì bạn chỉ là BA cao cấp làm việc thay cho cả team. Không hơn.
❓ Vậy làm sao để thoát khỏi vùng lầy "bận tầm thấp"?
**1. Tự cắt cho bằng được một “slot tư duy” mỗi tuần – rồi bảo vệ nó như sinh mạng**
- Không họp.
- Không chat/email.
- Chỉ để bạn được suy nghĩ về hệ thống, về đội ngũ, về hướng đi.
- 📌 Vì nếu chính bạn không nghĩ, thì ai sẽ nghĩ thay bạn?

**2. Thiết lập luật phân quyền – rõ, rắn, rành mạch**
- Không ôm phần junior cần làm.
- Không chốt hộ.
- Không gỡ giúp.
- Không làm thay.

Bạn dạy họ cách tư duy – không phải cách phụ thuộc.
**3. Tách mình khỏi vai “người chữa cháy”, quay lại vai “người dẫn lửa”**
Bạn không sinh ra để đi sửa từng dòng mô tả bị sai.
Bạn ở đây để đặt câu hỏi:
- “Vì sao sai đó lại lọt được qua vòng review?”
- “Chúng ta đang thiếu điều gì ở quy trình này?”

▲ Nếu bạn không tự ngoi lên – chẳng ai kéo bạn ra
Vì bạn đang làm rất tốt vai trò “người cứu hộ”. Nên chẳng ai biết bạn đang kiệt sức. Và chẳng ai biết rằng, người team đang cần không phải một cỗ máy phản ứng, mà là một người dẫn đường.
● Bận không đồng nghĩa với đúng. Và nếu bạn không còn được dẫn dắt – thì bạn không còn là leader.
💬 Gửi đến bạn – người BA Lead đang đọc tới đây:
Nếu bạn đang thấy mình bị kẹt –
- Không phải vì quá yếu, mà vì... quá trách nhiệm.
- Không phải vì làm sai, mà vì làm thay quá nhiều.

Thì đây là lời nhắc: Đừng để mình trở thành “cái bóng đa năng” cho cả team, rồi đánh mất điều duy nhất chỉ bạn mới có thể làm: dẫn.


---

## DAY 60/100 — ESTIMATE TASK CHO BA – KHÔNG PHẢI ĐẾM MÀN HÌNH, MÀ ĐO ĐỘ XOẮN CỦA TƯ DUY

*Trang 142–144*

▲ Lưu ý: Công thức trong bài không phải chuẩn tuyệt đối. Các hệ số như độ phức tạp, thời gian confirm, khả năng reuse...thay đổi tùy dự án, tổ chức, và năng lực BA. Hãy dùng như một khung tư duy để bóc effort – đừng áp dụng máy móc.

Nhiều bạn BA kể cả đã làm vài năm, vẫn thường estimate effort dựa theo số lượng màn hình hoặc độ dài tài liệu. Ví dụ như task “Đổi điểm lấy voucher” – nhìn vào thì đơn giản:
Chỉ 1 màn hình – nhập điểm, chọn voucher, nhấn “Đổi”. Nhiều người sẽ nghĩ: "Task này chắc chỉ mất 1 ngày viết UC là xong." Nhưng thực tế lại mất đến 3–4 ngày, chưa kể vòng confirm qua nhiều bên. Vì phía sau cái nút “Đổi” bé xíu đó là cả một mê cung:
- Rule đổi khác nhau theo từng loại voucher
- Điều kiện ràng buộc: phải hoàn thành nhiệm vụ tuần
- Campaign sinh nhật + campaign khác cùng lúc → rule đè nhau
- Hệ thống cần kiểm soát tần suất thao tác để tránh lạm dụng

Và cần xác minh logic với cả pháp lý, vận hành để tránh sai sót nghiệp vụ
→ Một task tưởng “nhẹ như cái nút” lại xoắn não với 5 tầng logic.
Chốt lại: Estimate kiểu đếm màn hình thì chỉ có toang.
■ Vậy estimate thế nào mới đúng?
BA không estimate bằng mắt.
BA estimate bằng khả năng ngửi ra logic ẩn và ngầm hiểu độ xoắn.
📐 Công thức estimate task cho BA:
Estimate = (Effort base x Complexity x Team factor x (1 – Reuse rate)) + Time Confirm + Review Time + Buffer
■ Giải nghĩa từng phần:
- Effort base – thời gian viết tài liệu nếu nghiệp vụ đã rõ
- Complexity – rule đan chéo, logic phân nhánh
- Team factor – kinh nghiệm người viết
- Reuse rate – dùng lại UC, flow, form có sẵn
- Time confirm – thời gian xác minh với stakeholder
- Review time – thời gian rà tài liệu & xử lý comment
- Buffer – dự phòng rủi ro có thể đoán trước (rule thay đổi, stakeholder bẻ lái)

● Gợi ý thời gian review (nên cộng luôn vào estimate):
Task nhỏ: +0.5h
Task vừa: +1h
Task lớn hoặc UC phức tạp: +0.5–1 ngày để review + revise
📌 Viết nhanh mà không review kỹ → DEV/QC hiểu sai → mất gấp đôi effort fix sau.
Đừng tiếc 1 giờ mà phải trả giá bằng 3 ngày xử lý hậu quả.
🔍 Một ví dụ:
Task: Viết UC “Xét duyệt tạm ứng lương”
- Effort base: 4h
- Complexity: 2.0
- Team factor: 1.0
- Reuse rate: 0.2
- Time confirm: 1 ngày
- Review: 1h
- Buffer: 0.5 ngày

👉 Tổng estimate = 6.4h effort + 1h review + 1.5 ngày triển khai thực tế
● Góc nhìn của BA Lead/PM:
BA Lead/PM không chỉ nhìn số giờ effort – mà bóc ra thành 3 lớp:
- Effort – giờ công BA cần để hoàn thành
- Duration – effort chia theo % resource available + confirm time
- Elapsed time – tổng thời gian từ lúc giao đến khi bàn giao xong

BA Lead/PM cũng cộng thêm:
- Contingency Reserve (dự phòng cho rủi ro đã biết): dùng khi rule chưa rõ, flow hay thay đổi
- Management Reserve (dự phòng cho rủi ro chưa biết): ví dụ khách đổi hướng, business pivot

→ BA estimate effort đúng → PM mới dám vẽ timeline chuẩn.
🤝 Khi bị sếp hỏi: “Có mỗi cái nút mà làm lâu vậy?” Câu trả lời không cần khô cứng, nhưng cần logic: “Task này nhìn đơn giản, nhưng có rule đè giữa 2 campaign, phải lọc điều kiện user, anti-fraud, và cần xác minh với nhiều bên. Em estimate effort + review + buffer để đảm bảo chất lượng. Nếu cần em có thể chia sẻ breakdown hoặc dữ liệu các task tương tự đã làm.”

Không cần “chống chế” – chỉ cần thuyết minh bằng logic có cơ sở.
■ Thế nào là DONE?
DONE không phải là “viết xong tài liệu”.
DONE =
- Tài liệu đầy đủ, đúng phạm vi
- Đã được review & revise
- Confirm logic với stakeholder
- Đặt đúng nơi – đúng tên – đúng version
- Có thể DEV làm và TEST hiểu mà không hỏi tới lui

Nếu bạn chưa review, chưa xử lý comment, chưa xác minh nghiệp vụ → chưa DONE.

👀 Estimate là kỹ năng sống còn của BA.
Đó là cách bạn giữ niềm tin của team, bảo vệ chất lượng delivery,
và khẳng định tư duy hệ thống của chính mình.
Vì thực tế hiện nay vẫn đầy rẫy những câu hỏi khịa kiểu:
“Ủa? Có mỗi cái màn hình mà sao làm lâu vậy?”
“Có cái nút thôi mà ngồi 3 ngày?”
Không sao. Bạn không cần biện minh.
Bạn chỉ cần chìa công thức – chỉ vào logic – và đưa dữ liệu.
📌 Estimate không phải để chứng minh bạn nhanh – mà để chứng minh bạn hiểu. Và hiểu sâu – chính là nền móng vững nhất để không toang trong mọi dự án.


---

## DAY 61/100 — SAO HÔM QUA ĐI CHỈ 50K, MÀ HÔM NAY CŨNG THẾ LẠI 65K?

*Trang 145–147*

🪄 Một tối Chủ Nhật, Hà Nội mưa rào...
Trời mưa. Giá đặt xe tăng vọt. Tôi không đi đâu cả. Nhưng lại nổi hứng... phân tích hệ thống dynamic pricing
● Case study: Gọi xe Xanh SM
Bạn đặt xe đi 5km ở Ba Đình
Hôm qua: 50k
Hôm nay: trời mưa, giờ tan tầm → 90k
Vẫn cùng 1 tuyến đường, nhưng giá thay đổi.
Không phải do hãng “chặt chém”.
Mà là vì hệ thống thấy:
- Nhu cầu tăng đột biến
- Ít xe sẵn sàng trong khu vực
- Điều kiện vận hành khó khăn (mưa, dễ kẹt xe, delay)

→ Giá cần tăng để đảm bảo:
Tài xế có động lực nhận chuyến
Người đặt xe thật sự nghiêm túc
Cân bằng cung – cầu
Vậy nên, giá hôm nay khác hôm qua.
Không cảm tính. Mà là thuật toán sống.

📌 Nhưng nếu bạn là BA, bạn không được dừng ở việc... hiểu logic đó.
Bạn phải viết được logic đó thành hệ thống có thể vận hành, cấu hình, mở rộng, và giải thích được. Nhiều bạn BA sẽ viết kiểu:
- “Nếu trời mưa thì cộng 15k”
- “Nếu giờ cao điểm thì nhân giá 1.2 lần”
- Nghe có vẻ đúng. Nhưng sai ở cấp độ thiết kế.
- Vì mỗi lần muốn đổi mức giá, DEV phải sửa code, test lại, deploy.
- Team vận hành không có cách nào điều chỉnh theo thị trường.

■ Thiết kế đúng: phải có Rule Engine
Bạn cần đề xuất xây dựng một mô-đun định giá linh hoạt, cho phép:
- Tạo mới rule giá
- Bật/tắt rule bất kỳ lúc nào
- Thiết lập điều kiện, hành động, độ ưu tiên
- Không cần DEV code lại mỗi lần thay đổi

Ví dụ:
Nếu trời mưa → cộng 15k
Nếu giờ 17h–19h → nhân hệ số 1.3
Nếu user huỷ 3 chuyến trong 7 ngày → cộng 10k
Nếu là user VIP dịp sinh nhật → giảm 20k
Tất cả phải cấu hình được qua giao diện backend.
Vận hành chủ động, không cần “push code”.
💭 Và đừng quên: giải thích giá cho người dùng
Khi giá tăng, điều đầu tiên khách hàng làm là... nổi cáu.
Nhưng nếu có dòng này trên app:
💬 Giá bạn thấy gồm:
Giá cơ bản: 50k
Phụ phí trời mưa: +15k
Giờ cao điểm: +10k
Tổng: 75k
→ Họ hiểu. Họ bớt ấm ức. Và họ không gọi hotline cãi nhau.

Nghĩa là:
- Trải nghiệm người dùng tốt hơn
- Tỷ lệ khiếu nại giảm
- QC test dễ hơn
- BA trace lỗi dễ hơn

Đó là lý do mà trong mô hình dynamic pricing, việc “hiển thị lý do giá” quan trọng không kém việc tính đúng giá.
🧩 Vậy BA cần đảm bảo những gì?
Tách từng yếu tố ảnh hưởng giá thành rule riêng
Thiết kế cấu trúc rule engine linh hoạt, override được nhau, test được logic
Thiết kế màn hình hiển thị breakdown giá rõ ràng
Log toàn bộ rule được áp dụng vào từng đơn hàng
Dự phòng kịch bản giá lỗi, mâu thuẫn rule, hoặc thiếu dữ liệu
🪄 Tổng kết:
Làm dynamic pricing không khó về mặt tính toán.
Cái khó là thiết kế ra được một hệ thống sống:
Tự thích nghi
Minh bạch
Có thể cấu hình
Dễ kiểm soát – dễ giải thích – dễ mở rộng
Là BA, nếu bạn chỉ nghĩ “làm sao tính ra con số”, bạn sẽ toang.
Bạn cần nghĩ:
- Người dùng có hiểu con số đó không?
- Vận hành có chỉnh được không?
- DEV có maintain được không?

Tối mưa rảnh, phân tích hệ thống hộ nhau – biết đâu lại ra mini course


---

## DAY 62/100 — KHI DỰ ÁN CHỈ CÓ... DEADLINE VÀ 1 CÂU NÓI MƠ HỒ BA NÊN LÀM GÌ ĐẦU TIÊN?

*Trang 148–152*

“Làm cái hệ thống đặt bàn cho nhà hàng đi – cho chuyên nghiệp hơn, đỡ lộn xộn. Anh cần chạy demo trong 2 tuần nữa nhé.”
Đó là tất cả những gì tôi nhận được khi bắt đầu dự án này.
- Không tài liệu.
- Không flow.
- Không ai mô tả được “chuyên nghiệp” là như thế nào.
- Chỉ có deadline và một câu nói mơ hồ đầy quyết đoán.

BA mà không tỉnh – là dính ngay combo chết người:
- Làm sai bài toán gốc
- Giao sai chức năng
- Xây hệ thống xong không ai xài
- Và cuối cùng: đổ lỗi ngược lại cho BA vì "không hiểu yêu cầu"

■ **BA cần làm gì khi bắt đầu một dự án from scratch?**
Tôi chia sẻ lại từng bước tôi đã làm trong những dự án kiểu này, từ con số 0, không có hệ thống cũ, không quy trình chuẩn, chỉ có deadline và một câu nói... “mang tính truyền cảm hứng”.
1. **Khởi động bằng tư duy “Problem First” – không phải “System First”**
✖ Sai lầm phổ biến:
- Khi bắt đầu dự án, nhiều bên sẽ nói: “Làm app để quản lý ”, “Cần có chức năng A, B, C”, “Xây dashboard để theo dõi”
- Tức là toàn nói về giải pháp và tính năng mà chưa ai hỏi đúng câu quan trọng nhất:
  “Thực tế hiện tại đang xử lý như thế nào? Có vấn đề gì khiến phải làm hệ thống?”

■ **Cách tiếp cận đúng của BA:**
Không hỏi "muốn hệ thống có gì"
Mà hỏi "đang làm thế nào?", "đang gặp khó ở đâu?", "điều gì khiến mọi người thấy cần thay đổi?"
● **Mục tiêu:**
Làm rõ bài toán gốc trước khi bàn về giải pháp
Phân biệt rõ giữa: cái người dùng muốn và cái họ đang cố gắng giải quyết

**2. Xác định đúng stakeholder ngay từ đầu – kẻo lạc hướng cả hệ thống**
Một trong những lý do khiến dự án đi sai hướng là vì BA nghe sai người hoặc gom tất cả stakeholder vào một rổ. Trong bất kỳ dự án nào, stakeholder luôn có nhiều vai trò – và điều nguy hiểm là:
- Người ra yêu cầu chưa chắc là người sử dụng,
- Người sử dụng chưa chắc có tiếng nói,
- Và người chịu ảnh hưởng chưa chắc được mời họp.

■ Việc cần làm ngay từ đầu: Liệt kê và phân loại stakeholder theo vai trò chức năng, không theo chức danh, ví dụ:
- Người ra yêu cầu / quyết định – thường là quản lý cấp cao, họ quan tâm đến hiệu quả tổng thể
- Người vận hành trực tiếp – người thực sự thao tác hàng ngày trên hệ thống
- Người phối hợp / hỗ trợ – những người liên quan gián tiếp đến quy trình
- Người chịu ảnh hưởng / nhận kết quả – có thể là khách hàng nội bộ, đối tác, khách bên ngoài

● Mỗi nhóm này cần tiếp cận khác nhau: Người ra yêu cầu cần hiểu bức tranh lớn
- Người vận hành cần luồng thao tác tối ưu
- Người hỗ trợ cần logic rõ ràng, trạng thái minh bạch
- Người nhận kết quả cần đầu ra dễ hiểu, đúng thời điểm

**3. Dẫn dắt workshop đầu tiên – vẽ lại bức tranh toàn cảnh**
Một trong những bước BA giỏi luôn chủ động làm, là không vội viết tính năng, mà tổ chức một buổi workshop để làm rõ thực tế hiện tại và định hình logic tổng thể.
✖ Sai lầm phổ biến:
Gặp khách hàng là hỏi: “Anh/chị cần hệ thống làm gì? Muốn có chức năng gì?”
→ Nghe tưởng đúng, nhưng bạn sẽ thu về một danh sách mong muốn rời rạc, thiếu kết nối, mà không có bức tranh hệ thống nào đứng đằng sau.
■ Cách làm đúng:
Tôi tổ chức 1 buổi workshop ngắn với các đại diện đến từ:
Người thao tác trực tiếp
Người phối hợp liên phòng ban
Người quản lý giám sát
Người nhận kết quả / chịu ảnh hưởng
Không yêu cầu họ mô tả tính năng. Tôi hướng dẫn họ vẽ lại quy trình hiện tại – theo ngôn ngữ của họ, không ép kỹ thuật.

📋 Những câu hỏi gợi mở thường dùng:
Một nghiệp vụ cụ thể diễn ra như thế nào, từ đầu đến cuối?
Ai là người bắt đầu, ai là người thực hiện, ai là người kiểm tra?
Tại đâu thường xảy ra lỗi hoặc trễ tiến độ?
Nếu quy mô tăng gấp đôi, đoạn nào dễ vỡ nhất?
● Mục tiêu buổi workshop:
Làm rõ thực trạng (AS-IS)
Phát hiện điểm tắc (pain points)
Xác định mục tiêu cần đạt (TO-BE)

**4. Xây dựng khung phân tích đầu tiên – đừng vội viết Use Case**
Sau buổi workshop làm rõ hiện trạng, điều quan trọng nhất BA cần làm không phải là lao vào viết tài liệu, mà là dựng khung hệ thống nền tảng để dẫn dắt mọi phân tích phía sau.
✖ Sai lầm phổ biến:
Vừa nghe xong buổi họp đầu tiên đã ngồi viết Use Case
→ Viết ra hàng loạt chức năng rời rạc, thiếu logic tổng thể
→ DEV không biết bắt đầu từ đâu, TEST không hiểu gì để test
■ Việc tôi luôn làm ngay sau workshop:
📘 Từ điển nghiệp vụ (Business Glossary)
Tập hợp các thuật ngữ đang được các bên sử dụng, thống nhất nghĩa:
Một từ – một nghĩa duy nhất
Ai cũng hiểu giống nhau, tránh nói A hiểu B
Ví dụ: “đơn hàng”, “phiếu đăng ký”, “đơn khiếu nại”, “tài khoản” – mỗi tổ chức có định nghĩa riêng
● Sơ đồ tổng quan dòng nghiệp vụ (Business Context / Flow Overview)
Vẽ luồng chính từ điểm bắt đầu → qua các bước xử lý → đến đầu ra cuối cùng.
Giúp trả lời câu hỏi:
Hệ thống nằm ở đâu trong bức tranh tổng thể?
Dữ liệu đi qua những bước nào?
Những ai liên quan?
→ DEV nhìn sơ đồ đã hiểu cần xử lý đoạn nào trước, trạng thái nào là quan trọng, chỗ nào cần kiểm tra kỹ.

🧩 **Danh sách feature sơ bộ – chia theo hành trình hoặc cụm logic**
Tôi không viết đặc tả. Tôi chỉ gom nhóm chức năng ở mức sơ cấp:
Nhóm tạo / gửi / xử lý
Nhóm theo dõi trạng thái
Nhóm kiểm tra / xác nhận
Nhóm báo cáo / thống kê

● Mục tiêu:
Cả team có chung góc nhìn. Không bị cuốn vào chi tiết sớm. Có cơ sở để chia phase triển khai và phân tích sâu dần
1. Lập kế hoạch phân tích chi tiết – chia phase rõ ràng
2. Sau khi dựng được bức tranh tổng thể, tôi không lao ngay vào viết 20 Use Case.

Tôi lập một kế hoạch phân tích theo từng phase rõ ràng – để:
Team không bị “ngợp”
DEV biết bắt đầu từ đâu
Stakeholder thấy được giá trị sớm → có phản hồi thật → chỉnh kịp
■ Cách tôi thường chia phase:
📌 Phase 1 – Xây dựng lõi vận hành (MVP)
Tập trung vào:
Luồng nghiệp vụ chính cần chạy được (nếu không có, hệ thống vô nghĩa)
Giao diện nội bộ / thao tác đơn giản
Xử lý thủ công chấp nhận được
● Mục tiêu:
Dự án chạy được ở mức tối thiểu để test logic, kiểm nghiệm giả định.
📌 Phase 2 – Tối ưu quy trình
Sau khi có phản hồi từ phase 1, tôi bổ sung:
Tự động hóa bước lặp
Cảnh báo, kiểm tra lỗi
Giao diện cho các nhóm người dùng khác nhau
Báo cáo phục vụ vận hành thực tế

● Mục tiêu:
Hệ thống không chỉ chạy được, mà chạy ổn định và giảm lỗi vận hành.
📌 Phase 3 – Tăng trải nghiệm và mở rộng
Lúc này mới tính:
Gợi ý, đề xuất thông minh
Tối ưu UX
Kết nối các bộ phận, hệ thống khác
Phân tích số liệu chuyên sâu
● Mục tiêu:
Biến hệ thống từ công cụ xử lý nghiệp vụ thành trợ lý hỗ trợ quyết định.
💡 Nguyên tắc khi chia phase:
Không chia theo màn hình ("làm giao diện A trước, B sau”)
Không chia theo người nói ("sếp cần trước, nhân viên để sau”)
Mà chia theo giá trị nghiệp vụ mang lại và độ rủi ro logic
🔑 Nguyên tắc cốt lõi:
“Một bản phân tích tốt không cần phải dài – nhưng phải có thứ tự.
Và Use Case hay nhất là Use Case đúng thời điểm.”
🔚 Dự án mơ hồ không phải chuyện hiếm.
Cái hiếm là có một BA đủ tỉnh để không lao vào viết tài liệu ngay khi chưa hiểu rõ bài toán.
5 bước trên là thứ tôi nghĩ khi bạn áp dụng mỗi khi bước vào dự án mà:
- Không có tài liệu
- Không ai chốt được yêu cầu
- Deadline thì vẫn dí

Không phải lý thuyết.
Không màu mè.
Chỉ là cách để không chết chìm cùng cả team khi mọi thứ đều chưa rõ.
Nếu bạn đang bị “quăng vào” một dự án kiểu đó – đọc lại từng bước, làm từng việc, và giữ cái đầu đủ lạnh để dẫn dắt team, không bị kéo theo người nói to nhất.
Thế thôi chúc tuần mới vui vẻ tràn đầy hiệu quả nhé.


---

## DAY 63/100 — LÀM SẢN PHẨM... NHƯNG KHÔNG AI ĐƯỢC QUYỀN QUYẾT ĐỊNH

*Trang 153–154*

Một đội ngũ kỹ thuật – sản phẩm – thiết kế đã ngồi cùng nhau suốt nhiều tuần.
- Họ đi nghiên cứu người dùng.
- Họ test từ bản wireframe đến prototype.
- Họ biết “nỗi đau” thật sự nằm ở đâu.

Nhưng đến buổi duyệt thứ 4 – có một người không ở trong hành trình ấy bước vào và nói: “Tôi thấy nên bỏ đoạn này, thêm phần kia. Sao UI nhìn vẫn thiếu chuyên nghiệp? Sao chức năng này chưa đủ?”
Lúc đó, cả phòng họp im lặng. Không ai phản ứng gay gắt. Chỉ là một kiểu im lặng lạnh lùng – của những người biết rõ mình không có quyền phản biện.
Tưởng như chuyện nhỏ. Nhưng đó là dấu hiệu của một văn hóa sản phẩm gãy:
✖ Người đưa ra quyết định không ở trong hành trình.
✖ Người ở trong hành trình không được quyền quyết định.
Cứ thế, mọi sáng tạo đều bị “chốt” lại giữa chừng. Mọi cải tiến đều phải “trình” – dù người trình hiểu người dùng hơn gấp 10 lần.
Đội sản phẩm không ghét góp ý. Họ cần góp ý. Nhưng điều khiến họ gục ngã là: họ không được tin. Không tin dữ liệu họ có. Không tin đề xuất của họ. Không tin logic mà họ đang cố gắng bảo vệ. Và ở phía ngược lại người duyệt cũng có lý do riêng. Không ai muốn suốt ngày nhảy vào chỉ tay, bắt đội ngũ sửa tới sửa lui. Thật ra, họ cũng mệt.
Nhưng đứng ở vị trí cao hơn – họ là người phải gánh trách nhiệm:
- Nếu sản phẩm thất bại, họ mất tiền.
- Nếu khách hàng than phiền, họ bị gọi tên.
- Nếu thương hiệu bị ảnh hưởng, họ là người đứng mũi chịu sào.

Thế là họ bắt đầu lo sợ:
- Sợ đội ngũ làm chưa tới.
- Sợ ra mắt xong không ai xài.
- Sợ bị hỏi “Ai duyệt cái này vậy?”

Và khi sợ... họ chen vào, họ giật quyền quyết định – dù không ở trong hành trình làm sản phẩm từ đầu.

Một sản phẩm tốt cần 2 thứ:
- Người làm đủ sâu để thấy vấn đề thật.
- Người duyệt đủ tin để không chen ngang giữa chừng.

Niềm tin là thứ không thể ép buộc, nhưng có thể xây được.
- Bằng dữ liệu.
- Bằng cách đội sản phẩm trình bày logic của mình.
- Bằng cách lãnh đạo học cách “giao quyền từng phần và quan sát.”

Muốn làm sản phẩm tốt – không thể chỉ có kỹ năng. Phải có văn hóa tin nhau.
Tin rằng nếu người làm sản phẩm nói “đừng làm tính năng này” thì họ đang cố bảo vệ hệ thống, không phải cãi. Tin rằng nếu một team dám làm khác thì đó là vì họ tin vào hành trình họ đã đi với người dùng.
Một đội sản phẩm không cần người giỏi ra quyết định. Họ cần người đủ tin để không ra quyết định một mình.


---

## DAY 64/100 — CÂY BI AI GIAO KPI THẾ NÀO CHO ĐÚNG VÀ HIỆU QUẢ?

*Trang 155–156*

“Mỗi sprint phải đẩy 20 UC, chốt 4 SRS, tạo 5 ‘idea cải tiến’, tham dự 4 cuộc họp, xử lý tối thiểu 30 comment trên Jira.” Nghe cứ như ép doanh số cho… tài liệu. Khi KPI biến BA thành “công nhân gõ chữ”, giá trị thật sự sẽ chết khô.

**Vì sao KPI “đếm file” giết chết tư duy BA?**
Khi chỉ tập trung vào output, người làm sẽ tối ưu số lượng chứ không còn đào sâu logic.
Ví dụ: “Viết đủ 3 SRS/tuần” → BA sẽ copy-paste hoặc mô tả ẩu để chạy kịp số.
Khi KPI không xuất phát từ pain-point thật, sẽ sinh ra hành vi giả vờ bận rộn.
Ví dụ: “Phải gặp 2 stakeholder mới/sprint” → BA rủ nhầm người vào họp cho đủ số.
Khi không đo được chất lượng đầu ra, bug và rework sẽ càng ngày càng nhiều.
Ví dụ: “Xử lý 30 comment Jira” → BA spam chat để đạt KPI, còn DEV thì loay hoay không hiểu spec.
Khi ép số lượng cải tiến, ý tưởng… dù sản phẩm đang ổn định, BA sẽ cố nghĩ ra feature vô nghĩa để đủ chỉ tiêu.

**Giao KPI đúng: Đo bằng giá trị, không phải số lượng**
First-pass requirement accuracy (FPRA): Tỷ lệ yêu cầu được DEV/QA làm đúng ngay lần đầu, không phải sửa lại vì sai logic.
Time-to-clarify: Thời gian từ lúc nhận yêu cầu đến lúc đặc tả đủ và sẵn sàng dev.
Stakeholder alignment score: Mức độ đồng thuận và hiểu đúng giữa các bên. Có thể đo bằng mini survey nội bộ.
Feature adoption rate: Tỷ lệ người dùng sử dụng tính năng do BA phân tích sau 30 ngày triển khai.
Số lỗi do phân tích sai (requirement-related bug): Giảm dần theo sprint là tín hiệu KPI đang đi đúng hướng.

Đặt KPI đúng – 5 bước không thể thiếu
Bắt đầu từ pain-point. Đừng ép KPI cho có. Hãy hỏi: đang gặp vấn đề ở đâu? Rework? Bug? Dev hỏi lại nhiều?
Map nguyên nhân – kết quả. BA ảnh hưởng phần nào của vòng đời phát triển? Dẫn dắt logic, làm rõ yêu cầu, align stakeholder… hãy đo cái đó.

SMART hóa từng KPI.
Ví dụ:
FPRA = % use case qua QA không bug BA
Có baseline (72%), có mục tiêu (85%), có thời gian (2 quý), có cách tracking (tag bug).
Đo bằng công cụ thật, không bằng cảm giác, để BA không phải tự đếm điểm thủ công.
Có retro, có update.
Sprint nào cũng xem lại KPI. Không để KPI cũ giết team mới.

💬 “Một KPI tốt mở khóa tư duy hệ thống; KPI đếm số khóa miệng mọi câu hỏi ‘tại sao’.”

**Roadmap áp dụng**
Sprint 0 – Baseline: Gắn tag lỗi “requirement unclear”, đo FPRA hiện tại.
Sprint 1 – Pilot: Chọn 1 module làm thử, training kỹ thuật đào sâu yêu cầu như 5 Why, tư duy data object.
Sprint 2 – Mở rộng: Nhân rộng ra toàn team, thiết lập dashboard theo dõi tự động.
Sprint 3 – Tối ưu: Retro, điều chỉnh KPI theo thực tế và mục tiêu quý.

● **Đừng biến BA thành người chạy số lượng.**
KPI là thứ để phát hiện điểm nghẽn, nuôi tư duy hệ thống – không phải ép người gõ giấy lấy điểm. Một KPI sai có thể làm hỏng cả team trong vài sprint. Một KPI đúng sẽ khiến BA tỏa sáng như người dẫn đường chiến lược.


---

## DAY 65/100 — CHUYÊN MỤC “ANH ƠI…”

*Trang 157–159*

Hôm nay không viết chia sẻ kiến thức, mà chuyển sang chuyên mục “Anh ơi…” – nơi BA gửi những ca khó xử nhất trong dự án, và mình sẽ cùng gỡ.
Chuyên mục bắt đầu!
**Câu hỏi**
Em chào anh, em đang có issue trong công việc chưa biết nên xử lý thế nào nhờ anh hỗ trợ góp ý.
Hiện em qua công ty mới, ở đây làm product. PO dự án là người có ý tưởng phát triển sản phẩm, là người trực tiếp em trao đổi lấy yêu cầu.
PO này khác định nghĩa PO mà em từng biết, tức là chỉ đưa ra yêu cầu, ý tưởng, không quản lý backlog, user story.
Khi tài liệu em viết ra thì PO nói không có thời gian để đọc xác nhận, quá bận, em hãy trình bày bằng lời đi. PO nói quá bận không thể đọc nổi nhiều trang tài liệu như vậy.
Em thấy khó xử khi vừa phải viết tài liệu chi tiết sau đó lại trình bày chi tiết từng chữ lại.
Vậy theo anh BA có nên đáp ứng nhu cầu đó của PO không, hay do em kiểu thiển cận quá? Trước đó khi em đi làm thì tài liệu các bên liên quan phải đọc kỹ, còn trình bày thì chỉ nói tổng quan, không đi sâu chi tiết

**Trả lời**
Anh hiểu vấn đề em đang gặp và đây là một tình huống rất phổ biến trong môi trường làm product, nơi mà vai trò của PO có thể khác biệt khá nhiều giữa các công ty.
Cách giao tiếp, trao đổi kỳ vọng cũng cần được tinh chỉnh linh hoạt, chứ không thể bê nguyên cách làm cũ sang.
● Trước hết, không có ai sai trong câu chuyện này.
PO không sai khi bận rộn và không thể đọc kỹ tài liệu. Chuyện này xảy ra rất nhiều khi PO phải lo cả vận hành, roadmap, hoặc còn kiêm team lead.
Em cũng không sai khi mong đợi tài liệu được đọc và xác nhận để tránh hiểu nhầm. Đó là tư duy BA chuyên nghiệp.
Tuy nhiên, vấn đề không nằm ở ai đúng ai sai, mà là: mình cần thích nghi với cách vận hành mới và chủ động “thiết kế lại” cách làm việc giữa BA và PO.

● **Góc nhìn chiến lược: BA giỏi không viết nhiều – mà thiết kế cách để người ta dễ hiểu**
**1. PO không đọc không có nghĩa là không chịu trách nhiệm**
Họ vẫn ra quyết định, vẫn approve requirement, nhưng cách họ tiếp nhận thông tin cần được tối ưu hơn, giống như trình bày pitch deck thay vì gửi một bản BRD dài 100 trang.
Vậy em cần tách 2 lớp thông tin:
Lớp 1: Slide hoặc summary ngắn gọn, 1–2 trang, thể hiện những điểm chính (giống executive summary): mục tiêu, chức năng chính, flow tổng quát, điểm rủi ro.
Lớp 2: Tài liệu chi tiết (SRS, user flow, rule list…) để DEV, QC, Design dùng.
Cách này vừa giúp PO nắm ý chính, vừa không bỏ qua trách nhiệm deliver chuẩn của BA.
**2. Chấp nhận trình bày miệng – nhưng phải có cấu trúc và trace lại**
PO nói “trình bày bằng lời” → em có thể tạo khung trình bày cố định, ví dụ:
- Vấn đề business cần giải
- Cách xử lý đã phân tích
- Flow người dùng
- Các tình huống rẽ nhánh, constraint
Sau buổi nói, em nên gửi lại qua chat hoặc email vắn tắt các điểm đã chốt để làm bằng chứng và giúp PO có cái để đọc lại nhanh.
**3. Đưa ra khuyến nghị về cách phối hợp làm việc – chứ không chống đối**
Anh gợi ý em đặt lại expectation với PO theo cách như sau:
“Em hiểu anh/chị rất bận nên không thể đọc hết tài liệu chi tiết. Để mình phối hợp hiệu quả hơn, em sẽ luôn chuẩn bị một bản slide ngắn gọn trước mỗi buổi trao đổi, còn tài liệu chi tiết em vẫn viết để đội DEV, QC nắm. Sau buổi mình nói chuyện, em sẽ gửi recap lại. Nếu có gì chưa đúng anh/chị cứ phản hồi giúp em chỉnh.”
■ Câu này không đổ lỗi, không trách móc, mà thể hiện:
- Em chủ động giải quyết vấn đề.
- Em hiểu vai trò và áp lực của PO.
- Em vẫn bảo vệ chuẩn chất lượng yêu cầu.

■ Kết luận
Là BA làm product, em không thể mong ai cũng đọc hết tài liệu. Nhưng em phải đảm bảo họ hiểu – và hệ thống vẫn chạy đúng.
Vì thế:
Không nên từ chối việc trình bày miệng, mà hãy chuẩn hóa cách trình bày đó như một “ritual” trong teamwork.
Không được bỏ tài liệu chi tiết, vì đó là xương sống để DEV, QC, và chính em trace lại sau này.
Không ngồi than thở vì PO không đọc, mà hãy chủ động thiết kế giải pháp phù hợp với nhịp làm việc thực tế của người ta.
Chúc anh chị em BA luôn vững tay chèo giữa muôn kiểu PO khác nhau.


---

## DAY 66/100 — BA CHỌN CÔNG TY STARTUP HÃY NHÌN NHƯ MỘT NHÀ ĐẦU TƯ, ĐỪNG CHỌN VÌ CẢM XÚC

*Trang 160–161*

Trong giai đoạn pre-seed đến series A, có rất nhiều startup gọi được vốn. Điều đó thường khiến người ta tin rằng: “Công ty này gọi được tiền → chắc là ổn → vào đó làm BA sẽ có đất dụng võ.”
Sai. Rất sai.
Là một BA, bạn cần nhìn vào startup không chỉ như một người đi làm. Bạn phải nhìn nó như một hệ thống sẽ phát triển – hoặc sẽ đổ sập.
Và góc nhìn giúp bạn nhận ra điều đó chính là góc nhìn của nhà đầu tư nghiêm túc.

**Nhà đầu tư thật sự nhìn gì?**
Họ không chỉ nhìn pitch deck đẹp. Họ nhìn đội ngũ có hệ thống tư duy không, có năng lực đo lường, lặp lại, sửa sai không, có mô hình đang chạy thật hay mới chỉ là ý tưởng trôi nổi.
Họ gọi đó là “execution confidence” – không phải vì bạn hứa hẹn hay kể chuyện hay, mà vì bạn có khả năng biến một idea thành mười flow thật, một trăm users thật, và feedback thật để iterate sản phẩm.
**BA thì sao?**
Cũng phải nhìn y như vậy. Startup là môi trường tốc độ cao, tài nguyên ít, và biến số nhiều.
Nếu bạn bước vào một startup chỉ vì họ gọi được vài tỷ, nhưng:
- Không có quy trình ra quyết định rõ ràng.
- Không có cách đo lường user behavior.
- Không có mô hình phân tích dữ liệu để định hướng sản phẩm.
- Không có ranh giới vai trò giữa BA – DEV – Product.
Thì bạn không phải đang làm BA, mà đang làm lính cứu hỏa. Gỡ bug, vá flow, họp mồm. Mỗi sáng nhận task theo cảm xúc của sếp, chiều họp lại thấy product quay xe.

**Ngược lại, một startup đáng để BA đầu quân thường có các dấu hiệu**
Founder hiểu rõ insight thị trường hơn là chỉ nhìn đối thủ. Họ không copy tính năng vì “bên kia có”, mà biết tại sao cần – có xứng đáng đầu tư không.

Product có roadmap được xây dựa trên dữ liệu, không chỉ dự cảm. Có tracking hành vi người dùng, có chỉ số churn, retention để làm cơ sở ra quyết định.
Team nhỏ nhưng có quy tắc phối hợp rõ ràng. Họ có thể chưa dùng tool xịn, chưa có tài liệu long-form, nhưng mỗi người đều hiểu mình đang làm gì và tại sao.
Ở nơi đó, BA có thể làm discovery flow thật sự – chứ không phải chỉ mô tả tính năng. Có thể góp tiếng nói vào chiến lược – vì hệ thống họ đang xây cần người hiểu toàn cảnh. Và được tôn trọng vì khả năng thiết kế logic – chứ không bị coi là người “viết cho dev dễ hiểu”.

**Câu hỏi gốc rễ**
Bạn muốn vào một startup “gọi được vốn”, hay một startup “xây được nền”?
Vốn là để sống sót. Nhưng nền là để scale. Nhiều founder gọi được tiền vì kể chuyện hay – nhưng chính investor thật sự cũng lo: “liệu team này có biết mình đang làm gì không, hay sẽ đốt hết tiền để chạy theo ảo tưởng growth?”

**Vai trò của BA**
Là BA, bạn không thể kiểm soát định hướng đầu tư. Nhưng bạn có thể chọn môi trường có tư duy hệ thống, có data làm nền, có roadmap có logic, và có sự rõ ràng về vai trò BA.
Đừng để vẻ ngoài “gọi vốn thành công” đánh lừa bạn. Hãy nhìn một startup như nhà đầu tư nhìn: liệu công ty này có khả năng vận hành ổn định và cần một BA để lớn mạnh, hay chỉ cần một người ghi lại những ý tưởng sắp đổi vào tuần sau?
BA không phải người chép ý tưởng từ founder. BA là người giữ logic sống sót khi sản phẩm lạc hướng.
Chọn sai môi trường, bạn sẽ mất một năm tuổi nghề để học lại từ đầu.
Chọn đúng môi trường, bạn không chỉ phân tích flow – bạn sẽ học được cách xây một hệ thống từ gốc.


---

## DAY 67/100 — ÁP DỤNG CI/CD BA KHÔNG VIẾT CODE NHƯNG CÓ THỂ GÂY LỖI PRODUCTION!

*Trang 162–164*

🚀 **CI/CD là gì?**
CI (Continuous Integration – tích hợp liên tục): Mỗi lần Dev (developer – lập trình viên) đẩy code lên hệ thống, hệ thống sẽ tự động build (biên dịch) và chạy kiểm thử ngay lập tức.
CD (Continuous Delivery/Deployment – phân phối/triển khai liên tục): Khi code đã qua kiểm thử, hệ thống sẽ tự động đưa code mới lên môi trường staging hoặc production – không còn bước kiểm thủ công từ QC trước khi deploy.

● **Mục tiêu chính:**
Ra tính năng nhanh hơn. Giảm lỗi do thao tác thủ công. Luôn giữ hệ thống trong trạng thái có thể triển khai. Nhưng đi kèm: nếu logic sai – hệ thống sẽ “triển khai sai” nhanh, không báo trước.

● **CI và CD ảnh hưởng gì đến BA?**
CI đòi BA phải làm rõ logic sớm, giúp Dev và QC có đủ thông tin để code/test luôn – không đợi đến sát ngày UAT mới sửa.
CD buộc BA phải chia nhỏ chức năng, giúp hệ thống có thể triển khai từng phần, rollback (quay lại phiên bản cũ) dễ dàng nếu lỗi.

🔥 **Trước và sau CI/CD – Điều gì thay đổi?**
Trước CI/CD: Dev code xong → QC test thủ công → lỗi logic được phát hiện sớm → có thời gian sửa. BA sai vẫn có cơ hội “chữa cháy”.
Sau CI/CD: Dev đẩy code xong → hệ thống tự test, tự triển khai. Nếu test case thiếu hoặc hiểu sai logic → lỗi ngay trên production. Sai là bung. Không sửa kịp.

■ **Một ví dụ thực tế**
Ứng dụng đặt món ăn. BA mô tả tính năng: “Khách hàng thân thiết được giảm 10% giá món.”

Nghe đơn giản. Nhưng không ghi rõ:
- Thế nào là thân thiết?
- Áp dụng trên giá gốc hay giá đã giảm?
- Combo có được giảm tiếp không?
- Giới hạn một lần/ngày hay bao nhiêu lần tùy thích?
Dev code đúng theo hiểu. QC test pass. CI/CD tự động đẩy production.
Khách đặt combo + thân thiết → giảm tiếp 10% → doanh nghiệp bị ảnh hưởng doanh thu ngoài dự kiến. Vì sao? Vì logic không rõ. Và CI/CD đã giúp triển khai cái sai một cách nhanh – gọn – lẹ.

♟ **Vậy BA cần làm gì trong CI/CD?**
**1. Viết tài liệu đủ rõ để test được, và test tự động được**
Viết cho người hiểu là chưa đủ. Phải viết sao cho Dev hiểu đúng, QC viết test đúng, hệ thống có thể chạy test tự động được. Nghĩa là:
- Nêu rõ Input – Output.
- Ghi kỹ luật xử lý.
- Mô tả các điều kiện, ngoại lệ.
- Nêu rõ kết quả mong đợi (expected result).
**2. Liên kết logic ↔ test case (Traceability – khả năng truy vết)**
BA không viết test case thay cho QC. Nhưng BA phải chắc chắn mỗi business rule đều được kiểm tra. Thực tế, BA nên liệt kê các tình huống biên (boundary case), viết bảng tình huống – kết quả mong đợi (dù đơn giản). Với team áp dụng BDD (Behavior Driven Development), có thể viết luôn câu Gherkin (Given – When – Then).
**3. Hỗ trợ đúng loại test phù hợp**
CI/CD không chỉ test đơn giản. Nó bao gồm:
- Unit test (kiểm tra từng hàm).
- Integration test (kiểm tra các phần kết nối với nhau).
- End-to-end test (mô phỏng luồng người dùng thật).
BA không cần viết test này, nhưng BA cần hiểu logic nào cần test ở đâu, biết cách đưa ra tình huống kiểm thử đủ độ phức tạp, phối hợp với Dev/QC khi test bị fail để xác minh đúng/sai từ đâu.

**4. Thiết kế chức năng theo hướng chia nhỏ – dễ test – dễ rollback**
Triển khai một cụm tính năng lớn là rủi ro cực cao trong CI/CD. BA cần phân nhỏ theo từng module độc lập, thiết kế bật/tắt (Feature Toggle – công tắc chức năng), có kế hoạch rollout (triển khai thử một phần người dùng trước), và luôn nghĩ đến fallback (quay về trạng thái trước nếu lỗi).
**5. Tham gia test sớm – mindset “test từ đầu” (Shift-left testing)**
Nếu đợi đến khi Dev code xong rồi mới check thì đã quá muộn.
BA nên tham gia review test case cùng QC, confirm lại từng luật nghiệp vụ có test chưa. Thấy rule nào dễ gây hiểu lầm → viết lại, bổ sung ví dụ luôn.
**6. Sau khi release – BA vẫn chưa xong việc**
CI/CD chạy xong không có nghĩa là BA được “thoát trách nhiệm”.
BA cần theo dõi hệ thống có hoạt động đúng như logic đã phân tích không, đọc log (ghi chú lỗi), theo dõi số liệu (conversion rate, error rate…), hợp tác xử lý hotfix nếu logic sai hoặc test chưa đủ case.
Đôi khi bạn sẽ là người giải thích lý do logic fail chứ không phải Dev.
■ **Checklist dành cho BA trong team dùng CI/CD**
- Logic rõ ràng, có thể test được chưa?
- Đã mapping rule → test case chưa?
- Có viết bảng tình huống ví dụ chưa?
- Chia tính năng thành phần nhỏ dễ kiểm thử chưa?
- Có fallback, toggle, rollout strategy chưa?
- Sau khi release, có theo dõi phản ứng của hệ thống không?
■ **Một ví dụ tốt – khi BA làm đúng, CI/CD chạy mượt**
Tính năng: tặng 100 điểm khi khách đánh giá 5 sao.
BA mô tả rất rõ:
- Đơn phải được giao thành công.
- Mỗi đơn chỉ được tặng điểm một lần.
- Nếu đơn bị hủy → thu hồi điểm.
- Mỗi khách chỉ được tặng một lần/ngày.
Dev viết code đúng. QC viết test đầy đủ. CI/CD build – test – deploy → chạy mượt.
Tính năng thành công. Không lỗi. Không support production.


---

## DAY 68/100 — SCOPE ĐÃ NOTE RÕ MÀ VẪN ĂN BUG OAN – VÌ KHÁCH KHÔNG ĐỌC HAY VÌ MÌNH CHƯA LÀM TỚI?

*Trang 165–166*

Mấy hôm nay inbox đổ về nhiều, đủ thể loại tình huống dở khóc dở cười. Và câu hỏi được chọn hôm nay là một case rất kinh điển của anh em BA làm outsource, khi mà mình demo kỹ càng, báo cáo đầy đủ, nhưng khách… vẫn không công nhận là đã xong.
❓ **Câu hỏi**
Anh ơi, em nhờ góp ý chút. Em là BA outsource, mỗi tuần em đều chuẩn bị slide tóm tắt update trước buổi demo, ghi rõ phần nào đã làm – phần nào chưa. Nhưng khách không để ý, nghe phiên dịch không sát, đến lúc test lại báo bug mấy cái em đã note rõ là chưa làm, rồi còn dí thêm yêu cầu mới.
Vấn đề là PO, CTO ban đầu có họp, nhưng giữa chừng vắng mặt, chỉ còn QC và Designer vô test – mà họ lại không nắm scope hay timeline. Họ cứ test tổng thể rồi bảo team làm thiếu hoặc bug. Có cách nào tối ưu quy trình bàn giao và quản kỳ vọng tốt hơn không anh?
💡 **Trả lời**
Chào em, nghe xong là thấy… quen quen. Đây là một trong những case kinh điển của BA khi làm outsource cho khách hàng “không có thời gian” nhưng lại có rất nhiều đòi hỏi. Anh sẽ chia sẻ lại góc nhìn và cách xử lý như sau.
✖ **Trạng thái hiện tại**
Demo không được nghe: em có chuẩn bị rất kỹ, nhưng khách không nghe – hoặc phiên dịch không hiểu.
Scope bị hiểu sai: dù đã note rõ, nhưng vẫn bị hỏi “Sao chưa có cái này?”.
Người test không phải người tham gia từ đầu, nên test “toàn cảnh”, không hiểu phân chia sprint.
Kết quả: em giao xong nhưng không được công nhận là xong, bị dí feature, bị gán bug oan, mất sức, mất uy tín, mất tinh thần.

■ **Hướng xử lý để quản lý kỳ vọng tốt hơn**
**Dùng công cụ thay cho trình bày – giảm lệ thuộc phiên dịch**
Đừng kỳ vọng khách sẽ nghe kỹ trong họp, nhất là khi có rào cản ngôn ngữ.
Thay vì chỉ nói miệng, hãy gửi trước một file Release Note đơn giản bằng tiếng Anh, dạng checklist rõ ràng:

🧩 Module: Review
✔ Đã làm:
- User có thể viết review sau khi mua hàng
- Admin đã xem được review
✖ Chưa làm (ghi rõ): Admin chưa xóa được review → sẽ làm ở Sprint 3
📌 Gửi file này trước một ngày demo. Phần nào chưa làm thì bôi đậm, tô màu cho dễ thấy. Vừa giúp phiên dịch nói sát ý, vừa là bằng chứng đã cảnh báo từ đầu, không ai nói “không biết” được nữa.
**Ghim scope từng sprint và bám sát**
Làm rõ phần nào nằm trong sprint hiện tại, phần nào là của sprint sau.
Khi họ test tổng thể, em gửi lại scope đã chốt từ trước, highlight rõ: “Phần chưa nằm trong scope, sẽ làm ở Sprint 3 theo plan ngày xx/yy.”
Anh thường trình bày tiến độ theo dạng bảng này (dễ hiểu, dễ nhìn, không cãi được):
Tính năng | Sprint | Trạng thái
**Dán scope vào đầu mỗi buổi họp**
Ở slide đầu tiên mỗi buổi demo, đặt một dòng duy nhất thật to và rõ:
“This demo only covers Sprint 2 scope as defined below. Items in Sprint 3 are not included yet.”
Em lặp lại câu này mỗi lần bắt đầu. Phiên dịch cũng dễ theo hơn. Khách dù bận vẫn nghe câu đầu là đủ.
**Cách xử lý khi bị test vượt scope**
Nếu khách test tính năng chưa tới, em đừng phản ứng bằng giải thích, mà dùng đúng tài liệu đã gửi từ đầu: “As noted in the Release Checklist sent yesterday, ‘delete review’ is not yet implemented. It’s planned for Sprint 3.”
Quan trọng là trả lời theo hướng có kế hoạch rõ ràng, chứ không phải “chưa làm được”.
**Gắn người đúng vào vai trò quyết định**
Tình huống em gặp là PO/CTO không dự họp, đến lúc final thì phán xét.
Giải pháp: sau mỗi buổi demo, gửi lại biên bản hoặc tóm tắt tiếng Anh đơn giản cho PO/CTO, có checklist trạng thái. Có thể dùng email, hoặc chat, miễn là có bằng chứng.

Chúc em không bị đổ lỗi vì những cái đã nói từ lâu mà không ai chịu nghe, và giữ được sự điềm tĩnh khi cả team bị dội bom bởi người không đọc timeline.


---

## DAY 69/100 — KHI NGƯỜI DÙNG CHỈ THAO TÁC BẰNG MỘT TAY – VÀ BÀI HỌC DESIGN THINKING CHO BA

*Trang 167–168*

Không phải lúc nào người dùng cũng rảnh rỗi, ngồi ngay ngắn, hai tay đặt đúng vị trí, tinh thần ổn định, và ánh sáng hoàn hảo.
Có những lúc vì lý do nào đó họ chỉ có một tay để thao tác. Tay còn lại đang làm gì – ta không rõ. Và cũng không cần biết.
Nhưng nếu bạn làm sản phẩm, nếu bạn là BA, bạn cần quan tâm. Và đó là lúc Design Thinking thật sự được kích hoạt.
💡 **Design Thinking là gì?**
Là cách tiếp cận sản phẩm bắt đầu từ sự thấu cảm người dùng, đi qua việc hiểu đúng vấn đề, rồi từ đó thiết kế giải pháp phù hợp với hoàn cảnh thật.
Nói đơn giản: Design Thinking không bắt đầu từ “chúng ta muốn gì”, mà từ “người dùng đang gặp chuyện gì?”.
Và nếu người dùng của bạn chỉ thao tác được một tay, đang dùng app trong điều kiện không lý tưởng, thì đừng thiết kế như thể họ đang ngồi tại bàn làm việc, chuột bên cạnh, tâm trí sẵn sàng, mạng mạnh mẽ.
UX không chỉ phục vụ “người dùng tiêu chuẩn” – đôi khi, nó cần hỗ trợ cả những người dùng đang trong tình huống khó thao tác.
Đó là lý do giao diện mobile cần bắt đầu từ một câu hỏi rất cơ bản:
“Nếu người dùng chỉ có một tay để dùng – ngón cái của họ chạm được đến đâu?”

📱 **Mobile – điều khiển thuận tay**
Tất cả nút chức năng quan trọng được gom về phía bên trái màn hình. Vì nhiều người dùng thao tác bằng tay trái – tay còn lại không tiện sử dụng.
UX tốt là UX hiểu tay nào đang rảnh, không phải tay nào thuận.
💻 **Desktop – ưu tiên phím tắt**
Rê chuột đôi khi mất thời gian, đặc biệt khi người dùng cần chuyển tab nhanh.
Tổ hợp phím trở thành công cụ giải cứu:
Alt + Tab → chuyển tab
Esc → tắt nhanh
Một cú nhấn đúng lúc có thể cứu cả trải nghiệm.

🔇 **Âm thanh mặc định tắt – chỉ bật khi có tai nghe**
Không phải lúc nào người dùng cũng sẵn sàng nghe nội dung ngay lập tức.
App nên mặc định phát trong im lặng. Nếu có tai nghe, hệ thống tự động bật tiếng.
Sản phẩm tốt là sản phẩm không gây bất ngờ ngoài ý muốn.

■ **Offline mode – dành cho nơi mạng yếu**
Có những không gian không tiện kết nối: tầng hầm, thang máy, nơi riêng tư.
App nên cho phép tải trước nội dung, để người dùng chủ động sử dụng bất cứ khi nào.
Không có mạng – vẫn có trải nghiệm.

● **Và có thể bạn sẽ nhận ra**
Khi bạn không còn chăm chăm hỏi “sếp muốn gì”, mà bắt đầu nghĩ đến “người dùng đang sống trong hoàn cảnh nào?”.
Khi bạn tạm gác lại bảng checklist, và bắt đầu viết lại trải nghiệm bằng sự tinh tế.
Khi bạn thật sự đặt mình vào vị trí người dùng và hỏi:
“Nếu mình là họ – mình muốn hệ thống phản ứng thế nào?”

● Nếu bạn muốn học tư duy đó – thực tế, thấu cảm, sâu sắc
Mình mời bạn tham gia mini course: “Design Thinking dành cho BA”.
Không slide màu mè, không lý thuyết khô cứng.
Chỉ có:
Những hành vi thật cần được bóc tách.
Những flow cần được viết lại đúng với đời sống.
Và những góc nhìn khiến bạn không bao giờ viết tính năng vô cảm nữa.
📌 Mình sẽ ghim link đăng ký dưới phần comment.


---

## DAY 70/100 — ĐÀO LẠI LỖI CŨ – ĐÚC RA CHUẨN MỚI CHO TEAM BA

*Trang 169–170*

✖ “Lỗi này hình như mình gặp hoài rồi mà?”
✖ “Cái bug này từng fix mà?”
✖ “Tại sao vẫn không ai rút ra được kinh nghiệm gì?”
Một lần nọ, tôi hỏi cả team BA:
“Chúng ta từng vấp gì trong dự án cũ – và liệu có ai rút ra được quy chuẩn gì không?”
Không ai trả lời. Không phải vì không nhớ, mà vì… chưa bao giờ ngồi lại để review nghiêm túc.

✖ **Sai lầm phổ biến trong team BA**
Không ghi lại lỗi BA từng gây ra. Sau mỗi dự án chỉ gửi tổng hợp qua email, rồi move on. Không phân tích nguyên nhân gốc: lỗi là do không hỏi kỹ, do giải pháp chưa match use case, hay do assume sai từ đầu? Không biến sai lầm thành guideline. Sai lặp lại ở 2–3 dự án, nhưng checklist thì vẫn rỗng.

■ **Đừng chỉ “nhìn lại cho biết” – Hãy “rút ra để đổi cách làm”**
Nhiều team BA sau dự án chỉ wrap-up cho có, rồi… xếp góc. Lỗi thì lặp lại, còn process thì không tiến hoá.
Cái thiếu không phải là buổi họp, mà là hành động biến sai lầm thành tài sản dùng chung.
Muốn BA team lên trình, thì mỗi lần sai phải để lại một dấu hiệu nhận biết và cách ứng phó cụ thể, để không ai khác phải “trả giá học lại bài cũ”.

■ **Cách tổ chức buổi “Review sai lầm – Rút quy chuẩn”**
● Mục tiêu: không phải tìm ai sai, mà là tìm cách để cả team không lặp lại nữa.
Bước 1: Gửi form trước họp. Gợi ý nội dung form:
- Mô tả lỗi bạn từng gây ra (ngắn gọn, cụ thể)
- Hậu quả là gì? (ảnh hưởng DEV/TEST/USER)
- Bạn nghĩ vì sao lỗi đó xảy ra?
- Có quy chuẩn nào có thể ngăn lỗi đó không?
Bước 2: Họp review – Giữ tinh thần “không blame”
Mở đầu bằng một câu rất rõ: “Buổi này không phải để chỉ trích – mà là để bóc tách sai lầm, tìm ra quy chuẩn tốt hơn cho dự án sau.”

Bước 3: Mỗi người trình bày 1 lỗi – cả team phân tích
Ví dụ:
Lỗi: Flow duyệt không đầy đủ → DEV hiểu sai, QA trả về.
Nguyên nhân: assume user chỉ duyệt 1 bước.
Giải pháp rút ra: từ nay tất cả UC phải có Exception flow.
Bước 4: Ghi nhận vào bảng tổng hợp lỗi.
Bước 5: Rút nguyên nhân sâu bằng sơ đồ xương cá (Fishbone)
Dùng khi muốn truy nguyên tận gốc, không chỉ chạm bề mặt.
Ví dụ lỗi: tính năng triển khai sai logic nghiệp vụ.
Dán giấy A3, vẽ sơ đồ Fishbone theo 6 nhánh:
- Con người (People): BA mới, thiếu kinh nghiệm?
- Tài liệu (Document): thiếu Exception Flow, rule viết chung chung?
- Phương pháp (Method): không có checklist review, không trace CR?
- Công cụ (Tool): không có nơi lưu CR, không log lại assumption?
- Giao tiếp (Communication): không recap với DEV, không hỏi rõ SME?
- Môi trường (Environment): deadline quá gấp, không đủ thời gian test?
Từ đó, nhóm được nguyên nhân gốc để quyết định:
■ Viết thêm checklist gì?
■ Cập nhật template nào?
■ Bổ sung slot nào vào quy trình?

Bước 6: Cập nhật tài sản tri thức
- Update checklist hoặc UC template.
- Dán vào wiki.
- Nhắc lại trước sprint mới.

📌 “Sai lầm là tài sản – nếu ta biết rút ruột nó thành quy chuẩn.”

💬 Bạn có từng gặp lỗi nào trong team BA mà cứ lặp đi lặp lại hoài? Hoặc từng tổ chức buổi review nào “rất quyết tâm” nhưng cuối cùng chẳng đọng lại gì?
Cứ thoải mái chia sẻ một lỗi mà bạn từng rút ra được bài học thật sự – biết đâu lại giúp thêm nhiều team khác tránh được một pha “toang không cần thiết”.


---

## DAY 71/100 — HỌ VẪN ĐI HỌP. VẪN NHẬN TASK. NHƯNG HỌ ĐÃ RỜI ĐI TỪ RẤT LÂU RỒI.

*Trang 171–172*

“Em không nghỉ vì lương. Em nghỉ vì mỗi sáng mở Jira ra, em không biết mình đang làm điều này… cho ai nữa.”
Có những sự rời đi không kèm theo giận dữ, không có va chạm. Chỉ là… họ không còn lý do để tiếp tục gắn bó.
Không phải vì công ty tệ.
Không phải vì sếp ép.
Mà vì… họ không còn tin sản phẩm này có ý nghĩa.
🔋 **Có những cái mệt không đến từ việc nhiều**
Mà đến từ việc… không còn thấy mình tạo ra điều gì đáng để làm.
Viết tài liệu cho một tính năng biết trước sẽ bị đổi.
Thảo luận logic cho một thứ không ai quan tâm người dùng nghĩ gì.
Ra mắt dashboard để “check done”, rồi không ai dùng.
Fix bug trong khi vấn đề gốc… ai cũng né.
Mỗi ngày như một vòng lặp: làm cho đúng – rồi quên.
🧩 **Nhiều nơi gọi mình là làm Agile. Nhưng…**
Sprint thì đều, nhưng buổi phân tích thì ai cũng mong sớm xong để về làm task.
Daily thì vẫn có, nhưng không ai dám nói điều mình thật sự lo.
Và đến khi có lỗi, câu cửa miệng bật ra là:
- “BA có viết rõ chưa?”
- “SRS chốt chưa?”
- “Diagram chưa có, sao test được?”
Không ai sai. Ai cũng đang cố làm phần của mình cho đúng – và đủ. Nhưng… không còn ai nhìn về người dùng. Agile dần biến dạng. Thay vì cùng tiến hoá theo nhu cầu sản phẩm, mọi người bắt đầu dựng rào chắn bằng tài liệu – để phòng thân.
● **Agile không chết vì thiếu sprint**
Agile chết vì không ai còn tin nhau – và không ai còn tin sản phẩm.
📌 **Một sản phẩm “đúng” không nằm trong quy trình. Nó nằm ở chỗ:**
Có người thật dùng nó.
Có vấn đề thật được giải quyết.
Có đội ngũ thật sự tin mình đang làm điều nên làm.

Cuối tuần rồi
Nếu ai đó đang nằm nhìn trần nhà và nghĩ: “Mình làm tất cả thứ này… để làm gì vậy?”
Thì có lẽ… đã đến lúc dừng lại một nhịp. Không phải để bỏ. Mà để nhắc mình lý do bắt đầu.
🔚 **Nhưng một mình BA thì không đủ**
Một mình hỏi “nghiệp vụ thật sự là gì”.
Một mình giữ user trong đầu khi cả phòng đang push deadline.
Một mình gồng để “giữ logic sản phẩm” giữa những dòng SRS bị đọc như tài liệu bảo hiểm… thì sớm muộn cũng cạn.
✦ **Muốn sản phẩm sống lại, không cần cả team lột xác**
Chỉ cần một người ngừng hỏi “viết chưa?”, và bắt đầu hỏi lại: “Viết cái này… cho ai?”
Chỉ cần một DEV bỏ qua một bước phòng thủ và hỏi: “Nếu user thao tác thế này thì có ổn không?”
Chỉ cần một TEST dừng một dòng test case và hỏi: “Flow này đã rõ pain point người dùng chưa?”
Chỉ cần một người quản lý dám bảo vệ quyết định vì người dùng – thay vì “sếp bảo vậy”.
💬 **Một mình BA không gánh nổi sản phẩm**
Nhưng BA có thể là người châm lại ngòi lửa của sự tử tế với user. Không phải bằng mấy cuộc họp hoành tráng. Mà bằng những câu hỏi nhỏ, gọn, nhưng thật. Và nếu bạn hỏi:
“Liệu có ai còn quan tâm sản phẩm làm ra có giúp được ai không?”
Câu trả lời là: Có.
Và có thể… họ cũng đang đợi bạn mở lời trước.
p/s: Dù mọi thứ đang rối, nếu bạn vẫn còn giữ được một câu hỏi tử tế cho người dùng – thì sản phẩm ấy vẫn còn hy vọng. Và bạn không hề đơn độc.


---

## DAY 72/100 — BA TOOLKIT COLLABORATIVE GAME – SPEED BOAT

*Trang 173–174*

Có những buổi họp mà bạn cảm nhận rõ ràng:
- DEV thì lặng thinh.
- QC thì nhìn trần nhà.
- PM hỏi: “Tại sao lại delay sprint này?”
Không ai trả lời thẳng. Chỉ có tiếng thở dài. Và rồi cái vòng lặp “im lặng – đổ lỗi – cố gắng làm cho xong” lại tiếp tục. Lúc đó, nếu bạn là BA mà chỉ hỏi: “Vướng gì thế mọi người?” thì không ai trả lời đâu. Nhưng nếu bạn vẽ ra một chiếc tàu cao tốc, đặt câu hỏi:
“Tàu của team mình đang bị kéo lại bởi những mỏ neo nào?”
Thì câu chuyện bắt đầu khác.
🚤 **Speed Boat là gì?**
Đây là một collaborative game mà BA dùng để kéo ra những rào cản đang giấu trong lòng team – thứ không ai nói thẳng ra nhưng đang âm thầm giết chết hiệu suất và tinh thần.
- Chiếc tàu là sản phẩm.
- Hòn đảo là mục tiêu team hướng tới.
- Những mỏ neo là các yếu tố khiến tàu không thể lướt nhanh – delay, lỗi lặp, cảm xúc ức chế, quy trình nhiêu khê…
🔍 **Vì sao nên dùng?**
Có những vấn đề, càng hỏi trực diện càng không ai dám nói. Nhưng khi vẽ ra hình ảnh, khi mọi người được quyền dán sticker “rào cản” thay vì “chỉ trích người”, thì bức tranh thật mới hiện ra.
Dùng kỹ thuật này khi team than:
- Tài liệu đầy đủ mà DEV vẫn làm sai.
- Test case đủ mà QA vẫn bỏ sót bug.
- Dự án đầy task mà user chẳng hài lòng.
Sau buổi Speed Boat, hoá ra:
- DEV không dám hỏi lại vì sợ bị nói là “đọc không kỹ”.
- QA không đủ test data nhưng ngại nhờ BA viết mock.
- User không hiểu bản demo, nhưng team tưởng họ OK.
Cả đống “mỏ neo” lộ diện. Không do năng lực, mà do nghi ngờ, ngại ngần, nghĩ hộ người khác.

● **Dẫn dắt buổi chơi thế nào?**
Bắt đầu từ mục tiêu.
Hỏi team: “Chúng ta đang cố gắng đưa tàu tới đâu?” → ra được mục tiêu cụ thể (ví dụ: ra mắt version A đúng ngày, tăng CSAT lên 8.5…).
Gợi ra các mỏ neo.
Yêu cầu mỗi người ghi những điều họ cho là đang kéo lùi team, ghi vào giấy hoặc sticker.
Tự do dán vào hình tàu.
Ai thấy neo nào nặng thì dán sâu hơn, ai thấy trúng ý thì dán đè.
Cùng đọc to – phân nhóm – tìm mẫu chung.
Neo kỹ thuật? Neo giao tiếp? Neo từ process? Neo do manager?
Đưa ra hành động cụ thể.
Chốt mỗi nhóm neo là một action:
- “BA sẽ dùng summary 1 trang trước khi gửi doc.”
- “DEV được quyền hỏi BA bất cứ lúc nào nếu unclear.”
- “Team thống nhất check demo với user bằng video, không chỉ bản PDF.”
✦ **Hiệu ứng sau buổi đó**
Không khí team thay đổi hẳn. Không cần training hoành tráng, không cần app mới, chỉ cần ai cũng cảm thấy mình có tiếng nói và mọi người nhìn sản phẩm như một con tàu chung – không phải mảnh đất riêng của DEV, TEST, BA.
❗ Một số sai lầm BA hay mắc khi dùng Speed Boat
Chơi để cho có, không follow-up bằng hành động.
Để buổi chơi thành nơi “kể tội” cá nhân.
Không dẫn dắt kỹ phần phân loại neo → loãng.
Không nhấn mạnh mục tiêu tàu ngay từ đầu → rơi vào kể khổ chứ không phải gỡ rối.
■ Tip thêm cho BA dùng tốt Speed Boat
Đưa team hình ảnh thật – tàu, đảo, mỏ neo. Càng hình tượng, càng dễ gợi mở.
Nếu team đông trên 8 người, chia thành nhóm 2–3 người. Mỗi nhóm tự brainstorm neo trước. Sau buổi họp, gửi lại ảnh chụp và bảng tổng hợp hành động cụ thể. Đừng để mọi thứ dừng ở mức “chơi vui phết đấy!”.
● Kết
BA không chỉ đi eliciting requirement. BA còn là người phát hiện mỏ neo, gọi tên mỏ neo, giúp tháo mỏ neo – để con tàu tiến về phía mục tiêu, thay vì lết mệt mỏi giữa deadline và blame game.


---

## DAY 73/100 — MỘT RUNNER GIỎI KHÔNG TĂNG TỐC SỚM MÀ BIẾT ĐỀU ĐẶN ĐẾN PHÚT CUỐI

*Trang 175–177*

Ở giải marathon, người ta không chạy bằng máu lửa. Họ chạy bằng pace và bằng tim.
Có những runner pace 8, tim ổn, đều đặn dừng ở mọi trạm nước. Không cố bám nhóm sub 4, không gồng. Và tới km 38, họ vẫn còn chạy.
Còn người mở đầu với pace 4, và rồi chườm đá ở trạm y tế. Chạy nhanh không khó. Chạy không gãy mới khó.
Tôi đã thấy những team phần mềm giống y như vậy.
**Sprint đầu – chạy như gió**
Dev làm mượt. QC test sạch.
BA phân tích logic chi li từng dòng. Plan 20 point, làm ra 38.
Sếp vỗ tay. Team tự tin. Scope tăng.
**Sprint sau vẫn “ráng thêm chút nữa”**
Demo dí – vẫn cười. Bug chưa fix xong – vẫn “em nhận luôn”.
Nhưng đến sprint thứ N… Dev xin nghỉ 2 ngày (đi phỏng vấn).
QC out. BA bắt đầu quên check flow phụ.
Sprint failed. “Ủa, sprint đầu chạy ngon vậy mà giờ toang?”
**Vì sao toang?**
Không ai toang vì sprint 1.
- Team toang vì nhiều sprint liên tiếp không có buffer.
- Team toang vì không có trạm nước nào.
- Team toang vì chạy 42 km mà cứ nghĩ mình đang đua 100 m.
✖ **Sai lầm chết người của nhiều team mạnh**
Sprint đầu ngon → tưởng giữ được mãi.
Không track velocity thật → chỉ nhìn số giờ.
Không chừa buffer → gặp phát sinh là sập.
Scope creep “nho nhỏ” mỗi ngày → backlog biến thành bãi mìn.
Không ai nói không → ai cũng gồng, gồng đến khi không còn nói nổi.
Tất cả diễn ra như một cuộc đua mà không ai dám dừng chân uống nước. Chỉ chạy. Và gãy.

■ **Agile Principle #8 – thứ mà ít người đủ dũng cảm để sống theo**
“Agile processes promote sustainable development. The sponsors, developers, and users should be able to maintain a constant pace indefinitely.”
Không ai nói bạn phải chạy chậm. Nhưng Agile nói rõ: bạn phải chạy được… lâu.
● **Muốn giữ pace? Nghề BA/PO phải làm pacer. Không làm cheerleader.**
Pacer là người giữ nhịp cho cả team. Không hô hào. Không gồng hộ. Chỉ lặng lẽ đi trước – đúng nhịp – đúng lượng – đúng thời điểm nghỉ.

Bốn câu hỏi sau sẽ giúp bạn biết mình đang làm pacer, hay chỉ là người “chạy ké” trong sprint:
**1. Bạn plan sprint theo velocity thật, hay theo “cảm giác tin tưởng”?**
Sprint trước làm được 25 → sprint này cứ đẩy 28 cho tròn số?
Bạn đang đốt năng lượng giai đoạn đầu và tự đặt bẫy sprint sau.
● Một pacer thật sự sẽ nói:
“Ba sprint gần nhất dao động từ 20–22. Sprint này có demo và một bug tồn → Plan 18–19 là hợp lý.”

**2. Bạn có để buffer, hay sprint nào cũng căng như dây đàn?**
Buffer không phải xa xỉ phẩm. Nó là trạm nước trong cuộc đua 42 km.
■ Không chừa 20% buffer = không có không gian xử lý bất ngờ.
Không có trạm nước = đến km 30 sẽ không còn ai đủ sức chạy.

**3. Khi scope creep xuất hiện – bạn xử lý hay nhắm mắt?**
Mỗi lần ai đó nói “chỉnh nhẹ cái logic”… bạn gật đầu?
✦ Một pacer sẽ hỏi: “Ok, vậy mình dời task A hoặc B sang sprint sau để QA còn đủ thời gian test. Đồng ý chứ?”

**4. Retro của bạn có action không, hay chỉ ‘mệt ghê – cố sprint sau’?**
Retro là nơi chỉnh nhịp, không phải nơi than thở rồi để sprint sau lặp lại y chang.
■ Pacer sẽ chốt: “Sprint sau: task nào chưa có DONE rõ ràng sẽ không vào board. BA và QA review checklist trước.”

● **Kết luận của một người đã từng chạy gãy sprint**
Không ai nhớ bạn gánh mấy point. Không ai ghi công bạn làm 10h tối.
Chỉ có hai câu hỏi sau cùng:
→ Sản phẩm còn dùng được không?
→ Team còn ai?
Và câu trả lời phụ thuộc vào pace bạn giữ được trong suốt cuộc đua.

● Kết lại
Sản phẩm không chết vì làm chậm.
Sản phẩm chết vì cả team lao đầu chạy mà không ai giữ nhịp.
Bạn có thể sprint một lần, hai lần. Nhưng không ai sprint nổi cả quý.
Và không ai đáng phải gãy chỉ vì không được quyền nói: “Nghỉ chút đã.”
Làm sản phẩm cũng như chạy marathon – không có trạm nước, không có buffer, không ai về được đích.


---

## DAY 74/100 — KHI BẠN VIẾT TÀI LIỆU NHƯNG NGƯỜI KHÁC LẠI ĐIỀU PHỐI, CÒN DEV THÌ KHÔNG THÈM ĐỌC

*Trang 178–180*

Đã gần một tuần rồi tôi không viết. Không phải vì bí ý tưởng – mà vì viết rồi lại xoá.
Gõ được nửa bài, lại thấy không đủ sâu, không đủ chất, không đủ “đáng để đọc” – thế là tôi bỏ. Off luôn. Để series tạm lặng vài hôm.
Vài ngày trước, vào lúc 2h sáng, tôi nhận được tin nhắn:
“Em chào anh, em theo dõi series 100 ngày của anh và mong được anh tư vấn ạ.
Hiện em bị dev trong team nghi ngờ năng lực, có người nói ‘cậu không hiểu hệ thống’ và không đọc tài liệu em viết dù đã được khách hàng chốt.
Một chị BA khác thường chen ngang khi em trao đổi với dev, nói to và được dev nghe theo dù không trực tiếp viết tài liệu.
Em hiền nên thường nhường lời, nhưng lại bị xem là yếu. Em muốn lấy lại vai trò BA chính và sự tin tưởng từ dev mà chưa biết nên xử lý thế nào. Mong anh chia sẻ giúp em. Em cảm ơn anh!”
OK, giờ vào việc luôn thôi.
🔍 **1. Phân tích tình huống của em**
Em đã lấy yêu cầu từ khách hàng, viết tài liệu, gửi khách hàng review và chốt, bàn giao cho dev.
Làm đúng bài bản. Nhưng sau đó, dev lại nói:
“Cậu không hiểu hệ thống này làm gì.”
“Tớ không cần đọc tài liệu của cậu, tớ hiểu rồi.”
Đồng thời:
Chị BA khác chen vào khi em trao đổi. Chị ấy thường nói to, hùng hồn, có lúc sai, có lúc đúng. Em hiền, không ngắt lời, để chị ấy nói hết rồi mới sửa. Dev ngày càng nghiêng về chị ấy, đẩy em ra khỏi vai trò BA chính. Em bị giao nhiệm vụ ghi chép, dù chính em là người viết tài liệu.
✦ **2. Gốc rễ vấn đề – em đang mất vai trò điều phối**
Em không sai về chuyên môn. Nhưng em đang: Không làm chủ không gian trao đổi. Không cắt được nhiễu từ người chen ngang. Không phản ứng lại khi các bạn dev xử lý không chuyên nghiệp. Không “định hình lại vai” của mình trước team.
Đây không phải lỗi cá nhân. Đây là kỹ năng “giữ thế trận” – thứ một BA cần rèn nếu muốn dẫn dắt được hệ thống thay vì bị cuốn theo.

● **3. Hệ quả nếu không xử lý sớm**
Bị “hạ cấp ngầm” → chỉ còn là người ghi chép.
Dev không theo tài liệu → hệ thống lệch logic.
Không kiểm soát được trao đổi → hệ thống thiếu nhất quán.
Người không chịu trách nhiệm viết tài liệu lại dẫn dắt logic – gây rủi ro khó truy vết.
Đây không còn là mâu thuẫn cá nhân. Đây là dấu hiệu rối hệ thống vì thiếu người cầm nhịp.

● **4. Cách xử lý từng tình huống**
■ Khi dev nói “cậu không hiểu hệ thống”
Sau khi lấy yêu cầu và viết bản nháp → luôn có một buổi review nghiệp vụ với Tech Lead hoặc SA:
Chốt khả năng xử lý.
Ghim các ràng buộc hệ thống.
Làm rõ logic phức tạp hoặc những chỗ cần “bẻ flow” vì technical constraint.
Ghi rõ trong tài liệu (hoặc recap mail): “Luồng này đã được confirm với khách hàng vào ngày [xx], và đã review khả năng triển khai với Tech Lead [Tên] trong buổi ngày [yy].”
Chỉ cần một câu này – dev không thể nói “không hiểu hệ thống” mà không “đụng” Tech Lead.
Khi bàn giao cho dev: “Đây là bản đã được align giữa nghiệp vụ và kỹ thuật. Nếu thấy điểm nào chưa rõ hoặc có vấn đề kỹ thuật, anh/chị comment vào file giúp để mình cùng Tech Lead thống nhất điều chỉnh.”
■ Khi dev từ chối đọc tài liệu
Xử lý tuỳ độ căng: “Em hiểu là mình có thể nhớ flow cũ, nhưng nếu không đọc lại tài liệu đã chốt thì đang tranh luận theo trí nhớ cá nhân. Mà hệ thống không chạy theo trí nhớ – nó chạy theo cái đã confirm giữa BA, khách hàng và kỹ thuật rồi ạ.”
Đặt trách nhiệm lên dev một cách logic – không xúc phạm: “Không đọc = không có tư cách phản biện.”
Khẳng định rõ mục đích tài liệu: Không phải “file mô tả màn hình” – mà là base pháp lý của hệ thống.

■ Xử lý chị BA chen ngang
Ngay khi chị ấy chen ngang, không để yên. Nói ngay:
“Chị cho em xin phép điều phối buổi này, vì em đang là người tổng hợp và cập nhật toàn bộ tài liệu nghiệp vụ. Nếu có điểm nào cần bổ sung, mình cùng note lại và thảo luận sau để tránh đứt mạch.”
Đây là cách “cắt lời chuyên nghiệp” – không xúc phạm, nhưng giữ quyền điều phối.
■ Chốt vai trò với team lead để được ‘thực hiện role BA đúng cách’
Gửi mail hoặc gặp riêng leader, với tone cầu thị nhưng có thông điệp:
“Dạo gần đây em thấy việc dev không follow tài liệu, và một số người không viết tài liệu lại can thiệp vào logic nghiệp vụ khiến hệ thống có nguy cơ lệch chuẩn. Em xin phép được đứng ra điều phối toàn bộ phần flow nghiệp vụ đã chốt. Nếu team thấy cần, em sẽ tổ chức thêm session để đảm bảo mọi người hiểu đúng trước khi triển khai.”
Không kể tội.
Không vạch mặt.
Nhưng truyền thông mạnh rằng: “Em đang giữ logic – không phải vai phụ.”
💡 Bài học: BA không cần nói to – nhưng cần nói có trọng lượng
Vị thế không tự có – mà phải giữ bằng kỹ năng, logic, và chiến lược.
Không ai giao quyền BA cho bạn – bạn phải thể hiện để giữ được vai.
Người nói to hơn chưa chắc đúng hơn.
Người không đọc tài liệu thì không thể phản biện đúng cách.
● Lời nhắn cuối
Bạn đã từng bị gạt ra rìa khi làm đúng? Comment chia sẻ tình huống của bạn, tôi sẽ chọn lọc và trả lời trong các bài sau.
Một số tình huống tôi sẽ viết tiếp:
Tester hiểu sai vì không bám case.
PM bảo “cứ làm theo kế hoạch”, khách hàng thì thay đổi liên tục.
BA junior muốn “lên tiếng” nhưng sợ bị nói là thiếu kinh nghiệm.


---

## DAY 75/100 — CÓ MỘT TEAM BA NỌ – VIẾT TÀI LIỆU RÕ RÀNG, NHƯNG VẪN BỊ SẾP CHÊ THIẾU

*Trang 181–183*

“Anh tưởng tài liệu xong là dev hiểu được hết chứ?”
“Chị thấy tính năng đơn giản thôi, sao tài liệu tới 10 trang?”
Team BA đó không phải lần đầu làm nghề. Họ có checklist, có mẫu chuẩn, có flow, có rule, có cả mapping API. Họ làm đủ. Nhưng vẫn… chưa đúng – theo định nghĩa của sếp. Mọi chuyện bắt đầu từ những cuộc họp lưng chừng. Sếp giao việc bằng miệng:
“Làm giống bên XYZ là được.”
Khi nhận tài liệu, sếp phản hồi: “Anh thấy chưa đủ sâu.”
Nhưng khi hỏi lại:
“Đủ là tới đâu ạ?” – thì câu trả lời vẫn mơ hồ:
“Cứ làm sao để dev nó hiểu là được.”
Team bắt đầu mơ hồ không chỉ về yêu cầu, mà còn mơ hồ cả về đích đến. Viết cho ai? Viết để review, hay để bàn giao, hay để lưu trữ audit? Không ai xác định rõ. Nhưng kỳ vọng thì vẫn cứ tăng.
✖ **Khi kỳ vọng không rõ ràng – thì output nào cũng bị chê**
Viết kỹ → bị than dài.
Viết ngắn → bị chê thiếu logic.
Làm bản đẹp → sếp nói màu mè.
Làm bản thô → sếp bảo không chuyên nghiệp.
Không phải vì làm sai. Mà vì chưa quản lý được kỳ vọng của người đánh giá.
■ **Team rút ra 4 bài học – không từ sách vở, mà từ những lần làm chưa tốt phải rework**
**1. Không để sếp tự tưởng tượng output**
Ngay khi nhận task, họ gửi 3 phương án output rõ ràng:
Tính năng mới: Use Case + UI + Flow logic.
Nâng cấp: Bảng so sánh hiện tại – đề xuất + impact phân tích.
Tích hợp: API spec + mapping + rule xử lý lỗi.
Ví dụ: sếp bảo làm “form đặt lịch đơn giản thôi” → Team hỏi: “Anh cần bản demo cho khách, hay bản dev backend?” Nhờ vậy, sếp chọn đúng combo – lần đó không ai bị chê.

**2. Gắn nhãn tài liệu – tránh hiểu lầm**
Tài liệu bị đọc sai mục đích là thảm hoạ. Họ gắn nhãn từ đầu:
[Review only] – xác nhận logic.
[Ready for Dev] – đầy đủ rule + mapping.
[Quick Note] – thảo luận nội bộ.
Sếp từng bảo “thiếu flow lỗi” ở bản review. Team phản hồi: “Dạ bản này để chốt logic. Exception tụi em bổ sung trong bản dev-ready.” Một dòng nhãn rõ – tiết kiệm nửa ngày tranh luận.
**3. Giới hạn rework bằng dữ liệu, không than thở**
Team bắt đầu log:
- Bao nhiêu tài liệu bị sửa do yêu cầu đổi?
- Bao nhiêu feedback đến sau deadline?
- Bao nhiêu bản bị góp ý sai do đọc nhầm mục đích?
Sau 2 tháng, họ báo cáo:
“Tuần 6: Yêu cầu đổi 3 lần trong 4 ngày → gây rework 9h BA, delay 6h DEV.”
Không đổ lỗi. Chỉ để chỉ ra rằng: nếu muốn output tốt, thì điểm chốt cũng cần rõ ràng.
**4. Không chống lại kỳ vọng – mà cụ thể hoá để thương lượng**
Sếp nói: “Tài liệu phải dễ hiểu.”
→ Họ hỏi: “Dễ theo hướng ngắn gọn, hay có flow hình ảnh?”
Sếp bảo: “Đừng làm dài dòng.”
→ Họ đề xuất: “Một bản mô tả nhanh để review, một bản đầy đủ cho dev.”
Không ai nổi nóng.
Không ai nhún nhường.
Chỉ là biến lời nói cảm tính thành cấu trúc có thể thống nhất.

💡 **BA Lead không chỉ là người giỏi viết**
Mà là người dẫn dắt cách sếp hiểu và đánh giá output của team. Ngoài 4 kỹ thuật trên, một BA Lead còn cần làm thêm 3 điều:
**1. Thiết lập working agreement từ đầu dự án**
Lịch gửi tài liệu – thời hạn phản hồi.
Cách review: họp hay comment?
Phiên bản nào là bản chính để dev triển khai?
→ Làm rõ ngay từ đầu để không có chuyện “anh tưởng”, “em không biết”.

**2. Biết giới hạn – nhưng không né trách nhiệm**
Ví dụ, khi được yêu cầu viết test case thay cho tester, họ phản hồi:
“Tụi em sẽ hỗ trợ walkthrough logic và confirm rule.
Còn phần viết test case chi tiết, mình nên phân công nhóm kiểm thử để đảm bảo đúng kỹ năng và đúng tiến độ.”
Không làm thay. Nhưng vẫn hỗ trợ có trách nhiệm.
**3. Tổ chức retro nội bộ – học từ feedback**
Lập danh sách feedback thường gặp.
Phân loại: đúng – sai – mơ hồ.
Tạo checklist phản hồi ngược khi nhận task mới.
→ Biến mỗi góp ý thành nguyên liệu cải tiến.

■ **Kết**
Một BA Lead không chỉ quản lý task – mà là người thiết kế cách mọi người hiểu, đánh giá, và tin tưởng vào giá trị của tài liệu phân tích.
Kỹ năng viết là nền.
Kỹ năng định hình kỳ vọng – mới là thứ giúp BA Lead bảo vệ giá trị của team trong môi trường đầy cảm tính.

✍️ Nếu bạn từng bị đánh giá sai vì output không đúng với kỳ vọng mơ hồ – bạn không đơn độc. Và nếu bạn đang là BA Lead, hãy giúp team của mình vững vàng bằng tư duy, không chỉ bằng câu chữ.


---

## DAY 76/100 — CÁC THÔNG SỐ NON-FUNCTIONAL BA CẦN BIẾT

*Trang 184–186*

Trong một hệ thống bất kỳ, dù nghiệp vụ có mượt đến đâu, chỉ cần một thông số kỹ thuật bị bỏ qua cũng đủ khiến trải nghiệm người dùng bị gãy.

Non-Functional Requirements (NFR) không phải phần “dành cho dev lo sau”, mà là xương sống để hệ thống chịu được áp lực thật: khi người dùng đông, khi có lỗi mạng, khi xử lý chậm, hoặc khi cần bảo vệ dữ liệu.

Dưới đây là 6 nhóm thông số mà BA nào cũng cần nắm rõ.

**1. Timeout – Giới hạn thời gian chờ tối đa cho một yêu cầu**

Khi hệ thống gọi đến một dịch vụ – ví dụ kiểm tra điều kiện khuyến mãi – nhưng bên kia chưa phản hồi, thì đến lúc nào hệ thống nên ngừng chờ và coi như lỗi?

Nếu không xác định timeout rõ ràng, hệ thống sẽ đứng hình, gây treo giao diện, thậm chí lock tài nguyên backend.

Timeout phổ biến (mang tính tham khảo):

Dưới 3 giây với thao tác đơn.

10–15 giây với xử lý lô hoặc thao tác cần backend xác thực chéo.

👉 Không có timeout = hệ thống đứng chờ vô hạn → trải nghiệm “lì đòn”, không rõ trạng thái, dễ mất dữ liệu do người dùng thao tác lại.

**2. Latency – Thời gian trễ từ khi gửi yêu cầu đến khi nhận phản hồi**

Ví dụ: một người dùng nhấn “Xác nhận”, và thấy phản hồi sau 3 giây – liệu đó là ổn hay chậm?

Latency ảnh hưởng trực tiếp đến cảm giác mượt.

Ứng dụng cần phản hồi nhanh (đặt hàng, xác thực mã, thanh toán...) → latency nên <1 giây.

Giao diện thông tin → có thể chấp nhận 2–3 giây.

👉 Không đặt ngưỡng latency rõ ràng, không phân loại dịch vụ cần real-time, hệ thống có thể phản hồi chậm mà vẫn “hợp lệ”, tạo ra sự bực bội tích tụ nơi người dùng.

**3. Retry – Cơ chế thử lại nếu request thất bại**

Khi gửi thông tin qua mạng (ví dụ gọi API đến một hệ thống khác), luôn có xác suất thất bại: do mất mạng, nghẽn server, hoặc lỗi tạm thời.

Nếu không có retry → chỉ cần lỗi một lần là yêu cầu bị bỏ.

Nếu retry quá nhiều → hệ thống sẽ quá tải.

Nếu retry sai logic → có thể gây trùng giao dịch (gửi 2 đơn hàng, 2 email, 2 lần trừ tiền).

Một retry hợp lý thường:

Giới hạn 2–3 lần.

Cách nhau 2–5 giây.

Chỉ áp dụng với thao tác idempotent (gọi lại không gây tác dụng phụ).

👉 BA cần chỉ rõ có retry không, khi nào retry, và logic xử lý sau khi retry thất bại hoàn toàn.

**4. Security Requirements – Yêu cầu bảo mật hệ thống**

Đây là nhóm thường bị BA bỏ qua hoặc viết rất sơ sài kiểu: “Hệ thống phải đảm bảo an toàn thông tin.”

Nhưng cụ thể là gì? Một vài yêu cầu bảo mật tối thiểu cần làm rõ:

Authentication (Xác thực)
- Hệ thống dùng gì để xác thực? Username/password, OTP, SSO, vân tay?
- Nếu dùng OTP thì thời hạn bao lâu? Có giới hạn số lần gửi lại không?

Authorization (Phân quyền)
- Người dùng có phân quyền không? Có phải kiểm tra vai trò trước khi hiển thị nút?
- Có quyền thao tác theo từng trường hợp không? (ví dụ: chỉ người tạo mới được sửa)

Encryption (Mã hóa)
- Dữ liệu lưu trữ (database, log) và truyền tải (API) có được mã hóa không?
- Mã hóa dùng thuật toán nào (AES256, SHA256...), áp dụng ở đâu?

Audit & Logging (Kiểm toán & ghi log)
- Hành động nào cần ghi log? Log được lưu bao lâu?
- Có cần chức năng xem lịch sử thao tác không?

👉 Nếu không làm rõ nhóm này, hệ thống ra đời có thể lộ thông tin người dùng, bị thao túng quyền, không truy vết được lỗi, và không đủ điều kiện tuân thủ bảo mật (ISO, GDPR...).

**5. CCU (Concurrent Users) – Số người dùng đồng thời**

Một hệ thống có thể có 1 triệu user đăng ký, nhưng nếu chỉ 100 người dùng đồng thời thì thiết kế khác xa với hệ thống có 10.000 người truy cập cùng lúc.

BA cần hỏi: Khi nào là peak time?

Tình huống nào có thể tạo đột biến số lượng người dùng?

Có cần giới hạn session login đồng thời không?

👉 Không ước lượng CCU sẽ khiến dev và hạ tầng đánh giá thấp khả năng chịu tải, dẫn đến vỡ trận, timeout hàng loạt, hoặc bị chặn kết nối ngoài mong muốn.

**6. TPS (Transactions Per Second) – Số lượng giao dịch mỗi giây**

Khác với CCU, TPS đo chính xác khối lượng hành động thực sự được xử lý mỗi giây – như số đơn hàng tạo mới, số lần gọi API thanh toán, số email gửi đi.

Ví dụ:

Hệ thống thanh toán online → cần xử lý ổn định 100–200 TPS vào giờ cao điểm.

Hệ thống báo cáo nội bộ → chỉ cần 5–10 TPS là đủ.

👉 Không nắm được TPS khiến bạn không thể kiểm thử hiệu năng đúng, cũng không đo được hệ thống sẽ bị “chết nghẽn” ở đâu.

💬 **Kết luận**

Non-Functional không phải phần “để sau rồi tính”. Chúng nằm ngay trong logic hệ thống, ảnh hưởng đến cảm giác người dùng, sự ổn định, bảo mật, và chi phí vận hành.

📌 **Checklist nhanh dành cho BA trước khi bàn giao tài liệu**

Timeout của từng request là bao nhiêu?

Latency cho phép ở mức nào? Có cần real-time không?

Retry có được bật không? Bao nhiêu lần, logic ra sao?

Hệ thống có những yêu cầu bảo mật nào bắt buộc?

Dự kiến số user đồng thời (CCU) là bao nhiêu?

Mỗi giây hệ thống cần xử lý bao nhiêu giao dịch (TPS)?


---

## DAY 77/100 — LÀM BA CHO MOBILE APP ĐỪNG TƯỞNG GIỐNG WEB LÀ ĐỦ!

*Trang 187–189*

App mobile thì cũng là hệ thống thôi mà – logic giống web, flow giống nhau, chỉ khác giao diện chút xíu.” Một nhận định tưởng vô hại, nhưng đã khiến không ít dự án vỡ trận vì bug, bị từ chối duyệt app, và bị người dùng phản ánh liên tục ngay từ tuần đầu ra mắt.

🕯️ **Câu chuyện thật: Bê tư duy web sang mobile – Và cái kết đắng**

Trong một dự án phát triển mobile app phục vụ việc đặt lịch khám bệnh, đội ngũ BA đã sử dụng lại gần như toàn bộ thiết kế từ hệ thống web trước đó:
- Form đặt lịch vẫn gồm 7 trường thông tin liên tục cần nhập.
- Không phân biệt hành vi giữa iOS và Android.
- Không mô tả các tình huống như mất mạng, quyền truy cập bị từ chối, hay khi ứng dụng bị tắt đột ngột.

Khi chạy thử bản đầu tiên, loạt vấn đề thực tế xuất hiện:
- Bệnh nhân thoát giữa chừng vì form nhập quá dài, thao tác bất tiện trên màn hình nhỏ.
- GPS không hoạt động vì hệ thống không xử lý khi người dùng từ chối cấp quyền.
- Khi mất kết nối mạng trong lúc gửi yêu cầu, app hoàn toàn không phản hồi.
- Nếu người dùng đang đặt lịch mà có cuộc gọi đến, quay lại ứng dụng thì toàn bộ dữ liệu bị mất.

App không lỗi ở nghiệp vụ. App lỗi vì tài liệu thiếu các đặc tả nền tảng quan trọng – những thứ tưởng nhỏ nhưng lại là sống còn khi chạy thật.

Vấn đề không nằm ở dev, mà bắt đầu từ chính việc BA chưa thay đổi tư duy khi chuyển từ web sang mobile.

🔍 **7 khác biệt then chốt BA cần ghi nhớ khi làm mobile app**

**1. Trải nghiệm người dùng là trung tâm, không phải quy trình nghiệp vụ**

Web: người dùng có thời gian, chuột, mạng mạnh.

Mobile: họ vừa đi vừa dùng, mạng yếu, thao tác bằng ngón tay.

👉 Đừng dồn hết thông tin vào một form dài. Hãy chia nhỏ, điều hướng thông minh.

**2. Xử lý khi mất mạng, mạng yếu**

Tôi từng để app đứng im 10 giây vì dev không xử lý timeout → người dùng bấm 3 lần rồi quit.

📌 Cần ghi rõ: nếu mạng yếu thì sao, có retry không, có lưu local tạm không.

**3. Quyền truy cập (permission): xin không được thì làm gì?**

App dùng GPS, camera, push notification... nhưng bạn không mô tả khi bị từ chối quyền thì dev cũng không biết xử lý.

👉 Luôn đặt câu hỏi: nếu user không cấp quyền thì sao, cần hướng dẫn gì, có fallback hay không.

**4. Khác biệt iOS và Android – Đừng tưởng giống nhau**

Một tính năng – hai hành vi. iOS xử lý khác Android. Alert, back button, permission, animation... đều có thể khác.

📌 Mô tả rõ các hành vi cần phân biệt theo OS, ví dụ: “Trên Android hiện dialog xác nhận, trên iOS dùng native modal.”

**5. Hành vi khi tắt app giữa chừng (cuộc gọi, đa nhiệm)**

Một shipper đang điền thông tin, có cuộc gọi đến → quay lại app: mất hết.

👉 BA cần mô tả rõ: app lưu tạm dữ liệu bao lâu, resume sẽ vào màn hình nào, nếu session hết hạn, cần báo gì.

**6. Xoay màn hình – Có xoay không? Xoay thì sao?**

Có những app xoay màn hình thì UI vỡ, mất focus, hoặc reset.

📌 Cần hỏi UI/UX team: màn nào cho xoay, có cần thiết kế lại cho landscape không, nếu không xoay thì cần lock orientation.

**7. Hiển thị trạng thái rõ ràng: gửi thành công, loading, lỗi**

Tôi từng không viết rõ cần loading khi gửi đơn → người dùng tưởng app đơ, bấm 3 lần.

👉 Mỗi action phải có: loading feedback, xác nhận thành công, báo lỗi rõ ràng và có hướng xử lý.

🧩 **Yêu cầu bắt buộc để đưa app lên App Store / Google Play**

1. Chức năng xoá tài khoản

Nếu app có login – bắt buộc phải cho user xoá tài khoản vĩnh viễn.

Không có → App Store reject thẳng tay.

📌 BA cần mô tả vị trí nút xoá, quy trình xác nhận, logic xóa dữ liệu user khỏi hệ thống.

2. Chính sách quyền riêng tư + điều khoản sử dụng

Google & Apple yêu cầu có link tới Privacy Policy và Terms of Use.

📌 BA phải xác định đặt link ở đâu (màn login, footer...), giao diện hiển thị (webview hay mở trình duyệt).

**3. Push Notification – Không chỉ là gửi được, mà phải mô tả đúng – đủ – có kiểm soát**

Trong nhiều dự án mobile, BA chỉ viết vỏn vẹn một dòng: “Hệ thống gửi push notification khi có sự kiện.”

Nhưng đó là chưa đủ. Việc gửi thông báo là phần dễ – xử lý sau khi người dùng bấm vào mới là thứ khiến app sống hay chết.

📌 Những điểm BA bắt buộc phải làm rõ:

Mục đích gửi thông báo: gửi để làm gì? Thông báo đơn thuần, nhắc nhở hành động, hay cảnh báo tức thời?

Tần suất & quyền kiểm soát: user có được phép tắt loại thông báo này không, có menu để quản lý không?

Hành vi khi người dùng bấm vào notification: nếu app đang chạy nền, đang mở sẵn, hay đang bị kill hoàn toàn thì có tái tạo đúng context không?

▲ Lưu ý

Những vấn đề được nêu trong bài viết mang tính tham khảo, chưa hẳn đã bao quát toàn bộ các tình huống có thể phát sinh trong dự án mobile.

Mỗi hệ thống có đặc thù riêng, nên BA cần liên tục cập nhật và bổ sung phù hợp với bối cảnh thực tế.

📎 Checklist tặng kèm

Nếu bạn đang cần checklist rà soát toàn diện khi làm tài liệu cho dự án mobile app, mình có sẵn bộ “Checklist 17 mục App Store/Google Play dành riêng cho BA”.

📩 Comment email của bạn bên dưới, mình sẽ gửi tặng bản đầy đủ.


---

## DAY 78/100 — CÂU CHUYỆN MỘT BUỔI OFFBOARDING – KẾT THÚC HĐLĐ VÀ... MỞ RA BÀI HỌC QUẢN TRỊ KHÔNG CÓ TRONG HANDBOOK

*Trang 190–191*

Ở một công ty nọ, có một bạn nhân sự trẻ không giỏi xuất chúng, cũng chẳng phải key member nổi bật.

Nhưng là người lặng lẽ support mọi người, biết nhận phần việc không ai muốn, luôn đúng hẹn, và chưa bao giờ nói câu “không phải việc của em”.

Bạn ấy làm BA – vai trò mà nếu làm tốt thì chẳng ai để ý, còn làm sai thì cả team dính bug. Hợp đồng lao động của bạn kéo dài 1 năm. Đến cuối quý thì hết hạn.

Không phải là không có review. Cuối năm ngoái, bạn từng được mời vào một buổi đánh giá ngắn – nơi bạn được nhận vài lời khen “ổn”, vài góp ý “cần chủ động hơn”, và lời kết:

“Cố gắng thêm vài tháng nữa, rồi mình tính tiếp.”

Nhưng “tính tiếp” đó... chẳng bao giờ tới.

Sau buổi review đó, không ai nhắc gì thêm. Không cuộc họp follow-up. Không kế hoạch phát triển. Không tín hiệu giữ chân.

Mọi thứ vẫn diễn ra như thường: task vẫn giao, dự án vẫn chạy, bạn vẫn đi làm đều – như thể HĐLĐ 1 năm kia... không hề tồn tại cái mốc kết thúc.

Cho đến ngày HR gọi bạn lên.

💬 “Hết hợp đồng thì chuyển sang cộng tác viên nhé em. Không còn bảo hiểm xã hội, không có ngày phép, và hợp đồng chỉ ký ngắn hạn 3 tháng.”

Bạn ấy cười nhẹ. Không hỏi thêm. Không ký.

Hôm sau gửi mail xin nghỉ – vẫn bàn giao chỉn chu, vẫn đi làm đến hết tuần, vẫn gỡ sticky note khỏi màn hình trước khi rời bàn.

“Thì ra một năm của mình, gói gọn lại chỉ còn là một con số trên file excel.”

🛑 Ở phía còn lại, team leader bất ngờ.

Bạn ấy không phải nhân sự giỏi nhất, nhưng là người giúp team ổn định nhất. Không than phiền, không đòi hỏi.

Chỉ tiếc là... không được giữ lại bằng một lời nói tử tế.

● Và lúc ấy, người leader ấy mới ngồi lại, mở sổ, ghi ra 3 điều cần thay đổi – không phải để giữ lại bạn đó, mà để giữ lấy chính tư cách làm quản lý

Tuyển người giỏi là kỹ năng – nhưng giữ người giỏi mới khó.

Đừng đợi đến khi người ta dọn bàn rồi mới nhận ra: “À, hoá ra bạn ấy quan trọng đến vậy.”

Im lặng không có nghĩa là hài lòng.

Những người lặng lẽ thường ra đi lặng lẽ – và để lại khoảng trống lớn nhất.

Offboarding không phải thủ tục – mà là dịp cuối cùng để người quản lý truyền thông điệp:

“Cảm ơn vì bạn từng là một phần tạo nên team này.”

💡 Từ đó, team có một điều mới trong quy trình offboarding

Không chỉ có checklist bàn giao, mà có thêm:

■ Một cuộc trò chuyện riêng giữa quản lý và nhân sự.

■ Một lời cảm ơn cụ thể.

■ Một lời chúc cho chặng đường tiếp theo.

■ Và một câu hỏi thành thật: “Nếu có điều gì khiến em ra đi – anh/chị mong được nghe để học.”

💬 “Làm sếp không chỉ là ký offer, mà còn là biết nói lời tử tế khi ký goodbye.”

📌 Làm quản lý, hãy học cách chia tay nhân sự như cách bạn từng háo hức khi chào đón họ.

Bởi vì cách bạn nói lời cuối – chính là thứ mà những người còn lại sẽ nhớ, sẽ nhìn, và sẽ học theo.

🔖 Bạn từng rời đi trong im lặng? Hay từng tiếc nuối một người ra đi không lời? Đừng để bài học ấy trôi qua.

Viết lại. Ghi nhớ. Và từ mai – làm leader với đôi mắt đủ tinh, và trái tim đủ ấm.


---

## DAY 79/100 — VÌ SAO CẦN HIỂU BUSINESS MODEL CANVAS TRƯỚC KHI VIẾT BẤT KỲ FLOW NÀO?

*Trang 192–193*

📌 Nhiều BA viết flow cực kỳ đẹp, rule đầy đủ, bước rõ ràng, UX hợp lý. Nhưng khi lên họp review, lại nhận về câu hỏi từ phía kinh doanh:

💬 “Flow thì ổn rồi. Nhưng không đúng hướng sản phẩm.”

💬 “Tính năng này viết kỹ đấy, nhưng không tạo ra giá trị thật.”

💬 “Cái này hợp lý về logic... nhưng không đúng với mô hình vận hành của bên anh.”

Tại sao lại vậy? Vì bạn viết flow khi chưa nhìn được bức tranh toàn cảnh.

✖ Đây là một trong những lỗi “chết người” của nhiều bạn BA chưa có nhiều kinh nghiệm:
- Lao vào viết flow theo tính năng.
- Không đặt câu hỏi: “Tính năng này sinh tiền kiểu gì?”
- Không xác định: “Người dùng chính là ai? Và họ có trả tiền cho hành vi đó không?”
- Không biết mô hình kinh doanh đang là: bán lẻ, SaaS, hay freemium?

💣 Viết flow mà không hiểu business model thì bạn chỉ đang... làm đẹp cho 1 sản phẩm có thể sai hướng ngay từ đầu. Trước khi vẽ bất kỳ flow nào, hãy dùng Business Model Canvas để trả lời 9 câu hỏi gốc rễ:

✔ Khách hàng mục tiêu là ai?

✔ Họ gặp vấn đề gì?

✔ Sản phẩm giải quyết nỗi đau nào?

✔ Kênh phân phối là gì?

✔ Cách tương tác với khách hàng thế nào?

✔ Doanh thu đến từ đâu?

✔ Chi phí hoạt động gồm những gì?

✔ Tài nguyên quan trọng nào cần duy trì?

✔ Đối tác chiến lược là ai?

📌 Trả lời được 9 câu này, bạn mới biết:

Flow bạn sắp viết có giúp kiếm tiền hay không. Đối tượng user nào là ưu tiên viết trước.

Chỗ nào cần optimize để scale, chỗ nào chỉ là “nice to have”.

💼 Với mỗi loại Business Model, cách viết flow sẽ khác:

Product Sale (Bán hàng 1 lần)

💡 Mô hình: bán sản phẩm trực tiếp.

🎯 Mục tiêu: tối ưu conversion.

📌 Flow mẫu: Trang sản phẩm > Thêm vào giỏ > Thanh toán. Ưu tiên tối giản bước, hiển thị rõ giá + phí ship. Tích hợp upsell/cross-sell ngay trong flow.

Subscription / SaaS

💡 Mô hình: thu phí định kỳ theo gói.

🎯 Mục tiêu: giữ chân user, giảm churn.

📌 Flow mẫu:

Đăng ký > Chọn gói > Dùng thử > Thanh toán > Gia hạn.

Có logic cảnh báo sắp hết hạn, tự động gia hạn, downgrade khi failed payment.

Freemium

💡 Mô hình: free tính năng cơ bản, trả tiền cho tính năng nâng cao.

🎯 Mục tiêu: tăng tỷ lệ chuyển đổi Free → Premium.

📌 Flow mẫu:

Người dùng free sử dụng bình thường > Gặp giới hạn > Nhấn nâng cấp.

Flow nâng cấp phải giữ nguyên session, không reload app.

Dẫn dắt bằng giá trị, không đơn thuần là nút thanh toán.

Platform 2-sided (Shopee, Grab)

💡 Mô hình: kết nối hai nhóm người dùng (buyer – seller).

🎯 Mục tiêu: cân bằng hệ sinh thái.

📌 Flow mẫu:

Buyer đặt đơn > Hệ thống gán seller phù hợp > Seller xác nhận.

Phải viết flow xử lý khi không ai nhận đơn, đơn bị hủy, hoặc seller vi phạm.

Data Monetization / Lead Gen

💡 Mô hình: thu thập dữ liệu – bán hoặc phân tích.

🎯 Mục tiêu: thu được dữ liệu đủ chất lượng + hợp pháp.

📌 Flow mẫu:

User điền form > Đồng ý điều khoản > Submit.

Có thêm flow: xác nhận email (double opt-in), điều kiện chia sẻ cho bên thứ ba.

■ Không hiểu business model = viết flow thiếu hồn. Bạn có thể vẽ đúng từng bước, nhưng không biết tại sao nó tồn tại. Không biết nên giữ lại cái nào, bỏ cái nào khi scope bị cắt. Không giúp team ưu tiên – vì bạn không thấy big picture.


---

## DAY 80/100 — PHÂN BIỆT 3 LOẠI LỖI – ĐỂ DEV KHÔNG FIX SAI, QA KHÔNG LOG NHẦM, VÀ USER KHÔNG CHỬI OAN

*Trang 194–195*

💥 “Sao lại báo lỗi? Em nhập đúng rồi mà!”

💥 “Anh fix rồi mà vẫn lỗi. À, lần này lỗi khác!”

💥 “Ủa BA ghi lỗi kiểu này là lỗi system hay do user vậy ạ?”

Nếu bạn từng nghe DEV hỏi những câu này, thì có thể bạn đang viết lỗi... lộn xộn.

🚨 Một dự án toang vì viết lỗi không rõ ràng

Trong một hệ thống chấm công, khi người dùng nhập giờ ra sớm hơn giờ vào, hệ thống báo lỗi:

✖ **“Không thể xử lý yêu cầu. Vui lòng thử lại sau.”**

DEV tưởng system lỗi.

QA log bug là “hệ thống không chấp nhận dữ liệu đúng”.

BA thì bảo “do user nhập sai”.

Kết quả: sửa đi sửa lại 3 vòng, cuối cùng mới phát hiện là do không phân biệt được loại lỗi ngay từ đầu.

✖ **Lỗi sai tư duy: Gộp tất cả lỗi vào một rổ**

Nhiều bạn BA viết message lỗi kiểu “cho có”, không phân biệt đâu là lỗi người dùng, đâu là lỗi system, đâu là lỗi nghiệp vụ.

Dẫn đến: test case không xác định được đúng, dev không có đủ thông tin để xử lý logic phù hợp hoặc quyết định cách hiển thị lỗi, người dùng thì không biết mình sai ở đâu – dẫn đến bối rối, thao tác lại sai tiếp.

**3 loại lỗi – hiểu đúng ngay từ đầu, dự án đỡ loạn về sau**

Khi hệ thống vận hành, sẽ luôn tồn tại 3 loại lỗi chính, mỗi loại cần mindset và cách xử lý riêng.

**1. Lỗi do người dùng nhập sai (Validation Error)**

Lỗi xảy ra khi người dùng bỏ trống trường bắt buộc, nhập sai định dạng, vượt max length.

Ví dụ:
- Bỏ trống số điện thoại
- Nhập email thiếu @ hoặc có ký tự lạ
- Nhập số vượt giới hạn cho phép

Cách xử lý đúng: hiển thị lỗi ngay tại trường bị sai, message cụ thể, tone thân thiện:

“Email không hợp lệ. Vui lòng nhập theo định dạng abc@xyz.com.”

Không popup, không doạ người dùng, và tuyệt đối không ghi kiểu: “Đã xảy ra lỗi” – câu này vô nghĩa.

**2. Lỗi do hệ thống (Exception/System Error)**

Đây là lỗi backend lỗi thật: API timeout, server die, database connection fail.

Ví dụ:
- API trả 500
- Timeout khi gọi payment gateway
- Lỗi ghi dữ liệu vào DB

Cách xử lý đúng: “Hệ thống đang bận. Vui lòng thử lại sau vài phút.” Đồng thời, ghi log đầy đủ cho dev trace lỗi – đừng để dev phải đoán mò.

**3. Lỗi do vi phạm logic nghiệp vụ (Business Rule Error)**

Người dùng nhập hợp lệ, hệ thống hoạt động bình thường, nhưng logic nghiệp vụ không cho phép thao tác đó.

Ví dụ:
- Nhập sai mật khẩu quá 5 lần → tài khoản bị khoá
- Chọn thời gian trùng với lịch đã đặt
- Gửi yêu cầu nhưng thiếu giấy tờ bắt buộc

Cách xử lý đúng: “Tài khoản của bạn đã bị khoá tạm thời do nhập sai mật khẩu quá 5 lần. Vui lòng thử lại sau 30 phút.”

Không phải lỗi system. Cũng không phải do user ngu. Mà là business rule đang bảo vệ hệ thống.

🔎 Trước khi giao tài liệu – hỏi bản thân 3 câu này
- Lỗi tôi mô tả thuộc loại nào? (Validation, Exception, Rule)
- Tôi có ghi rõ cách xử lý cụ thể cho từng loại lỗi chưa?
- Message lỗi tôi viết có giúp người đọc hiểu sai chỗ nào và sửa được không?


---

## DAY 81/100 — SPRINT VẪN TRỄ DÙ ĐÃ AGILE SCRUM: KẾ HOẠCH SAI TỪ ĐẦU HAY CÁCH SỐNG SAI VỚI AGILE?

*Trang 196–197*

🗣️ Một buổi tối, sau giờ làm, một bạn BA 3 năm kinh nghiệm nhắn tin cho tôi:

“Anh Phú ơi, công ty em chạy agile scrum cả năm nay rồi. Sprint nào cũng có planning, backlog groom đầy đủ. Mà sprint vẫn trễ. To-do thì nhiều mà done thì ít. Team thì bảo quá tải, quản lý thì bảo plan fail. Em không hiểu: tại sao vẫn trễ dù đã agile?”

Tôi thở dài. Không phải lần đầu nghe chuyện này. Nhưng tôi hỏi lại: “Sprint plan em làm trong bao lâu?”

Bạn BA trả lời: dạ khoảng 1 tiếng, team dev có 4 người, thường chia tầm 15 task. BA em sẽ gom task trước, viết mô tả sơ sơ trên Jira, rồi lên họp cả team để confirm lại. Nhưng thật ra buổi họp đó cũng nhanh, mọi người chỉ lướt qua từng task, assign người làm, rồi estimate luôn.

“Khi estimate task, có ai trong team phản biện không? Ví dụ dev nói task đó phức tạp hơn, cần nhiều thời gian hơn?”

Bạn BA trả lời: dạ không anh... thường là lead estimate trước, ví dụ ghi task đó là 1 ngày hoặc 2 ngày, rồi đưa lên Jira luôn. Trong buổi planning thì mọi người chỉ lướt lại, ai làm task nào thì nhận thôi, chứ cũng không ai nói thêm gì.

“Có gắn rõ Definition of Done, điều kiện test, hay những rủi ro ẩn không?”

“Dạ... tụi em chưa chi tiết tới vậy. Miễn dev hiểu là được.”

Đấy, trễ sprint không phải vì scrum không hiệu quả. Trễ vì đội đang sống giả vờ với scrum, và lập kế hoạch kiểu duy ý chí.

🖊️ **Lý do sprint trễ dù áp dụng Scrum: Kế hoạch thất bại vì**

**1.Không đủ dữ kiện để lập kế hoạch thực tế.**

Ước lượng task theo cảm tính “tầm 1 ngày xong”, không kiểm tra logic phụ thuộc.

Không rõ Done nghĩa là gì: code xong, test xong, review xong hay deploy xong.

Không tính chi phí context switching, một dev vừa làm bug vừa làm tính năng thì toang là đúng rồi.

💬 Plan không có dữ liệu, không có risk, không có rõ ràng thì nó chỉ là wish-list chứ không phải kế hoạch.

**2.Sprint planning diễn ra như thủ tục, không phải chiến thuật.**

Cả team đến họp planning mà không ai tranh luận effort. Ai nói bao lâu thì để vậy.

Không phân biệt loại task R&D, spike, bug, feature nên estimate toàn sai.

Không buffer cho các tình huống như nghỉ phép, họp gấp, prod bug.

💣 Sprint trễ không vì làm chậm, mà vì từ đầu đã plan sai và không ai dám nói nó sai.

**3.Scrum chỉ mang hình thức, mindset thì vẫn Waterfall.**

Product backlog không được groom đúng, task to, mù mờ.

Không break task theo flow thực tế dev, test, review, deploy; cứ quăng một task “làm tính năng ABC” rồi bảo dev tự hiểu.

Sếp vẫn giao chỉ tiêu kiểu tháng này phải xong, còn scrum thì chỉ để báo cáo cho đẹp.

■ Vậy làm sao để lập kế hoạch sprint không fail?
- Chúng ta có dám commit không.
  - Nếu không hãy hỏi vì sao: task chưa rõ, phụ thuộc ai, hay thiếu người.
- Chúng ta đã đủ thông tin chưa. Mỗi task đã có:
  - Giao diện hoặc luồng chuẩn.
  - Rule nghiệp vụ, dữ liệu liên quan.
  - Definition of Done.
  - Người review, test rõ ràng.

Chúng ta có tính đến những gì không nằm trong Jira chưa.
- Thời gian support prod.
- Họp đột xuất.
- Review tài liệu, meeting với BA, code review.

📎 Lập kế hoạch thất bại không phải vì dev yếu. Mà vì cả team sống trong ảo tưởng: tưởng đã làm scrum, nhưng vẫn nghĩ theo cách cũ.

Một sprint tốt không phải sprint nhiều việc, mà là sprint đúng cam kết.

Kế hoạch tốt bắt đầu từ việc dám đối mặt với thực tế, chứ không phải trang trí Jira cho đẹp.

Comment chia sẻ trải nghiệm team bạn gặp tình huống trễ sprint nhé.


---

## DAY 82/100 — “NỐI CUỐC” – TÍNH NĂNG NHỎ, HIỆU QUẢ LỚN TRONG BÀI TOÁN TỐI ƯU VẬN HÀNH RIDE-HAILING

*Trang 198–199*

Một buổi tối bình thường, tôi gọi một chuyến xe máy công nghệ. Khi vào app, tôi thấy một dòng chữ: “Tài xế đang trả khách...”.Chỉ một dòng đơn giản nhưng đằng sau đó là cả một cơ chế nối cuốc cực kỳ thông minh.

**1. Nối cuốc là gì?**

Trong các app gọi xe như XanhSM, Grab, Be..., nối cuốc là cơ chế cho phép hệ thống gán trước cuốc tiếp theo cho tài xế khi họ đang thực hiện cuốc hiện tại.

Ví dụ:
- Tài xế đang trên đường trả khách A.
- Hệ thống đã gán cuốc của khách B cho họ, vì điểm trả A gần điểm đón B.
- Sau khi thả khách A, tài xế di chuyển sang đón khách B luôn, không downtime.

**2. Tại sao tính năng này lại cực kỳ quan trọng?**

■ Tăng hiệu suất tài xế: giảm thời gian chờ giữa các cuốc → nhiều cuốc hơn mỗi giờ → thu nhập cao hơn.

■ Cải thiện trải nghiệm khách hàng: thời gian chờ ngắn hơn, đặc biệt trong giờ cao điểm hoặc mưa gió.

■ Giảm chi phí hệ thống: tối ưu số tài xế đang hoạt động mà vẫn đảm bảo tỷ lệ nhận cuốc cao.

■ Tăng retention tài xế và khách: cảm giác “có cuốc liên tục” khiến tài xế gắn bó hơn, khách thì ít phải chờ.

**3. Những bài toán BA cần giải khi làm tính năng này**

💬 Thuật toán matching phải đủ nhanh, đủ thông minh.

Ưu tiên tài xế sắp trả khách gần điểm đón mới.

Tính toán ETA chính xác để tránh delay cho khách chờ.

🎯 Cân đối công bằng.

Không để một nhóm tài xế “ôm cuốc” liên tục, còn nhóm khác thì chờ mãi không có cuốc.

💬 Trải nghiệm người dùng rõ ràng.

Khách thấy thông báo “tài xế đang trả khách” để tránh cảm giác bị bỏ rơi, có tùy chọn hủy nếu không muốn chờ.

![Hình minh họa giao diện nối cuốc trên ứng dụng gọi xe: "18:56 - Tài xế đang trên đường tới đón bạn.", bản đồ hiển thị điểm "Đang trả khách", và thông báo "Yay, tài xế xe 29BK-003.74 sẽ đón bạn trong 4 phút."](img_196.jpg)

**4. Những yếu tố ảnh hưởng đến “chất lượng nối cuốc”**
- Độ chính xác ETA: nếu tài xế trả khách lâu hơn dự kiến → ảnh hưởng cuốc sau.
- Hành vi tài xế: có tài xế “delay cố tình” để né cuốc không muốn.
- Vùng hoạt động: nối cuốc hiệu quả hơn trong khu vực đô thị mật độ cao.

🎯 Tính năng nối cuốc nhìn đơn giản – nhưng là ví dụ điển hình cho triết lý làm sản phẩm: “Tối ưu vận hành là tối ưu trải nghiệm.”

Bạn không cần phải build tính năng “wow” cho khách ngay từ đầu. Hãy bắt đầu bằng việc giúp hệ thống thông minh hơn, âm thầm nhưng hiệu quả hơn cho tất cả.


---

## DAY 83/100 — LÀM BA TRONG “TÂY DU KÝ CORP” KHI BẠN KHÔNG CHỈ PHÂN TÍCH NGHIỆP VỤ, MÀ CÒN PHẢI ĐỌC VỊ LÒNG NGƯỜI

*Trang 200–203*

Tôi xem lại Tây Du Ký lần thứ n, và lần này, tôi không còn thấy yêu quái. Tôi thấy... một công ty, nơi có một sếp Đường Tăng, một dev tên Ngộ Không, một bạn nghiệp vụ kiểu Bát Giới, chị vận hành tên Sa Tăng, và một anh support lặng thầm như Bạch Long Mã.

Và tôi thấy BA ở giữa phải hiểu tất cả họ, nếu không muốn flow mình viết ra bị nghiền nát trong họp review.

🧘 **1. Sếp Đường Tăng – Lý tưởng hóa requirement, nói hay nhưng thiếu thực tế**

💡 Kiểu người: sếp cấp cao, strategic visionary. Họ rất có tâm và có tầm. Họ hay nói về AI, CX, automation, data-driven culture... nhưng hiếm khi đưa ra yêu cầu cụ thể. Gặp vendor nói hay là... dính thính ngay.

🔥 Nguy cơ với BA:
- Yêu cầu mơ hồ.
- Không khả thi kỹ thuật.
- Dễ “đốt tiền” mà chẳng có output rõ ràng.

🎯 Chiến lược BA nên dùng:
- Tách mộng thành MVP và future phase → “Ý anh là dùng AI để phân tích nhu cầu khách hàng. Em chia ra 3 phase: tracking hành vi, phân cụm, đề xuất sản phẩm.”
- Hỏi về success metric → “Khi triển khai xong, anh muốn cải thiện chỉ số nào? Retention hay CTR?”
- Chốt bằng use case cụ thể → “Sau khi khách hủy đơn, hệ thống sẽ làm gì để tạo trải nghiệm ‘khác biệt’ như anh mong muốn?”
- Luôn back to budget và capability → “Giải pháp này cần tối thiểu 2 tháng backend + 1 tháng data. Nếu budget team mình chưa đủ, mình tạm phase sau nhé?”

🐒 **2. Tôn Ngộ Không – Dev lead siêu giỏi, thẳng như ruột ngựa**

💡 Kiểu người: technical stakeholder, architect, senior dev. Họ sẽ vả thẳng vào flow bạn viết nếu thấy sai logic. Họ giỏi, có tiếng nói trong team, và rất ghét sự hời hợt.

🔥 Nguy cơ với BA:
- Gãy flow vì thiếu logic.
- Bị mất điểm nếu không hiểu hệ thống.
- Căng thẳng nếu BA “vẽ mộng”.

🎯 Chiến lược BA nên dùng:
- Review 1–1 trước buổi họp team → “Anh xem giúp em phần điều kiện xử lý đơn này, có bug nào ẩn không?”
- Chuẩn bị logic bảng, exception flow, edge case → với Ngộ Không, một chỗ mâu thuẫn là đủ khiến BA “ăn gậy”.
- Tôn trọng góc nhìn kỹ thuật, không tranh đúng sai → “Quan điểm kỹ thuật của anh rất hợp lý. Em sẽ điều chỉnh luồng cho phù hợp constraint.”
- Ghi công khai trong diagram → “Flow được refine nhờ góp ý của dev lead – thank anh.”

🐷 **3. Trư Bát Giới – Nghiệp vụ dễ đổi mood, sống cảm xúc**

💡 Kiểu người: operational stakeholder, CSKH, sales, marketing. Góp ý rất chân thành: “Chị thấy nút này chưa ấm áp...”, “Khách hay phản ánh khúc này kỳ kỳ em ạ.” Họ là “gương mặt người dùng thật” và cũng rất cảm tính.

🔥 Nguy cơ với BA:
- Dễ thay đổi yêu cầu.
- Hay yêu cầu không logic.
- Dễ bị cảm xúc chi phối mà không rõ lý do.

🎯 Chiến lược BA nên dùng:
- Làm prototype hoặc mockup sớm → “Chị xem thử layout này có hợp chưa? Chị click thử giúp em flow nha.”
- Lặp lại yêu cầu để xác nhận → “Ý chị là: nếu khách nhập sai mã khuyến mãi thì hệ thống nên hiện popup giải thích, đúng không?”
- Tách đề xuất thành nhóm ngắn hạn, ưu tiên thấp, phase sau → không bác bỏ nhưng cũng không để họ dẫn dắt backlog.
- Hỏi insight thật sau cảm xúc → “Chị thấy khó dùng vì khúc nào? Do hiển thị hay logic xử lý?”

🪨 **4. Sa Tăng – Người vận hành hệ thống, ít nói nhưng nắm gốc rễ**

💡 Kiểu người: silent core stakeholder, kế toán, hành chính, admin hệ thống. Không nói nhiều, không drama. Nhưng làm sai flow thì họ gánh, và họ biết tất cả workaround đang âm thầm diễn ra.

🔥 Nguy cơ với BA:
- Bị bỏ qua.
- Flow không khớp thực tế.
- Không ai thèm lắng nghe họ.

🎯 Chiến lược BA nên dùng:
- Gặp riêng, shadow thao tác thật → “Chị xử lý đơn sai lệch dữ liệu bằng cách nào? Có phải gửi mail tay không?”
- Ghi lại các exception flow họ đang tự xử lý → những cái đó không có trong manual nhưng là “lẽ sống” của hệ thống.
- Gọi họ góp ý sớm trong buổi review internal → họ giúp bạn lấp lỗ hổng logic trước khi dev nhận task.
- Ghi rõ vai trò của họ trong flow → tên họ phải xuất hiện, không được gộp thành “hệ thống xử lý”.

🐎 **5. Bạch Long Mã – Người gánh backend ngầm, không nói nhưng thiếu là toang**

💡 Kiểu người: invisible support, IT support, vận hành nội bộ, người giữ hệ thống chạy ổn. Bạn tưởng họ không liên quan? Họ khởi động service, giữ log, bảo trì cron job, xử lý in ấn, monitor dashboard. Một ngày họ nghỉ phép – cả công ty đứng hình.

🔥 Nguy cơ với BA:
- Flow vẫn đúng nhưng hệ thống không chạy.
- Không có backup cho task âm thầm.
- Không rõ ai support cho feature cụ thể.

🎯 Chiến lược BA nên dùng:
- Lập danh sách “ai đang support hệ thống ngầm” → mapping tính năng, người gánh, risk nếu họ nghỉ.
- Ghi lại dependency rõ ràng trong tài liệu → “Form này phụ thuộc job chạy lúc 2 a.m. của anh Quang IT.”
- Tạo phương án thay thế nếu họ vắng mặt → “Trong trường hợp anh nghỉ, ai có thể monitor log thay anh?”
- Ghi nhận họ bằng hành động, không lời khen suông → đề xuất họ trong bản phân tích stakeholder hoặc kèm vào báo cáo effort flow.

🎯 Tổng kết

“Làm BA không chỉ viết đúng – mà phải hiểu đúng người đang đưa yêu cầu.”

Không có stakeholder nào “khó chịu” – chỉ là bạn chưa biết cách giao tiếp với từng kiểu người.


---

## DAY 84/100 — KHÁCH HÀNG ĐỘT NGỘT ĐỔI NGƯỜI ĐẠI DIỆN BA NÊN XỬ LÝ BÀN GIAO VÀ ONBOARDING THẾ NÀO?

*Trang 204–205*

🖊️ “Em ơi, từ hôm nay anh Trung không phụ trách nữa nhé. Chị Hà sẽ làm việc với em. Mình mong dự án vẫn chạy đúng tiến độ nha!” Nghe xong câu này, tôi toát mồ hôi. Vì chị Hà người đại diện mới chưa từng dự họp dự án, chưa đọc tài liệu nào, và... có vẻ chưa ưng hướng đi hiện tại. 🚨

Nếu bạn từng gặp trường hợp client đổi người đại diện giữa dòng, bạn sẽ hiểu:

👉 Mọi giả định trước đó có thể không còn giá trị.

👉 Những gì bạn tưởng là “xong rồi”, có thể bị xé nháp.

👉 Dự án có thể trễ, fail, hoặc tệ hơn: đổ lỗi ngược cho bạn.

✖ Cách làm sai mà nhiều bạn BA junior hay mắc

Tiếp tục triển khai như cũ, hy vọng người mới sẽ “bắt kịp”. Gửi tài liệu cũ và chỉ nói: “Chị xem giúp em file này nha!”. Không cập nhật lại hiểu biết của người mới, dẫn đến việc người này... hiểu sai toàn bộ scope.

■ **Checklist xử lý bàn giao + onboarding khách hàng mới**

**I. Chuẩn bị nội bộ trước khi gặp người đại diện mới**

Tổng hợp lại toàn bộ tài liệu hiện tại:
- SRS/BRD, diagram, các quyết định đã được approve.
- Highlight các điểm quan trọng:
- Yêu cầu có tranh cãi.
- Các giả định nền tảng.
- Những điểm còn đang open/discussion.
- Check contract + timeline để xác định rủi ro nếu scope thay đổi.

**II. Onboarding người đại diện mới – 1:1 kick-off**

Làm một buổi onboarding riêng, không gộp vào cuộc họp sprint. Hỏi lại các thông tin cơ bản (dù đã biết):
- Chị mong muốn gì ở dự án này?
- Mục tiêu thành công của chị là gì?
- Có phần nào chị chưa rõ / chưa đồng thuận?

Confirm lại với người mới:
- Chị có muốn rà lại toàn bộ scope hiện tại không, hay chỉ một phần?
- Ưu tiên nào chị thấy chưa hợp lý?
- Có quy định nội bộ mới nào ảnh hưởng đến yêu cầu không?

**III. Tái phân tích – Re-elicitation + Scope Confirmation**

Tạo phiên bản mới của requirement matrix:
- Đánh dấu những gì được xác nhận lại.
- Gắn cờ các mục cần review lại.
- Tổ chức workshop nhỏ để tái confirm các flow chính.
- Cập nhật log thay đổi và gửi recap ngắn gọn cho cả team.

**IV. Cập nhật tài liệu & quản lý kỳ vọng**

Tài liệu nào thay đổi → cập nhật ngay, có thể tạo SRS v1.1 để dễ tracking.

Gửi recap các điểm thay đổi + ảnh hưởng đến timeline (nếu có).

Tái confirm acceptance criteria cho từng tính năng.

💬 Đừng giả định người mới sẽ tiếp nối người cũ – họ đến với một cái đầu hoàn toàn khác.

📌 Bạn đã từng bị “đổi người” giữa chừng chưa? Comment chia sẻ câu chuyện thực chiến nhất của bạn – biết đâu sẽ thành Day kế tiếp trong chuỗi này!


---

## DAY 85/100 — RANH GIỚI CỦA BA KHÔNG RÕ THÌ DỄ TOANG, MÀ RÕ QUÁ LẠI BỊ NÓI... CHẢNH

*Trang 206–207*

“Cái này BA lo luôn nhé, chứ giờ ai làm?”

“Ơ, em là BA mà? Em hiểu nhất còn gì?”

“Chỗ này cũng liên quan logic – BA confirm giúp rồi viết test case hộ luôn nhé.”

Mỗi lần nghe những câu này, BA sẽ làm gì?

👉 Cắn răng làm, rồi tối về stress?

👉 Từ chối, rồi bị đánh giá thiếu hỗ trợ teamwork?

🎬 **Bối cảnh thật tại một công ty “vừa vừa”**

Không phải startup nhỏ, cũng chẳng phải tập đoàn. PM thì nửa thời gian lo họp, nửa thời gian làm report. DEV đang thiếu người, còn QC chỉ test được những gì “viết sẵn”.

Và BA được xem là “người hiểu việc nhất” – trở thành trung tâm gánh team.

Bạn mình từng làm BA trong môi trường như vậy. Mỗi ngày trôi qua như một cái máy hút task:
- Họp với khách xong phải viết cả user story, rồi thiết kế UIUX.
- Test case thì QC không hiểu nghiệp vụ, đành viết hộ.
- PM đẩy timeline, bảo em confirm hộ luôn với DEV đi cho nhanh.

Cuối sprint, DEV bảo thiếu spec. QC bảo test case không đúng. PM bảo “Tại sao em không confirm kỹ?”.

Kết quả: gánh hết trách nhiệm, mà lỗi thì vẫn là của BA.

💣 **Nguyên nhân không nằm ở người – mà ở ranh giới chưa bao giờ được xác định**
- Ở môi trường nhỏ, không ai rảnh để làm RACI.
- Không ai rảnh họp nguyên buổi “định nghĩa vai trò”.
- Nhưng không có ranh giới thì BA sẽ bị “lôi đầu” ở mọi lỗi – kể cả lỗi không phải của mình.

💬 **Vậy làm sao để xác định ranh giới?**

**1. Thay vì “chia vai”, hãy chia “điểm dừng”**

BA không cần nói: “Việc này không phải của em.” Nhưng có thể nói:

“Em confirm logic đến bước này, còn việc viết test case kỹ hơn nên để QC làm thì sẽ đảm bảo chặt hơn.”

👉 Trong môi trường resource ít, không chia được vai thì chia giới hạn trách nhiệm.

**2. Dùng “khung bàn giao” (handoff frame) – thay vì “vai trò rõ ràng”**

Không cần viết policy. Chỉ cần nói rõ: “Khi BA hoàn thành mô tả nghiệp vụ → UIUX có thể hỏi thêm nhưng không đẩy lại task thiết kế.”

“BA confirm logic → QC viết test case, nếu cần hỏi thì hỏi, chứ không phải nhờ viết hộ.”

👉 Quan trọng là set expectation trước – nhẹ nhàng nhưng dứt khoát.

**3. Giao tiếp như một “người điều phối”, không phải “người gánh vác”**

“Phần này cần clear hơn, để em hẹn cả DEV và QC một buổi mini-sync 15’.”

“Phần test này nếu có chỗ chưa rõ, em suggest QC hỏi lại chỗ rule nghiệp vụ cụ thể để làm rõ.”

👉 Luôn đặt vai trò người khác trong trung tâm trách nhiệm, mình chỉ hỗ trợ clarify – chứ không gánh thay.

**4. Nếu buộc phải làm hộ – hãy ghi lại rõ ràng, public việc đang làm**

Ví dụ: viết test case hộ QC?
- Log Jira, gắn label “Support QC – BA hỗ trợ tạo test case dựa trên rule.”
- Ghi chú ở Confluence: “BA chỉ viết test case phần logic nghiệp vụ, còn UI và negative test case sẽ do QC bổ sung.”

👉 Việc nhỏ này giúp chuyển từ gánh việc → hỗ trợ có điều kiện, không bị “lưu truyền miệng” rồi trách ngược.

📚 Làm BA không nên tính toán, nhưng nếu bạn không biết ranh giới của mình – bạn sẽ
- Làm không hết mà bị trách toàn phần.
- Mất thời gian support việc không giúp gì cho chất lượng phân tích.
- Bị hiểu sai vai trò → không phát triển lên senior được.

Ranh giới không phải để đùn đẩy – mà là để mọi người làm đúng việc, đúng chuyên môn.

📌 Nếu bạn đang là BA ở team nhỏ – bạn thấy cách nào hiệu quả để giữ ranh giới mà vẫn giữ được hoà khí?

Chia sẻ xuống dưới – vì chúng ta đang cùng chiến đấu ở những môi trường giống nhau


---

## DAY 86/100 — REVERSE-ENGINEER: KỸ NĂNG SỐNG CÒN KHI BA BƯỚC VÀO HỆ THỐNG CŨ

*Trang 208–211*

Bạn được giao viết lại tài liệu cho một tính năng đã chạy 3 năm, không tài liệu gốc, dev cũ đã nghỉ, test thì nhớ nhớ quên quên? → Chào mừng đến thử thách reverse-engineering, kỹ năng sinh tồn của BA.

🧩 **Bối cảnh ban đầu**

Bạn được giao viết lại tài liệu cho một tính năng đã hoạt động hơn 3 năm: “Khi xác nhận đơn giao hàng thì hệ thống sẽ tự động tạo phiếu xuất kho.”

Nhưng...

✖ Không có bất kỳ tài liệu cũ nào.

✖ Dev từng code tính năng này đã nghỉ.

✖ Tester chỉ nhớ là “test theo checklist chị kế toán gửi”.

✖ Chị kế toán thì chỉ nói: “Miễn sao hệ thống tự trừ kho đúng là được!”.

==> Bạn không thể viết tài liệu kiểu “nghe kể” hoặc “nhìn UI rồi tả đại”.

💬 **Reverse-engineer là gì?**

Là kỹ năng giải mã ý đồ nghiệp vụ từ một tính năng đang tồn tại. Tức là: tính năng không còn người nhớ, không còn tài liệu, mình phải hiểu nó để mô tả lại một cách mạch lạc, chuẩn chỉnh, dễ maintain về sau.

🔍 **Tư duy cốt lõi khi reverse-engineer**

Không tin ai hoàn toàn, kể cả người dùng, tester hay chính hệ thống. Tách biệt 3 lớp: giao diện – xử lý – kết quả (UI – logic – output). Truy vết: hiểu được tại sao nó hoạt động như thế, khi nào thì sai, ai phụ trách quy trình này. Viết lại bằng logic rõ ràng hơn cả người viết ban đầu.

🪜 **6 bước truy vết và viết lại tài liệu chuẩn**

**Bước 1: Xác định rõ input và output**

Input: người dùng click nút “Xác nhận đơn hàng” ở danh sách đơn giao hàng.

Output mong muốn: hệ thống tạo một phiếu xuất kho mới, gắn với đơn hàng này, cập nhật tồn kho, và hiển thị ở module quản lý phiếu xuất.

📌 Không dừng ở việc “ấn nút là ra phiếu” – phải xác định rõ: phiếu nào, gắn với đơn nào, cập nhật dữ liệu nào.

**Bước 2: Thao tác trên hệ thống và ghi lại hành vi từng bước**

Bạn vào hệ thống staging, thao tác như người dùng:

Bước 1: vào danh sách đơn hàng, chọn một đơn ở trạng thái “Chờ giao”.

Bước 2: click “Xác nhận”.

Kết quả:

Hệ thống hiện popup xác nhận.

Nhấn OK → trạng thái đơn hàng chuyển sang “Đã giao”.

Bạn vào module “Phiếu xuất kho” thì thấy xuất hiện phiếu mới, đúng số lượng đơn hàng.

==> Note lại toàn bộ UI, trạng thái thay đổi, và module liên quan.

**Bước 3: Đào code hoặc hỏi dev còn sót**

Bạn không có dev hỗ trợ, nên dùng log viewer và kiểm tra DB. Khi nhấn xác nhận, ghi nhận hệ thống gọi 2 API:

/confirm-shipping

/create-export-slip

Trong bảng export_slip có dòng mới:

order_id = 2345

status = GENERATED_AUTO

created_by = SYSTEM

📌 Xác nhận hệ thống thực sự tạo phiếu xuất và có dấu hiệu nhận biết: status đặc biệt, người tạo là “SYSTEM” chứ không phải user.

**Bước 4: Đối chiếu với dữ liệu thực tế**

Trên UI: trạng thái hiển thị là “Phiếu đã tạo thành công”.

Trong DB: status = GENERATED_AUTO (không ai định nghĩa trước).

Có một phiếu có quantity = 0.

📌 Phát hiện bất thường: UI nói “đã tạo”, nhưng thực tế phiếu rỗng, báo hiệu khả năng hệ thống vẫn tạo phiếu kể cả khi hết hàng.

Bước 5: Hỏi người dùng theo hướng ngược

Bạn hỏi chị kế toán: “Có khi nào chị xác nhận đơn mà phiếu không đúng không?”

Chị bảo: “Có! Nếu kho hết hàng mà vẫn xác nhận thì vẫn tạo phiếu, nhưng không có hàng nên không trừ gì cả.”

📌 Vỡ lẽ ra rule ngầm:

Hệ thống vẫn tạo phiếu kể cả khi hàng không đủ, nhưng số lượng xuất là 0.

Người dùng phải tự đi điều chỉnh lại phiếu sau.

==> Cái này không hề hiện trong UI hay logic code – chỉ có user mới biết.

Bạn không có dev hỗ trợ, nên dùng log viewer và kiểm tra DB.

Khi nhấn xác nhận, ghi nhận hệ thống gọi 2 API:

/confirm-shipping

/create-export-slip

Trong bảng export_slip có dòng mới:

order_id = 2345

status = GENERATED_AUTO

created_by = SYSTEM

📌 Xác nhận hệ thống thực sự tạo phiếu xuất và có dấu hiệu nhận biết: status đặc biệt, người tạo là “SYSTEM” chứ không phải user.

**Bước 4: Đối chiếu với dữ liệu thực tế**

Trên UI: trạng thái hiển thị là “Phiếu đã tạo thành công”.

Trong DB: status = GENERATED_AUTO (không ai định nghĩa trước).

Có một phiếu có quantity = 0.

📌 Phát hiện bất thường: UI nói “đã tạo”, nhưng thực tế phiếu rỗng, báo hiệu khả năng hệ thống vẫn tạo phiếu kể cả khi hết hàng.

**Bước 5: Hỏi người dùng theo hướng ngược**

Bạn hỏi chị kế toán: “Có khi nào chị xác nhận đơn mà phiếu không đúng không?”

Chị bảo: “Có! Nếu kho hết hàng mà vẫn xác nhận thì vẫn tạo phiếu, nhưng không có hàng nên không trừ gì cả.”

📌 Vỡ lẽ ra rule ngầm:

Hệ thống vẫn tạo phiếu kể cả khi hàng không đủ, nhưng số lượng xuất là 0.

Người dùng phải tự đi điều chỉnh lại phiếu sau.

==> Cái này không hề hiện trong UI hay logic code – chỉ có user mới biết.

**Bước 6: Viết lại tài liệu theo 3 tầng, rõ ràng, mạch lạc**

Đừng chỉ chép lại giao diện. Tài liệu chuẩn cần thể hiện đầy đủ ý định nghiệp vụ, logic hệ thống, cấu trúc dữ liệu.

■ **Gợi ý cấu trúc 3 tầng khi viết lại:**

**Tầng 1 – Giao diện (UI)**
- Mô tả từng field trên màn hình.
- Có bắt buộc nhập không.
- Khi nào ẩn hoặc hiện.
- Có placeholder, tooltip, gợi ý gì không.

**Tầng 2 – Logic xử lý (Business Rule)**
- Khi người dùng nhấn Lưu thì hệ thống làm gì.
- Điều kiện nào sẽ hiển thị cảnh báo hoặc lỗi.
- Trạng thái nào sẽ được chuyển tiếp sau hành động.

**Tầng 3 – Dữ liệu (Data Mapping)**
- Mỗi field tương ứng với cột nào trong DB.
- Lưu theo định dạng gì (date, enum, text...).
- Có trigger hay xử lý ngầm nào khi lưu không.

Bạn từng gặp trường hợp như vậy chưa? Bình luận hoặc lưu lại bài viết này nhé.


---

## DAY 87/100 — GÓP Ý MÀ KHÔNG LÀM NGƯỜI KHÁC NẢN: NGHỆ THUẬT QUẢN TRỊ ÍT AI DẠY BẠN

*Trang 212–213*

Một leader giỏi không phải là người góp ý đúng mà là người khiến người khác vẫn muốn làm việc cùng sau khi bị góp ý.

💬 **Phản hồi là con dao hai lưỡi – có thể giúp người ta tiến bộ, hoặc khiến họ gãy tinh thần.**

Dù bạn nói với thiện chí đến đâu, thì trong mắt người nhận, góp ý vẫn là một dạng từ chối, rằng thứ họ làm ra chưa đủ tốt, họ chưa đạt kỳ vọng. Và phản ứng phổ biến của họ không phải là tiếp nhận ngay, mà là:

Phòng thủ ngầm: “Biết rồi khỏi nhắc.”

Căng thẳng: “Tôi làm gì cũng sai à?”

Tự ti: “Chắc mình dở thật...”

Im lặng rút lui: “Từ nay cứ im cho đỡ bị góp ý.”

Kể cả người chuyên nghiệp cũng có cảm xúc. Vấn đề là cách bạn phản hồi quyết định cảm xúc đó đi về đâu.

💡 **Nguyên tắc 1: Chỉ trích hành vi – không công kích con người**

Tại sao quan trọng?

Vì lòng tự trọng là thứ cực kỳ nhạy cảm – đặc biệt khi người làm sai đã nhận thức được lỗi của mình. Nếu bạn công kích vào “bản thân họ” thay vì “hành vi cụ thể”, tâm lý phòng vệ sẽ lập tức trỗi dậy.

Ví dụ thực tế – một bạn BA bỏ sót case người dùng nhập sai mã OTP:

✖ “Em làm BA mà còn quên cả cái này thì chịu,” → Đâm vào lòng tự trọng, người nghe sẽ thấy mình bị đánh giá là kém cỏi.

■ “Trong flow xử lý, đoạn nhập OTP còn thiếu case sai định dạng. Mình bổ sung thêm để DEV xử lý đầy đủ nhé.”

→ Góp ý vào task, không gán nhãn người → người nghe vẫn giữ được giá trị bản thân và sẵn sàng sửa.

💡 **Nguyên tắc 2: Góp ý đúng lúc – đúng chỗ – đúng tâm thế**

Tại sao quan trọng?

Vì thời điểm và không gian góp ý sẽ quyết định việc người nhận cảm thấy bị làm nhục hay được tôn trọng. Khi đang căng thẳng, mệt mỏi, hoặc bị nêu tên trước đám đông, bản năng sinh tồn sẽ mạnh hơn lý trí tiếp thu.

Ví dụ thực tế – BA thiếu exception trong buổi họp với DEV, TEST:

✖ Leader nói ngay trong họp: “BA gì mà không nghĩ đến case nhập sai dữ liệu?”

→ Bạn BA mất mặt trước team, sau đó chỉ dám gửi tài liệu qua mail, không trình bày nữa.

■ Leader nói riêng sau họp: “Phần flow em trình bày rõ, chỉ thiếu vài case exception thường gặp. Mình bổ sung là ổn. Nếu cần, anh/chị gửi em checklist rà soát.”

→ Bạn BA giữ được tinh thần, lần sau chủ động nhờ review trước khi họp.

💡 **Nguyên tắc 3: Luôn để lại một lối đi**

Tại sao quan trọng?

Vì người nhận feedback không chỉ cần biết sai ở đâu – mà cần biết phải đi tiếp thế nào. Góp ý không để “chốt sổ” lỗi sai, mà để mở ra một cách sửa.

Ví dụ thực tế – junior BA làm bảng test case lộn xộn, thiếu trace logic:

✖ “Làm vậy là không chấp nhận được, em làm lại hết đi.” → Tạo cảm giác “không đủ năng lực”, người nghe làm lại chỉ để tránh bị mắng, không hiểu bản chất sai.

■ “Anh thấy phần mapping logic của em hơi rối – anh gửi file mẫu, rồi em thử format lại nhé.”

→ Không chỉ lỗi mà còn chỉ đường, giúp người nghe thấy: “À, mình làm được nếu có hướng.”

💡 **Nguyên tắc 4: Đừng nhầm ‘thẳng thắn’ với ‘thiếu kiểm soát cảm xúc’**

Tại sao quan trọng?

Vì nhiều leader hay tự nhận “tôi thẳng tính” để hợp thức hóa các cú đâm quá tay. Nhưng nói đúng mà làm người khác gãy – thì không còn là góp ý, mà là xả giận.

Ví dụ thực tế – QA báo nhiều lỗi nghiêm trọng ngay trước ngày release, cả team căng:

✖ Leader bùng nổ: “Test kiểu gì mà để lỗi như vậy? Có ai chịu trách nhiệm không?”

→ Cả team co lại, không ai dám lên tiếng, văn hóa đổ lỗi hình thành.

■ Leader kiềm lại, sau 15 phút mời team họp: “Release lần này lỗi khá nhiều – mình cần cùng ngồi lại xem checklist nào bị bỏ sót.”

→ Không hạ ai – mà hạ cái lỗi, từ đó tạo không khí sửa sai mà vẫn giữ tinh thần đội.

🔥 “Bạn có thể đúng – nhưng cách bạn nói có thể giết chết sự hợp tác.”

Góp ý không chỉ là kỹ năng giao tiếp. Đó là công cụ lãnh đạo. Nếu bạn biết nói sao để người khác nhận lỗi mà không mất tinh thần, nhận góp ý mà vẫn muốn làm tốt hơn, thì bạn không còn là sếp nữa. Bạn là người dẫn đường.


---

## DAY 88/100 — TRONG TEAM CÓ NGƯỜI “NÓI NHIỀU HƠN LÀM” – XỬ LÝ THẾ NÀO CHO RA CHẤT QUẢN LÝ?

*Trang 214–215*

Một người “nói nhiều hơn làm” trong team không chỉ là chuyện cá nhân.
Nó là bài test dành cho người dẫn dắt: liệu bạn có dám bóc tách sự hào nhoáng để truy tới tận rễ hiệu suất thật?

■ **Câu chuyện thật**
Bạn B – profile đẹp, nói năng mạch lạc, phát biểu dõng dạc ở mọi buổi grooming. Câu nào cũng có thuật ngữ:
“Em nghĩ nên trace requirement bằng traceability matrix”,
“Em đề xuất dùng Kano để đánh giá mức độ hài lòng”…
Nghe thì sang. Nhưng rồi 2 tuần sau:
- Use Case viết chưa xong.
- Flow Figma không sync với logic backend.
- Tester hỏi lại 5 lần vì mô tả thiếu bước.

🎤 **Đỉnh điểm:** khi bị nhắc, bạn ấy trả lời trong buổi retro: “Em đã research hết rồi, chỉ là chưa có thời gian cập nhật tài liệu thôi.” Nghe có quen?

✦ **Nhưng vấn đề nằm ở người quản lý**
Không phải vì bạn B dở. Mà vì người quản lý không dám gọi tên đúng vấn đề từ đầu. Và để mặc tiêu chuẩn của team bị kéo lệch về hướng “nói giỏi là được ghi nhận”.

● **Đẳng cấp xử lý không nằm ở “quát được to hơn”**
Mà nằm ở mấy điểm phân hoá sau:

1. **Bạn có đủ tỉnh để phân biệt “người trình diễn” với “người đang cố gắng chứng minh mình hữu ích”?**
Không phải ai nói nhiều cũng kém.
Nhiều người nói nhiều vì sợ bị loại, vì chưa tìm ra cách thể hiện giá trị thật.
📌 Một người quản lý đẳng cấp:
Không phản ứng theo cảm tính.
Mà phân tích động cơ, bối cảnh – rồi mới xử lý hành vi.

2. **Bạn có xây được hệ quy chiếu tiêu chuẩn để cả team tự điều chỉnh mà không cần bạn quát?**
Không phải sửa từng người. Mà xây hệ chuẩn công khai.
Review đầu ra theo checklist.
Tài liệu Use Case phải đủ main flow, exception, business rule.
Cách QC review cũng public cho cả team biết.
Khi bạn không cần nói – team vẫn biết cái gì là “đủ chuẩn”.
Lúc đó, “người nói nhiều” sẽ hoặc tiến hoá – hoặc tự rút lui.

3. **Bạn có dám giữ công bằng đến tận cùng kể cả khi người đó là “con cưng của sếp”?**
Nhiều quản lý thấy rõ vấn đề nhưng né tránh. Sợ động chạm. Sợ ảnh hưởng chính trị.
Một người dẫn dắt giỏi:
Vẫn feedback riêng, không dằn mặt trước team.
Ghi nhận người làm thật công khai, công bằng.
Nếu cần, trình bày với sếp bằng dữ liệu, không buôn chuyện.
Đẳng cấp là khi bạn bảo vệ được giá trị làm nghề, chứ không phải vị trí làm sếp.

4. **Bạn có biết “nâng” người đó lên – thay vì chỉ “dìm” xuống?**
Không phải ai cũng cần bị trị – nhiều người chỉ cần giao đúng việc để sáng ra.
📌 Gợi ý xử lý:
“Tuần này em đề xuất trace use case đúng không? Vậy giao em làm bảng trace cho 5 chức năng chính. Tuần sau review nhé.”
Từ nói → làm.
Từ phản biện → sở hữu.
Từ lý thuyết → kết quả thật.

5. **Bạn có ghi nhận theo kết quả – chứ không ghi nhận theo “khả năng hùng biện”?**
Là quản lý:
Đừng bị cuốn vào các cuộc họp màu mè.
Đừng quên ghi nhận người ít nói nhưng làm vững.
Và đừng bao giờ để junior nghĩ rằng: “Chỉ cần nói hay là đủ sống.”


---

## DAY 89/100 — MAD UNICORN – KHỞI NGHIỆP GIAO HÀNG & NHỮNG CÂU HỎI MÀ NGƯỜI LÀM BA KHÔNG THỂ TRỐN

*Trang 216–217*

Xem xong Mad Unicorn, tôi không nghĩ về startup. Tôi nghĩ về nghề BA. Nghĩ về những lúc mình hùng hổ vẽ flow, viết tài liệu chi chít use case… Nhưng lại chẳng biết người dùng thật sự bực mình ở đâu.

🎬 **Một bộ phim startup nhưng không bắt đầu từ công nghệ**
Bối cảnh phim là hành trình khởi nghiệp trong ngành giao hàng. Không bắt đầu bằng gọi vốn. Không bắt đầu bằng viết app. Mà bắt đầu bằng… những đơn hàng bị giao trễ, những câu than nhẹ như gió của người dùng, kiểu:
“Giao giờ này chắc lại mất hàng.”
“Gọi tổng đài hoài không được.”
“Ứng dụng gì mà khó dùng quá vậy?”
Và từ những lời đó, một người quyết định đứng ra làm lại mọi thứ – theo cách khác.

● **Không lập trình, không dashboard – chỉ có một câu hỏi**
Người dùng thật sự đang tổn thương ở đâu trong hệ thống hiện tại?
Và thế là mọi thay đổi bắt đầu.
Không dùng big data để phân tích xu hướng.
Mà đi ship từng đơn để nghe người ta càm ràm bằng tai thật.
Không optimize backend bằng tool.
Mà ngồi sửa tay từng bước trong quy trình giao, chỉ để đảm bảo đúng giờ và không mất hàng.

🛑 **Trong khi đó, đối thủ – bên kia chiến tuyến – làm ngược lại**
Dùng thuật toán dự đoán tuyến đường.
Có hệ thống quản lý tự động, callbot AI…
Dashboard thì trực quan đẹp đẽ.
Nhưng lại không thấy được một điều:
Khách hàng không rời đi vì thiếu tính năng.
Họ rời đi vì cảm thấy mình không được tôn trọng.

✦ **Tôi chợt giật mình**
Có bao nhiêu hệ thống chúng ta từng làm cũng rơi vào cảnh đó?
Đủ chức năng, đủ luồng, đủ permission.
Nhưng vẫn khiến người dùng thấy… mệt.

👀 **Và tôi nghĩ tới vai trò BA trong những cuộc chiến đó**
BA không nằm trong spotlight.
Không phải founder. Không phải developer.
Nhưng là người kết nối tất cả những gì rời rạc: người dùng, nhu cầu, quy trình, dữ liệu, cảm xúc.
Người phải hiểu được những điều chưa ai nói ra.

💭 **Có những đoạn phim khiến tôi dừng lại, lấy giấy bút ghi chép**
Khi cả hệ thống bị chửi chỉ vì một bước xác nhận sai chỗ.
Khi flow được vẽ lại từ đầu, không phải vì sai logic, mà vì không ai hiểu nó đang phục vụ điều gì.
Khi khách hàng gào lên: “Tôi không cần app đẹp! Tôi cần người tới đúng giờ, và không mất hàng của má tôi.”
Lúc đó tôi hiểu: requirement thực sự không nằm trong Jira. Nó nằm trong từng lần khách nổi nóng – mà mình bỏ qua.

📘 **BA học được gì từ Mad Unicorn?**
- Đừng phân tích hệ thống nếu chưa hiểu người dùng đang cảm gì.
- Cảm xúc là đầu mối để xác định vấn đề thật. Không có nó, mọi thứ bạn viết chỉ là giả định.
- Một BA giỏi không viết nhiều hơn – mà thấy sâu hơn.
- Người dùng nói “muốn theo dõi trạng thái giao hàng”, nhưng thứ họ thật sự cần là sự chắc chắn.
- Làm hệ thống mà bỏ qua người đầu tiên từng tin mình – là mất gốc.
- Đừng để “người dùng cũ” trở thành kẻ thù vì một nút lỗi nhỏ không ai xử lý.

📌 **Mad Unicorn không dạy BA làm nghề**
Nhưng lại nhắc BA một điều mà không cuốn sách nào viết:
“Đôi khi, cả hệ thống vận hành tốt… nhưng vẫn khiến người ta bỏ đi, vì họ cảm thấy không được hiểu.”
Hệ thống không cần cầu kỳ.
Chỉ cần đúng nỗi đau.
Chỉ cần làm cho người dùng thấy: “Tôi hiểu bạn đang cần gì. Và tôi làm ra cái này vì bạn.”


---

## DAY 90/100 — P.O.L.C DÀNH CHO BA LEAD

*Trang 218–219*

Bạn là BA Lead? Tức là bạn vừa làm nghề vừa phải giữ team, giữ chất lượng, giữ deadline. Không còn là người “chạy việc BA”, bạn cần quản trị cả hệ thống tư duy và vận hành của đội ngũ BA.
Và P.O.L.C không phải lý thuyết quản trị suông mà là framework sống còn để bạn không bị cuốn vào mớ deadline, họp loạn xạ.

1. 💭 **Planning: lập kế hoạch để giữ team không bị dạt**
BA Lead không thể chạy ad-hoc.
■ Bạn phải vạch kế hoạch phân tích tổng thể cho team: ai phân tích gì, timeline từng người.
■ Chủ động lên lộ trình làm rõ requirement, review, confirm, UAT theo từng sprint.
■ Có phương án backup nhân sự khi một BA nghỉ đột xuất.
💡 Không có planning là bạn đẩy team ra biển không la bàn. Vừa yếu team, vừa mất uy với dev và PM.

2. 🧩 **Organizing: tổ chức để dựng hệ thống, không chỉ phân task**
■ Xây template, guideline, thư viện use case dùng chung, tránh mỗi người viết mỗi kiểu.
■ Chia team theo luồng (by feature, by module, by stakeholder) để tăng chuyên môn và tối ưu kiến thức tích lũy.
■ Tạo hệ thống quản lý yêu cầu thay đổi, trace logic giữa CR, UC, data, màn hình.
💡 Team mạnh là team có hệ thống hỗ trợ, không phải team phụ thuộc vào một người lead giỏi.

3. 💡 **Leading: dẫn dắt tư duy và giải quyết vấn đề**
Đừng ngồi review từng dòng mô tả UC. Hãy dẫn team tư duy.
■ Gợi mở câu hỏi đúng: “Case này cần hỏi gì”, “Flow này có kịch bản lỗi nào chưa nghĩ tới”.
■ Bảo vệ team khỏi yêu cầu vô lý bằng lập luận rõ ràng, dẫn dữ liệu và logic system.
■ Dẫn dắt đội làm retrospective sau mỗi sprint, không để lỗi lặp lại.
💡 BA Lead không nhất thiết phải làm giỏi nhất, nhưng phải dám đi trước và truyền tư duy cho người đi sau.

4. 📊 **Controlling: kiểm soát chất lượng và logic hệ thống**
Đừng quản lý task, hãy quản lý chất lượng.
■ Có review checklist cho mọi tài liệu: logic, exception, traceability, UX/flow.
■ Theo dõi tiến độ và rào cản của từng BA, không để đến lúc trễ mới báo.
■ Theo sát chỉ số hiệu quả của team: tỷ lệ task bị reject hoặc UAT fail, thời gian trung bình xử lý CR.
💡 Controlling không phải micromanagement mà là nhìn hệ thống ở tầng cao để không “toang” từ gốc.
🔥 “BA Lead không gào to nhất team, mà là người giữ vững tư duy và thiết kế hệ thống vững nhất giữa bão yêu cầu.”


---

## DAY 91/100 — NGÔN NGỮ KHÁCH HÀNG MỘT THỨ TIẾNG KHÔNG ĐƯỢC DẠY Ở TRUNG TÂM ANH NGỮ NÀO, NHƯNG BA NÀO CŨNG BUỘC PHẢI NGHE HIỂU NHƯ NGƯỜI BẢN XỨ

*Trang 220*

Phiên dịch tập 1]
🎧 Nghe: “Tuỳ em”
🧠 Dịch chuẩn:
“Tôi chưa nghĩ ra. Em cứ làm đi, nếu không đúng tôi sẽ bảo là không đúng.”
☠️ Cạm bẫy:
Không hề là “em toàn quyền quyết định”.
Mà là “cứ làm đi để tôi còn có quyền chê”.
🛡️ Cách BA sinh tồn:
“Vậy anh/chị có thể giúp em chọn một trong hai hướng sau không ạ?” (kèm prototype, flow, impact analysis nhẹ nhàng)
🎧 Nghe: “Có mỗi chức năng bé tí ấy mà”
🧠 Dịch chuẩn:
“Tôi thấy nhỏ, nhưng đằng sau là cả backend, hệ thống phân quyền, validate, đồng bộ, audit log…”
☠️ Cạm bẫy:
Nghe nhỏ nhưng code dài 3 ngày.
Test 5 case, bug 8 case.
🛡️ Cách BA sinh tồn:
“Vâng, để em phân tích tác động hệ thống và ước lượng effort trước rồi mình chốt ạ.”
🎧 Nghe: “Anh làm tất cả cũng vì dự án mà”
🧠 Dịch chuẩn:
“Anh sắp đẩy 1 thứ rất gấp, không rõ, nhưng em đừng từ chối.”
☠️ Cạm bẫy:
Dùng cảm xúc thay tài liệu.
Đẩy deadline mà không rõ requirement.
🛡️ Cách BA sinh tồn:
“Em rất trân trọng sự hỗ trợ của anh, vậy mình thống nhất rõ scope để DEV không bị lúng túng ạ.”


---

## DAY 92/100 — CÂU CHUYỆN TÁI ÔNG THẤT MÃ VÀ NHỮNG TRIẾT LÝ UYÊN THÂM

*Trang 221–222*

Ngày ngựa mất, cả làng đến chia buồn. Ông lão chỉ cười, không trách cũng không tiếc.
Ngày ngựa về, lại dắt thêm một con tốt hơn.
Cả làng đến chúc mừng. Ông cũng cười. Nhưng vẫn không vui.
Rồi con trai ông ngã gãy chân vì con ngựa mới. Người làng lại thương cảm.
Cuối cùng, chiến tranh nổ ra, trai làng đều bị gọi đi lính, chỉ mình cậu con trai gãy chân được ở lại. Thoát chết.
Nghe thì đơn giản, nhưng câu chuyện Tái Ông Thất Mã chính là một trong những ẩn dụ cổ xưa sâu sắc nhất về nhận thức, kiểm soát và lòng kiên định trước biến động.
Dưới đây là bốn tầng triết lý ẩn sau câu chuyện ấy, và cũng là kim chỉ nam cho bất kỳ ai đang đi trên hành trình sự nghiệp đầy bất định, như nghề BA vậy.

1. **Phúc, họa chưa đến hồi kết, đừng vội gắn nhãn**
Ngựa mất, chưa chắc là xui. Ngựa được, chưa chắc là may. Điều tốt xấu chỉ là một lát cắt tạm thời. Đa phần người đời khổ, không phải vì biến cố, mà vì gắn nhãn quá sớm.
Trong nghề BA cũng vậy:
Bị rút khỏi dự án, tưởng là thất bại. Nhưng có khi lại thoát khỏi vòng luẩn quẩn của một sản phẩm đã chết từ lúc lên ý tưởng.
Không được promote, tưởng là thiệt thòi. Nhưng nhờ vậy mà giữ được thời gian học và đào sâu tư duy nền tảng.
Bài học: đừng để một lát cắt vụn vặt trong sự nghiệp định nghĩa toàn bộ giá trị của bạn.

2. **Kẻ tỉnh thức là kẻ không để cảm xúc dắt mũi**
Cả làng vui buồn theo biến cố. Chỉ ông lão là đứng ngoài vòng xoáy cảm xúc ấy.
Không vì được mà ngạo. Không vì mất mà sầu. Đó là tỉnh thức. Là trí tuệ của người không sống bằng phản ứng, mà sống bằng phản tỉnh.
Là BA, bạn sẽ gặp đủ mọi thứ:
- Sếp đổi hướng liên tục.
- Dev xoay tech stack giữa chừng.
- Stakeholder đổi yêu cầu ba lần một tuần.

Bạn không thể kiểm soát tất cả.
Nhưng bạn có thể kiểm soát chính mình bằng cách ngưng phản ứng và bắt đầu đặt câu hỏi:
“Chuyện này dạy mình điều gì?”
“Đây là cảm xúc, hay là sự thật?”

3. **Càng kiểm soát, càng mất kiểm soát, buông đúng lúc là trí tuệ**
Người đời thường muốn giữ. Giữ con đường đang đi. Giữ chức danh đang có. Giữ dự án mình đã đổ máu. Nhưng đôi khi, giữ là sai.
■ Một BA từng thiết kế hệ thống A sẽ rất dễ dính chặt vào mô hình cũ, dù nó không còn hợp.
■ Một BA leader từng thành công với phong cách push nhanh sẽ bối rối khi team chuyển sang style chậm chắc.
Chấp vào cái đã có là gốc rễ của sự lạc hậu.
Người có trí tuệ không cố giữ ngựa.
Họ học cách buông và chuyển sang thiết kế xe khác.

4. **Cái được lớn nhất là sự trưởng thành, chứ không phải là giữ được con ngựa nào**
Cuối cùng, ông lão vẫn mất. Con trai ông cũng sẽ già. Ngựa rồi cũng chết. Cái còn lại là một người từng đi qua tất cả biến động đó mà vẫn không đánh mất mình.
Đó là đích đến thầm lặng của mọi hành trình. Không phải để được gì, mà để trở thành ai.
■ Một BA giỏi, không phải là người chưa từng bị loại khỏi dự án.
■ Mà là người biết đứng dậy, hiểu sâu hơn, và không cay cú với đời.
Tái Ông mất ngựa không phải chỉ là một câu chuyện để đọc rồi quên. Nó là thứ bạn phải sống qua mới hiểu.
Và đến một ngày, khi bạn ngồi một mình sau cú rút khỏi dự án tâm huyết, khi ai đó khác cầm lái hệ thống bạn từng thiết kế bằng cả tấm lòng, bạn sẽ nhớ lại câu chuyện này và nhận ra:
Cái mất ấy là món quà cho hành trình trưởng thành mà bạn không thể học được nếu chỉ đi mãi một đường thẳng.


---

## DAY 93/100 — TOP 5 LỖI MÀ SENIOR BA / BA LEAD THƯỜNG MẮC PHẢI

*Trang 223–224*

📌 Làm BA lâu năm, tưởng là sẽ vững hơn, nhiều kinh nghiệm hơn, nhưng thật ra lại dễ chủ quan hơn. Tôi từng nghĩ: “Cái này mình làm nhiều rồi”, cho đến khi team rơi vào đống issue.
Dưới đây là 5 lỗi phổ biến mà rất nhiều Senior BA, Lead BA gặp phải.
👉 Đây là tổng hợp dựa trên quan sát và kinh nghiệm cá nhân, không đại diện cho bài nghiên cứu, một report chính thống nào đâu nhé, tham khảo hoan hỉ. 🙌

1. **Quá tự tin vào kinh nghiệm, không hỏi lại người dùng**
“Cái này giống dự án cũ mình từng làm…”
● Làm lâu dễ sinh chủ quan, không hỏi lại stakeholder, không validate assumption, phân tích sai từ gốc.
■ Ghi nhớ: mỗi dự án là một bối cảnh mới. Kinh nghiệm là đèn soi đường, không phải lý do để khỏi cần hỏi.

2. **Cố ôm việc, không phân quyền, nghĩ rằng team junior chưa đủ trình**
Hậu quả: tắc bottleneck, leader làm BA part time, còn BA thì không được lớn.
● Senior giỏi là người biết chia sân chơi và dám để team sai trong tầm kiểm soát. Không tạo sandbox, junior mãi không lên được.
■ Giải pháp: đưa checklist, review đầu – giữa – cuối, để junior chủ động, mình kiểm soát theo chu kỳ.

3. **Bị kéo vào họp chiến thuật thay vì giữ góc nhìn chiến lược**
Cứ mỗi lần khách than là bay vào xử lý case nhỏ. Cuối cùng dự án không có người đứng mũi chịu sào.
● BA Lead không phải lính cứu hỏa. Nếu không giữ cái đầu tỉnh, sẽ trở thành người xử lý lỗi thay vì định hướng toàn cục.
■ Giải pháp: ủy quyền xử lý daily task, còn mình lo chuyện sản phẩm có đang đúng hướng không.

4. **Không training lại team về tư duy sản phẩm và kỹ thuật mới**
Làm BA 5 năm nhưng vẫn hỏi “Non functional là gì”. Làm tài liệu xịn mà tư duy vẫn kiểu “feature là xong”.
● Nếu mình không update, team dậm chân tại chỗ. Mà team dậm chân thì dự án lạc hậu.
■ Giải pháp: làm mini sharing nội bộ 2 tuần 1 lần, mỗi người lên 1 chủ đề, vừa học vừa tạo văn hóa chia sẻ.

5. **Không chịu bị feedback**
“Tôi lead mà, góp ý gì nữa?”
Và thế là từ từ mất kết nối với DEV, mất tiếng nói với business.
● Senior mà mất khả năng lắng nghe là dấu hiệu của… “hết thời”. Đôi khi junior nói đúng, chỉ vì chưa nói hay nên bị bỏ qua.
■ Giải pháp: tạo một kênh ẩn danh hoặc safe zone cho team góp ý, và chủ động hỏi: “Mọi người thấy mình đang bị lệch ở đâu không?”

✦ Tóm lại: là Senior không có nghĩa là miễn nhiễm với sai lầm. Mà là phải tỉnh táo để tự phát hiện – tự sửa – và giúp người khác tránh.
“Người càng giỏi càng phải biết… đi học lại chính mình.”


---

## DAY 94/100 — KÝ HỢP ĐỒNG CHỐT KHUNG, PHÂN TÍCH DETAIL THÌ SCOPE NỞ

*Trang 225–226*

Định ém mấy bài hay hay để viết vào ebook nhưng hôm nay nhá hàng tí vì thấy nhiều case gặp phải vấn đề này. Một trong những cái bẫy chết người của dự án là: hợp đồng ký thì tưởng đã chốt, nhưng khi BA phân tích chi tiết, scope cứ phình ra vô tận. Vậy đâu là cách để khóa scope ngay từ đầu đến cuối?
**Trước khi bắt đầu phân tích (ngay sau khi ký hợp đồng)**
✖ Sai: Nghĩ rằng SOW chỉ là “cái khung tổng quát”, còn chi tiết thì để phân tích sau. Không định nghĩa ranh giới rõ ràng.
■ Đúng: Ngay sau khi ký hợp đồng, BA và PM phải cùng khách hàng chốt rõ phạm vi ở mức “danh mục tính năng cấp cao” và định nghĩa In/Out scope. Cái này có thể là một context diagram hoặc một feature list sơ bộ.

Ví dụ: SOW ghi “Quản lý kho”.
✖ Sai: Nghĩ quản lý kho là gì thì lúc phân tích mới rõ.
■ Đúng: Chốt rõ quản lý kho chỉ gồm “nhập – xuất – tồn” cơ bản, không bao gồm “chuỗi cung ứng” hay “sản xuất”.
Kết quả cần chốt trước: Một bản Scope Baseline tối thiểu, được cả hai bên ký xác nhận.

**Trong quá trình phân tích detail**
✖ Sai: BA nghe khách nói gì cũng ghi hết, rồi bổ sung liên tục mà không gắn với scope baseline.
■ Đúng: Mỗi requirement chi tiết phải được trace ngược về mục trong Scope Baseline. Cái nào không trace được thì đánh dấu là “ngoài scope” và đưa sang danh sách Change Request.

Ví dụ: Phân tích “tính lương”. Khách bảo: ngoài lương cơ bản, thêm KPI, thưởng dự án, bảo hiểm, liên thông với thuế.
✖ Sai: BA ghi hết vào tài liệu và coi như trong hợp đồng.
■ Đúng: BA giữ nguyên baseline “tính lương cơ bản”. Tất cả phần KPI, thưởng, thuế đưa sang danh sách CR để khách hàng quyết định có mua thêm hay không.
Kết quả cần chốt trong: Một danh sách yêu cầu được phân loại rõ ràng “Trong scope” và “Ngoài scope (CR)”.

**Sau khi phân tích xong và trong lúc triển khai**
✖ Sai: Không tái xác nhận scope sau khi phân tích, dẫn đến chuyện khi dev xong thì khách bảo “Cái này đâu đủ, tôi còn nói cái kia nữa mà.”
■ Đúng: Sau khi phân tích xong, BA phải tổng hợp thành tài liệu Scope Detail và tổ chức buổi sign-off. Khách ký xác nhận “Đây là toàn bộ phạm vi chi tiết cho dự án”. Mọi thứ phát sinh sau đó đều đi theo cơ chế CR.
Ví dụ: Sau khi phân tích nhân sự, BA đưa ra tài liệu chi tiết: quản lý hồ sơ, chấm công, lương cơ bản.
■ Đúng: Tổ chức sign-off, khách ký xác nhận. Khi khách sau này bảo thêm KPI, có cơ sở để nói “Đây là yêu cầu mới, thuộc CR”.
Kết quả cần chốt sau: Một bản tài liệu Scope Detail đã được khách hàng sign-off.

👉 “Ký hợp đồng là khóa khung. Phân tích detail là khóa cửa. Sign-off là khóa chốt. Thiếu bước nào thì scope nở ngay ở đó.”
Checklist cho BA để không bị scope nở
Trước dự án: Xác định scope baseline với danh mục tính năng cấp cao.
Trong phân tích: Trace từng requirement về baseline, tách riêng yêu cầu ngoài scope.
Sau phân tích: Tổ chức sign-off phạm vi chi tiết, chốt cơ chế CR cho mọi phát sinh.
Bạn đã từng thiếu bước khóa nào và bị scope nở chưa? Comment chia sẻ để anh em cùng rút kinh nghiệm.


---

## DAY 95/100 — VÙNG XÁM TRONG KHẢO SÁT YÊU CẦU – CÁI BẪY GIẾT CHẾT DỰ ÁN

*Trang 227–228*

Trong một buổi khảo sát, khách nói: “Dữ liệu bao gồm nhưng không giới hạn ở…”
Hoặc: “Hệ thống có khả năng mở rộng, sau này thêm gì cũng được.”
Nếu bạn ghi nguyên văn vào SRS, xin chúc mừng, bạn vừa ký một cái hợp đồng trắng cho khách hàng. Đến lúc đi triển khai, đội DEV và BA sẽ bị “truy” vì cái gì cũng được hiểu là “đã bao gồm”.
Sai lầm thường gặp
Ghi mơ hồ vào tài liệu, copy y nguyên câu khách.
Không chất vấn tới cùng, sợ mất lòng, sợ bị coi là “khó chịu”.
Không chốt biên để mọi thứ lửng lơ, đến lúc go-live mới vỡ mặt.
Vậy BA cần làm gì để né vùng xám?
**Biến định tính thành định lượng**
Sai: “Hệ thống phải nhanh.”
Đúng: “Thời gian phản hồi < 2 giây với 1.000 bản ghi.”
📌 Ví dụ: khách nói “bộ lọc nhanh.” → Bạn hỏi: nhanh là bao nhiêu giây, với bao nhiêu dữ liệu, từ đó ghi rõ KPI.
**Vẽ ranh giới bằng định nghĩa**
Sai: “Khách hàng” ai cũng hiểu.
Đúng: Glossary: “Khách hàng = người trả tiền”, “Người dùng cuối = người thao tác hệ thống”.
📌 Ví dụ: báo cáo doanh thu “theo khách hàng” → phải làm rõ là theo “người trả tiền”, không phải bất kỳ ai có tài khoản.
**Đặt câu hỏi ngược để tìm điểm gãy**
Sai: chỉ hỏi “khi nào dùng?”
Đúng: hỏi thêm “khi nào không dùng?”, “trường hợp ngoại lệ là gì?”.
📌 Ví dụ: yêu cầu “gửi SMS xác thực” → hỏi thêm: nếu nhà mạng lỗi thì sao, retry mấy lần, bao lâu thì chuyển sang gọi?
**Công khai assumption và constraint**
Sai: ghi “có khả năng mở rộng” mà không ràng buộc gì.
Đúng: viết rõ “Hỗ trợ tối đa 30 TPS cho SMS. Nếu cần 60 TPS → phải nâng hạ tầng, chi phí X.”
📌 Ví dụ: “Xuất báo cáo” → chốt tối đa 50.000 dòng/lần, vượt hơn phải tách lô.

**Chốt phạm vi và cơ chế thay đổi**
Sai: “Sau này thêm gì cũng được.”
Đúng: ghi rõ
- Giai đoạn 1: chỉ A, B, C.
- Out of scope: X, Y, Z.
- Thêm mới → qua CR, ước lượng lại.

📌 Ví dụ: “Tích hợp nhà mạng” → chốt: Viettel, MobiFone, VinaPhone. Nhà mạng khác = CR.


---

## DAY 96/100 — TƯ DUY FAIL FAST – CỨU DỰ ÁN NGAY TỪ GIAI ĐOẠN PHÂN TÍCH

*Trang 229–230*

Làm BA mà ôm nỗi sợ sai thì thua ngay từ vạch xuất phát. Fail Fast không phải triết lý màu mè, nó là cái phanh khẩn cấp cứu dự án khi còn nằm trên bàn phân tích.

1. **Câu chuyện thực chiến**
Dự án triển khai hệ thống điểm danh cho chuỗi phòng gym. BA junior dành cả tháng để “thu thập đủ yêu cầu”, viết tài liệu 80 trang. Khi trình lên, khách hàng mới bảo:
“Anh ơi, bên em có phòng không có internet, điểm danh offline thế nào?”
“Chỗ này cần QR code chứ không phải vân tay.”
Cả tháng phân tích thành giấy lộn. Trong khi đó, một BA khác chỉ vẽ ba màn hình thô ngay tuần đầu: đăng ký, điểm danh, đồng bộ dữ liệu. Đưa ra test với stakeholder, lộ ngay constraint về offline và online.
👉 Sai sớm, nhưng cứu team cả tháng trời.

2. **Sai lầm thường gặp (Fail Late)**
✖ Cách làm sai của nhiều BA:
- Cầu toàn, “đợi đủ yêu cầu mới dám vẽ flow”.
- Chạy theo format SRS, viết dài; stakeholder đọc không hết, góp ý thì đã muộn.
- Ngại cho DEV và QC review sớm vì sợ “bị chê non tay”.
- Sợ bị khách hàng chỉnh tới chỉnh lui nên giữ im luôn, đến khi build xong mới bung, vừa tốn effort vừa mất uy tín.

Kết quả: dự án chỉ “fail late”, tức là fail trong giai đoạn đã commit effort, tốn tiền, tốn deadline.

3. **Cách làm đúng – Tư duy Fail Fast của Senior BA**
Cách làm đúng là chủ động dựng kịch bản sai ngay từ đầu để lộ bug tư duy.
■ Rapid Prototyping
Vẽ wireframe hoặc mô hình thô, chưa cần pixel perfect. Mục tiêu là ép stakeholder nhìn và phản ứng.
Ví dụ: với hệ thống thanh toán, vẽ hai flow “thành công” và “thất bại”. Khách sẽ bật ra: “Nếu thất bại thì phải hoàn tiền sau 24 giờ.” → Requirement mới.

■ Assumption Log
Ghi công khai mọi giả định: “Giả định 1: khách hàng luôn có internet khi điểm danh.”
Đưa stakeholder confirm. Nếu họ phủ nhận, fail ngay, còn hơn fail sau ba tháng code.
■ Counter-case Workshop
Lấy flow chính, nhờ DEV và QC “phá” bằng các case cực đoan.
Ví dụ: “Điểm danh offline trong bảy ngày liên tiếp không sync được thì sao?” → Stakeholder lộ constraint, team fix sớm.
“Fail Fast không giết dự án, ngược lại, nó cứu dự án khỏi ảo tưởng.”


---

## DAY 97/100 — 10 SAI LẦM CỦA BA LEADER LÀM TỤT NĂNG LƯỢNG ĐỘI NGŨ

*Trang 231–232*

Một BA Leader giỏi không chỉ viết requirement, mà còn biết giữ nhịp năng lượng cho cả team. Nếu bạn chỉ tập trung vào tài liệu mà quên cách dẫn dắt, sớm muộn gì đội ngũ cũng kiệt sức.

1. **Biến mọi việc thành “cháy nhà”**
Sai lầm: ngày nào cũng có việc “gấp”, task nào cũng “khẩn”.
Hệ quả: team chai lì, mất phân biệt thật giả, không còn phản ứng nhanh với sự cố thật sự.
Cách đúng: thiết lập thang mức độ (ví dụ: P0 – ảnh hưởng sản xuất, P1 – ảnh hưởng nhóm khách hàng, P2 – ảnh hưởng nội bộ). Chỉ gọi “khẩn cấp” với P0.

2. **Không làm rõ ưu tiên**
Sai lầm: mọi feature đều được gắn nhãn “quan trọng”.
Hệ quả: team bối rối, nỗ lực dàn trải, kết quả không đâu ra đâu.
Cách đúng: sử dụng tiêu chí định lượng: tác động đến mục tiêu kinh doanh, số lượng người dùng bị ảnh hưởng, giá trị đem lại. Công khai bảng xếp hạng ưu tiên để cả team có cùng “kim chỉ nam”.

3. **Điều hành vi mô**
Sai lầm: soi từng field trên thiết kế, comment từng dòng subtask.
Hệ quả: dev mất tự chủ, BA Lead kiệt sức, niềm tin lẫn nhau giảm sút.
Cách đúng: đặt rõ ràng “định nghĩa hoàn thành” (ví dụ: use case chạy end-to-end, không còn exception chưa xử lý). Sau đó giao quyền cho dev, QC quyết định cách triển khai chi tiết.

4. **Bỏ quên sự ghi nhận**
Sai lầm: chỉ thấy bug, quên thấy nỗ lực.
Hệ quả: người giỏi dễ nản, mất động lực ở những chặng marathon dài.
Cách đúng: ghi nhận cụ thể và công khai. Ví dụ: “Nhờ bạn bắt sớm lỗi A nên tránh được rollback, tiết kiệm 2 ngày.” Một lời khen đúng lúc giá trị hơn cả incentive.

5. **Dung túng hành vi độc hại**
Sai lầm: để một “cá nhân ngôi sao” nhưng thường xuyên tiêu cực, đổ lỗi.
Hệ quả: cả team mất năng lượng, văn hóa làm việc bị bào mòn.
Cách đúng: đặt nguyên tắc ứng xử rõ ràng ngay từ đầu. Khi vi phạm, trao đổi riêng, tập trung vào hành vi cụ thể. Nếu tái diễn, cần quyết liệt bảo vệ tập thể.

6. **Che mất bức tranh lớn – không rõ ràng mục tiêu**
Sai lầm: team chỉ thấy ticket Jira, không thấy mục tiêu.
Hệ quả: công việc biến thành gánh nặng máy móc.
Cách đúng: luôn trả lời câu hỏi “tại sao”. Mỗi feature cần có lý do kinh doanh, kết quả mong đợi, và cách đo lường thành công. Khi hiểu được bức tranh lớn, task nhỏ cũng mang ý nghĩa.

7. **Gật đầu với mọi thứ**
Sai lầm: bất kỳ yêu cầu nào từ khách hàng hay sếp cũng được đồng ý.
Hệ quả: backlog phình to, scope vỡ, team biến thành “thùng rác yêu cầu”.
Cách đúng: tập thói quen nói “Không có lý lẽ”. Ví dụ: “Nếu nhận thêm yêu cầu này, sprint sẽ trễ 3 ngày, và ảnh hưởng tính năng kia. Anh/chị muốn đổi ưu tiên hay chờ sang sprint sau?”

8. **Bỏ qua 1-1**
Sai lầm: chỉ gặp nhân sự khi có lỗi.
Hệ quả: team không có cơ hội chia sẻ khó khăn thật sự, BA Lead mất sự gắn kết.
Cách đúng: lên lịch 1-1 định kỳ. Nội dung không chỉ xoay quanh công việc, mà còn hỏi về khó khăn, mong muốn phát triển. Người giỏi ở lại vì họ thấy mình “được nhìn thấy”.

9. **Né tránh phản hồi khó**
Sai lầm: trì hoãn, ngại va chạm.
Hệ quả: vấn đề tích tụ, niềm tin sụp đổ.
Cách đúng: góp ý sớm, riêng tư, cụ thể. Thay vì “Em làm việc chưa tốt”, hãy nói: “Trong buổi họp hôm qua, khi em cắt ngang dev, team đã khó chia sẻ. Lần sau em thử lắng nghe hết rồi phản hồi nhé.”

10. **Không bao giờ nghỉ**
Sai lầm: lúc nào cũng online, nhắn tin kể cả nửa đêm.
Hệ quả: team nghĩ “Leader không nghỉ thì mình cũng không được nghỉ”, kết quả burnout tập thể.
Cách đúng: nêu gương. Tắt thông báo ngoài giờ, để chế độ bàn giao on-call. Khi leader biết nghỉ, team mới dám nghỉ.
“Năng lượng đội ngũ không tự sinh ra – nó được thiết kế bởi cách Leader dẫn dắt.”


---

## DAY 98/100 — PHÂN BIỆT AUTO-SUGGEST, AUTO-COMPLETE, ML-BASED RECOMMENDATION VÀ CÁCH VIẾT YÊU CẦU ĐÚNG BẢN CHẤT

*Trang 233–234*

“Em viết requirement: nhập chữ thì hệ thống gợi ý ra vài từ. Dev hỏi: gợi ý kiểu gì?
Em bảo: thì giống Google thôi ạ!”
👉 Vậy là xong. Dự án… đi đâu không biết.
✖ Khi BA viết “gợi ý” nhưng không phân biệt bản chất
Ví dụ: “Hệ thống gợi ý từ phù hợp khi người dùng nhập liệu.”
Nhưng không nói rõ: gợi ý dựa vào đâu. Cơ chế là rule hay machine learning. Kết quả có sắp xếp không. Bao nhiêu ký tự thì bắt đầu gợi ý.
👉 Dev sẽ tự đoán, hoặc hỏi đi hỏi lại, hoặc làm xong thì bị business bác bỏ. Cả ba đều toang.
■ Bốn khái niệm BA cần hiểu rõ
**Auto-complete**
- Gợi ý để hoàn tất chuỗi đang gõ.
- Dựa trên ký tự đầu (prefix).
- Dùng trong ô tìm kiếm, form địa chỉ.

**Auto-suggest**
- Gợi ý các lựa chọn liên quan.
- Không nhất thiết trùng prefix.
- Dùng trong chọn tag, danh mục.

**ML-based recommendation**
- Gợi ý theo hành vi người dùng, không cần nhập gì.
- Dùng machine learning để cá nhân hóa.
- Ứng dụng: gợi ý sản phẩm, gợi ý bài viết.

**Manual rule-based suggestion**
- Gợi ý theo danh sách cố định do admin cấu hình.
- Không dùng AI.

Ví dụ: gợi ý mẫu nội dung khi gửi yêu cầu.
● Phân biệt bằng ví dụ
Auto-complete: gõ “Pho” → gợi ý “Phở bò”, “Phở gà”, “Phở cuốn”.
Auto-suggest: gõ “đói bụng” → gợi ý “Phở”, “Cơm tấm”, “Bánh mì”.
Recommendation: không gõ gì → gợi ý “Bạn từng ăn Phở bò, thử Bún bò Huế nhé.”
Manual rule: gõ “phản hồi chậm” → gợi ý “Bạn có thể liên hệ CSKH.”
■ Cách viết requirement không bị mơ hồ
Trigger: nhập mấy ký tự thì gợi ý, có delay không.
Cơ chế lọc: prefix match, full-text, synonym hay AI.
Nguồn dữ liệu: từ DB, từ cấu hình thủ công hay từ AI model.
Cập nhật dữ liệu: có cần thao tác gì từ admin không.
UI hiển thị: dropdown, bao nhiêu dòng, có scroll không.
Fallback: không có kết quả thì hiển thị gì.
📌 Năm câu hỏi khi khảo sát tính năng gợi ý
Gợi ý có cá nhân hóa theo người dùng không.
Có cần học từ hành vi trước đó không.
Khi chưa gõ gì, có hiển thị gợi ý mặc định không.
Admin có cần cấu hình thủ công danh sách gợi ý không.
Gợi ý có phân loại không, ví dụ tag, nhóm.
Bạn đã từng hiểu sai giữa auto-complete và recommendation chưa.
Chia sẻ một tình huống bạn từng gặp để mọi người cùng học nhé.


---

## DAY 99/100 — OUTCOME VÀ OUTPUT: ĐỪNG NHẦM LẪN GIỮA "BẬN RỘN" VÀ "HIỆU QUẢ"

*Trang 235*

Có một kiểu “ngụy biện” rất phổ biến trong nghề BA:
“Em làm xong 10 use case rồi.”
“Em refine đủ backlog cho sprint này rồi.”
“Tuần vừa rồi em họp với khách hàng 8 buổi.”
Nghe thì căng như dây đàn. Nhưng business hỏi ngược lại: “Thế sau từng ấy việc, chúng ta đạt được điều gì?” Và lúc đó, nhiều bạn… cứng họng.
✖ **Sai lầm chết người**
Bạn nhầm Output với Outcome.
- Output = Thứ bạn sản xuất ra: tài liệu, backlog, wireframe, meeting note…
- Outcome = Thứ business đạt được: tăng doanh thu, giảm chi phí, nâng trải nghiệm khách hàng, rút ngắn lead time…

Làm nhiều chưa chắc tạo ra giá trị. Bận rộn không có nghĩa là hiệu quả.
■ **Nghĩ như BA thực chiến**
BA không chỉ là “task owner”, mà là người giữ cầu nối giá trị. Bạn viết requirement để làm gì? Để:
- UC đó cắt được thời gian nhập liệu từ 5 phút xuống còn 2 phút.
- Rule đó giảm được 30% lỗi nhập sai số.
- Flow đó giữ lại 15% khách hàng vốn định bỏ ngang giỏ hàng.

Nếu bạn không chứng minh được mối quan hệ này, mọi output của bạn đều là giấy vụn.
● Làm sao để có Outcome – dễ hiểu, áp dụng ngay
1. Đừng hỏi: mình làm gì? → Hãy hỏi: việc này giải quyết nỗi đau nào?
   - Viết UC nhập dữ liệu → Giảm thời gian nhập từ 5 phút còn 2 phút.
   - Thiết kế dashboard → Giúp sếp ra quyết định nhanh, không phải lục excel.
2. Luôn dịch task sang “lợi ích”
   - Viết: “Tôi đã hoàn thành 10 backlog item.” → Không ai quan tâm.
   - Viết: “10 backlog này giúp hệ thống không còn lỗi double booking.” → Đây mới là outcome.
3. Nghĩ như khách hàng
   - Khách hàng không quan tâm bạn họp mấy buổi, viết mấy chục trang SRS.
   - Họ chỉ quan tâm: Hệ thống này có làm đời họ dễ thở hơn không?


---

## DAY 100/100 — 10 NĂM LÀM NGHỀ – TÔI GIỮ LẠI ĐÚNG 3 THỨ: MINDSET, HỆ THỐNG VÀ BẢN LĨNH

*Trang 236–237*

Sau 10 năm làm BA, tôi không giữ được nhiều…
Không giữ được hết những người từng đồng hành.
Không giữ được toàn bộ dự án từng làm.
Cũng không giữ được sức trẻ như ngày đầu bước vào nghề.
Nhưng có 3 thứ tôi giữ rất chặt – vì nếu mất, tôi không thể đi tiếp với nghề này.

Tôi từng nhận một dự án giữa chừng – BA trước nghỉ ngang, không tài liệu.
Chỉ có một đống ticket dev đang làm dở, và khách hàng đang nổi giận. Không thể hỏi ai, không thể trách ai. Tôi ngồi lại, lần từng dấu vết, vẽ lại flow từ đầu, gọi stakeholder từng người để xâu chuỗi. Có lúc muốn gục. Nhưng cũng chính lúc đó, tôi nghiệm ra:
**Không ai cứu mình ngoài chính mình – và thứ mình đã rèn trước đó.**

Tôi đã từng:
- Đi họp mà không dám nói, sợ sai.
- Viết tài liệu mà không có cấu trúc – hôm sau nhìn lại còn không hiểu nổi.
- Dựng giải pháp mà không dám bảo vệ khi bị ép đổi xoành xoạch.

Tôi tưởng mình "linh hoạt", "biết điều".
Thực ra là thiếu tư duy, thiếu hệ thống, thiếu bản lĩnh.

Làm nghề này mà:
- Không rèn tư duy phân tích → Rất dễ bị dắt mũi bởi những lời nói mơ hồ.
- Không xây hệ thống cá nhân → Lúc nào cũng bắt đầu lại từ số 0.
- Không có bản lĩnh → Rất dễ thành cái bóng, viết theo người khác, sống bằng deadline chứ không sống bằng chuẩn nghề.

Tôi không nói bạn phải "cứng đầu".
Nhưng nếu bạn không có cái lõi bên trong, bạn sẽ lắc theo mọi luồng gió trong dự án.
Và chẳng ai nhớ bạn đã từng làm gì.

■ 3 thứ đáng giữ lại
1. **Mindset – Tư duy rõ ràng**
   - Không chạy theo lời người khác.
   - Luôn hỏi: "Vấn đề gốc là gì?" trước khi viết bất kỳ requirement nào.
   - Biết nhìn từ hệ thống, không chỉ từ từng ticket lẻ.
2. **Hệ thống – Để không bị cuốn theo deadline**
   - Tôi tự tạo template, checklist, mẫu flow, form phân tích.
   - Dự án nào cũng có thể reuse.
   - Không còn cảnh mỗi lần đổi team là bắt đầu lại từ đầu.
3. **Bản lĩnh – Dám nói điều đúng**
   - Tôi không nói “gân cổ cãi”.
   - Tôi nói: khi nào cần nói. Và nói được bằng lý do rõ ràng.
   - Bản lĩnh không phải là phản kháng. Mà là vững vàng.

💭 Làm nghề lâu không có nghĩa là trưởng thành. Nhưng giữ được những thứ đúng – thì không thể không lớn.
