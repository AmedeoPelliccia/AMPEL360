# Templates Index — Artifact Generation Templates

**AMPEL360 CA360º — K01 Standards Templates Catalog**

---

## Metadata

- **ATA:** 00 (GENERAL)
- **Program:** SPACET Q10 PLUS GENERATION
- **Phase:** LC01 (Problem Statement / Generation / Prompting Engineering)
- **KNOT:** K01
- **AoR Owner:** STK_CM (Configuration Management)
- **Category:** DELIVERABLE
- **Type:** INDEX
- **Status:** ACTIVE
- **Issue-Revision:** I01-R01

---

## Purpose

This index catalogs all official templates available for artifact generation in the AMPEL360 SPACET Q10 PLUS GENERATION program. Templates ensure consistency, completeness, and compliance with standards across all deliverables.

Templates are used by:
- **F05: Artifact Generator** — Wizard-based artifact creation
- **Manual creation** — Reference for structure and mandatory fields
- **Validation** — Baseline for schema compliance checking

---

## 1. Template Catalog

### 1.1 Deliverable Templates

#### TEMPLATE-001: Specification Document
**File:** `templates/deliverable-spec-template.md`  
**Category:** DELIVERABLE  
**Type:** SPEC  
**Version:** v1.0.0  
**Usage:** Technical specifications, system descriptions, feature definitions

**Structure:**
- Front matter (metadata)
- Purpose and scope
- Requirements or specifications
- References
- Change log

**Mandatory Fields:**
- `document_id`, `title`, `ata`, `owner_aor`, `category`, `type`, `status`, `issue_rev`

**Example Instantiation:**
```
00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Standards_Pack_DELIVERABLE_SPEC_I01-R01_ACTIVE.md
```

---

#### TEMPLATE-002: Policy Document
**File:** `templates/deliverable-policy-template.md`  
**Category:** DELIVERABLE  
**Type:** POLICY  
**Version:** v1.0.0  
**Usage:** Policies, governance documents, rules

**Structure:**
- Front matter (metadata)
- Policy statement
- Scope and applicability
- Roles and responsibilities
- Compliance and enforcement
- References
- Change log

**Mandatory Fields:**
- `document_id`, `title`, `ata`, `owner_aor`, `category`, `type`, `status`, `issue_rev`, `policy_level`

**Example Instantiation:**
```
00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K04_STK_CM__Change_Control_Procedure_DELIVERABLE_POLICY_I01-R01_ACTIVE.md
```

---

#### TEMPLATE-003: Procedure Document
**File:** `templates/deliverable-procedure-template.md`  
**Category:** DELIVERABLE  
**Type:** PROC  
**Version:** v1.0.0  
**Usage:** Step-by-step procedures, workflows, processes

**Structure:**
- Front matter (metadata)
- Purpose and scope
- Prerequisites
- Step-by-step instructions
- Roles and responsibilities
- Verification and validation
- References
- Change log

**Mandatory Fields:**
- `document_id`, `title`, `ata`, `owner_aor`, `category`, `type`, `status`, `issue_rev`

**Example Instantiation:**
```
00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K06_STK_CM__Baseline_Release_Procedure_DELIVERABLE_POLICY_I01-R01_ACTIVE.md
```

---

#### TEMPLATE-004: Standard Document
**File:** `templates/deliverable-standard-template.md`  
**Category:** DELIVERABLE  
**Type:** STANDARD  
**Version:** v1.0.0  
**Usage:** Standards, normative requirements, conventions

**Structure:**
- Front matter (metadata)
- Purpose and scope
- Normative requirements
- Validation and compliance
- References
- Migration guide (if applicable)
- Change log

**Mandatory Fields:**
- `document_id`, `title`, `ata`, `owner_aor`, `category`, `type`, `status`, `issue_rev`, `standard_version`

**Example Instantiation:**
```
00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Nomenclature_Standard_DELIVERABLE_STANDARD_I01-R01_ACTIVE.md
```

---

