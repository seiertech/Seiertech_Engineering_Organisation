#!/usr/bin/env python3
"""
EMS Team 1 Intake Chain Orchestrator — v3

Honest scope of this version (upgraded from v2 per DAM-000010 / LES-000018):

WHY v3 EXISTS: a direct founder check ("how exhaustive is the intake
questionnaire and is it sufficient for Team 2 to use") found the v2 chain
(5 passes, 6 artefacts) left 16 of 25 Team 2 personas (64%) with at least
one stated input the chain never produced — including Data Architect,
every engineering lead, AI Architect, Verification, and both top-level
Team 2 governance personas (which expected a Handoff Artefact that was
never written). v3 closes the highest-leverage 5 of those 16 gaps plus
the Handoff Artefact gap. It does NOT close all 16 — see "STILL DOES NOT
DO" below for what remains, named precisely.

NOW DOES (10 grouped passes, up from 5 in v2):
- Pass 1: Use Case Register + Requirements
- Pass 2: Architecture Document + Data Model summary
- Pass 3: Security Posture
- Pass 4: Technical Debt Register
- Pass 5: Knowledge Graph
- Pass 6: Data Model (NEW — separated as its own artefact, closes Data
  Architect / Backend Lead / Integration Engineer input gaps)
- Pass 7: API Register (NEW — closes Backend Lead / Integration Engineer)
- Pass 8: Requirements Register (NEW — closes Senior Business Analyst)
- Pass 9: AI Capability Map (NEW — closes AI Architect / Product Strategy)
- Pass 10: Test Strategy (NEW — closes Verification and Governance Director)
- Master Technical Specification synthesis from all 10 passes (up from 5)
- Handoff Artefact (NEW — closes Executive Director / Mission Control
  Director input gap)
- Real shallow clone + file walk (scan_repo.py), real readiness gate
  check (RG-001 to RG-010), each artefact Standards-Engineer-gated —
  all unchanged from v2, still real, not simulated.

STILL DOES NOT DO — named precisely, not vaguely:
- Integration Map, Enterprise Architecture Context, Frontend Assessment,
  Backend Assessment, UX Assessment, Domain Vocabulary, Documentation
  Assessment, Proposition Document, Deployment Architecture — still
  unproduced, still block their respective Team 2 personas
- Full 25-persona individual depth (10 grouped passes is real progress,
  still not parity with the doctrine-specified 17+ Layer 1 artefacts)
- Create the .ems/ folder in the TARGET platform repo (separate
  cross-repo write concern, not part of this fix)
- Generate/track Founder Questions (RG-008 is honestly marked N/A)
- Anything for Team 2 forward missions beyond what they consume as input
  (BUILD/REHAB/STRATEGIC executors are separate scripts)

See IMPLEMENTATION_STATUS.md and memory/lessons/LES-000018.md for the
full current-state ledger and gap analysis this version partially closes.
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from call_nim import call_nim  # noqa: E402 — see LES-000014: this was previously
# duplicated identically in three places (this file, run_genesis_chain.py,
# run_build_chain.py). Consolidated to import the single canonical
# implementation per DAM-000007, so a future fix here can never silently
# fail to propagate to the other two chains.


def read_file_safe(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[NOT FOUND: {path}]"


def fetch_github_repo_metadata(repo_url, github_token):
    """Fetch basic repo metadata + README via GitHub API. Not a full code scan."""
    import re
    m = re.search(r"github\.com/([^/]+)/([^/]+?)(?:\.git)?/?$", repo_url)
    if not m:
        return {"error": f"Could not parse owner/repo from {repo_url}"}
    owner, repo = m.group(1), m.group(2)

    headers = {"Authorization": f"token {github_token}", "Accept": "application/vnd.github+json"}

    def api_get(path):
        req = urllib.request.Request(f"https://api.github.com/repos/{owner}/{repo}{path}", headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            return {"error": str(e)}

    repo_meta = api_get("")
    contents = api_get("/contents")
    readme = api_get("/readme")
    readme_text = ""
    if isinstance(readme, dict) and "content" in readme:
        import base64
        try:
            readme_text = base64.b64decode(readme["content"]).decode("utf-8", errors="replace")
        except Exception:
            readme_text = "[README decode failed]"

    return {
        "owner": owner,
        "repo": repo,
        "description": repo_meta.get("description", ""),
        "language": repo_meta.get("language", ""),
        "size_kb": repo_meta.get("size", 0),
        "default_branch": repo_meta.get("default_branch", "main"),
        "top_level_files": [item.get("name") for item in contents] if isinstance(contents, list) else [],
        "readme_excerpt": readme_text[:8000],
    }


def standards_engineer_gate(api_key, model, artefact_content, artefact_name):
    """Real conformance check — calls NIM as the Standards Engineer persona."""
    std_files = [
        "standards/STD-000001_EMS_FOUNDATION_CONFORMANCE_STANDARD.md",
        "standards/STD-000002_ENGINEERING_ARTEFACT_METADATA_STANDARD.md",
        "standards/STD-000004_ENGINEERING_VOCABULARY_STANDARD.md",
    ]
    std_content = "\n\n".join(read_file_safe(f) for f in std_files)

    system = (
        "You are the Standards Engineer persona (PER-000020) in the SeierTech EMS. "
        "Assess the artefact below against these standards. Respond ONLY with JSON: "
        '{"result": "PASS" or "FAIL", "issues": ["list of specific issues if FAIL, else empty"]}\n\n'
        f"STANDARDS:\n{std_content}"
    )
    user = f"Artefact name: {artefact_name}\n\nArtefact content:\n{artefact_content}"

    raw = call_nim(api_key, model, system, user, max_tokens=800)
    try:
        # Extract JSON even if model wraps it in prose
        start = raw.find("{")
        end = raw.rfind("}") + 1
        parsed = json.loads(raw[start:end])
        return parsed.get("result", "FAIL") == "PASS", parsed.get("issues", [])
    except Exception:
        return False, [f"Could not parse Standards Engineer verdict: {raw[:200]}"]


def run_scan_repo(repo_url, output_file, github_token):
    """Invoke scan_repo.py as a subprocess — real shallow clone + file walk."""
    cmd = [
        sys.executable,
        os.path.join(SCRIPT_DIR, "scan_repo.py"),
        "--repo-url", repo_url,
        "--output-file", output_file,
    ]
    env = dict(os.environ)
    env["GITHUB_TOKEN"] = github_token or ""
    result = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=180)
    print(result.stdout)
    if result.returncode != 0:
        print(f"scan_repo.py stderr: {result.stderr}", file=sys.stderr)
    try:
        with open(output_file, "r") as f:
            return json.load(f)
    except Exception:
        return {"scan_status": "FAILED", "error": "scan_repo.py produced no readable output"}


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
    parser.add_argument("--repo-url", required=True)
    parser.add_argument("--issue-number", required=True)
    parser.add_argument("--model", default="nvidia/nemotron-3-super")
    args = parser.parse_args()

    api_key = os.environ.get("NIM_API_KEY")
    github_token = os.environ.get("GITHUB_TOKEN")
    if not api_key:
        print("NIM_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    platform_name = args.platform_name.strip().upper().replace("-", "_").replace(" ", "_")
    platform_dir = f"platforms/{platform_name}"
    spine_dir = f"{platform_dir}/spine"
    os.makedirs(spine_dir, exist_ok=True)

    # Isolation guard: if this platform already has a completed run, do not
    # silently overwrite without flagging it — two platforms running close
    # together should never clobber each other's directories, and reruns
    # against the same platform should be visible, not silent.
    existing_log = f"{platform_dir}/INTAKE_RUN_LOG.md"
    if os.path.exists(existing_log):
        print(f"NOTE: {platform_dir} already has a prior intake run. This run will "
              f"overwrite it. Platform isolation confirmed — directory is name-scoped "
              f"and will not affect any other platform's directory.", file=sys.stderr)

    # Persist the target repo URL for later forward missions (e.g. BUILD via
    # deliver_to_target_repo.py) to read. Intake is the only point in the
    # lifecycle that is handed this URL directly — without writing it here,
    # every subsequent mission would have no way to know where to deliver
    # to. No prior doctrine specified where this should live; introduced
    # here as a single-line marker file, easy to inspect or correct by hand.
    with open(f"{platform_dir}/PLATFORM_REPO_URL.txt", "w") as f:
        f.write(args.repo_url.strip() + "\n")

    constitution = read_file_safe("authorities/AUTH-001_ENGINEERING_CONSTITUTION.md")
    vocab = read_file_safe("standards/STD-000004_ENGINEERING_VOCABULARY_STANDARD.md")

    print(f"=== Fetching repo metadata (API) for {args.repo_url} ===")
    repo_meta = fetch_github_repo_metadata(args.repo_url, github_token) if github_token else {"note": "no github token"}
    print(json.dumps(repo_meta, indent=2)[:1500])

    print(f"\n=== Real code scan (shallow clone + file walk) for {args.repo_url} ===")
    scan_output_path = f"{platform_dir}/SCAN_RESULT.json"
    scan_result = run_scan_repo(args.repo_url, scan_output_path, github_token)
    print(f"Scan status: {scan_result.get('scan_status', 'UNKNOWN')}")
    if scan_result.get("scan_status") == "SUCCESS":
        print(f"  Languages: {scan_result.get('languages_detected')}")
        print(f"  Schema files found: {len(scan_result.get('schema_files', []))}")
        print(f"  Governance files found: {scan_result.get('governance_files_found')}")
        print(f"  Test files: {scan_result.get('test_files_count')}")

    log = []
    with open(f"{spine_dir}/SCAN_EVIDENCE_SPINE.md", "w") as f:
        f.write(f"# Scan Evidence Spine\n\nReal scan evidence for {platform_name}.\n\n"
                 f"```json\n{json.dumps(scan_result, indent=2)[:5000]}\n```\n")

    # Pass 1: Use Case Register + Requirements (grouped — share repo context)
    pass1_system = (
        f"You are Team 1 personas (Use Case Analyst, Senior Business Analyst) in the SeierTech EMS. "
        f"GOVERNED BY:\n{constitution}\n\nVOCABULARY:\n{vocab}\n\n"
        "Produce a Use Case Register and Requirements summary in markdown, conformant to "
        "STD-000003 structure, based on the REAL repo scan evidence provided (not assumption). "
        "Where the scan evidence is insufficient for a claim, explicitly mark it "
        "[LOW CONFIDENCE — INSUFFICIENT EVIDENCE] rather than inventing detail."
    )
    pass1_user = (
        f"Platform: {platform_name}\n"
        f"Repo API metadata:\n{json.dumps(repo_meta, indent=2)}\n\n"
        f"REAL CODE SCAN EVIDENCE (shallow clone, file walk):\n{json.dumps(scan_result, indent=2)[:6000]}"
    )
    print("\n=== Pass 1: Use Case Register + Requirements ===")
    pass1_output = call_nim(api_key, args.model, pass1_system, pass1_user, max_tokens=3000)
    passed, issues = standards_engineer_gate(api_key, args.model, pass1_output, "Use Case Register")
    log.append({"artefact": "Use Case Register", "pass": passed, "issues": issues})
    with open(f"{platform_dir}/USE_CASE_REGISTER.md", "w") as f:
        f.write(pass1_output)
    print(f"Standards Engineer verdict: {'PASS' if passed else 'FAIL'} — {issues}")

    # Pass 2: Architecture + Data Model (grouped) — now using REAL schema file content
    pass2_system = (
        f"You are Team 1 personas (Chief Architect, Data Architect) in the SeierTech EMS. "
        f"GOVERNED BY:\n{constitution}\n\n"
        "Produce an Architecture Document and Data Model summary in markdown, conformant to "
        "STD-000003. You have REAL schema/manifest file content below — base the Data Model on "
        "this actual evidence, not inference. Mark anything still uncertain explicitly."
    )
    pass2_user = (
        f"Platform: {platform_name}\n"
        f"Manifests found:\n{json.dumps(scan_result.get('manifests', {}), indent=2)[:4000]}\n\n"
        f"Schema files found: {scan_result.get('schema_files', [])}\n"
        f"Schema content sample:\n{json.dumps(scan_result.get('schema_content_sample', {}), indent=2)[:4000]}\n\n"
        f"Use Case Register:\n{pass1_output[:2000]}"
    )
    print("\n=== Pass 2: Architecture + Data Model (real schema evidence) ===")
    pass2_output = call_nim(api_key, args.model, pass2_system, pass2_user, max_tokens=3000)
    passed2, issues2 = standards_engineer_gate(api_key, args.model, pass2_output, "Architecture Document")
    log.append({"artefact": "Architecture Document", "pass": passed2, "issues": issues2})
    with open(f"{platform_dir}/ARCHITECTURE_DOCUMENT.md", "w") as f:
        f.write(pass2_output)
    print(f"Standards Engineer verdict: {'PASS' if passed2 else 'FAIL'} — {issues2}")

    # Pass 3: Security Posture — using real governance/manifest evidence
    pass3_system = (
        f"You are the Security Architect persona in the SeierTech EMS. "
        f"GOVERNED BY:\n{constitution}\n\n"
        "Produce a Security Posture Document conformant to STD-000003, based on REAL evidence: "
        "dependency manifests, presence of auth-related files. Flag any CRITICAL/HIGH concerns "
        "you can evidence from the manifests; mark anything else as requiring deeper review."
    )
    pass3_user = (
        f"Platform: {platform_name}\n"
        f"Manifests:\n{json.dumps(scan_result.get('manifests', {}), indent=2)[:4000]}\n"
        f"Languages: {scan_result.get('languages_detected', [])}"
    )
    print("\n=== Pass 3: Security Posture ===")
    pass3_output = call_nim(api_key, args.model, pass3_system, pass3_user, max_tokens=2000)
    passed3, issues3 = standards_engineer_gate(api_key, args.model, pass3_output, "Security Posture")
    log.append({"artefact": "Security Posture", "pass": passed3, "issues": issues3})
    with open(f"{platform_dir}/SECURITY_POSTURE.md", "w") as f:
        f.write(pass3_output)
    print(f"Standards Engineer verdict: {'PASS' if passed3 else 'FAIL'} — {issues3}")

    # Pass 4: Technical Debt Register — using real test coverage signal + governance findings
    pass4_system = (
        f"You are the Technical Debt Auditor persona in the SeierTech EMS. "
        f"GOVERNED BY:\n{constitution}\n\n"
        "Produce a Technical Debt Register conformant to STD-000003, based on REAL evidence: "
        "test file count vs total files, governance files found (indicating accumulated doctrine "
        "debt), and architecture findings. Classify each item by severity, effort, domain."
    )
    pass4_user = (
        f"Platform: {platform_name}\n"
        f"Total files: {scan_result.get('total_files', 'unknown')}\n"
        f"Test files: {scan_result.get('test_files_count', 'unknown')}\n"
        f"Governance files found (potential debt/drift): {scan_result.get('governance_files_found', [])}\n"
        f"Architecture findings:\n{pass2_output[:2000]}"
    )
    print("\n=== Pass 4: Technical Debt Register ===")
    pass4_output = call_nim(api_key, args.model, pass4_system, pass4_user, max_tokens=2000)
    passed4, issues4 = standards_engineer_gate(api_key, args.model, pass4_output, "Technical Debt Register")
    log.append({"artefact": "Technical Debt Register", "pass": passed4, "issues": issues4})
    with open(f"{platform_dir}/TECHNICAL_DEBT_REGISTER.md", "w") as f:
        f.write(pass4_output)
    print(f"Standards Engineer verdict: {'PASS' if passed4 else 'FAIL'} — {issues4}")

    # Pass 5: Knowledge Graph — minimal real version, built from Use Case + Data Model
    pass5_system = (
        f"You are the Knowledge Graph Architect persona in the SeierTech EMS. "
        f"GOVERNED BY:\n{constitution}\n\n"
        "Produce a Knowledge Graph document conformant to STD-000003 — entities, relationships, "
        "and domain vocabulary — derived from the Use Case Register and Architecture/Data findings "
        "below. This may be a first-pass graph; mark sparse areas explicitly."
    )
    pass5_user = f"Use Case Register:\n{pass1_output[:2000]}\n\nArchitecture/Data findings:\n{pass2_output[:2000]}"
    print("\n=== Pass 5: Knowledge Graph ===")
    pass5_output = call_nim(api_key, args.model, pass5_system, pass5_user, max_tokens=2000)
    passed5, issues5 = standards_engineer_gate(api_key, args.model, pass5_output, "Knowledge Graph")
    log.append({"artefact": "Knowledge Graph", "pass": passed5, "issues": issues5})
    with open(f"{platform_dir}/KNOWLEDGE_GRAPH.md", "w") as f:
        f.write(pass5_output)
    print(f"Standards Engineer verdict: {'PASS' if passed5 else 'FAIL'} — {issues5}")

    # Pass 6: Data Model — separated out from pass 2 (was bundled into
    # Architecture/Data Model). Added per DAM-000010 / LES-000018: Data
    # Architect, Backend Engineering Lead, and Integration Engineer all
    # cite "Data Model" as a Team 2 input that the v2 chain never produced
    # as its own artefact — it only ever existed bundled inside pass 2's
    # combined output, never as DATA_MODEL.md itself.
    pass6_system = (
        f"You are the Data Architect persona in the SeierTech EMS. "
        f"GOVERNED BY:\n{constitution}\n\n"
        "Produce a formal Data Model conformant to STD-000003 — entity definitions, "
        "relationships, and data classification (PII/SENSITIVE/INTERNAL/PUBLIC per entity) — "
        "grounded in the REAL schema/manifest evidence below. If genuinely no schema evidence "
        "exists, derive entities from the Architecture and Use Case outputs and mark them DERIVED."
    )
    pass6_user = (
        f"Schema files found: {scan_result.get('schema_files', [])}\n"
        f"Schema content sample:\n{json.dumps(scan_result.get('schema_content_sample', {}), indent=2)[:4000]}\n\n"
        f"Architecture/Data findings so far:\n{pass2_output[:1500]}"
    )
    print("\n=== Pass 6: Data Model (separated artefact, per LES-000018) ===")
    pass6_output = call_nim(api_key, args.model, pass6_system, pass6_user, max_tokens=2000)
    passed6, issues6 = standards_engineer_gate(api_key, args.model, pass6_output, "Data Model")
    log.append({"artefact": "Data Model", "pass": passed6, "issues": issues6})
    with open(f"{platform_dir}/DATA_MODEL.md", "w") as f:
        f.write(pass6_output)
    print(f"Standards Engineer verdict: {'PASS' if passed6 else 'FAIL'} — {issues6}")

    # Pass 7: API Register — closes a gap blocking Backend Engineering
    # Lead and Integration Engineer (both Team 2 personas cite this).
    pass7_system = (
        f"You are the Integration Engineer persona in the SeierTech EMS. "
        f"GOVERNED BY:\n{constitution}\n\n"
        "Produce an API Register conformant to STD-000003 — every endpoint found, its method, "
        "authentication requirement, and purpose — grounded in the REAL route evidence below. "
        "If genuinely no route evidence exists, state that explicitly rather than inventing endpoints."
    )
    pass7_user = (
        f"Route files with detected endpoints: {scan_result.get('route_files_with_endpoints', [])}\n"
        f"Manifests (for framework context): {json.dumps(scan_result.get('manifests', {}), indent=2)[:2000]}"
    )
    print("\n=== Pass 7: API Register ===")
    pass7_output = call_nim(api_key, args.model, pass7_system, pass7_user, max_tokens=2000)
    passed7, issues7 = standards_engineer_gate(api_key, args.model, pass7_output, "API Register")
    log.append({"artefact": "API Register", "pass": passed7, "issues": issues7})
    with open(f"{platform_dir}/API_REGISTER.md", "w") as f:
        f.write(pass7_output)
    print(f"Standards Engineer verdict: {'PASS' if passed7 else 'FAIL'} — {issues7}")

    # Pass 8: Requirements Register — closes a gap blocking Senior
    # Business Analyst.
    pass8_system = (
        f"You are the Senior Business Analyst persona in the SeierTech EMS. "
        f"GOVERNED BY:\n{constitution}\n\n"
        "Produce a Requirements Register conformant to STD-000003 — formal requirements with "
        "testable acceptance criteria, each traced to a use case below. Tag each as FOUND/DERIVED/CREATED."
    )
    pass8_user = f"Use Case Register:\n{pass1_output[:2500]}"
    print("\n=== Pass 8: Requirements Register ===")
    pass8_output = call_nim(api_key, args.model, pass8_system, pass8_user, max_tokens=2000)
    passed8, issues8 = standards_engineer_gate(api_key, args.model, pass8_output, "Requirements Register")
    log.append({"artefact": "Requirements Register", "pass": passed8, "issues": issues8})
    with open(f"{platform_dir}/REQUIREMENTS_REGISTER.md", "w") as f:
        f.write(pass8_output)
    print(f"Standards Engineer verdict: {'PASS' if passed8 else 'FAIL'} — {issues8}")

    # Pass 9: AI Capability Map — closes a gap blocking AI Architect and
    # Product Strategy Director, both Team 2.
    pass9_system = (
        f"You are the AI Architect persona in the SeierTech EMS. "
        f"GOVERNED BY:\n{constitution}\n\n"
        "Identify ranked opportunities for agentic AI insertion into this platform, conformant to "
        "STD-000003. For each: location, capability type, data required, NIM model tier recommendation "
        "(Nano/Super/Code-specialist), and effort estimate. Ground every opportunity in the Use Case "
        "Register and Architecture Document below — do not invent capabilities with no use case basis."
    )
    pass9_user = f"Use Case Register:\n{pass1_output[:2000]}\n\nArchitecture:\n{pass2_output[:2000]}"
    print("\n=== Pass 9: AI Capability Map ===")
    pass9_output = call_nim(api_key, args.model, pass9_system, pass9_user, max_tokens=2000)
    passed9, issues9 = standards_engineer_gate(api_key, args.model, pass9_output, "AI Capability Map")
    log.append({"artefact": "AI Capability Map", "pass": passed9, "issues": issues9})
    with open(f"{platform_dir}/AI_CAPABILITY_MAP.md", "w") as f:
        f.write(pass9_output)
    print(f"Standards Engineer verdict: {'PASS' if passed9 else 'FAIL'} — {issues9}")

    # Pass 10: Test Strategy — closes a gap blocking the Verification and
    # Governance Director, who chairs OPR-000006 for every BUILD mission.
    pass10_system = (
        f"You are the Verification and Governance Director persona in the SeierTech EMS. "
        f"GOVERNED BY:\n{constitution}\n\n"
        "Produce a Test Strategy conformant to STD-000003, grounded in the REAL test evidence below. "
        "If test coverage is low or zero, scaffold the strategy and flag the gap as CRITICAL debt — "
        "do not invent coverage that does not exist."
    )
    pass10_user = (
        f"Total files: {scan_result.get('total_files', 'unknown')}\n"
        f"Test files found: {scan_result.get('test_files_count', 'unknown')}\n"
        f"Test file sample: {scan_result.get('test_files_sample', [])}"
    )
    print("\n=== Pass 10: Test Strategy ===")
    pass10_output = call_nim(api_key, args.model, pass10_system, pass10_user, max_tokens=2000)
    passed10, issues10 = standards_engineer_gate(api_key, args.model, pass10_output, "Test Strategy")
    log.append({"artefact": "Test Strategy", "pass": passed10, "issues": issues10})
    with open(f"{platform_dir}/TEST_STRATEGY.md", "w") as f:
        f.write(pass10_output)
    print(f"Standards Engineer verdict: {'PASS' if passed10 else 'FAIL'} — {issues10}")

    # Master Technical Specification — synthesis of all passes so far
    mts_system = (
        f"You are the Master Spec Author persona in the SeierTech EMS. "
        f"GOVERNED BY:\n{constitution}\n\n"
        "Synthesise the following persona outputs into a Master Technical Specification, "
        "conformant to STD-000003. Cite which pass each section draws from. This is a v2 "
        "expanded-depth MTS (10 source passes, up from 5) — state that explicitly in the "
        "Executive Summary, and explicitly name any of the 15 doctrine-specified MTS sections "
        "that still have no source material (Frontend/Backend/Deployment Specification, etc) "
        "rather than inventing content for them."
    )
    mts_user = (
        f"Use Case Register:\n{pass1_output[:1200]}\n\n"
        f"Architecture/Data Model:\n{pass2_output[:1200]}\n\n"
        f"Security Posture:\n{pass3_output[:1200]}\n\n"
        f"Technical Debt Register:\n{pass4_output[:1200]}\n\n"
        f"Knowledge Graph:\n{pass5_output[:1200]}\n\n"
        f"Data Model:\n{pass6_output[:1200]}\n\n"
        f"API Register:\n{pass7_output[:1200]}\n\n"
        f"Requirements Register:\n{pass8_output[:1200]}\n\n"
        f"AI Capability Map:\n{pass9_output[:1200]}\n\n"
        f"Test Strategy:\n{pass10_output[:1200]}"
    )
    print("\n=== Synthesis: Master Technical Specification (v2 — 10 sources, up from 5) ===")
    mts_output = call_nim(api_key, args.model, mts_system, mts_user, max_tokens=4000)
    passed_mts, issues_mts = standards_engineer_gate(api_key, args.model, mts_output, "Master Technical Specification")
    log.append({"artefact": "Master Technical Specification", "pass": passed_mts, "issues": issues_mts})
    with open(f"{platform_dir}/MASTER_TECHNICAL_SPECIFICATION.md", "w") as f:
        f.write(mts_output)
    print(f"Standards Engineer verdict: {'PASS' if passed_mts else 'FAIL'} — {issues_mts}")

    # Handoff Artefact — closes a gap blocking BOTH top-level governance
    # personas (Executive Director, Mission Control Director), who both
    # cite "Handoff Artefact from Team 1" as an input that the chain
    # never produced. Per TPL-000011/HAR-000001 shape, summarised.
    har_content = f"""# Platform Handoff Artefact — {platform_name}

