# SCHEMAS — JSON/YAML Schemas for Prompt Records and Problem Statements

**Parent Context:** LC01_PROBLEM_STATEMENT_GENERATION_PROMPTING_ENGINEERING  
**Purpose:** Schema definitions for structured data validation  
**Status:** Active (Portal Baseline)

---

## 1. Purpose

This directory contains **schema definitions** for:
- Prompt records and metadata
- Problem statement structures
- Evaluation results
- Agent configurations
- Engine inputs/outputs
- Traceability records

---

## 2. What Belongs Here

### Prompt Schemas
- Prompt definition schema
- Prompt metadata schema
- Prompt template schema
- Prompt catalog schema

### Problem Statement Schemas
- Problem statement structure
- Context definition schema
- Constraint specification schema
- Stakeholder input schema

### Evaluation Schemas
- Evaluation result schema
- Quality metrics schema
- Benchmark data schema
- Test report schema

### Configuration Schemas
- Agent configuration schema
- Engine configuration schema
- Router configuration schema
- Policy gate schema

### Traceability Schemas
- Traceability link schema
- Evidence binding schema
- Audit record schema

---

## 3. Schema Types

### JSON Schema
- Used for structured data validation
- Supports complex validation rules
- Machine-readable and enforceable
- Standard format for tooling

### YAML Schema (JSON Schema in YAML)
- Human-readable schema definitions
- Compatible with YAML data
- Convertible to JSON Schema
- Preferred for configuration

### Custom Schemas
- Domain-specific validation rules
- Composite schemas
- Extension schemas

---

## 4. Schema Requirements

All schemas must:
- Be valid JSON Schema (Draft 2020-12 or later)
- Include clear descriptions for all fields
- Define required vs. optional fields
- Specify data types and formats
- Include examples
- Document validation rules
- Be version controlled

---

## 5. Naming Conventions

Follow v6.0 nomenclature:
- `MODEL=SW`
- `PHASE=LC01`
- `CATEGORY=REGISTRY`
- `TYPE=SCHEMA`

**Example:**
```
00_AMPEL360_SPACET_Q10_BASELINE_PLUS_SW_10_LC01_K01_STK_DAB__prompt-definition-schema_REGISTRY_SCHEMA_I01-R01_ACTIVE.json
00_AMPEL360_SPACET_Q10_BASELINE_PLUS_SW_10_LC01_K01_STK_DAB__problem-statement-schema_REGISTRY_SCHEMA_I01-R01_ACTIVE.yaml
```

---

## 6. Core Schemas

### Prompt Definition Schema
Defines structure for prompt records:
```yaml
prompt_id: string (required, unique)
version: string (required, semantic version)
owner_aor: string (required, from STK_* allowlist)
purpose: string (required)
template: string (required)
parameters: object (optional)
constraints: object (optional)
allowed_tools: array (optional)
traceability: object (required)
metadata: object (optional)
```

### Problem Statement Schema
Defines structure for problem statements:
```yaml
statement_id: string (required, unique)
title: string (required)
description: string (required)
context: object (required)
  - program: string
  - system: string
  - block: string
  - phase: string
  - knot: string
  - aor: string
constraints: array (required)
stakeholders: array (required)
success_criteria: array (required)
traceability: object (required)
```

### Evaluation Result Schema
Defines structure for evaluation outputs:
```yaml
eval_id: string (required, unique)
timestamp: string (required, ISO 8601)
prompt_id: string (required)
prompt_version: string (required)
test_suite: string (required)
metrics: object (required)
  - quality_score: number
  - performance: object
  - reliability: object
pass_fail: boolean (required)
findings: array (optional)
recommendations: array (optional)
```

---

## 7. Validation Integration

Schemas are used by:
- **ENGINES/:** Validate inputs/outputs during execution
- **EVAL/:** Validate test data and results
- **AGENTS/:** Validate agent configurations
- **CI/:** Enforce schema compliance in PR gates

---

## 8. Schema Versioning

Schema changes must:
- Follow semantic versioning
- Maintain backwards compatibility where possible
- Document breaking changes
- Provide migration guidance
- Update dependent tools/engines

---

## 9. Testing

Each schema must have:
- Valid example instances
- Invalid example instances (for negative testing)
- Validation test suite
- Documentation of edge cases

Store test instances in FIXTURES/.

---

## 10. Documentation

Each schema must include:
- Purpose and scope
- Field descriptions
- Validation rules
- Usage examples
- Version history
- Related schemas
- Tool/engine dependencies

---

## 11. Maintenance

Regularly:
- Review schemas for completeness
- Update based on usage feedback
- Ensure consistency across schemas
- Validate against actual data
- Update documentation
- Test with validation tools

---
