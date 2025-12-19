# CA360º Portal Contract - Immutable File List for v1.1.0

**Purpose:** Defines the mandatory set of files that constitute the portal contract for release version 1.1.0

**Status:** ACTIVE  
**Version:** 1.1  
**Last Updated:** 2025-12-19

## Contract File Categories

### 1. Core Documentation (10 files)

Portal structure and governance documentation:

1. `CAXS/README.md` - Main portal overview and operation model
2. `CAXS/DIRECTORY_OVERVIEW.md` - Quick reference and navigation guide
3. `CAXS/AoR/README.md` - Area of Responsibility stakeholder documentation
4. `CAXS/KNOTS/README.md` - KNOTS execution model and closure criteria
5. `CAXS/LIFECYCLE/README.md` - Lifecycle phase definitions
6. `CAXS/OPT-INS/README.md` - OPT-INS axis definitions and ATA mappings
7. `CAXS/LEDGERS/README.md` - Ledger integration and traceability patterns
8. `CAXS/INFRASTRUCTURE/README.md` - Infrastructure components and validators
9. `CAXS/PROGRAMS/README.md` - AIRT and SPACET program documentation
10. `CAXS/ATA/README.md` - ATA chapter organization

### 2. Governance & Validation (6 files)

Portal governance, validation, and release management:

11. `CAXS/INFRASTRUCTURE/indexes/portal_entrypoints_index.md` - SSOT for all 14 AoR entry points and navigation patterns
12. `CAXS/INFRASTRUCTURE/validators/one_official_chain_uniqueness.md` - Explicit uniqueness key definition
13. `CAXS/INFRASTRUCTURE/validators/exceptions.yml` - Time-bounded exception registry
14. `CAXS/00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-portal-rc-protocol_DELIVERABLE_PROC_I01-R01_ACTIVE.md` - Release candidate protocol
15. `CAXS/00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-main-workflow-ssot_DELIVERABLE_PROC_I01-R01_ACTIVE.md` - Main execution workflow SSOT
16. `CAXS/REPORTS/validation/ca360_portal_validation_report.md` - Validation report template

### 3. Configuration Files (3 files)

v6.0 nomenclature configuration and constraints:

17. `configs/nomenclature/v6/vocabulary.json` - Controlled vocabulary for all v6.0 fields
18. `configs/nomenclature/v6/regex_constraints.json` - Regex patterns for v6.0 validation
19. `configs/nomenclature/v6/category_aor_constraints.json` - Category-AoR binding rules

### 4. CI/CD Automation (1 file)

Automated governance enforcement:

20. `.github/workflows/ca360_portal_gates.yml` - Portal gates CI workflow

### 5. AoR SSOT Templates (5 files)

Template pack for consistent AoR registry creation:

21. `CAXS/INFRASTRUCTURE/templates/aor_ssot_pack/README.md` - Template pack documentation
22. `CAXS/INFRASTRUCTURE/templates/aor_ssot_pack/roadmap_registry_template.md` - Roadmap registry template
23. `CAXS/INFRASTRUCTURE/templates/aor_ssot_pack/task_registry_template.md` - Task registry template
24. `CAXS/INFRASTRUCTURE/templates/aor_ssot_pack/evidence_index_template.md` - Evidence index template
25. `CAXS/INFRASTRUCTURE/templates/aor_ssot_pack/signoff_index_template.md` - Signoff index template

### 6. ONUP Template Pack (9 files)

Template pack for OPT-INS Node Uncertainty Pack (ONUP) creation:

26. `CAXS/INFRASTRUCTURE/templates/onup_pack/README.md` - ONUP template pack documentation
27. `CAXS/INFRASTRUCTURE/templates/onup_pack/onup_node_tasklist_idx_template.md` - Node tasklist index template
28. `CAXS/INFRASTRUCTURE/templates/onup_pack/onup_problem_statement_template.md` - Problem statement template
29. `CAXS/INFRASTRUCTURE/templates/onup_pack/onup_evidence_index_template.md` - Evidence index template
30. `CAXS/INFRASTRUCTURE/templates/onup_pack/onup_signoff_index_template.md` - Signoff index template
31. `CAXS/INFRASTRUCTURE/templates/onup_pack/onup_roadmap_registry_template.csv` - Roadmap registry CSV template
32. `CAXS/INFRASTRUCTURE/templates/onup_pack/onup_task_registry_template.csv` - Task registry CSV template
33. `CAXS/INFRASTRUCTURE/templates/onup_pack/onup_ata_impact_matrix_template.csv` - ATA impact matrix CSV template
34. `CAXS/INFRASTRUCTURE/templates/onup_pack/onup_aor_raci_template.csv` - AoR RACI CSV template

