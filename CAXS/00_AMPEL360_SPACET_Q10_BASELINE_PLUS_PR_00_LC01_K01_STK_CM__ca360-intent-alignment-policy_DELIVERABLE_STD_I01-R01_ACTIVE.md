---
document_id: "00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-intent-alignment-policy_DELIVERABLE_STD_I01-R01_ACTIVE"
title: "CA360º Intent Alignment Policy — Normative Standard"
project: "AMPEL360"
scope: "Intent validation rules for CIPP and KNOT identity alignment"
owner_aor: "STK_CM"
interfaces:
  required: ["STK_PMO","STK_SE","STK_DAB","STK_CERT"]
category: "DELIVERABLE"
type: "STD"
status: "ACTIVE"
issue_rev: "I01-R01"
---

# CA360º Intent Alignment Policy — Normative Standard

## 1. Purpose and Scope

This policy establishes **normative requirements** for validating that both CIPPs (Certainty Integration Pointers and Paths) and KNOTs (Uncertainty Resolution Objects) are **directionally aligned** with program intent.

**Key principle**: If CA360º treats CIPPs as "certainty routes" and KNOTs as "uncertainty producers," then both identities must be validated against intent—specifically:

**Vision → Mission → Scope → Pathway → Downstream Results**

Otherwise, you will accumulate perfectly-structured work that is **directionally wrong**.

---

## 2. Normative Intent Contract

### 2.1 Intent Key (Required for All CIPPs and KNOTs)

Every CIPP and KNOT **MUST** carry an **Intent Key**:

```yaml
intent_key:
  vision_id: VSN-###       # What long-term "north star" this supports
  mission_id: MSN-###      # What operational mission objective it advances
  scope_id: SCP-*          # Boundaries (program slice + exclusions)
  pathway_ids: [P01, ...]  # Which execution lane(s) it belongs to (P01-P05)
  outcome_ids: [OUT-###-###, ...] # Intended downstream results (measurable)
```

### 2.2 Deterministic Intent Hash (Machine Enforcement)

For machine enforcement, compute:

```
INTENT_HASH = sha256( canonical_json(INTENT_KEY + PGK_SCOPE + AoR_OWNER) )
```

This becomes the stable **"identity anchor"** that prevents semantic drift.

**Implementation**:

```python
import hashlib
import json

def compute_intent_hash(intent_key, pgk_scope, aor_owner):
    canonical = {
        "intent_key": {
            "vision_id": intent_key["vision_id"],
            "mission_id": intent_key["mission_id"],
            "scope_id": intent_key["scope_id"],
            "pathway_ids": sorted(intent_key["pathway_ids"]),
            "outcome_ids": sorted(intent_key["outcome_ids"])
        },
        "pgk_scope": pgk_scope,
        "aor_owner": aor_owner
    }
    canonical_json = json.dumps(canonical, sort_keys=True, separators=(',', ':'))
    return "sha256:" + hashlib.sha256(canonical_json.encode('utf-8')).hexdigest()
```

---

## 3. Required SSOT Truth Sources

You need **three SSOT registries** (or equivalent pages) that serve as the **"intent oracle"**:

### 3.1 Vision Registry (SSOT)

**Document**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__vision-registry_REGISTRY_IDX_I01-R01_ACTIVE.md`

**Contents**:
- `VISION_ID`: Unique identifier
- `definition`: Long-term strategic objective
- `time_horizon`: Target timeframe
- `disallowed_directions`: Explicit exclusions

### 3.2 Mission Registry (SSOT)

**Document**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_PMO__mission-registry_REGISTRY_IDX_I01-R01_ACTIVE.md`

**Contents**:
- `MISSION_ID`: Unique identifier
- `measurable mission objectives`: Quantifiable targets
- `success_metrics`: Acceptance criteria
- `constraints`: Known limitations

### 3.3 Scope & Outcome Registry (SSOT)

