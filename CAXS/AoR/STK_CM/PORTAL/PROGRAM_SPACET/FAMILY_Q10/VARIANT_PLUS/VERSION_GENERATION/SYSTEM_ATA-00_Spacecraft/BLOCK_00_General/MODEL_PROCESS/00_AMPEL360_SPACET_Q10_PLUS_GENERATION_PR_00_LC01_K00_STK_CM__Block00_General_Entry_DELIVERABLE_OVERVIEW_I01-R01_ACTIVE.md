# ATA-00 / Block 00 (General) — STK_CM Portal Entry (MODEL_PROCESS)

**Program:** SPACET  
**Family:** Q10  
**Variant:** PLUS  
**Version stream:** GENERATION  
**System:** ATA-00 — Spacecraft  
**Block:** 00 — General  
**AoR (Owner):** STK_CM  
**Lifecycle phase:** LC01  
**Knot:** K00 (Portal Entry)  
**Issue-Rev:** I01-R01  
**Status:** ACTIVE

---

## 1. Purpose

This document is the **entry point** for **Configuration Management (STK_CM)** governance under:

`SPACET / Q10 / PLUS / GENERATION → ATA-00 → Block 00 (General)`

It defines the **operating pathway** and provides direct navigation to the four governance knots:

- **K01 — Standards** (nomenclature, policies, templates, enforcement rules)
- **K04 — Change Control Gate** (approve changes for integration)
- **K06 — Baseline Release Gate** (validate and freeze release candidates)
- **K10 — Audit Gate** (prepare audit-ready baseline + export with CERT clearance)

This entry does **not** replace ATA engineering portals; it governs **program-level baseline control** and
audit-grade traceability.

---

## 2. What is governed here (Scope)

### In scope
- **Program baseline governance**: naming, CM rules, release discipline, registers, audits
- **Cross-ATA coherence**: impact visibility and clearance tracking for integrated changes
- **Gate evidence**: machine-readable reports + human-readable summaries for each gate
- **Exports**:
  - **BRP “Releaseable”** (K06)
  - **Audit-ready baseline + export bundle** (K10)

### Out of scope
- Primary engineering authoring inside ATA chapters (owned by relevant AoR portals)
- Tool ownership outside controlled linking (tools are referenced, not duplicated)

---

## 3. Operating model (Knots)

### K01 — Standards
**Purpose:** Define nomenclature, policies, templates  
**Output:** Standard release + enforcement rules  
**Gates:** nomenclature validation, schema validation

**Navigate:**
- [Standards_Pack](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Standards_Pack_DELIVERABLE_SPEC_I01-R01_ACTIVE.md)
- [Nomenclature_Standard](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Nomenclature_Standard_DELIVERABLE_STANDARD_I01-R01_ACTIVE.md)
- [Schema_Registry (CSV)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Schema_Registry_REGISTRY_REGISTER_I01-R01_ACTIVE.csv)
- [Templates_Index](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Templates_Index_DELIVERABLE_INDEX_I01-R01_ACTIVE.md)
- [Controlled_Vocabularies (CSV)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Controlled_Vocabularies_REGISTRY_VOCAB_I01-R01_ACTIVE.csv)
- [Enforcement_Rules (YAML)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Enforcement_Rules_DELIVERABLE_RULESET_I01-R01_ACTIVE.yaml)

---

### K04 — Change Control Gate
**Purpose:** Approve changes for integration  
**Output:** CR “Approved for integration”  
**Gates:** impact analysis complete, approval obtained, cross-ATA clearance

