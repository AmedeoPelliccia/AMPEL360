# LC03_DESIGN_MODELS
**Lifecycle Phase:** LC03 — Design Models (Architecture + Interface Modeling)

## Purpose
This directory contains **LC03 software artifacts** used to define, maintain, and baseline
the **architecture and design models** for the `MODEL_SOFTWARE` node (ATA-00 / Block 10). It covers:
- architecture modeling and MBSE/SysML workflows,
- design baseline generation and control,
- interface modeling utilities (ICDs, contracts, schema baselines),
- model transformations and design documentation generation.

LC03 is the authoritative location for **design intent** and **interface definition tooling** that
seeds downstream analysis (LC04), integration/testing (LC05), and release baselines (LC10/LC11).

## Contents (What belongs in LC03)
Artifacts in this directory typically include:

### A) Architecture & MBSE/SysML tooling
- SysML/MBSE model utilities (validation, consistency checks, exports)
- Architecture model generators and baseline packagers
- Model transformation utilities (model-to-schema, schema-to-doc, etc.)

### B) Design baseline generators
- Scripts/utilities to generate design baselines (snapshots, diffs, model manifests)
- Design documentation generators (model-to-doc pipelines)

### C) Interface modeling & contract utilities
- Interface definition utilities (ICD schema generators, contract validators)
- Interface compatibility tooling (versioning rules, diff tools, breaking-change checks)
- Interface baseline control helpers (interface manifests, interface CI mapping)

> Note: LC03 owns architecture/design and interface definition tooling. Numerical analyses and trade studies
> belong to LC04. Integration/test harnesses and verification closure tooling belong to LC05.

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC03`
- `KNOT` binding **as applicable** (commonly K03 for design baselines and interface control)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules
Place software here when it:
- supports system/software architecture definition and refinement,
- implements MBSE workflows (SysML validation, export, baseline creation),
- generates or controls design baselines (including model manifests),
- manages interface definitions as governed configuration items (ICDs/contracts),
- produces design documentation derived from authoritative models.

Do **not** place software here when it:
- primarily defines requirements/acceptance criteria or traceability capture (use LC02),
- primarily executes engineering analyses or trade studies (use LC04),
- is a test/prototyping harness or V&V tooling (use LC05),
- is cross-phase CM governance, templates, or export contracts (use LC00),
- is release packaging/serialization CM tooling (use LC10/LC11 as applicable).

## Ownership
**AoR (owners): STK_SE, STK_PHM, STK_DAB**

## References
- Main README: `MODEL_SOFTWARE` directory structure definition
- Lifecycle phases (LC00–LC14) definition
- Nomenclature Standard v6.0 and controlled vocabulary section

**References:**
- Main README Section 11: MODEL_SOFTWARE Directory Structure
- Lifecycle Phases: Section 10.2.8 of main README
