# HOW TO FIRE A MISSION — QUICK REFERENCE

| Field | Value |
|---|---|
| Document | How To Fire A Mission |
| Status | ACTIVE |
| Last Updated | 2026-06-30 |
| Purpose | The exact issue formats that work, what happens after you create the issue, and where to find results |

---

## Where To Create The Issue

GitHub Issues in **`seiertech/Seiertech_Engineering_Organisation`** (the EMS repo) — not in the target platform's own repo.

---

## Format 1 — Platform Intake (Brownfield)

For an existing platform with code already written. This activates Team 1.

**Exact format that works:**
```
Complete intake for [PLATFORM_NAME] — repo: [REPO_URL]
```

**Real example:**
```
Complete intake for COMMANDER_C2 — repo: https://github.com/your-org/commander-sdr
```

**Confirmed working variations** (tested directly against the parser, not assumed):

| What you write | What it parses to |
|---|---|
| `Complete intake for COMMANDER_C2 — repo: github.com/foo/bar` | platform=COMMANDER_C2, repo=https://github.com/foo/bar |
| `intake for COMMANDER_C2 repo github.com/foo/bar` (no em-dash, no colon) | Same result — the parser is more flexible than the canonical format suggests |
| Platform name in the title, repo URL in the issue body | Also works — the parser reads title+body together |

**What does NOT work:** platform names with spaces (use underscores or hyphens — `COMMANDER_C2` not `Commander C2`). The parser only accepts `[A-Za-z0-9_-]` for the platform name.

---

## Format 2 — Platform Genesis (Greenfield)

For a brand new platform with no code yet. This activates Team 2 directly.

**Exact format that works:**
```
Genesis: [PLATFORM_NAME] — [one line brief]
```

**Real example:**
```
Genesis: COMPASS — personal growth operating system for consumer mobile
```

**Status (updated since this doc was first written):** Genesis now has a real v1 executor (`run_genesis_chain.py`, per `DAM-000005`). It runs 3 grouped DESIGN-mode persona passes (Use Case+Requirements, Architecture+Data Model, Knowledge Graph — fewer than intake's 5, since there's no repository to scan, only a brief to design from), then the same real readiness gate check used for brownfield. No actual GitHub repository is created for the new platform yet — output lands in the EMS repo's `platforms/[NAME]/` the same as intake.

---

## Format 3 — Build (Forward Mission)

For an existing platform that has already reached READY (via either intake or genesis). This activates Team 2's forward build chain — Proposal, Technical Design Authority, Engineering Delivery Package, Verification, Release.

**Exact format that works:**
```
Build for [PLATFORM_NAME] — [instruction]
```

**Real example:**
```
Build for PULSE — add a password reset endpoint
```

**Status:** v1 executor (`run_build_chain.py`, per `DAM-000005`). A Technical Design Authority verdict of REJECTED or REVISION_REQUIRED is a genuine halt — the chain stops there, not a soft warning. A RELEASE decision triggers `deliver_to_target_repo.py` (per `DAM-000006`), which opens a real branch and Pull Request in the target platform repo containing the Engineering Delivery Package. **This is a committed proposal, not applied code** — no source file in the target repo is modified by this step. Requires `TARGET_REPO_TOKEN` to actually deliver (see `PLATFORM_ONBOARDING_CHECKLIST.md`); without it, the BUILD chain still completes normally, it just doesn't produce a PR.

---

## What Happens After You Create An Issue

1. GitHub Actions workflow `ems-mission-chain.yml` triggers automatically on issue creation
2. `detect-mission` job runs the deterministic parser — usually completes in seconds
3. Depending on what was parsed:
   - **INTAKE** → `execute-intake` job: labels `mission:intake`, `status:in-progress`, `chain:v2`; real shallow clone; 5 grouped persona passes; MTS synthesis; real readiness gate check; commits artefacts; posts the actual READY/BLOCKED status with named failing gates
   - **GENESIS** → `execute-genesis` job: labels `mission:genesis`, `status:in-progress`, `chain:v1`; 3 grouped DESIGN-mode passes (no repo to scan); MTS synthesis; same real gate check; commits artefacts; posts the same kind of honest status comment
   - **BUILD** → `execute-build` job: labels `mission:build`, `status:in-progress`, `chain:v1`; confirms the platform is genuinely READY first; runs Proposal → TDA → EDP → Verification → Release; on a RELEASE decision, attempts cross-repo delivery (requires `TARGET_REPO_TOKEN`); posts the final status (RELEASE/HOLD/REJECT, or a TDA halt)
