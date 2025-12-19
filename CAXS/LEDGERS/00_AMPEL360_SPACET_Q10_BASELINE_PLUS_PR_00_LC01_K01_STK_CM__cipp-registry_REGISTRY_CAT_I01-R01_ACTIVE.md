---
document_id: "00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-registry_REGISTRY_CAT_I01-R01_ACTIVE"
title: "CIPP Registry — Certainty Integration Pointers and Paths"
project: "AMPEL360"
scope: "Registry of deterministic integration routes for reusing certainty"
owner_aor: "STK_CM"
category: "REGISTRY"
type: "CAT"
status: "ACTIVE"
issue_rev: "I01-R01"
---

# CIPP Registry — Certainty Integration Pointers and Paths

## Purpose

The **CIPP Registry** is the single source of truth for all Certainty Integration Pointers and Paths (CIPPs) in the CA360º system.

**CIPPs are programmable, deterministically identifiable objects** that bind execution to established knowledge bases (released baselines, approved standards, validated schemas, certified procedures, known-good integration routes).

This registry enables:
1. **Deterministic reuse** of validated knowledge without re-creating uncertainty
2. **Intent-aligned routing** through validated integration paths
3. **Machine-verifiable** reference integrity (hash checks, version validation)
4. **Governance enforcement** of what constitutes "certainty"

---

## Core Distinction: CIPP vs KNOT

### CIPP (Certainty Objects)
- **Nature**: deterministic integration objects
- **Purpose**: reuse certainty
- **Inputs**: RELEASED/authoritative sources
- **Output**: routable pointer/path that is stable and machine-checkable
- **Failure mode**: broken reference (dangling pointer, hash mismatch, incompatible version)

### KNOT (Uncertainty Objects)
- **Nature**: uncertainty resolution objects
- **Purpose**: create certainty
- **Inputs**: hypotheses + constraints + impacted ATAs
- **Output**: resolved decision + evidence + (optionally) a minted/updated CIPP
- **Failure mode**: insufficient evidence / unresolved coupling / missing signoff

**Promotion Rule (Normative)**: A KNOT is "collapsed" only when it yields (a) a released artifact chain and (b) at least one CIPP that points to that chain for deterministic reuse.

---

## CIPP Registry Schema

