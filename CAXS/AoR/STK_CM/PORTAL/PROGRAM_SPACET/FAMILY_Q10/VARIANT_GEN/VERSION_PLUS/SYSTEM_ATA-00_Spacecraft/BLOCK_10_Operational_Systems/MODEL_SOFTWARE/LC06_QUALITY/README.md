# LC06_QUALITY
**Lifecycle Phase:** LC06 — Quality (QMS / Audits / Gates / Nonconformance)

## Purpose
This directory contains **LC06 software artifacts** that support the Quality function for the
`MODEL_SOFTWARE` portal node (ATA-00 / Block 10). It covers:
- QMS-enabled tooling and process-quality automation,
- audit management and evidence handling,
- nonconformance (NCR/NC) tracking workflows,
- quality gate validators and compliance checks,
- quality metrics collection and reporting.

LC06 is the authoritative location for **quality governance tooling** that ensures lifecycle outputs
(LC01–LC14) are produced and reviewed under controlled, auditable processes.

## Contents (What belongs in LC06)
Artifacts in this directory typically include:

### A) QMS & process quality automation
- Workflow validators enforcing defined process steps and deliverable completeness
- Document/process compliance checking utilities (naming policy, mandatory metadata, controlled vocabulary checks)

### B) Audit management & evidence handling
- Audit planning/execution tooling (audit schedules, checklists, findings tracking)
- Audit evidence packagers (collection, indexing, reproducible snapshots)

### C) Nonconformance management
- NCR/NC trackers, triage workflows, disposition and corrective action support
- Traceability hooks linking NCRs to affected artifacts/releases (as applicable)

### D) Quality gates & metrics
- Quality gate validators (pass/fail criteria, required evidence pointers)
- Metrics collection and reporting utilities (coverage of gates, defect rates, audit trends)

> Note: LC06 governs quality processes and gates. **Test execution and technical closure evidence generation**
> belong to LC05. **Safety/security assurance objectives and evidence** belong to LC07. **Authority-facing
> certification packs** belong to LC08.

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC06`
- `KNOT` binding **as applicable** (commonly K06 for quality governance and gate enforcement)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules
Place software here when it:
- supports QMS and process-quality management,
- implements or validates quality gates and compliance checks,
- manages audits (planning, findings, evidence packaging),
- tracks nonconformances and corrective actions,
- collects and reports quality metrics across lifecycle outputs.

Do **not** place software here when it:
- primarily executes tests or produces technical verification logs/closure outputs (use LC05),
- primarily defines safety or cybersecurity assurance content (use LC07),
- primarily assembles certification submissions and authority-facing packs (use LC08),
- is cross-phase portal governance, templates, or export contracts (use LC00),
- is release packaging/serialization CM tooling (use LC10 / LC11 as applicable).

## Ownership
**AoR (owners): STK_CM, STK_PMO, STK_TEST**

## References
- Main README: `MODEL_SOFTWARE` directory structure definition
- Lifecycle phases (LC00–LC14) definition
- Nomenclature Standard v6.0 and controlled vocabulary section
