# LEDGERS — Evidence and Trust Fabric

## Overview

The **LEDGERS** directory contains the **evidence and trust fabric** providing audit-grade continuity for all AMPEL360 work. This is the foundation of the "L" pillar in AMPEL360 (A-M-P-E-**L**-360).

---

## Purpose

Engineering work becomes **certifiable** only when it is:
- **Ledger-addressed** (immutable artifact paths with SHA256)
- **Trace-linked** (connected via typed relations)
- **Release-packaged** (manifested and signed)

---

## Ledger Components

### knowledge-ledger
**Path:** `knowledge-ledger/`

**Description:** Immutable artifact addressing system

**Contents:**
- Artifact registry with repo paths
- SHA256 content hashes
- Optional commit references
- Typed relations between artifacts
- Approval states and transitions
- Version chains

**Primary AoR:** STK_DAB, STK_CM

**Key Features:**
- Immutable addressing (path + sha256)
- Content-addressable storage
- Cryptographic integrity
- Audit trail preservation

---

### traceability-graph
**Path:** `traceability-graph/`

**Description:** REQ ↔ DESIGN ↔ V&V ↔ OPS linkage with audit queries (ATA 93)

**Contents:**
- Requirements traceability links
- Design-to-requirement mappings
- Verification-to-requirement links
- Operations-to-design links
- Impact analysis data
- Trace queries and reports

**Primary AoR:** STK_DAB, STK_SE

**Key Relations:**
- `satisfies` — Design satisfies requirement
- `verifies` — Test verifies requirement
- `allocatesTo` — Requirement allocated to subsystem
- `dependsOn` — Dependency relationship
- `evidencedBy` — Evidence supporting claim
- `derivedFrom` — Derived from parent item

---

### digital-product-passport
**Path:** `digital-product-passport/`

**Description:** Provenance, materials, lifecycle identity (ATA 94)

**Contents:**
- Product identity and provenance
- Material composition
- Manufacturing data
- Lifecycle events
- Ownership history
- Sustainability metrics

**Primary AoR:** STK_DAB, STK_CM

**Key Features:**
- Unique product identification
- Full lifecycle tracking
- Material traceability
- Carbon footprint data
- Circularity metrics
- Compliance records

---

### sbom-bom
**Path:** `sbom-bom/`

**Description:** Dependency integrity for SW/HW/Model compositions (ATA 95)

**Contents:**
- Software Bill of Materials (SBOM)
- Hardware Bill of Materials (HW-BOM)
- Model Bill of Materials (Model-BOM)
- Dependency graphs
- Vulnerability assessments
- License compliance

**Primary AoR:** STK_DAB, STK_CM

**Key Elements:**
- Component identification
- Version tracking
- Dependency chains
- Security assessments
- License information
- Supply chain data

---

### release-packs
**Path:** `release-packs/`

**Description:** Manifests, exports, PR-blocking compliance evidence (ATA 98)

**Contents:**
- Release manifests
- Signed packages
- Compliance evidence bundles
- Export control documentation
- Gate check results
- Certification packs

**Primary AoR:** STK_CM, STK_CERT

**Key Features:**
- Digital signatures
- Cryptographic verification
- Compliance bundling
- Release gates enforcement
- Audit-ready packaging
- Export control tracking

---

### master-registers
**Path:** `master-registers/`

**Description:** Golden records and controlled vocabulary datasets (ATA 99)

**Contents:**
- Master part register
- Controlled vocabulary
- Identifier registries
- Naming standards
- Reference data
- Configuration items

**Primary AoR:** STK_CM

**Key Elements:**
- Unique identifiers
- Controlled terms
- Golden records
- Reference datasets
- Validation rules
- CM baselines

---

## Ledger Integration

### Knowledge Flow

```
WORK → ARTIFACT → LEDGER → EVIDENCE → RELEASE
  ↑                                        ↓
  └──────────── Audit & Reuse ─────────────┘
```

Every artifact:
1. **Generated** with v6.0 nomenclature
2. **Registered** in knowledge-ledger
3. **Linked** in traceability-graph
4. **Evidenced** with proof artifacts
5. **Packaged** in release-packs
6. **Certified** through gate checks

---

## Usage Guidelines

### For Artifact Registration

1. **Generate artifact** following v6.0 nomenclature
2. **Compute SHA256** hash of content
3. **Register in knowledge-ledger** with path + hash
4. **Create trace links** in traceability-graph
5. **Generate evidence** as required by KNOT
6. **Update relevant ledgers** (DPP, SBOM, registers)

### For Traceability

1. **Identify source and target** artifacts
2. **Determine relation type** (satisfies, verifies, etc.)
3. **Record in traceability-graph** with metadata
4. **Validate bidirectional links** (forward and backward)
5. **Run trace queries** to verify completeness
6. **Generate trace reports** for audits

### For Releases

1. **Gather all artifacts** for release scope
2. **Generate SBOM/BOM** for all components
3. **Create DPP entries** for products
4. **Bundle evidence** from all ledgers
5. **Create release manifest** with cryptographic signatures
6. **Run gate checks** (PR-blocking validators)
7. **Package for release** with all evidence

---

## Ledger Queries

Each ledger supports queries for:

- **Artifact lookup** by path, hash, or identifier
- **Relation traversal** (upstream/downstream)
- **Impact analysis** (what is affected by change?)
- **Completeness checks** (all required links present?)
- **Evidence verification** (proof artifacts exist?)
- **Audit trails** (who, what, when, why?)

---

## Blockchain Integration

Ledgers may be enhanced with blockchain/DLT:

- **Immutability** — Tamper-evident records
- **Distributed trust** — Multi-party verification
- **Smart contracts** — Automated gate enforcement
- **Transparency** — Auditable by all stakeholders
- **Non-repudiation** — Cryptographic proofs

**Note:** Blockchain integration is managed by STK_DAB under ATA 94-98.

---

## Governance

- **Ledger entries are immutable** — Cannot be deleted or modified
- **All changes create new entries** — History is preserved
- **SHA256 hashes are mandatory** — For content integrity
- **Trace links are bidirectional** — Forward and backward
- **Evidence is required** — Cannot release without evidence
- **Signatures are binding** — Cryptographically verified

---

## Evidence Requirements

Different categories require different evidence levels:

| Category | Evidence Required |
|----------|-------------------|
| DELIVERABLE | Full traceability + approval signatures |
| EVIDENCE | Self-documenting with source links |
| REGISTRY | Validation proofs + CM approval |
| SIGNOFF | Authority signatures + audit trail |
| EXPORT_CONTROL | Compliance proofs + export licenses |

---

## Version

**Ledgers Structure Version:** 1.0  
**Last Updated:** 2025-12-19

---

## References

- [CAXS Main README](../README.md)
- [Ledgers Definition (Main README)](../../README.md#35-l--ledgers)
- [ATA 93-99 (N-AXIS)](../ATA/N-AXIS/)
- [v6.0 Nomenclature](../../README.md#92-controlled-vocabulary--nomenclature-v60)
