# LC11_OPERATIONS
**Lifecycle Phase:** LC11 — Operations (ConOps / Procedures / Operational Baselines)

## Purpose
This directory contains **LC11 software artifacts** that support operations for the
`MODEL_SOFTWARE` portal node (ATA-00 / Block 10), including:
- ConOps (Concept of Operations) tooling and operational scenario support,
- procedure generation and validation utilities,
- operational readiness validators and scorecards,
- operational baseline software/configuration tooling,
- mission operations control support utilities (monitoring, planning, control-room workflows),
- operations monitoring and runtime observability helpers.

LC11 is the authoritative location for **how the system is operated**: operational baselines,
procedures, readiness, and mission/ground operations tooling.

## Contents (What belongs in LC11)
Artifacts in this directory typically include:

### A) ConOps & operational scenario tooling
- ConOps generators and scenario modeling utilities (ops flows, mission sequences)
- Operational constraints and run-time policy validators (ops-level rules)

### B) Procedures & validation
- Procedure generators (checklists, runbooks, operational sequences)
- Procedure validators (consistency checks, completeness, versioned outputs)

### C) Operational readiness & baselines
- Readiness assessment tooling (criteria evaluation, readiness scorecards)
- Operational baseline managers (approved operational configurations and parameter sets)

### D) Mission operations control support (as applicable)
- Operations monitoring utilities (telemetry dashboards, alerting rulesets)
- Flight/mission planning support tools (program-defined planning artifacts)
- Control-room workflow helpers (handover logs, shift reports, event tracking)

> Note: LC11 focuses on **operational baselines and run-time procedures**. Industrialization, serialization,
> and production CM belong to LC10. Authority-facing certification packs and first-flight readiness assembly
> belong to LC08.

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC11`
- `KNOT` binding **as applicable** (commonly K11 for operations readiness and operational baselines)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules
Place software here when it:
- supports operational activities (ConOps, mission/ops flows, planning support),
- generates or validates operational procedures and runbooks,
- validates operational readiness criteria and produces readiness outputs,
- manages approved operational baselines and run-time configurations,
- supports mission operations control workflows (monitoring, reporting, event handling).

Do **not** place software here when it:
- primarily packages/serializes software releases or controls production baselines (use LC10),
- primarily assembles authority-facing certification packs (use LC08),
- primarily executes integration tests and produces technical closure logs (use LC05),
- primarily governs QMS/audits/NCR workflows and quality gates (use LC06),
- is cross-phase portal governance/templates/contracts (use LC00).

## Ownership
**AoR (owners): STK_OPS, STK_SPACEPORT, STK_CM**

## References
- Main README: `MODEL_SOFTWARE` directory structure definition
- Lifecycle phases (LC00–LC14) definition
- Nomenclature Standard v6.0 and controlled vocabulary section
