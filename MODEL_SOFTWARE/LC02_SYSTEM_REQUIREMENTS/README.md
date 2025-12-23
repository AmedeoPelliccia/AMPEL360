# LC01_PROBLEM_STATEMENT_GENERATION_PROMPTING_ENGINEERING
**Lifecycle Phase:** LC01 — Problem Statement / Generation / Prompting Engineering

## Purpose
This directory contains **LC01 software artifacts and generators** used to:
- frame and structure the problem space,
- establish ideation and exploration baselines,
- define NKU (Named Knowledge Unit) generation pathways,
- capture prompting-engineering baselines,
- produce **initial scope statements** and assumptions that seed downstream lifecycle phases.

This is the **pre-requirements** layer for the `MODEL_SOFTWARE` portal node (ATA-00 / Block 10): it creates
repeatable framing assets and generation pipelines that later become inputs for **LC02 System Requirements**.

## Contents (What belongs in LC01)
Artifacts in this directory typically include:

### A) Problem framing & scope baselines
- Problem statement generators (templates, structured prompts, framing checklists)
- Assumptions / constraints capture utilities (with versioned snapshots)
- Initial scope statement generators (what is in/out of scope for the node)

### B) Ideation & exploration tooling
- Ideation workflows (option exploration, hypothesis boards, concept scoping tools)
- NKU pathway generators (named knowledge units creation, tagging, lifecycle routing)

### C) Prompting engineering baselines
- Prompt libraries and baseline prompts used for generation in this node
- Prompt evaluation harnesses (prompt variants, acceptance heuristics, reproducibility notes)

### D) Seed artifacts (handoff to LC02)
- “Requirements seed” outputs only (candidate requirements, discovery notes, questions backlog)
  that are intended to be formalized in LC02 (capture/allocation/traceability).

> Note: LC01 may generate **candidate requirements** and discovery outputs, but **formal requirement capture,
> allocation, and traceability seeding** are LC02 responsibilities.

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC01`
- `KNOT` binding **as applicable** (commonly K01; may reference K02 handoff artifacts when relevant)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules
Place software here when it:
- supports **problem definition**, framing, or scoping,
- implements NKU generation pathways and early knowledge structuring,
- defines prompting-engineering baselines used across LC01 generation,
- produces initial scope/assumptions baselines that gate downstream work.

Do **not** place software here when it:
- is primarily for formal requirements capture/allocation/traceability (use LC02),
- is architecture/design modeling tooling (use LC03),
- is verification/test harness tooling (use LC05),
- is CM baseline/release governance (use LC00/LC10 as appropriate).

## Ownership
**AoR (owners): STK_DAB, STK_SE, STK_CM**

## References
- Main README: `MODEL_SOFTWARE` directory structure definition
- Lifecycle phases (LC00–LC14) definition
- Nomenclature Standard v6.0 and controlled vocabulary section

