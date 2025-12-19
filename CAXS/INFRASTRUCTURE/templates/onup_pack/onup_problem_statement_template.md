---
title: "Node Problem Statement — {{AXIS}} / ATA {{ATA}} / BLOCK {{BLOCK}} / {{PHASE}}"
project: "AMPEL360"
program: "{{PROGRAM}}"
family: "{{FAMILY}}"
variant: "{{VARIANT}}"
version: "{{VERSION}}"
model: "{{MODEL}}"
block: "{{BLOCK}}"
phase: "{{PHASE}}"
knot: "{{KNOT}}"
primary_aor: "{{PRIMARY_AOR}}"
issue_rev: "{{ISSUE_REV}}"
status: "{{STATUS}}"
node_subject: "{{NODE_SUBJECT}}"
intent:
  vision_id: "{{VISION_ID}}"  # e.g., VSN-001
  mission_id: "{{MISSION_ID}}"  # e.g., MSN-005
  scope_id: "{{SCOPE_ID}}"  # e.g., SCP-SPACET-Q10-BASELINE-PLUS
  pathway_ids: ["{{PATHWAY_1}}", "{{PATHWAY_2}}"]  # e.g., [P01, P04]
  outcome_ids: ["{{OUTCOME_ID_1}}", "{{OUTCOME_ID_2}}"]  # e.g., [OUT-005-001]
  intent_hash: "{{INTENT_HASH}}"  # sha256 computed from intent_key + pgk_scope + aor_owner
---

# Node Problem Statement — {{AXIS}} / ATA {{ATA}} / BLOCK {{BLOCK}} / {{PHASE}}

## 1. Context
Describe why this node exists, what it controls, and its boundary conditions.

## 2. Intent Alignment (normative)

This KNOT is aligned to the following program intent:

### Vision
**{{VISION_ID}}**: {{VISION_NAME}}
{{VISION_DESCRIPTION}}

### Mission
**{{MISSION_ID}}**: {{MISSION_NAME}}
{{MISSION_OBJECTIVE}}

### Scope
**{{SCOPE_ID}}**: {{SCOPE_NAME}}
Program slice: {{PGK_SCOPE}}

### Downstream Results (measurable outcomes)

| Outcome ID | Metric | Target | Evidence Hook |
|------------|--------|--------|---------------|
| {{OUTCOME_ID_1}} | {{METRIC_1}} | {{TARGET_1}} | {{EVIDENCE_HOOK_1}} |
| {{OUTCOME_ID_2}} | {{METRIC_2}} | {{TARGET_2}} | {{EVIDENCE_HOOK_2}} |

**Note**: All intent references (vision_id, mission_id, scope_id, outcome_ids) must exist in SSOT registries and be ACTIVE or RELEASED.

## 3. Uncertainty statement (normative)
Define the uncertainty as testable claims:
- U1: {{UNCERTAINTY_1}}
- U2: {{UNCERTAINTY_2}}

## 4. Hypotheses / candidate resolutions

| Hypothesis ID | Statement | Tied to Outcome IDs |
|---------------|-----------|---------------------|
| H1 | {{HYPOTHESIS_1}} | {{OUTCOME_ID_1}} |
| H2 | {{HYPOTHESIS_2}} | {{OUTCOME_ID_2}} |
| H3 | {{HYPOTHESIS_3}} | {{OUTCOME_ID_1}}, {{OUTCOME_ID_2}} |

## 5. Acceptance criteria (collapse criteria)
A node may be considered "collapsed" only when:
- C1: {{CRITERION_1}} (measurable)
- C2: {{CRITERION_2}} (measurable)
- C3: {{CRITERION_3}} (measurable)
- **C4**: At least one CIPP minted pointing to released artifacts (unless justified exception)

## 6. Method of Compliance / Evidence acceptability (pointer)
Reference MoC mapping rules and evidence acceptability basis:
- MoC basis link: {{MOC_BASIS_LINK}}
- Evidence rules link: {{EVIDENCE_RULES_LINK}}

## 7. Impact / entanglement summary
Summarize cross-ATA impacts; the authoritative list is the impact matrix CSV.
- Highest-severity coupling: {{TOP_COUPLING}}
- Safety/security triggers: {{SAFETY_SECURITY_TRIGGERS}}

## 8. Planned resolution approach (pathways P01–P05)
- P01: {{P01_PLAN}}
- P02: {{P02_PLAN}}
- P03: {{P03_PLAN}}
- P04: {{P04_PLAN}}
- P05: {{P05_PLAN}}

## 9. Required signoffs (if any)
If closure requires SIGNOFF:
- Signoff required: {{SIGNOFF_REQUIRED}} (true/false)
- Signoff authority AoR: {{SIGNOFF_AOR}} (must be STK_CM or STK_CERT)
- Decision artifact target: {{SIGNOFF_TARGET_LINK}}

## 10. CIPP Minting Plan (normative)

Upon successful KNOT collapse, the following CIPP(s) will be created:

| CIPP ID | CIPP Kind | Target Artifacts | Intent Hash | Notes |
|---------|-----------|------------------|-------------|-------|
| {{CIPP_ID_1}} | {{CIPP_KIND_1}} | {{TARGET_ARTIFACTS_1}} | {{INTENT_HASH}} | {{CIPP_NOTES_1}} |
| {{CIPP_ID_2}} | {{CIPP_KIND_2}} | {{TARGET_ARTIFACTS_2}} | {{INTENT_HASH}} | {{CIPP_NOTES_2}} |

**Exception clause**: If no CIPP can be minted, document justification here:
- {{CIPP_EXCEPTION_JUSTIFICATION}}

## References

- **CIPP vs KNOT Governance**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-vs-knot-governance_DELIVERABLE_STD_I01-R01_ACTIVE.md`
- **Intent Alignment Policy**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-intent-alignment-policy_DELIVERABLE_STD_I01-R01_ACTIVE.md`
- **Vision Registry**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__vision-registry_REGISTRY_IDX_I01-R01_ACTIVE.md`
- **Mission Registry**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_PMO__mission-registry_REGISTRY_IDX_I01-R01_ACTIVE.md`
- **Scope & Outcome Registry**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__scope-outcome-registry_REGISTRY_IDX_I01-R01_ACTIVE.md`

