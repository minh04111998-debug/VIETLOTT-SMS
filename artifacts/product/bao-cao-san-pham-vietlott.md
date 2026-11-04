# 📊 BÁO CÁO TÌM HIỂU SẢN PHẨM VIETLOTT

**Mã tài liệu:** `bao-cao-san-pham-vietlott.md`
**Vai trò biên soạn:** Business Analyst
**Nguồn dữ liệu tham khảo:** Cổng thông tin tổng hợp Vietlott SMS: <https://info.vietlott-sms.vn/>

## 1. TỔNG QUAN DANH MỤC SẢN PHẨM (PRODUCT LANDSCAPE)

| Sản phẩm | Cách chơi cơ bản | Kỳ quay thưởng | Phương thức quay | Cơ chế & Số lượng giải |
| :--- | :--- | :--- | :--- | :--- |
| **Mega 6/45** | Chọn 6 số từ `01-45` | 18h00 Thứ 4, 6, CN | Lồng cầu trực tiếp | **4 hạng giải** (1 Jackpot). Nhận giải cao nhất trên 1 vé. |
| **Power 6/55** | Chọn 6 số từ `01-55` | 18h00 Thứ 3, 5, 7 | Lồng cầu trực tiếp | **5 hạng giải** (2 Jackpot). Nhận giải cao nhất trên 1 vé. |
| **Max 3D / 3D+** | Chọn 1-2 bộ ba số (`000-999`) | 18h00 Thứ 2, 4, 6 | Lồng cầu trực tiếp | **4-7 hạng giải**. Trúng đồng thời các giải được cộng gộp. |
| **Max 3D Pro** | Chọn 2 bộ ba số (có thứ tự) | 18h00 Thứ 3, 5, 7 | Lồng cầu trực tiếp | **8 hạng giải**. Trúng đồng thời các giải được cộng gộp. |
| **Bingo18** | Đoán kết quả 3 lần quay số| 6 phút/kỳ (159 kỳ/ngày) | Hệ thống điện tử (RNG) | **5 cách chơi** (Ăn theo tỷ lệ cược). Không có Jackpot. |
| **Lotto 5/35** | Chọn 5 số chính (`01-35`) và 1 số đặc biệt (`01-12`) | 13h00 và 21h00 hàng ngày | Hệ thống tự động | **7 hạng giải** (1 Độc đắc). Có luật "Chia giải Độc Đắc". |

---

## 2. PHÂN TÍCH CHI TIẾT TỪNG SẢN PHẨM (PRODUCT SPECIFICATIONS)

### 2.1. Nhóm Xổ Số Ma Trận (Matrix) có giải Jackpot

#### A. Power 6/55

* **Cách chơi Cơ bản:** Người chơi lựa chọn 6 con số trong tập hợp từ `01` đến `55`.
* **Cách chơi Bao (System Play):** Trên kênh Vietlott SMS, hỗ trợ 5 mức Bao: **Bao 5, 7, 8, 9, 10** (Giới hạn tối đa Bao 10 do quy định hạn mức thanh toán qua ví điện tử/viễn thông). Không có Bao 6 vì chọn 6 số chính là 1 vé chuẩn.

  | Mức Bao | Cơ chế | Số vé sinh ra | Giá (VNĐ) |
  |---------|--------|---------------|----------|
  | **Bao 5** | Ghép 5 số cố định với 50 số còn lại | **50 vé** | 500.000 |
  | **Bao 7** | Tổ hợp chập 6 của 7 số đã chọn | **7 vé** | 70.000 |
  | **Bao 8** | Tổ hợp chập 6 của 8 số đã chọn | **28 vé** | 280.000 |
  | **Bao 9** | Tổ hợp chập 6 của 9 số đã chọn | **84 vé** | 840.000 |
  | **Bao 10** | Tổ hợp chập 6 của 10 số đã chọn | **210 vé** | 2.100.000 |

