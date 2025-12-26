# EXPORT — Converters to SysML/ReqIF/CSV/JSON and Portal Registry Writers

**Directory:** `LC02_SYSTEM_REQUIREMENTS/EXPORT/`

## Purpose
This directory contains **requirement export and conversion tools** that transform requirements into standard formats (SysML, ReqIF, CSV, JSON) and populate portal registries for consumption by other systems and stakeholders.

## Contents

### A) Format Converters
- SysML requirement export utilities
- ReqIF (Requirements Interchange Format) generators
- CSV export tools for spreadsheet analysis
- JSON export for API integration
- XML export utilities

### B) Portal Registry Writers
- Portal catalog population tools
- Registry synchronization utilities
- Index generation for requirement discovery
- Search metadata extractors

### C) Documentation Generators
- Requirement document builders (PDF, HTML)
- Requirement specification publishers
- Formatted report generators
- Stakeholder-specific views

### D) Integration Adapters
- External tool integration adapters
- Third-party system connectors
- Legacy system export bridges
- API endpoint implementations

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC02`
- `KNOT` binding (typically K02 for requirements work)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules

**Place artifacts here when they:**
- Convert requirements to external formats
- Export to industry-standard interchange formats
- Populate portal registries and catalogs
- Generate documentation for stakeholder delivery

**Do not place artifacts here when they:**
- Define schemas (use SCHEMAS/)
- Parse or normalize input data (use ENGINES/)
- Validate requirements (use VALIDATORS/)
- Build traceability graphs (use TRACE/)

## Dependencies
- SCHEMAS/ for source data structure
- ENGINES/ for normalized requirement data
- SysML/ReqIF/other format specifications
- Portal registry schemas (STK_DAB)

## Ownership
**AoR (owners): STK_DAB, STK_SE, STK_CM**

## References
- Main README: `MODEL_SOFTWARE/LC02_SYSTEM_REQUIREMENTS/README.md`
- SysML Specification
- ReqIF Standard
- Portal Registry Specifications (ATA 99)