#### TEMPLATE-005: Checklist
**File:** `templates/deliverable-checklist-template.md`  
**Category:** DELIVERABLE  
**Type:** CHECKLIST  
**Version:** v1.0.0  
**Usage:** Gate checklists, verification lists, compliance checks

**Structure:**
- Front matter (metadata)
- Purpose and applicability
- Checklist items with criteria
- Completion guidance
- References
- Change log

**Mandatory Fields:**
- `document_id`, `title`, `ata`, `owner_aor`, `category`, `type`, `status`, `issue_rev`, `gate` (if applicable)

**Example Instantiation:**
```
00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K04_STK_CM__Cross_ATA_Clearance_Checklist_DELIVERABLE_CHECKLIST_I01-R01_ACTIVE.md
```

---

#### TEMPLATE-006: Overview Document
**File:** `templates/deliverable-overview-template.md`  
**Category:** DELIVERABLE  
**Type:** OVERVIEW  
**Version:** v1.0.0  
**Usage:** Entry points, summaries, navigation guides

**Structure:**
- Front matter (metadata)
- Purpose and scope
- Operating model
- Navigation links
- References
- Quick index

**Mandatory Fields:**
- `document_id`, `title`, `ata`, `owner_aor`, `category`, `type`, `status`, `issue_rev`

**Example Instantiation:**
```
00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K00_STK_CM__Block00_General_Entry_DELIVERABLE_OVERVIEW_I01-R01_ACTIVE.md
```

---

### 1.2 Registry Templates

#### TEMPLATE-007: CSV Register
**File:** `templates/registry-register-template.csv`  
**Category:** REGISTRY  
**Type:** REGISTER / REG  
**Version:** v1.0.0  
**Usage:** Structured data registries, catalogs, inventories

**Structure:**
- Header row with field names
- Data rows with consistent formatting
- No empty columns
- Standard date format (YYYY-MM-DD)

**Mandatory Fields:**
- Unique identifier field (first column recommended)
- Status field
- Last_Updated field

**Example Instantiation:**
```
00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Schema_Registry_REGISTRY_REGISTER_I01-R01_ACTIVE.csv
```

---

#### TEMPLATE-008: Controlled Vocabulary
**File:** `templates/registry-vocab-template.csv`  
**Category:** REGISTRY  
**Type:** VOCAB  
**Version:** v1.0.0  
**Usage:** Controlled vocabularies, enumerations, code lists

**Structure:**
- Header: `Code,Name,Description,Category,Status,Last_Updated`
- Codes in consistent format
- Descriptions clear and concise
- Status tracking

**Mandatory Fields:**
- `Code`, `Name`, `Status`

**Example Instantiation:**
```
00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Controlled_Vocabularies_REGISTRY_VOCAB_I01-R01_ACTIVE.csv
```

---

#### TEMPLATE-009: Index Document
**File:** `templates/registry-index-template.md`  
**Category:** REGISTRY  
**Type:** INDEX  
**Version:** v1.0.0  
**Usage:** Indexes, catalogs (narrative form)

**Structure:**
- Front matter (metadata)
- Purpose
- Index entries organized by category
- Usage guidance
- References

**Mandatory Fields:**
- `document_id`, `title`, `ata`, `owner_aor`, `category`, `type`, `status`, `issue_rev`

**Example Instantiation:**
```
00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Templates_Index_DELIVERABLE_INDEX_I01-R01_ACTIVE.md
```

---

#### TEMPLATE-010: Matrix (Tabular)
**File:** `templates/registry-matrix-template.csv`  
**Category:** REGISTRY  
**Type:** MATRIX / TAB  
**Version:** v1.0.0  
**Usage:** Mapping tables, cross-reference matrices

**Structure:**
- Row headers (first column)
- Column headers (first row)
- Intersection values
- Legend/key if needed

**Mandatory Fields:**
- Row identifier column
- At least one mapping column

**Example Instantiation:**
```
00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K04_STK_CM__Approval_Matrix_REGISTRY_MATRIX_I01-R01_ACTIVE.csv
```