* **Quay thưởng:** 18h00 các ngày Thứ 3, Thứ 5 và Thứ 7 hàng tuần.
* **Cơ chế trúng giải:** Đặc biệt có tới 2 giải Jackpot:
  * **Jackpot 1:** Trùng khớp toàn bộ 6 con số chính (giá trị tích lũy từ 30 tỷ đồng).
  * **Jackpot 2:** Hệ thống quay thêm 1 số đặc biệt từ 49 quả bóng còn lại. Nếu trùng 5 số chính và trùng thêm con số đặc biệt này, trúng Jackpot 2 (tích lũy từ 3 tỷ đồng).
* **💡 Ví dụ thực tế:**
  * *Vé mua:* `[07 - 15 - 23 - 31 - 44 - 52]`
  * *Kết quả:* 6 số chính là `[07 - 15 - 23 - 31 - 44 - 49]`, 1 số đặc biệt là `[52]`.
  * *Kết quả dò:* Trùng 5 số chính và số còn lại trùng số đặc biệt `[52]`. Bạn đã trúng Jackpot 2.

#### B. Mega 6/45

* **Cách chơi Cơ bản:** Người chơi lựa chọn 6 con số trong tập hợp từ `01` đến `45`.
* **Cách chơi Bao (System Play):** Tương tự Power 6/55, kênh SMS hỗ trợ 5 mức Bao: **Bao 5, 7, 8, 9, 10**. Khác biệt duy nhất: Bao 5 chỉ tạo ra 40 vé (do tập hợp chỉ có 45 số, trừ 5 số đã chọn còn lại 40).

  | Mức Bao | Cơ chế | Số vé sinh ra | Giá (VNĐ) |
  |---------|--------|---------------|----------|
  | **Bao 5** | Ghép 5 số cố định với 40 số còn lại | **40 vé** | 400.000 |
  | **Bao 7** | Tổ hợp chập 6 của 7 số đã chọn | **7 vé** | 70.000 |
  | **Bao 8** | Tổ hợp chập 6 của 8 số đã chọn | **28 vé** | 280.000 |
  | **Bao 9** | Tổ hợp chập 6 của 9 số đã chọn | **84 vé** | 840.000 |
  | **Bao 10** | Tổ hợp chập 6 của 10 số đã chọn | **210 vé** | 2.100.000 |

* **Quay thưởng:** 18h00 các ngày Thứ 4, Thứ 6 và Chủ Nhật hàng tuần.
* **Cơ chế trúng giải:** So khớp không phân biệt thứ tự. Trùng từ 3 số trở lên sẽ trúng giải. Trùng 6 số trúng giải Jackpot (cộng dồn từ 12 tỷ đồng). Trúng qua hình thức chơi Bao sẽ cộng gộp giá trị tất cả các giải thành phần trúng thưởng (VD: Bao 7 trúng 4 số nhận 1.020.000đ).
* **💡 Ví dụ thực tế:**
  * *Vé mua:* `[05 - 12 - 20 - 28 - 35 - 41]`
  * *Kết quả:* `[05 - 18 - 20 - 28 - 30 - 41]`.
  * *Kết quả dò:* Trùng 4 số (`05, 20, 28, 41`). Trúng Giải Nhì (300.000 VNĐ).

#### ⚖️ Quy tắc tính thưởng chung cho Power 6/55 và Mega 6/45

> Các quy tắc dưới đây áp dụng cho cả 2 sản phẩm xổ số Ma trận 6 số (Power 6/55 và Mega 6/45).
**Rule 1: Luật "Chỉ nhận giải cao nhất" đối với 1 tờ vé chuẩn**

* *Văn bản gốc:* *"Trong trường hợp vé của người trúng thưởng trúng nhiều hạng giải thưởng thì người trúng thưởng chỉ được lĩnh một hạng giải thưởng cao nhất."*
* *Giải thích BA:* Nếu 1 tờ vé chuẩn (gồm 6 số, giá 10k) trúng Jackpot (trùng cả 6 số), tờ vé đó cũng thỏa mãn điều kiện trùng 5 số (Giải Nhất) và trùng 4 số (Giải Nhì). Tuy nhiên, hệ thống sẽ **chỉ trả tiền cho giải Jackpot**, không cộng thêm tiền giải Nhất và giải Nhì.
* *Lưu ý ngoại lệ (Edge Case):* Luật này CHỈ áp dụng cho **1 tờ vé chuẩn đơn lẻ**. Nếu khách hàng mua vé **Bao** (thực chất là mua tập hợp tổ hợp vé chuẩn gộp lại), thì các tờ vé khác nhau trong Bao đó sẽ trúng các giải khác nhau, và hệ thống **PHẢI cộng gộp** tất cả tiền thưởng của các tờ vé đó lại để trả cho khách.

