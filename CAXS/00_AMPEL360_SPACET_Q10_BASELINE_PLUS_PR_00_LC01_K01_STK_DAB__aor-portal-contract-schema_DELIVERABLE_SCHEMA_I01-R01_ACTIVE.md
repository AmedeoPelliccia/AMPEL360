# AoR Portal Contract Schema

**AMPEL360 CA360º — Portal Configuration Contract Schema**

---

## Metadata

- **ATA:** 00 (GENERAL)
- **Program:** SPACET Q10 BASELINE PLUS
- **Phase:** LC01 (Problem Statement / Generation / Prompting Engineering)
- **KNOT:** K01
- **AoR Owner:** STK_DAB (Digital Applications & Blockchains)
- **Category:** DELIVERABLE
- **Type:** SCHEMA
- **Status:** ACTIVE
- **Issue-Revision:** I01-R01

---

## Purpose

This schema defines the structure of an **AoR Portal Contract**, which specifies the configuration and enabled features for a specific AoR portal in the AMPEL360 CA360º ecosystem.

Every AoR portal must have a contract conforming to this schema. The contract is validated at CI time and gates RC/RELEASE transitions.

---

## Schema Version

**Version:** 1.0.0  
**Format:** YAML  
**Encoding:** UTF-8

---

## Schema Definition

