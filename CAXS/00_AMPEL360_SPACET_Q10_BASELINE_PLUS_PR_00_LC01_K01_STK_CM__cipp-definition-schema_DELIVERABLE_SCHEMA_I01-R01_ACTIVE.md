---
document_id: "00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-definition-schema_DELIVERABLE_SCHEMA_I01-R01_ACTIVE"
title: "CIPP Definition Schema — Programmable Objects"
project: "AMPEL360"
scope: "Schema for defining CIPPs as programmable, executable objects"
owner_aor: "STK_CM"
interfaces:
  required: ["STK_DAB","STK_SE"]
category: "DELIVERABLE"
type: "SCHEMA"
status: "ACTIVE"
issue_rev: "I01-R01"
---

# CIPP Definition Schema — Programmable Objects

## 1. Purpose

This schema defines the structure for **CIPP Definition Files** that transform CIPPs from registry entries into **programmable, executable objects** with deterministic behavior.

A CIPP Definition File allows CIPPs to be:
- **Executed** by automation tools
- **Validated** programmatically
- **Versioned** and tracked like code
- **Tested** for deterministic behavior

---

## 2. CIPP Definition File Format

### 2.1 File Naming Convention

CIPP definition files follow v6.0 nomenclature with `CATEGORY=DELIVERABLE` and `TYPE=SPEC`:

```
[ATA]_AMPEL360_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT]_[AoR]__cipp-[CIPP_ID]-definition_DELIVERABLE_SPEC_I##-R##_[STATUS].yaml
```

**Example**:
```
85_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_80_LC09_K09_STK_CEGT__cipp-001-definition_DELIVERABLE_SPEC_I01-R01_ACTIVE.yaml
```

### 2.2 YAML Structure (Normative)

```yaml
---
# CIPP Metadata (required)
cipp_id: CIPP-###
cipp_kind: POINTER | PATH | ROUTE | BINDING | EXPORT | DEPLOY
name: "Human-readable CIPP name"
description: "Clear description of what this CIPP does"
version: "I##-R##"
status: DRAFT | ACTIVE | RELEASED | OBSOLETE

# Intent Alignment (required)
intent:
  vision_id: VSN-###
  mission_id: MSN-###
  scope_id: SCP-*
  pathway_ids: [P01, P02, ...]
  outcome_ids: [OUT-###-###, ...]
  intent_hash: sha256:...

# PGK Scope (required)
pgk_scope: PROGRAM/FAMILY/VARIANT/VERSION/* (or explicit PGK)
aor_owner: STK_*

# Inputs (required for execution)
inputs:
  - name: input_1_name
    type: artifact | parameter | environment
    description: "What this input is"
    schema_ref: "path/to/schema.json" (if applicable)
    required: true | false
    default: "default_value" (if not required)

# Execution Steps (required)
steps:
  - step_id: "S1"
    description: "Describe what this step does"
    action: validate | transform | query | export | invoke
    target: "path/to/artifact.md or tool_name"
    parameters:
      param1: value1
      param2: value2
    validation:
      - check: sha256_match
        expected: sha256:...
      - check: status_constraint
        allowed: [ACTIVE, RELEASED]
    on_failure: halt | warn | skip

# Outputs (required)
outputs:
  - name: output_1_name
    type: artifact | data | report
    description: "What this output is"
    path: "relative/path/to/output"
    schema_ref: "path/to/schema.json" (if applicable)

# Target References (required)
target_refs:
  - path: relative/path/to/artifact.md
    sha256: <hash>
    status: ACTIVE | RELEASED
    role: source | dependency | template

# Validation Evidence (required)
validation_evidence_ref: path/to/evidence

# Downstream Outcomes (required)
downstream_outcomes:
  - outcome_id: OUT-###-###
    metric: "Metric description"
    target: "Target value"
    evidence_hook: "path/to/evidence"

# Constraints (optional)
constraints:
  export_control: true | false
  signoff_required: true | false
  signoff_aor: STK_CM | STK_CERT
  effectivity: "PGK slice or condition"
  version_constraints: ">=I02-R01 or semver"

# Dependencies (optional)
dependencies:
  - cipp_id: CIPP-###
    relation: requires | extends | supersedes
  - artifact_path: path/to/artifact
    relation: depends_on

# Metadata (optional)
metadata:
  created_by: K## or artifact_id
  created_date: YYYY-MM-DD
  last_validated: YYYY-MM-DD
  next_review_date: YYYY-MM-DD
  notes: "Additional context"
```

