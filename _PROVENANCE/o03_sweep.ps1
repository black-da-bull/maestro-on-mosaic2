<#
    o03_sweep.ps1 - discharge the O-03 / DEC-03 skill-files search burden.
    ASCII-ONLY (PowerShell 5.1 reads .ps1 as ANSI).

    READ-ONLY. This script never creates, moves, renames, or deletes anything.
    It only searches and writes two report files into _PROVENANCE\.

    Covers the checklist locations that can be swept mechanically:
      - every fixed drive (system/noise paths excluded)
      - every user profile: Downloads, Documents, Desktop, .claude\skills, AppData\...\Claude
      - Recycle Bin
      - renamed-file detection via content terms
    NOT covered (manual, see report): OneDrive WEB per account incl. web recycle bin,
    browser download history 2026-05-20 -> 2026-06-18, USB/external drives not mounted now.

    USAGE
      powershell -ExecutionPolicy Bypass -File .\o03_sweep.ps1
#>

[CmdletBinding()]
param(
    [string]$OutDir = 'D:\maestro-on-mosaic\_PROVENANCE'
)

$ErrorActionPreference = 'SilentlyContinue'
$stamp   = Get-Date -Format 'yyyyMMdd-HHmmss'
$csvPath = Join-Path $OutDir ('O03_SWEEP_' + $stamp + '.csv')
$mdPath  = Join-Path $OutDir ('O03_SWEEP_' + $stamp + '.md')

Write-Host ''
Write-Host '=== O-03 skill-files sweep (READ-ONLY) ===' -ForegroundColor Cyan
Write-Host ''

# ---------------- targets ----------------
$names = @(
    '00_OPERATOR_ABOUT_ME.md',
    'OPERATOR_CONTEXT.md',
    '01_METHODOLOGY.md',
    '02_FAILURE_MODES.md',
    '03_WHY_AI_DEFAULTS_HERE.md',
    '04_KERNEL.md',
    '05_WORKFLOW.md'
)
# loose name patterns (renames, numbering drift, folders)
$namePatterns = @(
    'OPERATOR_ABOUT', 'OPERATOR_CONTEXT', 'METHODOLOGY', 'FAILURE_MODE',
    'WHY_AI_DEFAULTS', 'KERNEL', 'WORKFLOW'
)
$pyPatterns  = @('parse_*.py', 'phantom*.py', 'fold_*.py')
$zipPatterns = @('*skill*.zip', '*forensic*.zip', '*transcript*.zip')
$folderNames = @('patterns', 'examples')

# content terms (renamed-file detection)
$terms = 'INV-17|INV-18|phantom commitment|FM-16|FM-18|skeleton file|Fabric pattern|not-novel|narrative-as-method|Tandy'
$contentExt = @('.md', '.txt', '.json', '.py', '.yaml', '.yml')

# ---------------- roots ----------------
$excl = '\\(Windows|Program Files|Program Files \(x86\)|WindowsApps|ProgramData\\Package Cache|node_modules|\$WinREAgent|OneDriveTemp)\\'

$roots = @()
foreach ($d in (Get-PSDrive -PSProvider FileSystem)) {
    if ($d.Free -ne $null -or (Test-Path -LiteralPath $d.Root)) { $roots += $d.Root }
}
$roots = $roots | Sort-Object -Unique
Write-Host ('Drives to sweep: ' + ($roots -join ' '))
Write-Host ''

$hits = @()

function Add-Hit($cat, $target, $item) {
    $script:hits += New-Object psobject -Property @{
        category = $cat
        target   = $target
        path     = $item.FullName
        sizeKB   = [math]::Round($item.Length / 1KB, 1)
        modified = $item.LastWriteTime.ToString('yyyy-MM-dd HH:mm')
    }
}

# ---------------- PASS 1: filename sweep ----------------
Write-Host '--- PASS 1: filenames ---' -ForegroundColor Yellow
foreach ($r in $roots) {
    Write-Host ('  scanning ' + $r + ' ...')
    $all = Get-ChildItem -LiteralPath $r -Recurse -Force -ErrorAction SilentlyContinue |
           Where-Object { $_.FullName -notmatch $excl }

    foreach ($f in $all) {
        if ($f.PSIsContainer) {
            if ($folderNames -contains $f.Name.ToLower()) {
                $script:hits += New-Object psobject -Property @{
                    category='folder'; target=$f.Name; path=$f.FullName; sizeKB=''
                    modified=$f.LastWriteTime.ToString('yyyy-MM-dd HH:mm')
                }
            }
            continue
        }
        # exact
        if ($names -contains $f.Name) { Add-Hit 'exact-name' $f.Name $f; continue }
        # loose
        $matched = $false
        foreach ($p in $namePatterns) {
            if ($f.Name -match $p) { Add-Hit 'loose-name' $p $f; $matched = $true; break }
        }
        if ($matched) { continue }
        # python
        foreach ($p in $pyPatterns) {
            if ($f.Name -like $p) { Add-Hit 'python' $p $f; $matched = $true; break }
        }
        if ($matched) { continue }
        # zips
        foreach ($p in $zipPatterns) {
            if ($f.Name -like $p) { Add-Hit 'zip' $p $f; break }
        }
    }
}
Write-Host ('  filename hits: ' + $hits.Count)

