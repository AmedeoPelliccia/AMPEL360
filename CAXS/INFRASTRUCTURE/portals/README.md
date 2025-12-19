# AoR Portal Contracts

## Purpose

This directory contains **AoR Portal Contracts (APC)** - machine-readable YAML files that define the operational contract for each Area of Responsibility (AoR) within the CA360º Portal ecosystem.

## What is an AoR Portal Contract?

An AoR Portal Contract is a comprehensive specification that defines:

- **Identity**: AoR name, ID, description, and stakeholder type
- **Entrypoints**: Primary and secondary navigation paths into the AoR's domain
- **Visibility**: Filters defining what content is visible to the AoR (OPT-INS, ATA, lifecycle phases, knots, categories, status)
- **Interfaces**: Communication patterns with other AoRs (objects exchanged, handshakes, triggers)
- **Outputs**: Deliverables and evidence produced by the AoR with definition-of-done criteria
- **Tools**: Required tooling (TALF-governed and templates)
- **Publishing**: Destinations for AoR outputs with integrity controls
- **Workqueue**: Input sources, KPIs, and prioritization rules
- **Governance**: Approval authorities and review cycles
- **CI Validation**: Gates that enforce contract compliance

## Files

### `aor_contract_PHM.yaml`

**AoR:** STK_PHM (Physical Hardware and Mechanical Engineering)

**Version:** 1.0  
**Status:** ACTIVE

**Key Characteristics:**
- Primary execution in LC04 (Engineering Analysis)
- Interfaces with SE, TEST, CERT, CM, CY
- Produces 6 output types: mechanical design specs, thermal/structural analysis, integration plans, evidence indices
- Requires TALF-governed tools (CATIA, ANSYS, MATLAB, Python)
- Publishes to analysis exports, evidence packages, monitoring registry
- KPIs: analysis coverage, rework rate, open high-risk items, MoC acceptance, evidence timeliness

## Contract Schema

```yaml
aor:
  id: string
  name: string
  full_name: string (STK_*)
  description: string
  owner: string
  stakeholder_type: string

entrypoints:
  primary: [path, description, access_pattern]
  secondary: [path, description, access_pattern]

visibility:
  filters:
    optin_axis: [list]
    ata: [range or list]
    lifecycle: [list]
    knots: [list]
    categories: [list]
    status: [list]
  scope_notes: string

interfaces:
  communicate_with:
    - aor: string
      aor_full: string
      description: string
      objects: [list]
      handshake: string
      triggers: [list]
      criticality: high|medium|low|critical

produce:
  outputs:
    - output_id: string
      category: DELIVERABLE|EVIDENCE|REGISTRY
      type: SPEC|RPT|PROC|INDEX
      path_pattern: string
      description: string
      definition_of_done: [list]
      requires_validation:
        - aor: string
          evidence: [list]
          gates: [list]
          ci_checks: [list]

tools:
  must_find:
    - tool_id: string
      location: string
      description: string
      io: {input: [list], output: [list]}
      format: string (optional)
      talf_governed: boolean (optional)

publish:
  destinations:
    - name: string
      path: string
      description: string
      formats: [list]
      manifest: string
      integrity: [list]
      retention: string
      access_control: string

workqueue:
  sources: [list of strings]
  kpis:
    - name: string
      description: string
      target: string
      measurement: string
  prioritization:
    - criteria: string
      weight: float

governance:
  approval_authority:
    - role: string
      scope: string
      gates: [list]
  review_cycles:
    - phase: string
      frequency: string
      focus: string

ci_validation:
  gates:
    - gate_id: string
      workflow: string
      gate_name: string
      validates: [list]

metadata:
  version: string
  schema_version: string
  created_date: date
  last_updated: date
  status: ACTIVE|DRAFT|SUPERSEDED
  owner: string
  reviewers: [list]
  related_contracts: [list]
  related_deliverables: [list]
  related_registries: [list]
```

## Usage

### Portal Backend Integration

AoR contracts are consumed by the CA360º Portal backend to:

1. **Route requests**: Map user role → AoR → entrypoints
2. **Filter visibility**: Apply visibility filters to content queries
3. **Enforce interfaces**: Validate cross-AoR handshakes and trigger events
4. **Track outputs**: Monitor output delivery against definition-of-done
5. **Validate tools**: Check TALF tool access before task launch (preflight)
6. **Publish artifacts**: Route outputs to correct destinations with integrity checks
7. **Prioritize work**: Apply workqueue prioritization rules
8. **Enforce governance**: Trigger review cycles and approval workflows

### CI/CD Integration

AoR contracts are validated in CI workflows (`.github/workflows/ca360_portal_gates.yml`):

- **Contract schema validation**: YAML structure and required fields
- **Cross-reference validation**: Tool IDs exist in tool_catalog, AoR IDs valid
- **Path validation**: Entrypoints, output paths, and publish destinations exist
- **Interface validation**: Referenced AoRs have reciprocal interfaces defined
- **TALF integration**: Tools marked `talf_governed: true` exist in TALF catalogs

### Adding a New AoR Contract

1. **Create contract file**: `aor_contract_{AOR_ID}.yaml`
2. **Define all required sections**: See schema above
3. **Link to TALF**: If AoR uses licensed tools, reference tool_ids from `tool_catalog.yaml`
4. **Define interfaces**: Specify handshakes with other AoRs (bidirectional)
5. **Specify outputs**: Include path patterns, definition-of-done, validation requirements
6. **Set up CI validation**: Add contract-specific checks to portal gates
7. **Review and approve**: STK_CM + STK_DAB review required

## Related Documentation

- **TALF (Tool Access & Licensing Fabric)**: `CAXS/INFRASTRUCTURE/access/`
- **Tool Catalog**: `CAXS/INFRASTRUCTURE/access/tool_catalog.yaml`
- **Entitlement Matrix**: `CAXS/INFRASTRUCTURE/access/entitlement_matrix.csv`
- **Portal Gates CI**: `.github/workflows/ca360_portal_gates.yml`
- **AoR SSOT Packs**: `CAXS/AoR/STK_*/`
- **PHM TALF Deliverable**: `CAXS/AoR/STK_PHM/PORTAL/DELIVERABLES/00_AMPEL360_SPACET_Q10_GEN_PLUS_PR_00_LC01_K01_STK_PHM__talf-tool-access-licensing-fabric_DELIVERABLE_PROC_I01-R01_DRAFT.md`

## Version Control

**Directory Version:** 1.0  
**Schema Version:** apc_v1.0  
**Last Updated:** 2025-12-19  
**Governance:** STK_CM approval required for new contracts or schema changes  
**Review Frequency:** Quarterly (or as needed for new AoRs)

## Future AoR Contracts

Planned contracts:
- `aor_contract_SE.yaml` (Systems Engineering)
- `aor_contract_TEST.yaml` (Test Engineering)
- `aor_contract_CERT.yaml` (Certification)
- `aor_contract_CM.yaml` (Configuration Management)
- `aor_contract_CY.yaml` (Cybersecurity)
- Additional 8 AoRs (total 14)

Each contract follows the same schema but with AoR-specific content reflecting their unique responsibilities, interfaces, outputs, and tooling requirements.
