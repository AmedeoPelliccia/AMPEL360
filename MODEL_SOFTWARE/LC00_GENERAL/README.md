# LC00_GENERAL
**Lifecycle Phase:** LC00 — General / Cross-Phase (Portal + Configuration Management layer)

## Purpose
This directory contains the **cross-phase (LC00) governance and shared control artifacts** for the
`MODEL_SOFTWARE` portal node (ATA-00 / Block 10). It exists to ensure that **all lifecycle phases (LC01–LC14)**
operate under a consistent **configuration management, naming, registry, export, and evidence** framework.

LC00_GENERAL is the **single source of truth** for:
- Portal node scope and boundaries (what belongs here vs. other LC folders)
- Cross-phase CM rules (baseline/release conventions, immutability rules, traceability expectations)
- Common templates and checklists reused across LC folders
- Registry seeds and canonical index structures used by the portal renderer
- Export and packaging contracts (release packs, manifests, retention, verification rules)

## Contents (What belongs in LC00_GENERAL)
Artifacts in this directory typically include:

### A) Portal governance & navigation
- Node scope statement and applicability notes (ATA-00 / B10 / MODEL_SOFTWARE)
- `00_INDEX.md` navigation for LC00–LC14
- Access/write rules aligned to lifecycle ownership (LC01–LC14 owners)

### B) CM cross-phase control
- Baseline and release conventions (IDs, tagging strategy, freeze/unfreeze policy)
- Configuration status accounting principles for software CIs
- Controlled vocabulary references and policy bindings (v6.0 compliance hooks)

### C) Shared templates (reused in multiple LCs)
- Standard stubs for: requirements, design, test evidence, audit packs, release notes
- KNOT checklist templates (K01–K14) to be instantiated per release/program increment

### D) Registry seeds (not phase-specific)
- Canonical registry schemas (CSV/JSON) and field definitions for:
  - Software CI Register
  - Approval/Signoff Register
  - SBOM index (if used)
  - Export manifest index (if used)

### E) Shared tooling (only if cross-phase)
- Utility scripts that support **CM enforcement** (naming validation, index generation, packaging checks)
- Common configuration constants used by multiple lifecycle workflows

> Note: **Product/source code** that is specific to a lifecycle phase or a single delivery should live in the
> relevant LC folder (LC02 requirements tooling, LC05 test harness, etc.), unless it is demonstrably cross-phase
> and governed here.

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC00`
- `KNOT` binding when applicable (K01..K14)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules
Place an artifact in `LC00_GENERAL` when it:
- Applies to **multiple lifecycle phases** (LC01–LC14), or
- Defines **cross-phase governance**, registries, templates, export contracts, or
- Is required to make the portal node **auditable and reproducible** (baseline/release discipline), or
- Is a shared utility strictly supporting CM (validation/index/packaging), not phase-specific engineering content

Do **not** place artifacts here when they are:
- Phase-specific deliverables (put them in the corresponding LC folder), or
- Single-use scripts without cross-phase value, or
- Uncontrolled binaries/outputs without traceability to a CI + manifest + evidence pointer

## Ownership
**Primary AoR (owner): STK_CM**  
**Cross-phase usage:** all lifecycle owners (LC01–LC14) consume LC00 rules/templates/registries as applicable.

## References
- Main README: `MODEL_SOFTWARE` directory structure definition
- Lifecycle phases (LC00–LC14) definition
- Nomenclature Standard v6.0 and controlled vocabulary section

