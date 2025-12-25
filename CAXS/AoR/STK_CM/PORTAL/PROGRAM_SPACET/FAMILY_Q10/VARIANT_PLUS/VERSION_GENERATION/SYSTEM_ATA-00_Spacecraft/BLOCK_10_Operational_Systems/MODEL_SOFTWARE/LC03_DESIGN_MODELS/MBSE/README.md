# MBSE — SysML/UML Generators, Package Skeleton Builders, Sync Engines

**Directory:** `LC03_DESIGN_MODELS/MBSE/`

## Purpose
This directory contains **Model-Based Systems Engineering (MBSE) automation tools** that generate, update, and synchronize SysML/UML models, create architecture skeletons, and maintain consistency between requirements and design models.

## Contents

### A) SysML/UML Model Generators
- Block definition diagram (BDD) generators
- Internal block diagram (IBD) generators
- Activity diagram builders
- State machine generators
- Sequence diagram builders
- Use case model generators

### B) Package Skeleton Builders
- System decomposition skeleton generators
- Architecture package structure builders
- Subsystem hierarchy generators
- Component structure initializers
- Model organization utilities

### C) Sync Engines
- Requirement-to-model synchronization tools
- Model consistency maintenance utilities
- Cross-model reference updaters
- Stereotype application engines
- Property propagation tools

### D) Model Automation Utilities
- Bulk model element creators
- Pattern-based model generation
- Model refactoring tools
- Template instantiation engines
- Model merge and integration utilities

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC03`
- `KNOT` binding (typically K03 for design work)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules

**Place artifacts here when they:**
- Generate or update SysML/UML model elements
- Build architecture skeletons and package structures
- Synchronize requirements with model elements
- Automate model creation or maintenance tasks

**Do not place artifacts here when they:**
- Generate interface-specific models (use INTERFACES/)
- Transform models to other formats (use TRANSFORMS/)
- Validate model structure or quality (use VALIDATORS/)
- Create model baselines or snapshots (use BASELINES/)

## Dependencies
- SysML/UML metamodel specifications
- LC02 requirement records and trace bindings
- Model authoring tool APIs (Cameo, Capella, etc.)
- SCHEMAS/ for model structure definitions

## Ownership
**AoR (owners): STK_SE, STK_CM**

## References
- Main README: `MODEL_SOFTWARE/LC03_DESIGN_MODELS/README.md`
- SysML Specification (OMG)
- UML Specification (OMG)
- AMPEL360 MBSE Guidelines
