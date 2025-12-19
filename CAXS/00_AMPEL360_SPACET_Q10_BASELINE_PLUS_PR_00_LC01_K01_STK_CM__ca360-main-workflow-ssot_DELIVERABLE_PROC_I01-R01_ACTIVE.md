---
document_id: "00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-main-workflow-ssot_DELIVERABLE_PROC_I01-R01_ACTIVE"
title: "CA360º Main Workflow — SSOT"
project: "AMPEL360"
scope: "CAXS Portal (CA360º) — role-routed execution workflow"
owner_aor: "STK_CM"
interfaces:
  required: ["STK_PMO","STK_SE","STK_TEST","STK_CERT","STK_SAF","STK_CY","STK_DAB","STK_OPS","STK_MRO","STK_CEGT","STK_SPACEPORT","STK_PHM","STK_AI"]
status: "ACTIVE"
issue_rev: "I01-R01"
---

# CA360º Main Workflow — SSOT

## 1. Intent

Define the single source of truth (SSOT) workflow to execute AMPEL360 work in CA360º:

1) choose a **portfolio slice** (PROGRAM/FAMILY/VARIANT/VERSION),  
2) choose an **OPT-INS node** (Axis + ATA + BLOCK + PHASE),  
3) extract **AoR-assigned KNOTs**,  
4) perform **tasking** (DELIVERABLE ↔ EVIDENCE ↔ SIGNOFF),  
5) **close the loop** (collapse uncertainty → RELEASED with audit defensibility).

This workflow is **deterministic**, **gate-enforced**, and **certifiable-grade**.

---

## 2. Authoritative references

### 2.1 Portal SSOT and contracts
- Portal entrypoints SSOT: `CAXS/INFRASTRUCTURE/indexes/portal_entrypoints_index.md`
- Validation report template: `CAXS/REPORTS/validation/ca360_portal_validation_report.md`
- Exceptions registry: `CAXS/INFRASTRUCTURE/validators/exceptions.yml`
- One Official Chain uniqueness: `CAXS/INFRASTRUCTURE/validators/one_official_chain_uniqueness.md`
- Portal contract file list: `CAXS/INFRASTRUCTURE/portal_contract_files_v1.0.md`
- Release evidence pack template: `CAXS/REPORTS/validation/release_evidence_pack_template.md`

### 2.2 v6.0 nomenclature enforcement
- v6.0 config root: `configs/nomenclature/v6/`
  - `vocabulary.json`
  - `regex_constraints.json`
  - `category_aor_constraints.json`
- v6.0 scope declaration (normative for filtering): `CAXS/INFRASTRUCTURE/v6.0_nomenclature_scope.md`

### 2.3 Gate workflow
- CI PR-blocking workflow: `.github/workflows/ca360_portal_gates.yml`

---

## 3. Definitions (normative)

### 3.1 Portfolio Governance Key (PGK) — fields 1–9
`PGK = (ATA, PROJECT, PROGRAM, FAMILY, VARIANT, VERSION, MODEL, BLOCK, PHASE)`

- PGK is the portfolio slice you are working in.
- Changing PGK is a **portfolio-level governance change** (requires decision + re-homing).

### 3.2 Artifact Governance Key (AGK) — fields 10–17
`AGK = (KNOT, AoR, SUBJECT, CATEGORY, TYPE, ISSUE-REV, STATUS, EXT)`

- AGK is the governed artifact instance within a PGK slice.

### 3.3 "One Official Chain" (normative)
Within a given PGK:

`UniqueKey = (PGK, AoR, SUBJECT, CATEGORY, TYPE)`  
`COUNT(status ∈ {ACTIVE, RELEASED}) ≤ 1`

### 3.4 Category↔AoR constraints (normative)
- `CATEGORY ∈ {SIGNOFF, EXPORT_CONTROL}` → `AoR ∈ {STK_CM, STK_CERT}` only (PR-blocking).

---

## 4. Workflow overview (single sequence)

### Step 0 — Select the execution slice
Choose:
- PROGRAM: `AIRT | SPACET`
- FAMILY: `Q100 | Q200LR | Q10 | QHABITAT`
- VARIANT: `GEN | BASELINE | FLIGHT_TEST | CERT | MSN | CUST`
- VERSION: `PLUS | PLUSULTRA`

This selection sets the **portfolio context** for work routing and reporting.

### Step 1 — Select OPT-INS node (Axis + ATA + BLOCK + PHASE)
Choose:
- Axis: `O | P | T | I | N | S`
- ATA: `00..116`
- BLOCK: `00..90`
- PHASE: `LC01..LC14`
- MODEL: choose the governing artifact model (typically `PR` for node governance packs; `SW/HW/BB` for implementation artifacts).

This resolves the **PGK** slice for the node.

### Step 1.5 — Resolve via CIPP if Certainty Exists (NEW)

**Purpose**: Prevent wasted KNOT work when the answer is already known and routable.