**Document**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__scope-outcome-registry_REGISTRY_IDX_I01-R01_ACTIVE.md`

**Contents**:

**Scope**:
- `SCOPE_ID`: Allowed (PROGRAM/FAMILY/VARIANT/VERSION) + included/excluded ATAs/blocks/phases

**Outcome**:
- `OUTCOME_ID`: Downstream result definitions and acceptance metrics (DOIs/KPIs)

**Rule (Normative)**: A CIPP/KNOT identity is **invalid** if it references IDs not present and RELEASED (or ACTIVE if allowed).

---

## 4. CIPP Intent Validation Rules (Normative)

### 4.1 Nature

CIPPs must be **directionally consistent AND deterministically executable**.

### 4.2 Mandatory Fields for CIPP Identity

```yaml
cipp_id: CIPP-###
intent_key:
  vision_id: VSN-###
  mission_id: MSN-###
  scope_id: SCP-*
  pathway_ids: [P01, ...]
  outcome_ids: [OUT-###-###, ...]
intent_hash: sha256:...
pgk_scope: PROGRAM/FAMILY/VARIANT/VERSION/* (or explicit PGK)
aor_owner: STK_*
target_refs:
  - path: relative/path/to/artifact.md
    sha256: <hash>
    status: ACTIVE | RELEASED
validation_evidence_ref: path/to/evidence
downstream_outcomes:
  - outcome_id: OUT-###-###
    metric: "..."
    target: "..."
    evidence_hook: "..."
status: DRAFT | ACTIVE | RELEASED | OBSOLETE
```

### 4.3 Validation Rule (Normative)

A CIPP **cannot be promoted to "CERTAINTY"** (status=ACTIVE or RELEASED) unless:

1. **Intent key resolves**: `INTENT_KEY` resolves to valid SSOT Vision/Mission/Scope/Outcomes
2. **Targets are released**: All `target_refs` are RELEASED (or policy-approved) and hashes match
3. **Outcomes have verifiable measurement hooks**: Each `outcome_id` has:
   - Evidence pointers that exist and are accessible
   - Measurable criteria that can be tested
4. **Category↔AoR constraints satisfied**: SIGNOFF/EXPORT_CONTROL triggers require appropriate AoR approval
5. **Intent hash matches**: Computed `intent_hash` equals stored value (prevents drift)

---

## 5. KNOT Intent Validation Rules (Normative)

### 5.1 Nature

KNOTs must be **directionally consistent AND outcome-closed**.

### 5.2 Mandatory Fields for KNOT Identity

```yaml
knot_id: K##
problem_statement: "..."
intent_key:
  vision_id: VSN-###
  mission_id: MSN-###
  scope_id: SCP-*
  pathway_ids: [P01, ...]
  outcome_ids: [OUT-###-###, ...]
intent_hash: sha256:...
hypotheses:
  - hypothesis_id: H01
    statement: "..."
    outcome_ids: [OUT-###-###, ...]
closure_criteria:
  - criterion_id: CC01
    test: "..."
    target: "..."
impact_matrix_ref: path/to/ata_impact_matrix.csv
task_registry_ref: path/to/task_registry.md
downstream_results:
  - outcome_id: OUT-###-###
    metric: "..."
    target: "..."
    evidence_hook: "..."
status: OPEN | ACTIVE | CLOSED | OBSOLETE
```

### 5.3 Validation Rule (Normative)

A KNOT is **not "collapsed"** (status=CLOSED) unless:

1. **Intent key resolves**: `INTENT_KEY` resolves to valid SSOT Vision/Mission/Scope/Outcomes
2. **Produces released outputs**: All task outputs moved to ACTIVE or RELEASED status
3. **Intended outcomes are met**: Each `outcome_id` has:
   - Evidence artifacts produced and accessible
   - Measurement criteria satisfied
4. **Mints at least one CIPP** (when applicable): Routes future work deterministically to those outcomes
5. **Intent hash matches**: Computed `intent_hash` equals stored value

**Exception**: A KNOT may close without minting a CIPP if justified (e.g., one-time exploration, negative result, no reusable route). Justification must be documented in closure notes.

---

## 6. CI Gates to Enforce Intent Alignment (PR-Blocking)

Add two PR-blocking gates for **in-scope governed artifacts** (CATEGORY ∈ {DELIVERABLE, REGISTRY, EVIDENCE, SIGNOFF}):

### 6.1 Gate A — Intent Reference Validity

**Purpose**: Ensure all intent references are valid and current.

**Checks**:

1. `VISION_ID`, `MISSION_ID`, `SCOPE_ID`, `OUTCOME_ID` **must exist** in respective registries
2. Referenced items **must be** `status ∈ {ACTIVE, RELEASED}`
3. `INTENT_HASH` **must match** computed value (prevents "edit intent without changing identity")

**Implementation**:

```yaml
- name: Gate A - Intent Reference Validity
  run: |
    echo "=== Gate A: Intent Reference Validity ==="
    python scripts/validate_intent_references.py \
      --vision-registry CAXS/LEDGERS/*__vision-registry_*.md \
      --mission-registry CAXS/LEDGERS/*__mission-registry_*.md \
      --scope-outcome-registry CAXS/LEDGERS/*__scope-outcome-registry_*.md \
      --artifacts "CAXS/**/*_DELIVERABLE_*.md" "CAXS/**/*_REGISTRY_*.md"
```

**Exit code**: Non-zero if any intent reference is invalid or intent hash mismatch.

### 6.2 Gate B — Outcome Trace Completeness

**Purpose**: Ensure outcomes are traceable to evidence and targets.

**Checks**:

**For CIPP**: Each `OUTCOME_ID` must link to:
- At least one **evidence hook** (path exists and accessible)
- At least one **deterministic target chain** (all targets resolvable)

**For KNOT**: Each `OUTCOME_ID` must link to:
- At least one **task output** (artifact produced)
- At least one **evidence artifact** (validation/test results)
- **Signoff** where policy requires (CATEGORY=SIGNOFF or EXPORT_CONTROL trigger)

**Implementation**:

```yaml
- name: Gate B - Outcome Trace Completeness
  run: |
    echo "=== Gate B: Outcome Trace Completeness ==="
    python scripts/validate_outcome_traces.py \
      --scope-outcome-registry CAXS/LEDGERS/*__scope-outcome-registry_*.md \
      --cipp-registry CAXS/LEDGERS/*__cipp-registry_*.md \
      --knot-artifacts "CAXS/**/*K*__*_DELIVERABLE_*.md"
```

**Exit code**: Non-zero if any outcome lacks required evidence hooks or target chains.

---

## 7. Minimal Template Additions

### 7.1 Add to KNOT Problem Statement Front-Matter

```yaml
---
document_id: "<v6.0 canonical filename>"
knot_id: K##
problem_statement: "..."
intent:
  vision_id: VSN-001
  mission_id: MSN-021
  scope_id: SCP-SPACET-Q10-BASELINE-PLUS
  pathway_ids: [P01, P02, P04]
  outcome_ids: [OUT-085-001, OUT-021-004]
  intent_hash: "sha256:..."
downstream_results:
  - outcome_id: OUT-085-001
    metric: "Material Circularity"
    target: ">= 0.85"
    evidence_hook: "CAXS/EVIDENCE/85_...__circularity-validation_EVIDENCE_TST_I01-R01_ACTIVE.md"
  - outcome_id: OUT-021-004
    metric: "ESG Reporting Completeness"
    target: "100%"
    evidence_hook: "CAXS/EVIDENCE/85_...__esg-audit_EVIDENCE_EVD_I01-R01_ACTIVE.md"
---
```

### 7.2 Add to CIPP Registry Rows (CSV Format)

For a CSV version of CIPP registry:

```csv
cipp_id,intent_hash,vision_id,mission_id,scope_id,pathway_ids,outcome_ids,pgk_scope,aor_owner,target_refs,target_sha256,validation_evidence_ref,status
CIPP-001,sha256:a1b2c3...,VSN-005,MSN-005,SCP-SPACET-Q10-BASELINE-PLUS,"P01,P04",OUT-005-001,SPACET/Q10/BASELINE/PLUS/*,STK_CEGT,"85_AMPEL360_...__circularity-kpis_REGISTRY_IDX_I01-R01_ACTIVE.md",sha256:d4e5f6...,__cipp-001-validation_EVIDENCE_LOG,ACTIVE
```

---

## 8. Workflow Integration

### 8.1 Insert Mandatory Step: Intent Validation

**Step 2.5 — Intent Validation**

After selecting OPT-INS node (Step 1) and before instantiating ONUP (Step 2):

1. **Validate INTENT_KEY** against Vision/Mission/Scope/Outcome SSOT registries
   - All IDs must exist and be ACTIVE or RELEASED
   - Compute and verify `intent_hash`

2. **Search for valid CIPP** with same `intent_hash` + `pgk_scope`
   - If found → **Execute via CIPP** (deterministic route)
   - If not found → **Continue to KNOT resolution**

3. **Record intent validation** in execution log

### 8.2 Update Closure Rule

**Release cannot occur unless Outcome Trace Completeness passes** (Gate B).

Specifically:
- All `outcome_ids` referenced by CIPP/KNOT must have:
  - Evidence hooks that exist and are accessible
  - Measurable criteria that have been tested/verified
  - Signoff where required by policy

---

## 9. Validation Scripts (To Be Implemented)

### 9.1 `scripts/validate_intent_references.py`

**Purpose**: Validate intent key references against SSOT registries.

**Inputs**:
- Vision registry path
- Mission registry path
- Scope & outcome registry path
- List of artifact paths to validate

**Checks**:
- All `vision_id`, `mission_id`, `scope_id`, `outcome_id` exist in registries
- Referenced items have `status ∈ {ACTIVE, RELEASED}`
- `intent_hash` matches computed value

**Output**: Exit code 0 (pass) or non-zero (fail) with error details

### 9.2 `scripts/validate_outcome_traces.py`

**Purpose**: Validate outcome trace completeness for CIPPs and KNOTs.

**Inputs**:
- Scope & outcome registry path
- CIPP registry path
- List of KNOT artifact paths

**Checks**:
- For each CIPP: outcomes link to evidence hooks and target chains
- For each KNOT: outcomes link to task outputs, evidence, and signoffs
- All referenced paths exist and are accessible

**Output**: Exit code 0 (pass) or non-zero (fail) with error details

### 9.3 `scripts/compute_intent_hash.py`

**Purpose**: Utility to compute intent hash for manual verification or testing.

**Inputs**:
- Intent key (as JSON)
- PGK scope
- AoR owner

**Output**: Computed `sha256:...` hash value

---

## 10. Pathway Definitions (P01-P05)

For reference, the OPT-INS framework pathways:

| Pathway | Name | Description |
|---------|------|-------------|
| **P01** | Design & Architecture | Requirements, system design, MBSE, ICD definition |
| **P02** | Implementation & Integration | Build, integration, component development |
| **P03** | Verification & Validation | Testing, V&V campaigns, certification evidence |
| **P04** | Operations & Sustainment | Operations, MRO, fleet management, circularity |
| **P05** | Governance & Compliance | CM, safety, certification, export control, signoffs |

**Note**: Pathways are **not mutually exclusive**. A CIPP or KNOT may span multiple pathways (e.g., [P01, P03, P05] for a certification-driven design artifact).

---

## 11. Example: Intent Key for CIPP-001

### 11.1 Intent Key

```yaml
intent_key:
  vision_id: VSN-005  # Circular Product Lifecycle
  mission_id: MSN-005  # Circular Material Recovery
  scope_id: SCP-SPACET-Q10-BASELINE-PLUS
  pathway_ids: [P01, P04]  # Design + Operations/Sustainment
  outcome_ids: [OUT-005-001]  # Material Circularity >= 0.85
```

### 11.2 Computed Intent Hash

```python
compute_intent_hash(
    intent_key={
        "vision_id": "VSN-005",
        "mission_id": "MSN-005",
        "scope_id": "SCP-SPACET-Q10-BASELINE-PLUS",
        "pathway_ids": ["P01", "P04"],
        "outcome_ids": ["OUT-005-001"]
    },
    pgk_scope="SPACET/Q10/BASELINE/PLUS/*",
    aor_owner="STK_CEGT"
)
# Output: sha256:a1b2c3d4e5f6...
```

### 11.3 Validation

1. Check Vision Registry: `VSN-005` exists and status=ACTIVE ✓
2. Check Mission Registry: `MSN-005` exists and status=ACTIVE ✓
3. Check Scope Registry: `SCP-SPACET-Q10-BASELINE-PLUS` exists and status=ACTIVE ✓
4. Check Outcome Registry: `OUT-005-001` exists and status=ACTIVE ✓
5. Verify intent hash matches computed value ✓

**Result**: Intent key is valid. CIPP-001 may proceed to determinism validation.

---

## 12. References

- **CIPP vs KNOT Governance**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-vs-knot-governance_DELIVERABLE_STD_I01-R01_ACTIVE.md`
- **CIPP Registry**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-registry_REGISTRY_CAT_I01-R01_ACTIVE.md`
- **Vision Registry**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__vision-registry_REGISTRY_IDX_I01-R01_ACTIVE.md`
- **Mission Registry**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_PMO__mission-registry_REGISTRY_IDX_I01-R01_ACTIVE.md`
- **Scope & Outcome Registry**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__scope-outcome-registry_REGISTRY_IDX_I01-R01_ACTIVE.md`
- **Main Workflow SSOT**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-main-workflow-ssot_DELIVERABLE_PROC_I01-R01_ACTIVE.md`

---

**Change History**

| Issue-Rev | Date | Author | Description |
|-----------|------|--------|-------------|
| I01-R01 | 2025-12-19 | STK_CM | Initial intent alignment policy with normative validation rules |