```yaml
# AoR Portal Contract Schema v1.0.0

contract_metadata:
  aor_id:
    type: string
    pattern: ^STK_(CM|PMO|SE|DAB|PHM|SAF|CERT|TEST|OPS|MRO|AI|CY|SPACEPORT|CEGT)$
    required: true
    description: "AoR identifier from the canonical STK allowlist"

  contract_version:
    type: string
    pattern: ^\d+\.\d+\.\d+$
    required: true
    description: "Semantic version of this contract"

  program:
    type: string
    enum: [AIRT, SPACET]
    required: true
    description: "Program this contract applies to"

  family:
    type: string
    enum: [Q100, Q200LR, Q10, QHABITAT]
    required: true
    description: "Product family this contract applies to"

  variant:
    type: string
    enum: [GEN, BASELINE, FLIGHT_TEST, CERT, MSN, CUST]
    required: true
    description: "Variant context"

  version:
    type: string
    enum: [PLUS, PLUSULTRA]
    required: true
    description: "Version tier"

  maintained_by:
    type: string
    required: true
    description: "Contact or team responsible for maintaining this contract"

  last_updated:
    type: string
    format: date
    required: true
    description: "ISO 8601 date of last update"

# Default workspace context
default_context:
  filters:
    opt_ins_axes:
      type: array
      items:
        type: string
        enum: [O-OPS, P-PROGRAM, T-TECHNOLOGY, I-INFRASTRUCTURES, N-NEURAL_NETWORKS, S-SIM_TEST]
      description: "Default OPT-INS axes to display"

    ata_chapters:
      type: array
      items:
        type: integer
        minimum: 0
        maximum: 116
      description: "Default ATA chapters in scope"

    lc_phases:
      type: array
      items:
        type: string
        pattern: ^LC(0[1-9]|1[0-4])$
      description: "Default lifecycle phases"

    knots:
      type: array
      items:
        type: string
        pattern: ^K(0[1-9]|1[0-4])$
      description: "Default KNOTs in scope"

    blocks:
      type: array
      items:
        type: string
        pattern: ^(00|10|20|30|40|50|60|70|80|90)$
      description: "Default BLOCKs in scope"

    categories:
      type: array
      items:
        type: string
        enum: [DELIVERABLE, EVIDENCE, REGISTRY, SIGNOFF, EXPORT_CONTROL, INTERNAL_PRODUCTION]
      description: "Default artifact categories"

    types:
      type: array
      items:
        type: string
      description: "Default artifact types (from TYPE allowlist)"

    statuses:
      type: array
      items:
        type: string
        enum: [DRAFT, ACTIVE, RELEASED, SUPERSEDED, OBSOLETE]
      description: "Default statuses to show"

  slice_selector:
    program_family_variants:
      type: array
      items:
        type: object
        properties:
          program:
            type: string
            enum: [AIRT, SPACET]
          family:
            type: string
            enum: [Q100, Q200LR, Q10, QHABITAT]
          variants:
            type: array
            items:
              type: string
              enum: [GEN, BASELINE, FLIGHT_TEST, CERT, MSN, CUST]
      description: "Allowed program/family/variant combinations"

    default_slice:
      type: object
      properties:
        program:
          type: string
        family:
          type: string
        variant:
          type: string
        version:
          type: string
        node:
          type: string
          description: "Default node selector (e.g., ATA chapter or OPT-INS axis)"
      description: "Default slice selection on portal load"

# Feature set (MoSCoW)
features:
  moscow:
    must:
      type: array
      items:
        type: string
        pattern: ^F-\d{2}$
      required: true
      description: "MUST features (non-negotiable), referencing canonical feature IDs"

    should:
      type: array
      items:
        type: string
        pattern: ^F-\d{2}$
      description: "SHOULD features (strongly recommended)"

    could:
      type: array
      items:
        type: string
        pattern: ^F-\d{2}$
      description: "COULD features (valuable but not required)"

    wont:
      type: array
      items:
        type: string
        pattern: ^F-\d{2}$
      description: "WON'T features (explicitly excluded)"

  config:
    type: object
    description: "Per-feature configuration overrides"
    additionalProperties:
      type: object
      properties:
        enabled:
          type: boolean
          description: "Feature enabled flag"
        settings:
          type: object
          description: "Feature-specific settings"

# Tool Launchpad (TALF-aware)
tool_launchpad:
  tiles:
    type: array
    items:
      type: object
      properties:
        tool_id:
          type: string
          required: true
          description: "Unique tool identifier"

        tool_name:
          type: string
          required: true
          description: "Human-readable tool name"

        version:
          type: string
          description: "Tool version or class"

        owner_aor:
          type: string
          pattern: ^STK_(CM|PMO|SE|DAB|PHM|SAF|CERT|TEST|OPS|MRO|AI|CY|SPACEPORT|CEGT)$
          required: true
          description: "AoR responsible for this tool"

        launch:
          type: object
          required: true
          properties:
            channel:
              type: string
              enum: [VDI, HPC_job, container, web, api]
              required: true
              description: "Launch channel"

            deep_link:
              type: string
              format: uri
              description: "Launch URL or command"

        workspace_bindings:
          type: object
          properties:
            repo_nodes:
              type: array
              items:
                type: string
              description: "Repository paths to mount"

            exports:
              type: array
              items:
                type: string
              description: "Export directories"

            datasets:
              type: array
              items:
                type: string
              description: "Dataset identifiers"

            templates:
              type: array
              items:
                type: string
              description: "Template identifiers"

        licensing:
          type: object
          properties:
            model:
              type: string
              enum: [concurrent, named, pool, unlimited, none]
              required: true
              description: "License model"

            pool_id:
              type: string
              description: "License pool identifier (if applicable)"

            checkout_mode:
              type: string
              enum: [automatic, manual, pre_reserved]
              description: "License checkout mode"

            constraints:
              type: object
              description: "License constraints (e.g., max duration)"

        preflight:
          type: object
          properties:
            checks:
              type: array
              items:
                type: string
                enum: [sso_session, entitlement, license, compute_profile, network, storage]
              description: "Preflight checks to run"

            requirements:
              type: object
              description: "Preflight requirements (e.g., minimum compute resources)"

        audit:
          type: object
          properties:
            events:
              type: array
              items:
                type: string
                enum: [launch, checkout, export, close, failure]
              description: "Events to log for audit"

        failure_modes:
          type: object
          properties:
            license_unavailable:
              type: string
              enum: [block, retry, queue, log]
              description: "Action when license is unavailable"

            entitlement_denied:
              type: string
              enum: [block, notify]
              description: "Action when entitlement check fails"

# Execution surfaces
execution:
  kanban:
    type: object
    properties:
      enabled:
        type: boolean
        default: true

      columns:
        type: array
        items:
          type: object
          properties:
            id:
              type: string
              required: true
            label:
              type: string
              required: true
            knot_stages:
              type: array
              items:
                type: string
                pattern: ^K(0[1-9]|1[0-4])$
        description: "Kanban column definitions"

      default_filters:
        type: object
        description: "Default filters for Kanban view"

  task_wizard:
    type: object
    properties:
      enabled:
        type: boolean
        default: true

      templates:
        type: array
        items:
          type: string
        description: "Available task templates"

  evidence_console:
    type: object
    properties:
      enabled:
        type: boolean
        default: true

      default_view:
        type: string
        enum: [index, attach, export, hash]
        default: index

  signoff_console:
    type: object
    properties:
      enabled:
        type: boolean
        default: true

      routing_rules:
        type: array
        items:
          type: object
          properties:
            signoff_type:
              type: string
            target_aor:
              type: string
              pattern: ^STK_(CM|PMO|SE|DAB|PHM|SAF|CERT|TEST|OPS|MRO|AI|CY|SPACEPORT|CEGT)$

# Assistant + communications
assistant:
  enabled:
    type: boolean
    default: false
    description: "Enable AI assistant (F10)"

  capabilities:
    type: array
    items:
      type: string
      enum: [draft_artifacts, propose_tasks, propose_raci, suggest_evidence, identify_gaps]
    description: "Allowed assistant capabilities"

  constraints:
    type: object
    properties:
      cannot_bypass_gates:
        type: boolean
        default: true
      cannot_invent_aors:
        type: boolean
        default: true
      must_cite_sources:
        type: boolean
        default: true
      must_link_ssot:
        type: boolean
        default: true

communications:
  threads:
    enabled:
      type: boolean
      default: false
      description: "Enable integrated communication threads (F11)"

    bindings:
      type: array
      items:
        type: string
        enum: [node, task, signoff, decision]
      description: "Object types that can have threads"

# Backend bindings
backend:
  validators:
    type: array
    items:
      type: string
    description: "Validator service IDs to invoke"

  indexers:
    type: array
    items:
      type: string
    description: "Indexer service IDs"

  trace_services:
    type: array
    items:
      type: string
    description: "Traceability and graph service IDs"

  notification_rules:
    type: array
    items:
      type: object
      properties:
        event:
          type: string
          enum: [gate_failure, signoff_request, license_failure, new_blocker, evidence_gap]
        channels:
          type: array
          items:
            type: string
            enum: [email, portal, webhook, sms]
        recipients:
          type: array
          items:
            type: string
```

