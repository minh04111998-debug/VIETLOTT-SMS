# Migration & Organization Script for Multi-Agent Engineering Architecture
$Root = "f:\VIETLOTT-SMS"

Write-Host "=== Bắt đầu di chuyển và tổ chức lại dự án Vietlott SMS ===" -ForegroundColor Cyan

# 1. AGENTS / PERSONAS
Write-Host "1. Tổ chức agents/personas..."
$roleMap = @{
    "pm" = ".agent\roles\pm.md"
    "po" = ".agent\roles\po.md"
    "ba" = ".agent\roles\ba.md"
    "da" = ".agent\roles\da.md"
    "dev" = ".agent\roles\dev.md"
    "qa" = ".agent\roles\qa.md"
}

foreach ($r in $roleMap.Keys) {
    $src = Join-Path $Root $roleMap[$r]
    $dest = Join-Path $Root "agents\personas\$r\persona.md"
    if (Test-Path $src) {
        Copy-Item -Path $src -Destination $dest -Force
        Write-Host "  [OK] agents/personas/$r/persona.md" -ForegroundColor Green
    }
}

# Designer persona
if (Test-Path "$Root\.agent\roles\designer.md") {
    $destDesignerDir = Join-Path $Root "agents\personas\designer"
    if (-not (Test-Path $destDesignerDir)) { New-Item -ItemType Directory -Path $destDesignerDir -Force | Out-Null }
    Copy-Item -Path "$Root\.agent\roles\designer.md" -Destination "$destDesignerDir\persona.md" -Force
}

# 2. AGENTS / DEFINITIONS
Write-Host "2. Tổ chức agents/definitions..."
if (Test-Path "$Root\.agent\_router\role-detector.md") {
    Copy-Item -Path "$Root\.agent\_router\role-detector.md" -Destination "$Root\agents\definitions\role-detector.md" -Force
}
if (Test-Path "$Root\.agent\harness\guardrails\boundaries.md") {
    Copy-Item -Path "$Root\.agent\harness\guardrails\boundaries.md" -Destination "$Root\agents\definitions\role-permission-matrix.md" -Force
}

# 3. SKILLS ORGANIZATION
Write-Host "3. Tổ chức skills theo domain..."
$skillCategorization = @{
    "pm" = @("pm", "pm-ceremony", "pm-readiness")
    "po" = @("po", "po-delivery", "po-discovery", "po-metrics")
    "ba" = @("ba", "ba-analysis", "ba-change", "ba-diagrams", "ba-requirements")
    "da" = @("da", "da-reporting", "da-visualization")
    "dev" = @("dev", "dev-refactor", "dev-review")
    "qa" = @("qa", "qa-automation", "qa-bug-management", "qa-test-plan")
    "shared" = @("markitdown", "designer", "designer-review", "designer-system")
}

foreach ($domain in $skillCategorization.Keys) {
    $skillsInDomain = $skillCategorization[$domain]
    foreach ($sk in $skillsInDomain) {
        $srcSkill = Join-Path $Root ".agent\skills\$sk"
        $destSkill = Join-Path $Root "skills\$domain\$sk"
        if (Test-Path $srcSkill) {
            Copy-Item -Path $srcSkill -Destination $destSkill -Recurse -Force
            Write-Host "  [OK] skills/$domain/$sk" -ForegroundColor Green
        }
    }
}

