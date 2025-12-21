# INDEX — BLOCK_10_Operational_Systems / MODEL_SOFTWARE (STK_CM)

**Path:** `.../SYSTEM_ATA-00_Spacecraft/BLOCK_10_Operational_Systems/MODEL_SOFTWARE/`  
**Owner (AoR):** STK_CM  
**Scope:** internal software/tooling used to enforce operational CM controls for Block 10

---

## Purpose

This folder hosts **internal production** software artifacts (scripts/config) that support:
- **K06** — data governance validation (schemas, identifiers, SSOT registers)
- **K08** — evidence packaging & release snapshots (operational snapshots, export bundles)
- **K13** — secure operations controls (optional: key management hooks, access control checks)
- **K09/K11/K14** — operational readiness and sustainment evidence automation (as applicable)

---

## Subfolders

- [INTERNAL_PRODUCTION/](./INTERNAL_PRODUCTION/) — scripts, configs, validators, packagers
- [EVIDENCE/](./EVIDENCE/) — outputs produced by tooling (reports/logs/receipts)
- [CONFIG/](./CONFIG/) — reusable profiles (CI profiles, validation profiles, bundle profiles)
- [TEST_FIXTURES/](./TEST_FIXTURES/) — non-sensitive fixtures for validation and regression tests
- [DOCS/](./DOCS/) — toolchain documentation (how to run, expected inputs/outputs)

---

## Recommended internal-production modules (by KNOT)

### K06 — Data governance validators
- nomenclature validator (filenames/metadata)
- registry schema validator
- SSOT consistency checker (cross-register integrity)
- uniqueness/identifier collision checks

### K08 — Snapshot and packaging builders
- release snapshot builder (freeze refs, manifests)
- evidence index generator (closure checks)
- export bundle builder (structure + checksums)
- audit-pack assembler (operational bundle completeness)

### K13 — Secure-ops hooks (only if used)
- signing integration hooks (no keys stored here)
- checksum verification tools
- access policy linting for bundle destinations/channels

---

## Notes / Controls

1. **No secrets** (keys/tokens) stored in this tree. Reference secure stores.
2. Tool outputs belong under `./EVIDENCE/` (not mixed with scripts).
3. Any profile that affects release gating must be versioned and traceable to baseline snapshots.

