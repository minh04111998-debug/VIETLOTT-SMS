# Fintech Knowledge: Trả Thưởng & Chi Hộ (Disbursement)

| Version | Ngày | Người thực hiện | Trạng thái |
|:---:|:---:|:---:|---|
| 1.0 | 2026-10-08 | BA / Fintech Knowledge Team | Approved |

> **Mã module:** `KB-FINTECH-04`  
> **Thuộc hệ thống:** Kiến trúc Tri thức Fintech Vietlott SMS  
> **Master Index:** [fintech-knowledge-base.md](file:///f:/VIETLOTT-SMS/knowledge/product/fintech-knowledge-base.md)

---

## 5. Trả thưởng & Chi hộ (Disbursement)

### 5.1. Quy trình trả thưởng tổng quan (5 bước)

Trích xuất từ tài liệu Confluence gốc `13.Quản lý Trúng thưởng - Trả thưởng`:

| Bước | Tên bước | Đối tượng thực hiện | Mô tả |
|------|----------|---------------------|-------|
| **1** | Trả kết quả trúng thưởng | **BGT** | Sau khi có KQQSMT mỗi kỳ quay, hệ thống BGT gửi file kết quả trúng thưởng cho từng đại lý |
| **2** | Phê duyệt kết quả trúng thưởng | **Vận hành nghiệp vụ** | Kiểm tra thông tin kỳ quay, Game, vé trúng có phải do đại lý phát hành → phê duyệt file dữ liệu |
| **3.1** | Xử lý trả thưởng mức trung bình/thấp | **Vận hành nghiệp vụ** | Xử lý vé chưa đủ điều kiện, lập lệnh phê duyệt trả thưởng cho Kế toán duyệt |
| **3.2** | Trả thưởng mức cao (> 10 tỷ) | **Vietlott** | Vietlott trực tiếp thực hiện chi trả cho khách hàng |
| **4** | Phê duyệt lệnh trả thưởng | **Kế toán** | Kế toán xem xét và phê duyệt lệnh do vận hành tạo |
| **5** | Cập nhật kết quả trả thưởng | **Vận hành nghiệp vụ** | Cập nhật kết quả (upload sao kê cho GD thủ công), xử lý GD thất bại |

> [!IMPORTANT]
> **Quy tắc nghiệp vụ:** Lệnh trả thưởng phải tách thành **2 cấp: Tạo → Duyệt**. Với chuyển tiền tự động qua VPBank là TK NH → TK NH; qua ViettelPay là ví → ví.

> **Nguồn:** [13.Quản lý Trúng thưởng - Trả thưởng.doc](file:///f:/VIETLOTT-SMS/artifacts/requirements/VIETLOTT%20SMS_%20Tài%20liệu%20nghiệp%20vụ/VIETLOTTSMS_ADMIN/Cập%20nhật%2001.12.2025/13.+Quản+lý+Trúng+thưởng+-+Trả+thưởng.doc)

### 5.2. Quy tắc tính thưởng

**Mega 6/45 & Power 6/55 (Nhóm Ma trận):**
- **Rule 1 — Chỉ nhận giải cao nhất** trên 1 tờ vé chuẩn (ngoại lệ: vé Bao cộng gộp)
- **Rule 2 — Chia đều nồi tiền (Pari-Mutuel)**: Nhiều người trúng Jackpot → chia đều theo tỷ lệ tiền mua
- **Rule 3 — Nhân tài khoản (Fixed Multiplier)**: Giải phụ = giá trị cố định × số lần mua bộ số

**Max 3D/3D+/Pro (Nhóm Dãy số):**
- Trúng nhiều giải → **cộng gộp toàn bộ** (khác với nhóm Ma trận)
- Chọn 2 bộ giống nhau → giá trị **gấp đôi**

**Bingo18 (Quay nhanh):**
- Trả thưởng **tự động** ngay sau kỳ quay — cộng tiền vào HMDT
- Nghiệp vụ riêng: Kiểm tra xác nhận trả thưởng vào HMDT tách theo site nhà mạng (Mobi, Viettel, VinaPhone)

**Lotto 5/35 (Sản phẩm mới):**
- **Chia giải Độc Đắc**: Khi Jackpot > 12 tỷ mà không trúng → chia cho các giải dưới vào kỳ 21h ngày tiếp theo
- Tỷ lệ chia: Nhất (1/3), Nhì+Ba+Tư+Năm (mỗi giải 1/6)

> **Nguồn:** [bao-cao-san-pham-vietlott.md §2](file:///f:/artifacts/product/bao-cao-san-pham-vietlott.md), Thư mục [03.5.Tra_Thuong](file:///f:/VIETLOTT-SMS/artifacts/requirements/VIETLOTT_SMS/VIETLOTT_SMS/03.Business_Analysis/03.5.Tra_Thuong) — 18 file tài liệu

### 5.3. Hạn chế trả thưởng theo kênh

| Kênh | Trả thưởng vào ví? | Ghi chú |
|------|---------------------|---------|
| ZaloPay | ✅ Có (API Disbursement) | Trả tự động, KH nhận biến động số dư |
| MoMo | ✅ Có | Báo cáo số dư tài khoản chuyên chi trên MoMo |
| MobiFone Money | ❌ **KHÔNG** | Chỉ thanh toán mua vé, không chi hộ |
| PostPay | ⚠️ Manual chuyển khoản ngân hàng | Không có API disbursement tự động |
| Ngân hàng (VPBank) | ✅ Có | Chuyển khoản tự động TK NH → TK NH |
| ViettelPay | ✅ Có | Chuyển khoản ví → ví |

---
