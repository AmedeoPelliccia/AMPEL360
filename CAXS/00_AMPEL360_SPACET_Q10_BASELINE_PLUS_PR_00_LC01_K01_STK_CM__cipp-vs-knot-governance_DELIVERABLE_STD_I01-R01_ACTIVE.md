---
document_id: "00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-vs-knot-governance_DELIVERABLE_STD_I01-R01_ACTIVE"
title: "CIPP vs KNOT Governance — Normative Standard"
project: "AMPEL360"
scope: "Differentiation and governance rules for certainty vs uncertainty objects"
owner_aor: "STK_CM"
interfaces:
  required: ["STK_PMO","STK_SE","STK_DAB","STK_CERT"]
category: "DELIVERABLE"
type: "STD"
status: "ACTIVE"
issue_rev: "I01-R01"
---

# CIPP vs KNOT Governance — Normative Standard

## 1. Core Distinction (Normative)

CA360º maintains two fundamentally different types of execution objects that **must not be blurred**:

### 1.1 CIPP (Certainty Integration Pointers and Paths)

**CIPPs are programmable, deterministically identifiable objects** that bind execution to established knowledge bases.

| Property | Definition |
|----------|------------|
| **Nature** | Deterministic integration objects |
| **Purpose** | Reuse certainty |
| **Inputs** | RELEASED/authoritative sources (released baselines, approved standards, validated schemas, certified procedures, known-good integration routes) |
| **Output** | A routable pointer/path that is stable and machine-checkable |
| **Failure mode** | Broken reference (dangling pointer, hash mismatch, incompatible version) |
| **Graph layer** | CIPP Graph (Certainty Layer) |

### 1.2 Uncertainty KNOT

**Uncertainty KNOTs are epistemic state nodes** representing unresolved design/verification/governance uncertainty.

| Property | Definition |
|----------|------------|
| **Nature** | Uncertainty resolution objects |
| **Purpose** | Create certainty |
| **Inputs** | Hypotheses + constraints + impacted ATAs + tasks |
| **Output** | Resolved decision + evidence + (optionally) a minted/updated CIPP |
| **Failure mode** | Insufficient evidence / unresolved coupling / missing signoff |
| **Graph layer** | KNOT Graph (Uncertainty Layer) |

### 1.3 Relationship (Normative)

**CIPP routes execution through known truth. KNOT produces new truth (or refines it) and then should mint/update a CIPP.**

---

## 2. Two-Layer Graph Model (Normative)

CA360º maintains **two graphs that interact but do not blur**:

### 2.1 CIPP Graph (Certainty Layer)

- **Nodes**: CIPPs (certainty objects)
- **Edges**: Deterministic dependencies (requires, implements, exports, consumes)
- **Constraint**: All referenced targets must be RELEASED (or explicitly allowed by policy)
- **Purpose**: Provide stable, reusable execution routes

### 2.2 KNOT Graph (Uncertainty Layer)

- **Nodes**: KNOT states (uncertainty nodes)
- **Edges**: Entanglement and coupling (hard, soft, conditional)
- **Output**: Resolution yields decisions/evidence and may promote nodes into the certainty layer by minting CIPPs
- **Purpose**: Reduce uncertainty through structured work

### 2.3 Promotion Rule (Normative)

**A KNOT is "collapsed" only when it yields:**
1. A released artifact chain (all outputs moved to ACTIVE or RELEASED status)
2. **At least one CIPP** that points to that chain for deterministic reuse

This ensures that new certainty is captured in a machine-executable form.

---

## 3. Governance Placement in v6.0 System

### 3.1 Categories and Ownership

| Artifact Type | Category | Type | Owner AoR |
|---------------|----------|------|-----------|
| CIPP registry | REGISTRY | CAT | STK_CM |
| CIPP definition spec | DELIVERABLE | SPEC | STK_CM or creating AoR |
| CIPP evidence (hash checks, integration tests) | EVIDENCE | LOG \| TST \| EVD | Creating AoR |
| CIPP enabling signoff | SIGNOFF | — | STK_CM \| STK_CERT |
| KNOT problem statement | DELIVERABLE | SPEC | Creating AoR |
| KNOT task outputs | DELIVERABLE | * | Task-assigned AoR |
| KNOT evidence | EVIDENCE | * | Task-assigned AoR |
| KNOT signoff | SIGNOFF | — | STK_CM \| STK_CERT (when compliance/export triggered) |