# 4. WORKFLOWS ORGANIZATION (Value Streams)
Write-Host "4. Tổ chức workflows theo Value Stream..."
$wfMap = @{
    "product-discovery" = @(
        ".agent\workflows\po\product-discovery.md",
        ".agent\workflows\po\product-strategy.md",
        ".agent\workflows\po\user-journey-mapping.md",
        ".agent\workflows\po\product-health-check.md",
        ".agent\workflows\po\stakeholder-alignment.md",
        ".agent\workflows\po\create-prd.md",
        ".agent\workflows\po\po-workflow.md",
        ".agent\workflows\designer\ux-audit.md"
    )
    "requirement" = @(
        ".agent\workflows\ba\scope-definition.md",
        ".agent\workflows\ba\elicitation-plan.md",
        ".agent\workflows\ba\create-brd.md",
        ".agent\workflows\ba\create-srs.md",
        ".agent\workflows\ba\requirements-review.md",
        ".agent\workflows\ba\change-request.md",
        ".agent\workflows\ba\impact-analysis.md",
        ".agent\workflows\ba\solution-evaluation.md",
        ".agent\workflows\ba\create-jira-task.md",
        ".agent\workflows\ba\ba-workflow.md",
        ".agent\harness\loop\ba-po-loop.md"
    )
    "feature-development" = @(
        ".agent\workflows\dev\dev-workflow.md",
        ".agent\workflows\dev\code-review.md",
        ".agent\workflows\dev\refactoring-plan.md",
        ".agent\workflows\designer\create-ui-design.md",
        ".agent\workflows\designer\import-design-system.md",
        ".agent\workflows\designer\design-review.md",
        ".agent\workflows\designer\designer-workflow.md",
        ".agent\workflows\po\backlog-refinement.md",
        ".agent\workflows\pm\sprint-ceremony.md"
    )
    "bug-fix" = @(
        ".agent\workflows\qa\bug-triage.md",
        ".agent\workflows\qa\create-test-plan.md",
        ".agent\workflows\qa\regression-plan.md",
        ".agent\workflows\qa\playwright-test.md",
        ".agent\workflows\qa\qa-workflow.md"
    )
    "data-analysis" = @(
        ".agent\workflows\da\da-workflow.md"
    )
    "release" = @(
        ".agent\workflows\pm\production-readiness.md",
        ".agent\workflows\pm\project-closing.md",
        ".agent\workflows\pm\project-kickoff.md",
        ".agent\workflows\pm\status-report.md",
        ".agent\workflows\pm\pm-workflow.md",
        ".agent\workflows\po\release-planning.md"
    )
}

foreach ($stream in $wfMap.Keys) {
    $files = $wfMap[$stream]
    foreach ($f in $files) {
        $srcWf = Join-Path $Root $f
        if (Test-Path $srcWf) {
            $destWf = Join-Path $Root "workflows\$stream\$(Split-Path $f -Leaf)"
            Copy-Item -Path $srcWf -Destination $destWf -Force
            Write-Host "  [OK] workflows/$stream/$(Split-Path $f -Leaf)" -ForegroundColor Green
        }
    }
}

# 5. RULES ORGANIZATION
Write-Host "5. Tổ chức rules theo Domain..."
# Global rules
if (Test-Path "$Root\.agent\harness\guardrails\banned-words.md") {
    Copy-Item "$Root\.agent\harness\guardrails\banned-words.md" "$Root\rules\global\banned-words.md" -Force
}
if (Test-Path "$Root\.agent\harness\guardrails\boundaries.md") {
    Copy-Item "$Root\.agent\harness\guardrails\boundaries.md" "$Root\rules\global\boundaries.md" -Force
}
if (Test-Path "$Root\.agent\_shared\context-budget.md") {
    Copy-Item "$Root\.agent\_shared\context-budget.md" "$Root\rules\global\context-budget.md" -Force
}
if (Test-Path "$Root\.agent\_shared\conventions.md") {
    Copy-Item "$Root\.agent\_shared\conventions.md" "$Root\rules\global\conventions.md" -Force
}

# Product rules
if (Test-Path "$Root\.agent\rules\po-rules.md") {
    Copy-Item "$Root\.agent\rules\po-rules.md" "$Root\rules\product\po-rules.md" -Force
}

# Business rules
if (Test-Path "$Root\.agent\harness\context\business-rules.md") {
    Copy-Item "$Root\.agent\harness\context\business-rules.md" "$Root\rules\business\vietlott-business-rules.md" -Force
}

