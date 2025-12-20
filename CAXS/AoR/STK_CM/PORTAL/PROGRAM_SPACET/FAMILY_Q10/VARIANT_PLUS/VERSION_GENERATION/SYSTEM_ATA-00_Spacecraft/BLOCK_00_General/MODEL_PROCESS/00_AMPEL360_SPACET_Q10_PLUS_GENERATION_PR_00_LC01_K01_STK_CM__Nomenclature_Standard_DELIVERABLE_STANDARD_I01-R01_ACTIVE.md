# Nomenclature Standard — v6.0

**AMPEL360 CA360º — Configuration Management Nomenclature Standard**

---

## Metadata

- **ATA:** 00 (GENERAL)
- **Program:** SPACET Q10 PLUS GENERATION
- **Phase:** LC01 (Problem Statement / Generation / Prompting Engineering)
- **KNOT:** K01
- **AoR Owner:** STK_CM (Configuration Management)
- **Category:** DELIVERABLE
- **Type:** STANDARD
- **Status:** ACTIVE
- **Issue-Revision:** I01-R01
- **Nomenclature Version:** v6.0

---

## Purpose

This document defines the **Nomenclature Standard v6.0** for the AMPEL360 SPACET Q10 PLUS GENERATION program. It establishes mandatory naming conventions, identifier patterns, and vocabulary rules for all artifacts, files, and configuration items.

The standard ensures:
- **Consistency**: Uniform naming across all program artifacts
- **Traceability**: Clear identification and version tracking
- **Automation**: Machine-parseable filenames and identifiers
- **Governance**: Controlled vocabularies and validation rules

---

## 1. Filename Pattern

### 1.1 Complete Pattern

All files MUST follow this pattern:

```
<ATA>_<PROGRAM>_<FAMILY>_<VARIANT>_<VERSION>_<PHASE>_<LIFECYCLE>_<KNOT>_<AOR>__<artifact-name>_<CATEGORY>_<TYPE>_<ISSUE>-<REVISION>_<STATUS>.<ext>
```

### 1.2 Field Definitions

| Field | Description | Format | Example |
|-------|-------------|--------|---------|
| `ATA` | ATA chapter code (2 digits) | `\d{2}` | `00`, `21`, `49` |
| `PROGRAM` | Program identifier | `AMPEL360` | `AMPEL360` |
| `FAMILY` | Aircraft/system family | `SPACET` | `SPACET` |
| `VARIANT` | Family variant | `Q10` | `Q10`, `Q100` |
| `VERSION` | Version stream | `(BASELINE|PLUS|GEN|CERT)` | `PLUS`, `BASELINE` |
| `PHASE` | Development phase | `(PLUS|GENERATION|PR|HW|SW)` | `GENERATION`, `PR` |
| `LIFECYCLE` | Lifecycle phase code | `\d{2}` | `00`, `01`, `06`, `10` |
| `KNOT` | Knot identifier | `K\d{2}` | `K01`, `K04`, `K06`, `K10` |
| `AOR` | Area of Responsibility | `STK_[A-Z]+` | `STK_CM`, `STK_SE` |
| `artifact-name` | Descriptive artifact name | `[a-z0-9-]+` | `standards-pack`, `cr-register` |
| `CATEGORY` | Artifact category | See §1.3 | `DELIVERABLE`, `REGISTRY` |
| `TYPE` | Artifact type | See §1.4 | `SPEC`, `POLICY`, `REG` |
| `ISSUE` | Major version | `I\d{2}` | `I01`, `I02` |
| `REVISION` | Minor version | `R\d{2}` | `R01`, `R02` |
| `STATUS` | Lifecycle status | See §1.5 | `ACTIVE`, `DRAFT` |
| `ext` | File extension | `(md|csv|yaml|json)` | `md`, `csv` |

### 1.3 Category Taxonomy

| Category | Description | Usage |
|----------|-------------|-------|
| `DELIVERABLE` | Primary engineering deliverable | Specifications, policies, procedures, standards |
| `REGISTRY` | Structured data registry | Registers, catalogs, indexes, schemas |
| `SIGNOFF` | Approval and signoff records | Approval matrices, signoff logs |
| `EXPORT_CONTROL` | Export-controlled content | Restricted distributions |
| `EVIDENCE` | Verification and validation evidence | Test results, analysis reports |
| `TEMPLATE` | Reusable template | Artifact generation templates |

### 1.4 Type Taxonomy

