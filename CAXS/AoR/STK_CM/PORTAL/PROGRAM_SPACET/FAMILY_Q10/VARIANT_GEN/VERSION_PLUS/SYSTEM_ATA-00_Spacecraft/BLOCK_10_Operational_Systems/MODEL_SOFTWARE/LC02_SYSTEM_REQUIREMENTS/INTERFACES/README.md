# INTERFACES — ICD Candidate Extraction and Cross-ATA Coupling Tools

**Directory:** `LC02_SYSTEM_REQUIREMENTS/INTERFACES/`

## Purpose
This directory contains **interface analysis tools** that identify interface control document (ICD) candidates from requirements and analyze cross-ATA coupling and dependencies.

## Contents

### A) ICD Candidate Extraction
- Interface requirement identification tools
- ICD candidate extraction engines
- Interface boundary detection utilities
- Interface specification generators

### B) Cross-ATA Coupling Analysis
- ATA chapter dependency analyzers
- Cross-domain coupling detectors
- Inter-system interface mappers
- Coupling strength assessment tools

### C) Interface Validation
- Interface completeness checkers
- Interface consistency validators
- Bidirectional interface verification
- Interface compatibility analyzers

### D) Interface Documentation
- ICD template generators
- Interface catalog builders
- Interface matrix generators
- Cross-reference documentation tools

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC02`
- `KNOT` binding (typically K02 for requirements work)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules

**Place artifacts here when they:**
- Extract or identify ICD candidates from requirements
- Analyze cross-ATA dependencies and coupling
- Validate interface definitions and completeness
- Generate interface documentation and catalogs

**Do not place artifacts here when they:**
- Define schemas (use SCHEMAS/)
- Parse general requirements (use ENGINES/)
- Build general traceability (use TRACE/)
- Export to external formats (use EXPORT/)

## Dependencies
- ATA chapter definitions and boundaries
- SCHEMAS/ for interface requirement structure
- TRACE/ for dependency analysis
- STK_SE interface governance standards

## Ownership
**AoR (owners): STK_SE, STK_DAB**

## References
- Main README: `MODEL_SOFTWARE/LC02_SYSTEM_REQUIREMENTS/README.md`
- ICD Governance Standards
- ATA Chapter Definitions
- OPT-INS Framework
