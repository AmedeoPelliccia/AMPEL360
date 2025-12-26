# LC08_CERTIFICATION_AND_FIRST_FLIGHT
**Lifecycle Phase:** LC08 — Certification and First Flight (Authority-facing Packs + Readiness Assembly)

## Purpose
This directory contains **LC08 software artifacts** that support:
- certification planning and execution tracking,
- assembly of **authority-facing deliverable packs**,
- preparation of **first-flight / mission readiness** evidence bundles,
- pre-submission compliance checks (completeness, formatting, traceability pointers),
for the `MODEL_SOFTWARE` portal node (ATA-00 / Block 10).

LC08 is the authoritative location for **pack builders, indexes, and readiness orchestration tooling**
that aggregates evidence produced across the lifecycle into submission-ready artifacts.

## Contents (What belongs in LC08)
Artifacts in this directory typically include:

### A) Certification planning & execution tooling
- Certification plan support utilities (milestones, deliverable mapping, submission schedules)
- Compliance status trackers (what is planned / produced / reviewed / approved)

### B) Authority-facing deliverable builders (pack assembly)
- Pack assemblers that collect and structure:
  - compliance matrices and indexes,
  - evidence manifests and evidence pointers,
  - release/baseline references (hashes, tags, CI mappings),
  - approval snapshots (who approved what, when).
- Authority-facing formatting/export utilities (program-defined formats)

### C) Compliance evidence indexing (aggregation, not primary generation)
- Evidence index generators that reference source evidence from:
  - LC05 (verification closure evidence),
  - LC06 (QMS/audit/NCR and quality gates),
  - LC07 (safety/security assurance objectives and evidence),
  - and relevant upstream artifacts (LC02/LC03/LC04).
- Traceability integrity checks (missing links, orphan evidence, inconsistent IDs)

### D) First-flight / mission readiness tools
- Readiness assessment tooling (criteria checkers, readiness scorecards)
- Readiness bundle builders (mission readiness evidence packs)

> Note: LC08 primarily **assembles, indexes, and prepares** authority-facing packs and readiness bundles.
> **Primary technical test execution evidence** belongs to LC05, **QMS/audits/NCR/gates** belong to LC06,
> and **safety/security assurance evidence** belongs to LC07.

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC08`
- `KNOT` binding **as applicable** (commonly K08 for certification planning and authority pack assembly)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules
Place software here when it:
- supports certification planning and compliance status tracking,
- assembles authority-facing deliverable packs from lifecycle evidence pointers,
- generates compliance matrices/indexes/manifests for submission packages,
- performs pre-submission checks (completeness, formatting, traceability integrity),
- builds first-flight/mission readiness bundles and readiness criteria scorecards.

Do **not** place software here when it:
- primarily executes verification tests or produces raw technical logs (use LC05),
- primarily manages QMS processes, audits, NCR workflows, or quality gates (use LC06),
- primarily performs safety/security case engineering and assurance tooling (use LC07),
- primarily defines requirements (LC02) or design models (LC03),
- is cross-phase portal governance/templates/contracts (use LC00),
- is release packaging/serialization CM tooling (use LC10 / LC11 as applicable).

## Ownership
**AoR (owners): STK_CERT, STK_TEST, STK_OPS**

## References
- Main README: `MODEL_SOFTWARE` directory structure definition
- Lifecycle phases (LC00–LC14) definition
- Nomenclature Standard v6.0 and controlled vocabulary section

