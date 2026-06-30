#!/usr/bin/env python3
"""
EMS Team 2 Genesis Chain Orchestrator — v1

This is the first real executable version of OPR-000011 Platform Genesis
Operation, built and tested as part of a brownfield+greenfield simulation
exercise (see PERSONA_SENSE_CHECK_REPORT.md and related session docs for
context). Prior to this, MISSION-000/GENESIS issues were correctly
detected but had NO executor at all — the workflow just posted an honest
"not yet built" comment.

HONEST SCOPE OF THIS v1:

NOW DOES:
- Takes a platform name + one-line brief (no repo to scan — nothing exists yet)
- Runs 3 grouped DESIGN-mode persona passes (not 25 individual calls):
  Pass 1: Use Case Register + Requirements (designed forward from the brief)
  Pass 2: Architecture Document + Data Model (designed forward from use cases)
  Pass 3: Knowledge Graph (derived from passes 1-2)
- MTS synthesis pass citing the above
- Each artefact gated by a real Standards Engineer NIM call (PASS/FAIL)
- A real deterministic readiness gate check at the end (same checker used
  for brownfield intake — proves the two-origin model converges on the
  same READY state)

STILL DOES NOT DO:
- Create an actual GitHub repository for the new platform (OPR-000011
  Phase 4 calls for this; this v1 only writes into the EMS repo's
  platforms/[NAME]/ folder, same limitation the v2 intake chain has for
  the TARGET repo's .ems/ folder)
- Security Posture, Technical Debt Register (empty by design for
  greenfield, but not yet explicitly produced as empty-but-present files)
- Full 25-persona Team 2 depth
- Founder Questions mechanism (same gap as brownfield — RG-008 will
  honestly show N/A)

See IMPLEMENTATION_STATUS.md for the full current-state ledger.
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def call_nim(api_key, model, system_content, user_content, max_tokens=4000):
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    payload = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content},
        ],
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        print(f"NIM HTTP error {e.code}: {e.read().decode('utf-8', errors='replace')}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"NIM call failed: {e}", file=sys.stderr)
        sys.exit(1)


def read_file_safe(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[NOT FOUND: {path}]"


def standards_engineer_gate(api_key, model, artefact_content, artefact_name):
    std_files = [
        "standards/STD-000001_EMS_FOUNDATION_CONFORMANCE_STANDARD.md",
        "standards/STD-000002_ENGINEERING_ARTEFACT_METADATA_STANDARD.md",
        "standards/STD-000004_ENGINEERING_VOCABULARY_STANDARD.md",
    ]
    std_content = "\n\n".join(read_file_safe(f) for f in std_files)

    system = (
        "You are the Standards Engineer persona (PER-000020 / T2-PER-000020) in the SeierTech EMS. "
        "Assess the artefact below against these standards. Respond ONLY with JSON: "
        '{"result": "PASS" or "FAIL", "issues": ["list of specific issues if FAIL, else empty"]}\n\n'
        f"STANDARDS:\n{std_content}"
    )
    user = f"Artefact name: {artefact_name}\n\nArtefact content:\n{artefact_content}"

    raw = call_nim(api_key, model, system, user, max_tokens=800)
    try:
        start = raw.find("{")
        end = raw.rfind("}") + 1
        parsed = json.loads(raw[start:end])
        return parsed.get("result", "FAIL") == "PASS", parsed.get("issues", [])
    except Exception:
        return False, [f"Could not parse Standards Engineer verdict: {raw[:200]}"]


def run_gate_check(platform_dir, platform_name, output_file):
    cmd = [
        sys.executable,
        os.path.join(SCRIPT_DIR, "check_readiness_gates.py"),
        "--platform-dir", platform_dir,
        "--platform-name", platform_name,
        "--reduced-scope",
        "--output-file", output_file,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    print(result.stdout)
    try:
        with open(output_file, "r") as f:
            return json.load(f)
    except Exception:
        return {"overall_status": "UNKNOWN", "error": "gate check produced no readable output"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform-name", required=True)
    parser.add_argument("--brief", required=True)
    parser.add_argument("--issue-number", required=True)
    parser.add_argument("--model", default="nvidia/nemotron-3-super")
    args = parser.parse_args()

    api_key = os.environ.get("NIM_API_KEY")
    if not api_key:
        print("NIM_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    platform_name = args.platform_name.strip().upper().replace("-", "_").replace(" ", "_")
    platform_dir = f"platforms/{platform_name}"
    spine_dir = f"{platform_dir}/spine"
    os.makedirs(spine_dir, exist_ok=True)

    constitution = read_file_safe("authorities/AUTH-001_ENGINEERING_CONSTITUTION.md")
    vocab = read_file_safe("standards/STD-000004_ENGINEERING_VOCABULARY_STANDARD.md")

    log = []

    with open(f"{spine_dir}/GENESIS_BRIEF_SPINE.md", "w") as f:
        f.write(f"# Genesis Brief Spine\n\nPlatform: {platform_name}\nBrief: {args.brief}\n\n"
                 f"This platform originated via MISSION-000 Platform Genesis — no prior codebase exists. "
                 f"All artefacts below are DESIGNED forward from this brief, not extracted from evidence.\n")

    # Pass 1: Use Case Register + Requirements (DESIGN mode)
    pass1_system = (
        f"You are Team 2 personas (Use Case Analyst, Senior Business Analyst) in the SeierTech EMS, "
        f"operating in GENESIS MODE — design forward from intent, never extract from code that doesn't exist. "
        f"GOVERNED BY:\n{constitution}\n\nVOCABULARY:\n{vocab}\n\n"
        "Produce a Use Case Register and Requirements summary in markdown, conformant to STD-000003, "
        "designed entirely from the platform brief below. Mark every item as DESIGNED, not FOUND."
    )
    pass1_user = f"Platform: {platform_name}\nBrief: {args.brief}"
    print("\n=== Genesis Pass 1: Use Case Register + Requirements (DESIGN mode) ===")
    pass1_output = call_nim(api_key, args.model, pass1_system, pass1_user, max_tokens=2500)
    passed1, issues1 = standards_engineer_gate(api_key, args.model, pass1_output, "Use Case Register (Genesis)")
    log.append({"artefact": "Use Case Register", "pass": passed1, "issues": issues1})
    with open(f"{platform_dir}/USE_CASE_REGISTER.md", "w") as f:
        f.write(pass1_output)
    print(f"Standards Engineer verdict: {'PASS' if passed1 else 'FAIL'} — {issues1}")

    # Pass 2: Architecture Document + Data Model (DESIGN mode)
    pass2_system = (
        f"You are Team 2 personas (Chief Architect, Data Architect) in the SeierTech EMS, "
        f"operating in GENESIS MODE — design the architecture and data model forward from the brief "
        f"and use cases, not extracted from any codebase. "
        f"GOVERNED BY:\n{constitution}\n\n"
        "Produce an Architecture Document and Data Model designed for this new platform, conformant to STD-000003."
    )
    pass2_user = f"Platform: {platform_name}\nBrief: {args.brief}\nUse Case Register:\n{pass1_output[:2000]}"
    print("\n=== Genesis Pass 2: Architecture Document + Data Model (DESIGN mode) ===")
    pass2_output = call_nim(api_key, args.model, pass2_system, pass2_user, max_tokens=2500)
    passed2, issues2 = standards_engineer_gate(api_key, args.model, pass2_output, "Architecture Document (Genesis)")
    log.append({"artefact": "Architecture Document", "pass": passed2, "issues": issues2})
    with open(f"{platform_dir}/ARCHITECTURE_DOCUMENT.md", "w") as f:
        f.write(pass2_output)
    print(f"Standards Engineer verdict: {'PASS' if passed2 else 'FAIL'} — {issues2}")

    # Pass 3: Knowledge Graph (DESIGN mode, derived from passes 1-2)
    pass3_system = (
        f"You are the Knowledge Graph Architect (Team 2) in the SeierTech EMS, operating in GENESIS MODE. "
        f"GOVERNED BY:\n{constitution}\n\n"
        "Design a Knowledge Graph for this new platform from the Use Case Register and Architecture "
        "Document below, conformant to STD-000003."
    )
    pass3_user = f"Use Case Register:\n{pass1_output[:1500]}\n\nArchitecture/Data:\n{pass2_output[:1500]}"
    print("\n=== Genesis Pass 3: Knowledge Graph (DESIGN mode) ===")
    pass3_output = call_nim(api_key, args.model, pass3_system, pass3_user, max_tokens=1500)
    passed3, issues3 = standards_engineer_gate(api_key, args.model, pass3_output, "Knowledge Graph (Genesis)")
    log.append({"artefact": "Knowledge Graph", "pass": passed3, "issues": issues3})
    with open(f"{platform_dir}/KNOWLEDGE_GRAPH.md", "w") as f:
        f.write(pass3_output)
    print(f"Standards Engineer verdict: {'PASS' if passed3 else 'FAIL'} — {issues3}")

    # MTS synthesis
    mts_system = (
        f"You are the Master Spec Author (Team 2) in the SeierTech EMS, operating in GENESIS MODE. "
        f"GOVERNED BY:\n{constitution}\n\n"
        "Synthesise the following designed artefacts into a Master Technical Specification, conformant "
        "to STD-000003. State explicitly in the Executive Summary that this platform originated via "
        "MISSION-000 Genesis — every artefact is DESIGNED, not extracted from a pre-existing codebase."
    )
    mts_user = (
        f"Platform: {platform_name}\nBrief: {args.brief}\n\n"
        f"Use Case Register:\n{pass1_output[:1500]}\n\n"
        f"Architecture/Data Model:\n{pass2_output[:1500]}\n\n"
        f"Knowledge Graph:\n{pass3_output[:1500]}"
    )
    print("\n=== Genesis Synthesis: Master Technical Specification (v1) ===")
    mts_output = call_nim(api_key, args.model, mts_system, mts_user, max_tokens=3000)
    passed_mts, issues_mts = standards_engineer_gate(api_key, args.model, mts_output, "Master Technical Specification (Genesis)")
    log.append({"artefact": "Master Technical Specification", "pass": passed_mts, "issues": issues_mts})
    with open(f"{platform_dir}/MASTER_TECHNICAL_SPECIFICATION.md", "w") as f:
        f.write(mts_output)
    print(f"Standards Engineer verdict: {'PASS' if passed_mts else 'FAIL'} — {issues_mts}")

    # Real readiness gate check — same checker used for brownfield, proving convergence
    print("\n=== Running real readiness gate check (RG-001 to RG-010) ===")
    gate_output_path = f"{platform_dir}/READINESS_GATE_RESULT.json"
    gate_result = run_gate_check(platform_dir, platform_name, gate_output_path)
    overall_status = gate_result.get("overall_status", "UNKNOWN")
    print(f"Overall readiness status: {overall_status}")

    genesis_note = f"""# {platform_name} — Genesis Run Log (v1)

