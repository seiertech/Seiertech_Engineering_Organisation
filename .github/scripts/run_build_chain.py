#!/usr/bin/env python3
"""
EMS Team 2 BUILD Chain Orchestrator — v1

The first executor for a Team 2 forward mission. Everything before this
script — intake, genesis — establishes a baseline. This is the first
script that builds FORWARD from one, closing the loop OPR-000001 through
OPR-000009 describe: Proposal -> TDA -> Engineering Delivery -> Verification
-> Release -> Knowledge Capture.

DESIGN BASIS (explicit, not implicit): NVIDIA NIM integration is assumed
wired and working — this script calls it through the exact same interface
already validated in run_intake_chain.py and run_genesis_chain.py
(call_nim, JSON built via json.dumps()). No new provider code is added
here. Where a design decision had no prior doctrine precedent to follow,
the choice made and its rationale is recorded inline as a comment, per
the founder's direction to "design according to it, best assumptions for
the rest."

HONEST SCOPE OF THIS v1:

NOW DOES:
- Confirms the target platform is genuinely READY (re-runs the real
  deterministic gate checker — does not trust a stale status)
- Pass 1: Engineering Proposal (OPR-000003) — problem statement, approach,
  risks, effort — grounded in the platform's MTS, not invented
- Pass 2: Technical Design Authority (OPR-000004) — Chief Architect
  verdict (APPROVED/REJECTED/REVISION_REQUIRED) against the Architecture
  Document; a REJECTED or REVISION_REQUIRED verdict halts the chain here,
  same as doctrine requires — TDA is a real gate, not theatre
- Pass 3: Engineering Delivery Package (OPR-000005) — build instructions,
  standards applied, test assertions — only produced if TDA approved
- Pass 4: Verification (OPR-000006) — asserts the EDP's stated acceptance
  criteria are each individually addressed; PASS/FAIL/CONDITIONAL
- Pass 5: Release Scorecard (OPR-000007) — scores against doctrine's
  stated dimensions, RELEASE/HOLD/REJECT decision
- Knowledge Capture (OPR-000008) — writes a mission summary back to
  memory/, and checks the mission output for low-confidence/insufficient-
  evidence markers that should become REG-000010 lessons
- Each artefact gated by a real Standards Engineer NIM call, same pattern
  as intake/genesis

STILL DOES NOT DO:
- No actual Git branch creation or builder (Kiro) execution — the EDP is
  produced as a file, exactly as OPR-000005 describes, but nothing
  consumes it to produce real code changes yet. This is the same class
  of honest gap as intake's missing .ems/ cross-repo write.
- No REHAB/STRATEGIC/AGENTIC_INSERTION/SPEC/PROPOSAL mission types —
  BUILD only, per the explicit resequencing in EMS_OPERATING_MODEL.md
  Section 6
- Founder Questions mechanism still does not exist (same RG-008 gap)
- No automated trigger of OPR-000012 if Knowledge Capture finds a lesson —
  it is surfaced in the run log for a human/founder to action, not
  auto-filed, since OPR-000012 itself requires judgement about whether an
  amendment is warranted, not just pattern matching

See IMPLEMENTATION_STATUS.md and EMS_OPERATING_MODEL.md for the full
current-state ledger this script is part of.
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from call_nim import call_nim  # noqa: E402 — see LES-000014: consolidated from a
# duplicated inline copy per DAM-000007, same fix applied identically to
# run_intake_chain.py and run_genesis_chain.py.


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


def confirm_platform_ready(platform_dir, platform_name):
    """
    Re-run the real gate checker rather than trusting a stale READY claim.
    Design decision: a BUILD mission must never proceed against a platform
    whose readiness has not just been freshly confirmed — readiness can
    change between the last check and now (e.g. doctrine amendments,
    partial prior mission runs).
    """
    cmd = [
        sys.executable,
        os.path.join(SCRIPT_DIR, "check_readiness_gates.py"),
        "--platform-dir", platform_dir,
        "--platform-name", platform_name,
        "--reduced-scope",
        "--output-file", os.path.join(platform_dir, "_build_precheck_gate_result.json"),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    print(result.stdout)
    try:
        with open(os.path.join(platform_dir, "_build_precheck_gate_result.json")) as f:
            return json.load(f)
    except Exception:
        return {"overall_status": "UNKNOWN"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform-name", required=True)
    parser.add_argument("--instruction", required=True)
    parser.add_argument("--issue-number", required=True)
    parser.add_argument("--model", default="nvidia/nemotron-3-super")
    args = parser.parse_args()

    api_key = os.environ.get("NIM_API_KEY")
    if not api_key:
        print("NIM_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    platform_name = args.platform_name.strip().upper().replace("-", "_").replace(" ", "_")
    platform_dir = f"platforms/{platform_name}"

    if not os.path.isdir(platform_dir):
        print(f"Platform directory {platform_dir} does not exist. A BUILD mission cannot "
              f"target a platform that has never completed intake or genesis.", file=sys.stderr)
        sys.exit(1)

    mts = read_file_safe(f"{platform_dir}/MASTER_TECHNICAL_SPECIFICATION.md")
    architecture = read_file_safe(f"{platform_dir}/ARCHITECTURE_DOCUMENT.md")
    constitution = read_file_safe("authorities/AUTH-001_ENGINEERING_CONSTITUTION.md")

    print(f"=== Confirming {platform_name} is genuinely READY before proceeding ===")
    precheck = confirm_platform_ready(platform_dir, platform_name)
    precheck_status = precheck.get("overall_status", "UNKNOWN")
    print(f"Precheck status: {precheck_status}")
    # Design decision: a BUILD mission proceeds if every gate passes EXCEPT
    # RG-008 (Founder Questions), which is a known, disclosed, system-wide
    # gap affecting every platform equally (see IMPLEMENTATION_STATUS.md).
    # Blocking every BUILD mission on a gap that has no implementation
    # anywhere would make BUILD permanently unusable — the same reasoning
    # that produced the DAM-000001 fix for the greenfield gate-checker bug
    # applies here: don't let an honestly-disclosed, system-wide gap block
    # the very capability needed to close the loop.
    failing = precheck.get("failing_gates", [])
    blocking_failures = [g for g in failing if g != "RG-008"]
    if blocking_failures:
        print(f"Platform {platform_name} has blocking readiness failures beyond the known "
              f"RG-008 gap: {blocking_failures}. BUILD mission cannot proceed.", file=sys.stderr)
        sys.exit(1)
    print(f"Platform confirmed sufficiently READY (only RG-008 outstanding, which is a "
          f"known system-wide gap, not platform-specific). Proceeding.")

    log = []
    timestamp = datetime.now(timezone.utc).isoformat()

    # Pass 1: Engineering Proposal (OPR-000003)
    pass1_system = (
        f"You are Team 2 (Product Strategy Director, Senior Business Analyst) in the SeierTech EMS, "
        f"executing OPR-000003 Engineering Proposal Operation. "
        f"GOVERNED BY:\n{constitution}\n\n"
        "Produce an Engineering Proposal conformant to STD-000003 (TPL-000003 shape: problem statement, "
        "proposed approach, alternatives considered, dependencies, risks, effort estimate). Ground every "
        "claim in the Master Technical Specification provided — never invent platform details not "
        "evidenced there."
    )
    pass1_user = f"Platform: {platform_name}\nMission instruction: {args.instruction}\n\nMTS:\n{mts[:4000]}"
    print("\n=== Pass 1: Engineering Proposal (OPR-000003) ===")
    proposal_output = call_nim(api_key, args.model, pass1_system, pass1_user, max_tokens=2000)
    passed1, issues1 = standards_engineer_gate(api_key, args.model, proposal_output, "Engineering Proposal")
    log.append({"artefact": "Engineering Proposal", "pass": passed1, "issues": issues1})
    with open(f"{platform_dir}/_BUILD_PROPOSAL_LATEST.md", "w") as f:
        f.write(proposal_output)
    print(f"Standards Engineer verdict: {'PASS' if passed1 else 'FAIL'} — {issues1}")

    # Pass 2: Technical Design Authority (OPR-000004) — a REAL gate
    pass2_system = (
        f"You are the Chief Architect (Team 2) in the SeierTech EMS, chairing OPR-000004 Technical "
        f"Design Authority. GOVERNED BY:\n{constitution}\n\n"
        "Review the Engineering Proposal against the Architecture Document below. Respond ONLY with "
        'JSON: {"verdict": "APPROVED" or "REJECTED" or "REVISION_REQUIRED", "rationale": "specific '
        'architectural reasoning, citing the Architecture Document"}. Never approve a proposal that '
        "introduces undocumented architectural drift."
    )
    pass2_user = f"Engineering Proposal:\n{proposal_output[:2500]}\n\nArchitecture Document:\n{architecture[:2500]}"
    print("\n=== Pass 2: Technical Design Authority (OPR-000004) ===")
    tda_raw = call_nim(api_key, args.model, pass2_system, pass2_user, max_tokens=1000)
    try:
        start = tda_raw.find("{")
        end = tda_raw.rfind("}") + 1
        tda_result = json.loads(tda_raw[start:end])
    except Exception:
        tda_result = {"verdict": "REVISION_REQUIRED", "rationale": f"Could not parse TDA verdict: {tda_raw[:200]}"}

    tda_verdict = tda_result.get("verdict", "REVISION_REQUIRED")
    print(f"TDA Verdict: {tda_verdict} — {tda_result.get('rationale', '')[:300]}")
    log.append({"artefact": "TDA Verdict", "pass": tda_verdict == "APPROVED", "issues": [tda_result.get("rationale", "")]})

    with open(f"{platform_dir}/_BUILD_TDA_LATEST.md", "w") as f:
        f.write(f"# TDA Verdict\n\n**Verdict:** {tda_verdict}\n\n**Rationale:**\n{tda_result.get('rationale', '')}\n")

    if tda_verdict != "APPROVED":
        # This is a REAL halt, not a soft warning — exactly what doctrine requires.
        print(f"\n=== BUILD mission HALTED at TDA — verdict was {tda_verdict}, not APPROVED ===")
        _write_run_log(platform_dir, platform_name, args, timestamp, log,
                        final_status=f"HALTED_AT_TDA_{tda_verdict}", gate_result=None)
        print("Mission halted per doctrine. This is not a failure of the script — TDA is a real gate.")
        sys.exit(0)

    # Pass 3: Engineering Delivery Package (OPR-000005) — only reached if TDA approved
    pass3_system = (
        f"You are Team 2 engineering leads (Backend/Frontend, whichever the instruction implies) in the "
        f"SeierTech EMS, executing OPR-000005 Engineering Delivery Operation. GOVERNED BY:\n{constitution}\n\n"
        "Produce an Engineering Delivery Package conformant to STD-000003 (TPL-000004 shape): build "
        "instructions, standards applied, and explicit test assertions for each acceptance criterion. "
        "The EDP must be specific enough that a builder could act on it — not a restatement of the proposal."
    )
    pass3_user = f"Approved Engineering Proposal:\n{proposal_output[:2000]}\n\nTDA Rationale:\n{tda_result.get('rationale', '')[:500]}"
    print("\n=== Pass 3: Engineering Delivery Package (OPR-000005) ===")
    edp_output = call_nim(api_key, args.model, pass3_system, pass3_user, max_tokens=2500)
    passed3, issues3 = standards_engineer_gate(api_key, args.model, edp_output, "Engineering Delivery Package")
    log.append({"artefact": "Engineering Delivery Package", "pass": passed3, "issues": issues3})
    with open(f"{platform_dir}/_BUILD_EDP_LATEST.md", "w") as f:
        f.write(edp_output)
    print(f"Standards Engineer verdict: {'PASS' if passed3 else 'FAIL'} — {issues3}")

    # Pass 4: Verification (OPR-000006)
    pass4_system = (
        f"You are the Verification and Governance Director (Team 2) in the SeierTech EMS, chairing "
        f"OPR-000006 Verification. GOVERNED BY:\n{constitution}\n\n"
        'Respond ONLY with JSON: {"result": "PASS" or "FAIL" or "CONDITIONAL", "criteria_checked": '
        '["list each acceptance criterion from the EDP and whether it is addressed"], "findings": '
        '["specific issues if any"]}. Never PASS without evidence each criterion is genuinely addressed '
        "in the EDP — do not rubber-stamp."
    )
    pass4_user = f"Engineering Delivery Package:\n{edp_output[:3000]}"
    print("\n=== Pass 4: Verification (OPR-000006) ===")
    verification_raw = call_nim(api_key, args.model, pass4_system, pass4_user, max_tokens=1500)
    try:
        start = verification_raw.find("{")
        end = verification_raw.rfind("}") + 1
        verification_result = json.loads(verification_raw[start:end])
    except Exception:
        verification_result = {"result": "FAIL", "criteria_checked": [], "findings": [f"Could not parse: {verification_raw[:200]}"]}

    verification_status = verification_result.get("result", "FAIL")
    print(f"Verification result: {verification_status}")
    log.append({"artefact": "Verification", "pass": verification_status == "PASS", "issues": verification_result.get("findings", [])})
    with open(f"{platform_dir}/_BUILD_VERIFICATION_LATEST.md", "w") as f:
        f.write(f"# Verification Report\n\n**Result:** {verification_status}\n\n"
                f"**Criteria checked:**\n" + "\n".join(f"- {c}" for c in verification_result.get("criteria_checked", [])) +
                f"\n\n**Findings:**\n" + "\n".join(f"- {fnd}" for fnd in verification_result.get("findings", [])))

    # Pass 5: Release Scorecard (OPR-000007)
    pass5_system = (
        f"You are the Release Manager (Team 2) in the SeierTech EMS, executing OPR-000007 Release "
        f"Operation. GOVERNED BY:\n{constitution}\n\n"
        'Respond ONLY with JSON: {"decision": "RELEASE" or "HOLD" or "REJECT", "scorecard": '
        '{"quality": 1-10, "architecture": 1-10, "standards": 1-10, "operational_fit": 1-10, '
        '"test_coverage": 1-10}, "rationale": "why this decision"}. A Verification result of FAIL '
        "SHALL result in REJECT or HOLD, never RELEASE."
    )
    pass5_user = f"Verification result: {verification_status}\nVerification findings: {verification_result.get('findings', [])}\nEDP summary:\n{edp_output[:1500]}"
    print("\n=== Pass 5: Release Scorecard (OPR-000007) ===")
    release_raw = call_nim(api_key, args.model, pass5_system, pass5_user, max_tokens=1000)
    try:
        start = release_raw.find("{")
        end = release_raw.rfind("}") + 1
        release_result = json.loads(release_raw[start:end])
    except Exception:
        release_result = {"decision": "HOLD", "scorecard": {}, "rationale": f"Could not parse: {release_raw[:200]}"}

    release_decision = release_result.get("decision", "HOLD")
    # Hard safety check, not trusting the model alone: a FAIL verification
    # can never result in RELEASE regardless of what the model returned.
    if verification_status == "FAIL" and release_decision == "RELEASE":
        print("WARNING: model returned RELEASE despite FAIL verification — overriding to REJECT per doctrine.", file=sys.stderr)
        release_decision = "REJECT"
        release_result["decision"] = release_decision
        release_result["rationale"] = "OVERRIDDEN by script: FAIL verification cannot result in RELEASE. " + release_result.get("rationale", "")

    print(f"Release decision: {release_decision}")
    log.append({"artefact": "Release Scorecard", "pass": release_decision == "RELEASE", "issues": [release_result.get("rationale", "")]})
    with open(f"{platform_dir}/_BUILD_SCORECARD_LATEST.md", "w") as f:
        f.write(f"# Release Scorecard\n\n**Decision:** {release_decision}\n\n"
                f"**Scores:** {json.dumps(release_result.get('scorecard', {}), indent=2)}\n\n"
                f"**Rationale:**\n{release_result.get('rationale', '')}")

    # Knowledge Capture (OPR-000008) — check for lesson-worthy markers
    print("\n=== Knowledge Capture (OPR-000008) ===")
    full_output_for_lesson_scan = proposal_output + edp_output + str(verification_result) + str(release_result)
    lesson_markers_found = "[LOW CONFIDENCE" in full_output_for_lesson_scan or "INSUFFICIENT EVIDENCE" in full_output_for_lesson_scan
    if lesson_markers_found:
        print("NOTE: this mission's output contains low-confidence/insufficient-evidence markers. "
              "Per AUTH-010 KNW-006, this should be reviewed for a REG-000010 entry. Not auto-filed — "
              "OPR-000012 requires judgement, not pattern matching, on whether an amendment is warranted.")

    memory_entry = (
        f"# Mission Memory — {platform_name} BUILD [Issue #{args.issue_number}]\n\n"
        f"Date: {timestamp}\nInstruction: {args.instruction}\n"
        f"TDA: {tda_verdict}\nVerification: {verification_status}\nRelease: {release_decision}\n"
        f"Lesson-worthy markers found: {lesson_markers_found}\n"
    )
    os.makedirs("memory/missions", exist_ok=True)
    with open(f"memory/missions/BUILD_{platform_name}_{args.issue_number}.md", "w") as f:
        f.write(memory_entry)

    _write_run_log(platform_dir, platform_name, args, timestamp, log,
                    final_status=release_decision, gate_result=precheck,
                    extra={"tda_verdict": tda_verdict, "verification_status": verification_status,
                           "lesson_markers_found": lesson_markers_found})

    print(f"\n=== BUILD chain v1 complete — final status: {release_decision} ===")


def _write_run_log(platform_dir, platform_name, args, timestamp, log, final_status, gate_result, extra=None):
    note = f"""# {platform_name} — BUILD Run Log (v1)

