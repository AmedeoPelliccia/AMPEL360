# EXPORT — exporters to CAE/simulation configs and downstream tools

**Directory:** `LC03_DESIGN_MODELS/EXPORT/`

## Purpose
This directory contains **model export tools** that transform design models into inputs for Computer-Aided Engineering (CAE) tools, simulation environments, and other downstream analysis and development tools.

## Contents

### A) CAE/Simulation Config Exporters
- Finite Element Analysis (FEA) input generators
- Computational Fluid Dynamics (CFD) config exporters
- Multi-body dynamics simulation exporters
- Thermal analysis input builders
- Structural analysis config generators

### B) Downstream Tool Integrations
- LC04 analysis model input generators
- LC05/LC06 test harness config exporters
- Code generation tool inputs
- Hardware design tool exports
- Manufacturing tool adapters

### C) Parameter Set Generators
- Simulation parameter extractors
- Configuration value compilers
- Initial condition generators
- Boundary condition exporters
- Material property exporters

### D) Format-Specific Exporters
- STEP/IGES geometry exporters
- Modelica model exporters
- MATLAB/Simulink exporters
- Python simulation script generators
- Custom tool format adapters

## Naming Convention
All artifacts in this directory follow the **v6.0 nomenclature standard** with:
- `MODEL=SW`
- `PHASE=LC03`
- `KNOT` binding (typically K03 for design work)
- Full compliance with the controlled vocabulary defined by the program standard

## Usage Rules

**Place artifacts here when they:**
- Export models to CAE or simulation tools
- Generate inputs for downstream analysis
- Create configuration files for external tools
- Transform models for specific tool consumption

**Do not place artifacts here when they:**
- Generate or modify design models (use MBSE/)
- Convert between model formats (use TRANSFORMS/)
- Validate model structure (use VALIDATORS/)
- Create model baselines (use BASELINES/)

## Dependencies
- CAE tool specifications and formats
- Simulation environment requirements
- LC04 analysis model interfaces
- Tool-specific format specifications

## Ownership
**AoR (owners): STK_SE, STK_DAB, STK_CAE**

## References
- Main README: `MODEL_SOFTWARE/LC03_DESIGN_MODELS/README.md`
- CAE Tool Integration Guidelines
- Simulation Framework Standards
- LC04 Interface Specifications
