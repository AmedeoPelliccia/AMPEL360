# CI Collectors (LC00_GENERAL / MODEL=SW)

**Path:** `.../MODEL_SOFTWARE/LC00_GENERAL/CI/collectors/`  
**Owner (AoR):** STK_CM (Configuration Management)  
**Scope:** Cross-phase CI data collection for portal-grade reporting, traceability, and gating.

---

## 1. Purpose

This directory contains **collector components** used by CI workflows to **gather, normalize, and emit**
machine-readable and human-readable artifacts needed by:

- phase gates (LC00–LCxx),
- PR summaries and dashboards,
- traceability graphs (Req ↔ Model ↔ Evidence ↔ KNOT),
- compliance/audit reporting (nomenclature, vocab, schema conformance),
- change impact signals (what must be revalidated and by whom).

Collectors do not "decide"; they **collect and serialize**. Decision logic belongs in `CI/gates/` or validators.

---

## 2. What a Collector Is

A **collector** is a small, deterministic CI component that:
1. reads repository artifacts (files, indexes, registries, manifests),
2. extracts structured signals,
3. emits normalized outputs into a standard folder (workspace artifact area),
4. returns a clear exit code and a concise summary.

Collectors must be safe to run in CI on PRs:
- no destructive actions,
- no reliance on external state (unless explicitly allowed by policy),
- deterministic results for the same inputs.

---

## 3. Scope (What Belongs Here)

Typical collectors include:

### 3.1 Metadata & Nomenclature Collectors
- enumerate changed files and parse v6.0 tokens,
- collect controlled vocabulary usage stats,
- detect unknown tokens and emit reports.

### 3.2 Registry Collectors
- aggregate registry entries (IDs, versions, owners),
- collect missing/duplicate IDs,
- build "registry delta" reports for PRs.

### 3.3 Trace Collectors
- build/update trace edges (Req↔KNOT, Model↔Req, Evidence↔Req),
- emit a normalized trace edge list (CSV/JSON),
- compute link integrity stats (broken links, orphans).

### 3.4 Coverage Collectors
- collect verification mappings (req→verification method),
- collect test coverage signals (where available),
- emit coverage matrices/deltas.

### 3.5 Change/Impact Collectors
- compute impacted AoRs and KNOTs from changed artifacts,
- collect coupling risk signals (if coupling tables exist),
- emit an "impact packet" used by gates and reviewers.

---

## 4. Out of Scope

- Gate decision logic (pass/fail thresholds) beyond minimal sanity checks
- Heavy validation (belongs in `VALIDATORS/` or `CI/gates/`)
- Publishing or exporting final baselines
- Non-software approvals/signoffs

---

## 5. Required Collector Interface (Standard Contract)

All collectors in this folder must implement the following contract:

### Inputs
- repository checkout (read-only)
- CI context (branch/PR, commit SHA)
- optional configuration file (preferred) or environment variables

### Outputs
- `artifacts/` emitted in a predictable layout (JSON/CSV/MD)
- one-line summary suitable for PR comment bodies
- exit codes:
  - `0` success
  - `2` success with warnings (non-blocking; gate decides)
  - `1` failure (collector itself failed; infrastructure issue)

### Mandatory Output Fields (for JSON Summaries)
- `collector_id`
- `run_id` (sha + timestamp)
- `inputs` (paths scanned / patterns)
- `counts` (files scanned, records emitted)
- `warnings[]`
- `errors[]`

---

## 6. Recommended Sub-structure

```
collectors/
├── python/           # Python collectors
├── node/             # NodeJS collectors
├── shared/           # shared utilities used by collectors
├── schemas/          # output schemas for collector JSON
└── fixtures/         # minimal tests for collectors
```

If you keep collectors flat, ensure each collector name is globally unique.

---

## 7. Naming Convention

Name collectors by **what they collect**, not by the pipeline step name:

- `collect_changed_files.*`
- `collect_nomenclature_tokens.*`
- `collect_registry_deltas.*`
- `collect_trace_edges.*`
- `collect_trace_integrity.*`
- `collect_coverage_matrix.*`
- `collect_impact_packet.*`
- `collect_release_manifest.*`
- `collect_hashes.*`
- `collect_release_notes.*`

Emit outputs under a stable prefix:

```
artifacts/collectors/<collector_id>/...
```

---

## 8. CM-Specific Collectors

For Configuration Management (STK_CM), the following collectors are essential:

### Gate 0 — Nomenclature/Vocab
- `collect_nomenclature_tokens` — Parse v6.0 naming tokens from changed files
- `collect_vocab_usage` — Collect controlled vocabulary usage stats

### Gate 1 — Registry/Trace Integrity
- `collect_registry_deltas` — Aggregate registry entry changes
- `collect_trace_edges` — Build trace edge mappings
- `collect_trace_integrity` — Verify link consistency (broken refs, orphans)

### Gate 2 — Change/Impact
- `collect_change_impact_packet` — Compute impacted LC/KNOT/AoR from changes

### Gate 3 — Release Readiness
- `collect_release_manifest` — Build reproducible bundle manifest
- `collect_hashes` — Generate SHA256 hashes for release artifacts
- `collect_release_notes` — Aggregate release notes from PRs

---

## 9. MoSCoW (Collector Layer)

### Must Have
- deterministic execution
- normalized JSON output + concise MD summary
- clear exit codes and error reporting
- no side effects beyond artifact emission

### Should Have
- output schemas with validation
- unit tests with fixtures
- support for "changed files only" mode on PRs

### Could Have
- performance profiling metrics
- optional incremental caching (CI-scoped only)

### Won't Have
- policy decisions (thresholds) hard-coded in collectors

---

## 10. Example Collector Output

```json
{
  "collector_id": "collect_nomenclature_tokens",
  "run_id": "abc123_2024-12-25T21:00:00Z",
  "inputs": {
    "paths_scanned": ["CAXS/AoR/STK_CM/**"],
    "patterns": ["*.md", "*.yaml"]
  },
  "counts": {
    "files_scanned": 42,
    "records_emitted": 128,
    "tokens_valid": 125,
    "tokens_unknown": 3
  },
  "warnings": [
    "Unknown token 'INVALID_LC99' in file CAXS/example.md:15"
  ],
  "errors": [],
  "summary": "Scanned 42 files, found 128 tokens (3 unknown)"
}
```

---

## 11. References

- Portal CI architecture: `../README.md`
- CI Gates: `../gates/` (if implemented)
- Validators: `../../VALIDATORS/` (or phase-specific)
- PORTAL Gate Engine: `../../PORTAL/gates/`
- Trace model: repository trace/registry specifications (as applicable)
- Nomenclature Standard: Main README Section 10 (v6.0)
- KNOTS Framework: Main README Section 7

---

**Status:** ACTIVE  
**Issue-Rev:** I01-R01
