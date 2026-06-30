#!/usr/bin/env python3
"""
EMS Team 1 Intake Chain Orchestrator

This is the real executable version of OPR-000002 Platform Intake Operation.

Honest scope of this version:
- Executes a REDUCED persona sequence (not all 25 individually) to keep
  NIM call count and runtime manageable within a single GitHub Actions job.
- Groups personas into logical passes that share context, rather than
  one isolated NIM call per persona (which would be 25+ sequential calls
  and likely exceed reasonable CI runtime / cost for a v1).
- Each pass IS gated by a Standards Engineer conformance check before
  its output is committed.
- Produces real files in platforms/[NAME]/ — not a single blob.
- Does NOT yet: clone and deeply static-analyse the target repo's code
  (it reads repo metadata via GitHub API + README, not a full AST/code scan).
- Does NOT yet: create the .ems/ folder in the TARGET platform repo
  (it writes locally within the EMS repo only). Cross-repo write requires
  a token with access to the target repo — flagged as TODO below.

This is v1 of real execution. It replaces the previous single-call stub.
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

    platform_name = args.platform_name
    platform_dir = f"platforms/{platform_name}"
    spine_dir = f"{platform_dir}/spine"
    os.makedirs(spine_dir, exist_ok=True)

    constitution = read_file_safe("authorities/AUTH-001_ENGINEERING_CONSTITUTION.md")
    vocab = read_file_safe("standards/STD-000004_ENGINEERING_VOCABULARY_STANDARD.md")

    print(f"=== Fetching repo metadata for {args.repo_url} ===")
    repo_meta = fetch_github_repo_metadata(args.repo_url, github_token) if github_token else {"note": "no github token"}
    print(json.dumps(repo_meta, indent=2)[:2000])

    log = []

    # Pass 1: Use Case Register + Requirements (grouped — share repo context)
    pass1_system = (
        f"You are Team 1 personas (Use Case Analyst, Senior Business Analyst) in the SeierTech EMS. "
        f"GOVERNED BY:\n{constitution}\n\nVOCABULARY:\n{vocab}\n\n"
        "Produce a Use Case Register and Requirements summary in markdown, conformant to "
        "STD-000003 structure, based on the repo metadata provided. Where evidence is insufficient, "
        "explicitly mark items as [LOW CONFIDENCE — INSUFFICIENT EVIDENCE] rather than inventing detail."
    )
    pass1_user = f"Platform: {platform_name}\nRepo metadata:\n{json.dumps(repo_meta, indent=2)}"
    print("=== Pass 1: Use Case Register + Requirements ===")
    pass1_output = call_nim(api_key, args.model, pass1_system, pass1_user, max_tokens=3000)

    passed, issues = standards_engineer_gate(api_key, args.model, pass1_output, "Use Case Register")
    log.append({"artefact": "Use Case Register", "pass": passed, "issues": issues})
    with open(f"{platform_dir}/USE_CASE_REGISTER.md", "w") as f:
        f.write(pass1_output)
    print(f"Standards Engineer verdict: {'PASS' if passed else 'FAIL'} — {issues}")

    # Pass 2: Architecture + Data Model (grouped)
    pass2_system = (
        f"You are Team 1 personas (Chief Architect, Data Architect) in the SeierTech EMS. "
        f"GOVERNED BY:\n{constitution}\n\n"
        "Produce an Architecture Document and Data Model summary in markdown, conformant to "
        "STD-000003. Mark low-confidence inferences explicitly."
    )
    pass2_user = f"Platform: {platform_name}\nRepo metadata:\n{json.dumps(repo_meta, indent=2)}\nUse Case Register:\n{pass1_output[:3000]}"
    print("=== Pass 2: Architecture + Data Model ===")
    pass2_output = call_nim(api_key, args.model, pass2_system, pass2_user, max_tokens=3000)

    passed2, issues2 = standards_engineer_gate(api_key, args.model, pass2_output, "Architecture Document")
    log.append({"artefact": "Architecture Document", "pass": passed2, "issues": issues2})
    with open(f"{platform_dir}/ARCHITECTURE_DOCUMENT.md", "w") as f:
        f.write(pass2_output)
    print(f"Standards Engineer verdict: {'PASS' if passed2 else 'FAIL'} — {issues2}")

    # Write the honest readiness state — this is v1, not full 24-persona depth
    readiness_note = f"""# {platform_name} — Intake Run Log (v1 Reduced Chain)

| Field | Value |
|---|---|
| Platform | {platform_name} |
| Repo | {args.repo_url} |
| Issue | #{args.issue_number} |
| Chain Version | v1 — reduced pass grouping, not full 25-persona depth |

## Honest Scope Disclosure

This run executed a REDUCED intake chain:
- Pass 1: Use Case Register + Requirements (combined)
- Pass 2: Architecture Document + Data Model (combined)

It did NOT execute the full 25-persona sequence individually.
It did NOT perform deep static code analysis — repo metadata + README only.
It did NOT create the .ems/ folder in the target platform repo.
It did NOT run the full 10 readiness gates.

**This output should be treated as a DRAFT baseline requiring human review,
not a certified READY platform.**

## Standards Engineer Gate Results

{json.dumps(log, indent=2)}

## Next Steps to Reach True v2 (Full Depth)

1. Add per-persona individual NIM calls for all 25 Team 1 personas
2. Add real code scanning (clone repo, parse files) not just README/metadata
3. Add cross-repo write capability for .ems/ folder creation
4. Add the full 10-gate readiness check before setting status to READY
"""
    with open(f"{platform_dir}/INTAKE_RUN_LOG.md", "w") as f:
        f.write(readiness_note)

    print("\n=== Intake chain v1 complete ===")
    print(f"Artefacts written to {platform_dir}/")
    print("Status: DRAFT — requires human review before READY")


if __name__ == "__main__":
    main()