### Required Fields

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| `cipp_id` | string | Yes | Unique CIPP identifier (format: CIPP-###) |
| `cipp_kind` | string | Yes | POINTER \| PATH \| ROUTE \| BINDING \| EXPORT \| DEPLOY |
| `intent_key` | object | Yes | (vision_id, mission_id, scope_id, pathway_ids[], outcome_ids[]) |
| `intent_hash` | string | Yes | sha256(canonical_json(intent_key + pgk_scope + aor_owner)) |
| `pgk_scope` | string | Yes | Explicit PGK or wildcard policy (e.g., "SPACET/Q10/BASELINE/PLUS/*") |
| `aor_owner` | string | Yes | Accountable AoR for this CIPP |
| `target_refs` | array | Yes | List of target artifact references (path + sha256 + status) |
| `target_status` | string | Yes | Required status of targets: ACTIVE \| RELEASED (prefer RELEASED) |
| `interface_contract_ref` | string | No | ICD/schema/API contract this CIPP guarantees |
| `effectivity` | string | No | PGK slice or condition when this CIPP applies |
| `dependencies` | array | No | Other CIPP_IDs or artifact dependencies |
| `validation_evidence_ref` | string | Yes | Link to evidence proving determinism (hashes, tests) |
| `downstream_outcomes` | array | Yes | List of OUTCOME_IDs with measurable criteria |
| `status` | string | Yes | DRAFT \| ACTIVE \| RELEASED \| OBSOLETE |
| `created_by` | string | Yes | KNOT_ID or artifact that minted this CIPP |
| `notes` | string | No | Additional context |

### Optional Fields for Advanced Use

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| `version_constraints` | string | No | Semver or Issue-Rev constraints (e.g., ">=I02-R01") |
| `execution_procedure_ref` | string | No | Link to deterministic procedure or tool invocation |
| `last_validated` | date | No | Date of last successful validation |
| `next_review_date` | date | No | Scheduled re-validation date |

---

## CIPP Registry Table

| cipp_id | cipp_kind | intent_hash | pgk_scope | aor_owner | target_refs | target_status | interface_contract_ref | validation_evidence_ref | downstream_outcomes | status | created_by | notes |
|---------|-----------|-------------|-----------|-----------|-------------|---------------|------------------------|-------------------------|---------------------|--------|------------|-------|
| CIPP-001 | ROUTE | sha256:a1b2c3... | SPACET/Q10/BASELINE/PLUS/* | STK_CEGT | [`85_AMPEL360_...__circularity-kpis_REGISTRY_IDX_I01-R01_ACTIVE.md:sha256:d4e5f6...`] | ACTIVE | ATA 85 Circularity KPI Schema v1.0 | `__cipp-001-validation_EVIDENCE_LOG` | [OUT-005-001] | ACTIVE | K09 | DPP circularity KPI export route |
| CIPP-002 | POINTER | sha256:b2c3d4... | SPACET/Q10/*/PLUS/PR/30/* | STK_DAB | [`91_AMPEL360_...__ssot-schemas_REGISTRY_CAT_I01-R01_RELEASED.md:sha256:e5f6g7...`] | RELEASED | ATA 91 Schema Registry v2.0 | `__cipp-002-validation_EVIDENCE_LOG` | [OUT-008-001] | RELEASED | K01 | SSOT schema baseline pointer |
| CIPP-003 | BINDING | sha256:c3d4e5... | AIRT/Q100/BASELINE/PLUS/HW/40/* | STK_PHM | [`28_AMPEL360_...__h2-fuel-system-icd_DELIVERABLE_ICD_I02-R03_RELEASED.md:sha256:f6g7h8...`] | RELEASED | ATA 28 H2 Fuel System ICD v2.3 | `__cipp-003-validation_EVIDENCE_TST` | [OUT-001-001, OUT-001-002] | RELEASED | K03 | H2 propulsion interface binding |
| CIPP-004 | PATH | sha256:d4e5f6... | */*/CERT/*/PR/00/LC08/* | STK_CERT | [`98_AMPEL360_...__cert-pack-manifest_DELIVERABLE_MANIFEST_I01-R01_RELEASED.md:sha256:g7h8i9...`, `93_AMPEL360_...__trace-graph-baseline_REGISTRY_IDX_I01-R02_RELEASED.md:sha256:h8i9j0...`] | RELEASED | ATA 98 Cert Pack Schema v1.0 | `__cipp-004-validation_EVIDENCE_EVD` | [OUT-004-001, OUT-004-002] | RELEASED | K08 | Certification evidence path |
| CIPP-005 | EXPORT | sha256:e5f6g7... | SPACET/Q10/BASELINE/PLUS/SW/30/* | STK_DAB | [`95_AMPEL360_...__sbom-export_DELIVERABLE_SBOM_I01-R01_RELEASED.md:sha256:i9j0k1...`] | RELEASED | ATA 95 SBOM Export Schema v1.0 | `__cipp-005-validation_EVIDENCE_LOG` | [OUT-004-001] | RELEASED | K10 | SBOM/BOM export route |
| CIPP-006 | ROUTE | sha256:f6g7h8... | SPACET/Q10/*/PLUS/*/90/* | STK_AI | [`90_AMPEL360_...__ai-model-registry_REGISTRY_CAT_I02-R01_ACTIVE.md:sha256:j0k1l2...`, `96_AMPEL360_...__ai-assurance_DELIVERABLE_POL_I01-R01_RELEASED.md:sha256:k1l2m3...`] | ACTIVE | ATA 90/96 AI Governance Framework | `__cipp-006-validation_EVIDENCE_TST` | [OUT-003-001, OUT-003-002] | ACTIVE | K03 | AI/ML model integration route |

---

## CIPP Validity Rules (Normative)

A CIPP is **valid** only if:

1. **Intent alignment**: `intent_hash` resolves to valid VISION/MISSION/SCOPE/OUTCOME IDs in SSOT registries
2. **Target existence**: All `target_refs` paths exist in repository
3. **Hash integrity**: All `target_refs` sha256 values match actual file hashes
4. **Status constraint**: All targets have `status ∈ {ACTIVE, RELEASED}` (prefer RELEASED for certainty)
5. **Version compatibility**: If `version_constraints` specified, all targets satisfy constraints
6. **Effectivity compatibility**: Caller's PGK slice matches `effectivity` or `pgk_scope`
7. **Evidence closure**: `validation_evidence_ref` exists and is accessible
8. **Outcome traceability**: Each `outcome_id` in `downstream_outcomes` links to evidence hook and deterministic target chain

---

## CIPP Determinism Gate (CI Enforcement)

The following checks are **PR-blocking** for in-scope CIPP artifacts (CATEGORY=REGISTRY, TYPE=CAT or CIPP definition files):

### Gate Checks

1. **No dangling `target_path`**: All paths in `target_refs` must exist
2. **Hash match**: sha256 values must match actual file content
3. **Target not DRAFT**: Targets must be ACTIVE or RELEASED (unless explicitly allowed by policy)
4. **Dependencies resolvable**: All `dependencies` CIPP_IDs exist and are valid
5. **SIGNOFF exists** (if applicable): If CIPP changes compliance/export behavior → SIGNOFF by STK_CM/STK_CERT required
6. **Intent validation**: `intent_hash` must match computed value from `intent_key` + `pgk_scope` + `aor_owner`
7. **Outcome trace completeness**: Each OUTCOME_ID must link to at least one evidence hook and deterministic target chain

---

## Governance Rules

1. **Creation**: CIPPs are minted by collapsed KNOTs or by STK_CM explicit decision
2. **Modification**: Changing a CIPP requires impact analysis on dependent work
3. **Deprecation**: CIPPs move to OBSOLETE when targets superseded or invalidated
4. **Promotion**: KNOT → CIPP promotion requires:
   - KNOT resolved with RELEASED artifacts
   - Evidence closure complete
   - At least one measurable outcome achieved
5. **Review cycle**: ACTIVE CIPPs should be re-validated annually or when dependencies change

---

## References

- **CIPP vs KNOT Governance Policy**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-vs-knot-governance_DELIVERABLE_STD_I01-R01_ACTIVE.md`
- **Intent Alignment Policy**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-intent-alignment-policy_DELIVERABLE_STD_I01-R01_ACTIVE.md`
- **Main Workflow SSOT**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-main-workflow-ssot_DELIVERABLE_PROC_I01-R01_ACTIVE.md`

---

**Change History**

| Issue-Rev | Date | Author | Description |
|-----------|------|--------|-------------|
| I01-R01 | 2025-12-19 | STK_CM | Initial CIPP registry with 6 baseline entries |
