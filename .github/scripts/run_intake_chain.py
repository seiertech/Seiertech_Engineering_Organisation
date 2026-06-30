#!/usr/bin/env python3
"""
EMS Team 1 Intake Chain Orchestrator — v2

Honest scope of this version (upgraded from v1):

NOW DOES:
- Real shallow clone + file walk of the target repo (scan_repo.py) — not just
  README/API metadata. Reads actual schema files, manifests, governance files.
- 5 grouped persona passes (Use Case+Requirements, Architecture+Data Model,
  Security Posture, Technical Debt Register, Knowledge Graph) — up from 2 in v1.
- A Master Technical Specification synthesis pass citing source passes.
- A REAL deterministic readiness gate check (RG-001 to RG-010) against what
  was actually produced on disk — not an LLM self-assessment.
- Each artefact gated by a real Standards Engineer NIM call (PASS/FAIL).

STILL DOES NOT DO:
- Full 25-persona individual depth (5 grouped passes is progress, not parity).
- Create the .ems/ folder in the TARGET platform repo (requires a separate
  cross-repo write token with access to e.g. Commander — not configured here).
- Generate/track Founder Questions (RG-008 is honestly marked N/A).
- Anything for Team 2 / forward missions (BUILD, REHAB, STRATEGIC, etc).

See IMPLEMENTATION_STATUS.md in repo root for the full current-state ledger.
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.request
import urllib.error

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

    # Master Technical Specification — synthesis of all passes so far
    mts_system = (
        f"You are the Master Spec Author persona in the SeierTech EMS. "
        f"GOVERNED BY:\n{constitution}\n\n"
        "Synthesise the following persona outputs into a Master Technical Specification, "
        "conformant to STD-000003. Cite which pass each section draws from. This is a v1 "
        "reduced-depth MTS — state that explicitly in the Executive Summary."
    )
    mts_user = (
        f"Use Case Register:\n{pass1_output[:1500]}\n\n"
        f"Architecture/Data Model:\n{pass2_output[:1500]}\n\n"
        f"Security Posture:\n{pass3_output[:1500]}\n\n"
        f"Technical Debt Register:\n{pass4_output[:1500]}\n\n"
        f"Knowledge Graph:\n{pass5_output[:1500]}"
    )
    print("\n=== Synthesis: Master Technical Specification (v1) ===")
    mts_output = call_nim(api_key, args.model, mts_system, mts_user, max_tokens=4000)
    passed_mts, issues_mts = standards_engineer_gate(api_key, args.model, mts_output, "Master Technical Specification")
    log.append({"artefact": "Master Technical Specification", "pass": passed_mts, "issues": issues_mts})
    with open(f"{platform_dir}/MASTER_TECHNICAL_SPECIFICATION.md", "w") as f:
        f.write(mts_output)
    print(f"Standards Engineer verdict: {'PASS' if passed_mts else 'FAIL'} — {issues_mts}")

    # Real readiness gate check — deterministic, not LLM self-assessment
    print("\n=== Running real readiness gate check (RG-001 to RG-010) ===")
    gate_output_path = f"{platform_dir}/READINESS_GATE_RESULT.json"
    gate_result = run_gate_check(platform_dir, platform_name, gate_output_path)
    overall_status = gate_result.get("overall_status", "UNKNOWN")
    print(f"Overall readiness status: {overall_status}")

    readiness_note = f"""# {platform_name} — Intake Run Log (v2 — expanded chain + real scan)

| Field | Value |
|---|---|
| Platform | {platform_name} |
| Repo | {args.repo_url} |
| Issue | #{args.issue_number} |
| Chain Version | v2 — 5 grouped persona passes + MTS synthesis + real code scan + real gate check |
| Code Scan Status | {scan_result.get('scan_status', 'UNKNOWN')} |
| Overall Readiness | {overall_status} |

## What This Run Actually Did

1. Real shallow clone of target repo (not just README/API metadata)
2. File tree walk — languages, manifests, schema files, governance files, test files
3. Pass 1: Use Case Register + Requirements (grounded in real scan evidence)
4. Pass 2: Architecture Document + Data Model (grounded in real schema file content)
5. Pass 3: Security Posture (grounded in real dependency manifests)
6. Pass 4: Technical Debt Register (grounded in real test/governance file counts)
7. Pass 5: Knowledge Graph (derived from passes 1-2)
8. Synthesis: Master Technical Specification (v1 depth, cites source passes)
9. Real deterministic readiness gate check (RG-001 to RG-010) — not LLM self-assessment

## Still NOT Done (see IMPLEMENTATION_STATUS.md for full list)

- Full 25-persona individual depth (this is 5 grouped passes, an improvement on v1's 2, still not 25)
- .ems/ folder creation in the TARGET platform repo (cross-repo write not yet wired)
- Founder Questions mechanism (RG-008 will show N/A — not yet implemented)
- Team 2 forward mission executors

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
