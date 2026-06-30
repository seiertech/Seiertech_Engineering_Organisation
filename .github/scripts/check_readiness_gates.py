#!/usr/bin/env python3
"""
EMS Readiness Gate Checker — real deterministic checks, not LLM self-assessment.

Checks the 10 readiness gates (RG-001 to RG-010) defined in REG-000001 against
what was ACTUALLY produced on disk for a platform. This does not ask the model
"are you ready?" — it checks for the literal presence and minimum content
quality of each required artefact.

Sets platform status to READY only if all gates pass. Otherwise BLOCKED with
a specific list of failing gates — actionable, not vague.
"""

import argparse
import json
import os
import sys

REQUIRED_ARTEFACTS = {
    "RG-001": ("Platform Record / metadata", ["PLATFORM_RECORD.md", "INTAKE_RUN_LOG.md"]),
    "RG-002": ("Repo scan completed", ["SCAN_RESULT.json"]),
    "RG-003": ("Data model extracted or created", ["DATA_MODEL.md", "ARCHITECTURE_DOCUMENT.md"]),
    "RG-004": ("Tech stack identified", ["SCAN_RESULT.json"]),
    "RG-005": ("Use case register populated", ["USE_CASE_REGISTER.md"]),
    "RG-006": ("Knowledge graph created or addressed", ["KNOWLEDGE_GRAPH.md"]),
    "RG-007": ("Persona spine files present", ["spine"]),  # directory check
    "RG-008": ("Founder questions resolved", None),  # special-cased below
    "RG-009": ("Master Technical Specification reviewed", ["MASTER_TECHNICAL_SPECIFICATION.md"]),
    "RG-010": ("Platform registered in Readiness Register", None),  # checked by caller via register update
}

MIN_CONTENT_CHARS = 200  # an artefact under this size is treated as effectively empty


def check_artefact_exists_and_nonempty(platform_dir, filename):
    path = os.path.join(platform_dir, filename)
    if not os.path.exists(path):
        return False, f"{filename} does not exist"
    if os.path.isdir(path):
        contents = os.listdir(path)
        if not contents:
            return False, f"{filename}/ exists but is empty"
        return True, f"{filename}/ contains {len(contents)} files"
    size = os.path.getsize(path)
    if size < MIN_CONTENT_CHARS:
        return False, f"{filename} exists but is only {size} bytes (likely empty/placeholder)"
    return True, f"{filename} present, {size} bytes"


def check_standards_engineer_log(platform_dir):
    """RG checks should also confirm Standards Engineer actually ran and passed."""
    log_path = os.path.join(platform_dir, "INTAKE_RUN_LOG.md")
    if not os.path.exists(log_path):
        return False, []
    with open(log_path, "r", encoding="utf-8") as f:
        content = f.read()
    fail_count = content.count('"pass": false')
    pass_count = content.count('"pass": true')
    return fail_count == 0 and pass_count > 0, {"pass_count": pass_count, "fail_count": fail_count}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform-dir", required=True)
    parser.add_argument("--platform-name", required=True)
    parser.add_argument("--reduced-scope", action="store_true",
                         help="Acknowledge this is a v1 reduced chain — relevant gates auto-marked N/A with explanation rather than silently passing")
    parser.add_argument("--output-file", required=True)
    args = parser.parse_args()

    results = {}
    all_pass = True

    for gate_id, (description, required_files) in REQUIRED_ARTEFACTS.items():
        if gate_id == "RG-008":
            # Founder questions — v1 chain does not yet generate a Questions to Founder
            # mechanism, so this is honestly marked as a gap, not silently passed.
            results[gate_id] = {
                "description": description,
                "result": "N/A — NOT YET IMPLEMENTED",
                "detail": "v1 chain does not generate or track founder questions. Cannot certify this gate as genuinely satisfied.",
            }
            all_pass = False
            continue

        if gate_id == "RG-010":
            results[gate_id] = {
                "description": description,
                "result": "PENDING",
                "detail": "Set by caller after this script runs, based on overall verdict.",
            }
            continue

        if gate_id == "RG-007":
            ok, detail = check_artefact_exists_and_nonempty(args.platform_dir, "spine")
            results[gate_id] = {"description": description, "result": "PASS" if ok else "FAIL", "detail": detail}
            if not ok:
                all_pass = False
            continue

        gate_pass = False
        details = []
        for fname in required_files:
            ok, detail = check_artefact_exists_and_nonempty(args.platform_dir, fname)
            details.append(detail)
            if ok:
                gate_pass = True  # any one of the listed acceptable artefacts satisfies the gate

        results[gate_id] = {
            "description": description,
            "result": "PASS" if gate_pass else "FAIL",
            "detail": "; ".join(details),
        }
        if not gate_pass:
            all_pass = False

    se_pass, se_detail = check_standards_engineer_log(args.platform_dir)
    results["STANDARDS_ENGINEER_GATE"] = {
        "description": "Standards Engineer ran and all assessed artefacts PASSED",
        "result": "PASS" if se_pass else "FAIL",
        "detail": se_detail,
    }
    if not se_pass:
        all_pass = False

    overall_status = "READY" if all_pass else "BLOCKED"

    if args.reduced_scope and not all_pass:
        # Be explicit this is expected given known v1 scope, not a surprise failure
        overall_status = "BLOCKED — v1 REDUCED SCOPE (see IMPLEMENTATION_STATUS.md)"

    failing_gates = [gid for gid, r in results.items() if r["result"] not in ("PASS", "PENDING")]

    output = {
        "platform_name": args.platform_name,
        "overall_status": overall_status,
        "all_gates_pass": all_pass,
        "failing_gates": failing_gates,
        "gate_results": results,
    }

    with open(args.output_file, "w") as f:
        json.dump(output, f, indent=2)

    print(json.dumps(output, indent=2))

    if not all_pass:
        print(f"\nPlatform {args.platform_name} is NOT READY. Failing/incomplete gates: {failing_gates}", file=sys.stderr)


if __name__ == "__main__":
    main()
