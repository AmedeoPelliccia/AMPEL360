# FIXTURES/ — Minimal Deterministic Fixtures for Unit Tests

**Location:** `LC00_GENERAL/FIXTURES/`  
**Owner (AoR):** STK_DAB (Digital Applications & Blockchains)  
**Status:** ACTIVE

---

## Purpose

This directory contains **minimal deterministic test fixtures** that support unit testing of LC00_GENERAL utilities and cross-phase validation.

## Scope

### What belongs here:
- **Sample artifacts** for testing (minimal, representative)
- **Test schemas** and controlled vocabularies
- **Mock data** for validators and generators
- **Reference outputs** for comparison testing
- **Edge case fixtures** for boundary testing
- **Integration test scenarios** (minimal, focused)

### What does NOT belong here:
- Full-scale test suites (place in phase-specific directories)
- Production artifacts (place in appropriate directories)
- Large datasets (use external test data repositories)
- Generated outputs (create in temporary directories)

---

## Guidelines

1. **Minimalism**: Keep fixtures small and focused
2. **Determinism**: Fixtures must produce reproducible results
3. **Representativeness**: Cover typical and edge cases
4. **Independence**: Each fixture should be self-contained
5. **Documentation**: Document purpose and expected behavior

---

## Expected Fixtures

Key fixtures that should be maintained here:

- **Sample Artifacts**: Representative artifacts with valid nomenclature
- **Test Schemas**: Simple schemas for validation testing
- **Vocabulary Samples**: Controlled vocabulary dictionaries
- **ID References**: Sample IDs and links for resolver testing
- **Manifest Examples**: Minimal manifests for export testing
- **Gate Test Cases**: Fixtures for gate validation testing
- **Error Cases**: Invalid artifacts for negative testing

---

## Fixture Organization

Organize fixtures by utility domain:

```
FIXTURES/
├── artifacts/
│   ├── valid_deliverable.md
│   ├── valid_evidence.json
│   ├── invalid_nomenclature.md
│   └── edge_case_artifact.yaml
├── schemas/
│   ├── simple_artifact_schema.json
│   ├── requirement_schema.yaml
│   └── invalid_schema.json
├── vocabularies/
│   ├── aor_sample.yaml
│   ├── knot_sample.yaml
│   └── minimal_vocab.yaml
├── ids/
│   ├── valid_references.txt
│   ├── broken_links.txt
│   └── hash_samples.txt
├── manifests/
│   ├── simple_manifest.yaml
│   ├── release_manifest.json
│   └── invalid_manifest.yaml
├── gates/
│   ├── intent_valid.yaml
│   ├── intent_invalid.yaml
│   └── cipp_valid.json
└── outputs/
    ├── expected_report.md
    ├── expected_manifest.yaml
    └── expected_bundle_structure.txt
```

---

## Usage

Fixtures are used in unit tests:

```python
# Example Python test
import pytest
from LC00_GENERAL.VOCAB.loaders import vocab_loader

def test_aor_allowlist_loading():
    # Load fixture vocabulary
    vocab = vocab_loader.load_vocab('FIXTURES/vocabularies/aor_sample.yaml')
    
    # Validate expected values
    assert 'STK_CM' in vocab['aor_allowlist']
    assert 'STK_DAB' in vocab['aor_allowlist']
    assert len(vocab['aor_allowlist']) == 14

def test_nomenclature_validation():
    # Test with valid fixture
    valid_artifact = 'FIXTURES/artifacts/valid_deliverable.md'
    assert validator.validate_filename(valid_artifact) == True
    
    # Test with invalid fixture
    invalid_artifact = 'FIXTURES/artifacts/invalid_nomenclature.md'
    assert validator.validate_filename(invalid_artifact) == False
```

---

## Fixture Examples

### Valid Artifact Fixture

File: `artifacts/valid_deliverable.md`

```markdown
# Sample Deliverable

Filename: 00_AMPEL360_SPACET_Q10_BASELINE_PLUS_PR_00_LC01_K01_STK_CM__sample-artifact_DELIVERABLE_STD_I01-R01_ACTIVE.md

Content: This is a minimal sample artifact for testing.
```

### Simple Schema Fixture

File: `schemas/simple_artifact_schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "id": {"type": "string"},
    "type": {"type": "string"},
    "status": {"type": "string"}
  },
  "required": ["id", "type", "status"]
}
```

### Vocabulary Fixture

File: `vocabularies/aor_sample.yaml`

```yaml
aor_allowlist:
  - STK_CM
  - STK_PMO
  - STK_SE
  - STK_DAB
  - STK_PHM
  - STK_SAF
  - STK_CERT
  - STK_TEST
  - STK_OPS
  - STK_MRO
  - STK_AI
  - STK_CY
  - STK_SPACEPORT
  - STK_CEGT
```

---

## Maintenance

- Keep fixtures minimal and focused
- Update fixtures when vocabularies or schemas change
- Add fixtures for new edge cases as discovered
- Document expected behavior for each fixture
- Remove obsolete fixtures when no longer needed
- Ensure fixtures are deterministic and reproducible

---

**References:**
- See parent README: `../README.md`
- Unit Testing Best Practices
- Test-Driven Development (TDD)
- Nomenclature Standard: Main README Section 10
