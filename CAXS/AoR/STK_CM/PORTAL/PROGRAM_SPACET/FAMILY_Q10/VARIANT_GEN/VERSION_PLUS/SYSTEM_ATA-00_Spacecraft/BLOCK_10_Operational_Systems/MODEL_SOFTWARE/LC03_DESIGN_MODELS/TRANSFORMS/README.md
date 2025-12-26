# TRANSFORMS — converters (SysML↔JSON/YAML), model-to-doc pipelines

**Directory:** `LC03_DESIGN_MODELS/TRANSFORMS/`

## Purpose
This directory contains **model transformation tools** that convert design models between different formats, generate documentation from models, and enable model interchange and integration.

## Contents

### A) Model Format Converters
- SysML to JSON converters
- SysML to YAML converters
- JSON/YAML to SysML importers
- XML model interchange utilities
- XMI format handlers
- Cross-tool model converters

### B) Model-to-Doc Pipelines
- Design summary generators
- Interface list exporters
- Architecture documentation builders
- Model report generators
- Diagram to document converters
- Specification document generators

### C) Model-to-Model Transformations
- Architecture refinement transformations
- Model abstraction generators
- View generation from models
- Model projection utilities
- Subsystem extraction tools

### D) Integration Utilities
- Model merge tools
- Model federation utilities
- Cross-model link resolvers
- Model synchronization adapters
- Legacy model importers

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC03`
- `KNOT` binding (typically K03 for design work)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules

**Place artifacts here when they:**
- Convert models between different formats
- Generate documentation from design models
- Transform models to other representations
- Enable model interchange and integration

**Do not place artifacts here when they:**
- Generate initial models (use MBSE/)
- Validate model structure (use VALIDATORS/)
- Export to downstream analysis tools (use EXPORT/)
- Create model baselines (use BASELINES/)

## Dependencies
- SysML/UML metamodel specifications
- JSON/YAML schema definitions
- Documentation template libraries
- XMI interchange format specifications

## Ownership
**AoR (owners): STK_SE, STK_DAB, STK_CM**

## References
- Main README: `MODEL_SOFTWARE/LC03_DESIGN_MODELS/README.md`
- SysML Specification (OMG)
- XMI Specification
- Model Interchange Standards
