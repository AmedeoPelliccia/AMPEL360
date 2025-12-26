# STK_CM Portal — PROGRAM_SPACET / FAMILY_Q10 / VARIANT_GEN

**AoR:** STK_CM  
**Program:** SPACET  
**Family:** Q10  
**Variant:** GEN  
**Domain:** PROG_GOV / CM (Configuration Management)  
**Status:** Active  
**Primary Knots:** K01, K04, K06, K10

---

## 1. Purpose

This portal is the **Configuration Management (CM) entry point** for the **SPACET Q10 family** under the
**VARIANT_GEN** baseline stream.

It governs how the PLUS stream is:
- standardized (K01),
- integrated (K04),
- released (K06),
- and made audit-ready (K10),

with explicit control of **variant-scoped** impacts and cross-ATA coherence.

---

## 2. Variant scope and intent (GEN)

### What VARIANT_GEN means here
VARIANT_GEN represents a **variant-specific baseline stream** for Q10 used to manage enhancements and
additive capabilities relative to a reference baseline (e.g., BASELINE or other declared parent).

This portal ensures GEN changes are:
- traceable to CRs and approvals,
- isolated/controlled when not intended for family-wide propagation,
- and releasable/auditable with deterministic freeze references.

### What PLUS is not
- It is not a substitute for ATA engineering portals.
- It is not an unconstrained “experimental” branch; integration is gate-controlled.

---

## 3. Operating model (Knots)

### K01 — Standards (PLUS stream)
**Purpose:** Define nomenclature, policies, templates  
**Output:** Standard release + enforcement rules  
**Gates:** nomenclature validation, schema validation

**PLUS stream rule:** any additional PLUS-only vocabularies or naming exceptions must be:
- explicitly versioned,
- enforced in validation rules,
- and documented with rationale.

---

### K04 — Change Control Gate
**Purpose:** Approve changes for integration  
**Output:** CR “Approved for integration”  
**Gates:** impact analysis complete, approval obtained, cross-ATA clearance

**PLUS stream rule:** every CR must declare one of:
- **PLUS-only** (does not propagate to other variants),
- **Candidate for family adoption** (requires explicit follow-up CR for propagation).

---

### K06 — Baseline Release Gate
**Purpose:** Validate and freeze release candidate  
**Output:** BRP “Releaseable”  
**Gates:** nomenclature compliance, uniqueness check, baseline integrity, CI validation pass

**PLUS stream rule:** the freeze reference must bind:
- family (Q10),
- variant (PLUS),
- release candidate ID,
- included ATA scopes (if partial),
- and the standards version used to validate the release.

---

### K10 — Audit Gate
**Purpose:** Prepare audit-ready baseline  
**Output:** “Audit-ready baseline” + export  
**Gates:** traceability complete, evidence closure, signoff obtained, CERT clearance

**PLUS stream rule:** CERT clearance must explicitly state:
- the baseline scope is **VARIANT_GEN**,
- whether it is audit-ready for internal QA only or external audit (as applicable),
- and any constraints on operational use.

---

## 4. Stakeholder interfaces (cross-AoR dependencies)

This portal coordinates only with:
- **STK_PMO** — milestones, reporting, prioritization for PLUS stream deliverables
- **STK_SE** — interface consistency (ICDs), architecture alignment, cross-ATA impacts
- **STK_SAF** — safety/security screening for PLUS changes and risk gating inputs
- **STK_CERT** — evidence expectations, export bundle structure, clearance statements
- **STK_DATA** — schema governance, registers integrity, traceability data quality

---

## 5. Navigation (variant-level)

### Start here
- `./LINKS/00_INDEX.md` (if present) or parent LINKS:
  - `../LINKS/00_INDEX.md`
  - `../LINKS/LINKS_REGISTER.csv`

### Typical flows
- **Submit a PLUS change** → K04 (impact + approvals + cross-ATA clearance)
- **Prepare a PLUS release candidate** → K06 (validate + freeze) → BRP “Releaseable”
- **Prepare PLUS for audit** → K10 (traceability + evidence closure + signoffs) → CERT clearance

---

## 6. Variant controls (minimum)

1. **PR-only** changes to governance artifacts and registers in this variant stream.
2. Any operational shortcut must be registered in the **LINKS register**.
3. PLUS changes must be explicitly scoped (PLUS-only vs candidate for propagation).
4. No baseline is **Releaseable** without passing all K06 gates and recording a freeze reference.
5. No baseline is **Audit-ready** without passing all K10 gates and receiving CERT clearance.
6. Schema or register changes require **STK_DATA review**; audit packaging changes require **STK_CERT review**.

---

## 7. Recommended variant registers (pointers)

Recommended registers for VARIANT_GEN CM (paths may vary by your repository standard):
- PLUS **CR Register** (variant-scoped)
- PLUS **Baseline Manifest Register** (frozen baselines for PLUS)
- PLUS **Exception/Deviation Register**
- PLUS **Signoff Register**
- PLUS **Audit Export Index**

All of the above must be discoverable through the LINKS register.

---

## 8. Maintainers

**Owner:** STK_CM  
**Review cycle:** every PLUS baseline release (K06) and before any audit gate (K10)

Cross-review requirements:
- STK_DATA: schema/register/data-governance changes
- STK_CERT: evidence/export/audit packaging changes
- STK_SE / STK_SAF / STK_PMO: as triggered by impact classification