---

### 1.3 Schema Templates

#### TEMPLATE-011: JSON Schema
**File:** `templates/schema-json-template.json`  
**Category:** REGISTRY  
**Type:** SCHEMA  
**Version:** v1.0.0  
**Usage:** Data structure definitions using JSON Schema

**Structure:**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "<schema-identifier>",
  "title": "<Schema Title>",
  "description": "<Schema Description>",
  "type": "object",
  "properties": {
    ...
  },
  "required": [...]
}
```

**Mandatory Fields:**
- `$schema`, `$id`, `title`, `type`

**Example Instantiation:**
```
00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K06_STK_CM__Baseline_Manifest_REGISTRY_SCHEMA_I01-R01_ACTIVE.json
```

---

#### TEMPLATE-012: YAML Configuration
**File:** `templates/config-yaml-template.yaml`  
**Category:** DELIVERABLE  
**Type:** CONFIG / RULESET  
**Version:** v1.0.0  
**Usage:** Configuration files, rule definitions

**Structure:**
```yaml
# Schema reference
# Configuration metadata
metadata:
  name: "<Config Name>"
  version: "<Version>"
  owner: "<AoR>"

# Configuration sections
...
```

**Mandatory Fields:**
- Metadata section with `name`, `version`, `owner`

**Example Instantiation:**
```
00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Enforcement_Rules_DELIVERABLE_RULESET_I01-R01_ACTIVE.yaml
```

---

### 1.4 Change Management Templates

#### TEMPLATE-013: Change Request
**File:** `templates/change-request-template.md`  
**Category:** DELIVERABLE  
**Type:** PROC  
**Version:** v1.0.0  
**Usage:** Change requests (CR/ECR/ECO)

**Structure:**
- Change request metadata
- Problem statement
- Proposed solution
- Impact analysis
- Approval routing
- Implementation plan

**Mandatory Fields:**
- `cr_id`, `title`, `type`, `priority`, `status`, `owner`, `date_created`

---

#### TEMPLATE-014: Impact Analysis
**File:** `templates/impact-analysis-template.md`  
**Category:** DELIVERABLE  
**Type:** PROC  
**Version:** v1.0.0  
**Usage:** Impact analysis reports for K04 gate

**Structure:**
- Change scope
- Cross-ATA impact assessment
- Risk screening
- Evidence requirements
- Approval recommendations

**Mandatory Fields:**
- `cr_id`, `analysis_date`, `analyst`, `affected_atas`, `risk_level`

---

#### TEMPLATE-015: BRP Template
**File:** `templates/brp-template.md`  
**Category:** DELIVERABLE  
**Type:** TEMPLATE  
**Version:** v1.0.0  
**Usage:** Baseline Release Package structure for K06 gate

**Structure:**
- Release metadata
- Baseline manifest
- Change summary
- Validation results
- Evidence bundle
- Sign-offs

**Mandatory Fields:**
- `release_id`, `baseline_version`, `freeze_date`, `release_manager`

---

### 1.5 Audit and Compliance Templates

#### TEMPLATE-016: Traceability Matrix
**File:** `templates/traceability-matrix-template.csv`  
**Category:** DELIVERABLE  
**Type:** TEMPLATE  
**Version:** v1.0.0  
**Usage:** Traceability matrices for K10 gate

**Structure:**
- Header: `Source_ID,Source_Type,Target_ID,Target_Type,Relationship,Verified,Last_Updated`
- Traceability links
- Verification status

**Mandatory Fields:**
- `Source_ID`, `Target_ID`, `Relationship`, `Verified`

---

#### TEMPLATE-017: Evidence Index
**File:** `templates/evidence-index-template.json`  
**Category:** REGISTRY  
**Type:** SCHEMA  
**Version:** v1.0.0  
**Usage:** Evidence tracking for K10 gate

**Structure:**
```json
{
  "evidence_id": "...",
  "evidence_type": "...",
  "description": "...",
  "location": "...",
  "hash": "...",
  "related_artifacts": [...]
}
```

---

#### TEMPLATE-018: CERT Clearance Statement
**File:** `templates/cert-clearance-template.md`  
**Category:** DELIVERABLE  
**Type:** TEMPLATE  
**Version:** v1.0.0  
**Usage:** CERT clearance records for K10 gate

**Structure:**
- Clearance metadata
- Review summary
- Compliance verification
- Conditions and limitations
- Formal approval

**Mandatory Fields:**
- `clearance_id`, `baseline_id`, `cert_reviewer`, `clearance_date`, `status`

---

## 2. Template Usage Guidelines

### 2.1 When to Use Templates

**MUST use templates for:**
- All formal deliverables (specifications, policies, procedures)
- Official registries and indexes
- Gate artifacts (checklists, reports, packages)
- Audit trail documents

**SHOULD use templates for:**
- Working documents that will become formal deliverables
- Meeting minutes and decision logs
- Status reports and dashboards

**MAY deviate from templates for:**
- Exploratory or research documents
- Personal notes and drafts
- External references

### 2.2 Template Instantiation Process

1. **Select template** based on artifact category and type
2. **Copy template** to target location with proper nomenclature
3. **Fill in metadata** (front matter or header section)
4. **Complete content** following structure guidance
5. **Validate** against nomenclature and schema rules
6. **Review** with relevant stakeholders
7. **Approve** through proper workflow
8. **Publish** to appropriate location

### 2.3 Template Customization

Templates MAY be customized if:
- Additional sections are needed for specific use cases
- Optional fields are added (not removed)
- Customization is documented in artifact metadata

Templates MUST NOT be customized by:
- Removing mandatory fields
- Changing field names or types
- Violating nomenclature standards
- Breaking schema compatibility

---

## 3. Template Versioning

### 3.1 Version Scheme

Templates follow semantic versioning: `vMAJOR.MINOR.PATCH`

**MAJOR** — Breaking changes to structure or mandatory fields  
**MINOR** — New optional sections or fields  
**PATCH** — Documentation updates, clarifications, bug fixes

### 3.2 Template Update Process

1. **Propose update** with rationale and impact analysis
2. **Review** with STK_CM and affected AoRs
3. **Test** with sample instantiations
4. **Approve** and version
5. **Update** Templates Index
6. **Communicate** to all users
7. **Provide migration guidance** if breaking changes

---

## 4. Template Repository

### 4.1 Storage Location

Templates are stored in:
```
CAXS/INFRASTRUCTURE/templates/
```

Organized by category:
```
templates/
  ├── deliverables/
  ├── registries/
  ├── schemas/
  ├── change-management/
  └── audit-compliance/
