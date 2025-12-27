# LC07_SAFETY_AND_SECURITY
**Lifecycle Phase:** LC07 — Safety and Security (Assurance Objectives + Evidence)

## Purpose
This directory contains **LC07 software artifacts** that support the Safety and Security assurance
activities for the `MODEL_SOFTWARE` portal node (ATA-00 / Block 10). It covers tooling for:
- safety case and security case support (generation, consistency checks, evidence indexing),
- hazard analysis automation (FHA / PSSA / SSA or program-equivalent),
- cybersecurity assurance utilities (control verification support, assurance objectives tracking),
- operational constraints / limits validators derived from safety and security requirements,
- risk assessment automation and validation workflows.

LC07 is the authoritative location for **assurance-focused tooling** that substantiates safety and
cybersecurity objectives with traceable, auditable evidence pointers.

## Contents (What belongs in LC07)
Artifacts in this directory typically include:

### A) Safety assurance tooling
- Safety case generators and consistency validators (structure, completeness checks)
- Hazard analysis automation (FHA/PSSA/SSA workflows, hazard/control mapping utilities)
- Safety constraint checkers (policy validators enforcing derived operational constraints)

### B) Security assurance tooling
- Cybersecurity assurance utilities (objective/control mapping, verification support tooling)
- Security scanning and validation tools (as governed by program policy)
- Risk assessment automation (threat/risk scoring helpers, mitigation tracking utilities)

### C) Constraints & limits validation
- Validators for operational limits/constraints derived from:
  - safety requirements and hazard controls, and/or
  - cybersecurity assurance objectives and controls.

> Note: LC07 is about safety/security assurance objectives and evidence tooling. **Quality process/QMS,
> audits, and nonconformance workflows** belong to LC06. **Authority-facing certification packs and
> formal compliance submissions** belong to LC08.

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC07`
- `KNOT` binding **as applicable** (commonly K07 for safety/security assurance activities)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules
Place software here when it:
- supports safety engineering assurance workflows (case structure, hazard analysis automation),
- supports cybersecurity assurance workflows (controls, assessments, validation tooling),
- validates derived operational constraints/limits tied to safety/security objectives,
- automates risk/threat/hazard assessments within the governed program method.

Do **not** place software here when it:
- primarily executes integration tests and produces technical closure evidence (use LC05),
- primarily governs QMS, audits, NCR management, or quality gates (use LC06),
- primarily assembles certification submissions and authority-facing packs (use LC08),
- primarily defines requirements/acceptance criteria (use LC02) or design models (use LC03),
- is cross-phase portal governance/templates/contracts (use LC00).

## Ownership
**AoR (owners): STK_SAF, STK_CY, STK_SE**

## References
- Main README: `MODEL_SOFTWARE` directory structure definition
- Lifecycle phases (LC00–LC14) definition
- Nomenclature Standard v6.0 and controlled vocabulary section

