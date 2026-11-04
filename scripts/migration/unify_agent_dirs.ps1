# Unification Script: Merge .agent, .agents, and agents into single .agents/
$Root = "f:\VIETLOTT-SMS"
$agentsDir = Join-Path $Root "agents"
$dotAgentsDir = Join-Path $Root ".agents"

Write-Host "=== Hop nhat hoan toan vao thu muc duy nhat .agents/ ===" -ForegroundColor Cyan

# 1. Di chuyen personas va definitions tu agents/ vao .agents/ neu agents/ con ton tai
if (Test-Path $agentsDir) {
    $srcDef = Join-Path $agentsDir "definitions"
    $targetDef = Join-Path $dotAgentsDir "definitions"
    if (Test-Path $srcDef) {
        if (-not (Test-Path $targetDef)) {
            Move-Item -Path $srcDef -Destination $targetDef -Force
            Write-Host "  Da chuyen definitions vao .agents/definitions" -ForegroundColor Green
        }
    }

    $srcPer = Join-Path $agentsDir "personas"
    $targetPer = Join-Path $dotAgentsDir "personas"
    if (Test-Path $srcPer) {
        if (-not (Test-Path $targetPer)) {
            Move-Item -Path $srcPer -Destination $targetPer -Force
            Write-Host "  Da chuyen personas vao .agents/personas" -ForegroundColor Green
        }
    }

    Remove-Item -Path $agentsDir -Recurse -Force
    Write-Host "  Da xoa thu muc trung lap agents/ tai root" -ForegroundColor Green
}

# 2. Dam bao .agents/skills co du 26 junctions
$ideSkills = Join-Path $dotAgentsDir "skills"
if (-not (Test-Path $ideSkills)) {
    New-Item -ItemType Directory -Path $ideSkills -Force | Out-Null
}

$skillDomains = @('pm', 'po', 'ba', 'da', 'dev', 'qa', 'shared')
foreach ($domain in $skillDomains) {
    $domainPath = Join-Path $Root "skills\$domain"
    if (Test-Path $domainPath) {
        Get-ChildItem -Directory $domainPath | ForEach-Object {
            $skillName = $_.Name
            $srcSkillPath = $_.FullName
            $targetSkillLink = Join-Path $ideSkills $skillName
            if (-not (Test-Path $targetSkillLink)) {
                cmd /c mklink /J "$targetSkillLink" "$srcSkillPath"
                Write-Host "  Linked skill: $skillName" -ForegroundColor Green
            }
        }
    }
}

# 3. Dam bao .agents/rules junction tro toi rules/
$ideRules = Join-Path $dotAgentsDir "rules"
$srcRules = Join-Path $Root "rules"
if (-not (Test-Path $ideRules)) {
    cmd /c mklink /J "$ideRules" "$srcRules"
    Write-Host "  Linked rules into .agents/rules" -ForegroundColor Green
}

# 4. Dam bao .agents/hooks.json
$srcHooks = Join-Path $Root "hooks\hooks.json"
$targetHooks = Join-Path $dotAgentsDir "hooks.json"
if (Test-Path $srcHooks) {
    Copy-Item $srcHooks $targetHooks -Force
    Write-Host "  Copied hooks.json to .agents/hooks.json" -ForegroundColor Green
}

Write-Host "=== Hoan tat: Chi con duy nhat 1 thu muc .agents/ tai root ===" -ForegroundColor Green
