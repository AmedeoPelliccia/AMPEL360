# LC09_GREEN_AIRCRAFT_BASELINES
**Lifecycle Phase:** LC09 — Green Aircraft / Baselines (Sustainability + Circularity KPIs)

## Purpose
This directory contains **LC09 software artifacts** that establish and maintain the
**sustainability and circularity baselines** for the `MODEL_SOFTWARE` portal node (ATA-00 / Block 10).
It supports:
- sustainability baseline definition and tracking,
- circularity KPI calculation and reporting,
- ESG reporting baseline generation,
- environmental impact metric tooling (e.g., CO₂e, energy intensity, material circularity),
- governance of “green baselines” as controlled, versioned artifacts.

LC09 is the authoritative location for **baseline-level sustainability metrics and reporting tooling**
that can be referenced by program baselines, releases, and lifecycle closure activities.

## Contents (What belongs in LC09)
Artifacts in this directory typically include:

### A) Sustainability baseline tooling
- Baseline calculators for environmental metrics (CO₂e, energy use, intensity indicators)
- Baseline pack generators (snapshot manifests, parameter sets, reproducibility notes)

### B) Circularity KPIs & circular economy workflows
- Circularity KPI calculators (reuse/recycle/return flows, material circularity indices)
- Circular economy workflow tools (tracking loops, return/reuse accounting support)

### C) ESG reporting generators
- ESG report generators and index builders (program-defined reporting formats)
- Evidence pointers and metric traceability utilities (inputs → KPI → baseline snapshot)

### D) Environmental impact assessment utilities (baseline-level)
- Impact assessment helpers (scenario comparisons at baseline level)
- Data normalization tooling for sustainability datasets used by KPI baselines

> Note: LC09 focuses on **sustainability/circularity baselines and reporting**. Detailed engineering analyses,
> trade studies, or model validation for green technologies belong to LC04. CM governance and baseline/release
> control rules remain in LC00/LC10.

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC09`
- `KNOT` binding **as applicable** (commonly K09 for sustainability baselines and KPI reporting)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules
Place software here when it:
- defines or updates sustainability baselines and their reproducible calculation pipelines,
- computes and tracks circularity KPIs and circular economy workflow metrics,
- generates ESG baseline reports and associated indexes/manifests,
- provides traceability from metric inputs to KPI outputs and baseline snapshots,
- supports CM consumption of sustainability baselines (STK_CM integration).

Do **not** place software here when it:
- primarily performs detailed engineering analyses, trade studies, or calculation model validation (use LC04),
- is QMS/audit/nonconformance tooling (use LC06),
- is safety/security assurance tooling (use LC07),
- is authority pack assembly (use LC08),
- is cross-phase portal governance/templates/contracts (use LC00),
- is release packaging/serialization CM tooling (use LC10 / LC11 as applicable).

## Ownership
**AoR (owners): STK_PMO, STK_DAB, STK_CM**

## References
- Main README: `MODEL_SOFTWARE` directory structure definition
- Lifecycle phases (LC00–LC14) definition
- Nomenclature Standard v6.0 and controlled vocabulary section


**Primary AoR:** STK_PMO, STK_DAB, STK_CM

**References:**
- Main README Section 11: MODEL_SOFTWARE Directory Structure
- Lifecycle Phases: Section 10.2.8 of main README