### 7. STK_CEGT Reference Implementation (6 files)

Operational registries for 14th stakeholder (reference for all AoRs):

35. `CAXS/AoR/STK_CEGT/roadmap_registry.md` - STK_CEGT roadmap tracking
36. `CAXS/AoR/STK_CEGT/task_registry.md` - STK_CEGT task execution
37. `CAXS/AoR/STK_CEGT/evidence_index.md` - STK_CEGT evidence cataloguing
38. `CAXS/AoR/STK_CEGT/signoff_index.md` - STK_CEGT signoff tracking
39. `CAXS/LEDGERS/85_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_80_LC09_K09_STK_CEGT__circularity-kpis_REGISTRY_IDX_I01-R01_ACTIVE.md` - Circularity KPI registry
40. `CAXS/LEDGERS/85_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_80_LC09_K09_STK_CEGT__esg-reporting_REGISTRY_IDX_I01-R01_ACTIVE.md` - ESG reporting index

### 8. Release Evidence (1 file)

Template for release evidence generation:

41. `CAXS/REPORTS/validation/release_evidence_pack_template.md` - Release evidence pack template

## Total Contract Files

**41 mandatory files** must be present and valid for v1.1.0 release.

## Validation Rules

### File Existence
All 41 files must exist at the specified paths. Missing files block release.

### File Integrity
For RELEASED versions, SHA256 hashes of all contract files are recorded in the release evidence pack.

### Link Integrity
All cross-references between contract files must resolve. Broken links block release.

### Configuration Validity
All JSON configuration files must parse correctly and contain required fields.

## Versioning

### MAJOR Version Change (2.0.0)
Triggers when:
- Contract files are removed or relocated
- Breaking changes to nomenclature format
- Structural reorganization of directories

### MINOR Version Change (1.1.0)
Triggers when:
- New contract files added
- Non-breaking additions to existing files
- New features or capabilities

### PATCH Version Change (1.0.1)
Triggers when:
- Bug fixes in existing files
- Documentation clarifications
- Typo corrections

## Exclusions from Contract

**The following are NOT part of the portal contract** (may change without version bump):

- Individual AoR directories (except STK_CEGT reference)
- ATA chapter subdirectories
- KNOTS, LIFECYCLE, BLOCKS, CATEGORIES subdirectories
- .gitkeep files
- STRUCTURE_VALIDATION.md (deprecated in favor of validation report)
- DIRECTORY_OVERVIEW.md non-normative sections

## RC Checklist Integration

For a release to proceed from RC to RELEASED:

- [ ] All 41 contract files present
- [ ] No files missing from contract list
- [ ] All JSON configs parse correctly
- [ ] All markdown links resolve
- [ ] SHA256 manifest generated
- [ ] Delta from previous version documented
- [ ] Stakeholder approvals obtained

## Modification Protocol

**To modify the contract file list:**

1. Propose changes in GitHub issue
2. Obtain STK_CM + STK_PMO approval
3. Update this file with rationale
4. Update release candidate protocol
5. Update CI gates if needed
6. Generate new release evidence pack
7. Increment portal version appropriately

## Version History

| Version | Date | Changes | Approver |
|---------|------|---------|----------|
| 1.0 | 2025-12-19 | Initial contract file list for v1.0.0 | STK_CM |
| 1.1 | 2025-12-19 | Added CA360º main workflow SSOT and ONUP template pack (9 files) | STK_CM |

## References

- **Release Candidate Protocol:** `CAXS/00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-portal-rc-protocol_DELIVERABLE_PROC_I01-R01_ACTIVE.md`
- **Main Workflow SSOT:** `CAXS/00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__ca360-main-workflow-ssot_DELIVERABLE_PROC_I01-R01_ACTIVE.md`
- **Validation Report:** `CAXS/REPORTS/validation/ca360_portal_validation_report.md`
- **Release Evidence Pack:** `CAXS/REPORTS/validation/release_evidence_pack_template.md`

---

**Document Status:** ACTIVE  
**Enforcement:** PR-blocking via CI gates  
**Authority:** STK_CM (Configuration Management)
