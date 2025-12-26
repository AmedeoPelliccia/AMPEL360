# SCHEMAS/ — Cross-Phase JSON/YAML Schemas

**Location:** `LC00_GENERAL/SCHEMAS/`  
**Owner (AoR):** STK_DAB (Digital Applications & Blockchains)  
**Status:** ACTIVE

---

## Purpose

This directory contains **canonical JSON/YAML schemas** that define the structure of artifacts, records, and data interchange formats used across all lifecycle phases (LC01–LC14).

## Scope

### What belongs here:
- **Canonical record schemas** (requirements, models, evidence, etc.)
- **JSON Schema** definitions for structured data validation
- **YAML schemas** for configuration and metadata files
- **Data interchange formats** used between phase tools
- **API schemas** for portal and service integrations
- **Cross-phase artifact structures** (common shapes)

### What does NOT belong here:
- Phase-specific schemas (place in relevant LCxx directory)
- Configuration files (place in VOCAB/ or root config)
- Schema validators (place in LIB/ or VOCAB/)
- Test data (place in FIXTURES/)

---

## Guidelines

1. **Versioning**: All schemas must be versioned (e.g., `v1.0`, `v2.0`)
2. **Documentation**: Each schema must include purpose, fields, constraints, and examples
3. **Validation**: Schemas must be machine-validatable (JSON Schema, YAML Schema)
4. **Stability**: Changes to schemas require impact analysis and migration plan
5. **References**: Use `$ref` for reusable schema components

---

## Expected Schemas

Common schemas that should be defined here:

- **Artifact Metadata Schema**: Common metadata for all artifacts
- **Requirement Record Schema**: Structure for requirement definitions
- **Evidence Record Schema**: Structure for evidence and proof artifacts
- **Traceability Link Schema**: Structure for trace relationships
- **Configuration Schema**: Common configuration format for tools
- **Manifest Schema**: Structure for release and export manifests
- **Provenance Schema**: Structure for audit and provenance records

---

## Schema Organization

Organize schemas by type:

```
SCHEMAS/
├── artifact/
│   ├── metadata_v1.0.json
│   └── identifier_v1.0.json
├── requirement/
│   ├── requirement_record_v1.0.yaml
│   └── allocation_v1.0.yaml
├── evidence/
│   ├── evidence_record_v1.0.json
│   └── closure_v1.0.json
├── traceability/
│   ├── link_v1.0.json
│   └── graph_v1.0.json
└── portal/
    ├── config_v1.0.yaml
    └── manifest_v1.0.json
```

---

## Usage

Schemas are used for validation:

```python
# Example Python usage
from jsonschema import validate
import json

# Load schema
with open('SCHEMAS/requirement/requirement_record_v1.0.json') as f:
    schema = json.load(f)

# Validate data
validate(instance=requirement_data, schema=schema)
```

---

## Maintenance

- Version schemas using semantic versioning
- Document breaking changes in migration guide
- Maintain backwards compatibility when possible
- Coordinate schema changes with all consuming tools
- Register schemas in ATA 91 (Data Schemas / Ontologies)

---

**References:**
- See parent README: `../README.md`
- ATA 91: Data Schemas / Ontologies / Semantic Model (SSOT)
- ATA 99: Master Registers (Golden Records) & Reference Datasets
- Nomenclature Standard: Main README Section 10
