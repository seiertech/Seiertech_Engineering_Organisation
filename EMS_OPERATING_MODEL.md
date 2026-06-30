# EMS OPERATING MODEL

| Field | Value |
|---|---|
| Document | EMS Operating Model |
| Status | ACTIVE — authoritative, synthesises existing doctrine, introduces no new process |
| Produced By | DAM-000004, in response to external review findings (30 June 2026) |
| Last Updated | 2026-06-30 |
| Nature | A synthesis document. Every claim below cites the Operation, Authority, or Standard it is drawn from. Where this document and an underlying Operation appear to disagree, the underlying Operation is authoritative and this document has drifted — fix this document, not the Operation. |

---

## 0. Why This Document Exists

An external review of the EMS (30 June 2026) found that the repository defines how engineering artefacts are governed, but does not yet define, in one place, how autonomous engineering itself operates. The review posed five specific questions. This document exists to answer all five, built entirely from artefacts that already existed at the time it was written — no new process, mission type, or governance mechanism was invented to produce it. See `DAM-000004` for the full amendment record.

The review also found, and a prior session verdict independently confirmed, that the system's governance documentation has outpaced its executed work — see Section 6 for an honest statement of that imbalance and what follows from it.

---

## 1. How Engineering Work Enters The System

All work enters as a GitHub Issue in the EMS repository, in one of two recognised formats, deterministically parsed (`issue_parser.py`, no LLM call needed for detection):

```
Complete intake for [PLATFORM_NAME] — repo: [REPO_URL]      → MISSION-001, brownfield
Genesis: [PLATFORM_NAME] — [one line brief]                  → MISSION-000, greenfield
```

Once a platform exists and has reached READY status, further work enters the same way — a GitHub Issue, free text or structured, classified by `OPR-000001` Mission Lifecycle Operation's Mission Control Director role into one of: BUILD, REHAB, STRATEGIC, AGENTIC_INSERTION, SPEC, PROPOSAL.

No work enters through any other channel. There is deliberately no separate ticket system, no chat-based instruction path, no direct file edit that bypasses this — Git and GitHub Issues are the only entry point, per `AUTH-003` Mission Governance Authority MSN-001 ("Every mission begins with a GitHub Issue. No issue, no mission").

---

## 2. How Autonomous Work Progresses

Progression differs by origin and is governed by which team is active — this is the most structurally important distinction in the whole model, and it is the answer the review's question most directly needs. All 50 personas across both teams, and the rule that they never operate simultaneously on the same platform, are governed by `AUTH-004` Workforce Authority.

### 2.1 Brownfield (existing platform)

```
MISSION-001 issued
  → OPR-000002 Platform Intake Operation
  → Team 1 (25 baseline-establishment personas) activates
  → 19 grouped persona passes (v4 chain, expanded from v3's 10 per DAM-000011, v2's 5 per
    DAM-000010): Use Case+Requirements, Architecture+Data Model, Security Posture, Technical
    Debt Register, Knowledge Graph, Data Model, API Register, Requirements Register, AI
    Capability Map, Test Strategy, Integration Map, Enterprise Architecture Context, Frontend
    Engineering Assessment, Backend Engineering Assessment, UX Assessment, Domain Vocabulary,
    Documentation Assessment, Proposition Document, Deployment Architecture
  → Each pass gated by a real Standards Engineer NIM call (PASS/FAIL, not simulated)
  → Master Technical Specification synthesised (from all 19 passes, covering all 15
    doctrine-specified MTS sections)
  → Handoff Artefact written directly by the intake chain (HANDOFF_ARTEFACT.md — a real,
    simplified instance; the full TPL-000011/HAR-000001 template shape is the doctrine target,
    not yet what the script produces verbatim)
  → OPR-000010 Platform Baseline Sync Operation (Build Governance Auditor classifies all found
    governance artefacts into REG-000007 Build Governance Register)
  → Team 1 stands down
  → Team 2 (25 forward-build personas) takes over, permanently
```

### 2.2 Greenfield (new platform)

```
MISSION-000 issued
  → OPR-000011 Platform Genesis Operation
  → Team 2 activates directly — no Team 1, no handoff, no prior codebase to read
  → 3 grouped DESIGN-mode persona passes (v1 chain): Use Case+Requirements,
    Architecture+Data Model, Knowledge Graph — fewer than brownfield's 5,
    because there is no repository to scan, only a brief to design from
  → Master Technical Specification synthesised
  → Team 2 holds the baseline from day one — it never needed a handoff
```

### 2.3 After either origin — Team 2 forward operation (the intended steady state)