### 3.2 Deterministic Identity Requirements (Normative)

**A CIPP is valid only if it is deterministically resolvable:**

1. `target_ref` exists (path resolvable in repository)
2. `target_sha256` matches actual file hash
3. `target_status ∈ {ACTIVE, RELEASED}` (prefer RELEASED for "certainty")
4. `version_constraints` are satisfied (semver or Issue-Rev constraints, if specified)
5. `effectivity` is compatible with the caller's PGK slice
6. `intent_key` resolves to valid VISION/MISSION/SCOPE/OUTCOME IDs

**A KNOT is valid only if:**

1. `intent_key` resolves to valid VISION/MISSION/SCOPE/OUTCOME IDs
2. `hypotheses[]` are explicitly stated and tied to `downstream_outcomes[]`
3. `closure_criteria` are testable and measurable
4. `impact_matrix_ref` documents cross-ATA entanglement
5. `task_registry_ref` maps tasks → outputs → evidence → outcomes

---

## 4. CIPP Data Model (Normative)

### 4.1 Required CIPP Fields

See **CIPP Registry** for full schema. Minimum required fields:

```yaml
cipp_id: CIPP-###
cipp_kind: POINTER | PATH | ROUTE | BINDING | EXPORT | DEPLOY
intent_key:
  vision_id: VSN-###
  mission_id: MSN-###
  scope_id: SCP-*
  pathway_ids: [P01, P02, ...]
  outcome_ids: [OUT-###-###, ...]
intent_hash: sha256:...
pgk_scope: PROGRAM/FAMILY/VARIANT/VERSION/* (or explicit PGK)
aor_owner: STK_*
target_refs:
  - path: relative/path/to/artifact.md
    sha256: <hash>
    status: ACTIVE | RELEASED
target_status: ACTIVE | RELEASED
validation_evidence_ref: path/to/evidence
downstream_outcomes: [OUT-###-###, ...]
status: DRAFT | ACTIVE | RELEASED | OBSOLETE
created_by: K## or artifact_id
```

### 4.2 CIPP Kinds (Normative Definitions)

| Kind | Purpose | Example Use |
|------|---------|-------------|
| **POINTER** | Single artifact reference with deterministic hash | Schema baseline, ICD reference |
| **PATH** | Multi-step execution sequence through related artifacts | Certification evidence chain, traceability path |
| **ROUTE** | Integration pathway with branching/conditional logic | Data export route, registry query route |
| **BINDING** | Interface contract enforcement between components | API binding, ICD enforcement |
| **EXPORT** | Deterministic export/transformation of data | SBOM export, DPP manifest generation |
| **DEPLOY** | Deployment/release package with dependencies | Release pack, deployment manifest |

---

## 5. Interaction with Main Workflow SSOT

### 5.1 Pre-Step: Resolve via CIPP if Certainty Exists

**Step 1.5 — "Resolve via CIPP if certainty exists"**

Before instantiating/working a node as uncertain:

1. Search the CIPP registry for matching:
   - `pgk_scope` + axis/ATA + interface_contract
   - Or matching `intent_key` (vision/mission/scope/outcome alignment)

2. If a **valid CIPP exists** and targets are RELEASED:
   - **Execute via CIPP** (deterministic path)
   - Skip KNOT instantiation
   - Record CIPP usage in execution log

3. If **no CIPP exists** (or invalid):
   - Instantiate ONUP (OPT-INS Node Uncertainty Pack)
   - Open/continue KNOT resolution
   - Proceed with workflow Steps 2-8

**Rationale**: This prevents wasted KNOT work when the answer is already known and routable.

### 5.2 Closure Rule Update

When a node is released (workflow Step 8):

1. Ensure any **new stable knowledge** is exported into the certainty layer by creating/updating CIPPs
2. Mint CIPP(s) pointing to:
   - Released artifacts
   - Evidence chains
   - Validated procedures
