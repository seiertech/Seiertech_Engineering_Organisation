# REG-000009 — DECISION REGISTER

| Field | Value |
|---|---|
| Artefact ID | REG-000009 |
| Artefact Class | Register |
| Title | Decision Register |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | OPERATIONAL |
| Owner | Chief Architect (PER-000007 / T2-PER-000007) |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Tracks every significant architectural and engineering decision made across every platform governed by the EMS — particularly during Technical Design Authority (OPR-000004), where the Chief Architect's verdicts and rationale must be preserved as a permanent, auditable record. This register was referenced as a real artefact across OPR-000004, the Build Governance Auditor (which reads it as context), and both Chief Architect persona definitions before it formally existed as a `REG-NNNNNN` artefact — this fills that gap.

---

## 2. Owner

Chief Architect persona. Both Team 1 (architectural decisions made during baseline establishment) and Team 2 (decisions made during forward TDA reviews) write to this register; Chief Architect is the consistent owner across both teams.

---

## 3. Update Trigger

- Every Technical Design Authority verdict (OPR-000004) — APPROVED, REJECTED, or REVISION_REQUIRED, with rationale
- Any architectural decision made during MISSION-001 intake (e.g. how an ambiguous existing pattern was resolved)
- Any architectural decision made during MISSION-000 genesis (e.g. why a particular architecture pattern was chosen for a new platform)
- Any decision that future missions or personas will need to understand the reasoning behind, not just the outcome

---

## 4. Schema

| Field | Type | Description |
|---|---|---|
| Decision ID | Reference | DEC-[PLATFORM]-NNNNNN |
| Platform | Reference | PLT-NNNNNN |
| Title | String | Short decision description |
| Context | String | The situation that required a decision |
| Options Considered | String | What alternatives were evaluated |
| Decision | String | What was decided |
| Rationale | String | Why this option was chosen over the alternatives |
| Consequences | String | Known trade-offs or follow-on implications |
| Decision Maker | String | Persona (usually Chief Architect) or Founder |
| Mission Ref | Reference | MSN-NNNNNN, if tied to a specific mission |
| TDA Verdict | Enum | APPROVED / REJECTED / REVISION_REQUIRED / N/A (if not a TDA decision) |
| Date | Date | ISO 8601 |
| Status | Enum | ACTIVE / SUPERSEDED |
| Superseded By | Reference | DEC-NNNNNN, if a later decision overrides this one |

---

## 5. Quality Rules

- Every TDA verdict produced by OPR-000004 SHALL be recorded here, not just communicated informally to the mission
- A decision marked SUPERSEDED must reference the decision that replaced it — no orphaned contradictions
- Rationale is mandatory, not optional — a decision without a recorded "why" is incomplete and should not be marked ACTIVE
- This register is consulted by the Build Governance Auditor (PER-000025) during intake as part of understanding existing architectural reasoning, and by the Master Spec Author when synthesising the MTS

---

## 6. Lifecycle

```
ACTIVE → SUPERSEDED (a later decision overrides this one — both remain in the register, linked)
```

Decisions are never deleted — even superseded ones remain as historical record of how the platform's architecture evolved.

---

## 7. Entries

| Decision ID | Platform | Title | TDA Verdict | Status | Date |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

*Populated during MISSION-001/MISSION-000 and ongoing forward TDA reviews. No entries yet — no platform has completed a live intake or TDA run.*

---

## 8. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Owned By | PER-000007 | Chief Architect (Team 1) |
| Owned By | T2-PER-000007 | Chief Architect (Team 2) |
| Produced By | OPR-000004 | Technical Design Authority Operation |
| Consumed By | PER-000025 | Build Governance Auditor (intake context) |
| Consumed By | PER-000024 / T2-PER-000024 | Master Spec Author (MTS synthesis) |
| Updated By | MSN-000001 | MISSION-001 Platform Intake |
| Updated By | MSN-000000 | MISSION-000 Platform Genesis |

---

## 9. Review Cycle

Continuous — updated on every TDA verdict and significant architectural decision. Reviewed during MTS updates to ensure architectural rationale stays traceable.

---

## 10. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — closes the doctrine gap identified in EMS_DOCTRINE_INVENTORY.md (Decision Register was referenced across OPR-000004, the Build Governance Auditor, and both Chief Architect personas but did not formally exist as a REG-NNNNNN artefact until now) | SeierTech EMS |
