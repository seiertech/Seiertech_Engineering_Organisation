# EMS DOCTRINE INVENTORY

| Field | Value |
|---|---|
| Document | EMS Doctrine Inventory |
| Status | ACTIVE — single source of truth for "what exists and where" |
| Last Updated | 2026-06-29 |
| Purpose | One index of every standard, authority, register, persona, operation, mission, and template in the repo — so nobody has to dig through folders to know what exists |

---

## How To Use This Document

Each section below lists what's **CURRENT** (the artefact you should actually read and use) separately from what's **LEGACY** (an earlier draft, superseded, kept for history but should not be referenced going forward). This split exists because a real mess was found while compiling this inventory — see the "Legacy Artefact Cleanup Needed" section at the bottom for the full list and what to do about it.

---

## Standards (STD-NNNNNN) — 6 active, 0 legacy

| ID | Title | What it governs |
|---|---|---|
| STD-000001 | EMS Foundation Conformance Standard | 10 quality gates every artefact must pass |
| STD-000002 | Engineering Artefact Metadata Standard | The metadata block every artefact must carry |
| STD-000003 | Engineering Artefact Structure Standard | The canonical structure per artefact class (13 subclasses) |
| STD-000004 | Engineering Vocabulary Standard | Single source of truth for terminology, prohibited terms |
| STD-000005 | Traceability Standard | Relationship declarations every artefact must carry |
| STD-000006 | Platform Baseline Sync Standard | The `.ems/` folder structure for governed platforms |

Clean — no legacy duplicates found in `standards/`.

---

## Authorities (AUTH-NNN) — 10 active, 0 legacy

| ID | Title | Domain |
|---|---|---|
| AUTH-001 | Engineering Constitution | Root authority — all others governed by this |
| AUTH-002 | Platform Governance Authority | Platform onboarding, readiness |
| AUTH-003 | Mission Governance Authority | Mission lifecycle, gates |
| AUTH-004 | Workforce Authority | Persona definition and governance |
| AUTH-005 | Standards Authority | Standards creation and enforcement |
| AUTH-006 | Data Governance Authority | Data models, classification |
| AUTH-007 | Security Governance Authority | Security posture, CRITICAL-finding veto |
| AUTH-008 | AI Governance Authority | NIM/provider usage, agentic insertion |
| AUTH-009 | Release Authority | Scorecard, release decisions |
| AUTH-010 | Knowledge Governance Authority | Knowledge Graph, memory, MTS currency |

Clean — no legacy duplicates found in `authorities/`.

---

## Registers — 7 active (REG-NNNNNN), 19 legacy (unprefixed)

### Active — use these

| ID | Title |
|---|---|
| REG-000001 | Readiness Register |
| REG-000002 | Mission Register |
| REG-000003 | Proposal Register |
| REG-000004 | Delivery Package Register |
| REG-000005 | Foundation Baseline Register |
| REG-000006 | Release Register |
| REG-000007 | Build Governance Register |

### Legacy — do NOT use, superseded by the above (see cleanup section)

`ANTI_PATTERN_INDEX.md`, `AUTHORITY_REGISTER.md`, `CAPABILITY_REGISTER.md`, `CHANGE_REGISTER.md`, `DEBT_REGISTER.md`, `DECISION_REGISTER.md`, `KNOWLEDGE_REGISTER.md`, `LESSON_REGISTER.md`, `MISSION_REGISTER.md`, `PATTERN_INDEX.md`, `PERSONA_REGISTER.md`, `PLATFORM_REGISTER.md`, `PROPOSAL_REGISTER.md`, `READINESS_REGISTER.md`, `RELEASE_REGISTER.md`, `REQUIREMENT_REGISTER.md`, `REVIEW_REGISTER.md`, `RISK_REGISTER.md`, `STANDARD_REGISTER.md`

All 19 are short (15-32 lines), all carry `**Status:** Draft`, none carry the proper STD-000002 metadata block. These are GPT's early scaffolding pass, before the EF-1 sprint formalised the 7 registers above. **Several of these legacy registers track concepts (Risk, Debt, Decision, Knowledge, Capability, Pattern, Anti-Pattern, Lesson, Review) that have NO corresponding REG-NNNNNN equivalent yet** — that's a real gap, not just duplication. See cleanup section.

---

## Operations (OPR-NNNNNN) — 11 active, 2 legacy

### Active — use these

| ID | Title |
|---|---|
| OPR-000001 | Mission Lifecycle Operation |
| OPR-000002 | Platform Intake Operation |
| OPR-000003 | Engineering Proposal Operation |
| OPR-000004 | Technical Design Authority Operation |
| OPR-000005 | Engineering Delivery Operation |
| OPR-000006 | Verification Operation |
| OPR-000007 | Release Operation |
| OPR-000008 | Knowledge Capture Operation |
| OPR-000009 | Baseline Operation |
| OPR-000010 | Platform Baseline Sync Operation |
| OPR-000011 | Platform Genesis Operation |

### Legacy — early placeholders, superseded

`operations/release-approval/README.md`, `operations/verification/README.md` — both are one-line placeholders ("Future contents will record review areas..."), fully superseded by OPR-000006 and OPR-000007.

---

