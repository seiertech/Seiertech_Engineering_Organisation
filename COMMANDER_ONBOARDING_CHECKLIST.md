# COMMANDER ONBOARDING CHECKLIST

| Field | Value |
|---|---|
| Document | Commander Onboarding Checklist |
| Status | ACTIVE — nothing here has been confirmed/completed yet |
| Purpose | Single place listing everything needed before MISSION-001 can be fired against Commander for real |
| Last Updated | 2026-06-29 |

---

## Why This Exists

Across this build session, several prerequisites for running intake against Commander were raised and then left unresolved across multiple messages — a repo URL was stated incorrectly at one point and not used, the NIM key setup was described but not confirmed done, and a decision was made to get the EMS itself "all sorted" before testing. This checklist consolidates every open item into one place so nothing gets lost.

**Status of every item below: NOT YET CONFIRMED.** This is a checklist to work through, not a record of completed steps.

---

## 1. Confirm the Real Commander Repository

- [ ] **Repo URL** — the actual GitHub URL for Commander SDR. An earlier guess in this session (`johanndewinnaar-blip/Kiro_Commander_SDR`) was flagged as wrong and was never used. Get the real one before anything else.
- [ ] **Visibility** — is the repo public or private?
  - If **public**: the default `GITHUB_TOKEN` available to GitHub Actions in the EMS repo should be sufficient to clone it (read-only access to public repos works without extra setup).
  - If **private**: a Personal Access Token (PAT) with read access to that specific repo is needed, stored as a separate secret (e.g. `TARGET_REPO_TOKEN`) — this is a different credential from the EMS repo's own `GITHUB_TOKEN`, which only has access to the EMS repo by default.
- [ ] **Branch** — confirm which branch should be scanned (likely `main`, but confirm — the scan script defaults to whatever the repo's default branch is via shallow clone).

---

## 2. NIM API Key

- [ ] Sign up at `build.nvidia.com` (free, no card required, confirmed earlier in this session)
- [ ] Generate an API key
- [ ] Add it to the **EMS repo's** GitHub Actions secrets (not Commander's):
  - Go to `github.com/seiertech/Seiertech_Engineering_Organisation` → Settings → Secrets and variables → Actions → New repository secret
  - Name: `NIM_API_KEY`
  - Value: the key from build.nvidia.com
- [ ] **Not yet done as of last check in this session** — confirm this has actually been added, not just planned.

---

## 3. Cross-Repo Write Access (only needed once you're past the first test run)

This is **not required for the first intake run** — the current v2 chain writes all output into the EMS repo (`platforms/COMMANDER_C2/`), not into Commander itself. It becomes required later for:

- [ ] `.ems/` folder creation **inside the Commander repo** (OPR-000010 Platform Baseline Sync) — needs a token with **write** access to Commander specifically
- [ ] Kiro-sync file delivery into Commander

Flagged here so it's not forgotten, but **do not block the first test run on this** — it's a later step.

---

## 4. Pre-Test Sanity Check (recommended before pointing at Commander for real)

Per the decision already made this session ("get the EMS all sorted before we run a test"):

- [ ] Confirm the v2 chain has actually run end-to-end at least once in the real GitHub Actions environment — as of last check, all validation was syntax/logic checks and fixture tests, **not a live run**. There may be environment gaps (e.g. `git` CLI availability on the runner, cross-job output passing) that only surface in a real run.
- [ ] Recommended: do one dry run against a small, public, throwaway repo first (not Commander) to catch any environment issues without burning a real run against the actual codebase.
- [ ] At least one AI provider should have a confirmed successful live call before relying on it. NIM is lower-risk (reuses logic validated earlier). Claude and OpenAI adapters in `ems_engine/providers/` have **zero live-call confirmation** as of last check.

---

## 5. What You Do NOT Need To Gather

To avoid over-preparing — these are NOT required before a first test:

- A populated `.ems/` folder in Commander (the chain creates EMS-side artefacts only for now, see item 3)
- Founder Questions answered in advance (the mechanism for this doesn't exist yet — RG-008 will correctly show N/A, not block on it)
- Full repo documentation, README polish, etc in Commander — the scanner works with whatever exists, including a messy/legacy state. That's the point of intake.

---

## 6. How To Actually Fire The Mission (once items 1-2 above are done)

Create a GitHub Issue in the **EMS repo** (`seiertech/Seiertech_Engineering_Organisation`), not in Commander, with this exact format:

```
Complete intake for COMMANDER_C2 — repo: [the real Commander repo URL]
```

See `HOW_TO_FIRE_A_MISSION.md` for the full quick-reference on formats, what happens next, and where to find results.

---

## Summary — What's Actually Blocking a First Test Right Now

In priority order:

1. **The real Commander repo URL and its visibility** — nothing else can proceed without this
2. **Confirm `NIM_API_KEY` is actually in GitHub secrets** — described as a step, not confirmed as done
3. *(Recommended, not blocking)* a dry run against a small public repo first

Everything else (cross-repo `.ems/` write, RAG, the full persona executor) is downstream of a successful first test and does not need to be resolved before firing the first intake mission.

---

## Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial checklist — consolidated scattered prerequisites from across the session into one place | SeierTech EMS |
