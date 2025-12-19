# TALF — Tool Access & Licensing Fabric (AoR: STK_PHM)

## Intent
Define the PHM requirements so CA360º becomes **operable** (not only governable):
- Entitlements (who can use which tools)
- License checkout (how access is granted, pools, constraints)
- Launch channel (VDI/HPC/container/API) and workspace bindings
- Preflight enforcement before "Start Task"
- Audit events linkable as Evidence for LC gates

## Scope
In-scope:
- PHM execution tooling classes (CAD/CAE/analysis/data mounts)
- AoR contract fields to declare access/licensing/launch/audit
- Preflight rules and audit evidence requirements

Out-of-scope:
- Procurement/vendor decisions
- IT platform implementation specifics (VDI vendor, scheduler brand)
- Informal off-portal usage

## Problem
PHM tasks can be routed and governed but execution is not deterministic:
- missing entitlements/group membership
- unclear or unavailable license checkout/pool
- launch not bound to node context (inputs/outputs/templates)
- blocked execution not recorded as standardized evidence

This creates delivery friction and audit gaps for LC03/LC06.

## Normative Requirements (MUST)
### TALF-R1 — Entitlements
Portal MUST check entitlements for each PHM-required tool prior to task start.

### TALF-R2 — Licensing Metadata
For each licensed tool, AoR declarations MUST include:
license_model, server_type, pool_id, checkout_mode, constraints.

### TALF-R3 — Preflight Gate
Portal MUST run preflight before "Start Task":
SSO valid, entitlement OK, license available (if required), compute profile ready.
Failure MUST block start (or explicit degraded mode) and record an auditable event.

### TALF-R4 — Audit Events
Portal MUST record: login, launch, checkout, checkout_fail, usage, export.
Events MUST be linkable from PHM Evidence Index and (when used) Release Evidence Packs.

### TALF-R5 — Tool Catalog SSOT
Tool references MUST use stable tool_id validated against a canonical tool_catalog.

## PHM Tool Set (Pilot — classes)
- CAD (VDI): CATIA-class CAD
- CAE/Solver (HPC): solver job submission
- Analysis (VDI/container): MATLAB/Python notebooks
- Workspace mounts: repo node + exports + datasets + templates

## Interfaces
- STK_CM: release packaging and baseline gates may require tool-access evidence snapshots
- STK_DAB: schema/catalog definitions for tool declarations
- STK_CY: security/export constraints affecting access and mounts
- STK_CERT: acceptance of tool/audit evidence as supporting proof for LC gates (where applicable)

## Definition of Done
- This deliverable is linked from PHM registries (task/roadmap/evidence/signoff)
- Tool catalog + entitlement matrix are populated for pilot tools
- Preflight blocks task start without entitlement/license and records evidence
- At least one success path and one blocked path are demonstrable and linkable

## Next Actions
Create tasks PHM-TALF-* in PHM portal registries and track through LC01→LC03→LC06.
