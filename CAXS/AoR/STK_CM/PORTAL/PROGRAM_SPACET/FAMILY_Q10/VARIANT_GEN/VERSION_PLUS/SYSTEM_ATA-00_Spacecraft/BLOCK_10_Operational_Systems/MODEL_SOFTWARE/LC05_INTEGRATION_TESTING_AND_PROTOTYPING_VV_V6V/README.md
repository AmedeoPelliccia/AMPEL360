# LC05_INTEGRATION_TESTING_AND_PROTOTYPING_VV_V6V
**Lifecycle Phase:** LC05 — Integration Testing & Prototyping (V&V / V6V)

## Purpose
This directory contains **LC05 software artifacts** that enable:
- prototyping and integration campaigns,
- verification/validation automation (V&V / V6V),
- SIL/HIL/PIL environment tooling,
- reproducible execution harnesses,
- generation of **verification closure evidence** for the `MODEL_SOFTWARE` node (ATA-00 / Block 10).

LC05 is the authoritative location for **integration and test execution tooling** and the
**evidence generators** that demonstrate closure against defined acceptance criteria.

## Contents (What belongs in LC05)
Artifacts in this directory typically include:

### A) Prototyping & integration tooling
- Prototyping frameworks and integration harnesses
- Integration environment bootstrappers (config, orchestration, environment manifests)
- Mock/stub generators used to integrate multi-component software chains

### B) SIL / HIL / PIL automation
- SIL execution harnesses and scenario runners
- HIL automation scripts (bench orchestration, I/O scripting, synchronization utilities)
- PIL utilities (target execution wrappers, profiling hooks, runtime controls)

### C) Test automation & evidence generation
- Automated test suites and runners (unit/integration/system-level as defined by program scope)
- Result collectors (logs, traces, coverage reports if applicable)
- Closure evidence generators producing versioned artifacts (reports, summaries, manifests)

### D) Traceability hooks (handoff)
- Evidence pointers linking: requirements (LC02) → design (LC03) → test execution outputs (LC05)
- Test campaign manifests capturing inputs, configs, and execution conditions for reproducibility

> Note: LC05 generates technical verification evidence. **Quality process/QMS governance** belongs to LC06,
> and **authority-facing certification packs / formal compliance submissions** belong to LC08.

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC05`
- `KNOT` binding **as applicable** (commonly K05 for integration/testing and closure evidence)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules
Place software here when it:
- supports integration testing and prototyping activities,
- implements V&V / V6V workflows and test campaign execution,
- automates SIL/HIL/PIL benches or equivalent integration environments,
- generates **closure evidence** (reports, manifests, logs summaries) in a reproducible manner.

Do **not** place software here when it:
- primarily defines requirements/acceptance criteria (use LC02),
- primarily defines architecture/design models (use LC03),
- is an engineering analysis/calculation model (use LC04),
- is QMS/audit/nonconformance management tooling (use LC06),
- is certification pack assembly and authority-facing submission tooling (use LC08),
- is cross-phase CM governance, templates, or export contracts (use LC00).

## Ownership
**AoR (owners): STK_TEST, STK_SE, STK_DAB**

## References
- Main README: `MODEL_SOFTWARE` directory structure definition
- Lifecycle phases (LC00–LC14) definition
- Nomenclature Standard v6.0 and controlled vocabulary section