# Technical rules
if (Test-Path "$Root\.agent\rules\dev-rules.md") {
    Copy-Item "$Root\.agent\rules\dev-rules.md" "$Root\rules\technical\dev-rules.md" -Force
}
if (Test-Path "$Root\.agent\rules\designer-rules.md") {
    Copy-Item "$Root\.agent\rules\designer-rules.md" "$Root\rules\technical\designer-rules.md" -Force
}

# Quality rules
if (Test-Path "$Root\.agent\rules\qa-rules.md") {
    Copy-Item "$Root\.agent\rules\qa-rules.md" "$Root\rules\quality\qa-rules.md" -Force
}
if (Test-Path "$Root\.agent\rules\ba-rules.md") {
    Copy-Item "$Root\.agent\rules\ba-rules.md" "$Root\rules\quality\ba-rules.md" -Force
}
if (Test-Path "$Root\.agent\rules\pm-rules.md") {
    Copy-Item "$Root\.agent\rules\pm-rules.md" "$Root\rules\quality\pm-rules.md" -Force
}
if (Test-Path "$Root\.agent\rules\da-rules.md") {
    Copy-Item "$Root\.agent\rules\da-rules.md" "$Root\rules\quality\da-rules.md" -Force
}

# Security rules
if (Test-Path "$Root\.agent\_shared\security-checklist.md") {
    Copy-Item "$Root\.agent\_shared\security-checklist.md" "$Root\rules\security\security-checklist.md" -Force
}

# 6. KNOWLEDGE
Write-Host "6. Tổ chức knowledge..."
if (Test-Path "$Root\.agent\harness\context\glossary.md") {
    Copy-Item "$Root\.agent\harness\context\glossary.md" "$Root\knowledge\glossary\glossary.md" -Force
}
if (Test-Path "$Root\.agent\harness\context\source-registry.md") {
    Copy-Item "$Root\.agent\harness\context\source-registry.md" "$Root\knowledge\standards\source-registry.md" -Force
}
if (Test-Path "$Root\.agent\harness\context\business-rules.md") {
    Copy-Item "$Root\.agent\harness\context\business-rules.md" "$Root\knowledge\business-rules\business-rules.md" -Force
}
if (Test-Path "$Root\04_Document\project-context.md") {
    Copy-Item "$Root\04_Document\project-context.md" "$Root\knowledge\product\project-context.md" -Force
}
if (Test-Path "$Root\04_Document\fintech-knowledge-base.md") {
    Copy-Item "$Root\04_Document\fintech-knowledge-base.md" "$Root\knowledge\product\fintech-knowledge-base.md" -Force
}

# 7. VALIDATORS & TOOLS & SCRIPTS
Write-Host "7. Tổ chức validators, tools, scripts..."
$scriptFiles = @(
    "ambiguity_scanner.py",
    "traceability_checker.py",
    "doc_structure_validator.py",
    "gate_runner.py"
)
foreach ($sf in $scriptFiles) {
    if (Test-Path "$Root\.agent\scripts\$sf") {
        Copy-Item "$Root\.agent\scripts\$sf" "$Root\validators\$sf" -Force
        Copy-Item "$Root\.agent\scripts\$sf" "$Root\scripts\$sf" -Force
    }
}

if (Test-Path "$Root\.agent\scripts\export_docx.ps1") {
    Copy-Item "$Root\.agent\scripts\export_docx.ps1" "$Root\scripts\export_docx.ps1" -Force
}
if (Test-Path "$Root\.agent\scripts\read_excel.ps1") {
    Copy-Item "$Root\.agent\scripts\read_excel.ps1" "$Root\scripts\read_excel.ps1" -Force
}
if (Test-Path "$Root\.agent\scripts\jira") {
    Copy-Item "$Root\.agent\scripts\jira" "$Root\tools\jira" -Recurse -Force
}
if (Test-Path "$Root\.agent\scripts\telegram") {
    Copy-Item "$Root\.agent\scripts\telegram" "$Root\tools\telegram" -Recurse -Force
}
if (Test-Path "$Root\.agent\integrations\Confluence") {
    Copy-Item "$Root\.agent\integrations\Confluence" "$Root\tools\confluence" -Recurse -Force
}
if (Test-Path "$Root\.agent\_shared\tool-registry.md") {
    Copy-Item "$Root\.agent\_shared\tool-registry.md" "$Root\tools\tool-registry.md" -Force
}