---

## 3. CIPP Kind-Specific Schemas

### 3.1 POINTER (Single Artifact Reference)

```yaml
cipp_kind: POINTER
steps:
  - step_id: S1
    action: validate
    target: "path/to/artifact.md"
    validation:
      - check: sha256_match
        expected: sha256:...
      - check: status_constraint
        allowed: [RELEASED]
outputs:
  - name: validated_reference
    type: artifact
    path: "path/to/artifact.md"
```

**Use case**: Point to a baseline schema, ICD, or standard with deterministic hash validation.

### 3.2 PATH (Multi-Step Sequence)

```yaml
cipp_kind: PATH
steps:
  - step_id: S1
    action: validate
    target: "path/to/requirement.md"
    validation:
      - check: sha256_match
      - check: status_constraint
  
  - step_id: S2
    action: query
    target: "path/to/trace_graph.md"
    parameters:
      query_type: trace_to_design
      requirement_id: REQ-001
  
  - step_id: S3
    action: validate
    target: "path/to/design.md"
    validation:
      - check: trace_complete
      - check: sha256_match
outputs:
  - name: trace_chain
    type: report
    path: "outputs/trace_report.json"
```

**Use case**: Certification evidence path, traceability chain validation.

### 3.3 ROUTE (Integration Pathway with Branching)

```yaml
cipp_kind: ROUTE
inputs:
  - name: source_data
    type: artifact
    description: "Input data to route"
    required: true

steps:
  - step_id: S1
    action: validate
    target: "${inputs.source_data}"
    validation:
      - check: schema_compliance
        schema_ref: "schemas/data_schema.json"
  
  - step_id: S2
    action: transform
    target: tool:data_transformer
    parameters:
      output_format: json
      mapping_rules: "path/to/mapping.yaml"
  
  - step_id: S3
    action: export
    target: "path/to/registry.md"
    parameters:
      merge_strategy: append
      validation: post_export
      
outputs:
  - name: exported_data
    type: data
    path: "path/to/registry.md"
    schema_ref: "schemas/registry_schema.json"
```

**Use case**: Data export route, KPI calculation and registry update.

### 3.4 BINDING (Interface Contract Enforcement)

```yaml
cipp_kind: BINDING
inputs:
  - name: component_a
    type: artifact
    description: "First component in interface"
    required: true
  - name: component_b
    type: artifact
    description: "Second component in interface"
    required: true

steps:
  - step_id: S1
    action: validate
    target: "path/to/icd.md"
    validation:
      - check: sha256_match
      - check: status_constraint
        allowed: [RELEASED]
  
  - step_id: S2
    action: invoke
    target: tool:interface_checker
    parameters:
      icd_ref: "path/to/icd.md"
      component_a: "${inputs.component_a}"
      component_b: "${inputs.component_b}"
      validation_level: strict
    on_failure: halt

outputs:
  - name: binding_validation_report
    type: report
    path: "outputs/binding_report.json"
```

**Use case**: API binding validation, ICD compliance enforcement.

### 3.5 EXPORT (Deterministic Export/Transformation)

```yaml
cipp_kind: EXPORT
inputs:
  - name: source_artifacts
    type: artifact
    description: "Artifacts to export"
    required: true

steps:
  - step_id: S1
    action: validate
    target: "${inputs.source_artifacts}"
    validation:
      - check: completeness
      - check: status_constraint
        allowed: [ACTIVE, RELEASED]
  
  - step_id: S2
    action: transform
    target: tool:sbom_generator
    parameters:
      format: SPDX
      include_dependencies: true
      output_path: "outputs/sbom.json"
  
  - step_id: S3
    action: validate
    target: "outputs/sbom.json"
    validation:
      - check: schema_compliance
        schema_ref: "schemas/spdx_schema.json"

outputs:
  - name: sbom_export
    type: data
    path: "outputs/sbom.json"
    schema_ref: "schemas/spdx_schema.json"
```

**Use case**: SBOM/BOM export, DPP manifest generation.

### 3.6 DEPLOY (Deployment/Release Package)

