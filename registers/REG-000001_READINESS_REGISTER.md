# REG-000001 — READINESS REGISTER

| Field | Value |
|---|---|
| Artefact ID | REG-000001 |
| Artefact Class | Register |
| Title | Readiness Register |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | OPERATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Tracks the onboarding and readiness status of every platform registered in the EMS. A platform must achieve READY status in this register before any mission may be issued against it.

---

## 2. Owner

SeierTech Engineering Organisation — Platform Authority Persona

---

## 3. Update Trigger

- Platform intake mission initiated
- Intake question answered by founder
- Spine extraction completed for a persona
- Readiness gate result recorded
- Platform status changes

---

## 4. Schema

| Field | Type | Description |
|---|---|---|
| Platform ID | Reference | PLT-NNNNNN |
| Platform Name | String | e.g. COMMANDER_C2 |
| Repo URL | String | GitHub repo URL |
| Intake Mission Ref | Reference | MSN-NNNNNN |
| Intake Status | Enum | NOT_STARTED / IN_PROGRESS / QUESTIONS_PENDING / COMPLETE |
| Spine Status | Enum | NOT_STARTED / IN_PROGRESS / COMPLETE |
| Personas Completed | List | List of persona IDs with completed spine extractions |
| Readiness Gates | Table | Gate / Result / Evidence |
| Questions to Founder | Integer | Count of unresolved questions |
| Overall Status | Enum | BLOCKED / IN_PROGRESS / READY |
| Last Updated | Date | ISO 8601 |
| Notes | String | Free text |

---

## 5. Readiness Gates

A platform must pass all gates to achieve READY status:

| Gate | Description |
|---|---|
| RG-001 | Platform Record created and metadata complete |
| RG-002 | Repo scan completed |
| RG-003 | Data model extracted |
| RG-004 | Tech stack identified |
| RG-005 | Use case register populated |
| RG-006 | Knowledge graph created or confirmed absent |
| RG-007 | All persona spine extractions complete |
| RG-008 | All founder questions resolved |
| RG-009 | Platform Record reviewed by Platform Authority persona |
| RG-010 | Platform registered in Platform Register |

---

## 6. Lifecycle

```
NOT_STARTED → IN_PROGRESS → QUESTIONS_PENDING → COMPLETE (Intake)
                                                → READY (Missions Unlocked)
```

---

## 7. Entries

| Platform ID | Platform Name | Intake Status | Spine Status | Overall Status | Last Updated |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

*No platforms onboarded yet. Issue MISSION-001 against a platform to begin intake.*

---

## 8. Relationships

| Relationship | Artefact ID | Artefact Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Depends On | STD-000005 | Traceability Standard |
| Updated By | MSN-000001 | MISSION-001 Platform Intake |
| Required By | All missions | — |

---

## 9. Quality Rules

- No platform may have READY status with unresolved founder questions
- No mission may reference a platform not at READY status
- Spine Status must be COMPLETE before Overall Status can be READY

---

## 10. Review Cycle

On every platform intake completion and on any platform state change.

---

## 11. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1 Sprint 1.3 | SeierTech EMS |
