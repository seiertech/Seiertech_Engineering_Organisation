# PLATFORM ONBOARDING CHECKLIST

| Field | Value |
|---|---|
| Document | Platform Onboarding Checklist |
| Status | ACTIVE — generic checklist, work through per platform |
| Purpose | Single place listing everything needed before MISSION-001 (brownfield) or MISSION-000 (greenfield) can be fired against a real platform |
| Last Updated | 2026-06-30 |

---

## Why This Exists

Across this build session, several prerequisites for running intake against a real platform were raised and then left unresolved across multiple messages — a repo URL was stated incorrectly at one point and not used, the NIM key setup was described but not confirmed done, and a decision was made to get the EMS itself "all sorted" before testing. This checklist consolidates every open item into one place so nothing gets lost.

**This document was originally named `COMMANDER_ONBOARDING_CHECKLIST.md`.** That was wrong from the start — every other piece of doctrine built this session was made deliberately platform-agnostic (see `PLATFORM_AGNOSTIC_AUDIT.md`, which fixed Commander leaking into core persona definitions), but this checklist was never swept along with that effort. Renamed and generalised here. Commander remains the worked example throughout, the same pattern used everywhere else in the doctrine (e.g. `STD-000004`'s naming convention table, `MSN-000000`/`MSN-000001`'s format illustrations).

**Status of every item below: NOT YET CONFIRMED for any platform as of this rewrite.** This is a checklist to work through per platform, not a record of completed steps.

---

## 1. Confirm the Real Target Repository

- [ ] **Repo URL** — the actual GitHub URL for the platform. For Commander specifically: an earlier guess in this session (`johanndewinnaar-blip/Kiro_Commander_SDR`) was flagged as wrong and was never used. Get the real one before anything else, for whichever platform you're onboarding.
- [ ] **Visibility** — is the repo public or private?
  - If **public**: the default `GITHUB_TOKEN` available to GitHub Actions in the EMS repo should be sufficient to clone it (read-only access to public repos works without extra setup).
  - If **private**: a Personal Access Token (PAT) with read access to that specific repo is needed, stored as a separate secret (e.g. `TARGET_REPO_TOKEN`) — this is a different credential from the EMS repo's own `GITHUB_TOKEN`, which only has access to the EMS repo by default.
- [ ] **Branch** — confirm which branch should be scanned (likely `main`, but confirm — the scan script defaults to whatever the repo's default branch is via shallow clone).

*(Greenfield platforms via MISSION-000 skip this section entirely — no repo exists yet. See `HOW_TO_FIRE_A_MISSION.md` for the Genesis format.)*

---

## 2. NIM API Key

This is a one-time setup, shared across every platform the EMS governs — not per-platform.

- [ ] Sign up at `build.nvidia.com` (free, no card required, confirmed earlier in this session)
- [ ] Generate an API key
- [ ] Add it to the **EMS repo's** GitHub Actions secrets (not the target platform's):
  - Go to `github.com/seiertech/Seiertech_Engineering_Organisation` → Settings → Secrets and variables → Actions → New repository secret
  - Name: `NIM_API_KEY`
  - Value: the key from build.nvidia.com
- [ ] **Not yet done as of last check in this session** — confirm this has actually been added, not just planned.

---

## 3. Cross-Repo Write Access — `TARGET_REPO_TOKEN`

This is also shared infrastructure, but the token itself must be **scoped to whichever specific platform repo** a BUILD mission is targeting — a single token cannot cover every future platform if they live in different repos/orgs; re-issue or re-scope as needed when onboarding a new platform.

**Status update (2026-06-30):** this is now built and live-wired (`deliver_to_target_repo.py`, `DAM-000006`), not just anticipated. It is **still not required for a first intake run** — intake only writes inside the EMS repo. It becomes required the first time a BUILD mission reaches a real RELEASE decision and the system attempts to deliver a proposal into the target platform.