| Type | Description | File Format | Category |
|------|-------------|-------------|----------|
| `SPEC` | Specification | Markdown | DELIVERABLE |
| `STANDARD` | Standard or normative document | Markdown | DELIVERABLE |
| `POLICY` | Policy document | Markdown | DELIVERABLE |
| `PROC` | Procedure or process | Markdown | DELIVERABLE |
| `TEMPLATE` | Artifact template | Markdown | TEMPLATE |
| `REG` | Register (structured data) | CSV, JSON, YAML | REGISTRY |
| `REGISTER` | Register alternative naming | CSV | REGISTRY |
| `CATALOG` | Catalog or index | Markdown, CSV | REGISTRY |
| `CAT` | Catalog short form | Markdown, CSV | REGISTRY |
| `INDEX` | Index document | Markdown | REGISTRY |
| `IDX` | Index short form | Markdown | REGISTRY |
| `SCHEMA` | Data schema definition | JSON, YAML | REGISTRY |
| `VOCAB` | Controlled vocabulary | CSV | REGISTRY |
| `MATRIX` | Matrix or mapping table | CSV | REGISTRY |
| `TAB` | Tabular data | CSV | REGISTRY |
| `RULESET` | Validation or enforcement rules | YAML, JSON | DELIVERABLE |
| `CONFIG` | Configuration file | YAML, JSON | DELIVERABLE |
| `MANIFEST` | Manifest or bill of materials | JSON, YAML | REGISTRY |
| `CHECKLIST` | Checklist or verification list | Markdown | DELIVERABLE |
| `OVERVIEW` | Overview or summary document | Markdown | DELIVERABLE |
| `STD` | Standard (alternative) | Markdown | DELIVERABLE |

### 1.5 Status Values

| Status | Description | Usage |
|--------|-------------|-------|
| `DRAFT` | Work in progress, not released | Initial development, not approved |
| `ACTIVE` | Currently in use, approved | Released and operational |
| `RELEASED` | Formally released baseline | Frozen, immutable version |
| `SUPERSEDED` | Replaced by newer version | Historical reference only |
| `OBSOLETE` | No longer valid or used | Archived, not referenced |

---

## 2. Issue-Revision Pattern

### 2.1 Versioning Rules

**Format:** `I<issue>-R<revision>` where both are 2-digit zero-padded numbers.

**Examples:**
- `I01-R01` — Issue 1, Revision 1 (initial version)
- `I01-R02` — Issue 1, Revision 2 (minor update)
- `I02-R01` — Issue 2, Revision 1 (major update)

### 2.2 Issue Increment (Major Version)

Increment Issue when making **breaking changes**:
- Changes to data schemas that invalidate existing data
- Removal of mandatory fields or constraints
- Changes to nomenclature patterns
- Major structural changes
- Changes to interfaces or APIs that break compatibility

### 2.3 Revision Increment (Minor Version)

Increment Revision when making **non-breaking changes**:
- Addition of optional fields
- Clarifications and corrections
- Documentation updates
- Bug fixes
- Addition of new vocabulary values

### 2.4 Version Compatibility

- Artifacts with the same Issue number MUST be backward compatible
- Artifacts referencing other artifacts SHOULD specify minimum required version
- Version dependencies MUST be documented in artifact metadata

---

## 3. Controlled Vocabularies

### 3.1 ATA Chapter Codes

ATA chapters follow the ATA 100 standard specification. Key codes for this program:

| Code | Name | Description |
|------|------|-------------|
| `00` | GENERAL | General information, program governance |
| `11` | Placards and Markings | Documentation and labeling |
| `21` | Air Conditioning | Environmental control systems |
| `30` | Data, Comms and Registry | Data management and communication |
| `49` | Airborne Auxiliary Power | APU systems |
| `91` | Data Schemas / Ontologies | Data models and ontologies |
| `93` | Traceability Graph | Traceability and relationships |
| `94` | DPP Core | Digital Product Passport |
| `95` | SBOM / BOM Exports | Software and hardware BOMs |
| `98` | Signed Release Packs | Release packages |
| `99` | Master Registers | Master data registers |

### 3.2 Area of Responsibility (AoR) Codes

