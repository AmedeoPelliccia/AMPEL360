# STK_CM Portal — LINKS

## Purpose
Curated link hub for **Configuration Management (STK_CM)**.
Provides controlled entry points to:
- **K01 Standards** (nomenclature, policies, templates, enforcement)
- **K04 Change Control** (CR workflow, impact, approvals)
- **K06 Baseline Release** (release candidates, freeze refs, BRP packages)
- **K10 Audit** (traceability, evidence closure, signoffs, CERT clearance)
- Program registers, CI dashboards, and export bundles

This folder contains **references**, not primary engineering content.

## Governance
- **Owner (AoR):** STK_CM
- **Update method:** PR-only (no direct edits on main)
- **Validation:** LINKS_REGISTER must pass schema validation (LINKS_REGISTER.schema.json). CSV data is mapped to JSON format in CI before validation.
- **Review cadence:** at every Baseline Release (K06) and before Audit Gate (K10)

## Rules
1. No untracked links: every link must be in LINKS_REGISTER.csv
2. Links must be tagged with at least: `knot`, `context`, `scope`
3. Use `access_level` to signal restrictions (PUBLIC/INTERNAL/CONFIDENTIAL)
4. Deprecations must be marked `DEPRECATED` (do not delete; archive if needed)

## How to add a link
1) Add a new row in LINKS_REGISTER.csv
2) Ensure schema passes
3) Update 00_INDEX.md if it is a high-frequency shortcut
