$Root = "f:\VIETLOTT-SMS"
$legacyDir = Join-Path $Root "_legacy_backup"

if (-not (Test-Path $legacyDir)) {
    New-Item -ItemType Directory -Path $legacyDir -Force | Out-Null
}

$folders = @('00_Draft', '01_Requirements', '02_Design', '03_Workspace', '04_Document', '05_Meetings', '06_Testing', '07_Scripts', '08_Template')

foreach ($f in $folders) {
    $src = Join-Path $Root $f
    if (Test-Path $src) {
        Move-Item -Path $src -Destination $legacyDir -Force
        Write-Host "Moved $f to _legacy_backup"
    }
}
Write-Host "Archiving completed successfully!"
