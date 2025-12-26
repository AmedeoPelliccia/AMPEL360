# LC13_MRO_AND_SUSTAINMENT
**Lifecycle Phase:** LC13 — MRO and Sustainment (Maintenance Programs + Reliability/PHM)

## Purpose
This directory contains **LC13 software artifacts** that support maintenance and sustainment for the
`MODEL_SOFTWARE` portal node (ATA-00 / Block 10), including:
- maintenance program tooling (planning, intervals, task program structures),
- maintenance manual and task card generators (program-defined formats),
- sustainment evidence tooling (closure evidence, sustainment readiness packs),
- reliability and maintainability support utilities (metrics, tracking, reporting),
- PHM (Prognostics and Health Management) integration utilities,
- maintenance scheduling and sustainment workflow automation.

LC13 is the authoritative location for **maintenance and sustainment lifecycle tooling** that enables
continued airworthiness/mission readiness in service.

## Contents (What belongs in LC13)
Artifacts in this directory typically include:

### A) Maintenance program tooling
- Maintenance program definition tools (tasks, intervals, applicability logic)
- Maintenance scheduling helpers (planning horizons, constraints, resource models)

### B) Manuals, task cards, and sustainment documentation generators
- Maintenance manual generators (structured outputs, publication pipelines)
- Task card generators and validators (format consistency, completeness checks)

### C) Sustainment evidence and readiness tooling
- Sustainment evidence packagers (program-defined sustainment evidence bundles)
- Closure evidence tooling for sustainment activities (traceable outputs, reproducible snapshots)

### D) Reliability / PHM integration utilities
- Reliability and sustainment metrics tooling (in-service metrics, trends, reporting)
- PHM integration utilities (health monitoring hooks, diagnostic/prognostic interfaces)
- Data normalization/ingestion helpers used for sustainment analytics (as applicable)

> Note: LC13 focuses on **maintenance and sustainment**. Customer support and service process tooling belong
> to LC12. Operational baselines and mission/ops tooling belong to LC11. End-of-life and circularity closure
> procedures belong to LC14.

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC13`
- `KNOT` binding **as applicable** (commonly K13 for MRO/sustainment tooling and evidence)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules
Place software here when it:
- supports maintenance activities and maintenance program management,
- generates MRO documentation (manuals, task cards) as governed artifacts,
- produces sustainment evidence bundles and readiness outputs,
- integrates or interfaces with PHM/reliability systems,
- tracks and reports sustainment/reliability metrics for in-service lifecycle support.

Do **not** place software here when it:
- primarily supports customer service and ticketing/knowledge base workflows (use LC12),
- primarily supports mission operations runtime/procedures (use LC11),
- primarily performs generic engineering analyses/trade studies unrelated to sustainment evidence (use LC04),
- is cross-phase portal governance/templates/contracts (use LC00),
- is retirement/EoL and circularity closure tooling (use LC14).

## Ownership
**AoR (owners): STK_MRO, STK_PHM, STK_DAB**

## References
- Main README: `MODEL_SOFTWARE` directory structure definition
- Lifecycle phases (LC00–LC14) definition
- Nomenclature Standard v6.0 and controlled vocabulary section

