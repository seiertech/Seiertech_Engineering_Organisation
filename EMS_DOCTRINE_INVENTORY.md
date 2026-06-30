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

## Registers — 9 active (REG-NNNNNN), 0 unprefixed remaining (archived)

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
| REG-000008 | Risk Register — **new**, closes a gap that existed at the time of the original audit |
| REG-000009 | Decision Register — **new**, closes a gap that existed at the time of the original audit |

### Archived — `registers/legacy/`

All 19 originally-flagged unprefixed draft registers have been moved to `registers/legacy/` (not deleted — Git history and the files themselves are preserved, just out of the active path). Before archiving, every legacy register was checked for live doctrine references (`grep` across all authorities, operations, standards, missions, and both team persona folders). Two genuinely had live references — Risk Register and Decision Register — and were formally rebuilt as REG-000008 and REG-000009 before archiving the drafts. The remaining 17 had zero live references anywhere in active doctrine and were archived as-is.

---

## Operations (OPR-NNNNNN) — 11 active, 0 unprefixed remaining (archived)

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

### Archived — `operations/legacy/`

`release-approval/`, `verification/` — both were one-line placeholders, fully superseded by OPR-000007 and OPR-000006 respectively. Moved, not deleted.

---

## Missions (MSN-NNNNNN) — 2 active, 0 unprefixed remaining (archived)

| ID | Title | Status |
|---|---|---|
| MSN-000000 | MISSION-000 Platform Genesis | Active |
| MSN-000001 | MISSION-001 Platform Intake | Active, v3.0 (Phase 7 added) |

**Archived** to `missions/legacy/`: `MISSION-001_PLATFORM_INTAKE.md` (69 lines, no proper ID prefix) — an early draft of what MSN-000001 became (276 lines, v3.0, proper metadata). Moved, not deleted.

---

## Templates (TPL-NNNNNN + HAR) — 11 active, 0 unprefixed remaining (archived)

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

### Archived — `templates/legacy/`

`engineering-proposal-template.md`, `mission-order-template.md`, `platform-intake-mission-template.md`, `scorecard-template.md` — superseded by TPL-000003, TPL-000002, TPL-000001, and TPL-000006 respectively. Moved, not deleted.

---

## Personas — 50 active (25 Team 1 + 25 Team 2), 0 legacy

Clean — `agents/` has no legacy duplication. Full detail in `agents/README.md`, `agents/team-1-baseline/TEAM_1_REGISTRY.md`, `agents/team-2-forward/TEAM_2_REGISTRY.md`.

**Note:** PER-000016 / T2-PER-000016 was renamed from "QA and Governance Director" to "Verification and Governance Director" on 2026-06-29, resolving a confirmed STD-000004 prohibited-vocabulary violation (see `EMS_VOCABULARY_AUDIT.md`). Folder names, persona titles, and all ~21 cross-references across both teams, three authorities, the relationship graph, both missions, and four operations were updated consistently.

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

## Legacy Artefact Cleanup — RESOLVED

Originally flagged as 26 unactioned legacy files/dirs requiring a decision. **Resolved on 2026-06-29:**

**Decision made:** every legacy artefact was checked for live doctrine references before being touched — not blindly deleted, not blindly kept.

- **Risk Register and Decision Register** were found to have genuine, load-bearing live references across multiple authorities (AUTH-006, AUTH-007) and personas (Security Architect in both teams, Chief Architect in both teams, Build Governance Auditor, OPR-000004). These were formally built as **REG-000008** and **REG-000009** respectively, with full STD-000002/STD-000003 conformant structure, before any archiving happened. Every place that referenced them informally (e.g. "the Risk Register," "Platform Decision Register") was updated to cite the proper artefact ID.
- **All other 17 legacy registers, 4 legacy templates, 2 legacy operation placeholders, and 1 legacy mission file** were confirmed to have **zero** live references anywhere in active doctrine (checked via repo-wide grep, not assumed), and were moved to `legacy/` subfolders within their respective directories (`registers/legacy/`, `templates/legacy/`, `operations/legacy/`, `missions/legacy/`) — preserved via `git mv`, not deleted, so history and content remain recoverable.
- One stale reference was caught during this cleanup that the original audit missed: `MSN-000001` itself pointed at the legacy `registers/RISK_REGISTER.md` path — corrected to `REG-000008_RISK_REGISTER.md`.

**Net result:** 0 unprefixed legacy artefacts remain in any active doctrine path. 2 real gaps closed with properly built registers. 26 files archived, recoverable, out of the way.

---

## Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial inventory compiled — surfaced 26 legacy/superseded artefacts and a real gap (no formal Risk/Decision/Knowledge registers at EMS level) requiring a founder decision | SeierTech EMS |
| 1.1.0 | 2026-06-29 | QA persona rename completed (21 references fixed across both teams). Legacy cleanup resolved: REG-000008 Risk Register and REG-000009 Decision Register built to close real doctrine gaps; remaining 17 registers + 4 templates + 2 operations + 1 mission archived to legacy/ subfolders, confirmed zero live references before archiving | SeierTech EMS |
