# Pre-Task Lifecycle Hook
# Muc dich: Kiem tra moi truong, quyen han va cac blocker truoc khi lam task

param(
    [string]$Role = "ba",
    [string]$Feature = "general"
)

$Root = Split-Path -Parent $PSScriptRoot
if (-not (Test-Path (Join-Path $Root "artifacts"))) {
    $Root = "f:\VIETLOTT-SMS"
}

Write-Host "=== [HOOK: PRE-TASK] Khoi tao kiem tra truoc khi thuc thi (Role: $Role, Feature: $Feature) ===" -ForegroundColor Cyan

$RequiredDirs = @("artifacts", "observability", "memory", "validators", "rules", "knowledge")

# 1. Kiem tra thu muc
foreach ($dir in $RequiredDirs) {
    $p = Join-Path $Root $dir
    if (-not (Test-Path $p)) {
        Write-Host "[-] Thieu thu muc bat buoc: $dir" -ForegroundColor Red
        exit 1
    }
}

# 2. Kiem tra file quy tac cua Role
$ruleFile = Join-Path $Root ".agents\rules\$Role-rules.md"
if (-not (Test-Path $ruleFile)) {
    $ruleFile = Join-Path $Root "rules\quality\$Role-rules.md"
}
if (-not (Test-Path $ruleFile)) {
    $ruleFile = Join-Path $Root "rules\product\$Role-rules.md"
}
if (-not (Test-Path $ruleFile)) {
    $ruleFile = Join-Path $Root "rules\technical\$Role-rules.md"
}

if (Test-Path $ruleFile) {
    Write-Host "[+] Nap thanh cong Rules cua Role $Role tu: $ruleFile" -ForegroundColor Green
} else {
    Write-Host "[!] Khong tim thay file rules rieng cho Role $Role. Su dung rules/global/core-principles.md." -ForegroundColor Yellow
}

# 3. Kiem tra cau hoi mo mang tinh Blocker trong open-questions.md
$openQuestionsPath = Join-Path $Root "observability\open-questions.md"
if (Test-Path $openQuestionsPath) {
    $content = Get-Content -Path $openQuestionsPath -Raw -Encoding UTF8
    if ($content -match "CO \(Blocking\).*Open") {
        Write-Host "[!] CANH BAO: Co cau hoi mo dang o trang thai BLOCKING chua duoc giai dap trong open-questions.md!" -ForegroundColor Yellow
        Write-Host "    Vui long kiem tra truoc khi dua ra quyet dinh nghiep vu quan trong." -ForegroundColor Yellow
    }
}

# 4. Khoi tao hoac cap nhat scratchpad trong memory (Append khong xoa noi dung cu)
$scratchpadPath = Join-Path $Root "memory\scratchpad.md"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$entry = @"

---
### Session: $timestamp | Role: $Role | Feature: $Feature
- **Trang thai:** In-Progress
- **Ghi chu tac vu:**

"@

if (Test-Path $scratchpadPath) {
    Add-Content -Path $scratchpadPath -Value $entry -Encoding UTF8
} else {
    $header = "# Active Scratchpad`n" + $entry
    Set-Content -Path $scratchpadPath -Value $header -Encoding UTF8
}

Write-Host "[+] Pre-task hook hoan tat. San sang thuc thi task!" -ForegroundColor Green
exit 0