Before instantiating/working a node as uncertain, search the CIPP registry for matching certainty routes:

**Search criteria**:
1. Match `pgk_scope` + axis/ATA + `interface_contract`
2. Match `intent_key` (vision/mission/scope/outcome alignment)

**If valid CIPP found**:
- **Execute via CIPP** (deterministic path)
- Verify all `target_refs` are RELEASED or ACTIVE
- Verify all `target_sha256` hashes match actual files
- Record CIPP usage in execution log
- **Skip KNOT instantiation** → proceed to execution using CIPP route

**If no valid CIPP found** (or CIPP is invalid):
- Continue to Step 2 (instantiate ONUP)
- Open/continue KNOT resolution

**CIPP validity checks**:
- `target_ref` paths exist in repository
- `target_sha256` matches actual file hash
- `target_status ∈ {ACTIVE, RELEASED}`
- `intent_key` resolves to valid VISION/MISSION/SCOPE/OUTCOME IDs
- `effectivity` compatible with caller's PGK slice

**References**:
- **CIPP Registry**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-registry_REGISTRY_CAT_I01-R01_ACTIVE.md`
- **CIPP vs KNOT Governance**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-vs-knot-governance_DELIVERABLE_STD_I01-R01_ACTIVE.md`

---

### Step 2 — Instantiate / Load the Node Uncertainty Pack (ONUP)

**Note**: This step is reached only if Step 1.5 did not find a valid CIPP route.

For the selected node, ensure the ONUP SSOT set exists (Domain view SSOT):

**Mandatory ONUP artifacts**
1) Node tasklist index (`REGISTRY/IDX`)  
2) Problem statement + hypotheses (`DELIVERABLE/STD` or `SPEC`)  
3) ATA impact analysis matrix (`REGISTRY/TAB`)  
4) AoR RACI matrix (`REGISTRY/TAB`)  
5) Roadmap registry (`REGISTRY/REG`)  
6) Task registry (`REGISTRY/REG`)  
7) Evidence index (`REGISTRY/IDX`)  
8) Signoff index (`REGISTRY/IDX`)  

If missing: generate from infrastructure templates (template pack under `CAXS/INFRASTRUCTURE/templates/onup_pack/`).

### Step 3 — Extract AoR routing and the required KNOT set
From the node's **AoR RACI**:
- determine `primary_aor` and interface AoRs (review/accept/signoff).
From the axis-specific KNOT semantics:
- derive the **required KNOT queue** for this node.

**Routing rules**
- If impact matrix triggers SAF/CY/CERT constraints, those AoRs become mandatory interfaces.
- If any task requires SIGNOFF/EXPORT_CONTROL, routing must land on STK_CM or STK_CERT.

### Step 4 — Decompose uncertainty into executable tasks (Kxx-T###)
Populate the **Task Registry** with manageable units:

Each task MUST bind:
- **DELIVERABLE output(s)** (REQ/SPEC/PLAN/STD/ICD/PROC/etc.)
- **EVIDENCE output(s)** (RPT/LOG/CASE/etc.)
- **SIGNOFF** artifacts where required (DEC/MIN)

**Minimum task registry fields (normative)**
- `task_id` = `Kxx-T###`
- `owner_aor`
- `acceptance_criteria` (measurable; testable)
- `outputs` (canonical v6.0 filenames, in-scope)
- `required_evidence` (canonical filenames, in-scope)
- `depends_on` (tasks and/or KNOT dependencies)
- `status` (DRAFT/ACTIVE/RELEASED/SUPERSEDED as allowed)

### Step 5 — Execute tasks and produce governed artifacts
For each task:
1) create/update outputs as `STATUS=DRAFT`
2) create required evidence artifacts (logs, reports, cases)
3) update SSOT indexes:
   - task registry (progress + links)
   - evidence index (new evidence)
   - signoff index (if applicable)
4) run local validation (same validator as CI) prior to PR

### Step 6 — Run gates (PR-blocking)
A PR cannot merge if any PR-blocking gate fails:

**Core gates (PR-blocking)**
1) Filename validation (v6.0 + PROJECT=AMPEL360, in-scope)  
2) AoR allowlist validation (14 stakeholders)  
3) Category↔AoR constraints (SIGNOFF/EXPORT_CONTROL restricted)  
4) KNOT range enforcement (K01–K14 only)  
5) One Official Chain uniqueness (DELIVERABLE uniqueness per UniqueKey)  
6) `.gitkeep` presence (directory tracking)  

**Operational gates (PR-blocking where configured)**
- Link integrity for critical SSOT references
- ONUP pack presence for required nodes/AoRs (as configured)

### Step 7 — Close the loop (collapse uncertainty → RELEASED)
A node (and its governed outputs) can be promoted to `STATUS=RELEASED` only when all conditions below hold:

**Closure conditions (normative)**
1) Completeness: all task outputs exist and are linked in SSOT registries  
2) Evidence: all required evidence exists and is referenced  
3) Policy: category↔AoR constraints satisfied  
4) Uniqueness: One Official Chain satisfied (`ACTIVE|RELEASED ≤ 1`)  
5) Link integrity: critical SSOT links resolve  
6) Impact resolution: no unresolved **hard-coupled** blockers in the impact matrix  
7) Signoff present where required (DEC/MIN recorded and linked)
8) **KNOT → CIPP Promotion** (normative): At least one CIPP minted, unless justified exception

**KNOT → CIPP Promotion Rule**:

A KNOT is "collapsed" only when it yields:
- A **released artifact chain** (all outputs moved to ACTIVE or RELEASED status)
- **At least one CIPP** that points to that chain for deterministic reuse

**Promotion steps**:
1. Identify new stable knowledge produced by KNOT resolution
2. Create CIPP entry(ies) in CIPP Registry pointing to:
   - Released artifacts (with sha256 hashes)
   - Evidence chains
   - Validated procedures or integration routes
3. Verify CIPP determinism (all targets exist, hashes match, intent validates)
4. Record KNOT → CIPP promotion in change log

**Exception**: A KNOT may close without minting a CIPP if justified (e.g., one-time exploration, negative result, no reusable route). Justification must be documented in closure notes.

**References**:
- **CIPP vs KNOT Governance**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-vs-knot-governance_DELIVERABLE_STD_I01-R01_ACTIVE.md`
- **CIPP Registry**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-registry_REGISTRY_CAT_I01-R01_ACTIVE.md`

---

### Step 8 — Generate Release Evidence Pack (when releasing a node/baseline)
When outputs move to RELEASED, generate a compliance-ready evidence bundle (per template):
- validation report (filled)
- gate run IDs and timestamps
- contract manifest (SHA256 for contract files)
- one-official-chain audit result (0 collisions)
- exceptions snapshot (non-expired / empty)
- delta summary vs previous release

### Step 9 — Feedback and evolution (K14 loop)
Open improvement tasks when:
- audit findings exist,
- anomalies/NCRs arise,
- drift triggers recert (N axis),
- new technology patterns require governance adaptation.

Record findings and decisions as governed artifacts; supersede impacted outputs per CM policy.

---

## 5. Decision points and routing rules (quick reference)

### 5.1 When is SIGNOFF mandatory?
SIGNOFF is mandatory when:
- compliance acceptability is asserted (CERT),
- safety/security acceptance is asserted (SAF/CY),
- baseline release/packaging decisions are made (CM),
- export-controlled release is produced (CM/CERT).

**Constraint:** SIGNOFF artifacts must be owned by STK_CM or STK_CERT.

### 5.2 When does a node reopen (REOPENED)?
A node reopens when:
- evidence contradicts a prior DEC,
- impact matrix changes from soft → hard coupling,
- a PGK field changes (portfolio-level re-homing),
- drift thresholds or operational anomalies trigger recert loops.

---

## 6. Minimal "operator checklist" (copy/paste)

**Before starting**
- [ ] Selected PROGRAM/FAMILY/VARIANT/VERSION  
- [ ] Selected Axis/ATA/BLOCK/PHASE  
- [ ] ONUP pack exists (8 SSOT artifacts)  
- [ ] AoR RACI and impact matrix populated (at least baseline rows)

**During execution**
- [ ] Tasks created as Kxx-T### with measurable acceptance criteria  
- [ ] Deliverables produced with canonical filenames (in-scope)  
- [ ] Evidence produced and indexed  
- [ ] Signoff routed correctly (CM/CERT only) when required  
- [ ] Gates run locally before PR

**Before release**
- [ ] One Official Chain collisions = 0  
- [ ] Impact matrix has no unresolved hard blockers  
- [ ] Evidence index complete  
- [ ] Signoff index complete (where required)  
- [ ] Release evidence pack generated and linked

---

## 7. Example instantiation (illustrative)

Selection:
- PROGRAM=SPACET, FAMILY=Q10, VARIANT=BASELINE, VERSION=PLUS
- Axis=T, ATA=21, BLOCK=10, PHASE=LC02, MODEL=PR (node governance pack)

Expected AoR routing (typical):
- Primary: STK_SE
- Interfaces: STK_TEST (V&V), STK_CERT (acceptability), STK_SAF (hazards), STK_CY (security/export), STK_CM (baseline/release)

Execution:
- Create K01/K02/K03/K06/K07/K11 tasks as needed
- Produce DELIVERABLE + EVIDENCE; route SIGNOFF to CM/CERT
- Close node → RELEASED + evidence pack

---

## 8. Change control
Edits to this SSOT procedure are governed as:
- `CATEGORY=DELIVERABLE`, `TYPE=PROC`, via CM change control.
- Any change to PGK field definitions or gates requires decision record and version bump per portal contract rules.