**Rule 2: Luật "Chia đều nồi tiền chung" đối với giải Jackpot (Pari-Mutuel)**

* *Văn bản gốc:* *"Trong trường hợp có nhiều người trúng thưởng giải Jackpot thì giải Jackpot được chia đều theo tỷ lệ giá trị tham gia dự thưởng của người trúng thưởng."*
* *Giải thích BA:* Giải Jackpot là một "nồi tiền chung". Nếu quỹ Jackpot đang có 30 tỷ và có 3 người cùng trúng thưởng, hệ thống không trả mỗi người 30 tỷ. Thay vào đó, 3 người này sẽ phải **chia nhau** 30 tỷ đó (mỗi người 10 tỷ).
* Tỷ lệ chia dựa trên số tiền họ đã mua cho bộ số đó. Nếu cả 3 người đều mua vé mệnh giá 10k, họ chia đều 1:1:1. Nếu người A mua bộ số đó 2 lần (mất 20k), thì người A được tính là 2 phần, tổng cộng chia làm 4 phần, người A lấy 2/4.

**Rule 3: Luật "Nhân tài khoản" đối với các giải phụ (Fixed Multiplier)**

* *Văn bản gốc:* *"Giá trị lĩnh thưởng của các giải thưởng từ Giải Nhất đến Giải Ba được tính theo số lần tham gia dự thưởng (01 lần là 10.000đ) nhân với giá trị giải thưởng."*
* *Giải thích BA:* Trái ngược với Jackpot phải "chia nhau", các giải phụ (Nhất, Nhì, Ba) là những giải có **số tiền cố định** và **không giới hạn số người trúng**.
* Ví dụ: Giải Nhất của Mega 6/45 là 10 triệu đồng. Nếu bạn mua bộ số `01-02-03-04-05-06` tận **5 lần** (bạn trả 50k), và bộ số đó trúng giải Nhất. Hệ thống sẽ nhân 5 lần tiền thưởng lên cho bạn: `10 triệu x 5 = 50 triệu đồng`. Có 1000 người trúng giải Nhất thì công ty vẫn chung đủ mỗi người 10 triệu.

#### C. Lotto 5/35

> **⭐ Điểm nhấn sản phẩm mới - Lotto 5/35:** Đây là sản phẩm xổ số ma trận mới nhất được thiết kế chuyên biệt cho hệ sinh thái Vietlott SMS.
>
> * **Cách chơi cơ bản:** Chọn 5 số chính từ tập hợp `01` đến `35` và 1 số đặc biệt từ tập hợp `01` đến `12`.
> * **Kỳ quay thưởng:** Tần suất cao 2 lần/ngày (13:00 và 21:00) từ Thứ 2 đến Chủ Nhật.
> * **Cơ chế & Số lượng giải thưởng:** Cung cấp tổng cộng **7 hạng giải thưởng** (Độc Đắc, Nhất, Nhì, Ba, Tư, Năm, Khuyến khích). Hệ thống quay thưởng sẽ chọn ra 5 số chính và 1 số đặc biệt để xét giải.
> * **Tính năng đặc biệt:** Nổi bật với luật **"Chia giải Độc Đắc"** (nếu quỹ giải Độc đắc vượt 12 tỷ đồng mà không có người trúng, phần tiền này sẽ được chia rải đều cho các hạng giải dưới) và hỗ trợ **"Mua Gói"** (nuôi 1 bộ số dài kỳ).

