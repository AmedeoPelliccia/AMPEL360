# IDS/ — ID Generation, Resolution, and Linking Utilities

**Location:** `LC00_GENERAL/IDS/`  
**Owner (AoR):** STK_DAB (Digital Applications & Blockchains)  
**Status:** ACTIVE

---

## Purpose

This directory contains **ID generation, resolution, and linking utilities** that ensure stable, unique, and traceable identifiers across the AMPEL360 system.

## Scope

### What belongs here:
- **ID generators** for artifacts, requirements, models, evidence
- **ID resolvers** for cross-referencing and link validation
- **Linking utilities** for establishing trace relationships
- **Hash utilities** for content-addressable identifiers (SHA256)
- **Link checkers** for verifying ID references and integrity
- **Provenance utilities** for tracking artifact lineage

### What does NOT belong here:
- Schemas (place in SCHEMAS/)
- Vocabularies (place in VOCAB/)
- General libraries (place in LIB/)
- Test fixtures (place in FIXTURES/)

---

## Guidelines

1. **Uniqueness**: All IDs must be globally unique within the system
2. **Stability**: IDs should be deterministic and reproducible when possible
3. **Traceability**: IDs must support audit trail and provenance tracking
4. **Resolution**: All ID references must be resolvable to concrete artifacts
5. **Integrity**: Use content hashing (SHA256) for immutable references

---

## Expected Utilities

Key utilities that should be developed here:

- **Artifact ID Generator**: Generate stable IDs for artifacts
- **Requirement ID Generator**: Generate requirement identifiers (REQ-###)
- **Evidence ID Generator**: Generate evidence identifiers (EVD-###)
- **Link Resolver**: Resolve ID references to file paths or URIs
- **Hash Generator**: Generate SHA256 hashes for content addressing
- **Link Checker**: Validate that all ID references resolve correctly
- **Provenance Tracker**: Track artifact creation and modification history

---

## ID Schemes

Common ID patterns used in AMPEL360:

### Filename-based IDs
Constructed from v6.0 nomenclature:
```
[ATA]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT]_[AoR]__[SUBJECT]_[CATEGORY]_[TYPE]_[ISSUE-REV]_[STATUS].[EXT]
```

### Semantic IDs
Purpose-specific identifier schemes:
- **REQ-###-###**: Requirements (system-subsystem)
- **EVD-###-###**: Evidence records
- **KNOT-K##-T###**: KNOT tasks
- **CIPP-###**: Certainty Integration Pointers
- **VSN-###**: Vision identifiers
- **MSN-###**: Mission identifiers
- **OUT-###-###**: Outcome identifiers

### Content-Addressable IDs
Hash-based identifiers:
- **sha256**: File content hashing for immutable references
- **git commit**: Git commit SHAs for version control

---

## Utility Organization

```
IDS/
├── generators/
│   ├── artifact_id.py
│   ├── requirement_id.py
│   ├── evidence_id.py
│   └── hash_generator.py
├── resolvers/
│   ├── link_resolver.py
│   ├── path_resolver.py
│   └── uri_resolver.py
├── validators/
│   ├── link_checker.py
│   ├── reference_validator.py
│   └── integrity_checker.py
└── provenance/
    ├── provenance_tracker.py
    └── lineage_builder.py
```

---

## Usage

ID utilities provide stable identification:

```python
# Example Python usage
from LC00_GENERAL.IDS.generators import artifact_id, hash_generator
from LC00_GENERAL.IDS.resolvers import link_resolver

# Generate artifact ID
aid = artifact_id.generate(
    ata='00',
    program='SPACET',
    family='Q10',
    subject='test-artifact'
)

# Generate content hash
file_hash = hash_generator.sha256_file('artifact.md')

# Resolve link
path = link_resolver.resolve('REQ-001-001')
```

---

## Maintenance

- Ensure ID generation is deterministic and reproducible
- Maintain backwards compatibility for ID schemes
- Update link checkers when new ID patterns are introduced
- Coordinate with STK_CM for configuration control
- Register ID schemes in ATA 93 (Traceability Graph)

---

**References:**
- See parent README: `../README.md`
- ATA 93: Traceability Graph (REQ↔DESIGN↔VV↔OPS) & Evidence Ledgers
- ATA 94: DPP Core (Digital Product Passport) & Provenance
- Nomenclature Standard: Main README Section 10
