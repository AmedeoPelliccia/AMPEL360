# LC01 — Problem Statement, Generation & Prompting Engineering (MODEL=SW)

**Portal Context:** CAXS → AoR → STK_CM → PORTAL → PROGRAM_SPACET → FAMILY_Q10 → VARIANT_GEN → VERSION_PLUS  
**System Context:** SYSTEM_ATA-00_Spacecraft → BLOCK_10_Operational_Systems  
**Lifecycle:** LC01_PROBLEM_STATEMENT_GENERATION_PROMPTING_ENGINEERING  
**Primary Owner (AoR):** STK_CM  
**Status:** Active (Portal Baseline)

---

## 1. Purpose

This directory contains **software artifacts** used to:
- define and structure **problem statements** (what is being solved and why),
- implement **generation and prompting workflows** (prompt catalogs, orchestrators, evaluators),
- ensure **traceability** from stakeholder intent → prompts → generated outputs → downstream LC phases,
- provide **portal-grade governance** for reproducible, reviewable, configuration-controlled prompt engineering.

This is the **LC01 software toolbox** powering the PORTAL’s “front door” into controlled generation.

---

## 2. Scope (What belongs here)

Store here any **executable or automatable** software that supports LC01, including:
- Prompt compilation / templating engines (YAML→prompt, prompt macros, parameterization)
- Prompt test harnesses (unit tests, golden outputs, regression suites)
- Evaluation tooling (rubrics, scoring pipelines, drift detection, dataset samplers)
- Portal-aware agent wrappers (AoR-aware assistants, policy routing, tool gating)
- Ingestion adapters (stakeholder input → normalized problem statement)
- CI scripts supporting LC01 gates (linting, prompt schema validation, diff summarizers)

**Note:** Narrative definitions and governance text should live as PR/MD artifacts in the corresponding process/doc areas; this folder is for **MODEL_SOFTWARE** only.

---

## 3. Out of scope (Do NOT place here)

- Final deliverables (manuals, exports, “published” baselines)
- Raw datasets (unless they are small test fixtures tightly coupled to a tool)
- Authority signoffs / certification approvals (K01 governance folders)
- Large generated outputs (these must be exported to the appropriate evidence/export locations)

---

## 4. Minimum expected contents (baseline)

At minimum, this LC01 folder should enable:
1) **Problem statement capture** (structured input → normalized record)  
2) **Prompt catalog** (versioned prompts with metadata)  
3) **Prompt evaluation** (repeatable tests + score outputs)  
4) **Traceability hooks** (IDs linking prompts to tasks, knots, and downstream artifacts)

---

## 5. Recommended sub-structure (tooling lanes)

Use these subfolders if/when needed (keep names stable once adopted):

- `PROMPTS/` — prompt definitions, templates, macro libraries (non-executable allowed if tool-driven)
- `ENGINES/` — prompt compilers, orchestrators, routers, policy gates
- `EVAL/` — evaluation suites, scoring tools, regression tests, benchmark harnesses
- `AGENTS/` — portal-aware assistants (AoR routing, tool access control, guardrails)
- `SCHEMAS/` — JSON/YAML schemas for prompt records and problem statements
- `CI/` — validators, linters, GitHub Actions helpers specific to LC01
- `FIXTURES/` — minimal test fixtures (small, deterministic)

If CGen auto-indexing is enabled, do not manually maintain indexes; rely on generated `00_INDEX.md` where applicable.

---

## 6. Interfaces (LC01 → downstream)

**Upstream inputs**
- Stakeholder intent / portal requests (AoR entry points)
- Constraints: program, system, block, lifecycle, knot, policy rules

**Downstream outputs**
- LC02: normalized requirements candidates (structured)
- LC03: design model prompts (SysML/MBSE generation prompts, ICD scaffolds)
- LC05/LC06: test/evidence prompt suites
- Portal backlog: knot-linked tasks and review packets

---

## 7. MoSCoW feature definition (Portal LC01 launchpad)

### Must have
- **Prompt Catalog Registry** (ID, version, owner, purpose, constraints, allowed tools)
- **Schema Validation** for prompt records and problem statements (fail CI on invalid metadata)
- **Regression Harness** (detect prompt drift, deterministic baselines where feasible)
- **Traceability Binding** (prompt ↔ KNOT task ↔ evidence/export pointers)
- **AoR-aware Access Control** (who can run what, and under which policy gates)

### Should have
- **Prompt Diff Summaries** (semantic + structural diffs for PR review)
- **Evaluation Dashboards** (scores, trends, drift signals)
- **Golden Set Management** (curated benchmark prompts + expected patterns)
- **Safety/Policy Gate Plugins** (red team checks, restricted output filters)

### Could have
- **Interactive Prompt Studio UI** (portal UI for composing/running prompts with guardrails)
- **Multi-agent Orchestration** (role-based agents cooperating per AoR/KNOT)
- **Auto-triage** from failed evals to backlog tasks (KNOT binding)

### Won’t have (in this folder)
- Non-software governance signoffs (stored in K01 / approval registries)
- Large published outputs or operational releases (export elsewhere)

---

## 8. Naming & compliance

All artifacts must follow the repository **v6.0 nomenclature** and controlled vocabulary rules.
At minimum:
- Include `MODEL=SW`, `PHASE=LC01`, and correct bindings for `SYSTEM`, `BLOCK`, `KNOT`, `AoR`.
- Do not introduce new uncontrolled tokens here; extend vocabularies only via the proper registry process.

**Examples (illustrative)**
- `..._SW_..._LC01_...__Prompt_Catalog_Registry_REGISTRY_MD_I01-R01_ACTIVE.md`
- `..._SW_..._LC01_...__Prompt_Schema_SCHEMA_JSON_I01-R01_ACTIVE.json`
- `..._SW_..._LC01_...__Eval_Harness_TOOL_PY_I01-R01_ACTIVE.py`

---

## 9. Review & change control

- Changes to engines, schemas, or evaluation logic require:
  - a PR with diff summary,
  - regression suite execution,
  - updated registry entries if IDs or interfaces change.
- STK_CM is responsible for ensuring LC01 tooling remains **configuration-controlled**, reproducible, and portal-consistent.

---
