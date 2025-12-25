# INTERFACES — ICD Scaffolding, Port/Signal Dictionary Compilers

**Directory:** `LC03_DESIGN_MODELS/INTERFACES/`

## Purpose
This directory contains **interface modeling tools** that generate Interface Control Document (ICD) scaffolds, compile port and signal dictionaries, and manage interface definitions for design models.

## Contents

### A) ICD Scaffolding
- ICD template generators
- Interface specification builders
- Interface requirement extractors
- ICD document structure generators
- Interface catalog builders

### B) Port/Signal Dictionary Compilers
- Port definition compilers
- Signal dictionary generators
- Interface data type catalogs
- Protocol specification builders
- Message format compilers

### C) Interface Model Generators
- Port and connector generators
- Interface block builders
- Flow specification generators
- Interface boundary modelers
- Communication path generators

### D) Cross-ATA Dependency Modelers
- Inter-system interface mappers
- Coupling graph integrators
- Dependency visualization tools
- Interface impact analyzers
- Cross-domain interface trackers

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC03`
- `KNOT` binding (typically K03 for design work)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules

**Place artifacts here when they:**
- Generate ICD scaffolds or interface specifications
- Compile port, signal, or protocol dictionaries
- Model interface boundaries and connections
- Analyze cross-ATA dependencies

**Do not place artifacts here when they:**
- Generate general architecture models (use MBSE/)
- Transform interface models to other formats (use TRANSFORMS/)
- Validate interface completeness (use VALIDATORS/)
- Export interface data (use EXPORT/)

## Dependencies
- LC02 interface requirement records
- Port/signal naming conventions
- Communication protocol specifications
- ATA chapter definitions and boundaries

## Ownership
**AoR (owners): STK_SE, STK_DAB**

## References
- Main README: `MODEL_SOFTWARE/LC03_DESIGN_MODELS/README.md`
- ICD Governance Standards
- Interface Design Guidelines
- OPT-INS Framework
