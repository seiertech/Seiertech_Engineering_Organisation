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

### Step 1 — Package skeleton (mechanical, low risk)
```
ems_engine/
├── __init__.py
├── cli.py
├── providers/
├── rag/
├── scan/
├── gates/
└── personas/
```
Pure restructure of existing working scripts into an installable package. No new logic.

### Step 2 — Provider abstraction (real new code — the multi-model capability)
```
providers/base.py       # abstract call(system, user, max_tokens) -> str
providers/nim.py        # existing logic, moved in
providers/claude.py     # new — Anthropic API adapter
providers/openai.py     # new — stub, same interface shape
providers/router.py     # selects provider per persona/platform from config
```
This is the actual deliverable for "use different AI models." Provider selection should be config-driven (per platform or per persona), not hardcoded.

### Step 3 — Move scan + gates logic into the package
Mechanical relocation of `scan_repo.py` and `check_readiness_gates.py` logic. Already tested — no behaviour change, just placement.

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

Start at Step 1 (package skeleton) — confirmed as the next step before this session paused. Proceed in order through Step 6. Do not skip the Step 4 standalone-retrieval proof before coupling RAG into the persona executor in Step 5.

Confirm the real Commander repo URL and its visibility (public/private) before any live test run — this was flagged as unresolved (an earlier stated URL was incorrect and was not used).

---

## Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial build plan — banked at end of session for continuation | SeierTech EMS |