# 8. EVALUATIONS & VERIFICATIONS
Write-Host "8. Tổ chức evaluations..."
if (Test-Path "$Root\.agent\harness\verification\quality-gate-runner.md") {
    Copy-Item "$Root\.agent\harness\verification\quality-gate-runner.md" "$Root\evaluations\workflows\quality-gate-runner.md" -Force
}
if (Test-Path "$Root\.agent\harness\verification\cross-review-protocol.md") {
    Copy-Item "$Root\.agent\harness\verification\cross-review-protocol.md" "$Root\evaluations\agents\cross-review-protocol.md" -Force
}
if (Test-Path "$Root\.agent\harness\verification\second-agent-critic.md") {
    Copy-Item "$Root\.agent\harness\verification\second-agent-critic.md" "$Root\evaluations\agents\second-agent-critic.md" -Force
}
if (Test-Path "$Root\.agent\harness\verification\smoke-test-scenarios.md") {
    Copy-Item "$Root\.agent\harness\verification\smoke-test-scenarios.md" "$Root\evaluations\regression\smoke-test-scenarios.md" -Force
}
if (Test-Path "$Root\.agent\harness\feedback\feedback-protocol.md") {
    Copy-Item "$Root\.agent\harness\feedback\feedback-protocol.md" "$Root\evaluations\workflows\feedback-protocol.md" -Force
}
# Output checklists
$checklists = Get-ChildItem -Path "$Root\.agent\harness\verification" -Filter "*-checklist.md"
foreach ($chk in $checklists) {
    Copy-Item $chk.FullName "$Root\evaluations\skills\$($chk.Name)" -Force
}

# 9. TEMPLATES & REFERENCES
Write-Host "9. Tổ chức templates & references..."
if (Test-Path "$Root\.agent\_shared\frameworks.md") {
    Copy-Item "$Root\.agent\_shared\frameworks.md" "$Root\references\frameworks.md" -Force
}
if (Test-Path "$Root\08_Template") {
    Get-ChildItem -Path "$Root\08_Template" | ForEach-Object {
        Copy-Item $_.FullName "$Root\templates\$($_.Name)" -Force
    }
}

# 10. OBSERVABILITY & MEMORY
Write-Host "10. Tổ chức observability & memory..."
if (Test-Path "$Root\.agent\harness\observation\observation-protocol.md") {
    Copy-Item "$Root\.agent\harness\observation\observation-protocol.md" "$Root\observability\observation-protocol.md" -Force
}
if (Test-Path "$Root\04_Document\agent-trace-log.md") {
    Copy-Item "$Root\04_Document\agent-trace-log.md" "$Root\memory\agent-trace-log.md" -Force
}

# 11. ARTIFACTS MIGRATION
Write-Host "11. Tổ chức artifacts..."
# Decisions
if (Test-Path "$Root\02_Design\adr") {
    Copy-Item "$Root\02_Design\adr\*" "$Root\artifacts\decisions" -Recurse -Force
}
# Technical
if (Test-Path "$Root\02_Design\ui-spec-vietlott-sms.md") {
    Copy-Item "$Root\02_Design\ui-spec-vietlott-sms.md" "$Root\artifacts\technical\ui-spec-vietlott-sms.md" -Force
}
if (Test-Path "$Root\04_Document\vietlott_sms_app_connection_guide.md") {
    Copy-Item "$Root\04_Document\vietlott_sms_app_connection_guide.md" "$Root\artifacts\technical\vietlott_sms_app_connection_guide.md" -Force
}
if (Test-Path "$Root\04_Document\vietlott_api_traffic.json") {
    Copy-Item "$Root\04_Document\vietlott_api_traffic.json" "$Root\artifacts\technical\vietlott_api_traffic.json" -Force
}

