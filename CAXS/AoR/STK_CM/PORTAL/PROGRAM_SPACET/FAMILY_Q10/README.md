# STK_CM Portal — PROGRAM_SPACET / FAMILY_Q10

**AoR:** STK_CM  
**Program:** SPACET  
**Family:** Q10  
**Domain:** PROG_GOV / CM (Configuration Management)  
**Status:** Active  
**Primary Knots:** K01, K04, K06, K10

---

## 1. Purpose

This portal provides the **Configuration Management (CM) governance entry point** for the **SPACET program**
at **Family level (Q10)**.

It defines and enforces how Q10 baselines are:
- standardized (nomenclature, policies, templates),
- changed (controlled integration approvals),
- released (validated + frozen release candidates),
- and made audit-ready (traceability + evidence + signoffs + CERT clearance).

This portal is **family-scoped**: it applies rules consistently across Q10 variants and blocks, without
replacing the engineering portals of individual ATAs.

---

## 2. Scope

### In scope (Q10 family CM)
- Q10-specific **baseline governance** and release discipline
- Change control routing and cross-ATA clearance for Q10 baseline integrations
- Family-scoped registers (baseline manifests, CR logs, exceptions, signoffs, audit packs)
- CI gate monitoring and evidence packaging for Q10 releases and audits
- Controlled exports: **BRP “Releaseable”** and **Audit-ready baseline** bundles for Q10

### Out of scope
- Authoring primary engineering content within ATA chapters (owned by the relevant AoR portals)
- Replacing external tools; this portal references them through controlled links

---

## 3. Operating model (Knots)

### K01 — Standards (Family Q10)
**Purpose:** Define nomenclature, policies, templates  
**Output:** Standard release + enforcement rules  
**Gates:** nomenclature validation, schema validation

**Q10 note:** any Q10-specific vocabulary extensions (e.g., family/variant fields) must be versioned and
declared here, with enforcement rules updated accordingly.

---

### K04 — Change Control Gate
**Purpose:** Approve changes for integration  
**Output:** CR “Approved for integration”  
**Gates:** impact analysis complete, approval obtained, cross-ATA clearance

**Q10 note:** approvals must explicitly state whether the change is:
- **Family-wide** (impacts all Q10 variants), or
- **Variant-scoped** (impacts a subset only).

---

### K06 — Baseline Release Gate
**Purpose:** Validate and freeze release candidate  
**Output:** BRP “Releaseable”  
**Gates:** nomenclature compliance, uniqueness check, baseline integrity, CI validation pass

**Q10 note:** the freeze reference must identify:
- family scope (Q10),
- release candidate ID,
- included variants/blocks (if not “ALL”).

---

### K10 — Audit Gate
**Purpose:** Prepare audit-ready baseline  
**Output:** “Audit-ready baseline” + export  
**Gates:** traceability complete, evidence closure, signoff obtained, CERT clearance

**Q10 note:** CERT clearance must be unambiguous about scope:
- which Q10 baseline(s) are covered,
- which variants/blocks are included,
- and any conditions/limitations.

---

## 4. Stakeholder interfaces (cross-AoR dependencies)

This portal coordinates only with:
- **STK_PMO** — planning, milestones, reporting alignment
- **STK_SE** — interface/ICD coherence, requirements and architecture consistency
- **STK_SAF** — safety/security impact screening and gating inputs
- **STK_CERT** — evidence expectations, clearance statements, audit packaging
- **STK_DATA** — schema governance, register integrity, traceability data quality

---

## 5. Navigation (family-level)

### Start here
- `../LINKS/00_INDEX.md` (or local `./LINKS/00_INDEX.md` if replicated per family) — curated shortcuts
- `../LINKS/LINKS_REGISTER.csv` — source of truth for operational references

### Typical flows
- **Propose a Q10 change** → K04 workflow → approvals + cross-ATA clearance
- **Build a Q10 release candidate** → K06 gates → freeze → BRP “Releaseable”
- **Prepare Q10 for audit** → K10 gates → export bundle → CERT clearance

---

## 6. Family-level controls (minimum)

1. **PR-only** updates to governance artifacts and registers.
2. Any operational reference must be recorded in the **LINKS register**.
3. A Q10 baseline may be declared **Releaseable** only if K06 gates PASS and the baseline is frozen.
4. A Q10 baseline may be declared **Audit-ready** only if K10 gates PASS and CERT clearance is issued.
5. If Q10 standards introduce schema changes, **STK_DATA review is mandatory**.
6. If audit packaging or compliance evidence changes, **STK_CERT review is mandatory**.

---

## 7. Recommended family registers (pointers)

These registers are recommended for Q10 CM (paths may vary by your repository standard):
- **CR Register** (family-scoped)
- **Baseline Manifest Register** (all frozen baselines for Q10)
- **Exception/Deviation Register**
- **Signoff Register**
- **Audit Export Index**

> If these are implemented, they must be discoverable through the LINKS register and referenced from
> the family-level index.

---

## 8. Maintainers

**Owner:** STK_CM  
**Review cycle:** every baseline release (K06) and before audit gate (K10)

Cross-review requirements:
- STK_DATA: any schema/register/governance-of-data changes
- STK_CERT: any evidence / export / audit packaging changes
- STK_SE / STK_SAF / STK_PMO: as triggered by impact classification

