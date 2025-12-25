# PROMPTS — Prompt Definitions, Templates, and Macro Libraries

**Parent Context:** LC01_PROBLEM_STATEMENT_GENERATION_PROMPTING_ENGINEERING  
**Purpose:** Storage and organization of prompt definitions, templates, and macro libraries  
**Status:** Active (Portal Baseline)

---

## 1. Purpose

This directory contains **prompt definitions, templates, and macro libraries** used for:
- Controlled prompt engineering workflows
- Reusable prompt patterns and templates
- Prompt parameterization and composition
- Macro-based prompt generation

---

## 2. What Belongs Here

### Prompt Definitions
- Individual prompt definitions with metadata (ID, version, purpose, constraints)
- Prompt variants for different contexts (AoR-specific, KNOT-specific)
- Versioned prompt records following the v6.0 nomenclature

### Templates
- Reusable prompt templates with variable substitution
- Context-aware templates (program/system/block/phase specific)
- Template libraries for common generation patterns

### Macro Libraries
- Prompt composition macros
- Parameterization functions
- Snippet libraries for common prompt components
- Tool-driven prompt construction helpers

### Non-Executable Artifacts (If Tool-Driven)
- YAML/JSON prompt configurations
- Prompt metadata registries
- Parameterization schemas

---

## 3. Organization

Organize prompts by:
- **By Purpose:** problem-statement/, requirements-generation/, design-generation/
- **By AoR:** STK_CM/, STK_SE/, STK_DAB/, etc.
- **By KNOT:** K01/, K02/, K03/, etc.

---

## 4. Naming Conventions

All prompt artifacts must follow v6.0 nomenclature:
- `MODEL=SW`
- `PHASE=LC01`
- `CATEGORY=REGISTRY` for prompt catalogs
- `TYPE` as appropriate (IDX, CAT, REG for registries; SPEC for specifications)

**Example:**
```
00_AMPEL360_SPACET_Q10_BASELINE_PLUS_SW_10_LC01_K01_STK_DAB__prompt-catalog_REGISTRY_CAT_I01-R01_ACTIVE.yaml
```

---

## 5. Traceability

All prompts must include:
- Unique prompt ID
- Version control
- Owner AoR
- Purpose statement
- Allowed tools/contexts
- Links to KNOT tasks and downstream artifacts

---

## 6. Version Control

- Prompts are configuration-controlled artifacts
- Changes require PR with diff summary
- Registry updates when IDs or interfaces change
- Maintain backwards compatibility where possible

---

## 7. Integration Points

**Upstream:**
- Stakeholder intent and requirements
- AoR constraints and policies
- KNOT task definitions

**Downstream:**
- ENGINES/ for prompt compilation and execution
- EVAL/ for prompt testing and validation
- AGENTS/ for portal-aware prompt routing

---

## 8. Review and Approval

All prompt changes must:
- Pass schema validation (see SCHEMAS/)
- Execute successfully in evaluation harness (see EVAL/)
- Be reviewed by appropriate AoR owner
- Be registered in prompt catalog

---