3. Update CIPP registry with new entries
4. Record KNOT → CIPP promotion in change log

**Gate**: A KNOT cannot be marked "collapsed/closed" unless it has produced at least one CIPP (or justified why none is needed).

---

## 6. CIPP Determinism Gate (CI Enforcement)

### 6.1 Gate Purpose

Make "certainty objects" defensible by enforcing deterministic validity.

### 6.2 Gate Checks (PR-Blocking for In-Scope CIPPs)

The following checks must **pass** for any PR that modifies CIPP registry or CIPP definition files:

1. **No dangling `target_path`**: All paths in `target_refs` must exist in repository
2. **sha256 matches actual file**: Compute sha256 of each target and verify match
3. **Target is not DRAFT**: Targets must have `status ∈ {ACTIVE, RELEASED}` (unless explicitly allowed by policy exception)
4. **Dependencies resolvable and compatible**: All `dependencies` (other CIPPs or artifacts) exist and satisfy version constraints
5. **SIGNOFF exists by STK_CM/STK_CERT** (if applicable): If CIPP changes compliance/export behavior, SIGNOFF artifact required
6. **Intent validation**: `intent_hash` must match computed value: `sha256(canonical_json(intent_key + pgk_scope + aor_owner))`
7. **Outcome trace completeness**: Each `outcome_id` in `downstream_outcomes` must link to:
   - At least one evidence hook
   - At least one deterministic target chain

### 6.3 Implementation

CI workflow (`.github/workflows/ca360_portal_gates.yml`) includes new step:

```yaml
- name: CIPP Determinism Gate
  run: |
    echo "=== Gate: CIPP Determinism Validation ==="
    # Run CIPP validator script
    python scripts/validate_cipp.py --registry CAXS/LEDGERS/*__cipp-registry_*.md
```

---

## 7. Practical Example

### 7.1 Scenario: DPP Circularity KPI Claim

**Uncertainty KNOT**: "Is this DPP circularity KPI claim defensible for Q10 BASELINE PLUS?"

**KNOT work**:
- Tasks produce evidence and signoff
- Validate KPI calculation method
- Generate test results
- Obtain STK_CEGT and STK_CERT approval

**CIPP produced after collapse**:

```yaml
cipp_id: CIPP-001
cipp_kind: ROUTE
intent_key:
  vision_id: VSN-005
  mission_id: MSN-005
  scope_id: SCP-SPACET-Q10-BASELINE-PLUS
  pathway_ids: [P01, P04]
  outcome_ids: [OUT-005-001]
pgk_scope: SPACET/Q10/BASELINE/PLUS/*
aor_owner: STK_CEGT
target_refs:
  - path: CAXS/LEDGERS/85_AMPEL360_...__circularity-kpis_REGISTRY_IDX_I01-R01_ACTIVE.md
    sha256: d4e5f6...
    status: ACTIVE
  - path: CAXS/LEDGERS/85_AMPEL360_...__esg-reporting_REGISTRY_IDX_I01-R01_ACTIVE.md
    sha256: e5f6g7...
    status: ACTIVE
  - path: CAXS/LEDGERS/94_AMPEL360_...__dpp-manifest-schema_DELIVERABLE_SCHEMA_I01-R01_RELEASED.md
    sha256: f6g7h8...
    status: RELEASED
  - path: CAXS/EVIDENCE/85_AMPEL360_...__circularity-validation_EVIDENCE_TST_I01-R01_ACTIVE.md
    sha256: g7h8i9...
    status: ACTIVE
validation_evidence_ref: CAXS/EVIDENCE/85_...__cipp-001-validation_EVIDENCE_LOG_I01-R01_ACTIVE.md
downstream_outcomes: [OUT-005-001]
status: ACTIVE
created_by: K09
```

**Result**: From then on, anyone needing the same outcome uses the CIPP route, not a new KNOT.

---

## 8. Workflow Integration Diagram

