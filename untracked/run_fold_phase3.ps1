# ================================
# FOLD PHASE 3 — GRAPH BUILD
# ================================

$root = "D:\maestro-on-mosaic"

$foldInput = Get-Content "$root\FOLD_INPUT.json" -Raw | ConvertFrom-Json
$chains = Get-Content "$root\MUTATION_CHAIN.json" -Raw | ConvertFrom-Json

Write-Host "Building graph..."

# Nodes
$nodes = $foldInput | ForEach-Object {
    [pscustomobject]@{
        id = $_.normalized_path
        type = $_.class
    }
}

# Edges from mutation chain
$edges = @()

foreach ($c in $chains) {
    $edges += [pscustomobject]@{
        source = $c.from
        target = $c.to
        type   = "temporal"
    }
}

# Reference edges (light semantic pass)
foreach ($f in $foldInput) {

    $fullPath = "$root\" + $f.path

    if (Test-Path $fullPath) {

        $content = Get-Content $fullPath -Raw -ErrorAction SilentlyContinue

        foreach ($target in $foldInput.normalized_path) {

            if ($content -like "*$target*") {

                $edges += [pscustomobject]@{
                    source = $f.normalized_path
                    target = $target
                    type   = "reference"
                }
            }
        }
    }
}

$graph = @{
    nodes = $nodes
    edges = $edges
}

$graph | ConvertTo-Json -Depth 6 |
Out-File "$root\SYSTEM_GRAPH.json"

Write-Host "✅ GRAPH COMPLETE"