## Missions (MSN-NNNNNN) — 2 active, 1 legacy

| ID | Title | Status |
|---|---|---|
| MSN-000000 | MISSION-000 Platform Genesis | Active |
| MSN-000001 | MISSION-001 Platform Intake | Active, v3.0 (Phase 7 added) |

**Legacy:** `missions/MISSION-001_PLATFORM_INTAKE.md` (69 lines, no proper ID prefix) — an early draft of what MSN-000001 became (276 lines, v3.0, proper metadata). Superseded.

---

## Templates (TPL-NNNNNN + HAR) — 11 active, 4 legacy

### Active — use these

| ID | Title |
|---|---|
| TPL-000001 | Platform Intake Template |
| TPL-000002 | Mission Template |
| TPL-000003 | Proposal Template |
| TPL-000004 | Engineering Delivery Package Template |
| TPL-000005 | Verification Report Template |
| TPL-000006 | Scorecard Template |
| TPL-000007 | Decision Template |
| TPL-000008 | Persona Template |
| TPL-000009 | Authority Template |
| TPL-000010 | Register Template |
| HAR-000001 | Platform Handoff Artefact Template (Team 1 → Team 2 baton) |

### Legacy — superseded

`engineering-proposal-template.md`, `mission-order-template.md`, `platform-intake-mission-template.md`, `scorecard-template.md` — early drafts, superseded by TPL-000003, TPL-000002, TPL-000001, and TPL-000006 respectively.

---

## Personas — 50 active (25 Team 1 + 25 Team 2), 0 legacy

Clean — `agents/` has no legacy duplication. Full detail in `agents/README.md`, `agents/team-1-baseline/TEAM_1_REGISTRY.md`, `agents/team-2-forward/TEAM_2_REGISTRY.md`.

| Team | Count | Purpose | Activates On |
|---|---|---|---|
| Team 1 — Baseline Establishment Force | 25 | Forensic intake, one-time per platform | MISSION-001 only |
| Team 2 — Forward Build Force | 25 | All forward missions, permanent | After handoff (or day one for genesis) |

---

## Python Engine (ems_engine/) — new, not doctrine, executable code

Not part of the markdown doctrine — this is the executable layer. See `PYTHON_ENGINE_BUILD_PLAN.md` for full status. Steps 1-3 done (package skeleton, provider abstraction, scan+gates relocation), Steps 4-5 (RAG, persona executor) paused pending founder decisions, Step 6 (wiring into the workflow) not started.

---

## Other Key Documents (root level)

| Document | Purpose |
|---|---|
| `IMPLEMENTATION_STATUS.md` | What actually executes today vs what's designed but not built — the honest ledger for the GitHub Actions chain |
| `PYTHON_ENGINE_BUILD_PLAN.md` | The ems_engine package build plan and decision record |
| `EMS_FOUNDATION_CERTIFICATION.md` | BASELINE-1.0 certification record (38 PASS, 0 FAIL) plus post-baseline additions |
| `governance/EMS_RELATIONSHIP_GRAPH.md` | The full artefact relationship graph — every node, every edge |
| `EMS_ARCHITECTURE.md` | The 8-domain EMS architecture model |
| `EMS_DOCTRINE_INVENTORY.md` | This document |

---

## Legacy Artefact Cleanup Needed

Found while compiling this inventory — **not yet actioned**, flagged here for a decision rather than silently deleted:

**26 legacy files/dirs total**, all early GPT scaffolding drafts, all marked `Draft` or clearly superseded by a properly-built, STD-000002-conformant equivalent:

- 19 unprefixed registers in `registers/`
- 4 unprefixed templates in `templates/`
- 2 unprefixed operation dirs in `operations/` (`release-approval/`, `verification/`)
- 1 unprefixed mission in `missions/`

**Two real findings buried in this, worth a decision:**

1. **Should the legacy files just be deleted, or archived to a `legacy/` folder?** Deleting loses zero functional content (everything is superseded), but Git history preserves them either way if you want to be cautious.

2. **Several legacy registers track concepts with no current REG-NNNNNN equivalent** — specifically Risk, Debt, Decision, Knowledge, Capability, Pattern/Anti-Pattern, Lesson, and Review. Some of these are partially covered elsewhere (e.g. debt is tracked per-platform in `TECHNICAL_DEBT_REGISTER.md` artefacts, decisions are meant to go in a Decision Register per several operations referencing `Platform Decision Register`) but **there is currently no REG-0000NN Decision Register, Risk Register, or Knowledge Register at the EMS level** — only the legacy drafts and scattered per-platform mentions. This is a genuine doctrine gap, not just file hygiene, and may be worth a proper Sprint EF-2 register expansion rather than just deleting the drafts.

**Recommendation:** don't delete yet. Decide first whether Risk/Decision/Knowledge registers need to be formally built as REG-0000NN artefacts (recommended — several operations already reference "Decision Register" and "Risk Register" as if they exist), then archive or delete the legacy drafts once their useful content (if any) has been carried forward.

---

## Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial inventory compiled — surfaced 26 legacy/superseded artefacts and a real gap (no formal Risk/Decision/Knowledge registers at EMS level) requiring a founder decision | SeierTech EMS |
