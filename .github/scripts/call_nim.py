#!/usr/bin/env python3
"""
EMS NIM Call Wrapper

Properly handles JSON construction for NVIDIA NIM API calls.
Avoids shell/JSON quoting failures by building the payload in Python
rather than interpolating markdown content into shell-quoted JSON strings.

Usage:
  python3 call_nim.py --system-files FILE1,FILE2,... --user-text "..." --max-tokens 4000 --model nvidia/nemotron-3-super
  python3 call_nim.py --system-text "..." --user-text "..." --output-file result.txt
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error


def read_files(file_list_str):
    """Read and concatenate multiple files, each clearly delimited."""
    if not file_list_str:
        return ""
    parts = []
    for path in file_list_str.split(","):
        path = path.strip()
        if not path:
            continue
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            parts.append(f"=== {path} ===\n{content}")
        except FileNotFoundError:
            parts.append(f"=== {path} ===\n[FILE NOT FOUND]")
    return "\n\n".join(parts)


def call_nim(api_key, model, system_content, user_content, max_tokens):
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
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            body = resp.read().decode("utf-8")
            result = json.loads(body)
            return result["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        print(f"NIM API HTTP error {e.code}: {err_body}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"NIM API call failed: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key-env", default="NIM_API_KEY", help="Env var name holding the API key")
    parser.add_argument("--model", default="nvidia/nemotron-3-super")
    parser.add_argument("--max-tokens", type=int, default=4000)
    parser.add_argument("--system-files", default="", help="Comma-separated file paths to inject as system context")
    parser.add_argument("--system-text", default="", help="Additional raw system text")
    parser.add_argument("--user-text", required=True, help="The user instruction")
    parser.add_argument("--output-file", required=True, help="Where to write the raw model output")

    args = parser.parse_args()

    api_key = os.environ.get(args.api_key_env)
    if not api_key:
        print(f"Missing API key in env var {args.api_key_env}", file=sys.stderr)
        sys.exit(1)

    file_content = read_files(args.system_files)
    system_content = (args.system_text + "\n\n" + file_content).strip()

    if not system_content:
        system_content = "You are an EMS reasoning agent operating under SeierTech doctrine."

    result = call_nim(api_key, args.model, system_content, args.user_text, args.max_tokens)

    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"NIM response written to {args.output_file} ({len(result)} chars)")


if __name__ == "__main__":
    main()
