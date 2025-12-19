# CA360º Portal Entrypoints Index

**Document Type:** REGISTRY  
**Category:** Portal Navigation  
**Status:** ACTIVE  
**Version:** 1.0  
**Last Updated:** 2025-12-19

---

## Purpose

This index provides the single source of truth (SSOT) for all CA360º portal entry points and navigation patterns. It serves as the deterministic contract for portal automation and user navigation.

---

## Portal Entry Points (14 AoR Stakeholders)

| AoR | Path | Primary ATA | Primary Phases |
|-----|------|-------------|----------------|
| STK_CM | `AoR/STK_CM/` | 00, 11, 99 | LC06, LC10 |
| STK_PMO | `AoR/STK_PMO/` | 00, 01-05 | LC06, LC09, LC10, LC14 |
| STK_SE | `AoR/STK_SE/` | 00, 20, 40, 51 | LC02, LC03, LC04 |
| STK_DAB | `AoR/STK_DAB/` | 42, 46, 90-99 | LC01, LC03, LC05 |
| STK_PHM | `AoR/STK_PHM/` | 20, 29, 32, 51-57 | LC03, LC04, LC10, LC13 |
| STK_SAF | `AoR/STK_SAF/` | 04, 26 | LC07 |
| STK_CERT | `AoR/STK_CERT/` | All (oversight) | LC08 |
| STK_TEST | `AoR/STK_TEST/` | 100-116 | LC05, LC06 |
| STK_OPS | `AoR/STK_OPS/` | 01-05 | LC11, LC12 |
| STK_MRO | `AoR/STK_MRO/` | 05, 12 | LC12, LC13 |
| STK_AI | `AoR/STK_AI/` | 90, 96, 114 | LC01, LC03, LC05 |
| STK_CY | `AoR/STK_CY/` | 20, 42, 87 | LC07 |
| STK_SPACEPORT | `AoR/STK_SPACEPORT/` | 80-89 | LC11 |
| STK_CEGT | `AoR/STK_CEGT/` | 85 | LC09 |

---

## Navigation Patterns

### Pattern 1: By Role (AoR-based)
```
AoR/<STK>/ → roadmaps → tasks → evidence
```

### Pattern 2: By Domain (OPT-INS/ATA-based)
```
OPT-INS/<axis>/ → ATA/<chapter>/ → BLOCK/<segment>/ → work
```

### Pattern 3: By Lifecycle Phase
```
LIFECYCLE/<phase>/ → KNOT → execute → evidence → ledgers
```

### Pattern 4: By Program/Product
```
PROGRAMS/<program>/<family>/ → VARIANT → AoR/KNOT → work
```

---

## Infrastructure Locations (Deterministic Contract)

### Portal Governance Documents
- **Main Workflow SSOT:** `CAXS/00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-main-workflow-ssot_DELIVERABLE_PROC_I01-R01_ACTIVE.md`
- **RC Protocol:** `CAXS/00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-portal-rc-protocol_DELIVERABLE_PROC_I01-R01_ACTIVE.md`

### Configuration Files
- `configs/nomenclature/v6/vocabulary.json`
- `configs/nomenclature/v6/regex_constraints.json`
- `configs/nomenclature/v6/category_aor_constraints.json`

### Required Components
- **Validators:** `INFRASTRUCTURE/validators/`
- **Schemas:** `INFRASTRUCTURE/schemas/`
- **Templates:** `INFRASTRUCTURE/templates/`
  - `aor_ssot_pack/` - AoR registry templates
  - `onup_pack/` - Node Uncertainty Pack templates
- **Indexes:** `INFRASTRUCTURE/indexes/`
- **Reports:** `REPORTS/validation/`

### Ledger Locations
- `LEDGERS/knowledge-ledger/`
- `LEDGERS/traceability-graph/`
- `LEDGERS/digital-product-passport/`
- `LEDGERS/sbom-bom/`
- `LEDGERS/release-packs/`
- `LEDGERS/master-registers/`

---

## Gate Validation Rules (PR-Blocking)

1. **Filename validation:** v6.0 nomenclature regex compliance
2. **AoR validation:** Must match allowlist (14 stakeholders including STK_CEGT)
3. **Category-AoR constraints:** SIGNOFF/EXPORT_CONTROL → STK_CM or STK_CERT only
4. **KNOT range:** K01-K14 only
5. **One official chain:** DELIVERABLE ≤1 ACTIVE/RELEASED per scope (see uniqueness key definition)
6. **.gitkeep presence:** All empty leaf directories

**One Official Chain Details:** See `CAXS/INFRASTRUCTURE/validators/one_official_chain_uniqueness.md`

**Exceptions Mechanism:** `CAXS/INFRASTRUCTURE/validators/exceptions.yml`

**CI Enforcement:** `.github/workflows/ca360_portal_gates.yml`

---

## v6.0 Nomenclature (Canonical)

```
[ATA]_[PROJECT]_[PROGRAM]_[FAMILY]_[VARIANT]_[VERSION]_[MODEL]_[BLOCK]_[PHASE]_[KNOT]_[AoR]__[SUBJECT]_[CATEGORY]_[TYPE]_[ISSUE-REV]_[STATUS].[EXT]
```

**Note:** PROJECT field is mandatory (always AMPEL360)

---

## Version Control

**Index Version:** 1.0  
**Last Validation:** 2025-12-19  
**Configuration:** configs/nomenclature/v6/
