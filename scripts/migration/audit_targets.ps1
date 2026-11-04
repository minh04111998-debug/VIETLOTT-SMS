$targets = @('hooks', 'validators', 'tools', 'templates', 'references', 'scripts', 'memory', 'observability')
foreach ($t in $targets) {
    Write-Host "=== $t ===" -ForegroundColor Cyan
    $p = Join-Path 'f:\VIETLOTT-SMS' $t
    Get-ChildItem -Path $p | ForEach-Object {
        Write-Host "  - $($_.Name) ($($_.PSIsContainer))"
    }
}