```yaml
cipp_kind: DEPLOY
inputs:
  - name: release_artifacts
    type: artifact
    description: "Artifacts to include in release"
    required: true
  - name: target_environment
    type: environment
    description: "Deployment target"
    required: true

steps:
  - step_id: S1
    action: validate
    target: "${inputs.release_artifacts}"
    validation:
      - check: all_released
      - check: signatures_valid
      - check: dependencies_resolved
  
  - step_id: S2
    action: invoke
    target: tool:manifest_generator
    parameters:
      artifacts: "${inputs.release_artifacts}"
      include_hashes: true
      include_signatures: true
      output_path: "outputs/release_manifest.json"
  
  - step_id: S3
    action: export
    target: "${inputs.target_environment}"
    parameters:
      manifest: "outputs/release_manifest.json"
      verify_before_deploy: true

outputs:
  - name: deployment_manifest
    type: data
    path: "outputs/release_manifest.json"
  - name: deployment_log
    type: report
    path: "outputs/deployment_log.txt"
```

**Use case**: Release pack creation, deployment manifest.

---

## 4. Action Types (Normative)

| Action | Purpose | Required Parameters | Outputs |
|--------|---------|---------------------|---------|
| `validate` | Verify artifact integrity and constraints | `target`, `validation[]` | Boolean pass/fail, validation report |
| `transform` | Convert/process data deterministically | `target`, `parameters` | Transformed data/artifact |
| `query` | Extract information from artifact or registry | `target`, `query_type`, `parameters` | Query results (data or report) |
| `export` | Write data to external target | `target`, `parameters` | Export confirmation, updated artifact |
| `invoke` | Execute external tool or script | `target`, `parameters` | Tool output (varies by tool) |

---

## 5. Validation Check Types (Normative)

| Check | Purpose | Parameters |
|-------|---------|------------|
| `sha256_match` | Verify file hash matches expected value | `expected: sha256:...` |
| `status_constraint` | Verify artifact status is allowed | `allowed: [ACTIVE, RELEASED]` |
| `schema_compliance` | Verify data conforms to schema | `schema_ref: path/to/schema.json` |
| `trace_complete` | Verify traceability links are complete | `trace_type: requirement_to_design` |
| `completeness` | Verify all required fields/artifacts present | (implicit based on context) |
| `all_released` | Verify all artifacts have status=RELEASED | (no parameters) |
| `signatures_valid` | Verify digital signatures are valid | (implicit, checks all signatures) |
| `dependencies_resolved` | Verify all dependencies exist and are valid | (implicit, checks dependency graph) |

---

## 6. Execution Model

### 6.1 CIPP Executor (Conceptual)

A CIPP Executor is a tool that:
1. Parses CIPP Definition YAML
2. Validates `intent_key` against SSOT registries
3. Resolves `inputs` and `target_refs`
4. Executes `steps` in sequence
5. Validates each step's output
6. Produces final `outputs`
7. Records execution log as evidence

### 6.2 Execution Context

```yaml
context:
  cipp_id: CIPP-###
  execution_id: exec-YYYYMMDD-HHMMSS-UUID
  executor_version: "1.0.0"
  repository_root: /path/to/repository
  environment:
    pgk_scope: SPACET/Q10/BASELINE/PLUS/*
    aor: STK_CEGT
    timestamp: YYYY-MM-DDTHH:MM:SSZ
```

### 6.3 Execution Log Schema

```yaml
execution_log:
  cipp_id: CIPP-###
  execution_id: exec-YYYYMMDD-HHMMSS-UUID
  status: SUCCESS | FAILURE | PARTIAL
  started_at: YYYY-MM-DDTHH:MM:SSZ
  completed_at: YYYY-MM-DDTHH:MM:SSZ
  steps:
    - step_id: S1
      status: SUCCESS | FAILURE | SKIPPED
      duration_ms: 1234
      validation_results:
        - check: sha256_match
          result: PASS
      errors: []
  outputs:
    - name: output_1_name
      path: path/to/output
      sha256: sha256:...
  errors: []
```

---

## 7. Example: CIPP-001 Definition (DPP Circularity KPI Route)

