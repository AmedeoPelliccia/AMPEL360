# VOCAB/ — Controlled Vocabulary Dictionaries and Loaders

**Location:** `LC00_GENERAL/VOCAB/`  
**Owner (AoR):** STK_CM (Configuration Management) / STK_DAB  
**Status:** ACTIVE

---

## Purpose

This directory contains **controlled vocabulary dictionaries** and **loaders** that enforce consistent terminology and nomenclature across the AMPEL360 system.

## Scope

### What belongs here:
- **Controlled vocabulary dictionaries** (AoR, KNOT, PHASE, BLOCK, STATUS, etc.)
- **Vocabulary loaders** and parsers
- **Token validators** for v6.0 nomenclature
- **Allowlists** for controlled fields (ATA, TYPE, CATEGORY, EXT)
- **Terminology mappings** and cross-references
- **Vocabulary checkers** and enforcement tools

### What does NOT belong here:
- Schemas (place in SCHEMAS/)
- General-purpose libraries (place in LIB/)
- Test fixtures (place in FIXTURES/)
- Configuration files (unless vocabulary-specific)

---

## Guidelines

1. **Single Source of Truth**: Vocabularies here are SSOT for allowed values
2. **Versioning**: Vocabulary changes must be versioned and controlled
3. **Validation**: All vocabularies must be machine-readable and validatable
4. **Documentation**: Each vocabulary must document purpose, values, and usage
5. **CM Control**: Changes require STK_CM approval and impact analysis

---

## Expected Vocabularies

Key vocabularies that should be maintained here:

- **AoR Allowlist**: STK_CM, STK_PMO, STK_SE, STK_DAB, etc.
- **KNOT IDs**: K01..K14 with descriptions
- **PHASE Tokens**: LC01..LC14 lifecycle phases
- **BLOCK Tokens**: 00..90 domain segmentation
- **STATUS Values**: DRAFT, ACTIVE, RELEASED, SUPERSEDED, OBSOLETE
- **CATEGORY Values**: DELIVERABLE, EVIDENCE, REGISTRY, SIGNOFF, etc.
- **TYPE Allowlist**: STD, POL, PROC, PLAN, REQ, SPEC, etc.
- **ATA Chapters**: 00..116 with descriptions
- **MODEL Tokens**: BB, HW, SW, PR
- **VARIANT Tokens**: GEN, BASELINE, FLIGHT_TEST, CERT, MSN, CUST
- **VERSION Tokens**: PLUS, PLUSULTRA
- **FAMILY Tokens**: Q100, Q200LR, Q10, QHABITAT
- **PROGRAM Tokens**: AIRT, SPACET

---

## Vocabulary Organization

Organize vocabularies by domain:

```
VOCAB/
├── nomenclature/
│   ├── aor_allowlist.yaml
│   ├── knot_ids.yaml
│   ├── phase_tokens.yaml
│   ├── block_tokens.yaml
│   └── status_values.yaml
├── categorization/
│   ├── category_values.yaml
│   ├── type_allowlist.yaml
│   └── ext_allowlist.yaml
├── hierarchy/
│   ├── ata_chapters.yaml
│   ├── program_family_matrix.yaml
│   └── variant_version_tokens.yaml
└── loaders/
    ├── vocab_loader.py
    ├── validator.py
    └── checker.py
```

---

## Usage

Vocabulary loaders provide validation:

```python
# Example Python usage
from LC00_GENERAL.VOCAB.loaders import vocab_loader, validator

# Load AoR allowlist
aor_list = vocab_loader.load_aor_allowlist()

# Validate AoR token
is_valid = validator.validate_aor('STK_CM')  # Returns True

# Validate full filename
validator.validate_filename(
    '00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__test_DELIVERABLE_STD_I01-R01_ACTIVE.md'
)
```

---

## Maintenance

- All vocabulary changes require PR with impact analysis
- Coordinate with STK_CM for configuration control
- Update dependent validators when vocabularies change
- Maintain changelog for vocabulary updates
- Register vocabularies in ATA 99 (Master Registers)

---

**References:**
- See parent README: `../README.md`
- Nomenclature Standard: Main README Section 10.2
- ATA 99: Master Registers (Golden Records) & Reference Datasets
- v6.0 Controlled Vocabulary: Main README Section 10.2
