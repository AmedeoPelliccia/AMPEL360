# SCHEMAS — Requirement Record Schemas and Controlled Vocabulary Dictionaries

**Directory:** `LC02_SYSTEM_REQUIREMENTS/SCHEMAS/`

## Purpose
This directory contains **requirement record schemas** and **controlled vocabulary dictionaries** that define the structure, validation rules, and standardized terminology for system requirements within the AMPEL360 CAXS framework.

## Contents

### A) Requirement Record Schemas
- JSON Schema / YAML schema definitions for requirement artifacts
- Schema versioning and migration utilities
- Field definitions and data types for requirements
- Validation rule specifications

### B) Controlled Vocabulary Dictionaries
- Standard terminology and allowed values
- Requirement type taxonomies
- Requirement priority/criticality scales
- Traceability relationship types
- Status and lifecycle state definitions

### C) Schema Validation Tools
- Schema validators and compliance checkers
- Schema evolution and backward compatibility tools
- Schema documentation generators

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC02`
- `KNOT` binding (typically K02 for requirements work)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules

**Place artifacts here when they:**
- Define the structure of requirement records
- Establish controlled vocabularies for requirements
- Provide schema validation capabilities
- Document schema evolution and versioning

**Do not place artifacts here when they:**
- Parse or process requirements (use ENGINES/)
- Validate requirement quality or consistency (use VALIDATORS/)
- Build traceability relationships (use TRACE/)
- Export requirements to other formats (use EXPORT/)

## Dependencies
- Nomenclature Standard v6.0
- ATA chapter definitions
- KNOT framework (K01-K14)
- STK_SE architecture standards

## Ownership
**AoR (owners): STK_SE, STK_CM**

## References
- Main README: `MODEL_SOFTWARE/LC02_SYSTEM_REQUIREMENTS/README.md`
- Nomenclature Standard v6.0
- AMPEL360 Controlled Vocabulary
