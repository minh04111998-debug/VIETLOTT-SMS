<#
.SYNOPSIS
    Export Markdown to DOCX using Pandoc.
.DESCRIPTION
    Converts Markdown files to professional DOCX format for BA document delivery.
    Supports single file or batch conversion from a directory.
.PARAMETER InputPath
    Path to a .md file or a directory containing .md files.
.PARAMETER OutputDir
    Optional. Directory to save DOCX files. Defaults to same directory as input.
.PARAMETER ReferenceDoc
    Optional. Path to a DOCX reference/template for consistent styling.
.EXAMPLE
    .\export_docx.ps1 -InputPath "f:\VIETLOTT-SMS\04_Document\srs-feature-x.md"
    .\export_docx.ps1 -InputPath "f:\VIETLOTT-SMS\04_Document" -OutputDir "f:\VIETLOTT-SMS\04_Document\exports"
#>

param(
    [Parameter(Mandatory = $true)]
    [string]$InputPath,

    [Parameter(Mandatory = $false)]
    [string]$OutputDir = "",

    [Parameter(Mandatory = $false)]
    [string]$ReferenceDoc = ""
)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

# --- Check Pandoc ---
$pandocPath = Get-Command pandoc -ErrorAction SilentlyContinue
if (-not $pandocPath) {
    Write-Error "❌ Pandoc chưa được cài đặt hoặc không nằm trong PATH."
    Write-Output "   Tải tại: https://pandoc.org/installing.html"
    Write-Output "   Hoặc cài bằng: winget install JohnMacFarlane.Pandoc"
    exit 1
}

Write-Output "✅ Pandoc found: $($pandocPath.Source)"

# --- Collect files ---
$mdFiles = @()
if (Test-Path $InputPath -PathType Leaf) {
    if ($InputPath -match '\.md$') {
        $mdFiles += Get-Item $InputPath
    } else {
        Write-Error "❌ File không phải Markdown (.md): $InputPath"
        exit 1
    }
} elseif (Test-Path $InputPath -PathType Container) {
    $mdFiles = Get-ChildItem -Path $InputPath -Filter "*.md" -File
    if ($mdFiles.Count -eq 0) {
        Write-Warning "⚠️ Không tìm thấy file .md nào trong: $InputPath"
        exit 0
    }
    Write-Output "📂 Tìm thấy $($mdFiles.Count) file .md trong $InputPath"
} else {
    Write-Error "❌ Đường dẫn không tồn tại: $InputPath"
    exit 1
}

# --- Determine output directory ---
if ([string]::IsNullOrWhiteSpace($OutputDir)) {
    if (Test-Path $InputPath -PathType Leaf) {
        $OutputDir = Split-Path $InputPath -Parent
    } else {
        $OutputDir = $InputPath
    }
}

if (-not (Test-Path $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
    Write-Output "📁 Đã tạo thư mục output: $OutputDir"
}

# --- Convert ---
$successCount = 0
$failCount = 0

foreach ($file in $mdFiles) {
    $outputFile = Join-Path $OutputDir ($file.BaseName + ".docx")
    $args_list = @(
        $file.FullName,
        "-o", $outputFile,
        "--from", "markdown",
        "--to", "docx",
        "--toc",                          # Table of Contents
        "--toc-depth=3",                  # TOC depth
        "--highlight-style=tango",        # Code highlighting
        "--wrap=auto"
    )

    # Add reference doc for consistent styling if provided
    if (-not [string]::IsNullOrWhiteSpace($ReferenceDoc) -and (Test-Path $ReferenceDoc)) {
        $args_list += "--reference-doc=$ReferenceDoc"
    }

    try {
        Write-Output "📄 Converting: $($file.Name) → $($file.BaseName).docx"
        & pandoc @args_list 2>&1
        if ($LASTEXITCODE -eq 0) {
            $successCount++
            Write-Output "   ✅ OK → $outputFile"
        } else {
            $failCount++
            Write-Warning "   ❌ Pandoc exited with code $LASTEXITCODE"
        }
    } catch {
        $failCount++
        Write-Error "   ❌ Error: $_"
    }
}

# --- Summary ---
Write-Output ""
Write-Output "═══════════════════════════════════════"
Write-Output "📊 Kết quả: $successCount thành công, $failCount thất bại (tổng $($mdFiles.Count) file)"
Write-Output "📁 Output: $OutputDir"
Write-Output "═══════════════════════════════════════"
