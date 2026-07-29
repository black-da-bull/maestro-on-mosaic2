<#
    route_untracked.ps1 - drain untracked/ into the filestore structure, then commit.
    ASCII-ONLY by design (PowerShell 5.1 reads .ps1 as ANSI; non-ASCII breaks parsing).

    Basis: DEC-29 (filestore SSOT), M19 (folder-local CLAUDE.md), ARCH-SYNTH-1.
           M18 REPLAY LAW - NOTHING IS EVER DELETED. Moves only. Undo script emitted.
           M16 - sealed archives are not committed sealed; extract + inventory first.

    This pass SKIPS media/binaries per operator instruction:
        art\  tracks\  website\  *.zip  *.docx  *.pdf  *.xlsx

    USAGE
      .\route_untracked.ps1                 # DRY RUN (default), changes nothing
      .\route_untracked.ps1 -Execute        # perform moves + git add + commit
      .\route_untracked.ps1 -Execute -Push  # and push to origin
#>

[CmdletBinding()]
param(
    [switch]$Execute,
    [switch]$Push,
    [string]$Root = 'D:\maestro-on-mosaic'
)

$ErrorActionPreference = 'Stop'
$stamp    = Get-Date -Format 'yyyyMMdd-HHmmss'
$Unt      = Join-Path $Root 'untracked'
$LogPath  = Join-Path $Unt ('_ROUTING_LOG_'  + $stamp + '.csv')
$UndoPath = Join-Path $Unt ('_ROUTING_UNDO_' + $stamp + '.ps1')
if ($Execute) { $mode = 'EXECUTE' } else { $mode = 'DRY RUN' }

Write-Host ''
Write-Host ('=== route_untracked.ps1 - ' + $mode + ' ===') -ForegroundColor Cyan
Write-Host ('Root: ' + $Root)
Write-Host ''

if (-not (Test-Path -LiteralPath $Unt)) { throw ('untracked not found at ' + $Unt) }

# ------------------------------------------------------- PHASE 0: preflight
Write-Host '--- PHASE 0: preflight ---' -ForegroundColor Yellow
Push-Location $Root
try {
    $branch = (git rev-parse --abbrev-ref HEAD 2>$null)
    if (-not $branch) { $branch = '<none>' }
    $remote = (git remote -v 2>$null | Select-Object -First 1)
    if (-not $remote) { $remote = '<NONE CONFIGURED - push will fail>' }
    Write-Host ('  branch : ' + $branch)
    Write-Host ('  remote : ' + $remote)
} catch {
    Write-Host ('  git error: ' + $_) -ForegroundColor Red
}
Pop-Location

$limit = 50MB
$big = Get-ChildItem -LiteralPath $Root -Recurse -File -Force -ErrorAction SilentlyContinue |
       Where-Object { $_.FullName -notmatch '\\\.git\\' -and $_.Length -gt $limit } |
       Sort-Object Length -Descending
if ($big) {
    Write-Host '  files over 50MB (must stay gitignored):' -ForegroundColor Yellow
    foreach ($b in ($big | Select-Object -First 15)) {
        $mb = [math]::Round($b.Length / 1MB, 1)
        Write-Host ('    ' + $mb + ' MB  ' + $b.FullName.Replace($Root, '.'))
    }
    Write-Host ('    total over 50MB: ' + $big.Count)
} else {
    Write-Host '  no files over 50MB outside .git - good.'
}

# ------------------------------------------------------- PHASE 1: skeleton
Write-Host ''
Write-Host '--- PHASE 1: folder skeleton ---' -ForegroundColor Yellow
$folders = @(
    '_PROVENANCE\method\fold',
    'derived\architecture',
    'derived\graph\fold',
    'artifacts\packs',
    'artifacts\transfer',
    'sessions\chatgpt-customgpt',
    '_TRIAGE',
    '_SANDBOX'
)
foreach ($f in $folders) {
    $p = Join-Path $Root $f
    if (Test-Path -LiteralPath $p) {
        Write-Host ('  exists : ' + $f)
    } else {
        Write-Host ('  create : ' + $f) -ForegroundColor Green
        if ($Execute) { New-Item -ItemType Directory -Path $p -Force | Out-Null }
    }
}

# ------------------------------------------------------- PHASE 2: folder contracts (M19)
Write-Host ''
Write-Host '--- PHASE 2: folder-local CLAUDE.md contracts (M19) ---' -ForegroundColor Yellow

$contracts = @{}

$contracts['artifacts'] = @'
# CLAUDE.md - artifacts/
**Axis:** ROLE=artifact x SOURCE-ORIGIN (D-Maestro/, OneDrive-v45/, ...)
**Rung:** INGEST EVIDENCE - immutable.
**Belongs:** material ingested from a named source, preserved as received.
**NEVER:** reorganize, rename, or de-duplicate anything here. Name-collisions across sources are
SIGNAL (DEC-28 thinning evidence), not waste. Differing variants are ALL preserved.
**Who writes:** ingest passes only, with a LEDGER entry.
'@