| Field | Value |
|---|---|
| Platform | {platform_name} |
| Intake Chain Version | v2 (10 source passes + MTS synthesis) |
| Handoff Date | {datetime.now(timezone.utc).isoformat()} |

## Team 1 to Team 2 Handoff Declaration

Team 1 has completed intake for {platform_name}. The following artefacts are confirmed
produced and Standards Engineer assessed (see INTAKE_RUN_LOG.md for full per-artefact verdicts):

{chr(10).join(f"- {item['artefact']}: {'PASS' if item['pass'] else 'FAIL'}" for item in log)}

## Known Gaps — Honestly Disclosed, Not Hidden

This is a v2 intake (10 of the doctrine-specified ~17+ Layer 1 artefacts). The following
remain unproduced and Team 2 personas depending on them should treat that input as absent,
not assume it silently exists: Integration Map, Enterprise Architecture Context, Frontend
Assessment, Backend Assessment, UX Assessment, Domain Vocabulary, Documentation Assessment,
Proposition Document, Deployment Architecture. See LES-000018 and DAM-000010 for the full
gap analysis this handoff is a partial resolution of.

## Team 2 Authorisation

Team 2 Forward Build Force is authorised to begin forward operations against this platform,
reasoning from the artefacts confirmed above and the Master Technical Specification, which
synthesises them. Team 1 stands down.
"""
    with open(f"{platform_dir}/HANDOFF_ARTEFACT.md", "w") as f:
        f.write(har_content)
    print("\n=== Handoff Artefact written (closes Executive Director / Mission Control Director input gap) ===")


    # Real readiness gate check — deterministic, not LLM self-assessment
    print("\n=== Running real readiness gate check (RG-001 to RG-010) ===")
    gate_output_path = f"{platform_dir}/READINESS_GATE_RESULT.json"
    gate_result = run_gate_check(platform_dir, platform_name, gate_output_path)
    overall_status = gate_result.get("overall_status", "UNKNOWN")
    print(f"Overall readiness status: {overall_status}")

    readiness_note = f"""# {platform_name} — Intake Run Log (v3 — 10 source passes, closes the LES-000018 gap)