- [ ] Generate a **fine-grained Personal Access Token** scoped specifically to the target platform repository
- [ ] Required scopes: `contents: write`, `pull-requests: write`
- [ ] Add it to the **EMS repo's** GitHub Actions secrets as `TARGET_REPO_TOKEN` (same location as `NIM_API_KEY` — Settings → Secrets and variables → Actions)
- [ ] Do **not** reuse the EMS repo's own token here — it cannot write to any other repo, that's a GitHub platform limit, and `TARGET_REPO_TOKEN` is deliberately a separate credential

**What this token enables once present:** a successful BUILD mission's RELEASE decision triggers a real branch, commit, and Pull Request against the target platform, containing the Engineering Delivery Package. **This is a committed proposal, not applied code** — no source file in the target platform is modified by this step. See `DAM-000006` for full honest scope.

**What happens if this token is missing:** the BUILD mission still completes normally — `deliver_to_target_repo.py` fails cleanly with a clear message and does not block the rest of the BUILD chain (`continue-on-error: true` in the workflow). You will simply not get a PR in the target platform until this token is added.

---

## 4. Pre-Test Sanity Check (recommended before pointing at a real platform for the first time)

Per the decision already made this session ("get the EMS all sorted before we run a test"):

- [ ] Confirm the chain has actually run end-to-end at least once in the real GitHub Actions environment — as of last check, all validation was syntax/logic checks and fixture tests, **not a live run**. There may be environment gaps (e.g. `git` CLI availability on the runner, cross-job output passing) that only surface in a real run.
- [ ] Recommended: do one dry run against a small, public, throwaway repo first (not your real target platform) to catch any environment issues without burning a real run against the actual codebase.
- [ ] At least one AI provider should have a confirmed successful live call before relying on it. NIM is lower-risk (reuses logic validated earlier). Claude and OpenAI adapters in `ems_engine/providers/` have **zero live-call confirmation** as of last check.

---

## 5. What You Do NOT Need To Gather

To avoid over-preparing — these are NOT required before a first test, for any platform:

- A populated `.ems/` folder in the target platform repo (the chain creates EMS-side artefacts only for now, see item 3)
- Founder Questions answered in advance (the mechanism for this doesn't exist yet — RG-008 will correctly show N/A, not block on it)
- Full repo documentation, README polish, etc in the target platform — the scanner works with whatever exists, including a messy/legacy state. That's the point of intake.

---

## 6. How To Actually Fire The Mission (once items 1-2 above are done)

Create a GitHub Issue in the **EMS repo** (`seiertech/Seiertech_Engineering_Organisation`), not in the target platform's own repo, with this exact format:

```
Complete intake for [PLATFORM_NAME] — repo: [the real target repo URL]
```

Real worked example, Commander as the consistent illustration used throughout this doctrine:

```
Complete intake for COMMANDER_C2 — repo: [the real Commander repo URL]
```

See `HOW_TO_FIRE_A_MISSION.md` for the full quick-reference on formats (including Genesis for greenfield and Build for forward missions), what happens next, and where to find results.

---

## Summary — What's Actually Blocking A First Test Right Now

In priority order, for whichever platform you're onboarding first:

1. **The real target repo URL and its visibility** — nothing else can proceed without this (skip if greenfield via MISSION-000)
2. **Confirm `NIM_API_KEY` is actually in GitHub secrets** — described as a step, not confirmed as done
3. *(Recommended, not blocking)* a dry run against a small public repo first

Everything else (cross-repo `TARGET_REPO_TOKEN` for delivery, RAG, the full persona executor) is downstream of a successful first test and does not need to be resolved before firing the first intake or genesis mission.

---

## Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial checklist (as `COMMANDER_ONBOARDING_CHECKLIST.md`) — consolidated scattered prerequisites from across the session into one place | SeierTech EMS |
| 2.0.0 | 2026-06-30 | Renamed and genuinely generalised — found during a direct founder challenge that this document had been left Commander-specific while every other piece of doctrine this session was made platform-agnostic. Content updated throughout: TARGET_REPO_TOKEN section now states it must be re-scoped per platform, repo-URL section clarified as skippable for greenfield, summary and mission-firing sections rewritten to use [PLATFORM_NAME] as the generic case with Commander kept only as the worked example | SeierTech EMS |