```
Mission issued (BUILD / REHAB / STRATEGIC / AGENTIC_INSERTION / SPEC / PROPOSAL)
  → OPR-000003 Engineering Proposal Operation (writes REG-000003 Proposal Register)
  → OPR-000004 Technical Design Authority (Chief Architect chairs — APPROVED/REJECTED/REVISION_REQUIRED)
  → OPR-000005 Engineering Delivery Operation (Engineering Delivery Package produced, builder executes;
    writes REG-000004 Delivery Package Register)
  → OPR-000006 Verification Operation (QA & Governance Director — now Verification & Governance
    Director, per LES-000005 — chairs; real test execution against acceptance criteria, not
    self-assessment)
  → OPR-000007 Release Operation (Scorecard, RELEASE/HOLD/REJECT decision)
  → OPR-000008 Knowledge Capture Operation (memory written back, REG-000010 checked for lessons,
    OPR-000012 triggered if a doctrine amendment is warranted)
  → OPR-000009 Baseline Operation (if a baseline-worthy milestone was reached; writes
    REG-000005 Foundation Baseline Register)
```

**Honest status note, not theory:** Section 2.1 and 2.2 are executed by real scripts today (`run_intake_chain.py` v2, `run_genesis_chain.py` v1), validated in a brownfield/greenfield simulation exercise that found and fixed three real bugs. Section 2.3's BUILD path now also has a real v1 executor (`run_build_chain.py`, see `DAM-000005`) — TDA, EDP, Verification, and Release are genuinely executed and gated, not just described. REHAB, STRATEGIC, AGENTIC_INSERTION, SPEC, and PROPOSAL still have no executor. No actual Git branch or builder (Kiro) execution yet consumes a produced EDP for any mission type — the loop reaches a real Release decision but does not yet produce real code changes. This is a narrower, more precise version of the imbalance LES-000009 named; see Section 6, updated accordingly.

---

## 3. How Engineering Decisions Are Made

Decision authority is distributed by domain, not centralised in a single role, and every significant decision is recorded, not just made:

| Decision Domain | Authority | Recorded In |
|---|---|---|
| Architectural approval (TDA) | Chief Architect, `OPR-000004` | `REG-000009` Decision Register |
| Security veto (CRITICAL findings) | Security Architect, `AUTH-007` | `REG-000008` Risk Register — absolute, cannot be overridden by Release Manager or Executive Director |
| Data classification (PII/SENSITIVE/INTERNAL/PUBLIC) | Data Architect, `AUTH-006` | Data Model artefacts per platform |
| Release decision (RELEASE/HOLD/REJECT) | Release Manager, `OPR-000007`, governed by `AUTH-009` | `REG-000006` Release Register |
| Standards conformance (PASS/FAIL) | Standards Engineer, `STD-000001`, governed by `AUTH-005` | Per-artefact, logged in mission run logs |
| Constitutional alignment / final escalation | Executive Director, `AUTH-001` | — |
| Doctrine change (does a finding become permanent doctrine) | Whichever domain persona owns the affected artefact, via `OPR-000012` | `REG-000010` Lesson Register + `DAM-NNNNNN` |

No single persona has unilateral authority across domains. The Executive Director is the escalation terminus, not a router that pre-approves every decision — most decisions resolve within their domain and never reach that level.

---

## 4. How Authority Is Applied

Authority flows downward from `AUTH-001` Engineering Constitution through nine domain authorities (`AUTH-002` through `AUTH-010`), each governing one slice of the system, each able to be cited by name in any artefact or persona reasoning step. Authority is applied in two ways:

**As a gate** — e.g. `AUTH-007` Security Governance Authority's CRITICAL-finding veto is absolute and structurally enforced in `OPR-000007`'s Release decision logic, not advisory.

**As injected context** — every real NIM call in the executable chains injects the relevant authority and standard text directly into the system prompt before any reasoning happens (`AUTH-008` AI Governance Authority AI-001: "Every NIM call SHALL be doctrine-injected"). This is the mechanism by which "authority" is not just written doctrine but actually shapes what the model produces.

Per `AUTH-010` (amended this session, see `DAM-000003`), authority over doctrine itself — not just platform engineering — is now also governed: no ad hoc fix to a standard, persona, or operation is permitted regardless of size; every doctrine change goes through `OPR-000012`.

---

## 5. How Engineering Work Completes

A mission is complete when, and only when, `OPR-000008` Knowledge Capture has executed — this is unconditional (`AUTH-003` MSN-REQ-010: "Knowledge Capture SHALL execute after every mission regardless of release decision"). Completion is not the same as success: a REJECTed release still completes the mission, with the rejection and its reasoning preserved exactly as a RELEASE would be.

Concretely, "complete" means:
- `REG-000002` Mission Register status set to COMPLETE
- The originating GitHub Issue closed with a summary comment
- `memory/` updated with what was learned
- `REG-000010` checked for any lesson this mission surfaced — if one exists and is genuine, `OPR-000012` is triggered before the mission is considered fully closed, per `AUTH-010` KNW-006

A platform reaching READY status (the end of intake or genesis) is a milestone, not a completion — it is the precondition for Team 2 missions to begin, governed by the 10 readiness gates in `REG-000001`. As of this document's writing, RG-008 (Founder Questions) has no implementation for either origin and honestly blocks every platform from ever reaching a fully certified READY state — this is disclosed, not hidden, in `IMPLEMENTATION_STATUS.md`.

