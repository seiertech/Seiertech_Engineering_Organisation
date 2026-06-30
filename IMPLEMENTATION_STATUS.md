# EMS IMPLEMENTATION STATUS — HONEST DISCLOSURE

| Field | Value |
|---|---|
| Document | Implementation Status |
| Status | ACTIVE — read this before trusting any other document's claims |
| Last Updated | 2026-06-29 (v2) |
| Purpose | Correct the gap between doctrine (fully written) and execution (partially built) |

---

## Why This Document Exists

The EMS doctrine — standards, authorities, registers, personas, operations, missions — is fully written and internally consistent. It describes the target operating model.

The **executable automation** that actually runs this doctrine against a real platform is **not yet at the same depth**. This document is the single source of truth for what actually executes today versus what is designed but not yet built.

---

## v2 Update Summary

Following an audit identifying that v1 had only 2 grouped persona passes, README-only evidence, and a structurally broken NIM JSON call, the following were fixed and upgraded in the same session:

| Fix | What changed |
|---|---|
| JSON quoting fault | Rebuilt all NIM calls in Python (`json.dumps`) instead of inline shell string interpolation — eliminates the class of bug entirely, not just the symptom |
| Code evidence | Added `scan_repo.py` — real shallow clone + file walk. Reads actual schema/manifest/governance/test files, not just README |
| Persona depth | Expanded from 2 grouped passes to 5 (Use Case+Requirements, Architecture+Data Model, Security Posture, Technical Debt Register, Knowledge Graph) plus an MTS synthesis pass |
| Readiness certification | Added `check_readiness_gates.py` — a real deterministic checker against RG-001 to RG-010, tested against both empty and populated platform directories to confirm it actually discriminates pass/fail rather than rubber-stamping |
| Issue status reporting | GitHub Issue comments now reflect the REAL gate check result (READY / BLOCKED / which gates failed), not a generic templated message |

---

## v3 Update Summary — Brownfield/Greenfield Simulation Exercise

A founder request to "run a simulation for brownfield intake and one for greenfield intake and test" led to building real local fixture repos and running the actual scripts against them (not just unit tests against synthetic fixtures, and not hand-waved walkthroughs) — this surfaced three genuine bugs that would otherwise have shipped silently:

| Bug found | Where | Fix |
|---|---|---|
| Route detection regex never matched Flask's actual `@app.route()` decorator syntax — only matched FastAPI-style `@app.get()`/`@app.post()` | `scan_repo.py` (both the `.github/scripts/` and `ems_engine/scan/` copies) | Added the correct Flask pattern plus Django markers; re-ran the scan against the fixture and confirmed detection now works |
| Readiness gate checker only recognised brownfield evidence files (`SCAN_RESULT.json`, `INTAKE_RUN_LOG.md`) for RG-001/002/004/Standards-Engineer-gate — meaning **a greenfield platform could never reach READY status regardless of how complete its genesis run was** | `check_readiness_gates.py` (both copies) | Extended gate definitions to accept genesis-equivalent evidence (`GENESIS_RUN_LOG.md`, architecture doc as tech-stack evidence). Re-tested both brownfield and greenfield fixtures after the fix — both now converge on the same honest ceiling (only RG-008 blocks). Added a permanent regression test (`test_genesis_origin_platform_can_reach_same_ceiling_as_brownfield`) so this bug class cannot silently return |
| The issue parser correctly extracted the genesis `brief` field into its JSON output but never wrote it to `GITHUB_OUTPUT` — meaning even once a genesis executor existed, the workflow would have had no way to pass the brief through to it | `issue_parser.py` | Added the missing `brief=` line; tested against both a genesis title and a regression check on intake titles, plus an edge case (brief containing an `=` character) |

**Additionally built during this exercise:** `run_genesis_chain.py` — the first real executor for MISSION-000 (previously genesis issues were correctly detected but the workflow only posted an honest "not yet built" comment, with no executor at all). Same validated pattern as the intake chain: real NIM calls via `json.dumps()`-built payloads, Standards Engineer gating per artefact, the same deterministic gate checker at the end. Wired into the live workflow, replacing the prior honest-decline-only job.

**What was tested and how:**
- A realistic brownfield fixture repo was built locally (Flask + Postgres app, with deliberately-included governance drift files — `MEMORY.md`, `ERRORS.md`, `.kiro_rules.md` — mirroring exactly the kind of accumulated doctrine the EMS is designed to find and reconcile)
- `scan_repo.py` was run against it via a real `git clone` (using `file://` to avoid needing network/GitHub access for the test) — not mocked
- The orchestrator's no-API-key failure path was confirmed clean (clear message, exit code 1, no stack trace, no partial state) for both intake and genesis chains
- Simulated-but-clearly-labelled intake/genesis artefact sets were used to exercise the gate checker's full range: empty → all-fail, deliberately-incomplete → specific named failures, complete → only the known RG-008 gap blocks
- The existing 9-test unit suite was re-run after every fix to confirm no regressions; a 10th test was added specifically for the bug found

**What this exercise did NOT do:** make any live NIM API call (no key available in this environment) — so the actual *content quality* of what NIM would produce for either chain remains unverified. It tested the orchestration, evidence-gathering, and gate-checking logic around those calls, which is exactly where the three real bugs were found — none of them were about prompt quality, all three were structural/plumbing bugs that would have affected every run regardless of what NIM returned.

