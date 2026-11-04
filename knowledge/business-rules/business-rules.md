# 📋 Business Rules — Quy Tắc Nghiệp Vụ Đã Xác Nhận

> **Nguồn:** Trích xuất từ [SRC-07: fintech-knowledge-base.md](file:///f:/knowledge/product/fintech-knowledge-base.md)
> **Trạng thái:** Draft — cần Human xác nhận với stakeholder và bộ phận pháp lý
> **Quy tắc:** AI KHÔNG ĐƯỢC tự bịa quy tắc nghiệp vụ. Mọi rule phải có nguồn trích dẫn.

---

## 1. Quy Tắc Mua Vé

| ID | Quy tắc | Nguồn | Trạng thái |
|----|---------|-------|-----------|
| BR-001 | Người chơi phải hoàn tất eKYC trước khi mua vé lần đầu | SRC-07, §6 | [⚠️ CẦN XÁC NHẬN] |
| BR-002 | Chặn giao dịch mua vé trong 30 giây cuối trước khi đóng kỳ quay (quy tắc T-30s) | SRC-07, §1.4 | [⚠️ CẦN XÁC NHẬN] |
| BR-003 | Mỗi kênh bán có mã kênh riêng gắn trên vé để đối soát | SRC-07, §4 | [⚠️ CẦN XÁC NHẬN] |
| BR-004 | Bingo18: 159 kỳ/ngày, mỗi kỳ cách 6 phút — áp lực TPS cao nhất | SRC-07, §1.4 | [✅ ĐÃ XÁC NHẬN] |

## 2. Quy Tắc Thanh Toán

| ID | Quy tắc | Nguồn | Trạng thái |
|----|---------|-------|-----------|
| BR-010 | Thanh toán qua PayByToken: không yêu cầu nhập lại thông tin thẻ/ví | SRC-07, §2 | [⚠️ CẦN XÁC NHẬN] |
| BR-011 | Một số kênh hỗ trợ Bypass OTP cho giao dịch nhỏ | SRC-07, §2 | [⚠️ CẦN XÁC NHẬN — cần xác nhận ngưỡng] |
| BR-012 | Hạn mức dự thưởng (HMDT) = số dư khả dụng trong TKDT | SRC-07, §11 | [⚠️ CẦN XÁC NHẬN] |

## 3. Quy Tắc Trả Thưởng

| ID | Quy tắc | Nguồn | Trạng thái |
|----|---------|-------|-----------|
| BR-020 | Giải nhỏ: Auto-payout — tự động trừ thuế TNCN và cộng vào TKNT | SRC-07, §5 | [⚠️ CẦN XÁC NHẬN — ngưỡng giải nhỏ?] |
| BR-021 | Giải lớn: Cần xác nhận thủ công qua Admin trước khi chi hộ (disbursement) | SRC-07, §5 | [⚠️ CẦN XÁC NHẬN — ngưỡng giải lớn?] |

## 4. Quy Tắc Đối Soát

| ID | Quy tắc | Nguồn | Trạng thái |
|----|---------|-------|-----------|
| BR-030 | Đối soát giữa Vietlott SMS và kênh bán theo chu kỳ (T+1 hoặc T+0) | SRC-07, §4 | [⚠️ CẦN XÁC NHẬN — chu kỳ chính xác?] |
| BR-031 | Hệ thống sử dụng Kế toán kép (Double-Entry Ledger) cho mọi giao dịch tài chính | SRC-07, §1.3 | [✅ ĐÃ XÁC NHẬN] |

## 5. Quy Tắc Bảo Mật & Pháp Lý

| ID | Quy tắc | Nguồn | Trạng thái |
|----|---------|-------|-----------|
| BR-040 | Tuân thủ QĐ 2345/QĐ-NHNN về an toàn bảo mật thanh toán trực tuyến | SRC-07, §7 | [✅ ĐÃ XÁC NHẬN] |
| BR-041 | Mã hóa dữ liệu nhạy cảm bằng PGP RSA-3072 | SRC-07, §9 | [⚠️ CẦN XÁC NHẬN] |
| BR-042 | eKYC bằng FaceID/Face Matching cho xác thực sinh trắc học | SRC-07, §6 | [⚠️ CẦN XÁC NHẬN] |

---

> [!IMPORTANT]
> Các rule đánh dấu `[⚠️ CẦN XÁC NHẬN]` chưa được stakeholder ký duyệt.
> AI **PHẢI** gắn nhãn giả định khi sử dụng các rule này trong output.
