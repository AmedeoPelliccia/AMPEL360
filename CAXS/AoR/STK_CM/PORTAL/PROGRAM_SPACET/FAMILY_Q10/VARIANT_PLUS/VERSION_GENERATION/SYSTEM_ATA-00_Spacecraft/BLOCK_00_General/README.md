# STK_CM Portal — PROGRAM_SPACET / FAMILY_Q10 / VARIANT_PLUS / VERSION_GENERATION / SYSTEM_ATA-00_Spacecraft / BLOCK_00_General

**AoR:** STK_CM  
**Program:** SPACET  
**Family:** Q10  
**Variant:** PLUS  
**Version Stream:** GENERATION  
**System:** ATA-00 — Spacecraft  
**Block:** 00 — General  
**Domain:** PROG_GOV / CM (Configuration Management)  
**Status:** Active  
**Primary Knots:** K01, K04, K06, K10

---

## 1. Purpose

This block page defines how **ATA-00 / Block 00 (General)** is governed under **STK_CM** for the
**SPACET Q10 PLUS — GENERATION** stream.

Block 00 is the **governance nucleus** for program-wide configuration management:
- standards and enforcement (K01),
- change approval discipline (K04),
- baseline release freeze discipline (K06),
- audit-ready packaging (K10).

It exists to ensure that any governance artifact change remains **controlled, reproducible, and auditable**.

---

## 2. Scope (Block 00 — General)

### In scope
- Nomenclature standard and controlled vocabularies (program/family/variant fields, status fields)
- CM policies: change control, baseline rules, release discipline, deviation/waiver handling
- Templates: front-matter, registers, manifests, checklists (K01 outputs)
- Program registers: CR log, baseline manifests, signoff register, audit export index
- Gate outputs and reports: validation summaries and machine-readable evidence

### Out of scope
- ATA-specific engineering deliverables outside governance (owned by ATA portals and relevant AoRs)
- Any change not passing K04 before integration

---

## 3. Required artifacts (minimum set)

Block 00 should expose (directly or via LINKS register) the following minimum set:

### Standards (K01)
- Nomenclature standard (versioned)
- Schema registry (versioned)
- Template registry (versioned)
- Enforcement rules / validators (versioned)

### Change control (K04)
- CR queue/board reference
- Impact analysis matrix reference (cross-ATA)
- Approval/signoff evidence locations

### Baseline release (K06)
- Current Release Candidate (RC) reference
- Freeze reference(s) for the RC
- BRP “Releaseable” packages index

### Audit (K10)
- Traceability matrix (latest baseline)
- Evidence index + closure report
- Signoff register
- CERT clearance statement
- Audit export bundle index

> Source of truth for discoverability: LINKS_REGISTER in the nearest LINKS hub.

---

## 4. Gate rules applied in this block

### K01 — Standards
**Gates:** nomenclature validation, schema validation  
**Outcome:** Standard release + enforcement rules

### K04 — Change Control Gate
**Gates:** impact analysis complete, approval obtained, cross-ATA clearance  
**Outcome:** CR “Approved for integration”

### K06 — Baseline Release Gate
**Gates:** nomenclature compliance, uniqueness check, baseline integrity, CI validation pass  
**Outcome:** BRP “Releaseable”

### K10 — Audit Gate
**Gates:** traceability complete, evidence closure, signoff obtained, CERT clearance  
**Outcome:** “Audit-ready baseline” + export

---

## 5. Cross-AoR dependencies (only)

- **STK_PMO** — schedule/readiness, reporting requirements
- **STK_SE** — cross-ATA interfaces, ICD consistency, architecture alignment
- **STK_SAF** — safety/security implications as triggered by impact classification
- **STK_CERT** — evidence expectations, clearance statements, audit packaging
- **STK_DATA** — schema governance, register integrity, traceability data quality

---

## 6. Controls (minimum)

1. PR-only changes to Block 00 governance artifacts and registers.
2. Any operational shortcut must be registered in the LINKS register.
3. No integration without K04 “Approved for integration”.
4. No BRP without K06 pass + freeze reference.
5. No audit-ready baseline without K10 pass + CERT clearance.
6. Schema/register changes require STK_DATA review; evidence/export changes require STK_CERT review.

---

## 7. Maintainers

**Owner:** STK_CM  
**Review cycle:** at every K06 release candidate and before any K10 audit export

