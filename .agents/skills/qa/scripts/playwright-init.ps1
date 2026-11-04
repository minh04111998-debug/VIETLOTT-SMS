<#
.SYNOPSIS
    Playwright Project Initializer — Setup tự động cho QA Agent

.DESCRIPTION
    Script này tự động:
    1. Kiểm tra Node.js đã cài đặt
    2. Tạo package.json (nếu chưa có)
    3. Cài đặt @playwright/test
    4. Cài đặt browser Chromium
    5. Tạo cấu trúc thư mục tests/
    6. Copy config mẫu
    7. Verify bằng cách list tests

.USAGE
    powershell -ExecutionPolicy Bypass -File .agents/skills/qa/scripts/playwright-init.ps1

.PARAMETER ProjectRoot
    Đường dẫn root của dự án. Mặc định: thư mục hiện tại.

.PARAMETER SkipBrowserInstall
    Bỏ qua cài đặt browser (nếu đã có).

.NOTES
    QA Agent sẽ gọi script này tại Bước 1 của playwright-test workflow.
    Ref: https://playwright.dev/docs/intro
#>

param(
    [string]$ProjectRoot = (Get-Location).Path,
    [switch]$SkipBrowserInstall
)

# ============================================================
# Configuration
# ============================================================
$ErrorActionPreference = "Stop"
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$EXAMPLES_DIR = Join-Path (Split-Path -Parent $SCRIPT_DIR) "examples"
$CONFIG_TEMPLATE = Join-Path $EXAMPLES_DIR "playwright.config.example.ts"

# ============================================================
# Helper Functions
# ============================================================
function Write-Step {
    param([string]$Step, [string]$Message)
    Write-Host "`n[$Step] $Message" -ForegroundColor Cyan
}

function Write-Success {
    param([string]$Message)
    Write-Host "  ✅ $Message" -ForegroundColor Green
}

function Write-Warning {
    param([string]$Message)
    Write-Host "  ⚠️ $Message" -ForegroundColor Yellow
}

function Write-Fail {
    param([string]$Message)
    Write-Host "  ❌ $Message" -ForegroundColor Red
}

# ============================================================
# Banner
# ============================================================
Write-Host ""
Write-Host "╔══════════════════════════════════════════╗" -ForegroundColor Magenta
Write-Host "║   🎭 Playwright Project Initializer     ║" -ForegroundColor Magenta
Write-Host "║   QA Agent — Automated Setup            ║" -ForegroundColor Magenta
Write-Host "╚══════════════════════════════════════════╝" -ForegroundColor Magenta
Write-Host ""
Write-Host "Project Root: $ProjectRoot"
Write-Host ""

# ============================================================
# Step 1: Check Node.js
# ============================================================
Write-Step "1/7" "Checking Node.js..."

try {
    $nodeVersion = & node --version 2>&1
    if ($LASTEXITCODE -ne 0) { throw "Node.js not found" }

    # Extract major version
    $majorVersion = [int]($nodeVersion -replace 'v(\d+)\..*', '$1')
    if ($majorVersion -lt 18) {
        Write-Fail "Node.js $nodeVersion detected. Playwright requires Node.js >= 18."
        Write-Host "  Download: https://nodejs.org/" -ForegroundColor Yellow
        exit 1
    }
    Write-Success "Node.js $nodeVersion"
}
catch {
    Write-Fail "Node.js is not installed!"
    Write-Host "  Download: https://nodejs.org/" -ForegroundColor Yellow
    exit 1
}

# ============================================================
# Step 2: Check/Create package.json
# ============================================================
Write-Step "2/7" "Checking package.json..."

$packageJsonPath = Join-Path $ProjectRoot "package.json"
if (Test-Path $packageJsonPath) {
    Write-Success "package.json exists"
}
else {
    Write-Warning "package.json not found. Creating..."
    Push-Location $ProjectRoot
    & npm init -y 2>&1 | Out-Null
    Pop-Location
    Write-Success "package.json created"
}

# ============================================================
# Step 3: Install @playwright/test
# ============================================================
Write-Step "3/7" "Installing @playwright/test..."

Push-Location $ProjectRoot

