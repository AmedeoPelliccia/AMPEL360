# VALIDATORS — Quality Checks, Constraint Checks, and Contradiction Detectors

**Directory:** `LC02_SYSTEM_REQUIREMENTS/VALIDATORS/`

## Purpose
This directory contains **requirement validation tools** that ensure requirements meet quality standards, satisfy constraints, and are free from contradictions, ambiguities, and completeness gaps.

## Contents

### A) Quality Checks
- Requirement quality attribute validators (clarity, completeness, testability)
- Writing quality checks (grammar, consistency, unambiguous language)
- Requirement structure validators
- Best practice compliance checkers

### B) Constraint Checks
- Technical constraint validation
- Inter-requirement constraint checking
- Regulatory and standards compliance validators
- Allocation and coverage constraint checks

### C) Contradiction Detectors
- Logical contradiction detection tools
- Conflict analysis engines
- Inconsistency identification utilities
- Resolution recommendation generators

### D) Completeness Analyzers
- Coverage analysis tools
- Gap detection utilities
- Missing requirement identification
- Traceability completeness validators

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC02`
- `KNOT` binding (typically K02 for requirements work)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules

**Place artifacts here when they:**
- Validate requirement quality and conformance
- Check constraints and consistency rules
- Detect contradictions or conflicts
- Assess requirement completeness and coverage

**Do not place artifacts here when they:**
- Define schemas or structures (use SCHEMAS/)
- Parse or normalize requirements (use ENGINES/)
- Build traceability relationships (use TRACE/)
- Generate gate pass/fail reports (use CI/)

## Dependencies
- SCHEMAS/ for validation rules
- ENGINES/ for normalized requirement data
- Quality standards and best practices (STK_SE, STK_CERT)

## Ownership
**AoR (owners): STK_SE, STK_CM, STK_CERT**

## References
- Main README: `MODEL_SOFTWARE/LC02_SYSTEM_REQUIREMENTS/README.md`
- AMPEL360 Quality Standards
- Requirements Engineering Best Practices
