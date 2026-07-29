# ================================
# FOLD PHASE 3.1 — IMPROVED GRAPH
# ================================

$root = "D:\maestro-on-mosaic"

Write-Host "Loading inputs..."

$foldInput = Get-Content "$root\FOLD_INPUT.json" -Raw | ConvertFrom-Json
$chains = Get-Content "$root\MUTATION_CHAIN.json" -Raw | ConvertFrom-Json


Write-Host "Building nodes..."

$nodes = $foldInput | ForEach-Object {
    [pscustomobject]@{
        id = $_.normalized_path
        type = $_.class
    }
}


Write-Host "Building edges..."

$edges = @()

# --- Temporal edges ---
foreach ($c in $chains) {
    $edges += [pscustomobject]@{
        source = $c.from
        target = $c.to
        type   = "temporal"
        weight = 1
    }
}


# --- Improved reference detection ---
Write-Host "Detecting references..."

foreach ($f in $foldInput) {

    $fullPath = "$root\" + $f.path

    if (!(Test-Path $fullPath)) { continue }

    $content = Get-Content $fullPath -Raw -ErrorAction SilentlyContinue

    if (-not $content) { continue }

    # normalize
    $contentClean = ($content -replace '\\','/').ToLower()

    foreach ($target in $foldInput) {

        $targetPath = $target.normalized_path.ToLower()
        $fileName = [System.IO.Path]::GetFileName($targetPath).ToLower()

        $matchScore = 0

        # filename match (strong)
        if ($contentClean -like "*$fileName*") {
            $matchScore += 2
        }

        # partial path match (medium)
        if ($contentClean -like "*$targetPath*") {
            $matchScore += 3
        }

        # keyword match (weak semantic)
        $keywords = @("maestro","foil","chimera","ust","matrix")

        foreach ($k in $keywords) {
            if ($contentClean -like "*$k*") {
                $matchScore += 1
            }
        }

        if ($matchScore -gt 0) {

            $edges += [pscustomobject]@{
                source = $f.normalized_path
                target = $target.normalized_path
                type   = "reference"
                weight = $matchScore
            }
        }
    }
}


Write-Host "Assembling graph..."

$graph = @{
    nodes = $nodes
    edges = $edges
}


$graph | ConvertTo-Json -Depth 6 |
Out-File "$root\SYSTEM_GRAPH_IMPROVED.json"


Write-Host "✅ GRAPH IMPROVED COMPLETE"