| Code | Name | Description |
|------|------|-------------|
| `STK_CM` | Configuration Management | Baseline, change control, releases |
| `STK_PMO` | Program Management Office | Planning, reporting, coordination |
| `STK_SE` | Systems Engineering | Requirements, architecture, interfaces |
| `STK_SAF` | Safety & Security | Safety, security, hazard analysis |
| `STK_CERT` | Certification | Compliance, audit, authority liaison |
| `STK_DAB` | Digital Applications & Blockchains | Data governance, digital services |
| `STK_PHM` | Prognostics & Health Management | Health monitoring, predictive analytics |
| `STK_TEST` | Testing | Verification, validation, test execution |
| `STK_OPS` | Operations | Operational procedures and support |
| `STK_MRO` | Maintenance, Repair, Overhaul | Maintenance procedures |
| `STK_CY` | Cybersecurity | Cybersecurity governance |
| `STK_CEGT` | Circular Economy & Green Tech | Sustainability, circularity |
| `STK_SPACEPORT` | Spaceport | Ground operations, launch facilities |
| `STK_AI` | Artificial Intelligence | AI systems and governance |

### 3.3 Lifecycle Phase Codes

| Code | Phase | Description |
|------|-------|-------------|
| `LC01` | Problem Statement / Generation | Initial problem definition and prompting |
| `LC02` | Requirements | Requirements definition and analysis |
| `LC03` | Design | Detailed design and specification |
| `LC04` | Development | Implementation and coding |
| `LC05` | Integration | Component integration |
| `LC06` | Verification / Quality | Testing and quality assurance |
| `LC07` | Deployment | Production deployment |
| `LC08` | Operations | Operational use |
| `LC09` | Maintenance | Maintenance and updates |
| `LC10` | Industrialization / CM | Configuration management, serialization |

### 3.4 Knot Identifiers

| Code | Name | Purpose |
|------|------|---------|
| `K00` | Portal Entry | Entry point and navigation |
| `K01` | Standards | Nomenclature, policies, templates |
| `K02` | Problem Definition | Problem statement and scoping |
| `K03` | Integration | Component integration |
| `K04` | Change Control Gate | Change approval and impact analysis |
| `K05` | Task Execution | Task definition and execution |
| `K06` | Baseline Release Gate | Release validation and freeze |
| `K07` | Completion | Task completion and closure |
| `K08` | Certification | Certification processes |
| `K09` | Validation | Verification and validation |
| `K10` | Audit Gate | Audit preparation and traceability |
| `K14` | Notification | Event notification and escalation |

### 3.5 Program/Family/Variant Codes

**Programs:**
- `SPACET` — Space Transport program
- `AIRT` — Air Transport program

**Families:**
- `Q10` — Q10 family
- `Q100` — Q100 family

**Variants:**
- `GEN` — Generation (initial development)
- `BASELINE` — Baseline configuration
- `PLUS` — Enhanced/Plus variant
- `CERT` — Certification variant

**Version Streams:**
- `GENERATION` — Generation phase
- `PR` — Program (general)
- `HW` — Hardware
- `SW` — Software

---

## 4. Identifier Patterns

### 4.1 Document Identifiers

Documents MAY include a `document_id` field in front matter:

```yaml
document_id: "<ATA>_<PROGRAM>_<FAMILY>_<VARIANT>_<VERSION>_<PHASE>_<LIFECYCLE>_<KNOT>_<AOR>__<artifact-name>_<CATEGORY>_<TYPE>_<ISSUE>-<REVISION>_<STATUS>"
```

This identifier MUST match the filename (without extension).

### 4.2 Asset Identifiers

For physical or logical assets:

```
<ATA>-<asset-type>-<sequential-id>
```

**Examples:**
- `21-PUMP-001` — ATA 21 pump, sequential ID 001
- `49-APU-002` — ATA 49 APU, sequential ID 002

### 4.3 Change Request Identifiers

```
CR-<YYYY>-<sequential>
```

**Examples:**
- `CR-2025-001` — Change request 1 in 2025
- `CR-2025-042` — Change request 42 in 2025

### 4.4 Registry Keys

Registry entries MUST have unique keys following these patterns:

**Generic:**
```
<registry-type>-<unique-id>
```

**Examples:**
- `SCHEMA-001` — Schema registry entry 001
- `TEMPLATE-005` — Template index entry 005
- `VOCAB-ATA` — Vocabulary for ATA codes

---

## 5. Metadata Requirements

### 5.1 Markdown Front Matter

All Markdown documents MUST include YAML front matter with these fields:

```yaml
---
document_id: "<full document identifier>"
title: "<human-readable title>"
ata: "<ATA code>"
program: "<PROGRAM>"
family: "<FAMILY>"
variant: "<VARIANT>"
version: "<VERSION>"
phase: "<PHASE>"
lifecycle: "<LC code>"
knot: "<K code>"
owner_aor: "<AOR code>"
category: "<CATEGORY>"
type: "<TYPE>"
status: "<STATUS>"
issue_rev: "<ISSUE-REVISION>"
last_updated: "<YYYY-MM-DD>"
---
```

