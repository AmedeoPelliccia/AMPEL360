# STK_CM Portal — SPACET

**AoR:** STK_CM  
**Domain:** PROG_GOV / CM (Configuration Management)  
**Program:** SPACET  
**Status:** Active  
**Primary Knots:** K01, K04, K06, K10

---

## 1. Purpose

This portal is the **single entry point for Configuration Management** for the **SPACET** program within CAXS.  
It governs and operationalizes:

- **Standards** (nomenclature, policies, templates, enforcement rules)
- **Change Control** (approval of changes for integration)
- **Baseline Release** (validate + freeze release candidates)
- **Audit Readiness** (traceability, evidence closure, signoffs, CERT clearance)

This portal does **not** replace ATA-specific portals; it provides **program-level governance**, cross-ATA coherence, and audit-grade traceability.

---

## 2. Scope

### In scope
- Program baseline governance: naming, CM rules, release discipline, registers, audits
- Cross-ATA impact visibility and clearance tracking for integrated changes
- CI gate monitoring and evidence packaging for releases and audits
- Export bundles: BRP (Releaseable) and Audit-ready baseline packs

### Out of scope
- Authoring/maintaining primary engineering content per ATA (owned by the relevant AoR portals)
- Managing proprietary external tools beyond controlled linking/integration points

---

## 3. Operating model (Knots and outputs)

### K01 — Standards
**Purpose:** Define nomenclature, policies, templates  
**Output:** Standard release + enforcement rules  
**Gates:** nomenclature validation, schema validation

### K04 — Change Control Gate
**Purpose:** Approve changes for integration  
**Output:** CR “Approved for integration”  
**Gates:** impact analysis complete, approval obtained, cross-ATA clearance

### K06 — Baseline Release Gate
**Purpose:** Validate and freeze release candidate  
**Output:** BRP “Releaseable”  
**Gates:** nomenclature compliance, uniqueness check, baseline integrity, CI validation pass

### K10 — Audit Gate
**Purpose:** Prepare audit-ready baseline  
**Output:** “Audit-ready baseline” + export  
**Gates:** traceability complete, evidence closure, signoff obtained, CERT clearance

---

## 4. Stakeholder interfaces (cross-AoR)

The STK_CM portal coordinates only with the following cross-dependencies (no others):

- **STK_PMO** — planning, milestones, reporting alignment
- **STK_SE** — interfaces, architecture consistency, ICD coverage
- **STK_SAF** — safety/security impact screening and gating inputs
- **STK_CERT** — evidence expectations, clearance statements, audit-facing packaging
- **STK_DATA** — schema governance, register integrity, traceability data quality

---

## 5. Navigation

### Start here
- `./LINKS/00_INDEX.md` — curated shortcuts (K01/K04/K06/K10, CI, registers)
- `./LINKS/LINKS_REGISTER.csv` — source of truth for portal references

### Typical user actions
- **Propose/triage a change** → follow K04 workflow; ensure impact analysis and approvals
- **Prepare a release candidate** → execute K06 gates; freeze and publish BRP “Releaseable”
- **Prepare for audit** → execute K10; generate export bundle; obtain CERT clearance

---

## 6. Controls and compliance rules

### Governance rules (minimum)
1. **PR-only changes** to governance artifacts in this portal (no direct edits on main).
2. Any link used operationally must be registered in `./LINKS/LINKS_REGISTER.csv`.
3. Any baseline declared “Releaseable” must be frozen (immutable reference) and auditable.
4. Any “Audit-ready baseline” must include:
   - traceability matrix,
   - evidence index + closure,
   - signoff register,
   - CERT clearance statement.

### Evidence principles (baseline-level)
- Every gate produces **machine-readable reports** (JSON) plus a **human-readable summary** (MD).
- Every export bundle must be **reproducible** from referenced commits/tags and CI runs.

---

## 7. Working conventions (recommended)

### Identifiers
- Use stable IDs for: CRs, baselines, release candidates, export bundles, evidence items.
- Do not reuse identifiers for retired/deprecated items.

### Status discipline
- ACTIVE: in current operational use
- DEPRECATED: replaced but kept for traceability
- ARCHIVED: historical reference only

### Access levels
- PUBLIC / INTERNAL / CONFIDENTIAL must be explicit for links and exports.

---

## 8. How this portal is used across the lifecycle

**Standards (K01)**  
→ enable automated compliance and consistent authoring

**Change Control (K04)**  
→ prevents uncontrolled integration and ensures cross-AoR accountability

**Baseline Release (K06)**  
→ produces a frozen release candidate with BRP packaging and CI-backed integrity

**Audit Gate (K10)**  
→ produces an audit-ready baseline plus an export bundle suitable for inspection

---

## 9. Directory pointers

- `./LINKS/` — curated link hub + register (source of truth for operational references)
- (Add local folders under `./` only when they represent CM governance artifacts for SPACET,
  not duplicated engineering content.)

---

## 10. Maintainers

**Owner:** STK_CM  
**Review cycle:** at every baseline release (K06) and before audit gate (K10)

If an update affects schemas/registers, STK_DATA review is mandatory.  
If an update affects compliance/evidence/audit packaging, STK_CERT review is mandatory.

