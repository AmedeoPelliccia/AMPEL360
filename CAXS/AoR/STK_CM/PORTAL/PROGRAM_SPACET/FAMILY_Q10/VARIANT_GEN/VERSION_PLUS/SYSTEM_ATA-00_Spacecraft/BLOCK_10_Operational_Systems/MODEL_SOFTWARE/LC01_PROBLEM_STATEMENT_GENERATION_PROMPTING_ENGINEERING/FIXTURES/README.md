# FIXTURES — Minimal Test Fixtures (Small, Deterministic)

**Parent Context:** LC01_PROBLEM_STATEMENT_GENERATION_PROMPTING_ENGINEERING  
**Purpose:** Test data and fixtures for validation and testing  
**Status:** Active (Portal Baseline)

---

## 1. Purpose

This directory contains **minimal test fixtures** for:
- Unit testing of engines and agents
- Schema validation testing
- CI/CD pipeline testing
- Regression test baselines
- Example data for documentation

---

## 2. What Belongs Here

### Test Data
- Small, deterministic test inputs
- Valid example instances
- Invalid example instances (for negative testing)
- Edge case data
- Boundary condition data

### Golden Outputs
- Expected/baseline outputs for regression testing
- Reference outputs for comparison
- Validated examples

### Configuration Fixtures
- Test configurations for engines
- Test configurations for agents
- Test configurations for validators

### Schema Examples
- Valid schema instances
- Invalid schema instances
- Edge case instances

---

## 3. Fixture Characteristics

All fixtures must be:
- **Small:** Minimal size, focused on specific test case
- **Deterministic:** Produce consistent results
- **Self-contained:** Include all necessary context
- **Documented:** Clear purpose and usage
- **Versioned:** Track with parent artifacts

---

## 4. Fixture Types

### Valid Fixtures
Used to test correct behavior:
- Well-formed prompt definitions
- Valid problem statements
- Correct evaluation results
- Proper configurations

### Invalid Fixtures
Used to test error handling:
- Malformed data
- Missing required fields
- Invalid data types
- Constraint violations

### Edge Case Fixtures
Used to test boundary conditions:
- Maximum/minimum values
- Empty inputs
- Complex structures
- Unusual but valid cases

---

## 5. Organization

Organize fixtures by:
- **By Component:** prompts/, schemas/, engines/, agents/
- **By Test Type:** valid/, invalid/, edge_cases/
- **By Purpose:** unit/, integration/, regression/

---

## 6. Naming Conventions

Follow v6.0 nomenclature:
- `MODEL=SW`
- `PHASE=LC01`
- `CATEGORY=INTERNAL_PRODUCTION` for test fixtures
- `TYPE` as appropriate (JSON, YAML, etc.)

**Example:**
```
00_AMPEL360_SPACET_Q10_BASELINE_PLUS_SW_10_LC01_K01_STK_DAB__valid-prompt-fixture_INTERNAL_PRODUCTION_SPEC_I01-R01_ACTIVE.yaml
00_AMPEL360_SPACET_Q10_BASELINE_PLUS_SW_10_LC01_K01_STK_DAB__invalid-schema-fixture_INTERNAL_PRODUCTION_SPEC_I01-R01_ACTIVE.json
```

---

## 7. Fixture Maintenance

### Keep Fixtures Minimal
- Focus on single test concern
- Remove unnecessary data
- Avoid duplication
- Use parameterization where possible

### Keep Fixtures Current
- Update with schema changes
- Refresh for new test cases
- Remove obsolete fixtures
- Document fixture purpose

### Version Control
- Track fixtures with code
- Document fixture changes
- Link to tests that use them
- Maintain backwards compatibility

---

## 8. Usage in Testing

### Unit Tests
```python
# Load fixture
fixture = load_fixture("valid-prompt-fixture.yaml")

# Execute test
result = prompt_compiler.compile(fixture)

# Validate result
assert result.is_valid()
```

### Integration Tests
```python
# Load multiple fixtures
inputs = load_fixtures("integration/inputs/")
expected = load_fixtures("integration/expected/")

# Execute workflow
results = workflow.execute(inputs)

# Compare with expected
assert results == expected
```

### Regression Tests
```python
# Load baseline fixture
baseline = load_fixture("regression/baseline.json")

# Execute current version
current = execute_current_version(test_input)

# Compare with baseline
assert current.matches(baseline, tolerance=0.01)
```

---

## 9. Integration Points

**Used By:**
- Unit tests in ENGINES/
- Unit tests in AGENTS/
- Schema validation in SCHEMAS/
- Evaluation tests in EVAL/
- CI validators in CI/

**Maintained By:**
- Test authors
- Schema maintainers
- CI/CD automation

---

## 10. Documentation

Each fixture should document:
- Purpose (what it tests)
- Usage (how to use it)
- Expected behavior
- Related tests
- Version/compatibility

Use inline comments or companion README files.

---

## 11. Best Practices

### DO:
- Keep fixtures small and focused
- Use meaningful names
- Document purpose clearly
- Version fixtures with code
- Test both valid and invalid cases
- Use fixtures for documentation examples

### DON'T:
- Store large datasets here (use data/ directory)
- Include sensitive data
- Duplicate fixtures unnecessarily
- Use non-deterministic data
- Hard-code environment-specific values
- Create fixtures without tests

---

## 12. Example Fixtures

### Valid Prompt Fixture
```yaml
# Purpose: Test basic prompt compilation
prompt_id: "PROMPT-001"
version: "1.0.0"
owner_aor: "STK_DAB"
purpose: "Test prompt for unit testing"
template: "Generate a {{artifact_type}} for {{context}}"
parameters:
  artifact_type: "requirement"
  context: "navigation system"
```

### Invalid Schema Fixture
```json
{
  "_comment": "Missing required 'prompt_id' field",
  "version": "1.0.0",
  "owner_aor": "STK_DAB",
  "template": "Invalid prompt without ID"
}
```

### Edge Case Fixture
```yaml
# Purpose: Test handling of maximum-length prompts
prompt_id: "PROMPT-999"
version: "99.99.99"
owner_aor: "STK_DAB"
purpose: "Very long purpose statement that exceeds typical length..."
template: "Very long template that tests length limits..."
```

---

## 13. Quality Criteria

Fixtures should:
- Be reviewed with code
- Pass schema validation (for valid fixtures)
- Fail validation appropriately (for invalid fixtures)
- Remain stable across versions
- Be reusable across tests
- Support multiple test scenarios

---
