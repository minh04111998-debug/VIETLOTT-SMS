# Post-Task Lifecycle Hook
# Muc dich: Kiem tra chat luong artifact (Ambiguity, PII, Banned words), xuat Gate Report, va chan thuc thi neu FAIL

param(
    [string]$ArtifactPath = "",
    [string]$Role = "ba",
    [string]$Feature = "general",
    [switch]$FromStdin = $false,
    [switch]$NonBlocking = $false
)

$Root = Split-Path -Parent $PSScriptRoot
if (-not (Test-Path (Join-Path $Root "artifacts"))) {
    $Root = "f:\VIETLOTT-SMS"
}

# Ho tro doc payload tu hook stdin chi khi duoc chi dinh co
if ($FromStdin) {
    try {
        $stdinContent = [Console]::In.ReadLine()
        if ($stdinContent) {
            $jsonInput = ConvertFrom-Json $stdinContent -ErrorAction SilentlyContinue
            if ($jsonInput -and $jsonInput.toolCall -and $jsonInput.toolCall.args -and $jsonInput.toolCall.args.TargetFile) {
                $ArtifactPath = $jsonInput.toolCall.args.TargetFile
            }
        }
    } catch {}
}

Write-Host "=== [HOOK: POST-TASK] Kiem tra chat luong va sinh Gate Report ===" -ForegroundColor Cyan

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$reportDate = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

if (-not $ArtifactPath -or -not (Test-Path $ArtifactPath)) {
    Write-Host "[!] Khong co Artifact cu the hop le duoc chi dinh. Bo qua kiem tra sau task." -ForegroundColor Yellow
    if ([Console]::IsInputRedirected) { [Console]::Out.WriteLine("{}") }
    exit 0
}

Write-Host "[*] Dang kiem tra artifact: $ArtifactPath"

# 1. Chay ambiguity scanner
$ambiguityScanner = Join-Path $Root "validators\ambiguity_scanner.py"
$ambiguityOutput = ""
$ambiguityPass = $true
if (Test-Path $ambiguityScanner) {
    Write-Host "  -> Chay Quet Tu Mo Ho (Ambiguity Scanner)..."
    $ambiguityOutput = python $ambiguityScanner --file "$ArtifactPath" 2>&1 | Out-String
    if ($ambiguityOutput -match "Found \d+ ambiguous issues") {
        $ambiguityPass = $false
        Write-Host "  [-] Phat hien tu mo ho trong tai lieu!" -ForegroundColor Red
    } else {
        Write-Host "  [+] Ambiguity Scan: PASS" -ForegroundColor Green
    }
}

# 2. Chay PII scanner
$piiScanner = Join-Path $Root "validators\pii_scanner.py"
$piiOutput = ""
$piiPass = $true
if (Test-Path $piiScanner) {
    Write-Host "  -> Chay Quet Du Lieu Nhay Cam (PII Scanner)..."
    $piiOutput = python $piiScanner --file "$ArtifactPath" 2>&1 | Out-String
    if ($LASTEXITCODE -ne 0) {
        $piiPass = $false
        Write-Host "  [-] Phat hien du lieu ca nhan (PII) chua masked!" -ForegroundColor Red
    } else {
        Write-Host "  [+] PII Scan: PASS" -ForegroundColor Green
    }
}

# 3. Chay banned words validator
$bannedWordsValidator = Join-Path $Root "validators\banned_words_validator.py"
$bannedWordsOutput = ""
$bannedWordsPass = $true
if (Test-Path $bannedWordsValidator) {
    Write-Host "  -> Chay Kiem Tra Tu Cam (Banned Words Validator)..."
    $bannedWordsOutput = python $bannedWordsValidator --file "$ArtifactPath" 2>&1 | Out-String
    if ($LASTEXITCODE -ne 0) {
        $bannedWordsPass = $false
        Write-Host "  [-] Phat hien tu cam nghiep vu!" -ForegroundColor Red
    } else {
        Write-Host "  [+] Banned Words Scan: PASS" -ForegroundColor Green
    }
}

# 4. Sinh Gate Report trong observability/gate-reports/
$overallStatus = if ($ambiguityPass -and $piiPass -and $bannedWordsPass) { "PASS" } else { "FAIL" }
$artifactBase = [System.IO.Path]::GetFileNameWithoutExtension($ArtifactPath)
$reportFileName = "QGR-$timestamp-$Role-$artifactBase.md"
$reportPath = Join-Path $Root "observability\gate-reports\$reportFileName"

$conc = if ($overallStatus -eq "PASS") {
    "- [x] Tai lieu dat chuan. Duoc phep ban giao downstream role hoac trinh ky duyet."
} else {
    "- [ ] BLOCKING: Can chinh sua cac vi pham tren truoc khi ban giao hoac baseline."
}

$artifactCode = '`' + $ArtifactPath + '`'
$fence = '```text'
$closeFence = '```'

$reportContent = @"
# Quality Gate Report - $(Split-Path $ArtifactPath -Leaf)

> **Ma bao cao:** QGR-$timestamp-$Role  
> **Thoi gian kiem tra:** $reportDate  
> **Vai tro thuc thi:** $Role  
> **Ket qua tong the:** **[$overallStatus]**  

---

## 1. Thong Tin Kiem Tra
- **Artifact:** $artifactCode
- **Quet tu mo ho (Ambiguity):** $(if ($ambiguityPass) { "PASS" } else { "FAIL" })
- **Bao mat du lieu (PII):** $(if ($piiPass) { "PASS" } else { "FAIL" })
- **Tu cam nghiep vu (Banned words):** $(if ($bannedWordsPass) { "PASS" } else { "FAIL" })

---

## 2. Chi Tiet Ket Qua Quet Tu Dong

### Ambiguity Scanner Output:
$fence
$ambiguityOutput
$closeFence

### PII Scanner Output:
$fence
$piiOutput
$closeFence

### Banned Words Output:
$fence
$bannedWordsOutput
$closeFence

---

## 3. Ket Luan & Buoc Tiep Theo
$conc
"@

[System.IO.File]::WriteAllText($reportPath, $reportContent, (New-Object System.Text.UTF8Encoding($false)))
Write-Host "[+] Da luu Gate Report tai: observability/gate-reports/$reportFileName" -ForegroundColor Green

if ($overallStatus -ne "PASS") {
    Write-Host "=== Post-task hook that bai: [$overallStatus] ===" -ForegroundColor Red
    if (-not $NonBlocking) {
        Write-Host "[-] BLOCKING: Quality Gate yeu cau sua cac vi pham truoc khi tiep tuc!" -ForegroundColor Red
        if ([Console]::IsInputRedirected) { [Console]::Out.WriteLine("{}") }
        exit 1
    }
}

Write-Host "=== Post-task hook hoan tat voi trang thai: [$overallStatus] ===" -ForegroundColor Green
if ([Console]::IsInputRedirected) { [Console]::Out.WriteLine("{}") }
exit 0
