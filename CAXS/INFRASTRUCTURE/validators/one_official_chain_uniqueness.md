# One Official Chain - Uniqueness Key Definition

## Purpose

This document defines the **explicit uniqueness key** for enforcing the "one official chain" rule for `CATEGORY=DELIVERABLE` artifacts in the CA360º portal.

## Uniqueness Key Definition

### Product Governance Key (PGK)

The **Product Governance Key (PGK)** defines the scope within which uniqueness is evaluated:

```
PGK = (ATA, PROJECT, PROGRAM, FAMILY, VARIANT, VERSION, MODEL, BLOCK, PHASE)
```

### Uniqueness Constraint

For artifacts with `CATEGORY=DELIVERABLE`, the following constraint is **enforced**:

```
UniqueKey = (PGK, AoR, SUBJECT, CATEGORY, TYPE)
COUNT(status ∈ {ACTIVE, RELEASED}) ≤ 1
```

**Translation:**
- Within a given PGK scope
- For a specific combination of (AoR, SUBJECT, CATEGORY, TYPE)
- There can be **at most one** artifact with status ACTIVE or RELEASED

## Examples

### Valid Scenario
```
Artifact 1: 42_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_20_LC03_K03_STK_DAB__ima-architecture_DELIVERABLE_SPEC_I01-R01_ACTIVE.md
Artifact 2: 42_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_20_LC03_K03_STK_DAB__ima-architecture_DELIVERABLE_SPEC_I01-R02_DRAFT.md
```
**Status:** ✅ VALID - Only one ACTIVE/RELEASED artifact for this UniqueKey

### Invalid Scenario
```
Artifact 1: 42_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_20_LC03_K03_STK_DAB__ima-architecture_DELIVERABLE_SPEC_I01-R01_ACTIVE.md
Artifact 2: 42_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_20_LC03_K03_STK_DAB__ima-architecture_DELIVERABLE_SPEC_I02-R01_ACTIVE.md
```
**Status:** ✗ INVALID - Two ACTIVE artifacts with same UniqueKey (violates one official chain)

## Enforcement

### PR-Blocking Gate

The validator checks:
1. Extract PGK + (AoR, SUBJECT, CATEGORY, TYPE) from all DELIVERABLE artifacts
2. Group by UniqueKey
3. Count artifacts with status ∈ {ACTIVE, RELEASED}
4. FAIL if count > 1

### Exception Mechanism

Exceptions to the one official chain rule must be:
- Registered in `CAXS/INFRASTRUCTURE/validators/exceptions.yml`
- Time-bounded with `expires_on` date
- Approved by STK_CM with evidence reference
- Automatically enforced by CI (fails if expired)

## Edge Cases

### Different PGK Scopes
```
Artifact 1: 42_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_20_LC03_K03_STK_DAB__ima-architecture_DELIVERABLE_SPEC_I01-R01_ACTIVE.md
Artifact 2: 42_AMPEL360_AIRT_Q100_BASELINE_PLUS_HW_20_LC03_K03_STK_DAB__ima-architecture_DELIVERABLE_SPEC_I01-R01_ACTIVE.md
```
**Status:** ✅ VALID - Different PROGRAM (SPACET vs AIRT) = different PGK

### Different AoR
```
Artifact 1: 42_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_20_LC03_K03_STK_DAB__ima-architecture_DELIVERABLE_SPEC_I01-R01_ACTIVE.md
Artifact 2: 42_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_20_LC03_K03_STK_SE__ima-architecture_DELIVERABLE_SPEC_I01-R01_ACTIVE.md
```
**Status:** ✅ VALID - Different AoR (STK_DAB vs STK_SE) = different UniqueKey

### Different SUBJECT
```
Artifact 1: 42_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_20_LC03_K03_STK_DAB__ima-architecture_DELIVERABLE_SPEC_I01-R01_ACTIVE.md
Artifact 2: 42_AMPEL360_SPACET_Q10_BASELINE_PLUS_HW_20_LC03_K03_STK_DAB__ima-implementation_DELIVERABLE_SPEC_I01-R01_ACTIVE.md
```
**Status:** ✅ VALID - Different SUBJECT (ima-architecture vs ima-implementation) = different UniqueKey

## Supersession Workflow

To supersede an existing DELIVERABLE:

1. Current artifact status: ACTIVE or RELEASED
2. Create new revision with status: DRAFT
3. Complete review and approval
4. **Atomically** (in same commit):
   - Change old artifact status: ACTIVE → SUPERSEDED
   - Change new artifact status: DRAFT → ACTIVE
5. This maintains count ≤ 1 throughout

## Audit Queries

Validators must support queries:

```sql
-- Find potential violations
SELECT PGK, AoR, SUBJECT, CATEGORY, TYPE, COUNT(*) as active_count
FROM artifacts
WHERE CATEGORY = 'DELIVERABLE' 
  AND status IN ('ACTIVE', 'RELEASED')
GROUP BY PGK, AoR, SUBJECT, CATEGORY, TYPE
HAVING COUNT(*) > 1
```

## Configuration References

- **Vocabulary:** `configs/nomenclature/v6/vocabulary.json`
- **Regex:** `configs/nomenclature/v6/regex_constraints.json`
- **Constraints:** `configs/nomenclature/v6/category_aor_constraints.json`
- **Exceptions:** `CAXS/INFRASTRUCTURE/validators/exceptions.yml`

## Version

**Document Version:** 1.0  
**Last Updated:** 2025-12-19  
**Enforcement:** PR-blocking in CI
