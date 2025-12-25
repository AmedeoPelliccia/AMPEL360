# CI/ — Shared CI Wrappers, Reporters, and Pipeline Helpers

**Location:** `LC00_GENERAL/CI/`  
**Owner (AoR):** STK_DAB (Digital Applications & Blockchains)  
**Status:** ACTIVE

---

## Purpose

This directory contains **shared CI/CD utilities** that support automated testing, validation, and reporting across GitHub Actions workflows and other pipeline systems.

## Scope

### What belongs here:
- **CI workflow wrappers** and helper scripts
- **Test runners** and automation frameworks
- **Validation orchestrators** (gate runners, validator chains)
- **Report generators** (JSON, Markdown, HTML summaries)
- **Pipeline helpers** (artifact collectors, result aggregators)
- **PR-blocking gate implementations** for CI

### What does NOT belong here:
- GitHub workflow YAML files (place in `.github/workflows/`)
- Phase-specific tests (place in relevant LCxx directory)
- Test fixtures (place in FIXTURES/)
- General libraries (place in LIB/)

---

## Guidelines

1. **Automation**: CI utilities must be fully automatable (no manual intervention)
2. **Determinism**: Results must be reproducible across runs
3. **Reporting**: Generate actionable reports (errors, warnings, suggestions)
4. **Performance**: Keep CI runs fast and efficient
5. **Failure Modes**: Clear error messages and exit codes

---

## Expected Utilities

Key utilities that should be developed here:

- **Gate Runner**: Orchestrate multiple validation gates
- **Nomenclature Validator**: Run v6.0 naming checks in CI
- **Schema Validator**: Validate artifacts against schemas
- **Link Checker**: Verify ID references and trace links
- **Report Generator**: Generate PR comments and dashboards
- **Artifact Collector**: Gather and package CI outputs
- **Test Orchestrator**: Run phase-specific test suites
- **Evidence Generator**: Create CI evidence records

---

## CI Gate Types

Gates implemented for CI workflows:

### PR-Blocking Gates
- **Gate A — Intent Reference Validity**: Vision/mission/scope validation
- **Gate B — CIPP Determinism**: CIPP reference validation
- **Gate C — Outcome Trace Completeness**: Outcome traceability
- **Gate F — Portal Contract Validation**: AoR contract validation
- **Nomenclature Gate**: v6.0 naming standard enforcement
- **Schema Gate**: JSON/YAML schema validation
- **Link Gate**: ID reference integrity checking

### Non-Blocking Checks
- **Complexity Analysis**: Code complexity metrics
- **Documentation Coverage**: Documentation completeness
- **Best Practice Checks**: Coding standards and conventions

---

## Utility Organization

```
CI/
├── runners/
│   ├── gate_runner.py
│   ├── test_orchestrator.py
│   └── validator_chain.py
├── validators/
│   ├── nomenclature_validator.py
│   ├── schema_validator.py
│   ├── link_checker.py
│   └── contract_validator.py
├── reporters/
│   ├── json_reporter.py
│   ├── markdown_reporter.py
│   ├── html_reporter.py
│   └── pr_commenter.py
├── collectors/
│   ├── artifact_collector.py
│   ├── result_aggregator.py
│   └── evidence_packager.py
├── gates/
│   ├── gate0_nomenclature_vocab.py
│   ├── gate1_registry_trace.py
│   ├── gate2_change_impact.py
│   └── gate3_release_bundle.py
└── helpers/
    ├── ci_logger.py
    ├── exit_codes.py
    └── env_loader.py
```

---

## Usage

CI utilities are invoked by GitHub Actions:

```yaml
# Example GitHub Actions workflow step
- name: Run Nomenclature Gate
  run: |
    python LC00_GENERAL/CI/validators/nomenclature_validator.py \
      --path CAXS/ \
      --report-format markdown \
      --output gate_report.md
```

```python
# Example Python usage
from LC00_GENERAL.CI.runners import gate_runner
from LC00_GENERAL.CI.reporters import markdown_reporter

# Run gates
results = gate_runner.run_gates(
    gates=['nomenclature', 'schema', 'link'],
    path='CAXS/'
)

# Generate report
report = markdown_reporter.generate(results)
```

---

## Maintenance

- Keep CI utilities synchronized with gate policies
- Update validators when nomenclature or schemas change
- Optimize performance for fast CI runs
- Generate actionable error messages
- Document exit codes and failure modes
- Test CI utilities with representative artifacts
- Coordinate with STK_CM for gate policy changes

---

**References:**
- See parent README: `../README.md`
- GitHub Workflows: `.github/workflows/`
- Nomenclature Standard: Main README Section 10
- Portal Gates: Main README Section 6.9
- KNOTS Framework: Main README Section 7