# Product
if (Test-Path "$Root\00_Draft\po-product-improvement-plan.md") {
    Copy-Item "$Root\00_Draft\po-product-improvement-plan.md" "$Root\artifacts\product\po-product-improvement-plan.md" -Force
}
if (Test-Path "$Root\00_Draft\bao-cao-san-pham-vietlott.md") {
    Copy-Item "$Root\00_Draft\bao-cao-san-pham-vietlott.md" "$Root\artifacts\product\bao-cao-san-pham-vietlott.md" -Force
}

# Requirements
if (Test-Path "$Root\00_Draft\srs-campaign-tang-ve-bank.md") {
    Copy-Item "$Root\00_Draft\srs-campaign-tang-ve-bank.md" "$Root\artifacts\requirements\srs-campaign-tang-ve-bank.md" -Force
}
if (Test-Path "$Root\00_Draft\ba-requirements-analysis.md") {
    Copy-Item "$Root\00_Draft\ba-requirements-analysis.md" "$Root\artifacts\requirements\ba-requirements-analysis.md" -Force
}
if (Test-Path "$Root\04_Document\SRS_He_Sinh_Thai_Thanh_Toan_Fintech_v1.0.md") {
    Copy-Item "$Root\04_Document\SRS_He_Sinh_Thai_Thanh_Toan_Fintech_v1.0.md" "$Root\artifacts\requirements\SRS_He_Sinh_Thai_Thanh_Toan_Fintech_v1.0.md" -Force
}

# Analysis
if (Test-Path "$Root\00_Draft\gap-analysis-campaign-tang-ve-bank.md") {
    Copy-Item "$Root\00_Draft\gap-analysis-campaign-tang-ve-bank.md" "$Root\artifacts\analysis\gap-analysis-campaign-tang-ve-bank.md" -Force
}
if (Test-Path "$Root\00_Draft\phan-tich-chi-tiet-doi-soat-tai-khoan-du-thuong.md") {
    Copy-Item "$Root\00_Draft\phan-tich-chi-tiet-doi-soat-tai-khoan-du-thuong.md" "$Root\artifacts\analysis\phan-tich-chi-tiet-doi-soat-tai-khoan-du-thuong.md" -Force
}
if (Test-Path "$Root\00_Draft\da-vietlott-sms-report-2026.md") {
    Copy-Item "$Root\00_Draft\da-vietlott-sms-report-2026.md" "$Root\artifacts\analysis\da-vietlott-sms-report-2026.md" -Force
}
if (Test-Path "$Root\05_Meetings\bien-ban-hop-vietlott-q3-2026-v2.docx") {
    Copy-Item "$Root\05_Meetings\bien-ban-hop-vietlott-q3-2026-v2.docx" "$Root\artifacts\analysis\bien-ban-hop-vietlott-q3-2026-v2.docx" -Force
}

# Plans
if (Test-Path "$Root\03_Workspace\onboarding-plan-ba-vietlottsms.md") {
    Copy-Item "$Root\03_Workspace\onboarding-plan-ba-vietlottsms.md" "$Root\plans\active\onboarding-plan-ba-vietlottsms.md" -Force
}
if (Test-Path "$Root\00_Draft\Master_Summary_4_Tasks.md") {
    Copy-Item "$Root\00_Draft\Master_Summary_4_Tasks.md" "$Root\plans\completed\Master_Summary_4_Tasks.md" -Force
}

Write-Host "=== Hoàn thành di chuyển và tổ chức sơ bộ ===" -ForegroundColor Green