$contracts['derived'] = @'
# CLAUDE.md - derived/
**Axis:** ROLE=derived output.
**Rung:** PROPOSED until an explicit operator statement promotes it. Never treat as canon.
**Belongs:** AI-produced synthesis, compiled graphs, generated reports.
**NEVER:** cite as authority; never overwrite an evidence file from here.
**Note:** graph/ holds FOIL/FOLD compilation output (Compilation domain).
Variant pairs (SYSTEM_GRAPH vs SYSTEM_GRAPH_IMPROVED) keep BOTH - the delta is the point.
'@

$contracts['sessions'] = @'
# CLAUDE.md - sessions/
**Axis:** ROLE=session transcript x origin surface.
**Rung:** PRIMARY EVIDENCE (DEC-02).
**Belongs:** raw dev-session exports, as exported.
**NEVER:** summarize in place, truncate, or clean up. Replay (M18) reads these verbatim;
compaction destroys the Q-A-F deltas the replay walks.
'@

$contracts['_TRIAGE'] = @'
# CLAUDE.md - _TRIAGE/
**Rung:** UNCLASSIFIED.
**Belongs:** files whose content has not been read yet (e.g. Untitled *.md).
**RULE:** never auto-route, auto-merge, or auto-delete anything here. An explicit
read-then-classify pass moves items out one at a time, with a reason recorded.
'@

$contracts['_SANDBOX'] = @'
# CLAUDE.md - _SANDBOX/
**Rung:** EXPERIMENT. Not evidence, not canon.
**RULE:** this folder may NEVER write outside itself. Source material is only ever copied IN.
Attempts are numbered attempt-NN/ with PLAN.md (incl. falsification criterion) and RESULT.md.
Failed attempts are KEPT - they are evidence of a search (M16). Gitignored.
'@

foreach ($k in $contracts.Keys) {
    $dir = Join-Path $Root $k
    $cm  = Join-Path $dir 'CLAUDE.md'
    if (Test-Path -LiteralPath $cm) {
        Write-Host ('  exists : ' + $k + '\CLAUDE.md')
    } else {
        Write-Host ('  write  : ' + $k + '\CLAUDE.md') -ForegroundColor Green
        if ($Execute) {
            if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
            Set-Content -LiteralPath $cm -Value $contracts[$k] -Encoding UTF8
        }
    }
}

# ------------------------------------------------------- PHASE 3: routing
Write-Host ''
Write-Host '--- PHASE 3: move plan (media/binaries skipped) ---' -ForegroundColor Yellow

$map = @(
    @{ n = 'run_fold_phase2.ps1';                    d = '_PROVENANCE\method\fold' },
    @{ n = 'run_fold_phase3.ps1';                    d = '_PROVENANCE\method\fold' },
    @{ n = 'run_fold_phase3_1.ps1';                  d = '_PROVENANCE\method\fold' },
    @{ n = 'FOLD_INPUT.json';                        d = 'derived\graph\fold' },
    @{ n = 'FOLD_MANIFEST.json';                     d = 'derived\graph\fold' },
    @{ n = 'FOLD_MANIFEST_CLASSIFIED.json';          d = 'derived\graph\fold' },
    @{ n = 'MUTATION_CHAIN.json';                    d = 'derived\graph\fold' },
    @{ n = 'TRACE_VALIDATION.json';                  d = 'derived\graph\fold' },
    @{ n = 'SYSTEM_GRAPH.json';                      d = 'derived\graph' },
    @{ n = 'SYSTEM_GRAPH_IMPROVED.json';             d = 'derived\graph' },
    @{ n = 'maestro architecture session.md';        d = 'sessions\chatgpt-customgpt' },
    @{ n = 'EXECUTIVE ARCHITECTURAL SYNTHESIS.md';   d = 'derived\architecture' },
    @{ n = '_ROUTING_AND_TAXONOMY_PROPOSAL_v0.1.md'; d = 'derived\architecture' },
    @{ n = 'Maestro_Session_Transfer_Packet.md';     d = 'artifacts\transfer' },
    @{ n = 'Maestro_Session_Transfer_Packet.yaml';   d = 'artifacts\transfer' },
    @{ n = 'Maestro_Session_Transfer_Packet.json';   d = 'artifacts\transfer' },
    @{ n = 'Untitled 1.md';                          d = '_TRIAGE' },
    @{ n = 'Untitled 2.md';                          d = '_TRIAGE' },
    @{ n = 'Untitled 3.md';                          d = '_TRIAGE' },
    @{ n = 'Untitled 4.md';                          d = '_TRIAGE' },
    @{ n = 'Untitled 5.md';                          d = '_TRIAGE' },
    @{ n = 'Untitled 6.md';                          d = '_TRIAGE' },
    @{ n = 'AI Music.md';                            d = '_TRIAGE' },
    @{ n = 'AI Music - lyrics.md';                   d = '_TRIAGE' },
    @{ n = 'Maestro - Fabric - Rebirth.md';          d = '_TRIAGE' }
)

