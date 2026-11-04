# Critique Failure Hook
# Muc dich: Tu dong tao bien ban bat dong khi vong lap CRITIQUE that bai qua 2 lan

param(
    [string]$Feature = "general",
    [string]$RoleProposed = "BA",
    [string]$RoleChallenged = "QA",
    [string]$Reason = "Bat dong ve Acceptance Criteria va xu ly ngoai le"
)

Write-Host "=== [HOOK: CRITIQUE FAILURE] Kich hoat Deadlock Escalation Protocol ===" -ForegroundColor Red

$Root = "f:\VIETLOTT-SMS"
$dateStr = Get-Date -Format "yyyyMMdd"
$timeStr = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$dossierFileName = "CC-$dateStr-$Feature.md"
$dossierPath = Join-Path $Root "observability\critique-conflicts\$dossierFileName"

$content = @"
# Bien Ban Bat Dong & Be Tac (Critique Conflict Dossier)

> **Ma ho so:** CC-$dateStr-$Feature
> **Thoi diem kich hoat:** $timeStr
> **Trang thai:** 🛑 HARD STOP — Cho Human phan xu

---

## 1. Thong Tin Tong Quan
- **Tinh nang lien quan:** $Feature
- **Vai tro de xuat:** $RoleProposed
- **Vai tro phan bien:** $RoleChallenged
- **So vong lap tu sua da qua:** 2 vong (Da cham nguong gioi han toi da)

---

## 2. Noi Dung Bat Dong Chinh
- **Ly do that bai:** $Reason
- **Luan diem cua $RoleProposed:** (Can giu tinh nang / yeu cau theo mong muon ban dau)
- **Luan diem cua $RoleChallenged:** (Phat hien rui ro testability / performance / security)

---

## 3. Cac Phuong An Danh Doi (Trade-offs) Trinh Human

### Phuong An A (Uu tien toc do & pham vi):
- Chap nhan giam bot validation de phat hanh nhanh.
- Rui ro: Tang nguy co loi exception tai runtime.

### Phuong An B (Uu tien chat luong & bao mat):
- Bo sung logic xu ly ngoai le day du va tang coverage.
- Rui ro: Keo dai thoi gian phat trien (tang 2-3 Story Points).

---

## 4. Quyet Dinh Cua Human
- [ ] Phe duyet Phuong an A
- [ ] Phe duyet Phuong an B
- [ ] Chi dao khac: ................................................
- **Nguoi ky quyet dinh:** ......................... | **Ngay:** YYYY-MM-DD
"@

Set-Content -Path $dossierPath -Value $content -Encoding UTF8
Write-Host "[!] DA KHOA TIEN TRINH (HARD STOP). Ho so be tac da duoc lap tai: observability/critique-conflicts/$dossierFileName" -ForegroundColor Red
exit 0
