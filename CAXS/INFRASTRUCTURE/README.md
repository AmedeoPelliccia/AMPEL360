# INFRASTRUCTURE — Supporting Tools and Systems

## Overview

The **INFRASTRUCTURE** directory contains supporting tools, systems, and configurations that enable the CAXS Portal (CA360º) to function as a deterministic, validated, and auditable execution platform.

---

## Infrastructure Components

### templates
**Path:** `templates/`

**Description:** Artifact templates aligned to v6.0 nomenclature

**Contents:**
- Document templates for all TYPE categories
- SysML model templates
- Evidence bundle templates
- Roadmap templates
- Task templates aligned to KNOTs
- Release pack templates

**Primary AoR:** STK_CM, STK_DAB

**Key Features:**
- v6.0 nomenclature pre-filled
- Required fields marked
- Validation placeholders
- Trace link sections
- Evidence requirements
- Approval workflows

---

### validators
**Path:** `validators/`

**Description:** PLC validators (nomenclature, identifiers, schema integrity)

**Contents:**
- Nomenclature validators (v6.0 enforcement)
- Identifier validators (ATA, KNOT, AoR, etc.)
- Schema validators (JSON/YAML schemas)
- Link checkers (traceability validation)
- Evidence validators (completeness checks)
- Gate validators (PR-blocking rules)

**Primary AoR:** STK_DAB, STK_CM

**Key Validators:**
- **nomenclature_validator** — Enforces v6.0 naming standard
- **knot_validator** — Ensures K01-K14 only
- **aor_validator** — Validates AoR allowlist
- **ata_validator** — Checks ATA 00-116 range
- **phase_validator** — Validates LC01-LC14
- **category_validator** — Enforces category-AoR constraints
- **schema_validator** — Validates against SSOT schemas
- **link_validator** — Verifies trace links exist
- **evidence_validator** — Checks evidence completeness
- **release_validator** — Gates release readiness

---

### schemas
**Path:** `schemas/`

**Description:** SSOT schemas and ontologies (ATA 91)

**Contents:**
- JSON schemas for all artifact types
- YAML schemas for configuration files
- Ontology definitions (RDF/OWL)
- Controlled vocabulary files
- Data models
- API schemas

**Primary AoR:** STK_DAB, STK_SE

**Key Schemas:**
- **artifact.schema.json** — Base artifact structure
- **knot.schema.json** — KNOT definition structure
- **roadmap.schema.json** — Roadmap structure
- **evidence.schema.json** — Evidence bundle structure
- **release.schema.json** — Release package structure
- **traceability.schema.json** — Trace link structure
- **dpp.schema.json** — Digital Product Passport
- **sbom.schema.json** — Software Bill of Materials

---

### automation
**Path:** `automation/`

**Description:** CI/PR automation scripts

**Contents:**
- CI/CD pipeline definitions
- PR validation scripts
- Automated test runners
- Artifact generation scripts
- Evidence collection automation
- Release packaging automation

**Primary AoR:** STK_DAB

**Key Automation:**
- **pre-commit hooks** — Validate before commit
- **PR validators** — Check PR compliance
- **artifact generators** — Generate from templates
- **evidence collectors** — Gather proof artifacts
- **link checkers** — Verify traceability
- **release packagers** — Bundle release artifacts
- **gate enforcers** — Block non-compliant work

---

### portals
**Path:** `portals/`

**Description:** Portal UI components and configurations

**Contents:**
- Portal page definitions
- Navigation configurations
- Role-based view configs
- Dashboard definitions
- Roadmap visualizations
- Uncertainty node displays

**Primary AoR:** STK_DAB, STK_PMO

**Key Components:**
- **aor_entry_points** — AoR-specific landing pages
- **roadmap_views** — Active/completed roadmap displays
- **uncertainty_dashboards** — Uncertainty node tracking
- **evidence_browsers** — Evidence ledger exploration
- **trace_visualizers** — Traceability graph displays
- **release_trackers** — Release status monitoring

---

### roadmaps
**Path:** `roadmaps/`

**Description:** Roadmap templates and orchestration configs

**Contents:**
- Roadmap templates
- Task decomposition patterns
- Dependency configurations
- Gate definitions
- Evidence requirements
- Orchestration rules

**Primary AoR:** STK_PMO, STK_DAB

**Key Elements:**
- **roadmap_templates** — Structured plan templates
- **task_patterns** — Reusable task structures
- **dependency_maps** — Task dependencies
- **gate_configs** — Roadmap gate definitions
- **evidence_maps** — Required evidence per task
- **orchestration_rules** — Execution order constraints

---

## Usage Guidelines

### For Template Usage

1. **Select appropriate template** from templates/
2. **Copy template** to working directory
3. **Fill in required fields** following v6.0
4. **Run nomenclature validator** to verify
5. **Generate content** following template guidance
6. **Run schema validator** to ensure compliance
7. **Commit artifact** with evidence

### For Validation

1. **Run validators** before committing
2. **Fix any errors** reported by validators
3. **Re-run validators** until clean
4. **Commit with validator logs** as evidence
5. **PR validation** runs automatically
6. **Address any PR blocks** from validators

### For Automation

1. **Configure CI/CD** for your scope
2. **Enable pre-commit hooks** for early validation
3. **Set up PR gates** for governance
4. **Automate evidence collection** where possible
5. **Integrate with ledgers** for automatic registration
6. **Monitor automation logs** for issues

---

## Validator Enforcement

Validators operate at multiple levels:

1. **Pre-commit** — Local validation before commit
2. **PR-blocking** — Must pass before merge
3. **Release-gating** — Must pass before release
4. **Audit-time** — Retrospective validation

**All validators are PR-blocking for CATEGORY=DELIVERABLE**

---

## Template Hierarchy

Templates are organized by:

- **CATEGORY** (DELIVERABLE, EVIDENCE, REGISTRY, etc.)
- **TYPE** (STD, SPEC, PLAN, REQ, etc.)
- **AoR** (for AoR-specific templates)
- **KNOT** (for KNOT-specific task templates)

---

## Schema Versioning

All schemas are versioned:

- **Major version** — Breaking changes
- **Minor version** — New optional fields
- **Patch version** — Documentation/fixes

Artifacts must declare their schema version for validation.

---

## Automation Integration

Automation scripts integrate with:

- **Git** — For version control operations
- **GitHub Actions** — For CI/CD pipelines
- **Validators** — For compliance checking
- **Ledgers** — For artifact registration
- **Portals** — For UI updates
- **Notification systems** — For alerts

---

## Governance

- **Templates are version-controlled** — Changes require CM approval
- **Validators are mandatory** — Cannot bypass PR gates
- **Schemas are SSOT** — Single source of truth for structure
- **Automation is auditable** — All actions logged
- **Portals reflect ledgers** — UI is read-only view of truth

---

## Version

**Infrastructure Version:** 1.0  
**Last Updated:** 2025-12-19

---

## References

- [CAXS Main README](../README.md)
- [v6.0 Nomenclature](../../README.md#92-controlled-vocabulary--nomenclature-v60)
- [KNOTS Directory](../KNOTS/README.md)
- [LEDGERS Directory](../LEDGERS/README.md)