* **Cách chơi Cơ bản:** Chọn 5 số chính (từ `01` đến `35`) và 1 số đặc biệt (từ `01` đến `12`). Mệnh giá vé cơ bản là 10.000đ.
* **Cách chơi Nâng cao (Bao số & Mua gói):**
  * **Bao số chính:** Người chơi chọn số lượng khác 5 số chính (gồm Bao 4 hoặc Bao 6 đến 15), giữ cố định 1 số đặc biệt:
    * *Bao 4:* Chọn 4 số chính + 1 số đặc biệt. Hệ thống tự động kết hợp 4 số này với 31 số còn lại để tạo thành 31 vé (Giá: 310.000đ).
    * *Bao 6 - Bao 15:* Chọn từ 6 đến 15 số chính + 1 số đặc biệt. Hệ thống tự động tạo tất cả các tổ hợp chập 5 số chính từ các số đã chọn, kết hợp với số đặc biệt để sinh ra các vé dự thưởng.
  * **Bao số đặc biệt (Bao 2 - Bao 12):** Người chơi chọn cố định 5 số chính, và chọn tập hợp số đặc biệt (từ 2 đến 12 số đặc biệt):
    * Hệ thống tự động ghép 5 số chính cố định này lần lượt với từng số đặc biệt đã chọn để sinh các vé dự thưởng. Số lượng vé sinh ra đúng bằng số lượng số đặc biệt được chọn (Giá: $N_{Số đặc biệt} \times 10.000đ$).
  * **Quy tắc loại trừ (BA Validation Rule):** Không cho phép kết hợp đồng thời cả Bao số chính và Bao số đặc biệt trong cùng một lượt mua. Chọn Bao số chính sẽ khóa tính năng chọn tập hợp số đặc biệt và ngược lại.
  * **Mua Gói (Nuôi số):** Chọn 1 bộ số yêu thích để tham gia liên tiếp N kỳ quay (tối đa 30 kỳ) và thanh toán 1 lần duy nhất. Các quy tắc nghiệp vụ (BA Rules) áp dụng cho chức năng Mua Gói:
    1. **Trúng thưởng giữa chừng:** Nếu bộ số trúng thưởng ở một kỳ bất kỳ, khách hàng nhận thưởng ngay kỳ đó. Vé vẫn tiếp tục có hiệu lực dự thưởng cho các kỳ còn lại trong gói mà không bị hủy.
    2. **Doanh thu & Sinh vé:** Khi thanh toán thành công, tiền được đưa vào trạng thái chờ. Hệ thống tự động sinh vé dự thưởng và hạch toán doanh thu vào hệ thống trước mỗi kỳ quay thay vì ghi nhận toàn bộ ngay từ đầu.
    3. **Sự cố hủy kỳ:** Nếu Vietlott hủy một kỳ quay bất kỳ (do sự cố), hệ thống sẽ tự động đẩy lùi lịch quay của các kỳ còn lại sang kỳ tiếp theo, hoặc hoàn tiền tương ứng cho kỳ bị hủy.
    4. **Giới hạn số kỳ:** Hệ thống áp dụng quy định số kỳ mua gói tối đa liên tiếp (Ví dụ: 30 kỳ) để giảm thiểu rủi ro vận hành dài hạn.
* **Quay thưởng:** 2 lần/ngày (13:00 và 21:00) từ Thứ 2 đến Chủ Nhật.
* **Cơ chế trúng giải (7 hạng giải):** Hệ thống quay ra 5 số chính + 1 **số đặc biệt**.

  | Hạng giải | Điều kiện (Số chính + Số đặc biệt) | Giá trị thưởng |
  |-----------|--------------------------------------|----------------|
  | **Độc Đắc** | 5 số chính + 1 số đặc biệt | Tối thiểu **6 tỷ** + tích lũy |
  | Nhất | 5 số chính (không cần số đặc biệt) | 10.000.000đ* |
  | Nhì | 4 số chính + 1 số đặc biệt | 5.000.000đ* |
  | Ba | 4 số chính (không cần số đặc biệt) | 500.000đ* |
  | Tư | 3 số chính + 1 số đặc biệt | 100.000đ* |
  | Năm | 3 số chính (không cần số đặc biệt) | 30.000đ* |
  | **Khuyến khích** | 2 số chính hoặc 1 số chính hoặc 0 số chính **+ số đặc biệt** | **10.000đ** |

  *(*) Giá trị cơ bản khi chưa có "Chia giải Độc Đắc". Khi Chia Độc đắc, giá trị giải sẽ tăng lên.*

