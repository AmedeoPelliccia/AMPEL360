# INDEX — MODEL_SOFTWARE (STK_CM) — SPACET / Q10 / PLUS / GENERATION — ATA-00 / Block 00 (General)

**Folder:** `.../SYSTEM_ATA-00_Spacecraft/BLOCK_00_General/MODEL_SOFTWARE/`  
**Owner (AoR):** STK_CM  
**Model token:** SW  
**Lifecycle:** LC01  
**Issue-Rev:** I01-R01 — **Status:** ACTIVE

---

## Navigation
- [K01 — Standards validation toolchain](#k01--standards-validation-toolchain)
- [K04 — Change-control automation support](#k04--change-control-automation-support)
- [K06 — Release candidate validation and packaging](#k06--release-candidate-validation-and-packaging)
- [K10 — Audit export assembly](#k10--audit-export-assembly)

---

## K01 — Standards validation toolchain

**Supports gates:** nomenclature validation, schema validation

### Overview
- [Validation_Toolchain_Overview — DELIVERABLE / OVERVIEW](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_SW_00_LC01_K01_STK_CM__Validation_Toolchain_Overview_DELIVERABLE_OVERVIEW_I01-R01_ACTIVE.md)

### Nomenclature validation
- [Nomenclature_Validator — INTERNAL_PRODUCTION / SCRIPT](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_SW_00_LC01_K01_STK_CM__Nomenclature_Validator_INTERNAL_PRODUCTION_SCRIPT_I01-R01_ACTIVE.py)
- [Nomenclature_Validator_Config — INTERNAL_PRODUCTION / CONFIG](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_SW_00_LC01_K01_STK_CM__Nomenclature_Validator_Config_INTERNAL_PRODUCTION_CONFIG_I01-R01_ACTIVE.yaml)

### Schema validation
- [Schema_Validator — INTERNAL_PRODUCTION / SCRIPT](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_SW_00_LC01_K01_STK_CM__Schema_Validator_INTERNAL_PRODUCTION_SCRIPT_I01-R01_ACTIVE.py)
- [Schema_Validator_Config — INTERNAL_PRODUCTION / CONFIG](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_SW_00_LC01_K01_STK_CM__Schema_Validator_Config_INTERNAL_PRODUCTION_CONFIG_I01-R01_ACTIVE.yaml)

### Registry adapters
- [CSV_to_JSON_Adapter — INTERNAL_PRODUCTION / SCRIPT](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_SW_00_LC01_K01_STK_CM__CSV_to_JSON_Adapter_INTERNAL_PRODUCTION_SCRIPT_I01-R01_ACTIVE.py)

---

## K04 — Change-control automation support

**Supports gates:** impact analysis complete (data hygiene), approval obtained (consistency checks)

- [CR_Register_Linter — INTERNAL_PRODUCTION / SCRIPT](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_SW_00_LC01_K04_STK_CM__CR_Register_Linter_INTERNAL_PRODUCTION_SCRIPT_I01-R01_ACTIVE.py)
- [Approval_Matrix_Checker — INTERNAL_PRODUCTION / SCRIPT](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_SW_00_LC01_K04_STK_CM__Approval_Matrix_Checker_INTERNAL_PRODUCTION_SCRIPT_I01-R01_ACTIVE.py)

---

## K06 — Release candidate validation and packaging

**Supports gates:** uniqueness check, baseline integrity, CI validation pass, BRP packaging

### Uniqueness
- [Uniqueness_Checker — INTERNAL_PRODUCTION / SCRIPT](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_SW_00_LC01_K06_STK_CM__Uniqueness_Checker_INTERNAL_PRODUCTION_SCRIPT_I01-R01_ACTIVE.py)

### Baseline integrity
- [Baseline_Integrity_Checker — INTERNAL_PRODUCTION / SCRIPT](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_SW_00_LC01_K06_STK_CM__Baseline_Integrity_Checker_INTERNAL_PRODUCTION_SCRIPT_I01-R01_ACTIVE.py)

### CI profile (what must pass)
- [CI_Validation_Profile — INTERNAL_PRODUCTION / CONFIG](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_SW_00_LC01_K06_STK_CM__CI_Validation_Profile_INTERNAL_PRODUCTION_CONFIG_I01-R01_ACTIVE.yaml)

### BRP packaging
- [BRP_Packager — INTERNAL_PRODUCTION / SCRIPT](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_SW_00_LC01_K06_STK_CM__BRP_Packager_INTERNAL_PRODUCTION_SCRIPT_I01-R01_ACTIVE.py)

---

## K10 — Audit export assembly

**Supports gates:** evidence closure (bundle completeness), signoff + CERT clearance inclusion (profile-driven)

- [Audit_Pack_Assembler — INTERNAL_PRODUCTION / SCRIPT](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_SW_00_LC01_K10_STK_CM__Audit_Pack_Assembler_INTERNAL_PRODUCTION_SCRIPT_I01-R01_ACTIVE.py)
- [Export_Bundle_Profile — INTERNAL_PRODUCTION / CONFIG](./00_AMPEL360_SPACET_Q10_PLUS_GENERATION_SW_00_LC01_K10_STK_CM__Export_Bundle_Profile_INTERNAL_PRODUCTION_CONFIG_I01-R01_ACTIVE.yaml)

