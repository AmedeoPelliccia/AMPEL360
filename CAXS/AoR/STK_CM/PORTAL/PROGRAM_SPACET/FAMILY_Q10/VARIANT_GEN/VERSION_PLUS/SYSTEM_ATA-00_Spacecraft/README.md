
# STK_CM Portal — PROGRAM_SPACET / FAMILY_Q10 / VARIANT_GEN / VERSION_PLUS / SYSTEM_ATA-00_Spacecraft

**AoR:** STK_CM  
**Program:** SPACET  
**Family:** Q10  
**Variant:** GEN  
**Version Stream:** PLUS  
**System:** ATA-00 — Spacecraft  
**Domain:** PROG_GOV / CM (Configuration Management)  
**Status:** Active  
**Primary Knots:** K01, K04, K06, K10

---

## 1. Purpose

This system-level portal page defines **Configuration Management governance** for **ATA-00 (Spacecraft)**
within the **SPACET / Q10 / GEN / PLUS** stream.

It provides the controlled entry point to:
- **K01 Standards** — nomenclature, policies, templates, enforcement
- **K04 Change Control** — approve changes for integration
- **K06 Baseline Release** — validate and freeze release candidates (BRP)
- **K10 Audit Gate** — prepare audit-ready baselines and exports with CERT clearance

for **ATA-00 governance artifacts**, ensuring cross-ATA coherence and audit-grade traceability.

---

## 2. Scope (ATA-00 within PLUS)

### In scope
- ATA-00 governance assets used program-wide (baseline CM policy, nomenclature, registers, templates)
- Generated updates to governance artifacts (only where generation is authorized and traceable)
- Cross-ATA visibility: ATA-00 governance changes affect multiple ATAs; this page anchors the linkage

### Out of scope
- Primary engineering content authoring inside other ATA chapters (owned by their portals)
- Uncontrolled changes not routed through K04 and validated through K06

---

## 3. ATA-00 responsibilities (STK_CM)

ATA-00 under STK_CM acts as the **program governance baseline**:
- Nomenclature standard and vocabulary governance
- CM policy set (change control, baselines, release discipline)
- Master registers (CR log, baseline manifests, signoffs, audit exports)
- Audit trail conventions and evidence packaging rules
- Operational pathway: **Standards → Automation → Baseline releases → Audits → CI**

---

## 4. Operating model (Knots) — ATA-00

### K01 — Standards
**Purpose:** Define nomenclature, policies, templates  
**Output:** Standard release + enforcement rules  
**Gates:** nomenclature validation, schema validation

**ATA-00 note:** changes to nomenclature/policy/templates are baseline-governance impacting and require
cross-ATA visibility by default.

---

### K04 — Change Control Gate
**Purpose:** Approve changes for integration  
**Output:** CR “Approved for integration”  
**Gates:** impact analysis complete, approval obtained, cross-ATA clearance

**ATA-00 note:** impact analysis must explicitly identify:
- governance assets affected (policies, templates, registers, validators),
- cross-ATA consequences (naming/metadata changes affect all ATAs),
- migration requirements (if any).

---

### K06 — Baseline Release Gate
**Purpose:** Validate and freeze release candidate  
**Output:** BRP “Releaseable”  
**Gates:** nomenclature compliance, uniqueness check, baseline integrity, CI validation pass

**ATA-00 note:** K06 must validate both:
- governance content, and
- enforcement tooling bindings (validator versions, schema sets, rule severities).

---

### K10 — Audit Gate
**Purpose:** Prepare audit-ready baseline  
**Output:** “Audit-ready baseline” + export  
**Gates:** traceability complete, evidence closure, signoff obtained, CERT clearance

**ATA-00 note:** CERT clearance must confirm the audit pack includes:
- standards version binding,
- gate reports (K01/K04/K06 outputs as applicable),
- signoff register,
- export reproducibility statement.

---

## 5. Cross-AoR dependencies (only)

This portal coordinates only with:
- **STK_PMO** — schedule, release readiness, reporting
- **STK_SE** — interface coherency, ICD impacts, architecture alignment
- **STK_SAF** — safety/security implications (as triggered by impact classification)
- **STK_CERT** — evidence expectations, clearance statements, audit packaging
- **STK_DATA** — schema governance, register integrity, traceability data quality

---

## 6. Required pointers (LINKS hub)

All operational references for ATA-00 under this stream must be discoverable through the applicable
LINKS register (nearest in the tree), including:
- Standards (nomenclature/policy/templates + enforcement)
- CR queue and impact matrix
- Release candidate freeze refs and BRP packages
- Traceability matrix, evidence index, signoff register, CERT clearance statement

---

## 7. Controls (minimum)

1. PR-only updates to governance assets and registers.
2. No change integrates without K04 “Approved for integration”.
3. No baseline is “Releaseable” without full K06 pass and a freeze reference.
4. No baseline is “Audit-ready” without K10 pass and CERT clearance.
5. ATA-00 changes that alter schemas or registers require **STK_DATA review**.
6. ATA-00 changes affecting evidence/audit packaging require **STK_CERT review**.

---

## 8. Maintainers

**Owner:** STK_CM  
**Review cycle:** every K06 release candidate and before any K10 audit export
