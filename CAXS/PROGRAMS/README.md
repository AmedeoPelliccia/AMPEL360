# PROGRAMS — AIRT and SPACET Product Lines

## Overview

The **PROGRAMS** directory organizes work by the two primary AMPEL360 programs: **AIRT** (Advanced Air Transport) and **SPACET** (Space Transport).

---

## Program Structure

### AIRT — Advanced Air Transport
**Path:** `AIRT/`

**Description:** Advanced Air Transport systems for atmospheric flight

**Families:**
- **Q100-PLUS** — BWB H₂-Electric Aircraft (INTEGRA)
- **Q200LR-PLUSULTRA** — Long-Range Advanced Variant

**Key Characteristics:**
- Blended Wing Body (BWB) configuration
- Hydrogen-electric propulsion
- Advanced atmospheric operations
- Commercial transport focus

**Primary ATA Domains:**
- Airframe (T-AXIS: ATA 20-79)
- Flight controls (ATA 27)
- Propulsion (ATA 70-79)
- Environmental control (ATA 21)

---

### SPACET — Space Transport
**Path:** `SPACET/`

**Description:** Space Transport systems for beyond-atmosphere operations

**Families:**
- **Q10-PLUS** — Space Transport Baseline
- **QHABITAT-PLUSULTRA** — Habitat-Class Space Vehicle

**Key Characteristics:**
- Space-rated systems
- Habitat capabilities
- Launch and re-entry operations
- Extended mission duration

**Primary ATA Domains:**
- Spaceport infrastructure (I-AXIS: ATA 80-89)
- Life support (ATA 35, 38)
- Thermal protection (ATA 30)
- Qualification testing (S-AXIS: ATA 110)

---

## Product Line Matrix (CM-Controlled)

| PROGRAM | VERSION | FAMILY | Description |
|---------|---------|--------|-------------|
| AIRT | PLUS | Q100 | BWB H₂-electric aircraft (INTEGRA) |
| AIRT | PLUSULTRA | Q200LR | Long-range advanced variant |
| SPACET | PLUS | Q10 | Space transport baseline |
| SPACET | PLUSULTRA | QHABITAT | Habitat-class space vehicle |

**Note:** This matrix is configuration-controlled. New families require CM approval.

---

## VERSION Tiers

### PLUS
**Description:** Baseline/foundational tier

**Characteristics:**
- Core capabilities
- Standard configurations
- Foundation for derivatives

### PLUSULTRA
**Description:** Advanced/extended tier

**Characteristics:**
- Enhanced capabilities
- Extended range/duration
- Advanced features

---

## Directory Organization

Each program contains:

```
PROGRAMS/
├── AIRT/
│   ├── Q100-PLUS/
│   │   ├── requirements/
│   │   ├── design/
│   │   ├── analysis/
│   │   ├── testing/
│   │   └── operations/
│   └── Q200LR-PLUSULTRA/
│       └── (same structure)
└── SPACET/
    ├── Q10-PLUS/
    │   └── (same structure)
    └── QHABITAT-PLUSULTRA/
        └── (same structure)
```

---

## Usage Guidelines

### For Program-Specific Work

1. **Identify program** (AIRT or SPACET)
2. **Select family** (Q100, Q200LR, Q10, QHABITAT)
3. **Identify version tier** (PLUS or PLUSULTRA)
4. **Navigate to appropriate subdirectory**
5. **Follow v6.0 nomenclature** including PROGRAM and FAMILY fields
6. **Align with ATA chapters** appropriate to program

### For Cross-Program Work

When developing common elements:
- **Document applicability** (AIRT+SPACET)
- **Use VARIANT=GEN** for generic/common artifacts
- **Reference ATA_PARTITION_MATRIX.yaml** for chapter applicability
- **Create program-specific addenda** when needed

---

## ATA Chapter Applicability

### Common to Both (AIRT+SPACET)

Most ATA chapters apply to both programs with potential addenda:

- **ATA 00** — General (common)
- **ATA 20-79** — On-board systems (mostly common)
- **ATA 90-99** — Neural networks/ledgers (common)
- **ATA 100-116** — SIM/TEST (common)

### AIRT-Specific

Some chapters are primarily AIRT:

- **ATA 09** — Towing/Taxiing (ground operations)
- **ATA 27** — Flight Controls (atmospheric flight)
- **ATA 60-69** — Propeller/Rotor family (if applicable)

### SPACET-Specific

Some chapters are primarily SPACET:

- **ATA 84** — Spaceport Safety/Emergency
- **ATA 110** — Qualification/Environmental Testing

**Refer to ATA_PARTITION_MATRIX.yaml for detailed applicability.**

---

## Program×Version→Family Validation

The **nomenclature validator** enforces the valid combinations:

- `AIRT + PLUS → Q100` ✓
- `AIRT + PLUSULTRA → Q200LR` ✓
- `SPACET + PLUS → Q10` ✓
- `SPACET + PLUSULTRA → QHABITAT` ✓
- Any other combination → ✗ (validator error)

---

## Variant Context

Within each program/family, work is further organized by VARIANT:

- **GEN** — General/generic configurations
- **BASELINE** — Configuration baselines
- **FLIGHT_TEST** — Flight test specific
- **CERT** — Certification specific
- **MSN** — Mission-specific (numbered)
- **CUST** — Customer-specific

---

## Integration with Framework

Programs integrate with:

- **AoR** — Each program has designated AoR leads
- **OPT-INS** — Programs span all six axes
- **KNOTS** — All KNOTs apply to programs
- **LIFECYCLE** — All phases apply (LC01-LC14)
- **BLOCKS** — All blocks apply with program-specific emphasis
- **LEDGERS** — Program artifacts registered in ledgers

---

## Program Governance

- **Program codes are fixed** — AIRT, SPACET only
- **Family codes are CM-controlled** — Q100, Q200LR, Q10, QHABITAT
- **Version tiers are fixed** — PLUS, PLUSULTRA only
- **Program×Version×Family matrix is validated** — Enforced by validators
- **New families require CM approval** — Standard upgrade process

---

## Roadmap Alignment

Program roadmaps:
- Are **program-specific** initially
- May have **cross-program dependencies**
- Are tracked in **ROADMAPS/active/**
- Reference **program/family** in scope
- Produce **program-specific artifacts**

---

## Version

**Programs Structure Version:** 1.0  
**Last Updated:** 2025-12-19

---

## References

- [CAXS Main README](../README.md)
- [Product Line Matrix (Main README)](../../README.md#2-product-line-matrix)
- [PROGRAM×VERSION→FAMILY Matrix (Main README)](../../README.md#926-program--version--family-matrix-cm-controlled)
- [ATA Partition Matrix](../../ATA_PARTITION_MATRIX.yaml)
