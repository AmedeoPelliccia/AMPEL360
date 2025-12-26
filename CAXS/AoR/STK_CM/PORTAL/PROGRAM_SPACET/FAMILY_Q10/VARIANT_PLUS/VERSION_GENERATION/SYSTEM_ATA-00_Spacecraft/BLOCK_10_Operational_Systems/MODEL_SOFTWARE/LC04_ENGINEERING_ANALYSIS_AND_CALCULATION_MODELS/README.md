# LC04 — Engineering Analysis & Calculation Models (MODEL=SW)

**Path (Portal Context):**  
`CAXS/AoR/STK_CM/PORTAL/PROGRAM_SPACET/FAMILY_Q10/VARIANT_PLUS/VERSION_GENERATION/SYSTEM_ATA-00_Spacecraft/BLOCK_10_Operational_Systems/MODEL_SOFTWARE/LC04_ENGINEERING_ANALYSIS_AND_CALCULATION_MODELS/`

**Owner (AoR):** STK_CM  
**Status:** Active (Portal Baseline)  
**Scope:** Configuration-controlled analysis tooling, calculation models, trade studies, and evidence-ready outputs (metadata-first).

---

## 1. Purpose

This directory contains **LC04 software artifacts and analysis assets** used to execute, validate, and package
engineering analysis and calculation models for Space-T (ATA-00 / Block 10) under CM governance.

LC04 outputs are expected to be:
- **traceable** (Req ↔ Design ↔ Analysis ↔ Evidence ↔ KNOT),
- **reproducible** (inputs + tool versions + run manifest),
- **auditable** (hashes, metadata schema conformance),
- **indexable** (every artifact registered in `INDEX.yaml`).

---

## 2. Naming Convention (LC04 compact scheme)

LC04 uses a compact naming scheme for analysis artifacts:

`{PROGRAM}_{FAMILY}_{VARIANT}_{VERSION}_{SYSTEM}_{BLOCK}_{MODEL}_{LC}_{ARTIFACT_TYPE}_{ARTIFACT_ID}_{VTAG}.{EXT}`

Where:
- `PROGRAM` = `SPACET`
- `FAMILY`  = `Q10`
- `VARIANT` = `PLUS`
- `VERSION` = `GEN` (alias of portal folder `VERSION_GENERATION`)
- `SYSTEM`  = `ATA00` (derived from `SYSTEM_ATA-00_Spacecraft`)
- `BLOCK`   = `B10` (derived from `BLOCK_10_Operational_Systems`)
- `MODEL`   = `SW`
- `LC`      = `LC04`
- `ARTIFACT_TYPE` = controlled list (see Section 3)
- `ARTIFACT_ID` = unique short ID (example: `MEM001`, `TS002`, `MET003`)
- `VTAG` = semantic version tag (example: `v1.0`)
- `EXT` = allowed extension per artifact type

**Example:**  
`SPACET_Q10_PLUS_GEN_ATA00_B10_SW_LC04_TRADE_TS002_v1.0.md`

---

## 3. Subfolders (lanes)

### 3.1 `_templates/`
Reusable templates for new LC04 artifacts:
- `00_AMPEL360_SPACET_Q10_GEN_PLUS_SW_10_LC04_K04_STK_CM__sizing-model-template_INTERNAL_PRODUCTION_SPEC_I01-R01_ACTIVE.csv`
- `00_AMPEL360_SPACET_Q10_GEN_PLUS_SW_10_LC04_K04_STK_CM__timing-analysis-template_INTERNAL_PRODUCTION_SPEC_I01-R01_ACTIVE.md`
- `00_AMPEL360_SPACET_Q10_GEN_PLUS_SW_10_LC04_K04_STK_CM__trade-study-template_INTERNAL_PRODUCTION_SPEC_I01-R01_ACTIVE.md`
- `calculation_sheet_template.py`

### 3.2 `_schemas/`
Schema(s) for LC04 metadata validation:
- `00_AMPEL360_SPACET_Q10_GEN_PLUS_SW_10_LC04_K04_STK_CM__analysis-model-metadata_REGISTRY_SCHEMA_I01-R01_ACTIVE.json`

### 3.3 `sizing_models/`
Sizing models, parametric envelopes, budget spreadsheets, sizing scripts.  
Recommended `ARTIFACT_TYPE`: `SIZING`

### 3.4 `timing_analysis/`
Timing / latency / scheduling analyses (SW timing budgets, worst-case envelopes).  
Recommended `ARTIFACT_TYPE`: `TIMING`

### 3.5 `complexity_metrics/`
Complexity and maintainability metrics, static metrics outputs (normalized).  
Recommended `ARTIFACT_TYPE`: `CMET`

### 3.6 `static_analysis_configs/`
Static analysis configurations (linters, analyzers, rule sets, baselines).  
Recommended `ARTIFACT_TYPE`: `SACFG`

### 3.7 `trade_studies/`
Trade studies, decision matrices, sensitivity analyses.  
Recommended `ARTIFACT_TYPE`: `TRADE`

### 3.8 `performance_models/`
Performance models (execution time, throughput, resource models, param sweeps).  
Recommended `ARTIFACT_TYPE`: `PERF`

### 3.9 `safety_analysis_sw/`
Safety-related software analyses for LC04 scope (hazard-linked computational evidence, constraints checking, safety margins).  
Recommended `ARTIFACT_TYPE`: `SAFETY`

---

## 4. Mandatory registration: `INDEX.yaml`

All new LC04 artifacts **MUST** be registered in `INDEX.yaml` with:
- filename + relative path
- artifact type + ID + version tag
- owner AoR and (if applicable) required signoff routing
- inputs/outputs + trace hooks (requirements, design refs, knot binding)

CI may enforce "no unindexed LC04 artifacts".

---

## 5. Access policy: `TALF_ACCESS.yaml`

`TALF_ACCESS.yaml` defines who can:
- create/update LC04 artifacts
- modify schemas/templates
- run exporters / evidence packagers (if configured)

STK_CM remains the controlling authority for baseline-impacting changes.

---

## 6. Quality gates (expected)

Minimum LC04 gates (recommended):
- **Gate0**: naming + path↔filename scope consistency
- **Gate1**: metadata schema conformance (where metadata applies)
- **Gate2**: index coverage (every artifact listed in `INDEX.yaml`)
- **Gate3**: packaging readiness (manifest + hashes) for export

---

## 7. Ownership
**AoR (owners): STK_PHM, STK_SE, STK_DAB**

## 8. References
- Main README: `MODEL_SOFTWARE/README.md` for directory structure definition
- Lifecycle phases (LC00–LC14) definition in main AMPEL360 README
- Nomenclature Standard v6.0 and controlled vocabulary section
- ATA 93 Traceability Graph specification
- ATA 99 Master Registers for SSOT schemas and vocabularies
