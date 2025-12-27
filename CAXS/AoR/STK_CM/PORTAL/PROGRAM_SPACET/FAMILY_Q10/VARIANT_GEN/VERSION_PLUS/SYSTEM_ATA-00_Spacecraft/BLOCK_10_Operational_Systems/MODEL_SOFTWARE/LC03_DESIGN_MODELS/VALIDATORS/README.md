# VALIDATORS — model linting, consistency checks, trace checks

**Directory:** `LC03_DESIGN_MODELS/VALIDATORS/`

## Purpose
This directory contains **design model validation tools** that ensure models meet quality standards, maintain structural integrity, satisfy consistency rules, and maintain proper traceability to requirements.

## Contents

### A) Model Linting
- Naming convention validators
- Package structure checkers
- Stereotype usage validators
- Modeling guideline enforcers
- Best practice compliance checkers
- Controlled vocabulary validators

### B) Consistency Checks
- Unconnected port detectors
- Orphan element identifiers
- Invalid link validators
- Circular dependency detectors
- Type consistency checkers
- Multiplicity constraint validators

### C) Trace Checks
- Requirement-to-model traceability validators
- Model element coverage analyzers
- Trace completeness checkers
- Trace link integrity validators
- KNOT task binding validators

### D) Structural Integrity Checks
- Model completeness analyzers
- Interface compatibility validators
- Hierarchy consistency checkers
- Constraint satisfaction validators
- Model well-formedness checkers

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC03`
- `KNOT` binding (typically K03 for design work)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules

**Place artifacts here when they:**
- Validate model structure and quality
- Check consistency and completeness
- Verify traceability to requirements
- Enforce modeling standards and guidelines

**Do not place artifacts here when they:**
- Generate or modify models (use MBSE/)
- Transform models to other formats (use TRANSFORMS/)
- Create model baselines (use BASELINES/)
- Implement CI gates (use CI/)

## Dependencies
- SysML/UML metamodel specifications
- LC02 requirement records and trace bindings
- Modeling guidelines and standards
- KNOT task definitions

## Ownership
**AoR (owners): STK_SE, STK_CM, STK_CERT**

## References
- Main README: `MODEL_SOFTWARE/LC03_DESIGN_MODELS/README.md`
- AMPEL360 Modeling Guidelines
- Quality Standards and Best Practices
- Traceability Framework
