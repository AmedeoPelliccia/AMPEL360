# EXPORT/ — Common Packaging, Manifest Emitters, and Bundle Builders

**Location:** `LC00_GENERAL/EXPORT/`  
**Owner (AoR):** STK_DAB (Digital Applications & Blockchains) / STK_CM  
**Status:** ACTIVE

---

## Purpose

This directory contains **export and packaging utilities** that create release packs, manifests, bundles, and deliverable packages for certification, operations, and external distribution.

## Scope

### What belongs here:
- **Manifest generators** (release manifests, export manifests)
- **Bundle builders** (artifact packaging, compression)
- **Export formatters** (SysML, ReqIF, CSV, JSON converters)
- **Signing utilities** (digital signatures for release packs)
- **SBOM generators** (Software/Hardware/Model Bill of Materials)
- **Release packagers** (certification packs, delivery bundles)

### What does NOT belong here:
- Final release artifacts (place in designated release directories)
- Schemas (place in SCHEMAS/)
- General libraries (place in LIB/)
- Test fixtures (place in FIXTURES/)

---

## Guidelines

1. **Determinism**: Exports must be reproducible
2. **Integrity**: All exports must include hashes and provenance
3. **Signing**: Release packs must be digitally signed
4. **Manifest**: Every export must have a manifest
5. **Traceability**: Exports must link to source artifacts

---

## Expected Utilities

Key utilities that should be developed here:

- **Manifest Generator**: Create release and export manifests
- **Bundle Builder**: Package artifacts into bundles (zip, tar.gz)
- **SBOM Generator**: Generate Software/Hardware/Model BOMs
- **Signing Utility**: Sign release packs with digital signatures
- **Format Converter**: Convert to external formats (SysML, ReqIF, CSV)
- **Release Packager**: Build certification and delivery packs
- **Hash Generator**: Generate SHA256 hashes for all exports

---

## Export Types

Common export formats and packages:

### Release Manifests
- **ATA 98**: Signed Release Packs / Manifests / Exports
- **Content**: Artifact list, hashes, signatures, provenance
- **Format**: JSON, YAML, or structured markdown

### SBOM Exports
- **ATA 95**: SBOM / SWHW BOM / Model BOM Exports
- **Content**: Dependencies, versions, licenses, vulnerabilities
- **Format**: SPDX, CycloneDX, or custom JSON

### Certification Packs
- **Content**: Compliance evidence, test results, approval records
- **Format**: PDF, structured archive with manifest

### Format Conversions
- **SysML**: Architecture and requirements models
- **ReqIF**: Requirements interchange format
- **CSV/Excel**: Tabular data exports
- **JSON/YAML**: Structured data exports

---

## Utility Organization

```
EXPORT/
├── manifests/
│   ├── manifest_generator.py
│   ├── release_manifest.py
│   └── export_manifest.py
├── bundlers/
│   ├── bundle_builder.py
│   ├── archive_creator.py
│   └── compression_utils.py
├── sbom/
│   ├── sbom_generator.py
│   ├── dependency_scanner.py
│   └── license_collector.py
├── signing/
│   ├── signer.py
│   ├── verifier.py
│   └── key_manager.py
├── converters/
│   ├── sysml_exporter.py
│   ├── reqif_exporter.py
│   ├── csv_exporter.py
│   └── json_exporter.py
└── packagers/
    ├── cert_pack_builder.py
    ├── delivery_pack_builder.py
    └── release_packager.py
```

---

## Usage

Export utilities create deliverable packages:

```python
# Example Python usage
from LC00_GENERAL.EXPORT.manifests import manifest_generator
from LC00_GENERAL.EXPORT.bundlers import bundle_builder
from LC00_GENERAL.EXPORT.signing import signer

# Generate manifest
manifest = manifest_generator.generate(
    artifacts=['artifact1.md', 'artifact2.json'],
    metadata={'version': 'I01-R01', 'status': 'RELEASED'}
)

# Build bundle
bundle = bundle_builder.create(
    manifest=manifest,
    output='release_pack.tar.gz',
    compression='gzip'
)

# Sign bundle
signature = signer.sign(
    bundle_path='release_pack.tar.gz',
    key_path='signing_key.pem'
)
```

---

## Manifest Structure

Example release manifest:

```yaml
manifest:
  id: MANIFEST-001-R01
  version: I01-R01
  status: RELEASED
  timestamp: 2024-12-25T21:00:00Z
  artifacts:
    - path: artifact1.md
      hash: sha256:abc123...
      type: DELIVERABLE
      status: RELEASED
    - path: artifact2.json
      hash: sha256:def456...
      type: EVIDENCE
      status: ACTIVE
  provenance:
    generator: export_manifest_v1.0
    creator: STK_CM
    signature: digital_signature_here
```

---

## Maintenance

- Ensure exports are deterministic and reproducible
- Update manifest schemas when artifact types change
- Test signing utilities with valid and invalid keys
- Coordinate with STK_CM for release governance
- Document export formats and conventions
- Register export types in ATA 98 (Signed Release Packs)

---

**References:**
- See parent README: `../README.md`
- ATA 95: SBOM / SWHW BOM / Model BOM Exports
- ATA 98: Signed Release Packs / Manifests / Exports
- ATA 99: Master Registers (Golden Records) & Reference Datasets
- Nomenclature Standard: Main README Section 10
