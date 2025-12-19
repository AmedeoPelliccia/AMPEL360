---
document_id: "00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__scope-outcome-registry_REGISTRY_IDX_I01-R01_ACTIVE"
title: "CA360º Scope & Outcome Registry — SSOT"
project: "AMPEL360"
scope: "Scope boundaries and outcome definitions for intent validation"
owner_aor: "STK_CM"
category: "REGISTRY"
type: "IDX"
status: "ACTIVE"
issue_rev: "I01-R01"
---

# CA360º Scope & Outcome Registry — SSOT

## Purpose

This registry defines the canonical set of:
1. **Scope Identifiers (SCOPE_ID)**: Program/family/variant boundaries with explicit inclusions and exclusions
2. **Outcome Identifiers (OUTCOME_ID)**: Measurable downstream results with acceptance criteria

Both are used for CIPP and KNOT intent validation to ensure work aligns with program boundaries and produces verifiable results.

---

## Part 1: Scope Registry

### Scope Schema

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| `scope_id` | string | Yes | Unique scope identifier (format: SCP-PROGRAM-FAMILY-VARIANT-VERSION) |
| `name` | string | Yes | Human-readable scope name |
| `pgk_slice` | string | Yes | PGK wildcard pattern (e.g., "SPACET/Q10/BASELINE/PLUS/*") |
| `included_atas` | string | Yes | Comma-separated ATA ranges included in scope |
| `excluded_atas` | string | No | Comma-separated ATA ranges explicitly excluded |
| `included_blocks` | string | Yes | Comma-separated BLOCK ranges included |
| `included_phases` | string | Yes | Comma-separated PHASE ranges included |
| `exclusion_rationale` | string | No | Justification for exclusions |
| `owner_aor` | string | Yes | Primary AoR accountable for scope definition |
| `status` | string | Yes | ACTIVE \| RELEASED \| OBSOLETE |
| `notes` | string | No | Additional context |

### Scope Registry Table

| scope_id | name | pgk_slice | included_atas | excluded_atas | included_blocks | included_phases | exclusion_rationale | owner_aor | status | notes |
|----------|------|-----------|---------------|---------------|-----------------|-----------------|---------------------|-----------|--------|-------|
| SCP-SPACET-Q10-BASELINE-PLUS | SPACET Q10 Baseline PLUS | SPACET/Q10/BASELINE/PLUS/* | 00-116 | 13-17,19,37,41,48,58-69 | 00-90 | LC01-LC14 | Reserved/not applicable ATAs per ATA allowlist | STK_CM | ACTIVE | Primary SPACET baseline scope |
| SCP-SPACET-Q10-CERT-PLUS | SPACET Q10 Certification PLUS | SPACET/Q10/CERT/PLUS/* | 00-116 | 13-17,19,37,41,48,58-69,80-89 | 00-90 | LC07-LC08,LC10 | Certification scope excludes off-board infrastructure | STK_CERT | ACTIVE | Certification-only scope |
| SCP-AIRT-Q100-BASELINE-PLUS | AIRT Q100 Baseline PLUS | AIRT/Q100/BASELINE/PLUS/* | 00-116 | 13-17,19,37,41,48,58-69,84,110 | 00-90 | LC01-LC14 | Reserved ATAs + space-specific chapters excluded | STK_CM | ACTIVE | BWB H2-electric baseline |
| SCP-AIRT-Q100-FLIGHT-TEST-PLUS | AIRT Q100 Flight Test PLUS | AIRT/Q100/FLIGHT_TEST/PLUS/* | 00-79,100-116 | 13-17,19,37,41,48,58-69,80-89 | 00-60 | LC05,LC08,LC11-LC12 | Focus on onboard systems and test/ops phases | STK_TEST | ACTIVE | Flight test campaign scope |
| SCP-SPACET-QHABITAT-BASELINE-PLUSULTRA | SPACET Habitat Baseline PLUSULTRA | SPACET/QHABITAT/BASELINE/PLUSULTRA/* | 00-116 | 13-17,19,37,41,48,58-69 | 00-90 | LC01-LC14 | Full habitat-class vehicle scope | STK_CM | ACTIVE | Advanced habitat variant |
| SCP-CROSS-PROGRAM-DIGITAL | Cross-Program Digital Infrastructure | */*/*/*/PR/30,90 | 90-99 | none | 30,90 | LC01,LC03,LC09,LC10 | Digital/AI/ledger scope across all programs | STK_DAB | ACTIVE | Shared digital assets |

