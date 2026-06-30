# PYTHON EMS ENGINE — BUILD PLAN

| Field | Value |
|---|---|
| Document | Python EMS Engine Build Plan |
| Status | PLANNED — not yet started |
| Decided | 2026-06-29 |
| Trigger | Need for multi-model support + second platform onboarding within ~1 week |
| Supersedes scope of | The 15-deliverable enterprise architecture review brief (parked — see note below) |

---

## Why This Exists

Two things converged in the same session:

1. A full enterprise architecture review brief was provided (mission queue, persona scheduler, concurrent execution, multi-provider routing, RAG, telemetry dashboards, 15 deliverables). Assessed as correct direction but wrong size for right now — that's infrastructure for many platforms at scale, not for finishing Commander.

2. A real, near-term need surfaced: a second platform needs the EMS within about a week, and multi-model support (not NIM-only) is now a stated requirement, partly to avoid introducing n8n as a competing orchestration layer.

**Decision:** Build a right-sized Python core now. Defer the rest of the enterprise brief (queue service, telemetry, priority scheduling, retry/escalation logic) until there's real multi-platform throughput to justify it. This document is the scope for the right-sized version only.

---

## What Already Exists (built and validated same session, before this plan)

| File | Status | What it does |
|---|---|---|
| `.github/scripts/call_nim.py` | WORKING | NIM-only API wrapper, JSON built via `json.dumps()` — fixes the original quoting fault |
| `.github/scripts/issue_parser.py` | WORKING, tested | Deterministic regex mission detection (INTAKE/GENESIS/AMBIGUOUS), tested against 3 real format strings |
| `.github/scripts/scan_repo.py` | WORKING | Real shallow clone + file walk — schema files, manifests, governance files, test inventory |
| `.github/scripts/check_readiness_gates.py` | WORKING, tested | Deterministic RG-001–RG-010 checker, tested against empty AND populated fixtures — proven to discriminate pass/fail, not rubber-stamp |
| `.github/scripts/run_intake_chain.py` | WORKING (v2) | Orchestrates 5 grouped persona passes (Use Case+Requirements, Architecture+Data Model, Security Posture, Technical Debt Register, Knowledge Graph) + MTS synthesis, each gated by a real Standards Engineer call |
| Platform name isolation | WORKING | Normalises platform names, warns (not silently overwrites) on rerun against same platform |

**Known limitation of current state:** single provider (NIM only), no concurrency, no RAG, orchestration logic and persona logic tangled together in one script, not yet run end-to-end against a real repo in the actual GitHub Actions runner environment.

---

## The Build Plan — 6 Steps, In Dependency Order

### Step 1 — Package skeleton (mechanical, low risk) — ✅ DONE
```
ems_engine/
├── __init__.py
├── providers/
├── rag/          (placeholder — see Step 4 notes below)
├── scan/
├── gates/
├── personas/     (placeholder — see Step 5 notes below)
└── tests/
```
Built and validated. All modules import cleanly (`python3 -c "from ems_engine... import ..."` succeeds).

### Step 2 — Provider abstraction (real new code — the multi-model capability) — ✅ DONE
```
providers/base.py       # AIProvider ABC, ProviderResponse, ProviderError
providers/nim.py        # relocated from call_nim.py logic, same behaviour
providers/claude.py     # new — Anthropic SDK adapter
providers/openai.py     # new — OpenAI SDK adapter, STUB STATUS (see below)
providers/router.py     # selects provider per explicit arg > platform config > env var > fallback (nim)
```

**Validated (9 unit tests, all passing, in `ems_engine/tests/test_core.py`):**
- Explicit provider argument wins over all other selection methods
- Fallback default is `nim` when nothing else specified
- `EMS_DEFAULT_PROVIDER` env var respected when no explicit/platform override
- Explicit argument beats env var (correct precedence order)
- Unknown provider name raises `ProviderError` clearly — does not silently do nothing
- Unconfigured provider (no API key) raises `ProviderError` clearly — does **not** silently fall back to a different provider, which would be worse than a loud failure
- All three providers (`nim`, `claude`, `openai`) confirmed registered

