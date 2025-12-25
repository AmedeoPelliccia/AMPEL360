# CI Gates (LC00_GENERAL / MODEL=SW)

**Path:** `.../MODEL_SOFTWARE/LC00_GENERAL/CI/gates/`  
**Owner (AoR):** STK_CM (Configuration Management)  
**Scope:** Decision logic layer for CM-controlled CI gates, consuming collector outputs.

---

## 1. Purpose

This directory contains **gate decision logic** that evaluates collector outputs and enforces
Configuration Management policies during CI/CD workflows. Gates are the **decision layer**
that determine pass/fail outcomes for PRs and releases.

**Core CM Principles:**
- Maintain **baselines reproducible** (what is "the truth" at each version)
- Control **change** (what changes, why, who approves, what to revalidate)
- Ensure **integrity** (nomenclature/vocab, links/trace, registries)
- Produce **evidence/export packages** (release bundles, manifests, hashes)

---

## 2. Gate vs Collector Separation

| Aspect | Collectors (`../collectors/`) | Gates (`./`) |
|--------|------------------------------|--------------|
| **Purpose** | Gather and serialize data | Decide pass/fail |
| **Output** | Artifacts (JSON/CSV/MD) | Gate result + recommendation |
| **Policy** | None (data only) | Enforces thresholds |
| **Blocking** | Never | Can block PRs |
| **Owner** | STK_CM | STK_CM |

**Key principle:** Collectors emit signals; gates decide.

---

## 3. CM Gate Definitions

### Gate 0 — Format (Nomenclature/Vocab)

**Purpose:** Enforce v6.0 naming standard and controlled vocabulary compliance.

**Consumes:**
- `collect_nomenclature_tokens` output
- `collect_vocab_usage` output

**Checks:**
- All file paths follow v6.0 nomenclature standard
- All tokens are from controlled vocabulary
- No unknown or deprecated tokens

**Blocking:** Yes (PR cannot merge with violations)

---

### Gate 1 — Integrity (Registry/Trace)

**Purpose:** Ensure IDs are unique, registries consistent, and trace links valid.

**Consumes:**
- `collect_registry_deltas` output
- `collect_trace_edges` output
- `collect_trace_integrity` output

**Checks:**
- No duplicate IDs across registries
- All referenced IDs exist in SSOT
- No broken trace links (orphans, missing refs)
- Trace edges are bi-directional and consistent

**Blocking:** Yes (integrity failures block merge)

---

### Gate 2 — Impact (Change Analysis)

**Purpose:** Identify what LC/KNOT/AoR are impacted and require revalidation.

**Consumes:**
- `collect_change_impact_packet` output
- Changed file list

**Checks:**
- Impact analysis completed for all changed artifacts
- Affected AoRs identified and notified
- Revalidation requirements documented
- Coupling risks flagged (if applicable)

**Blocking:** Configurable (can be warning-only for low-impact changes)

---

### Gate 3 — Release Readiness

**Purpose:** Validate release bundles are reproducible and complete.

**Consumes:**
- `collect_release_manifest` output
- `collect_hashes` output
- `collect_release_notes` output

**Checks:**
- Bundle manifest includes all required artifacts
- All hashes match computed values
- Evidence index complete
- Release notes aggregated

**Applies:** Only when exporting/releasing (not on regular PRs)

**Blocking:** Yes (release cannot proceed without passing)

---

## 4. Gate Interface Contract

All gates must implement the following interface:

### Inputs
- Collector output artifacts (JSON)
- Gate configuration (thresholds, policies)
- CI context (branch/PR, commit SHA)

### Outputs
- `gate_result.json` with structured outcome
- Exit codes:
  - `0` — Gate passed
  - `1` — Gate failed (blocking)
  - `2` — Gate passed with warnings (non-blocking)
- Human-readable summary for PR comments

### Required Output Fields

```json
{
  "gate_id": "gate1_registry_trace_integrity",
  "run_id": "sha_timestamp",
  "status": "PASSED | FAILED | WARNING",
  "blocking": true,
  "checks": [
    {
      "check_id": "unique_ids",
      "status": "PASSED",
      "details": "No duplicate IDs found"
    }
  ],
  "summary": "Gate 1 passed: all integrity checks successful",
  "recommendations": [],
  "evidence": {
    "collector_outputs_consumed": ["collect_registry_deltas", "collect_trace_edges"],
    "artifacts_checked": 42
  }
}
```

