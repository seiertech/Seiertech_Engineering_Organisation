# HOW TO FIRE A MISSION — QUICK REFERENCE

| Field | Value |
|---|---|
| Document | How To Fire A Mission |
| Status | ACTIVE |
| Last Updated | 2026-06-29 |
| Purpose | The exact issue formats that work, what happens after you create the issue, and where to find results |

---

## Where To Create The Issue

GitHub Issues in **`seiertech/Seiertech_Engineering_Organisation`** (the EMS repo) — not in the platform's own repo (e.g. not in Commander's repo).

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

For a brand new platform with no code yet. This activates Team 2 directly — **but note the honest status below.**

**Exact format that works:**
```
Genesis: [PLATFORM_NAME] — [one line brief]
```

**Real example:**
```
Genesis: COMPASS — personal growth operating system for consumer mobile
```

**⚠️ HONEST STATUS:** the issue parser correctly detects GENESIS missions, but **no executor has been built for them yet**. As of the last check, firing a Genesis issue gets you a GitHub Actions run that posts a comment explaining the chain is designed but not yet executable, and applies a `status:not-yet-implemented` label. It does not error or fail silently — it tells you honestly. Do not expect a real genesis run until this is built (see `IMPLEMENTATION_STATUS.md`).

---

## What Happens After You Create An Intake Issue

1. GitHub Actions workflow `ems-mission-chain.yml` triggers automatically on issue creation
2. `detect-mission` job runs the deterministic parser — usually completes in seconds
3. If parsed as `INTAKE`: `execute-intake` job runs
   - Labels the issue `mission:intake`, `status:in-progress`, `chain:v2`
   - Real shallow clone of the target repo
   - 5 grouped persona passes (Use Case+Requirements, Architecture+Data Model, Security Posture, Technical Debt Register, Knowledge Graph)
   - MTS synthesis pass
   - Real deterministic readiness gate check
   - Commits all artefacts to the EMS repo
   - Posts a comment on the issue with the actual READY/BLOCKED status and which gates failed (if any)
   - Updates the issue label to `status:draft-needs-review`
4. If the title/body is genuinely ambiguous (doesn't match either pattern): a comment is posted explaining the expected formats, no chain runs

---

## Where To Find Results

All output lands in the **EMS repo**, under `platforms/[PLATFORM_NAME]/`:

| File | What it is |
|---|---|
| `USE_CASE_REGISTER.md` | Pass 1 output |
| `ARCHITECTURE_DOCUMENT.md` | Pass 2 output (grounded in real schema evidence) |
| `SECURITY_POSTURE.md` | Pass 3 output |
| `TECHNICAL_DEBT_REGISTER.md` | Pass 4 output |
| `KNOWLEDGE_GRAPH.md` | Pass 5 output |
| `MASTER_TECHNICAL_SPECIFICATION.md` | Synthesis of all 5 passes |
| `SCAN_RESULT.json` | Raw real scan evidence — languages, manifests, schema files, governance files found, test counts |
| `READINESS_GATE_RESULT.json` | The real RG-001 to RG-010 gate check result — this is the actual READY/BLOCKED verdict |
| `INTAKE_RUN_LOG.md` | Human-readable summary of the whole run, including honest scope disclosure and the Standards Engineer verdict per artefact |
| `spine/SCAN_EVIDENCE_SPINE.md` | The shared scan evidence used across passes |

**Also check:** the GitHub Issue itself — the bot comment posted after the run states the real `overall_status` and lists `failing_gates` by name directly, you don't need to open any files to get the headline result.

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