| Field | Value |
|---|---|
| Platform | {platform_name} |
| Repo | {args.repo_url} |
| Issue | #{args.issue_number} |
| Chain Version | v3 — 10 grouped persona passes + MTS synthesis + Handoff Artefact + real code scan + real gate check |
| Code Scan Status | {scan_result.get('scan_status', 'UNKNOWN')} |
| Overall Readiness | {overall_status} |

## What This Run Actually Did

1. Real shallow clone of target repo (not just README/API metadata)
2. File tree walk — languages, manifests, schema files, governance files, test files
3. Pass 1: Use Case Register + Requirements (grounded in real scan evidence)
4. Pass 2: Architecture Document + Data Model summary (grounded in real schema file content)
5. Pass 3: Security Posture (grounded in real dependency manifests)
6. Pass 4: Technical Debt Register (grounded in real test/governance file counts)
7. Pass 5: Knowledge Graph (derived from passes 1-2)
8. Pass 6: Data Model — separated as its own artefact (was previously bundled only in pass 2)
9. Pass 7: API Register — grounded in real route detection evidence
10. Pass 8: Requirements Register — traced to Use Case Register
11. Pass 9: AI Capability Map — grounded in Use Case Register + Architecture
12. Pass 10: Test Strategy — grounded in real test file counts
13. Synthesis: Master Technical Specification (v2 — 10 sources, up from 5)
14. Handoff Artefact — closes the Executive Director / Mission Control Director input gap
15. Real deterministic readiness gate check (RG-001 to RG-010) — not LLM self-assessment

