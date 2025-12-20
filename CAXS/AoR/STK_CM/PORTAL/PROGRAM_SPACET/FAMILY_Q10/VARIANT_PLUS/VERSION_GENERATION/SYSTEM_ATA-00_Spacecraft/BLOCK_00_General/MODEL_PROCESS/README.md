# INDEX — STK_CM / SPACET / Q10 / PLUS / GENERATION — ATA-00 / Block 00 (General) — MODEL_PROCESS

**Path:** `.../SYSTEM_ATA-00_Spacecraft/BLOCK_00_General/MODEL_PROCESS/`  
**Owner (AoR):** STK_CM  
**Knots in scope:** K01, K04, K06, K10

---

## Navigation

- [Entry / Overview](#entry--overview)
- [K01 — Standards](#k01--standards)
- [K04 — Change-control gate](#k04--change-control-gate)
- [K06 — Baseline release gate](#k06--baseline-release-gate)
- [K10 — Audit gate](#k10--audit-gate)

---

## Entry / Overview

- **Block 00 General — Entry**
  - [Block00_General_Entry — OVERVIEW](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K00_STK_CM__Block00_General_Entry_DELIVERABLE_OVERVIEW_I01-R01_ACTIVE.md)

---

## K01 — Standards

**Purpose:** Define nomenclature, policies, templates  
**Output:** Standard release + enforcement rules  
**Gates:** nomenclature validation, schema validation

### Core documents
- [Standards_Pack — SPEC](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Standards_Pack_DELIVERABLE_SPEC_I01-R01_ACTIVE.md)
- [Nomenclature_Standard — STANDARD](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Nomenclature_Standard_DELIVERABLE_STANDARD_I01-R01_ACTIVE.md)
- [Templates_Index — INDEX](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Templates_Index_DELIVERABLE_INDEX_I01-R01_ACTIVE.md)

### Registries / vocabularies / enforcement
- [Schema_Registry — REGISTER (CSV)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Schema_Registry_REGISTRY_REGISTER_I01-R01_ACTIVE.csv)
- [Schema_Registry — SCHEMA (JSON)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Schema_Registry_REGISTRY_SCHEMA_I01-R01_ACTIVE.json)
- [Controlled_Vocabularies — VOCAB (CSV)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Controlled_Vocabularies_REGISTRY_VOCAB_I01-R01_ACTIVE.csv)
- [Enforcement_Rules — RULESET (YAML)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Enforcement_Rules_DELIVERABLE_RULESET_I01-R01_ACTIVE.yaml)

---

## K04 — Change-control gate

**Purpose:** Approve changes for integration  
**Output:** CR “Approved for integration”  
**Gates:** impact analysis complete, approval obtained, cross-ATA clearance

### Procedure + registers
- [Change_Control_Procedure — POLICY](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K04_STK_CM__Change_Control_Procedure_DELIVERABLE_POLICY_I01-R01_ACTIVE.md)
- [CR_Register — REGISTER (CSV)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K04_STK_CM__CR_Register_REGISTRY_REGISTER_I01-R01_ACTIVE.csv)
- [CR_Register — SCHEMA (JSON)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K04_STK_CM__CR_Register_REGISTRY_SCHEMA_I01-R01_ACTIVE.json)

### Templates / clearance artifacts
- [Impact_Analysis_Template — TEMPLATE](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K04_STK_CM__Impact_Analysis_Template_DELIVERABLE_TEMPLATE_I01-R01_ACTIVE.md)
- [Approval_Matrix — MATRIX (CSV)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K04_STK_CM__Approval_Matrix_REGISTRY_MATRIX_I01-R01_ACTIVE.csv)
- [Cross_ATA_Clearance_Checklist — CHECKLIST](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K04_STK_CM__Cross_ATA_Clearance_Checklist_DELIVERABLE_CHECKLIST_I01-R01_ACTIVE.md)

---

## K06 — Baseline release gate

**Purpose:** Validate and freeze release candidate  
**Output:** BRP “Releaseable”  
**Gates:** nomenclature compliance, uniqueness check, baseline integrity, CI validation pass

### Procedure + templates
- [Baseline_Release_Procedure — POLICY](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K06_STK_CM__Baseline_Release_Procedure_DELIVERABLE_POLICY_I01-R01_ACTIVE.md)
- [BRP_Template — TEMPLATE](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K06_STK_CM__BRP_Template_DELIVERABLE_TEMPLATE_I01-R01_ACTIVE.md)

### Integrity rules / profiles
- [Baseline_Manifest — SCHEMA (JSON)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K06_STK_CM__Baseline_Manifest_REGISTRY_SCHEMA_I01-R01_ACTIVE.json)
- [Uniqueness_Check_Rules — RULESET (JSON)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K06_STK_CM__Uniqueness_Check_Rules_DELIVERABLE_RULESET_I01-R01_ACTIVE.json)
- [CI_Validation_Profile — CONFIG (YAML)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K06_STK_CM__CI_Validation_Profile_DELIVERABLE_CONFIG_I01-R01_ACTIVE.yaml)

---

## K10 — Audit gate

**Purpose:** Prepare audit-ready baseline  
**Output:** “Audit-ready baseline” + export  
**Gates:** traceability complete, evidence closure, signoff obtained, CERT clearance

### Procedure + templates
- [Audit_Pack_Procedure — POLICY](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K10_STK_CM__Audit_Pack_Procedure_DELIVERABLE_POLICY_I01-R01_ACTIVE.md)
- [Traceability_Matrix_Template — TEMPLATE (CSV)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K10_STK_CM__Traceability_Matrix_Template_DELIVERABLE_TEMPLATE_I01-R01_ACTIVE.csv)
- [CERT_Clearance_Statement — TEMPLATE](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K10_STK_CM__CERT_Clearance_Statement_DELIVERABLE_TEMPLATE_I01-R01_ACTIVE.md)
- [Audit_Export_Bundle_Checklist — CHECKLIST](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K10_STK_CM__Audit_Export_Bundle_Checklist_DELIVERABLE_CHECKLIST_I01-R01_ACTIVE.md)

### Evidence / signoffs
- [Evidence_Index — SCHEMA (JSON)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K10_STK_CM__Evidence_Index_REGISTRY_SCHEMA_I01-R01_ACTIVE.json)
- [Signoff_Register — REGISTER (CSV)](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K10_STK_CM__Signoff_Register_REGISTRY_REGISTER_I01-R01_ACTIVE.csv)

---

## Notes
- If you normalize `[MODEL]=PROCESS` (recommended for consistency with `MODEL_PROCESS/`), you can mass-rename filenames from `..._PR_...` to `..._PROCESS_...` and then update the links in this index via the same search/replace.