* **⭐ Điểm độc đáo — "Chia giải Độc Đắc" (lần đầu tiên tại Việt Nam):** Khi giá trị Giải Độc Đắc vượt trên **12 tỷ đồng** mà không có người trúng, toàn bộ quỹ Độc đắc sẽ được chia cho khách hàng trúng từ giải Nhất đến giải Năm vào kỳ quay số **21:00 của ngày tiếp theo**.
  * **Tỷ lệ chia:** Giải Nhất (1/3 Quỹ). Giải Nhì, Ba, Tư, Năm (mỗi hạng giải nhận 1/6 Quỹ).
  * Nếu có hạng giải không có người trúng, phần tiền của hạng giải đó sẽ được chia đều cho các hạng giải còn lại (trừ Khuyến khích).
* **💡 Ví dụ thực tế:**
  * *Vé mua:* `[01 - 10 - 15 - 20 - 30]`
  * *Kết quả:* 5 số chính `[02 - 11 - 16 - 21 - 31]`, 1 số đặc biệt `[30]`
  * *Kết quả dò:* Không trùng số chính nào nhưng trùng 1 số đặc biệt `[30]`. Trúng giải Khuyến khích (10.000đ).

---

### 2.2. Nhóm Xổ Số Quay Nhanh (Fast Draw)

#### D. Bingo18 (Sản phẩm độc quyền trên Vietlott SMS)

* **Giới thiệu:** Bingo18 là sản phẩm xổ số quay nhanh liên tục **6 phút/kỳ** với **159 kỳ quay mỗi ngày**, được phát hành độc quyền duy nhất trên Vietlott SMS. Chỉ từ 10.000 đồng/vé, có cơ hội trúng thưởng gấp **120 lần** giá trị dự thưởng.
* **Cách chơi:** Hệ thống quay 3 lần, mỗi lần chọn 1 số từ 1-6 (tương tự tung 3 viên xúc xắc). **Đặc điểm cốt lõi:** Các lần quay là hoàn toàn độc lập, do đó **các số hoàn toàn có thể trùng nhau** (Ví dụ: quay ra `1-1-1` hoặc `2-5-2`). Có **5 cách chơi** độc lập:

  | # | Cách chơi | Mô tả | Giải thưởng tối đa | Lượt max/kỳ |
  |---|-----------|--------|---------------------|-------------|
  | 1 | **1 Số Trùng** | Chọn 1 con số (1-6), trúng khi kết quả có số đó xuất hiện 1/2/3 lần | 12k / 20k / 30k | 50.000 |
  | 2 | **2 Số Trùng Nhau** | Chọn 1 cặp số giống nhau (VD: hai số 3), trúng khi kết quả có ít nhất 2 số đó | **75.000đ** | 50.000 |
  | 3 | **3 Số Trùng Nhau** | Chọn 3 số giống nhau (VD: ba số 5) hoặc "3 số bất kỳ", trúng khi kết quả 3 số giống | **1.200.000đ** (đúng số) / 200.000đ (bất kỳ) | 6.000 - 25.000 |
  | 4 | **Cộng Tổng** | Đoán chính xác tổng 3 số (từ 3 đến 18) | **1.200.000đ** (Tổng 3 hoặc 18) đến 44.000đ (Tổng 10, 11) | 10.000 - 50.000 |
  | 5 | **Lớn Hòa Nhỏ** | Đoán tổng 3 số rơi vào phân vùng giá trị: **Nhỏ** (3→9), **Hòa** (10 hoặc 11), **Lớn** (12→18) | Nhỏ: 15k / Hòa: **20k** / Lớn: 15k | 50.000 |

* **Quay thưởng:** Liên tục **6 phút/kỳ**, từ 06h00 đến 21h53 hàng ngày.
* **💡 Ví dụ thực tế:**
  * *Vé mua:* Chọn cách chơi "Cộng Tổng", đặt cược vào Tổng 18 (tức là cả 3 lần quay đều ra số 6).
  * *Kết quả:* Quay ra `[6, 6, 6]`. Tổng = 18.
  * *Kết quả dò:* Trúng cách chơi Cộng Tổng 18. Nhận 1.200.000đ cho mỗi 10.000đ dự thưởng.

