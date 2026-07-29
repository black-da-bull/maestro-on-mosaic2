<#
    rescue_skill.ps1 - preserve the recovered maestro-forensic-transcript skill
    out of the volatile Temp dir into the filestore before Windows clears it.
    ASCII-ONLY. Source is READ; only the destination (in the filestore) is written.

    USAGE
      powershell -ExecutionPolicy Bypass -File .\rescue_skill.ps1
#>

[CmdletBinding()]
param(
    [string]$Src  = 'C:\Users\gamer\AppData\Local\Temp\claude\--wsl-localhost-ubuntu-home-wsl-projects-rebirth\4abffa73-200f-4157-a2a0-ec831b9943a3\scratchpad\upload\maestro-forensic-transcript',
    [string]$Dest = 'D:\maestro-on-mosaic\_PROVENANCE\skill_recovered_2026-07-20\maestro-forensic-transcript'
)

$ErrorActionPreference = 'Stop'

Write-Host ''
Write-Host '=== rescue recovered skill from Temp ===' -ForegroundColor Cyan
Write-Host ('  src : ' + $Src)
Write-Host ('  dst : ' + $Dest)
Write-Host ''

if (-not (Test-Path -LiteralPath $Src)) {
    Write-Host '  SOURCE NOT FOUND - Temp may already have been cleared.' -ForegroundColor Red
    Write-Host '  If so, the skill is still installed as a 1-file skeleton; recovery must come'
    Write-Host '  from OneDrive web / browser history / USB (the still-manual O-03 items).'
    return
}

# inventory source (read-only)
$srcFiles = Get-ChildItem -LiteralPath $Src -Recurse -File -Force
Write-Host ('  source contains ' + $srcFiles.Count + ' file(s):')
foreach ($f in $srcFiles) {
    $kb = [math]::Round($f.Length / 1KB, 1)
    Write-Host ('    ' + $kb + ' KB  ' + $f.FullName.Substring($Src.Length).TrimStart('\'))
}

# copy into filestore
if (-not (Test-Path -LiteralPath $Dest)) { New-Item -ItemType Directory -Path $Dest -Force | Out-Null }
Copy-Item -LiteralPath $Src -Destination (Split-Path $Dest -Parent) -Recurse -Force

# verify by count + size
$dstFiles = Get-ChildItem -LiteralPath $Dest -Recurse -File -Force
$srcBytes = ($srcFiles | Measure-Object Length -Sum).Sum
$dstBytes = ($dstFiles | Measure-Object Length -Sum).Sum

Write-Host ''
Write-Host ('  copied : ' + $dstFiles.Count + ' file(s), ' + [math]::Round($dstBytes/1KB,1) + ' KB')
if ($srcFiles.Count -eq $dstFiles.Count -and $srcBytes -eq $dstBytes) {
    Write-Host '  VERIFY : PASS (count + total size match)' -ForegroundColor Green
} else {
    Write-Host ('  VERIFY : MISMATCH - src ' + $srcFiles.Count + '/' + $srcBytes +
                ' vs dst ' + $dstFiles.Count + '/' + $dstBytes) -ForegroundColor Red
}

# manifest
$man = Join-Path (Split-Path $Dest -Parent) 'RECOVERY_MANIFEST.csv'
$dstFiles | Select-Object @{n='file';e={$_.FullName}}, @{n='sizeKB';e={[math]::Round($_.Length/1KB,1)}},
    @{n='modified';e={$_.LastWriteTime.ToString('yyyy-MM-dd HH:mm')}} |
    Export-Csv -NoTypeInformation -Encoding UTF8 $man

Write-Host ('  manifest : ' + $man)
Write-Host ''
Write-Host 'Done. The recovered skill now lives in the filestore (git-safe, non-volatile).' -ForegroundColor Cyan
Write-Host 'Tell Claude when this finishes; it will read the files and load the skill properly.'
Write-Host ''
