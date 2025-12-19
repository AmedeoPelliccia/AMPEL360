# CA360º Portal Release Candidate Protocol

**Document Type:** GOVERNANCE  
**Status:** ACTIVE  
**Version:** 1.0  
**Last Updated:** 2025-12-19

## Purpose

This protocol defines the process for treating the CA360º portal contract itself as a product, with explicit release criteria and status management.

## Portal Status Lifecycle

### STATUS=DRAFT
**Definition:** Portal structure is under active development  
**Allowed Changes:** Breaking changes, structural reorganization, new features  
**Testing:** Development testing only  
**Validation:** Optional

### STATUS=ACTIVE
**Definition:** Portal structure is operational but subject to iteration  
**Allowed Changes:** Non-breaking additions, documentation updates, refinements  
**Testing:** Required for structural changes  
**Validation:** Gates must pass, exceptions documented

### STATUS=RELEASED
**Definition:** Portal structure is stable and production-ready  
**Allowed Changes:** Bug fixes only, no structural changes  
**Testing:** Full validation required  
**Validation:** All gates PASS, all exceptions resolved or time-bounded, validation report generated and committed

### STATUS=SUPERSEDED
**Definition:** Portal structure has been replaced by newer version  
**Allowed Changes:** None (read-only)  
**Testing:** N/A  
**Validation:** Historical record only

## Release Candidate (RC) Criteria

A portal structure becomes a Release Candidate when:

### 1. Gates Pass (PR-Blocking)
✅ All 6 portal gates must pass:
- Filename validation (v6.0 with PROJECT)
- AoR validation (14 stakeholders)
- Category-AoR constraints
- KNOT range (K01-K14)
- One official chain mechanism
- .gitkeep presence

**Verification:** CI workflow `.github/workflows/ca360_portal_gates.yml` passes

### 2. SSOT Index Links Resolve
✅ Portal entrypoints index must have valid references:
- All 14 AoR directories exist
- All configuration files present and valid
- All infrastructure components documented
- All ledger locations defined

**Verification:** Linkcheck in CI passes

### 3. Exceptions Managed
✅ Exception registry state is valid:
- Empty (no exceptions), OR
- All exceptions are time-bounded with future expiry dates
- All exceptions have valid owner and approval references

**Verification:** `CAXS/INFRASTRUCTURE/validators/exceptions.yml` validates

### 4. Validation Report Generated
✅ Portal validation report must exist and show PASS:
- `CAXS/REPORTS/validation/ca360_portal_validation_report.md` exists
- Report shows all components present
- Report committed as evidence

**Verification:** Report file exists with passing status

### 5. Documentation Complete
✅ All required README files present:
- Root CAXS README
- AoR README with 14 stakeholders
- KNOTS README
- LIFECYCLE README
- OPT-INS README
- LEDGERS README
- INFRASTRUCTURE README
- PROGRAMS README
- Portal entrypoints index
- Validation report

**Verification:** 10+ README files present

### 6. Configuration Complete
✅ All v6.0 configuration files valid:
- `configs/nomenclature/v6/vocabulary.json`
- `configs/nomenclature/v6/regex_constraints.json`
- `configs/nomenclature/v6/category_aor_constraints.json`

**Verification:** JSON files parse and contain required fields

## Release Process

### Phase 1: Preparation
1. Ensure current status is STATUS=ACTIVE
2. Run all gates in CI
3. Fix any failures
4. Document remaining exceptions (if any)
5. Update all README files to reflect current state

### Phase 2: Release Candidate
1. Create RC tag: `vX.Y.Z-rc.N` (e.g., v1.0.0-rc.1)
2. Run full validation suite
3. Generate validation report
4. Commit validation report as evidence
5. Create release notes documenting:
   - New features/changes since last release
   - Breaking changes
   - Migration guide (if applicable)
   - Known limitations

### Phase 3: Review Period
1. Minimum 7-day review period for RC
2. Stakeholder sign-off required:
   - STK_CM (configuration management)
   - STK_PMO (program governance)
   - STK_DAB (automation/infrastructure)
3. Address feedback and create new RC if needed

### Phase 4: Release
1. All RC criteria confirmed PASS
2. All stakeholder approvals obtained
3. Create final tag: `vX.Y.Z`
4. Update STATUS to RELEASED
5. Archive release package:
   - Portal structure snapshot
   - Configuration files
   - Validation report
   - Approval evidence
   - Release notes

### Phase 5: Communication
1. Publish release announcement
2. Update documentation index
3. Notify all stakeholders
4. Archive previous RELEASED version as SUPERSEDED

## Versioning Scheme

**Format:** `MAJOR.MINOR.PATCH`

- **MAJOR:** Breaking changes to directory structure or naming conventions
- **MINOR:** New features (new directories, new configurations) without breaking changes
- **PATCH:** Bug fixes, documentation updates, non-structural improvements

**Examples:**
- `1.0.0`: Initial RELEASED version
- `1.1.0`: Added new AoR stakeholder (STK_CEGT)
- `1.1.1`: Fixed documentation errors
- `2.0.0`: Breaking change to v6.0 nomenclature format

## Current Status

**Portal Version:** 1.0.0-rc.1 (Release Candidate 1)  
**Status:** ACTIVE (not yet RELEASED)  
**Target Release:** 2026-Q1  

### RC.1 Checklist
- [x] Gates implemented
- [x] 14 AoR stakeholders present (including STK_CEGT)
- [x] Configuration files created
- [x] Portal entrypoints index published
- [x] Validation report template created
- [x] One official chain mechanism defined
- [x] Exceptions mechanism established
- [ ] All gates pass in CI (pending first run)
- [ ] Stakeholder review complete
- [ ] Validation report evidence committed
- [ ] Approval signoffs obtained

## Artifact Naming for Portal Itself

Portal release artifacts follow v6.0 nomenclature:

```
00_AMPEL360_<PROGRAM>_<FAMILY>_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-portal_REGISTRY_IDX_I<XX>-R<YY>_<STATUS>.md
```

**Example:**
```
00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-portal-v1-0-0_REGISTRY_IDX_I01-R01_RELEASED.md
```

## Maintenance After Release

### Allowed Changes (STATUS=RELEASED)
- Bug fixes (typos, broken links)
- Documentation clarifications
- Security patches
- .gitkeep additions for new empty directories

### NOT Allowed (STATUS=RELEASED)
- New directory structures
- Breaking changes to nomenclature
- Removal of existing directories
- Changes to configuration schemas

For significant changes, create new MAJOR or MINOR version.

## Exception: Hotfix Process

Critical issues in RELEASED version:

1. Create hotfix branch from release tag
2. Fix issue with minimal change
3. Create new PATCH version: vX.Y.Z+1
4. Fast-track review (48 hours)
5. Release with hotfix tag

## Governance

**Release Authority:** STK_CM  
**Technical Review:** STK_DAB  
**Strategic Approval:** STK_PMO  
**Quality Gate:** All portal gates + stakeholder signoffs

## References

- **Portal Gates CI:** `.github/workflows/ca360_portal_gates.yml`
- **Validation Report:** `CAXS/REPORTS/validation/ca360_portal_validation_report.md`
- **Exceptions Registry:** `CAXS/INFRASTRUCTURE/validators/exceptions.yml`
- **Portal Entrypoints:** `CAXS/INFRASTRUCTURE/indexes/portal_entrypoints_index.md`

## Version Control

**Protocol Version:** 1.0  
**Last Updated:** 2025-12-19  
**Next Review:** Upon each portal release