> [!TIP]
> **BA Insight:** Tần suất quay của Bingo18 là **6 phút/kỳ** với **159 kỳ/ngày** và mỗi kỳ có thể nhận tới 50.000 lượt mua. Đây là sản phẩm tạo áp lực lớn nhất lên hệ thống xử lý giao dịch (TPS) và SMS Gateway. DEV bắt buộc thiết kế Message Queue bất đồng bộ đạt TPS ≥ 2.000 cho luồng này.

### 2.3. Nhóm Xổ Số Dãy Số

#### E. Max 3D / 3D+ / 3D Pro

* **Cách chơi Cơ bản:** Mỗi số trong bộ ba được chọn từ 0 đến 9, tạo thành các bộ ba số từ `000` đến `999`.
  * **Max 3D:** Chọn **1 bộ** ba số.
  * **Max 3D+:** Chọn **2 bộ** ba số (VD: `123 - 456`).
  * **Max 3D Pro:** Chọn **2 bộ** ba số (VD: `123 - 456`), giải thưởng cao hơn 3D+ và có thêm giải phụ Đặc biệt.
* **Cách chơi Bao (Chỉ áp dụng cho Max 3D Pro):** Hệ thống hỗ trợ 2 hình thức chơi bao:
  1. **Bao bộ 3 số (tương đương Bao đảo chữ số):** Người chơi chọn 2 bộ ba số. Hệ thống tự động đảo vị trí các chữ số trong mỗi bộ ba số đó để tạo thành các cặp số dự thưởng.
     * *Số lượng vé & Giá tiền:* Phụ thuộc vào tính chất của các chữ số được chọn (giống nhau hay khác nhau). Do số lượng tổ hợp thay đổi theo từng bộ số chọn cụ thể nên trên giao diện App sẽ không hiển thị một mệnh giá cố định trước.
     * *💡 Ví dụ thực tế:* 
       * Nếu chọn hai bộ số là `112` và `456`:
         * Bộ thứ nhất `112` (chữ số lặp lại) sẽ tự động đảo thành 3 tổ hợp: `112`, `121`, `211`.
         * Bộ thứ hai `456` (các chữ số khác nhau hoàn toàn) sẽ tự động đảo thành 6 tổ hợp: `456`, `465`, `546`, `564`, `645`, `654`.
         * Hệ thống ghép các tổ hợp này lại tạo thành: $3 \times 6 = 18$ cặp vé dự thưởng (Ví dụ: `[112 - 456]`, `[112 - 465]`, ..., `[211 - 654]`). 
         * **Tổng tiền thanh toán:** $18 \text{ vé} \times 10.000\text{đ} = 180.000\text{đ}$.
       * Nếu chọn hai bộ số là `123` và `456` (tất cả các chữ số đều khác nhau):
         * Bộ thứ nhất `123` có 6 cách đảo; Bộ thứ hai `456` có 6 cách đảo.
         * Hệ thống ghép lại tạo thành: $6 \times 6 = 36$ cặp vé dự thưởng.
         * **Tổng tiền thanh toán:** $36 \text{ vé} \times 10.000\text{đ} = 360.000\text{đ}$.
  2. **Bao tổ hợp bộ 3 số (từ 3 đến 20 bộ số):** Người chơi chọn từ 3 đến 20 "bộ ba số" đầy đủ. Hệ thống tự động ghép các bộ này thành các cặp gồm 2 bộ ba số (có phân biệt thứ tự bộ trước - bộ sau).
     * *Số lượng vé & Giá tiền:* Tính theo công thức $N \times (N - 1)$ vé (mỗi vé 10.000đ).
     * *💡 Ví dụ thực tế:* 
       * Nếu người chơi chọn 3 bộ ba số là `123`, `456` và `789` ($N = 3$):
         * Hệ thống ghép cặp có phân biệt thứ tự để tạo ra $3 \times 2 = 6$ vé dự thưởng gồm:
           1. `[123 - 456]`
           2. `[456 - 123]` (đảo vị trí hai bộ số)
           3. `[123 - 789]`
           4. `[789 - 123]`
           5. `[456 - 789]`
           6. `[789 - 456]`
         * **Tổng tiền thanh toán:** $6 \text{ vé} \times 10.000\text{đ} = 60.000\text{đ}$ (Khớp hoàn toàn với giá trị "Bao 3 bộ 3 số" trong ảnh chụp màn hình).

