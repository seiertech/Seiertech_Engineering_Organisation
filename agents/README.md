# SEIERTECH EMS — AGENT ARMY

| Field | Value |
|---|---|
| Document | Agent Army Registry |
| Status | ACTIVE |
| Version | 3.0.0 |
| Total Personas | 50 (25 Team 1 + 25 Team 2) |
| Baseline | BASELINE-1.0 |

---

## Two Teams. One Mission. Finish Commander.

The SeierTech EMS operates two specialist teams of 25 personas each. They serve different phases of the platform lifecycle and never operate simultaneously on the same platform.

---

## Team 1 — Baseline Establishment Force

**Location:** `agents/team-1-baseline/`
**Activation:** MISSION-001 Platform Intake only
**Purpose:** Establish the baseline. Read the platform reality. Create what doesn't exist. Reconcile all governance. Deliver the MTS and the Handoff Artefact. Stand down.
**Mode:** Forensic — extract, derive, create, reconcile
**Stands down:** After Handoff Artefact signed off by Executive Director

## Team 2 — Forward Build Force

**Location:** `agents/team-2-forward/`
**Activation:** After Team 1 handoff (brownfield) or from day one (greenfield)
**Purpose:** Build the platform forward. Reason against the clean EMS baseline. Execute missions. Close loops. Never look backward.
**Mode:** Forward — design, build, execute, govern
**Never stands down:** Permanent operational force

---

## The Handoff

The moment that separates Team 1 from Team 2 is the Handoff Artefact (HAR).

```
Team 1 completes intake
         ↓
HAR produced — baseline summary, confidence levels, open items, recommended first missions
         ↓
Executive Director signs off
         ↓
Team 1 stands down
         ↓
Team 2 reads HAR + MTS
         ↓
Team 2 forward operations begin
         ↓
Team 2 operates forever
```

---

## Mission Routing

| Mission | Team | Notes |
|---|---|---|
| MISSION-001 Platform Intake | Team 1 | Team 1 only — forensic intake |
| MISSION-000 Platform Genesis | Team 2 | Team 2 only — greenfield design |
| BUILD | Team 2 | Forward build against clean baseline |
| REHAB | Team 2 | Debt reduction from Technical Debt Register |
| STRATEGIC | Team 2 | Capability direction from AI Capability Map |
| AGENTIC_INSERTION | Team 2 | Intelligence insertion from AI Capability Map |
| SPEC | Team 2 | Specification production |
| PROPOSAL | Team 2 | Proposal generation |

---

## For Commander

Commander is a brownfield platform. The sequence is:

1. Fire MISSION-001 → Team 1 activates → intake runs → baseline established
2. HAR produced → Team 1 stands down → Team 2 briefed
3. Team 2 fires forward missions until Commander is complete
4. Commander shipped

---

## Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Governed By | AUTH-004 | Workforce Authority |
| Team 1 Activates On | MSN-000001 | MISSION-001 Platform Intake |
| Team 2 Activates On | MSN-000000 + all forward missions | After handoff |
| Handoff Via | HAR-000001 | Platform Handoff Artefact Template |

---

## Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-01 | Initial persona registry | SeierTech EMS |
| 2.0.0 | 2026-06-29 | EF-1.4 full rewrite — 24 personas | SeierTech EMS |
| 3.0.0 | 2026-06-29 | Two-team restructure — Team 1 and Team 2 | SeierTech EMS |