---

## Validation Rules

### Required Features

Every AoR portal contract must include all MUST features (F01-F09) from the canonical feature catalog.

**Validation:**
```yaml
must_includes_all_required:
  F01, F02, F03, F04, F05, F06, F07, F08, F09
```

### Feature Consistency

Features listed in `wont` must not appear in `must`, `should`, or `could`.

### Tool Launchpad Completeness

If F09 (Tool Launchpad) is enabled, `tool_launchpad.tiles` must be non-empty.

### Contract-Feature Alignment

All feature IDs referenced must exist in the canonical portal feature catalog.

---

## Example Contract Snippet

```yaml
contract_metadata:
  aor_id: STK_PHM
  contract_version: 1.0.0
  program: SPACET
  family: Q10
  variant: BASELINE
  version: PLUS
  maintained_by: phm-team@ampel360.org
  last_updated: 2025-12-19

features:
  moscow:
    must: [F01, F02, F03, F04, F05, F06, F07, F08, F09]
    should: [F10, F13, F14]
    could: [F15, F17]
    wont: [F19, F20]

tool_launchpad:
  tiles:
    - tool_id: ansys-fluent-2024
      tool_name: "ANSYS Fluent"
      version: "2024.1"
      owner_aor: STK_PHM
      launch:
        channel: VDI
        deep_link: "vdi://ansys-fluent-2024"
      licensing:
        model: concurrent
        pool_id: ansys-pool-01
        checkout_mode: automatic
      preflight:
        checks: [sso_session, entitlement, license, compute_profile]
      audit:
        events: [launch, checkout, close, failure]
      failure_modes:
        license_unavailable: queue
```

---

## CI Validation

Contracts are validated at PR time using a schema validator. The validator checks:

1. Schema conformance (YAML structure)
2. Required feature inclusion (all MUST features)
3. Feature ID validity (all IDs exist in catalog)
4. AoR ID validity (from STK allowlist)
5. Tool launchpad completeness (if F09 enabled)

**Validator location:**  
`src/validators/portal_contract_validator.py` (or equivalent)

---

## References

- **Portal Feature Catalog (SSOT):** `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_DAB__portal-feature-catalog_REGISTRY_CAT_I01-R01_ACTIVE.md`
- **Tool Launchpad Specification:** `00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_DAB__tool-launchpad-specification_DELIVERABLE_SPEC_I01-R01_ACTIVE.md`
- **v6.0 Nomenclature:** README.md section 10

---

## Change Log

| Revision | Date | Author | Changes |
|----------|------|--------|---------|
| I01-R01 | 2025-12-19 | STK_DAB | Initial schema definition |

---

**END OF DOCUMENT**