> [!TIP]
> **BA Finding:** Trên website nguồn `info.vietlott-sms.vn/game_3d.html`, bảng giá "Chơi bao bộ ba số" từ mức 3 đến 7 bộ đang bị lỗi đánh máy sai lệch (bị copy nhầm cột giá từ bảng Bao chữ số). DEV/QA tuyệt đối không bám theo bảng này mà cần dùng đúng công thức toán học: `Tổng tiền = N * (N - 1) * 10.000đ`.

* **Quay thưởng:** Mỗi kỳ quay ra **20 bộ ba số** (2 giải Đặc biệt + 4 Nhất + 6 Nhì + 8 Ba).
  * Max 3D & 3D+ quay Thứ 2, 4, 6 lúc 18h00.
  * Max 3D Pro quay Thứ 3, 5, 7 lúc 18h00.

* **Cơ cấu giải thưởng:**

  **Max 3D (1 bộ ba số):**

  | Giải | Điều kiện | Giá trị (VNĐ) |
  |-------|-----------|----------------|
  | Đặc biệt | Trùng 1 trong 2 bộ quay thưởng ĐB | 1.000.000 |
  | Nhất | Trùng 1 trong 4 bộ quay thưởng Nhất | 350.000 |
  | Nhì | Trùng 1 trong 6 bộ quay thưởng Nhì | 210.000 |
  | Ba | Trùng 1 trong 8 bộ quay thưởng Ba | 100.000 |

  **Max 3D+ (2 bộ ba số):**

  | Giải | Điều kiện | Giá trị (VNĐ) |
  |-------|-----------|----------------|
  | Đặc biệt | Trùng cả 2 bộ ĐB | **1.000.000.000** (1 tỷ) |
  | Nhất | Trùng 2 trong 4 bộ Nhất | 40.000.000 |
  | Nhì | Trùng 2 trong 6 bộ Nhì | 10.000.000 |
  | Ba | Trùng 2 trong 8 bộ Ba | 5.000.000 |
  | Tư | Trùng 2 bộ bất kỳ từ ĐB/Nhất/Nhì/Ba | 1.000.000 |
  | Năm | Trùng 1 bộ Đặc biệt | 150.000 |
  | Sáu | Trùng 1 bộ Nhất/Nhì/Ba | 40.000 |

  **Max 3D Pro (2 bộ ba số — phân biệt thứ tự quay):**

  | Giải | Điều kiện | Giá trị (VNĐ) |
  |-------|-----------|----------------|
  | **Đặc biệt** | Trùng 2 bộ ĐB **đúng thứ tự quay** | **2.000.000.000** (2 tỷ) |
  | **Phụ Đặc biệt** | Trùng 2 bộ ĐB **ngược thứ tự quay** | **400.000.000** |
  | Nhất | Trùng 2 trong 4 bộ Nhất | 30.000.000 |
  | Nhì | Trùng 2 trong 6 bộ Nhì | 10.000.000 |
  | Ba | Trùng 2 trong 8 bộ Ba | 4.000.000 |
  | Tư | Trùng 2 bộ bất kỳ | 1.000.000 |
  | Năm | Trùng 1 bộ Đặc biệt | 100.000 |
  | Sáu | Trùng 1 bộ Nhất/Nhì/Ba | 40.000 |

* **Quy tắc tính thưởng riêng cho Max 3D/3D+/Pro (khác với Power/Mega):**
  * Trúng **đồng thời các giải** được **cộng gộp toàn bộ** (khác với luật "chỉ nhận giải cao nhất" của Power/Mega).
  * Nếu 3D+ hoặc Pro chọn 2 bộ ba số **giống nhau**, giá trị giải thưởng **gấp đôi** bảng trên.

* **💡 Ví dụ thực tế (Max 3D Pro):**
  * *Vé mua:* `[123 - 456]`
  * *Kết quả Đặc biệt:* `123 - 456` → Trúng **2 tỷ đồng** (đúng thứ tự quay).
  * *Kết quả Đặc biệt:* `456 - 123` → Trúng **400 triệu đồng** (ngược thứ tự quay).