```

### 4.2 Access and Permissions

- **Read**: All users
- **Write**: STK_CM only
- **Approve**: STK_CM leads with cross-AoR review

---

## 5. Integration with Portal Features

### 5.1 F05: Artifact Generator

The Artifact Generator uses this index to:
- Present available templates
- Guide users through wizard-based creation
- Pre-populate mandatory fields
- Validate against templates and schemas

### 5.2 F06: Gates & Validator Console

Validators reference templates to:
- Verify structure compliance
- Check mandatory field presence
- Validate against expected format

### 5.3 F_CM06: Nomenclature & Standards Enforcement

Standards enforcement uses templates to:
- Validate artifact structure
- Ensure consistency
- Generate compliance reports

---

## 6. References

- **Standards Pack**: `00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Standards_Pack_DELIVERABLE_SPEC_I01-R01_ACTIVE.md`
- **Nomenclature Standard**: `00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Nomenclature_Standard_DELIVERABLE_STANDARD_I01-R01_ACTIVE.md`
- **Schema Registry**: `00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Schema_Registry_REGISTRY_REGISTER_I01-R01_ACTIVE.csv`

---

## Change Log

| Revision | Date | Author | Changes |
|----------|------|--------|---------|
| I01-R01 | 2025-12-20 | STK_CM | Initial templates index |

---

**END OF DOCUMENT**
