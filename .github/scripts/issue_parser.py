#!/usr/bin/env python3
"""
EMS Mission Issue Parser

Determines mission type from a GitHub Issue without relying on an LLM call
for simple, deterministic pattern matching. Falls back to NIM only for
genuinely ambiguous free text.

This avoids burning a NIM call (and a quoting-fragile one) just to detect
"Complete intake for X — repo: Y" which is a pure regex match.
"""

import argparse
import json
import os
import re
import sys


def parse_deterministic(title, body):
    """Try simple, reliable pattern matching first."""
    text = f"{title}\n{body}"

    # INTAKE pattern: "Complete intake for [NAME] — repo: [URL]" or "intake for X repo Y"
    intake_match = re.search(
        r"intake\s+for\s+([A-Za-z0-9_\-]+).*?repo[:\s]+(\S+)",
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if intake_match:
        return {
            "mission_type": "INTAKE",
            "platform_name": intake_match.group(1).strip().upper().replace("-", "_"),
            "repo_url": normalise_repo_url(intake_match.group(2).strip()),
        }

    # GENESIS pattern: "Genesis: [NAME] — [brief]"
    genesis_match = re.search(
        r"genesis\s*:\s*([A-Za-z0-9_\-]+)\s*[—\-]\s*(.+)",
        text,
        re.IGNORECASE,
    )
    if genesis_match:
        return {
            "mission_type": "GENESIS",
            "platform_name": genesis_match.group(1).strip().upper().replace("-", "_"),
            "repo_url": "",
            "brief": genesis_match.group(2).strip(),
        }

    return None


def normalise_repo_url(raw):
    raw = raw.strip().rstrip(".,;")
    if raw.startswith("github.com/"):
        raw = "https://" + raw
    elif not raw.startswith("http"):
        raw = "https://github.com/" + raw
    return raw


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--body", default="")
    parser.add_argument("--output-file", required=True)
    args = parser.parse_args()

    result = parse_deterministic(args.title, args.body or "")

    if result is None:
        # Genuinely ambiguous — mark for NIM-assisted parsing downstream
        result = {
            "mission_type": "AMBIGUOUS",
            "platform_name": "",
            "repo_url": "",
        }

    with open(args.output_file, "w") as f:
        json.dump(result, f, indent=2)

    # Also print as GITHUB_OUTPUT compatible lines for direct use
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"mission_type={result['mission_type']}\n")
            f.write(f"platform_name={result['platform_name']}\n")
            f.write(f"repo_url={result.get('repo_url', '')}\n")
            # 'brief' is only present for GENESIS missions. Without this line
            # the workflow's genesis job has no way to receive the brief
            # text — found and fixed before the genesis job was ever wired
            # into the live workflow.
            f.write(f"brief={result.get('brief', '')}\n")

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