**Honest caveat — NOT validated:** no live API call has been made to ANY provider through this new code yet (no API keys available in this build environment). `NIMProvider` reuses logic from `call_nim.py` which WAS validated live in earlier sessions, so it's lower-risk. `ClaudeProvider` and `OpenAIProvider` are written to the documented SDK shapes but have zero live-call confirmation — **treat as unverified until a real call succeeds.**

Per-platform provider override mechanism built: `platforms/[NAME]/PROVIDER_CONFIG.json` with a `{"provider": "claude"}` shape, read by the router if present. Not yet used anywhere — no such file exists yet for Commander or any platform.

### Step 3 — Move scan + gates logic into the package — ✅ DONE
- `ems_engine/scan/scanner.py` — relocated from `.github/scripts/scan_repo.py`. Original CLI behaviour preserved exactly (the standalone script still works unmodified); added an importable `scan_repository(repo_url, github_token)` function for the persona executor to use later.
- `ems_engine/gates/checker.py` — relocated from `.github/scripts/check_readiness_gates.py`. Core logic extracted into an importable `check_readiness(platform_dir, platform_name, reduced_scope)` function, with `main()` now calling it rather than duplicating the logic.

**Validated:** Re-ran the exact same empty-dir and populated-dir fixture tests used to validate the original CLI version against the new importable function — **identical results** (empty dir: BLOCKED, 10 failing gates; populated dir: passes RG-001/005/006/007/009, correctly still flags RG-008 as N/A). Confirms relocation was behaviour-preserving, not a silent regression. These are now permanent tests in `ems_engine/tests/test_core.py`, not one-off manual checks.

**Important: the original `.github/scripts/*.py` files were left completely untouched.** The existing GitHub Actions workflow (`ems-mission-chain.yml`) still calls them directly and is confirmed still valid (YAML parses, scripts still compile). Nothing about the live/working chain changed — the package is a parallel, additive structure, not yet wired into the workflow. That wiring is Step 6.

`requirements.txt` added at repo root — documents that NIM/scan/gates need no extra dependencies (stdlib only, though `scan` requires the `git` CLI to be on PATH), while `anthropic` and `openai` packages are needed only if those providers are actually selected.

---

## ⏸️ Stopped Here — Steps 4 and 5 Require Founder Input Before Proceeding

Steps 1-3 above were completed without supervision because they were mechanical (restructuring) or had a single well-understood correct interface (provider abstraction pattern). Steps 4 (Chroma RAG) and 5 (persona executor) both involve real architectural decisions — collection structure, chunking strategy, concurrency/dependency graph correctness — that should be confirmed before building, per the original plan. Placeholder `__init__.py` files exist in `ems_engine/rag/` and `ems_engine/personas/` explaining exactly this and what's blocked on what.



### Step 4 — Chroma RAG layer (new architecture)
```
rag/chroma_store.py     # local embedded Chroma — init, index, query. No hosted service.
rag/indexer.py          # what gets indexed
```
**What to index:**
- EMS doctrine (authorities + standards, ~16 files) — one shared collection
- Per-platform spine artefacts — one namespaced collection per platform (prevents Commander/Platform-B context bleed)
- Per-platform scan evidence — same per-platform collection
- Mission history/memory — as it accumulates

**First proof-of-concept milestone:** index the 16 doctrine files only, prove retrieval works, BEFORE wiring RAG into the persona executor. Do not couple step 4 and step 5 until retrieval is proven standalone.

**Explicitly deferred:** real-time re-indexing on every write, hosted Chroma server, RAG for trivial calls like issue parsing.