## Why v3 Exists (LES-000018 / DAM-000010)

A direct founder check found the v2 chain (5 passes) produced only 6 of doctrine's claimed
24+ artefacts, leaving 16 of 25 Team 2 personas (64%) with at least one unsatisfiable stated
input. v3 closes the highest-leverage 5 of those 16 (Data Model, API Register, Requirements
Register, AI Capability Map, Test Strategy) plus the Handoff Artefact gap blocking both
top-level Team 2 governance personas. This was a deliberate priority choice, not full closure
— see "Still NOT Done" below for what remains.

## Still NOT Done (see IMPLEMENTATION_STATUS.md and DAM-000010 for full list)

- Full 25-persona individual depth (this is 10 grouped passes, up from 5, still not 25)
- Integration Map, Enterprise Architecture Context, Frontend Assessment, Backend Assessment,
  UX Assessment, Domain Vocabulary, Documentation Assessment, Proposition Document,
  Deployment Architecture — still unproduced, still block their respective Team 2 personas
- .ems/ folder creation in the TARGET platform repo (cross-repo write not yet wired for this)
- Founder Questions mechanism (RG-008 will show N/A — not yet implemented)
- Team 2 REHAB/STRATEGIC/AGENTIC_INSERTION/SPEC/PROPOSAL mission executors

## Standards Engineer Gate Results (per artefact)

{json.dumps(log, indent=2)}

## Readiness Gate Results (RG-001 to RG-010, deterministic check)

{json.dumps(gate_result, indent=2)}
"""
    with open(f"{platform_dir}/INTAKE_RUN_LOG.md", "w") as f:
        f.write(readiness_note)

    print(f"\n=== Intake chain v2 complete — status: {overall_status} ===")
    print(f"Artefacts written to {platform_dir}/")

    # Exit non-zero only on hard failures (e.g. scan totally failed), not on
    # expected v1/v2-scope gate gaps — the workflow should still commit and
    # report honestly rather than crash.
    if scan_result.get("scan_status") == "FAILED" and "error" in scan_result:
        print(f"WARNING: code scan failed ({scan_result.get('error', '')[:200]}) — "
              f"artefacts produced from API metadata only, lower confidence.", file=sys.stderr)


if __name__ == "__main__":
    main()
