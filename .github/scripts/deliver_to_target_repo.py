#!/usr/bin/env python3
"""
EMS Cross-Repo Delivery — v1

Solves the two fundamentals identified as the highest-leverage remaining
gap: (1) the thing that actually changes code, (2) cross-repo write
capability. These are really one capability split in half — without
write access to the target repo, there is nothing for (1) to act on.

HONEST SCOPE — READ BEFORE ASSUMING THIS WRITES CODE:

The Engineering Delivery Package produced by run_build_chain.py today is
markdown describing intended changes (build instructions, standards
applied, test assertions) — it is NOT a diff or a set of file contents.
There is therefore no patch for this script to apply. Pretending
otherwise would overclaim a capability that doesn't exist yet.

What this script actually does:
1. Clones the TARGET platform repo (not the EMS repo) using a separate,
   target-repo-scoped token — the default GITHUB_TOKEN GitHub Actions
   provides is scoped only to the EMS repo and cannot write elsewhere;
   this is a platform limit, not a doctrine choice
2. Creates a branch: mission/MSN-{issue_number}
3. Commits the EDP itself into that branch, at a fixed, predictable path
   (.ems/missions/MSN-{issue_number}_EDP.md) so a human or a future
   builder agent (Kiro) can find and act on it
4. Opens a real Pull Request against the target repo's default branch,
   with the EDP and TDA rationale in the PR body

What this is: the first time anything in this EMS reaches across the
repo boundary and produces a visible, real artefact in the actual
target platform. That is a genuine capability gain, not nothing.

What this is NOT: autonomous code generation. No file in the target
repo's actual source tree is modified. The PR contains the proposal,
not the implementation. Closing THAT gap — Kiro or a builder agent
reading the committed EDP and writing real code against it — is the
next increment after this one, not part of this script.

REQUIRES (not yet available — this is the one piece a human must
provide, same as NIM_API_KEY): a secret named TARGET_REPO_TOKEN, a
fine-grained GitHub PAT scoped to the specific target platform repo with
contents:write and pull-requests:write. Without it this script fails
cleanly with a clear message, same pattern as the NIM_API_KEY check in
every other script in this directory.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request


def read_file_safe(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[NOT FOUND: {path}]"


def get_target_repo_url(platform_dir):
    """
    The target repo URL is not currently stored anywhere structured for
    a BUILD mission — intake/genesis know it at the time they run, but
    nothing persists it for later forward missions to read. Design
    decision: write it once, during intake/genesis, to a small marker
    file, and have this script (and any future forward-mission script)
    read it from there rather than requiring it to be re-supplied on
    every BUILD mission issue. This is new — no prior doctrine specified
    where this should live, so PLATFORM_REPO_URL.txt is introduced here,
    one line, nothing else, easy to inspect or correct by hand.
    """
    marker_path = os.path.join(platform_dir, "PLATFORM_REPO_URL.txt")
    if os.path.exists(marker_path):
        with open(marker_path, "r") as f:
            url = f.read().strip()
            if url:
                return url
    return None


def clone_target_repo(repo_url, token, dest):
    auth_url = repo_url
    if token and repo_url.startswith("https://github.com/"):
        auth_url = repo_url.replace("https://github.com/", f"https://x-access-token:{token}@github.com/")
    cmd = ["git", "clone", "--depth", "1", auth_url, dest]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        safe_err = result.stderr.replace(token or "___NOTOKEN___", "***")
        return False, safe_err
    return True, ""


def github_api_call(method, url, token, payload=None):
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    data = json.dumps(payload).encode("utf-8") if payload else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"GitHub API error {e.code} on {method} {url}: {body}", file=sys.stderr)
        return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform-name", required=True)
    parser.add_argument("--issue-number", required=True)
    args = parser.parse_args()

    target_token = os.environ.get("TARGET_REPO_TOKEN")
    if not target_token:
        print("TARGET_REPO_TOKEN not set. Cross-repo delivery requires a separate "
              "fine-grained PAT scoped to the target platform repo — the EMS repo's "
              "own GITHUB_TOKEN cannot write to other repositories. See "
              "COMMANDER_ONBOARDING_CHECKLIST.md.", file=sys.stderr)
        sys.exit(1)

    platform_name = args.platform_name.strip().upper().replace("-", "_").replace(" ", "_")
    platform_dir = f"platforms/{platform_name}"

    edp_path = f"{platform_dir}/_BUILD_EDP_LATEST.md"
    tda_path = f"{platform_dir}/_BUILD_TDA_LATEST.md"

    if not os.path.exists(edp_path):
        print(f"No EDP found at {edp_path}. Cross-repo delivery requires a completed "
              f"BUILD chain run (run_build_chain.py) with an APPROVED TDA verdict "
              f"before there is anything to deliver.", file=sys.stderr)
        sys.exit(1)

    edp_content = read_file_safe(edp_path)
    tda_content = read_file_safe(tda_path)

    repo_url = get_target_repo_url(platform_dir)
    if not repo_url:
        print(f"No target repo URL found for {platform_name} "
              f"({platform_dir}/PLATFORM_REPO_URL.txt missing or empty). "
              f"This should have been written during intake/genesis.", file=sys.stderr)
        sys.exit(1)

    branch_name = f"mission/MSN-{args.issue_number}"

    with tempfile.TemporaryDirectory() as tmpdir:
        clone_path = os.path.join(tmpdir, "target")
        print(f"Cloning target repo {repo_url}...")
        ok, err = clone_target_repo(repo_url, target_token, clone_path)
        if not ok:
            print(f"Clone failed: {err}", file=sys.stderr)
            sys.exit(1)

        subprocess.run(["git", "config", "user.name", "SeierTech EMS"], cwd=clone_path)
        subprocess.run(["git", "config", "user.email", "ems@seiertech.com"], cwd=clone_path)
        subprocess.run(["git", "checkout", "-b", branch_name], cwd=clone_path, check=True)

        missions_dir = os.path.join(clone_path, ".ems", "missions")
        os.makedirs(missions_dir, exist_ok=True)
        edp_dest = os.path.join(missions_dir, f"MSN-{args.issue_number}_EDP.md")
        with open(edp_dest, "w") as f:
            f.write(f"# Engineering Delivery Package — Mission MSN-{args.issue_number}\n\n"
                     f"Produced by the SeierTech EMS BUILD chain (run_build_chain.py v1).\n\n"
                     f"**This is a proposal, not an applied code change.** No source file in "
                     f"this repository has been modified by this commit. A human or future "
                     f"builder agent should read this EDP and implement it.\n\n---\n\n{edp_content}\n\n"
                     f"---\n\n## TDA Verdict\n\n{tda_content}\n")

        subprocess.run(["git", "add", "."], cwd=clone_path, check=True)
        commit_result = subprocess.run(
            ["git", "commit", "-m", f"EMS: BUILD proposal for mission MSN-{args.issue_number} (Issue #{args.issue_number})"],
            cwd=clone_path, capture_output=True, text=True,
        )
        if commit_result.returncode != 0:
            print(f"Nothing to commit or commit failed: {commit_result.stderr}", file=sys.stderr)
            sys.exit(1)

        push_url = repo_url.replace("https://github.com/", f"https://x-access-token:{target_token}@github.com/")
        push_result = subprocess.run(
            ["git", "push", push_url, branch_name],
            cwd=clone_path, capture_output=True, text=True,
        )
        if push_result.returncode != 0:
            safe_err = push_result.stderr.replace(target_token, "***")
            print(f"Push failed: {safe_err}", file=sys.stderr)
            sys.exit(1)

    print(f"Branch {branch_name} pushed to {repo_url}")

    m = re.search(r"github\.com/([^/]+)/([^/]+?)(?:\.git)?/?$", repo_url)
    if not m:
        print(f"Could not parse owner/repo from {repo_url} — branch pushed but no PR opened.", file=sys.stderr)
        sys.exit(0)
    owner, repo = m.group(1), m.group(2)

    pr_body = (
        f"**Automated proposal from SeierTech EMS — BUILD chain v1**\n\n"
        f"This PR was opened by `run_build_chain.py` followed by `deliver_to_target_repo.py` "
        f"(v1 cross-repo delivery). It contains an Engineering Delivery Package — a structured "
        f"proposal, not an applied code change. See `.ems/missions/MSN-{args.issue_number}_EDP.md` "
        f"for the full EDP and TDA rationale.\n\n"
        f"**This PR does not modify any source file in this repository.** A human or future "
        f"builder agent should review the EDP and implement it as a follow-up change.\n\n"
        f"Originating EMS Issue: #{args.issue_number}"
    )
    pr_result = github_api_call(
        "POST",
        f"https://api.github.com/repos/{owner}/{repo}/pulls",
        target_token,
        payload={
            "title": f"EMS Proposal: Mission MSN-{args.issue_number}",
            "head": branch_name,
            "base": "main",
            "body": pr_body,
        },
    )

    if pr_result and "html_url" in pr_result:
        print(f"Pull Request opened: {pr_result['html_url']}")
        with open(f"{platform_dir}/_BUILD_DELIVERY_LATEST.md", "w") as f:
            f.write(f"# Delivery Record — Mission MSN-{args.issue_number}\n\n"
                     f"Target repo: {repo_url}\nBranch: {branch_name}\nPR: {pr_result['html_url']}\n")
    else:
        print("Branch pushed but PR creation failed or returned no URL — check GitHub API "
              "response above.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