| Field | Value |
|---|---|
| Platform | {platform_name} |
| Origin | MISSION-000 Platform Genesis (GREENFIELD) |
| Brief | {args.brief} |
| Issue | #{args.issue_number} |
| Chain Version | v1 — 3 grouped DESIGN-mode passes + MTS synthesis + real gate check |
| Overall Readiness | {overall_status} |

## What This Run Actually Did

1. No repo scan — nothing exists yet, this is the defining trait of genesis
2. Pass 1: Use Case Register + Requirements, designed forward from the brief
3. Pass 2: Architecture Document + Data Model, designed forward from use cases
4. Pass 3: Knowledge Graph, derived from passes 1-2
5. Synthesis: Master Technical Specification (v1 depth, cites source passes)
6. Real deterministic readiness gate check (RG-001 to RG-010) — same checker
   used for brownfield intake, proving both origins converge on the same
   READY state mechanism

## Still NOT Done (see IMPLEMENTATION_STATUS.md)

- No actual GitHub repository created for the new platform yet
- Security Posture and Technical Debt Register not yet produced (even as
  empty-but-present files, which greenfield should have per doctrine)
- Full 25-persona Team 2 depth
- Founder Questions mechanism (RG-008 will show N/A, same as brownfield)

## Standards Engineer Gate Results (per artefact)

{json.dumps(log, indent=2)}

## Readiness Gate Results (RG-001 to RG-010, deterministic check)

{json.dumps(gate_result, indent=2)}
"""
    with open(f"{platform_dir}/GENESIS_RUN_LOG.md", "w") as f:
        f.write(genesis_note)

    print(f"\n=== Genesis chain v1 complete — status: {overall_status} ===")
    print(f"Artefacts written to {platform_dir}/")


if __name__ == "__main__":
    main()
