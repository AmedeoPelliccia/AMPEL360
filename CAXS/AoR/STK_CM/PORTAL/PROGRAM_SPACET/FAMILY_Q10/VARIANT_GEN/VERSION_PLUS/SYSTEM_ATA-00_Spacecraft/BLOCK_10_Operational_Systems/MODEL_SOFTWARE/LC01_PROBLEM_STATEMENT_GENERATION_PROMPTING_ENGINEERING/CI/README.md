# CI — Validators, Linters, GitHub Actions Helpers Specific to LC01

**Parent Context:** LC01_PROBLEM_STATEMENT_GENERATION_PROMPTING_ENGINEERING  
**Purpose:** Continuous Integration tools and automation for LC01 artifacts  
**Status:** Active (Portal Baseline)

---

## 1. Purpose

This directory contains **CI/CD automation** for:
- Validation of LC01 artifacts
- Linting of prompts, schemas, and code
- GitHub Actions workflow helpers
- PR gate enforcement
- Automated testing and reporting

---

## 2. What Belongs Here

### Validators
- Nomenclature validators (v6.0 compliance)
- Schema validators (JSON/YAML validation)
- Prompt catalog validators
- Traceability link validators
- Evidence binding validators

### Linters
- Prompt quality linters
- Code style linters (Python, JavaScript, etc.)
- YAML/JSON syntax linters
- Documentation linters
- Naming convention linters

### GitHub Actions Helpers
- Reusable workflow components
- Custom actions for LC01 validation
- Test execution helpers
- Report generation utilities
- Notification helpers

### PR Gate Scripts
- Pre-commit hooks
- PR validation scripts
- Blocking gate enforcement
- Evidence collection scripts

---

## 3. Validation Categories

### Nomenclature Validation
- Filename format compliance
- Token validity (ATA, PROGRAM, FAMILY, etc.)
- Required field presence
- Naming pattern consistency

### Schema Validation
- JSON Schema compliance
- YAML structure validation
- Required field checking
- Data type validation
- Constraint enforcement

### Content Validation
- Prompt metadata completeness
- Problem statement structure
- Traceability link validity
- Reference integrity
- Version consistency

### Code Quality
- Style guide compliance
- Security best practices
- Performance anti-patterns
- Error handling coverage
- Documentation completeness

---

## 4. CI Workflows

### On Every Push
1. Run nomenclature validators
2. Run schema validators
3. Run linters
4. Run unit tests
5. Generate validation report

### On Pull Request
1. Run full validation suite
2. Run regression tests (from EVAL/)
3. Check traceability completeness
4. Validate evidence bindings
5. Enforce PR gates (block on critical failures)

### Nightly/Scheduled
1. Run comprehensive test suites
2. Run performance benchmarks
3. Check for schema drift
4. Validate golden sets
5. Generate compliance reports

---

## 5. Gate Enforcement

### Blocking Gates (PR-blocking)
- Nomenclature violations
- Schema validation failures
- Broken traceability links
- Failed regression tests
- Security vulnerabilities

### Warning Gates (non-blocking)
- Style guide violations
- Performance degradation
- Missing documentation
- Code complexity issues

### Manual Review Gates
- Significant prompt changes
- New schema introductions
- Policy gate modifications
- Breaking API changes

---

## 6. Naming Conventions

Follow v6.0 nomenclature:
- `MODEL=SW`
- `PHASE=LC01`
- `CATEGORY=INTERNAL_PRODUCTION` for CI scripts
- `TYPE` as appropriate

**Example:**
```
00_AMPEL360_SPACET_Q10_BASELINE_PLUS_SW_10_LC01_K01_STK_DAB__nomenclature-validator_INTERNAL_PRODUCTION_SPEC_I01-R01_ACTIVE.py
00_AMPEL360_SPACET_Q10_BASELINE_PLUS_SW_10_LC01_K01_STK_DAB__schema-validator_INTERNAL_PRODUCTION_SPEC_I01-R01_ACTIVE.py
```

---

## 7. GitHub Actions Integration

### Workflow Files
Store workflow definitions in `.github/workflows/`

Reference LC01 CI scripts:
```yaml
- name: Validate LC01 Nomenclature
  run: |
    python CAXS/.../LC01.../CI/nomenclature_validator.py
```

### Custom Actions
Create reusable actions for common tasks:
- Prompt validation action
- Schema validation action
- Traceability check action
- Evidence validation action

---

## 8. Validation Reports

Validators must generate:
- Clear pass/fail status
- Detailed error messages
- Location of violations (file, line)
- Suggested fixes (where possible)
- Summary statistics

Report formats:
- Console output (for CI logs)
- JSON (for tooling integration)
- Markdown (for PR comments)
- HTML (for dashboards)

---

## 9. Integration Points

**Inputs:**
- PROMPTS/ for prompt validation
- SCHEMAS/ for schema validation
- ENGINES/ for code validation
- AGENTS/ for agent validation
- EVAL/ for test execution

**Outputs:**
- Validation reports
- Test results
- Lint reports
- Evidence records
- PR gate status

**Integration:**
- GitHub Actions workflows
- PR comment bot
- Status badges
- Dashboard updates

---

## 10. Testing

CI tools must be tested:
- Positive test cases (valid inputs)
- Negative test cases (invalid inputs)
- Edge cases
- Performance under load
- Integration with GitHub Actions

---

## 11. Performance

CI scripts should:
- Run quickly (target < 5 min for full suite)
- Run incrementally (validate only changed files when possible)
- Cache dependencies
- Parallelize where feasible
- Provide progress feedback

---

## 12. Documentation

Each CI tool must document:
- Purpose and scope
- Usage instructions
- Configuration options
- Exit codes and their meanings
- Error messages and resolutions
- Performance characteristics

---

## 13. Maintenance

Regularly:
- Update validators for new requirements
- Add tests for new validation rules
- Optimize performance
- Update documentation
- Review and tune gate thresholds
- Align with latest GitHub Actions features

---

## 14. Example Validators

### Nomenclature Validator
```python
# Validates v6.0 filename format
# Checks all tokens against allowlists
# Enforces naming invariants
# Reports violations with context
```

### Schema Validator
```python
# Validates JSON/YAML against schemas
# Checks required fields
# Validates data types and formats
# Reports schema violations
```

### Traceability Validator
```python
# Checks traceability links
# Validates reference integrity
# Ensures evidence bindings
# Reports broken links
```

---