### Step 5 — Persona executor (real new architecture)
```
personas/executor.py    # given a persona config: pull RAG context, call provider, gate via Standards Engineer
personas/registry.py    # reads persona definitions from agents/team-1-baseline/ and agents/team-2-forward/
```
Replaces the hardcoded 5 passes in `run_intake_chain.py` with a generic "run this persona" function. Same 5 passes initially as a regression check, but now reusable for the remaining ~20 personas without rewriting orchestration each time.

### Step 6 — CLI entry point + GitHub Actions update
```
cli.py   # python -m ems_engine intake --platform X --repo Y
```
Workflow YAML calls this instead of the standalone scripts directly.

---

## Concurrency — Where It's Actually Safe

Not all 5 (or eventually 25) persona passes need to be sequential. Independent passes (e.g. Security Posture and Technical Debt Register don't depend on each other's output) can run concurrently via `asyncio` or a thread pool once Step 5 exists. Sequential dependency chains (e.g. Architecture → Knowledge Graph, which consumes Architecture's output) stay sequential. This is a property of the persona dependency graph, not a global "make everything parallel" decision — get this wrong and outputs become incoherent.

---

## What Stays Exactly The Same

- EMS doctrine itself (standards, authorities, personas as markdown) — untouched
- Readiness gate logic — same 10 gates, same rules, just relocated to the package
- GitHub Actions trigger model — issue → workflow → still no persistent always-on service
- Git remains the system of record — state lives as files in the repo, not a queue database

---

## What Is Explicitly Parked (from the original architecture review brief)

These are correct ideas for a later stage, not now:

- Persistent mission queue service
- Priority scheduling
- Full retry/escalation automation
- Operational telemetry dashboards
- Token/cost monitoring dashboards
- Enterprise multi-tenant deployment considerations

Revisit when running 3+ platforms or hitting genuine throughput limits — not before.

---

## Also Still Outstanding (pre-existing gaps, unrelated to this plan, see IMPLEMENTATION_STATUS.md)

- Cross-repo `.ems/` folder creation in the TARGET platform repo (needs separate write token)
- Founder Questions mechanism (RG-008)
- Full 25-persona individual depth (currently 5 grouped passes)
- Genesis (MISSION-000) executor — not built
- Team 2 forward mission executors (BUILD/REHAB/STRATEGIC/etc) — not built
- **The v2 chain has never been run end-to-end against a real repo in the actual GitHub Actions runner** — all validation so far is syntax checks + logic tests against fixtures, not a live run. Recommend a dry run against a small public repo before pointing this at Commander.

---

## Immediate Next Action On Return

**Steps 1, 2, and 3 are complete** (package skeleton, provider abstraction, scan+gates relocation) — built and validated without supervision while paused, per the agreed boundary (mechanical work + well-understood interface patterns only). See the "✅ DONE" sections above for exactly what was built and what was/wasn't validated.

**Next decision needed from founder before Step 4 starts:** confirm the RAG collection structure (per-platform namespacing — recommended in this plan — vs a single shared collection) and chunking strategy before any Chroma code is written. See `ems_engine/rag/__init__.py` for the specific open questions.

Also still outstanding from before, unrelated to the Python engine work:
- Confirm the real Commander repo URL and its visibility (public/private) before any live test run
- A live API call has never succeeded through any of the new provider adapters — first real test should confirm at least one provider end-to-end before building further on top of the abstraction
- Step 6 (wiring `ems_engine` into the GitHub Actions workflow, replacing direct calls to `.github/scripts/*.py`) has NOT been done — the original scripts are still what the live workflow runs today

---

## Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial build plan — banked at end of session for continuation | SeierTech EMS |
| 1.1.0 | 2026-06-29 | Steps 1-3 completed in background (package skeleton, provider abstraction with 9 passing unit tests, scan+gates relocation confirmed behaviour-identical to validated originals). Stopped at Step 4 boundary per agreed scope — RAG/persona executor require founder decisions before building. | SeierTech EMS |