```yaml
---
cipp_id: CIPP-001
cipp_kind: ROUTE
name: "DPP Circularity KPI Export Route"
description: "Deterministic route for exporting circularity KPI data to DPP manifest"
version: "I01-R01"
status: ACTIVE

intent:
  vision_id: VSN-005
  mission_id: MSN-005
  scope_id: SCP-SPACET-Q10-BASELINE-PLUS
  pathway_ids: [P01, P04]
  outcome_ids: [OUT-005-001]
  intent_hash: sha256:a1b2c3d4e5f6...

pgk_scope: SPACET/Q10/BASELINE/PLUS/*
aor_owner: STK_CEGT

inputs:
  - name: material_data
    type: artifact
    description: "Material composition and recycling data"
    required: true

steps:
  - step_id: S1
    description: "Validate KPI registry structure"
    action: validate
    target: "CAXS/LEDGERS/85_AMPEL360_...__circularity-kpis_REGISTRY_IDX_I01-R01_ACTIVE.md"
    validation:
      - check: sha256_match
        expected: sha256:d4e5f6...
      - check: status_constraint
        allowed: [ACTIVE, RELEASED]
    on_failure: halt

  - step_id: S2
    description: "Validate ESG reporting index"
    action: validate
    target: "CAXS/LEDGERS/85_AMPEL360_...__esg-reporting_REGISTRY_IDX_I01-R01_ACTIVE.md"
    validation:
      - check: sha256_match
        expected: sha256:e5f6g7...
    on_failure: halt

  - step_id: S3
    description: "Calculate Material Circularity Index"
    action: invoke
    target: tool:mci_calculator
    parameters:
      method: ellen_macarthur_foundation
      input_data: "${inputs.material_data}"
      output_format: json
    on_failure: halt

  - step_id: S4
    description: "Validate MCI result against target"
    action: validate
    target: "${outputs.mci_result}"
    validation:
      - check: value_constraint
        field: mci_value
        constraint: ">= 0.85"
    on_failure: warn

  - step_id: S5
    description: "Export to DPP manifest"
    action: export
    target: "CAXS/LEDGERS/94_AMPEL360_...__dpp-manifest_DELIVERABLE_MANIFEST_I01-R01_ACTIVE.md"
    parameters:
      merge_strategy: update
      field_path: "circularity.kpis.material_circularity_index"
      value: "${outputs.mci_result}"
    on_failure: halt

outputs:
  - name: mci_result
    type: data
    path: "outputs/mci_calculation.json"
    schema_ref: "schemas/mci_schema.json"
  - name: export_log
    type: report
    path: "outputs/dpp_export_log.json"

target_refs:
  - path: CAXS/LEDGERS/85_AMPEL360_...__circularity-kpis_REGISTRY_IDX_I01-R01_ACTIVE.md
    sha256: d4e5f6...
    status: ACTIVE
    role: source
  - path: CAXS/LEDGERS/85_AMPEL360_...__esg-reporting_REGISTRY_IDX_I01-R01_ACTIVE.md
    sha256: e5f6g7...
    status: ACTIVE
    role: source
  - path: CAXS/LEDGERS/94_AMPEL360_...__dpp-manifest-schema_DELIVERABLE_SCHEMA_I01-R01_RELEASED.md
    sha256: f6g7h8...
    status: RELEASED
    role: dependency

validation_evidence_ref: CAXS/EVIDENCE/85_...__cipp-001-validation_EVIDENCE_LOG_I01-R01_ACTIVE.md

downstream_outcomes:
  - outcome_id: OUT-005-001
    metric: "Material Circularity Index"
    target: ">= 0.85"
    evidence_hook: "CAXS/EVIDENCE/85_...__circularity-validation_EVIDENCE_TST_I01-R01_ACTIVE.md"

metadata:
  created_by: K09
  created_date: 2025-12-19
  notes: "Initial CIPP for DPP circularity integration"
```

---

## 8. Governance Rules

1. **Creation**: CIPP definitions are created during KNOT collapse or by STK_CM decision
2. **Modification**: Changes to CIPP definitions require version increment (Issue-Rev)
3. **Validation**: All CIPP definitions must pass schema validation before ACTIVE status
4. **Testing**: CIPP definitions should be tested in isolated environment before production use
5. **Deprecation**: CIPP definitions move to OBSOLETE when targets superseded or execution model changes

---

## 9. References

- **CIPP Registry**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-registry_REGISTRY_CAT_I01-R01_ACTIVE.md`
- **CIPP vs KNOT Governance**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__cipp-vs-knot-governance_DELIVERABLE_STD_I01-R01_ACTIVE.md`
- **Intent Alignment Policy**: `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-intent-alignment-policy_DELIVERABLE_STD_I01-R01_ACTIVE.md`

---

**Change History**

| Issue-Rev | Date | Author | Description |
|-----------|------|--------|-------------|
| I01-R01 | 2025-12-19 | STK_CM | Initial CIPP definition schema for programmable objects |