## What Actually Works Today (v2)

| Component | Status |
|---|---|
| Issue parsing (INTAKE / GENESIS detection) | WORKING — deterministic regex, tested against 3 real format cases |
| NIM API call mechanism | FIXED — Python `json.dumps()` construction, immune to content-based quoting failures |
| Real repo scanning | WORKING — shallow clone, file walk, schema/manifest/governance/test file detection and content extraction |
| Intake chain — v2 (5 passes + MTS) | WORKING — 5 grouped persona passes + synthesis, each gated by a real Standards Engineer NIM call |
| Readiness gate check | WORKING — deterministic, tested to correctly FAIL on empty/missing artefacts and correctly PASS on populated ones |
| Artefact commit to EMS repo | WORKING — real files in `platforms/[NAME]/`, including `SCAN_RESULT.json` and `READINESS_GATE_RESULT.json` |
| GitHub Issue status comments | WORKING — reports actual gate status and named failing gates, not generic text |

---

## What Is Designed But NOT Yet Executable (v2 remaining gaps)

| Component | Gap |
|---|---|
| Full 25-persona Team 1 sequence | 5 grouped passes now (up from 2), still not 25 individual gated steps. Next increment if more depth is wanted. |
| .ems/ folder creation in TARGET platform repo | NOT implemented. Requires a separate token with write access to the target repo (e.g. Commander) — `GITHUB_TOKEN` in this workflow only has EMS repo access by default. |
| Founder Questions mechanism (RG-008) | NOT implemented. Gate checker honestly reports this as N/A rather than silently passing it. |
| Genesis (MISSION-000) execution | v1 IMPLEMENTED (2026-06-29) — `run_genesis_chain.py`, 3 grouped DESIGN-mode persona passes + MTS synthesis + the same real gate check used for brownfield. No actual GitHub repo created yet for the new platform — writes into the EMS repo's `platforms/[NAME]/` only, same limitation as intake's `.ems/` gap. |
| Verification / Release loop (OPR-000006, OPR-000007) | NOT implemented as automation. |
| Handoff Artefact (HAR) auto-generation | NOT implemented. Template exists; nothing populates it automatically yet. |
| Build Governance Auditor archaeology as automation | The scan now DOES detect governance files (MEMORY.md, ERRORS.md, etc.) and surfaces them in `SCAN_RESULT.json`, but does not yet classify/reconcile them per PER-000025's full doctrine — that classification pass is not yet a dedicated NIM call. |
| Team 2 forward mission chains (BUILD/REHAB/STRATEGIC/etc) | NOT implemented. No GitHub Actions job exists for any Team 2 mission type yet. |
| kiro-sync/ generation | NOT implemented. |

---

## What This Means Practically (v2)

If you fire `Complete intake for COMMANDER_C2 — repo: ...` right now, you will get:

1. A real GitHub Actions run with correctly-formed NIM API calls
2. A real shallow clone and file scan of Commander — actual schema files, manifests, test counts, governance files found
3. Five real grounded artefacts: Use Case Register, Architecture Document, Security Posture, Technical Debt Register, Knowledge Graph
4. A Master Technical Specification synthesising all five
5. A real Standards Engineer PASS/FAIL verdict on each artefact
6. A real, deterministic readiness gate check — `READY` only if all 10 gates genuinely pass, otherwise `BLOCKED` with the specific failing gate IDs named
7. A GitHub Issue comment reporting that real status — not a generic "draft, please review" message

You will **still not** get `.ems/` created in the Commander repo itself, a Founder Questions exchange, or full 25-persona-deep coverage from this run. Those remain the next build increments.

---

## Recommended Next Build Increments (in priority order)

1. **Cross-repo write token** — add a `TARGET_REPO_TOKEN` secret scoped to Commander, wire it into a new `.ems/` creation step
2. **Founder Questions mechanism** — when scan evidence is insufficient for a claim, accumulate structured questions and post them as an issue comment, track resolution
3. **Expand to remaining ~20 persona passes** — same pattern as the 5 already built, incremental and additive
4. **Build Governance Auditor classification pass** — take the governance files `scan_repo.py` already finds and run the FOUND/CONFLICTING/ABSORBED/ORPHANED classification as a dedicated gated pass
5. **Build the Genesis executor** — mirror the intake pattern for MISSION-000
6. **Build one Team 2 mission executor** — start with BUILD, prove TDA → EDP → Verification → Release end to end

Each increment is additive — the v2 chain keeps working while these are built.

---

## Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial honest disclosure — created in response to founder audit identifying doctrine/execution gap | SeierTech EMS |
| 2.0.0 | 2026-06-29 | v2 fixes: real repo scanning, 5 persona passes (up from 2), deterministic readiness gate checker, accurate issue status reporting | SeierTech EMS |
| 3.0.0 | 2026-06-29 | v3 — brownfield/greenfield simulation exercise. Built real local fixture repos, ran actual scripts (not mocks) against them. Found and fixed 3 real bugs: Flask route detection regex gap, gate checker structurally unable to ever pass a greenfield platform, issue parser not passing the genesis brief through GITHUB_OUTPUT. Built and wired in run_genesis_chain.py — genesis (MISSION-000) now has a real v1 executor, was previously detection-only | SeierTech EMS |