# ---------------- PASS 2: content sweep ----------------
Write-Host ''
Write-Host '--- PASS 2: content terms (renamed files) ---' -ForegroundColor Yellow
$contentRoots = @()
foreach ($u in (Get-ChildItem 'C:\Users' -Directory -ErrorAction SilentlyContinue)) {
    foreach ($sub in @('Downloads','Documents','Desktop','.claude','AppData\Roaming\Claude','OneDrive')) {
        $p = Join-Path $u.FullName $sub
        if (Test-Path -LiteralPath $p) { $contentRoots += $p }
    }
}
foreach ($r in $roots) { if ($r -notlike 'C:*') { $contentRoots += $r } }
$contentRoots = $contentRoots | Sort-Object -Unique

$cHits = 0
foreach ($cr in $contentRoots) {
    Write-Host ('  grepping ' + $cr + ' ...')
    $cands = Get-ChildItem -LiteralPath $cr -Recurse -File -Force -ErrorAction SilentlyContinue |
             Where-Object { $contentExt -contains $_.Extension.ToLower() -and
                            $_.Length -lt 5MB -and
                            $_.FullName -notmatch $excl }
    foreach ($c in $cands) {
        $m = Select-String -LiteralPath $c.FullName -Pattern $terms -List -ErrorAction SilentlyContinue
        if ($m) {
            $script:hits += New-Object psobject -Property @{
                category='content-term'; target=$m.Matches[0].Value; path=$c.FullName
                sizeKB=[math]::Round($c.Length/1KB,1)
                modified=$c.LastWriteTime.ToString('yyyy-MM-dd HH:mm')
            }
            $cHits++
        }
    }
}
Write-Host ('  content hits: ' + $cHits)

# ---------------- report ----------------
$hits | Select-Object category, target, path, sizeKB, modified |
    Sort-Object category, target, path |
    Export-Csv -NoTypeInformation -Encoding UTF8 $csvPath

$lines = @()
$lines += '# O-03 SWEEP RESULT - ' + $stamp
$lines += ''
$lines += 'READ-ONLY sweep. Nothing was modified.'
$lines += ''
$lines += '## Per-component verdict (mechanical locations only)'
$lines += ''
$lines += '| Component | Verdict | Evidence |'
$lines += '|---|---|---|'
foreach ($n in $names) {
    $found = $hits | Where-Object { $_.category -eq 'exact-name' -and $_.target -eq $n }
    if ($found) {
        $first = ($found | Select-Object -First 1)
        $lines += ('| ' + $n + ' | FOUND | ' + $first.path + ' (' + $first.modified + ') |')
    } else {
        $lines += ('| ' + $n + ' | NOT FOUND | - |')
    }
}
$lines += ''
$lines += '## Counts by category'
foreach ($g in ($hits | Group-Object category | Sort-Object Name)) {
    $lines += ('- ' + $g.Name + ': ' + $g.Count)
}
$lines += ''
$lines += '## STILL MANUAL (not dischargeable by script)'
$lines += '- OneDrive WEB per account (school / work / home), INCLUDING the web recycle bin'
$lines += '- Browser download history 2026-05-20 -> 2026-06-18 (filenames persist after file moves)'
$lines += '- USB / external drives not mounted at sweep time'
$lines += ''
$lines += 'Per the checklist closing rule: do NOT reclassify O-03 to "never externalized -'
$lines += 'reconstruction target" until the three manual items above are also swept.'
$lines += ''
$lines += ('Full hit list: ' + $csvPath)

Set-Content -LiteralPath $mdPath -Value $lines -Encoding UTF8

Write-Host ''
Write-Host ('Report : ' + $mdPath) -ForegroundColor Green
Write-Host ('Hits   : ' + $csvPath) -ForegroundColor Green
Write-Host ''
Write-Host 'Done. Nothing was modified.' -ForegroundColor Cyan
Write-Host ''