---

## Part 2: Outcome Registry

### Outcome Schema

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| `outcome_id` | string | Yes | Unique outcome identifier (format: OUT-MSN-###) |
| `name` | string | Yes | Short outcome name |
| `mission_id` | string | Yes | Parent MISSION_ID this outcome supports |
| `metric_type` | string | Yes | DOI \| KPI \| MILESTONE \| EVIDENCE |
| `metric_definition` | string | Yes | Clear definition of what is measured |
| `target_value` | string | Yes | Acceptance threshold (e.g., ">= 0.85", "< 5%", "COMPLETE") |
| `measurement_method` | string | Yes | How the metric is measured/verified |
| `evidence_hook` | string | No | Path to evidence artifact or registry entry |
| `owner_aor` | string | Yes | AoR accountable for outcome delivery |
| `status` | string | Yes | ACTIVE \| RELEASED \| OBSOLETE |
| `notes` | string | No | Additional context |

### Outcome Registry Table

| outcome_id | name | mission_id | metric_type | metric_definition | target_value | measurement_method | evidence_hook | owner_aor | status | notes |
|------------|------|------------|-------------|-------------------|--------------|-------------------|---------------|-----------|--------|-------|
| OUT-001-001 | H2 Range Achievement | MSN-001 | KPI | Aircraft range with full H2 fuel load | >= 1000 km | Flight test measurement + simulation validation | ATA 28/71 test results | STK_PHM | ACTIVE | Primary propulsion KPI |
| OUT-001-002 | H2 System TRL | MSN-001 | MILESTONE | Technology Readiness Level of H2 propulsion system | TRL 8+ | NASA TRL assessment with authority review | LC04 analysis evidence | STK_PHM | ACTIVE | Certification prerequisite |
| OUT-002-001 | Digital Twin Coverage | MSN-002 | KPI | Percentage of critical systems with validated digital twin | 100% | System-by-system validation report | ATA 101 catalog | STK_DAB | ACTIVE | Baseline requirement |
| OUT-002-002 | Digital Twin Accuracy | MSN-002 | KPI | Prediction error vs. flight test data | < 5% | Statistical analysis of twin vs. actual performance | ATA 108 test results | STK_TEST | ACTIVE | Fidelity validation |
| OUT-003-001 | PHM Detection Rate | MSN-003 | KPI | True positive rate for anomaly detection | > 90% | Confusion matrix analysis on test dataset | ATA 45/90 validation | STK_AI | ACTIVE | Safety-critical performance |
| OUT-003-002 | PHM False Positive Rate | MSN-003 | KPI | False alarm rate | < 1% | Operational data analysis over 100 flight hours | ATA 96 monitoring logs | STK_AI | ACTIVE | Operational acceptability |
| OUT-004-001 | Cert Artifact Automation | MSN-004 | KPI | Percentage of certification artifacts auto-generated | >= 80% | Count of auto-generated vs. manual artifacts | ATA 98 manifest | STK_CERT | ACTIVE | Efficiency target |
| OUT-004-002 | Traceability Completeness | MSN-004 | KPI | Percentage of requirements with complete trace to V&V | 100% | Automated trace query results | ATA 93 trace graph | STK_SE | ACTIVE | Certification requirement |
| OUT-005-001 | Material Circularity | MSN-005 | KPI | Material Circularity Index for vehicle | >= 0.85 | MCI calculation per Ellen MacArthur Foundation method | ATA 85/94 DPP data | STK_CEGT | ACTIVE | ESG commitment |
| OUT-005-002 | Hazardous Waste | MSN-005 | KPI | Percentage of waste to landfill (hazardous) | 0% | Waste stream tracking and certification | ATA 85 circularity logs | STK_CEGT | ACTIVE | Environmental compliance |
| OUT-006-001 | Encryption Coverage | MSN-006 | KPI | Percentage of critical data paths with encryption | 100% | Network architecture audit | ATA 87 security evidence | STK_CY | ACTIVE | Zero-trust baseline |
| OUT-006-002 | NIST CSF Compliance | MSN-006 | EVIDENCE | NIST Cybersecurity Framework 2.0 compliance evidence | COMPLETE | Third-party audit report | ATA 20 cyber governance | STK_CY | ACTIVE | Authority requirement |
| OUT-007-001 | Launch Turnaround Time | MSN-007 | KPI | Mean turnaround time between launches | < 24 hours | Operations log analysis | ATA 80-89 ops data | STK_SPACEPORT | ACTIVE | Operational efficiency |
| OUT-007-002 | On-Time Launch Rate | MSN-007 | KPI | Percentage of launches within scheduled window | >= 95% | Schedule adherence tracking | ATA 11 ops reports | STK_OPS | ACTIVE | Reliability metric |
| OUT-008-001 | MBSE Model Coverage | MSN-008 | KPI | Percentage of design artifacts in SysML v2 | 100% | Artifact inventory vs. SysML repository | SE model registry | STK_SE | ACTIVE | MBSE convergence |
| OUT-009-001 | Safety Case Automation | MSN-009 | KPI | Percentage of safety case auto-generated | >= 70% | Safety artifact count analysis | ATA 07 safety evidence | STK_SAF | ACTIVE | Efficiency + consistency |
| OUT-010-001 | Test Cycle Reduction | MSN-010 | KPI | Percentage reduction in integration test cycle time | >= 50% | Baseline vs. current cycle time comparison | ATA 100 test logs | STK_TEST | ACTIVE | Development velocity |

## Governance Rules

### Scope Registry
1. **Addition**: New SCOPE_ID requires STK_CM + program leadership approval
2. **Modification**: Scope changes require impact analysis on all dependent CIPP/KNOT items
3. **Deprecation**: SCOPE_ID moves to OBSOLETE when program phase complete
4. **PGK alignment**: `pgk_slice` must use valid PGK field values per v6.0 nomenclature

### Outcome Registry
1. **Addition**: New OUTCOME_ID requires parent MISSION_ID approval
2. **Modification**: Target value changes require stakeholder review and traceability update
3. **Deprecation**: OUTCOME_ID moves to OBSOLETE when superseded or no longer measured
4. **Mission linking**: All OUTCOME_IDs must reference an ACTIVE MISSION_ID
5. **Evidence hooks**: RELEASED outcomes must have valid `evidence_hook` references

## Validation Constraints

### Scope
- `scope_id` must match regex: `^SCP-[A-Z]+-[A-Z0-9]+-[A-Z_]+-[A-Z]+$`
- `scope_id` must be unique (no duplicates)
- `pgk_slice` must use valid PGK components per v6.0 vocabulary
- `status` must be one of: ACTIVE, RELEASED, OBSOLETE

### Outcome
- `outcome_id` must match regex: `^OUT-\d{3}-\d{3}$`
- `outcome_id` must be unique (no duplicates)
- `mission_id` must exist in Mission Registry with ACTIVE status
- `metric_type` must be one of: DOI, KPI, MILESTONE, EVIDENCE
- `status` must be one of: ACTIVE, RELEASED, OBSOLETE
- `target_value` must be measurable/testable

## References

- **Vision Registry**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__vision-registry_REGISTRY_IDX_I01-R01_ACTIVE.md`
- **Mission Registry**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_PMO__mission-registry_REGISTRY_IDX_I01-R01_ACTIVE.md`
- **Intent Alignment Policy**: `__ca360-intent-alignment-policy_DELIVERABLE_STD`

---

**Change History**

| Issue-Rev | Date | Author | Description |
|-----------|------|--------|-------------|
| I01-R01 | 2025-12-19 | STK_CM | Initial scope and outcome registry |