---

## 5. Directory Structure

```
gates/
├── gate0_nomenclature_vocab.py    # Format gate
├── gate1_registry_trace.py        # Integrity gate
├── gate2_change_impact.py         # Impact analysis gate
├── gate3_release_bundle.py        # Release readiness gate
├── shared/
│   ├── gate_runner.py             # Gate orchestration
│   ├── result_formatter.py        # Output formatting
│   └── policy_loader.py           # Policy configuration
├── policies/
│   ├── default_policy.yaml        # Default thresholds
│   └── strict_policy.yaml         # Strict mode for releases
├── schemas/
│   └── gate_result_schema.json    # Output validation schema
└── fixtures/
    └── test_collector_outputs/    # Test fixtures
```

---

## 6. CM Change-Control Flow

The complete PR → baseline → export flow for CM:

```
┌─────────────────────────────────────────────────────────────────┐
│                    PR OPENED / UPDATED                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  COLLECTORS RUN (parallel)                                      │
│  ├── collect_nomenclature_tokens                                │
│  ├── collect_registry_deltas                                    │
│  ├── collect_trace_edges                                        │
│  └── collect_change_impact_packet                               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  GATES RUN (sequential, can short-circuit)                      │
│  ├── Gate 0: Nomenclature/Vocab    ──▶ FAIL = block PR          │
│  ├── Gate 1: Registry/Trace        ──▶ FAIL = block PR          │
│  └── Gate 2: Change/Impact         ──▶ WARN = flag for review   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  SIGNOFF (if gates pass)                                        │
│  ├── Required reviewers notified (based on impact)              │
│  ├── AoR owners approve changes to their scope                  │
│  └── CM approves baseline-affecting changes                     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  MERGE TO BASELINE BRANCH                                       │
│  ├── Baseline manifest updated                                  │
│  ├── Freeze point recorded                                      │
│  └── "Known-good" state captured                                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼ (when releasing)
┌─────────────────────────────────────────────────────────────────┐
│  RELEASE WORKFLOW                                               │
│  ├── collect_release_manifest                                   │
│  ├── collect_hashes                                             │
│  ├── Gate 3: Release Bundle        ──▶ FAIL = block release     │
│  └── Export packager builds bundle                              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  RELEASE ARTIFACTS                                              │
│  ├── Signed release bundle                                      │
│  ├── Manifest with hashes                                       │
│  ├── Evidence index                                             │
│  └── Audit log entry                                            │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. Usage in GitHub Actions

```yaml
# Example gate workflow step
jobs:
  ci-gates:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run Collectors
        run: |
          python CI/collectors/python/collect_nomenclature_tokens.py
          python CI/collectors/python/collect_registry_deltas.py
          python CI/collectors/python/collect_trace_edges.py
          python CI/collectors/python/collect_change_impact_packet.py
      
      - name: Run Gate 0 - Nomenclature
        run: python CI/gates/gate0_nomenclature_vocab.py
        
      - name: Run Gate 1 - Integrity
        run: python CI/gates/gate1_registry_trace.py
        
      - name: Run Gate 2 - Impact
        run: python CI/gates/gate2_change_impact.py
        continue-on-error: true  # Warning-only mode
```

---

## 8. MoSCoW (Gate Layer)

### Must Have
- Clear pass/fail/warning outcomes
- Configurable thresholds via policy files
- PR-blocking capability for critical gates
- Audit trail of gate decisions

### Should Have
- Policy-as-code with version control
- Gate bypass with approval workflow
- Integration with PR comment system
- Historical gate metrics

### Could Have
- ML-based anomaly detection
- Predictive impact scoring
- Automated signoff routing by severity

### Won't Have
- Manual intervention requirements in automated gates
- Hard-coded thresholds (use policy files)

---

## 9. References

- Collectors: `../collectors/README.md`
- PORTAL Gates: `../../PORTAL/gates/`
- Validators: `../validators/`
- Export Utilities: `../../EXPORT/`
- Nomenclature Standard: Main README Section 10 (v6.0)
- Portal Gates: Main system README `../../README.md` (see "Portal Gates" section)

---

**Status:** ACTIVE  
**Issue-Rev:** I01-R01
