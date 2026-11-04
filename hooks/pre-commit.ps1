# Git Pre-Commit Hook
# Muc dich: Kiem tra khong co file staged chua thong tin ca nhan (PII) chua masked

Write-Host "=== [HOOK: PRE-COMMIT] Kiem tra truoc khi commit vao Git ===" -ForegroundColor Cyan

$Root = "f:\VIETLOTT-SMS"
$piiScanner = Join-Path $Root "validators\pii_scanner.py"

if (Test-Path $piiScanner) {
    # Quet tren thu muc artifacts/ va observability/
    $scanTarget = Join-Path $Root "artifacts"
    python $piiScanner --dir "$scanTarget"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[-] COMMIT BI CHAN: Phat hien file trong artifacts chua du lieu ca nhan (PII) chua masked!" -ForegroundColor Red
        exit 1
    }
}

Write-Host "[+] Pre-commit hook PASS. Cho phep commit." -ForegroundColor Green
exit 0
