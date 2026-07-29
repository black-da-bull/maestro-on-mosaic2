# ================================
# FOLD PHASE 2 — CLEAN EXECUTION
# ================================

$root = "D:\maestro-on-mosaic"
$manifestPath = "$root\FOLD_MANIFEST.json"

if (!(Test-Path $manifestPath)) {
    Write-Host "ERROR: Manifest not found" -ForegroundColor Red
    exit
}

$manifest = Get-Content $manifestPath -Raw | ConvertFrom-Json


function Classify-File($f) {

    if ($f.path -match "\\archive\\|\.zip$|\.tar|\.bundle") { return "archive" }

    elseif ($f.path -match "canon\\|Canonical|knowledgeSpine|root|master\.project") { return "canonical" }

    elseif ($f.path -match "conversation|devsession|\.agi") { return "session_source" }

    elseif ($f.path -match "CHAIN_INDEX|TRACE_MAP|ARTIFACT_MAP|ledger|log|report") { return "trace" }

    elseif ($f.size -gt 100000 -and $f.path -match "\.txt|\.md") { return "session_candidate" }

    elseif ($f.path -match "\.yaml$|\.json$|\.md$") { return "structured_doc" }

    else { return "unknown" }
}

Write-Host "Classifying..."

$classified = $manifest | ForEach-Object {
    $_ | Add-Member -NotePropertyName class -NotePropertyValue (Classify-File $_) -PassThru
}

$classified | ConvertTo-Json -Depth 6 | Out-File "$root\FOLD_MANIFEST_CLASSIFIED.json"



Write-Host "Building FOLD input..."

$foldInput = $classified | Where-Object {
    $_.class -in @("session_source","canonical","trace")
}

$foldInput | ConvertTo-Json -Depth 6 | Out-File "$root\FOLD_INPUT.json"



Write-Host "Extracting mutation chain..."

$sessions = $foldInput | Where-Object { $_.class -eq "session_source" }

$ordered = $sessions | ForEach-Object {
    if ($_.path -match "(\d{4}-\d{2}-\d{2})") {
        [pscustomobject]@{
            path = $_.path
            date = [datetime]$matches[1]
        }
    }
} | Sort-Object date

$chains = @()

for ($i=0; $i -lt $ordered.Count - 1; $i++) {
    $chains += [pscustomobject]@{
        from  = $ordered[$i].path
        to    = $ordered[$i+1].path
        type  = "temporal_mutation"
    }
}

$chains | ConvertTo-Json -Depth 5 | Out-File "$root\MUTATION_CHAIN.json"



Write-Host "Validating trace files..."

$allPaths = $foldInput.normalized_path

$traceFiles = $foldInput | Where-Object { $_.class -eq "trace" }

$validation = foreach ($t in $traceFiles) {

    $fullPath = "$root\" + $t.path

    if (Test-Path $fullPath) {

        $content = Get-Content $fullPath -Raw -ErrorAction SilentlyContinue

        $matches = $allPaths | Where-Object { $content -like "*$_*" }

        [pscustomobject]@{
            path = $t.path
            references_found = $matches.Count
            valid = ($matches.Count -gt 0)
        }
    }
    else {
        [pscustomobject]@{
            path = $t.path
            references_found = 0
            valid = $false
        }
    }
}

$validation | ConvertTo-Json -Depth 5 | Out-File "$root\TRACE_VALIDATION.json"


Write-Host "✅ DONE"
