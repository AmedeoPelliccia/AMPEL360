# MODEL_SOFTWARE — Lifecycle-Organized Software Artifacts

This directory organizes software artifacts, automation tooling, and process scripts across all AMPEL360 lifecycle phases. Each subdirectory corresponds to a specific lifecycle phase and contains software models (MODEL=SW) aligned with the v6.0 nomenclature standard.

## Directory Structure

```
MODEL_SOFTWARE/
├── LC00_GENERAL/                                              # Cross-phase utilities
├── LC01_PROBLEM_STATEMENT_GENERATION_PROMPTING_ENGINEERING/   # Problem framing tools
├── LC02_SYSTEM_REQUIREMENTS/                                  # Requirements management
├── LC03_DESIGN_MODELS/                                        # Architecture & design tools
├── LC04_ENGINEERING_ANALYSIS_AND_CALCULATION_MODELS/          # Analysis software
├── LC05_INTEGRATION_TESTING_AND_PROTOTYPING_VV_V6V/          # Test & integration tools
├── LC06_QUALITY/                                              # QMS & quality tools
├── LC07_SAFETY_AND_SECURITY/                                  # Safety & security tools
├── LC08_CERTIFICATION_AND_FIRST_FLIGHT/                       # Certification tools
├── LC09_GREEN_AIRCRAFT_BASELINES/                             # Sustainability tools
├── LC10_INDUSTRIALIZATION_SERIALIZATION_PRODUCTION_PLAN_CM/   # Production tools
├── LC11_OPERATIONS/                                           # Operational tools
├── LC12_SUPPORT_AND_SERVICES/                                 # Support tools
├── LC13_MRO_AND_SUSTAINMENT/                                  # Maintenance tools
└── LC14_RETIREMENT_MANAGEMENT_AND_CIRCULARITY/                # End-of-life tools
```

## Purpose

Each directory contains:
- **Scripts and tools** specific to that lifecycle phase
- **Validators and generators** for phase-specific artifacts
- **Automation software** supporting KNOT (K01..K14) framework tasks
- **Process utilities** aligned with AoR responsibilities

## Naming Convention

All software artifacts in this directory tree follow the **v6.0 nomenclature standard** with:
- `MODEL=SW` token
- Appropriate `PHASE` token (LC01..LC14)
- Proper `KNOT` binding (K01..K14)
- Full compliance with controlled vocabulary (Section 10.2 of main README)

## Usage Guidelines

1. **Cross-phase artifacts**: Place in `LC00_GENERAL/`
2. **Phase-specific tools**: Place in the corresponding `LC##_*/` directory
3. **Configuration control**: All artifacts must be version-tracked
4. **Traceability**: Software must link to requirements and evidence
5. **KNOT alignment**: Tools should support uncertainty resolution tasks

## References

- **Main README**: See Section 11 for detailed phase descriptions
- **Nomenclature Standard**: See Section 10 of main README (v6.0)
- **Lifecycle Phases**: See Section 10.2.8 of main README
- **KNOTS Framework**: See Section 7 of main README

---

**Owner (AoR)**: STK_DAB (Digital Applications & Blockchains)  
**Status**: ACTIVE  
**Issue-Rev**: I01-R01