$rows = @()
$undo = @()
$undo += ('# Undo routing pass ' + $stamp)
$undo += '$ErrorActionPreference = "Stop"'

foreach ($m in $map) {
    $src    = Join-Path $Unt  $m.n
    $dstDir = Join-Path $Root $m.d
    $dst    = Join-Path $dstDir $m.n

    if (-not (Test-Path -LiteralPath $src)) {
        Write-Host ('  MISSING  ' + $m.n) -ForegroundColor DarkGray
        $rows += New-Object psobject -Property @{ file = $m.n; dest = $m.d; result = 'MISSING' }
        continue
    }
    if (Test-Path -LiteralPath $dst) {
        Write-Host ('  CONFLICT ' + $m.n + '  (destination exists, SKIPPED, nothing overwritten)') -ForegroundColor Red
        $rows += New-Object psobject -Property @{ file = $m.n; dest = $m.d; result = 'CONFLICT-SKIPPED' }
        continue
    }

    Write-Host ('  MOVE     ' + $m.n + '  ->  ' + $m.d) -ForegroundColor Green
    $rows += New-Object psobject -Property @{ file = $m.n; dest = $m.d; result = 'MOVED' }
    $undo += ('Move-Item -LiteralPath "' + $dst + '" -Destination "' + $src + '"')

    if ($Execute) {
        if (-not (Test-Path -LiteralPath $dstDir)) { New-Item -ItemType Directory -Path $dstDir -Force | Out-Null }
        Move-Item -LiteralPath $src -Destination $dst
    }
}

Write-Host ''
Write-Host '  LEFT IN PLACE (later passes): art\  tracks\  website\  *.zip  *.docx  *.pdf  *.xlsx' -ForegroundColor DarkCyan

if ($Execute) {
    $rows | Select-Object file, dest, result | Export-Csv -NoTypeInformation -Encoding UTF8 $LogPath
    Set-Content -LiteralPath $UndoPath -Value $undo -Encoding UTF8
    Write-Host ''
    Write-Host ('  log  : ' + $LogPath)
    Write-Host ('  undo : ' + $UndoPath)
}

# ------------------------------------------------------- PHASE 4: git
Write-Host ''
Write-Host '--- PHASE 4: git ---' -ForegroundColor Yellow
if (-not $Execute) {
    Write-Host '  (dry run - no git actions). Re-run with -Execute to apply.'
    Write-Host ''
    Write-Host 'Done. Nothing was changed.' -ForegroundColor Cyan
    Write-Host ''
    return
}

Push-Location $Root
try {
    git add -A

    $staged = git diff --cached --name-only
    $oversize = @()
    foreach ($s in $staged) {
        $fp = Join-Path $Root $s
        if (Test-Path -LiteralPath $fp) {
            $len = (Get-Item -LiteralPath $fp).Length
            if ($len -gt 100MB) {
                $oversize += ($s + '  (' + [math]::Round($len / 1MB, 1) + ' MB)')
            }
        }
    }
    if ($oversize.Count -gt 0) {
        Write-Host '  ABORT - staged files exceed the GitHub 100MB limit:' -ForegroundColor Red
        foreach ($o in $oversize) { Write-Host ('    ' + $o) -ForegroundColor Red }
        Write-Host '  Fix .gitignore, then run: git reset' -ForegroundColor Red
        Pop-Location
        return
    }

    Write-Host ('  staging ' + $staged.Count + ' path(s)')

    $msg = "Route untracked into filestore structure; add repo hygiene`n`n" +
           "- DEC-29: D:\maestro-on-mosaic confirmed filestore SSOT; Rebirth = executable runner`n" +
           "- M19: folder-local CLAUDE.md contracts (auto-load on demand)`n" +
           "- ARCH-SYNTH-1: EXECUTIVE ARCHITECTURAL SYNTHESIS registered (M1 exposure closed)`n" +
           "- .gitignore added: media/archives/executables excluded (text-only repo)`n" +
           "- Media pass deferred: art, tracks, website, zip/docx/pdf/xlsx left in untracked`n" +
           "- No deletions (M18). Undo script emitted alongside routing log."

    git commit -m $msg
    Write-Host '  committed.' -ForegroundColor Green

    if ($Push) {
        Write-Host '  pushing...'
        git push
        Write-Host '  pushed.' -ForegroundColor Green
    } else {
        Write-Host '  (not pushed - re-run with -Push, or run: git push)' -ForegroundColor DarkCyan
    }
} finally {
    Pop-Location
}

Write-Host ''
Write-Host 'Done.' -ForegroundColor Cyan
Write-Host ''
