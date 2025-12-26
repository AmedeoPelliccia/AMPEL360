# LC02_SYSTEM_REQUIREMENTS
**Lifecycle Phase:** LC02 — System Requirements

## Purpose
This directory contains **LC02 software artifacts and tools** used to:
- capture, structure, and manage system requirements,
- allocate requirements across system architecture,
- establish and maintain traceability relationships,
- validate requirement quality and consistency,
- generate requirement evidence for certification and compliance.

This is the **formal requirements layer** for the `MODEL_SOFTWARE` portal node (ATA-00 / Block 10): it provides
controlled requirement management tools, validators, and automation that support the entire requirements lifecycle
from capture through certification.

## Directory Structure

The LC02_SYSTEM_REQUIREMENTS directory is organized into the following subdirectories:

### SCHEMAS/ — Requirement Record Schemas and Controlled Vocabulary Dictionaries
- Requirement record schema definitions (JSON Schema, YAML schemas)
- Controlled vocabulary dictionaries and taxonomies
- Schema validation tools and evolution utilities
- Field definitions and data type specifications

**See:** `SCHEMAS/README.md`

### ENGINES/ — Parsers, Normalizers, ID Services, and Baseline Managers
- Requirement document parsers and import utilities
- Requirement text normalization and standardization tools
- ID generation, assignment, and lifecycle management services
- Baseline creation, versioning, and configuration control tools

**See:** `ENGINES/README.md`

### VALIDATORS/ — Quality Checks, Constraint Checks, and Contradiction Detectors
- Requirement quality attribute validators
- Constraint and consistency checking tools
- Contradiction and conflict detection engines
- Completeness and coverage analyzers

**See:** `VALIDATORS/README.md`

### TRACE/ — Trace Graph Builders, Link Resolvers, and Impact Analyzers
- Traceability graph construction and maintenance tools
- Trace link validation and resolution utilities
- Change impact analysis engines
- Traceability report and matrix generators

**See:** `TRACE/README.md`

### INTERFACES/ — ICD Candidate Extraction and Cross-ATA Coupling Tools
- Interface Control Document (ICD) candidate extraction tools
- Cross-ATA dependency and coupling analyzers
- Interface validation and completeness checkers
- Interface catalog and documentation generators

**See:** `INTERFACES/README.md`

### EXPORT/ — Converters to SysML/ReqIF/CSV/JSON and Portal Registry Writers
- Format converters (SysML, ReqIF, CSV, JSON, XML)
- Portal catalog and registry population tools
- Documentation generators and publishers
- Integration adapters for external systems

**See:** `EXPORT/README.md`

### CI/ — LC02 Gate Scripts for GitHub Actions and Pipelines
- PR-blocking validation gate scripts for LC02
- GitHub Actions workflow integrations
- Gate result formatters and evidence generators
- Automated validation orchestration tools

**See:** `CI/README.md`

### FIXTURES/ — Small Deterministic Test Fixtures
- Sample requirements and test data
- Schema validation test cases
- Traceability test scenarios
- Integration test fixtures

**See:** `FIXTURES/README.md`

## Contents (What belongs in LC02)
Artifacts in this directory typically include:

### A) Requirement capture & management
- Requirement parsers, normalizers, and import/export utilities
- Requirement ID generation and lifecycle management services
- Requirement baseline management and version control tools
- Schema definitions and validation engines

### B) Requirement validation & quality
- Quality attribute validators (clarity, completeness, testability)
- Constraint checkers and consistency analyzers
- Contradiction detectors and conflict resolution tools
- Completeness and coverage assessment utilities

### C) Traceability & impact analysis
- Traceability graph construction and maintenance tools
- Trace link validation and broken link detection
- Change impact analysis and dependency tracking
- Traceability matrix and report generators

### D) Interface & ICD management
- ICD candidate extraction from requirements
- Cross-ATA coupling and dependency analysis
- Interface validation and documentation tools

### E) Integration & export
- SysML, ReqIF, CSV, JSON export converters
- Portal registry population utilities
- CI/CD gate scripts and validators
- Test fixtures and validation datasets

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC02`
- `KNOT` binding (typically K02 for requirements work)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules
Place software here when it:
- captures, processes, or validates **system requirements**,
- builds or maintains requirement **traceability relationships**,
- generates requirement **baselines** or **configuration snapshots**,
- performs requirement **quality checks** or **constraint validation**,
- extracts **interface requirements** or analyzes **cross-ATA dependencies**,
- exports requirements to **standard formats** (SysML, ReqIF, etc.),
- implements **LC02-specific CI gates** or validation workflows.

Do **not** place software here when it:
- is for problem framing or ideation (use LC01),
- is architecture/design modeling (use LC03),
- is engineering analysis or calculation (use LC04),
- is verification/test execution (use LC05),
- is CM baseline/release governance at the program level (use LC10).

## Ownership
**AoR (owners): STK_SE, STK_CM, STK_DAB**

## References
- Main README: `MODEL_SOFTWARE/README.md` for directory structure definition
- Lifecycle phases (LC00–LC14) definition in main AMPEL360 README
- Nomenclature Standard v6.0 and controlled vocabulary section
- ATA 93 Traceability Graph specification
- ATA 99 Master Registers for SSOT schemas and vocabularies