4. If the title/body is genuinely ambiguous (doesn't match any of the three patterns): a comment is posted explaining the expected formats, no chain runs

---

## Where To Find Results

All output lands in the **EMS repo**, under `platforms/[PLATFORM_NAME]/`. Exact filenames depend on mission type:

**INTAKE (brownfield):**

| File | What it is |
|---|---|
| `USE_CASE_REGISTER.md` | Pass 1 output |
| `ARCHITECTURE_DOCUMENT.md` | Pass 2 output (grounded in real schema evidence) |
| `SECURITY_POSTURE.md` | Pass 3 output |
| `TECHNICAL_DEBT_REGISTER.md` | Pass 4 output |
| `KNOWLEDGE_GRAPH.md` | Pass 5 output |
| `MASTER_TECHNICAL_SPECIFICATION.md` | Synthesis of all 5 passes |
| `SCAN_RESULT.json` | Raw real scan evidence — languages, manifests, schema files, governance files found, test counts |
| `PLATFORM_REPO_URL.txt` | Persisted target repo URL — what any later BUILD mission delivers back to |
| `READINESS_GATE_RESULT.json` | The real RG-001 to RG-010 gate check result — this is the actual READY/BLOCKED verdict |
| `INTAKE_RUN_LOG.md` | Human-readable summary, including honest scope disclosure and Standards Engineer verdict per artefact |

**GENESIS (greenfield):** same artefact set minus `SCAN_RESULT.json`/`SECURITY_POSTURE.md`/`TECHNICAL_DEBT_REGISTER.md`/`PLATFORM_REPO_URL.txt` (no repo to scan or deliver to yet), plus `GENESIS_RUN_LOG.md` instead of `INTAKE_RUN_LOG.md`.

**BUILD (forward):**

| File | What it is |
|---|---|
| `_BUILD_PROPOSAL_LATEST.md` | The Engineering Proposal |
| `_BUILD_TDA_LATEST.md` | The TDA verdict and rationale |
| `_BUILD_EDP_LATEST.md` | The Engineering Delivery Package (only produced if TDA approved) |
| `_BUILD_VERIFICATION_LATEST.md` | The Verification result and criteria checked |
| `_BUILD_SCORECARD_LATEST.md` | The Release Scorecard and decision |
| `_BUILD_DELIVERY_LATEST.md` | The target-repo branch/PR record (only if delivery succeeded) |
| `BUILD_RUN_LOG_{issue}.md` | Human-readable summary of the whole BUILD run |

**Also check:** the GitHub Issue itself — the bot comment posted after every run states the real outcome directly, you don't need to open any files to get the headline result.

---

## If Something Looks Wrong

| Symptom | Likely cause | Where to look |
|---|---|---|
| Issue gets no comment, no labels at all | Workflow didn't trigger, or `detect-mission` failed silently | GitHub Actions tab → check the workflow run logs directly |
| Comment says "could not deterministically parse" | Title/body didn't match either format — check spelling of "intake"/"Genesis:" and that a repo URL or brief is present | Re-edit the issue title/body to match the formats above exactly |
| Status comes back `BLOCKED — REDUCED SCOPE` | Expected for v2 — this is not a failure, it's the gate checker honestly reporting that RG-008 (Founder Questions) isn't implemented yet, or that other gates need attention | Read `READINESS_GATE_RESULT.json` for the specific `failing_gates` list |
| Workflow run fails entirely (red X) | Could be a real bug, or `NIM_API_KEY` missing/invalid, or the target repo clone failed (private repo, wrong URL) | Check the Actions log directly — `scan_repo.py` is designed to fail gracefully (returns `scan_status: FAILED` rather than crashing) but other failure modes are possible and not yet all handled |

---

## Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial quick-reference, formats verified by running the actual parser, not assumed from memory | SeierTech EMS |
| 2.0.0 | 2026-06-30 | Document had gone stale relative to real progress: Genesis status corrected (now has a real v1 executor, was previously "not yet built"), BUILD format added entirely (didn't exist when this doc was first written), results tables expanded to cover all three mission types, Commander-specific phrasing in the intro generalised | SeierTech EMS |