---

## 6. The Honest Imbalance — LES-000009, Updated 2026-06-30 (Fourth Pass)

When this section was first written, the EMS had zero closed Team 2 forward missions and no path across the repo boundary. Two amendments since have narrowed that considerably: `DAM-000005` produced the first real BUILD executor (Proposal through Release, gated, tested against a fixture up to the live-call boundary). `DAM-000006` produced cross-repo delivery — a RELEASE decision now results in a real branch and Pull Request inside the actual target platform repository, tested end to end against a local fixture using genuine `git` operations.

What remains true, stated precisely rather than left vague: the Pull Request `DAM-000006` produces contains a *proposal* — the Engineering Delivery Package committed as a markdown document — not applied code. No source file in any target repository has ever been modified by this system. The gap is no longer "nothing happens in the target repo" — something real and visible now happens. The gap is now specifically: nothing yet *reads* that committed proposal and writes working code against it. Additionally, REHAB, STRATEGIC, AGENTIC_INSERTION, SPEC, and PROPOSAL mission types still have no executor, and the Founder Questions mechanism (RG-008) is still absent system-wide.

A second, distinct dimension of the same imbalance surfaced when a direct founder question — "is the intake exhaustive enough for Team 2 to actually use" — was checked precisely rather than assumed: `DAM-000010` found 16 of 25 Team 2 personas (64%) had at least one stated input the intake chain never produced. `DAM-000010` closed 7 of the 16; `DAM-000011`, fired in direct response to "proceed with the rest," closed the remaining 9. This dimension of the imbalance is now fully closed — every Team 2 persona has a real, gated, scan-grounded source artefact for every input it was originally missing. This is the first dimension of this section's tracked imbalance to reach genuine zero, not just narrowed.

This continues to be stated plainly per Loop Engineering's own premise that a finding which doesn't change what happens next is not a finding.

**What follows from this, concretely:** two live options remain, founder's call — (a) wire an actual builder (Kiro or equivalent) to read the committed EDP from a delivered PR and produce real code changes, closing the proposal-to-applied-code gap precisely, or (b) make a real live NIM call against an actual platform to validate that the content these chains produce is good enough to be worth building against in the first place, since every test to date — including all 19 intake passes now in place — has validated orchestration logic and structural correctness, never actual content quality. Recorded as binding guidance per the same `OPR-000012` discipline as before.

---

## 7. What This Document Is Not

This is not a new Operation, Authority, or Standard, and it does not supersede any of the 12 Operations it synthesises — each remains independently authoritative for its own domain. This document does not authorise repository restructuring, retire any existing artefact, or expand EMS scope beyond what already existed when it was written. Per the external review's own immediate recommendations, none of that is justified yet, and this document does not claim otherwise.

---

## 8. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Produced By | DAM-000004 | Doctrine Amendment |
| Updated By | DAM-000005, DAM-000006 | Subsequent amendments |
| Governed By | AUTH-001 | Engineering Constitution |
| Synthesises | OPR-000001 through OPR-000012 | All current Operations |
| Cites | AUTH-001, 002, 003, 004, 005, 006, 007, 008, 009, 010 | All 10 current Authorities |
| Cites | REG-000001, 002, 003, 004, 005, 006, 007, 008, 009, 010 | All 10 current Registers |

---

## 9. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-30 | Initial creation — produced by DAM-000004 in direct response to an external review identifying the absence of this document as the primary architectural finding | SeierTech EMS |
| 1.1.0 | 2026-06-30 | Updated Section 2.3 and Section 6 following DAM-000005 — BUILD now has a real v1 executor, narrowing but not closing the imbalance; new binding guidance recorded pointing at the gap between Release decision and actual shipped code | SeierTech EMS |
| 1.2.0 | 2026-06-30 | Updated Section 6 following DAM-000006 — cross-repo delivery built, a RELEASE decision now produces a real PR in the target repo; gap re-stated precisely as proposal-to-applied-code, not "nothing happens" | SeierTech EMS |
| 1.3.0 | 2026-06-30 | DAM-000007 — corrected a false self-citation in Section 8 (claimed all 10 authorities/registers cited, actually only 6 of each); genuinely wove in the missing 4+4 at their substantively correct points in Sections 2 and 4, found during a full doctrine sweep | SeierTech EMS |
| 1.4.0 | 2026-06-30 | DAM-000010 — Section 2.1 lifecycle diagram updated to the real 10-pass v3 intake chain (was 5); Section 6 updated with the intake-depth dimension of the imbalance, found by directly checking intake output against all 25 Team 2 personas' stated inputs (64% had a gap, now ~36%); fixed a duplicate Handoff Artefact line introduced during the same edit | SeierTech EMS |
| 1.5.0 | 2026-06-30 | DAM-000011 — Section 2.1 lifecycle diagram updated to the real 19-pass v4 intake chain (was 10); Section 6 updated — the intake-depth dimension of the imbalance is now fully closed, the first tracked dimension to reach genuine zero rather than just narrowed | SeierTech EMS |