# Check if already installed
$playwrightInstalled = $false
try {
    $packageJson = Get-Content $packageJsonPath -Raw | ConvertFrom-Json
    if ($packageJson.devDependencies -and $packageJson.devDependencies.'@playwright/test') {
        $playwrightInstalled = $true
        $installedVersion = $packageJson.devDependencies.'@playwright/test'
        Write-Success "@playwright/test $installedVersion already installed"
    }
}
catch {
    # package.json parse error — proceed with install
}

if (-not $playwrightInstalled) {
    Write-Host "  Installing..." -ForegroundColor Gray
    & npm install -D "@playwright/test" 2>&1 | ForEach-Object { Write-Host "  $_" -ForegroundColor Gray }
    if ($LASTEXITCODE -ne 0) {
        Write-Fail "Failed to install @playwright/test"
        Pop-Location
        exit 1
    }
    Write-Success "@playwright/test installed"
}

Pop-Location

# ============================================================
# Step 4: Install Chromium Browser
# ============================================================
Write-Step "4/7" "Installing Chromium browser..."

if ($SkipBrowserInstall) {
    Write-Warning "Skipped (--SkipBrowserInstall flag)"
}
else {
    Push-Location $ProjectRoot
    & npx playwright install chromium 2>&1 | ForEach-Object { Write-Host "  $_" -ForegroundColor Gray }
    if ($LASTEXITCODE -ne 0) {
        Write-Fail "Failed to install Chromium. Try: npx playwright install --with-deps chromium"
        Pop-Location
        exit 1
    }
    Write-Success "Chromium installed"
    Pop-Location
}

# ============================================================
# Step 5: Create Directory Structure
# ============================================================
Write-Step "5/7" "Creating test directory structure..."

$directories = @(
    "tests/pages",
    "tests/fixtures",
    "tests/auth",
    "tests/api",
    "test-results"
)

foreach ($dir in $directories) {
    $fullPath = Join-Path $ProjectRoot $dir
    if (-not (Test-Path $fullPath)) {
        New-Item -ItemType Directory -Path $fullPath -Force | Out-Null
        Write-Success "Created: $dir/"
    }
    else {
        Write-Host "  📁 Exists: $dir/" -ForegroundColor Gray
    }
}

# ============================================================
# Step 6: Copy Config Template
# ============================================================
Write-Step "6/7" "Setting up playwright.config.ts..."

$configDest = Join-Path $ProjectRoot "playwright.config.ts"
if (Test-Path $configDest) {
    Write-Warning "playwright.config.ts already exists — skipping (no overwrite)"
}
else {
    if (Test-Path $CONFIG_TEMPLATE) {
        Copy-Item $CONFIG_TEMPLATE $configDest
        Write-Success "Copied config template → playwright.config.ts"
    }
    else {
        Write-Warning "Config template not found at: $CONFIG_TEMPLATE"
        Write-Warning "Create playwright.config.ts manually or refer to SKILL.md §5.3"
    }
}

# ============================================================
# Step 7: Verify Installation
# ============================================================
Write-Step "7/7" "Verifying installation..."

Push-Location $ProjectRoot

try {
    $pwVersion = & npx playwright --version 2>&1
    Write-Success "Playwright version: $pwVersion"
}
catch {
    Write-Fail "Playwright verification failed"
    Pop-Location
    exit 1
}

# List tests (if any exist)
$testFiles = Get-ChildItem -Path (Join-Path $ProjectRoot "tests") -Recurse -Filter "*.spec.ts" -ErrorAction SilentlyContinue
if ($testFiles.Count -gt 0) {
    Write-Host "  Found $($testFiles.Count) test file(s):" -ForegroundColor Gray
    foreach ($f in $testFiles) {
        Write-Host "    📄 $($f.Name)" -ForegroundColor Gray
    }
}
else {
    Write-Host "  No test files yet. Use '/playwright-test generate' to create them." -ForegroundColor Gray
}

Pop-Location

# ============================================================
# Done!
# ============================================================
Write-Host ""
Write-Host "╔══════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║   🎉 Playwright Setup Complete!          ║" -ForegroundColor Green
Write-Host "╚══════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor White
Write-Host "  1. Create test files in tests/ directory" -ForegroundColor Gray
Write-Host "  2. Run: npx playwright test" -ForegroundColor Gray
Write-Host "  3. View report: npx playwright show-report" -ForegroundColor Gray
Write-Host ""
