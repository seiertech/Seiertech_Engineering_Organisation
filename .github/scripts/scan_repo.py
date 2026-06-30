#!/usr/bin/env python3
"""
EMS Repo Scanner — real shallow clone + file walk, not just README/metadata.

Clones the target repo shallow (depth=1), walks the file tree, and extracts:
- Full directory structure (respecting common ignore patterns)
- Language/framework signals from package manifests
- Schema/migration file contents (the actual source of truth for Data Model)
- API route definitions (best-effort pattern matching across common frameworks)
- Existing governance files (MEMORY.md, ERRORS.md, *.md doctrine-like files)
- Test file inventory

Output is a single structured JSON written to disk, consumed by the
intake chain orchestrator and injected into NIM calls as real evidence
instead of low-confidence inference from a README alone.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile

IGNORE_DIRS = {
    ".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build",
    ".next", ".nuxt", "coverage", ".pytest_cache", "vendor", ".turbo",
}

MANIFEST_FILES = {
    "package.json": "node",
    "requirements.txt": "python",
    "pyproject.toml": "python",
    "Pipfile": "python",
    "go.mod": "go",
    "Cargo.toml": "rust",
    "pom.xml": "java",
    "build.gradle": "java/kotlin",
    "Gemfile": "ruby",
    "composer.json": "php",
}

SCHEMA_PATTERNS = [
    re.compile(r"schema\.prisma$", re.IGNORECASE),
    re.compile(r"models?\.py$", re.IGNORECASE),
    re.compile(r"\.sql$", re.IGNORECASE),
    re.compile(r"migrations?[\\/]", re.IGNORECASE),
    re.compile(r"entity\.(ts|js)$", re.IGNORECASE),
]

GOVERNANCE_PATTERNS = [
    re.compile(r"^MEMORY\.md$", re.IGNORECASE),
    re.compile(r"^ERRORS?\.md$", re.IGNORECASE),
    re.compile(r"^RULES\.md$", re.IGNORECASE),
    re.compile(r"^CLAUDE\.md$", re.IGNORECASE),
    re.compile(r"^\.cursorrules$", re.IGNORECASE),
    re.compile(r"^\.kiro[\\/]", re.IGNORECASE),
    re.compile(r"DOCTRINE", re.IGNORECASE),
    re.compile(r"CONFORMANCE", re.IGNORECASE),
]

TEST_PATTERNS = [
    re.compile(r"(test|spec)s?[\\/]", re.IGNORECASE),
    re.compile(r"\.(test|spec)\.(js|ts|py|jsx|tsx)$", re.IGNORECASE),
    re.compile(r"^test_.*\.py$", re.IGNORECASE),
]

ROUTE_HINT_PATTERNS = [
    re.compile(r"@(app|router)\.(get|post|put|delete|patch)\(", re.IGNORECASE),  # FastAPI/Flask
    re.compile(r"router\.(get|post|put|delete|patch)\(", re.IGNORECASE),  # Express
    re.compile(r"@(Get|Post|Put|Delete|Patch)Mapping", re.IGNORECASE),  # Spring
]

MAX_FILE_READ_BYTES = 50_000
MAX_FILES_TO_READ_CONTENT = 40


def clone_shallow(repo_url, token, dest):
    auth_url = repo_url
    if token and repo_url.startswith("https://github.com/"):
        auth_url = repo_url.replace("https://github.com/", f"https://x-access-token:{token}@github.com/")
    cmd = ["git", "clone", "--depth", "1", auth_url, dest]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        # Redact token from any error output before surfacing
        safe_err = result.stderr.replace(token or "___NOTOKEN___", "***")
        return False, safe_err
    return True, ""


def should_ignore_dir(dirname):
    return dirname in IGNORE_DIRS or dirname.startswith(".")


def walk_repo(root):
    structure = []
    manifests = {}
    schema_files = []
    governance_files = []
    test_files = []
    route_hits = []
    languages = set()

    files_read = 0

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not should_ignore_dir(d)]
        rel_dir = os.path.relpath(dirpath, root)

        for fname in filenames:
            rel_path = os.path.normpath(os.path.join(rel_dir, fname)) if rel_dir != "." else fname
            structure.append(rel_path)

            if fname in MANIFEST_FILES:
                languages.add(MANIFEST_FILES[fname])
                full_path = os.path.join(dirpath, fname)
                try:
                    with open(full_path, "r", encoding="utf-8", errors="replace") as f:
                        manifests[rel_path] = f.read()[:MAX_FILE_READ_BYTES]
                except Exception:
                    pass

            if any(p.search(rel_path) for p in SCHEMA_PATTERNS):
                schema_files.append(rel_path)

            if any(p.search(fname) or p.search(rel_path) for p in GOVERNANCE_PATTERNS):
                governance_files.append(rel_path)

            if any(p.search(rel_path) for p in TEST_PATTERNS):
                test_files.append(rel_path)

    # Second pass: read content of schema files (bounded) for real evidence
    schema_content = {}
    for rel_path in schema_files[:MAX_FILES_TO_READ_CONTENT]:
        full_path = os.path.join(root, rel_path)
        try:
            with open(full_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
                schema_content[rel_path] = content[:MAX_FILE_READ_BYTES]
                if any(p.search(content) for p in ROUTE_HINT_PATTERNS):
                    route_hits.append(rel_path)
        except Exception:
            pass

    # Also scan likely route files even outside schema pattern matches (bounded effort)
    route_candidates = [
        f for f in structure
        if re.search(r"(route|controller|api|views?)", f, re.IGNORECASE)
        and f.endswith((".py", ".js", ".ts", ".java"))
    ][:MAX_FILES_TO_READ_CONTENT]

    for rel_path in route_candidates:
        if rel_path in schema_content:
            continue
        full_path = os.path.join(root, rel_path)
        try:
            with open(full_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
                if any(p.search(content) for p in ROUTE_HINT_PATTERNS):
                    route_hits.append(rel_path)
        except Exception:
            pass

    governance_content = {}
    for rel_path in governance_files[:MAX_FILES_TO_READ_CONTENT]:
        full_path = os.path.join(root, rel_path)
        try:
            with open(full_path, "r", encoding="utf-8", errors="replace") as f:
                governance_content[rel_path] = f.read()[:MAX_FILE_READ_BYTES]
        except Exception:
            pass

    return {
        "total_files": len(structure),
        "languages_detected": sorted(languages),
        "manifests": manifests,
        "schema_files": schema_files,
        "schema_content_sample": schema_content,
        "governance_files_found": governance_files,
        "governance_content_sample": governance_content,
        "test_files_count": len(test_files),
        "test_files_sample": test_files[:30],
        "route_files_with_endpoints": route_hits,
        "top_level_structure": sorted({f.split(os.sep)[0] for f in structure}),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-url", required=True)
    parser.add_argument("--output-file", required=True)
    parser.add_argument("--github-token-env", default="GITHUB_TOKEN")
    args = parser.parse_args()

    token = os.environ.get(args.github_token_env, "")

    with tempfile.TemporaryDirectory() as tmpdir:
        clone_path = os.path.join(tmpdir, "repo")
        print(f"Cloning {args.repo_url} (shallow, depth=1)...")
        ok, err = clone_shallow(args.repo_url, token, clone_path)

        if not ok:
            result = {
                "scan_status": "FAILED",
                "error": err,
                "note": "Falling back to metadata-only mode upstream. This scan produced no code evidence.",
            }
            with open(args.output_file, "w") as f:
                json.dump(result, f, indent=2)
            print(f"Clone failed: {err}", file=sys.stderr)
            # Exit 0 — caller should handle FAILED status gracefully, not crash the workflow
            sys.exit(0)

        print("Clone succeeded. Walking file tree...")
        scan_result = walk_repo(clone_path)
        scan_result["scan_status"] = "SUCCESS"

    with open(args.output_file, "w") as f:
        json.dump(scan_result, f, indent=2)

    print(f"Scan complete: {scan_result['total_files']} files, "
          f"{len(scan_result['languages_detected'])} languages, "
          f"{len(scan_result['schema_files'])} schema files, "
          f"{len(scan_result['governance_files_found'])} governance files found")


if __name__ == "__main__":
    main()
