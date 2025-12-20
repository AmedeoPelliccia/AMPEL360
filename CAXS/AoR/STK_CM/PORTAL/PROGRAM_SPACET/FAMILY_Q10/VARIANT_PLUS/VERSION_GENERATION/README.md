# STK_CM Portal — PROGRAM_SPACET / FAMILY_Q10 / VARIANT_PLUS / VERSION_GENERATION

**AoR:** STK_CM  
**Program:** SPACET  
**Family:** Q10  
**Variant:** PLUS  
**Version Stream:** GENERATION  
**Domain:** PROG_GOV / CM (Configuration Management)  
**Status:** Active  
**Primary Knots:** K01, K04, K06, K10

---

## 1. Purpose

This portal defines the **Configuration Management governance** for the **GENERATION version stream**
within **SPACET / Q10 / PLUS**.

GENERATION is the stream where **candidate changes and generated artifacts** are brought under control,
validated, and promoted through the CM knots:

- **K01 Standards** → define/enforce rules and templates used by generation
- **K04 Change Control** → approve changes for integration
- **K06 Baseline Release** → validate and freeze a release candidate
- **K10 Audit Gate** → package an audit-ready baseline + export with CERT clearance

This stream exists to ensure automation and generation remain **deterministic, reproducible, and auditable**.

---

## 2. Scope (GENERATION stream)

### In scope
- Version-scoped governance for generated outputs destined for integration into PLUS baselines
- Enforcement of naming, schema, uniqueness, and baseline integrity on generated content
- Registers and evidence required to justify generation and promotion decisions
- CI gate monitoring and packaging for release candidates and audit packs

### Out of scope
- Authoring engineering content outside CM governance (handled in ATA and other AoR portals)
- Uncontrolled experimentation without CRs and gate pass records

---

## 3. Operating model (Knots)

### K01 — Standards (GENERATION)
**Purpose:** Define nomenclature, policies, templates  
**Output:** Standard release + enforcement rules  
**Gates:** nomenclature validation, schema validation

**GENERATION rule:** generation pipelines must reference:
- the exact **standards version** used,
- and the exact **schema versions** used for validation.

---

### K04 — Change Control Gate (GENERATION promotions)
**Purpose:** Approve changes for integration  
**Output:** CR “Approved for integration”  
**Gates:** impact analysis complete, approval obtained, cross-ATA clearance

**GENERATION rule:** any promotion of generated content requires a CR that declares:
- generation source (pipeline/run ID or generator reference),
- scope of generated artifacts (paths/IDs),
- intended propagation (GENERATION → baseline candidate),
- evidence plan for K06/K10.

---

### K06 — Baseline Release Gate (Release Candidate in GENERATION)
**Purpose:** Validate and freeze release candidate  
**Output:** BRP “Releaseable”  
**Gates:** nomenclature compliance, uniqueness check, baseline integrity, CI validation pass

**GENERATION rule:** the BRP must include:
- generator identity reference (tool version / pipeline version),
- validation reports (nomenclature, uniqueness, integrity, CI),
- and a freeze reference binding the candidate baseline.

---

### K10 — Audit Gate (GENERATION audit packaging)
**Purpose:** Prepare audit-ready baseline  
**Output:** “Audit-ready baseline” + export  
**Gates:** traceability complete, evidence closure, signoff obtained, CERT clearance

**GENERATION rule:** audit readiness must demonstrate:
- traceability from generated artifacts to CR approvals and CI pass,
- closure of evidence for generation correctness and governance compliance,
- explicit CERT clearance covering the GENERATION scope exported.

---

## 4. Required evidence (GENERATION-specific)

GENERATION baselines must carry, at minimum, evidence for:
- **Standards binding:** which naming and schema rules were used
- **Generation provenance:** generator/pipeline identity (version) and run reference
- **Determinism:** ability to reproduce the same outputs from the same inputs (where applicable)
- **Validation outputs:** gate reports and CI summaries included in BRP/audit exports

> The portal does not prescribe the toolchain, but it requires that provenance and validation evidence
> be captured and exportable.

---

## 5. Stakeholder interfaces (cross-AoR dependencies)

This portal coordinates only with:
- **STK_PMO** — schedule and delivery alignment for generated baselines
- **STK_SE** — cross-ATA interface integrity and ICD impacts
- **STK_SAF** — safety/security screening when generated outputs affect safety-relevant scope
- **STK_CERT** — evidence expectations, export packaging, clearance statements
- **STK_DATA** — schema governance, register integrity, traceability data quality

---

## 6. Navigation

### Start here
- Parent links hub:
  - `../../LINKS/00_INDEX.md`
  - `../../LINKS/LINKS_REGISTER.csv`

### Typical actions
- **Run generation → propose promotion** (create CR) → K04 approvals
- **Validate candidate baseline** → K06 gates → freeze → BRP “Releaseable”
- **Prepare for audit** → K10 gates → export bundle → CERT clearance

---

## 7. Controls (minimum)

1. **PR-only** updates to governance artifacts and registers.
2. Any operational shortcut must be recorded in the LINKS register.
3. No generated content is promoted without a CR passing K04 (Approved for integration).
4. No baseline is **Releaseable** without passing all K06 gates and recording a freeze reference.
5. No baseline is **Audit-ready** without passing all K10 gates and receiving CERT clearance.
6. Schema/register changes require **STK_DATA review**; audit packaging changes require **STK_CERT review**.

---

## 8. Maintainers

**Owner:** STK_CM  
**Review cycle:** at every K06 release candidate and before any K10 audit export

Cross-review requirements:
- STK_DATA: any schema/register/data-governance modifications
- STK_CERT: any evidence/export/audit packaging modifications
- STK_SE / STK_SAF / STK_PMO: as triggered by declared impact

