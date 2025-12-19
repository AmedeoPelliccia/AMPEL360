# TALF — Tool Access & Licensing Fabric (Infrastructure)

## Purpose

This directory contains the **Single Source of Truth (SSOT)** catalogs for CA360º Portal's Tool Access & Licensing Fabric (TALF). TALF ensures deterministic tool access with licensing enforcement and auditable event trails.

## Files

### 1. `tool_catalog.yaml`
**Canonical registry of all portal-accessible tools.**

Contains:
- Tool definitions with unique `tool_id`
- Tool class (CAD/CAE/ANALYSIS)
- Delivery channel (VDI/HPC/CONTAINER/API)
- Licensing requirements (model, server, pool, checkout mode, constraints)
- Access requirements (SSO, entitlement groups, export control)
- Workspace mount specifications
- Preflight check definitions

**Usage:**
- AoR contracts reference tools by `tool_id`
- Portal validates tool access against this catalog
- CI gates reject unknown `tool_id` references

**Owner:** STK_DAB (schema), STK_CM (governance)

### 2. `entitlement_matrix.csv`
**Mapping between tool_id and entitlement groups.**

Contains:
- tool_id → entitlement_group mappings
- AoR assignments
- Role definitions
- Access level specifications
- Grant dates and notes

**Usage:**
- Portal checks user group membership before tool launch
- Preflight gates block access if entitlement missing
- PMO uses for capacity planning and access audits

**Owner:** STK_CM (governance), STK_CY (security)

### 3. `license_events_registry.md`
**Schema and examples for license/audit events.**

Contains:
- Event type definitions (login, launch, checkout, checkout_fail, usage, export, close, timeout, killed)
- JSON schema for event records
- Sample event examples (success + blocked paths)
- Event collection mechanisms
- Evidence linkage to LC gates
- Retention and compliance policies

**Usage:**
- Portal backend records events per schema
- Blocking events (checkout_fail) generate auditable evidence
- Events are indexed in AoR evidence registries
- Release evidence packs link to events for LC gates
- Analytics for license pool utilization and capacity planning

**Owner:** STK_DAB (schema), STK_CM (governance)

## CI Validation (Gate E)

The CI workflow (`.github/workflows/ca360_portal_gates.yml`) includes **Gate E: TALF Validation** which:

1. **File existence checks:** Validates all three SSOT files exist
2. **Structure validation:** Checks required sections and fields in each file
3. **Cross-validation:** Ensures `tool_id` references in `entitlement_matrix.csv` exist in `tool_catalog.yaml`
4. **PHM PORTAL structure:** Validates PHM AoR has TALF deliverable and registries
5. **Required fields:** Ensures tool_catalog includes all mandatory fields (licensing, access, workspace, preflight_checks)

**CI rejects PRs if:**
- Unknown `tool_id` referenced in entitlement matrix
- tool_catalog missing required fields for licensed tools
- SSOT files missing or malformed

## Usage in AoR Contracts

AoRs declare tool requirements by referencing `tool_id` from `tool_catalog.yaml`:

```yaml
# Example: PHM AoR contract
required_tools:
  - tool_id: catia-v5-vdi
    usage: "CAD modeling for thermal components"
    
  - tool_id: ansys-hpc-solver
    usage: "Structural FEA for mechanical loads"
    
  - tool_id: python-jupyter-container
    usage: "Post-processing and data visualization"
```

Portal enforces:
- User has required entitlements (via `entitlement_matrix.csv`)
- License available (via preflight checks)
- Workspace mounts configured (via `tool_catalog.yaml` mount specs)
- Audit events recorded (via `license_events_registry.md` schema)

## Pilot: STK_PHM

**Scope:** PHM (Physical & Mechanical Engineering) tooling classes

**Tools:**
- CAD (VDI): CATIA V5/V6
- CAE/Solver (HPC): ANSYS, Nastran
- Analysis (VDI/Container): MATLAB, Python Jupyter

**Lifecycle:** LC01 → LC03 → LC06

**Evidence:**
- LC03: Preflight + tool reference validation operational
- LC06: Audit events + evidence linkage accepted

See: `CAXS/AoR/STK_PHM/PORTAL/DELIVERABLES/` for PHM TALF deliverable

## Interfaces

### STK_CM (Configuration Management)
- Release packaging may require tool-access evidence snapshots
- Baseline gates may validate tool versions and license compliance

### STK_DAB (Data & Architecture Board)
- Schema definitions for tool catalog and event registry
- Validation rules for tool declarations

### STK_CY (Cybersecurity)
- Security/export constraints affecting tool access
- Workspace mount security policies
- Audit event retention and access control

### STK_CERT (Certification)
- Acceptance of tool/audit evidence as supporting proof for LC gates
- Validation that tool usage meets certification requirements

### STK_PMO (Program Management Office)
- License pool utilization analytics
- Blocking event escalation
- Capacity planning and resource forecasting

## Adding New Tools

1. **Define tool in `tool_catalog.yaml`:**
   - Assign unique `tool_id`
   - Specify tool_class, delivery_channel, licensing, access, workspace, preflight_checks
   - For licensed tools: MUST include license_model, server_type, pool_id, checkout_mode

2. **Map entitlements in `entitlement_matrix.csv`:**
   - Add rows mapping `tool_id` to entitlement_group(s)
   - Specify AoR, role, access_level

3. **Update AoR contracts:**
   - Reference `tool_id` in AoR tool requirements

4. **CI validation:**
   - Gate E will validate tool_id consistency
   - Ensure all required fields present

5. **Evidence:**
   - Document tool addition in AoR evidence index
   - Link to tool_catalog commit/hash

## Version Control

**Catalog Version:** 1.0  
**Last Updated:** 2025-12-19  
**Governance:** STK_CM approval required for catalog changes  
**Review Frequency:** Quarterly (or as needed for new tool additions)

## References

- **TALF Deliverable (PHM):** `CAXS/AoR/STK_PHM/PORTAL/DELIVERABLES/00_AMPEL360_SPACET_Q10_GEN_PLUS_PR_00_LC01_K01_STK_PHM__talf-tool-access-licensing-fabric_DELIVERABLE_PROC_I01-R01_DRAFT.md`
- **PHM Task Registry:** `CAXS/AoR/STK_PHM/PORTAL/REGISTRIES/task_registry.md`
- **PHM Evidence Index:** `CAXS/AoR/STK_PHM/PORTAL/REGISTRIES/evidence_index.md`
- **CI Gate E:** `.github/workflows/ca360_portal_gates.yml`