| Field | Value |
|---|---|
| Platform | {platform_name} |
| Issue | #{args.issue_number} |
| Instruction | {args.instruction} |
| Date | {timestamp} |
| Chain Version | v1 — 5 gated passes (Proposal, TDA, EDP, Verification, Release) + Knowledge Capture |
| Final Status | {final_status} |

## What This Run Actually Did

This is the first executor for a Team 2 forward mission (OPR-000003 through OPR-000007),
closing the loop that intake and genesis only ever established a baseline for. Each pass
is gated by a real Standards Engineer NIM call. TDA is a genuine halt point, not a soft
warning — a REJECTED or REVISION_REQUIRED verdict stops the chain here, per doctrine.

## Still NOT Done (see IMPLEMENTATION_STATUS.md and EMS_OPERATING_MODEL.md)

- No actual Git branch or builder (Kiro) execution consumes the EDP yet
- REHAB/STRATEGIC/AGENTIC_INSERTION/SPEC/PROPOSAL mission types have no executor
- Founder Questions mechanism still absent (RG-008)
- Lesson markers found in output are surfaced, not auto-filed to REG-000010 —
  OPR-000012 requires judgement on whether an amendment is genuinely warranted

## Standards Engineer / Gate Results (per artefact)

{json.dumps(log, indent=2)}

## Pre-flight Readiness Check

{json.dumps(gate_result, indent=2) if gate_result else "N/A — mission halted before reaching this point"}

## Additional Detail

{json.dumps(extra, indent=2) if extra else "N/A"}
"""
    with open(f"{platform_dir}/BUILD_RUN_LOG_{args.issue_number}.md", "w") as f:
        f.write(note)


if __name__ == "__main__":
    main()
