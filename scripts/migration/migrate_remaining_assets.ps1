# Migration Script Part 2 - Complete Asset Migration into 20 Harness Components
$Root = "f:\VIETLOTT-SMS"

Write-Host "=== Bat dau di chuyen tai san con lai ===" -ForegroundColor Cyan

# 1. DIAGRAMS -> knowledge/architecture/diagrams
$diagramsDir = Join-Path $Root "knowledge\architecture\diagrams"
if (-not (Test-Path $diagramsDir)) { New-Item -ItemType Directory -Path $diagramsDir -Force | Out-Null }

Get-ChildItem -Path "$Root\00_Draft" -Include "*.drawio", "*.xml", "*.png" -File | ForEach-Object {
    Copy-Item $_.FullName $diagramsDir -Force
    Write-Host "  [OK] Diagram: $($_.Name)" -ForegroundColor Green
}

# 2. PYTHON UTILITY SCRIPTS -> scripts/
Get-ChildItem -Path "$Root\00_Draft" -Filter "*.py" -File | ForEach-Object {
    Copy-Item $_.FullName "$Root\scripts\$($_.Name)" -Force
}
Get-ChildItem -Path "$Root\07_Scripts" -Include "*.py", "*.ps1", "*.bat" -File | ForEach-Object {
    Copy-Item $_.FullName "$Root\scripts\$($_.Name)" -Force
}

# 3. REQUIREMENTS & ANALYSIS ARTIFACTS
Get-ChildItem -Path "$Root\00_Draft" -Include "*srs*.html", "*srs*.md", "*gap-analysis*.html", "*gap-analysis*.md" -File | ForEach-Object {
    Copy-Item $_.FullName "$Root\artifacts\requirements\$($_.Name)" -Force
}
Get-ChildItem -Path "$Root\00_Draft" -Include "*doi-soat*.md", "*da-*.md", "*meeting*.html" -File | ForEach-Object {
    Copy-Item $_.FullName "$Root\artifacts\analysis\$($_.Name)" -Force
}

# 4. DATA ANALYSIS & POWERBI -> artifacts/analysis/data
$dataDir = Join-Path $Root "artifacts\analysis\data"
if (-not (Test-Path $dataDir)) { New-Item -ItemType Directory -Path $dataDir -Force | Out-Null }

if (Test-Path "$Root\01_Requirements") {
    Get-ChildItem -Path "$Root\01_Requirements" | ForEach-Object {
        Copy-Item $_.FullName $dataDir -Recurse -Force
    }
}

# 5. UI/UX & DESIGN -> artifacts/technical/design
$designDest = Join-Path $Root "artifacts\technical\design"
if (-not (Test-Path $designDest)) { New-Item -ItemType Directory -Path $designDest -Force | Out-Null }

if (Test-Path "$Root\02_Design") {
    Get-ChildItem -Path "$Root\02_Design" -Exclude "adr" | ForEach-Object {
        Copy-Item $_.FullName $designDest -Recurse -Force
    }
}

# 6. BASELINE SOURCES & ARCHIVES -> knowledge/product/sources
$sourcesDest = Join-Path $Root "knowledge\product\sources"
if (-not (Test-Path $sourcesDest)) { New-Item -ItemType Directory -Path $sourcesDest -Force | Out-Null }

if (Test-Path "$Root\04_Document") {
    Get-ChildItem -Path "$Root\04_Document" -Include "*_extracted.txt", "*.rar", "*.html" | ForEach-Object {
        Copy-Item $_.FullName $sourcesDest -Force
    }
}

Write-Host "=== Hoan thanh di chuyen toan bo tai san vao 20 thu muc Harness ===" -ForegroundColor Green
