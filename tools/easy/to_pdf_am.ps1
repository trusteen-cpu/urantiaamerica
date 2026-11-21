# Easy-Reading Commentary Edition (es/fr/pt): docx -> pdf with Microsoft Word (optional step; needs Word installed).
# Usage: powershell -ExecutionPolicy Bypass -File to_pdf_am.ps1 -Lang es [-Draft] [-Only Paper-009,Foreword]
#   Converts site/<lang>/easy/files/*.docx (or tools/easy/_draft_<lang>/files with -Draft) whose PDF is missing or older.
#   Then run build_easy_am.py <lang> again: the reader shows a PDF button only for papers that have a PDF.
param([Parameter(Mandatory=$true)][ValidateSet("es","fr","pt")][string]$Lang, [switch]$Draft, [string[]]$Only)
if ($Draft) { $dir = Join-Path $PSScriptRoot "_draft_$Lang\files" } else { $dir = Join-Path $PSScriptRoot "..\..\site\$Lang\easy\files" }
$dir = Resolve-Path $dir
$word = New-Object -ComObject Word.Application
$word.Visible = $false; $word.DisplayAlerts = 0
try {
  Get-ChildItem $dir -Filter *.docx | ForEach-Object {
    $pdf = [IO.Path]::ChangeExtension($_.FullName, ".pdf")
    if ($Only -and -not ($Only | Where-Object { $_ -and $pdf -like "*$_*" })) { return }
    if (-not $Only -and (Test-Path $pdf) -and ((Get-Item $pdf).LastWriteTime -gt $_.LastWriteTime)) { return }
    $doc = $word.Documents.Open($_.FullName, $false, $true)
    $doc.SaveAs2($pdf, 17); $doc.Close(0)
    Write-Output ("pdf: " + $_.Name)
  }
} finally { $word.Quit() }
