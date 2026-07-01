#!/usr/bin/env python3
"""
EMS loop contract sweep validator.

Purpose:
- Perform the founder-requested left-to-right and right-to-left sweep.
- Check that loop engineering is not only documented, but present across
  execution-relevant artefact classes.
- This is deliberately lightweight and deterministic: it checks evidence of
  wiring, not semantic quality of every artefact.

It is safe to run locally or in GitHub Actions:

    python3 .github/scripts/validate_loop_contract_sweep.py
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterable, List

ROOT = Path(__file__).resolve().parents[2]

CATEGORIES = [
    ("constitution", ["authorities/AUTH-001_ENGINEERING_CONSTITUTION.md"]),
    ("authorities", ["authorities"]),
    ("standards", ["standards"]),
    ("registers", ["registers"]),
    ("operations", ["operations"]),
    ("templates", ["templates"]),
    ("personas", ["personas", "agents"]),
    ("workflows", [".github/workflows"]),
    ("python", [".github/scripts"]),
    ("memory", ["memory"]),
]

REQUIRED_FILES = {
    "standard": "standards/STD-000005_EMS_LOOP_ENGINEERING_STANDARD.md",
    "operation": "operations/OPR-000013_LOOP_ENGINEERING_OPERATION.md",
    "template": "templates/TPL-000013_LOOP_CONTRACT_TEMPLATE.md",
    "pattern_library": "operations/EMS_LOOP_PATTERN_LIBRARY.md",
    "validator": ".github/scripts/validate_loop_contract_sweep.py",
}

CONTRACT_TERMS = [
    "Trigger",
    "Goal",
    "Work Unit",
    "Actor",
    "Verifier",
    "Governor",
    "Stop Condition",
    "Output Artefact",
    "Knowledge Update",
]

STOP_TERMS = [
    "COMPLETE",
    "READY_WITH_KNOWN_CEILING",
    "BLOCKED_BY_GATE",
    "HALTED_BY_AUTHORITY",
    "VERIFIER_FAILED",
    "RELEASE_HOLD",
    "RELEASE_REJECTED",
    "DELIVERED_TO_TARGET",
    "DELIVERY_FAILED",
    "DEPENDENCY_MISSING",
    "NO_EVIDENCE",
    "NO_PROGRESS",
    "HUMAN_REQUIRED",
    "AMBIGUOUS_INPUT",
    "TIME_OR_BUDGET_EXHAUSTED",
]


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return ""


def iter_files(paths: Iterable[str]) -> Iterable[Path]:
    for rel in paths:
        base = ROOT / rel
        if base.is_file():
            yield base
        elif base.is_dir():
            for path in base.rglob("*"):
                if path.is_file() and path.suffix.lower() in {".md", ".yml", ".yaml", ".py", ".json"}:
                    yield path


def category_evidence(paths: List[str]) -> Dict[str, object]:
    files = list(iter_files(paths))
    haystack_by_file = {str(p.relative_to(ROOT)): read(p) for p in files}
    combined = "\n".join(haystack_by_file.values())
    matched_terms = [term for term in CONTRACT_TERMS if term in combined]
    matched_stops = [term for term in STOP_TERMS if term in combined]
    matched_files = [name for name, text in haystack_by_file.items() if any(term in text for term in CONTRACT_TERMS + STOP_TERMS)]
    return {
        "files_scanned": len(files),
        "matched_files": matched_files[:25],
        "contract_terms_found": matched_terms,
        "stop_terms_found": matched_stops,
        "status": "WIRED" if matched_files else "NO_DIRECT_EVIDENCE",
    }


def required_file_status() -> Dict[str, object]:
    result = {}
    for name, rel in REQUIRED_FILES.items():
        path = ROOT / rel
        text = read(path)
        result[name] = {
            "path": rel,
            "exists": path.exists(),
            "contract_terms_found": [term for term in CONTRACT_TERMS if term in text],
            "stop_terms_found": [term for term in STOP_TERMS if term in text],
        }
    return result


def main() -> int:
    left_to_right = []
    for category, paths in CATEGORIES:
        left_to_right.append({"category": category, **category_evidence(paths)})

    right_to_left = []
    for category, paths in reversed(CATEGORIES):
        right_to_left.append({"category": category, **category_evidence(paths)})

    report = {
        "validator": "validate_loop_contract_sweep.py",
        "standard": "STD-000005 EMS Loop Engineering Standard",
        "operation": "OPR-000013 Loop Engineering Operation",
        "required_files": required_file_status(),
        "left_to_right": left_to_right,
        "right_to_left": right_to_left,
        "honest_limitations": [
            "This validator confirms textual and structural wiring evidence; it does not prove semantic quality of every loop.",
            "Existing older artefacts are allowed to be partially wired; the standard applies prospectively and to material amendments.",
            "A category with NO_DIRECT_EVIDENCE is not automatically a failure where the directory is absent or intentionally not yet populated.",
        ],
    }

    out_dir = ROOT / "reports"
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / "LOOP_CONTRACT_SWEEP_REPORT.json"
    out_file.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(json.dumps(report, indent=2))

    required_missing = [name for name, status in report["required_files"].items() if not status["exists"]]
    if required_missing:
        print(f"Missing required loop engineering files: {required_missing}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
