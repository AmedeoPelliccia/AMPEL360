"""
LC04 Calculation Sheet Template

Filename (example):
SPACET_Q10_PLUS_GEN_ATA00_B10_SW_LC04_SIZING_MEM001_v1.0.py

This script should:
- load inputs (JSON/YAML/CSV)
- validate ranges/units (as applicable)
- compute outputs deterministically
- emit:
  - results.json / results.csv
  - run_manifest.json (tool versions, hashes, inputs/outputs)
"""

import json
import hashlib
import platform
from datetime import datetime, timezone
from pathlib import Path


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    root = Path(".")
    inputs_path = root / "inputs.json"  # customize
    outputs_path = root / "results.json"
    manifest_path = root / "run_manifest.json"

    if not inputs_path.exists():
        raise FileNotFoundError(f"Missing inputs: {inputs_path}")

    try:
        input_data = json.loads(inputs_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in inputs file: {e}") from e

    # TODO: validate input_data (ranges/units) deterministically
    results = {
        "computed_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "outputs": {}
    }

    try:
        outputs_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    except OSError as e:
        raise OSError(f"Failed to write results file: {e}") from e

    manifest = {
        "toolchain": "python",
        "tool_versions": {
            "python": platform.python_version(),
            "platform": platform.platform()
        },
        "sha256_inputs": { inputs_path.as_posix(): sha256_file(inputs_path) },
        "sha256_outputs": { outputs_path.as_posix(): sha256_file(outputs_path) }
    }

    try:
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    except OSError as e:
        raise OSError(f"Failed to write manifest file: {e}") from e

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
