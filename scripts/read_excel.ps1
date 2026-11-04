param(
    [Parameter(Mandatory = $true)]
    [string]$FilePath
)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

if (-not (Test-Path $FilePath)) {
    Write-Error "File not found: $FilePath"
    exit 1
}

Write-Output "File found: $FilePath"

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

try {
    $wb = $excel.Workbooks.Open($filePath)
    foreach ($ws in $wb.Worksheets) {
        Write-Output "=== SHEET: $($ws.Name) ==="
        $usedRange = $ws.UsedRange
        $rows = $usedRange.Rows.Count
        $cols = $usedRange.Columns.Count
        for ($r = 1; $r -le $rows; $r++) {
            $rowData = @()
            for ($c = 1; $c -le $cols; $c++) {
                $cell = $usedRange.Cells.Item($r, $c)
                if ($null -ne $cell.Value2) {
                    $val = $cell.Value2.ToString()
                } else {
                    $val = ""
                }
                $rowData += $val
            }
            Write-Output ($rowData -join " | ")
        }
    }
    $wb.Close($false)
} finally {
    $excel.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
}
