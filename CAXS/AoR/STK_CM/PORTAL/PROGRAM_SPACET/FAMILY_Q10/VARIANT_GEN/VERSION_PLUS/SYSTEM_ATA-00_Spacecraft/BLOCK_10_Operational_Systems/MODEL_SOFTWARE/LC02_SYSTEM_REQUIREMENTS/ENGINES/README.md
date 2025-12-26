# ENGINES — Parsers, Normalizers, ID Services, and Baseline Managers

**Directory:** `LC02_SYSTEM_REQUIREMENTS/ENGINES/`

## Purpose
This directory contains **requirement processing engines** that parse, normalize, and manage requirements throughout their lifecycle, ensuring consistency, traceability, and baseline integrity.

## Contents

### A) Parsers
- Requirement document parsers (text, markdown, structured formats)
- Multi-format import utilities
- Natural language requirement extraction tools
- Requirement metadata extractors

### B) Normalizers
- Requirement text normalization utilities
- Standardization engines for requirement format and structure
- Consistency harmonization tools
- Cross-reference resolution utilities

### C) ID Services
- Requirement ID generation and assignment services
- ID uniqueness validation
- ID schema enforcement tools
- ID lifecycle management utilities

### D) Baseline Managers
- Requirement baseline creation and management
- Baseline comparison and diff utilities
- Baseline freeze and release tools
- Baseline versioning and configuration control

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC02`
- `KNOT` binding (typically K02 for requirements work)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules

**Place artifacts here when they:**
- Parse requirements from source documents
- Normalize or standardize requirement formats
- Generate or manage requirement identifiers
- Create or manage requirement baselines

**Do not place artifacts here when they:**
- Define schemas (use SCHEMAS/)
- Validate quality or detect contradictions (use VALIDATORS/)
- Build traceability graphs (use TRACE/)
- Export to external formats (use EXPORT/)

## Dependencies
- SCHEMAS/ for requirement record structure
- Nomenclature Standard v6.0 for ID generation
- Configuration management tools (STK_CM)

## Ownership
**AoR (owners): STK_SE, STK_CM, STK_DAB**

## References
- Main README: `MODEL_SOFTWARE/LC02_SYSTEM_REQUIREMENTS/README.md`
- Nomenclature Standard v6.0
- Configuration Management Baseline Standards