**Navigate:**
- [Change_Control_Procedure](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K04_STK_CM__Change_Control_Procedure_DELIVERABLE_POLICY_I01-R01_ACTIVE.md)
- [CR_Register (CSV)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K04_STK_CM__CR_Register_REGISTRY_REGISTER_I01-R01_ACTIVE.csv)
- [Impact_Analysis_Template](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K04_STK_CM__Impact_Analysis_Template_DELIVERABLE_TEMPLATE_I01-R01_ACTIVE.md)
- [Approval_Matrix (CSV)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K04_STK_CM__Approval_Matrix_REGISTRY_MATRIX_I01-R01_ACTIVE.csv)
- [Cross_ATA_Clearance_Checklist](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K04_STK_CM__Cross_ATA_Clearance_Checklist_DELIVERABLE_CHECKLIST_I01-R01_ACTIVE.md)

---

### K06 — Baseline Release Gate
**Purpose:** Validate and freeze release candidate  
**Output:** BRP “Releaseable”  
**Gates:** nomenclature compliance, uniqueness check, baseline integrity, CI validation pass

**Navigate:**
- [Baseline_Release_Procedure](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K06_STK_CM__Baseline_Release_Procedure_DELIVERABLE_POLICY_I01-R01_ACTIVE.md)
- [BRP_Template](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K06_STK_CM__BRP_Template_DELIVERABLE_TEMPLATE_I01-R01_ACTIVE.md)
- [Baseline_Manifest (JSON Schema)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K06_STK_CM__Baseline_Manifest_REGISTRY_SCHEMA_I01-R01_ACTIVE.json)
- [Uniqueness_Check_Rules (JSON)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K06_STK_CM__Uniqueness_Check_Rules_DELIVERABLE_RULESET_I01-R01_ACTIVE.json)
- [CI_Validation_Profile (YAML)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K06_STK_CM__CI_Validation_Profile_DELIVERABLE_CONFIG_I01-R01_ACTIVE.yaml)

---

### K10 — Audit Gate
**Purpose:** Prepare audit-ready baseline  
**Output:** “Audit-ready baseline” + export  
**Gates:** traceability complete, evidence closure, signoff obtained, CERT clearance

**Navigate:**
- [Audit_Pack_Procedure](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K10_STK_CM__Audit_Pack_Procedure_DELIVERABLE_POLICY_I01-R01_ACTIVE.md)
- [Traceability_Matrix_Template (CSV)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K10_STK_CM__Traceability_Matrix_Template_DELIVERABLE_TEMPLATE_I01-R01_ACTIVE.csv)
- [Evidence_Index (JSON Schema)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K10_STK_CM__Evidence_Index_REGISTRY_SCHEMA_I01-R01_ACTIVE.json)
- [Signoff_Register (CSV)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K10_STK_CM__Signoff_Register_REGISTRY_REGISTER_I01-R01_ACTIVE.csv)
- [CERT_Clearance_Statement](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K10_STK_CM__CERT_Clearance_Statement_DELIVERABLE_TEMPLATE_I01-R01_ACTIVE.md)
- [Audit_Export_Bundle_Checklist](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K10_STK_CM__Audit_Export_Bundle_Checklist_DELIVERABLE_CHECKLIST_I01-R01_ACTIVE.md)

---

## 4. Cross-AoR dependencies (only)

This portal coordinates only with:
- **STK_PMO** — planning, milestones, reporting alignment
- **STK_SE** — cross-ATA interface coherence (ICDs), architecture and requirements consistency
- **STK_SAF** — safety/security impact screening (as triggered by CR impact classification)
- **STK_CERT** — evidence expectations, clearance statements, audit packaging
- **STK_DATA** — schema governance, register integrity, traceability data quality

---

## 5. Controls (minimum)

1. **PR-only** updates to governance artifacts and registers in this block.
2. No change integrates without **K04** output: CR “Approved for integration”.
3. No baseline is **Releaseable** without passing all **K06** gates and recording a freeze reference.
4. No baseline is **Audit-ready** without passing all **K10** gates and receiving **CERT clearance**.
5. Schema/register changes require **STK_DATA review**; audit packaging changes require **STK_CERT review**.

---

## 6. Quick index (file list)

If you maintain a folder-level index file, link it here:
- `00_INDEX.md` (recommended) — curated list of all artifacts in this folder.