**Example:**
```yaml
---
document_id: "00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__nomenclature-standard_DELIVERABLE_STANDARD_I01-R01_ACTIVE"
title: "Nomenclature Standard — v6.0"
ata: "00"
program: "AMPEL360"
family: "SPACET"
variant: "Q10"
version: "PLUS"
phase: "GENERATION"
lifecycle: "LC01"
knot: "K01"
owner_aor: "STK_CM"
category: "DELIVERABLE"
type: "STANDARD"
status: "ACTIVE"
issue_rev: "I01-R01"
last_updated: "2025-12-20"
---
```

### 5.2 CSV Headers

CSV files MUST include a header row with field names matching the controlled vocabularies where applicable.

### 5.3 YAML/JSON Schema

YAML and JSON files SHOULD reference their schema in metadata or comments:

```yaml
# Schema: baseline-manifest-schema-v1.0.json
```

```json
{
  "$schema": "baseline-manifest-schema-v1.0.json",
  ...
}
```

---

## 6. Validation Rules

### 6.1 Nomenclature Validation

Files MUST pass these validations:

1. **Pattern match**: Filename matches the complete nomenclature pattern
2. **Field validation**: All fields use valid controlled vocabulary values
3. **Consistency**: Filename matches document_id in front matter (if present)
4. **Extension**: File extension matches type (`.md` for text, `.csv` for tabular, etc.)

### 6.2 Uniqueness Validation

1. **Document IDs**: No duplicate document_id values across the baseline
2. **Filenames**: No duplicate filenames (case-insensitive)
3. **Registry keys**: No duplicate keys within a registry
4. **Asset IDs**: No duplicate asset identifiers

### 6.3 Severity Levels

| Level | Description | Action |
|-------|-------------|--------|
| `ERROR` | Blocking violation | Must be fixed before approval |
| `WARNING` | Non-blocking violation | Should be fixed, can be waived |
| `INFO` | Informational | Suggestion only |

---

## 7. Examples

### 7.1 Specification Document

```
00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Standards_Pack_DELIVERABLE_SPEC_I01-R01_ACTIVE.md
```

**Breakdown:**
- ATA: `00` (GENERAL)
- Program: `AMPEL360`
- Family: `SPACET`
- Variant: `Q10`
- Version: `PLUS`
- Phase: `GENERATION`
- Lifecycle: `PR_00_LC01`
- Knot: `K01`
- AoR: `STK_CM`
- Name: `Standards_Pack`
- Category: `DELIVERABLE`
- Type: `SPEC`
- Issue-Rev: `I01-R01`
- Status: `ACTIVE`

### 7.2 Registry CSV

```
00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Schema_Registry_REGISTRY_REGISTER_I01-R01_ACTIVE.csv
```

### 7.3 Policy Document

```
00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K04_STK_CM__Change_Control_Procedure_DELIVERABLE_POLICY_I01-R01_ACTIVE.md
```

### 7.4 Template

```
00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K06_STK_CM__BRP_Template_DELIVERABLE_TEMPLATE_I01-R01_ACTIVE.md
```

---

## 8. Migration Guide

### 8.1 From v5.x to v6.0

**Breaking Changes:**
- None (v6.0 is the initial formalized version)

**New Features:**
- Formal Issue-Revision versioning
- Extended AoR taxonomy
- Knot identifier mapping
- Lifecycle phase codes

**Migration Actions:**
- Review existing filenames for compliance
- Add front matter to Markdown documents
- Update registry keys to new format
- Run nomenclature validator

---

## 9. References

- **Standards Pack**: `00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Standards_Pack_DELIVERABLE_SPEC_I01-R01_ACTIVE.md`
- **Controlled Vocabularies**: `00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Controlled_Vocabularies_REGISTRY_VOCAB_I01-R01_ACTIVE.csv`
- **Enforcement Rules**: `00_AMPEL360_SPACET_Q10_PLUS_GENERATION_PR_00_LC01_K01_STK_CM__Enforcement_Rules_DELIVERABLE_RULESET_I01-R01_ACTIVE.yaml`

---

## Change Log

| Revision | Date | Author | Changes |
|----------|------|--------|---------|
| I01-R01 | 2025-12-20 | STK_CM | Initial v6.0 nomenclature standard |

---

**END OF DOCUMENT**