```
┌─────────────────────────────────────────────────────────────┐
│ Step 0: Select Portfolio Slice (PGK)                        │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────────┐
│ Step 1: Select OPT-INS Node (Axis + ATA + BLOCK + PHASE)   │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────────┐
│ Step 1.5: Resolve via CIPP if Certainty Exists (NEW)       │
│                                                             │
│ Search CIPP Registry:                                       │
│   - Match pgk_scope + axis/ATA + interface_contract        │
│   - Match intent_key (vision/mission/scope/outcome)        │
│                                                             │
│ ┌─────────────────────┐         ┌─────────────────────┐    │
│ │ Valid CIPP found?   │  YES    │ Execute via CIPP    │    │
│ │ Targets RELEASED?   ├────────►│ (deterministic)     │    │
│ └──────────┬──────────┘         └─────────────────────┘    │
│            │ NO                                             │
└────────────┼────────────────────────────────────────────────┘
             │
┌────────────▼────────────────────────────────────────────────┐
│ Step 2: Instantiate ONUP (Uncertainty Pack)                │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────────┐
│ Steps 3-7: Execute KNOT Tasks → Generate Artifacts         │
└───────────────────────┬─────────────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────────────┐
│ Step 8: Close Loop → Release Artifacts                     │
│                                                             │
│ ┌─────────────────────────────────────────────────┐        │
│ │ Promotion Rule Check:                           │        │
│ │  - Released artifact chain? ✓                   │        │
│ │  - Evidence closure complete? ✓                 │        │
│ │  - At least one CIPP minted? ✓                  │        │
│ └─────────────────────────────────────────────────┘        │
│                                                             │
│ Mint CIPP(s) → Update CIPP Registry → Record Promotion     │
└─────────────────────────────────────────────────────────────┘
```

---

## 9. Registry Schemas/Columns

### 9.1 CIPP Registry Schema

See: **CIPP Registry** (`00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-registry_REGISTRY_CAT_I01-R01_ACTIVE.md`)

### 9.2 Intent Key Schema

```yaml
intent_key:
  vision_id: VSN-###       # Must exist in Vision Registry
  mission_id: MSN-###      # Must exist in Mission Registry
  scope_id: SCP-*          # Must exist in Scope Registry
  pathway_ids: [P01, ...]  # P01-P05 from OPT-INS framework
  outcome_ids: [OUT-###-###, ...] # Must exist in Outcome Registry
```

### 9.3 Intent Hash Calculation

```python
import hashlib
import json

def compute_intent_hash(intent_key, pgk_scope, aor_owner):
    canonical = {
        "intent_key": intent_key,
        "pgk_scope": pgk_scope,
        "aor_owner": aor_owner
    }
    canonical_json = json.dumps(canonical, sort_keys=True, separators=(',', ':'))
    return "sha256:" + hashlib.sha256(canonical_json.encode('utf-8')).hexdigest()
```

---

## 10. Validation Scripts

### 10.1 CIPP Validator

Location: `scripts/validate_cipp.py` (to be created)

**Checks**:
- Intent hash computation and validation
- Target reference existence and hash verification
- Dependency resolution
- Outcome trace completeness

### 10.2 KNOT → CIPP Promotion Validator

Location: `scripts/validate_knot_promotion.py` (to be created)

**Checks**:
- KNOT closure criteria met
- Released artifact chain exists
- At least one CIPP minted
- Evidence closure complete

---

## 11. References

- **CIPP Registry**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-registry_REGISTRY_CAT_I01-R01_ACTIVE.md`
- **Intent Alignment Policy**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-intent-alignment-policy_DELIVERABLE_STD_I01-R01_ACTIVE.md`
- **Vision Registry**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__vision-registry_REGISTRY_IDX_I01-R01_ACTIVE.md`
- **Mission Registry**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_PMO__mission-registry_REGISTRY_IDX_I01-R01_ACTIVE.md`
- **Scope & Outcome Registry**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__scope-outcome-registry_REGISTRY_IDX_I01-R01_ACTIVE.md`
- **Main Workflow SSOT**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-main-workflow-ssot_DELIVERABLE_PROC_I01-R01_ACTIVE.md`

---

**Change History**

| Issue-Rev | Date | Author | Description |
|-----------|------|--------|-------------|
| I01-R01 | 2025-12-19 | STK_CM | Initial normative standard for CIPP vs KNOT governance |
