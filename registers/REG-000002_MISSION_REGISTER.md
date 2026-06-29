# REG-000002 — MISSION REGISTER

| Field | Value |
|---|---|
| Artefact ID | REG-000002 |
| Artefact Class | Register |
| Title | Mission Register |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | OPERATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

The authoritative index of all missions issued within the EMS. Every mission from intake to strategic intelligence is recorded here from the moment a GitHub Issue is created.

---

## 2. Owner

SeierTech Engineering Organisation — Operations Lead Persona

---

## 3. Update Trigger

- GitHub Issue created (mission enters ISSUED)
- Chain activated (mission enters IN_PROGRESS)
- EDP produced (mission enters EDP_READY)
- Verification complete (mission enters VERIFIED)
- Scorecard approved (mission enters RELEASE_READY)
- Merged and baselined (mission enters COMPLETE)

---

## 4. Schema

| Field | Type | Description |
|---|---|---|
| Mission ID | Reference | MSN-NNNNNN |
| GitHub Issue | Integer | Issue number |
| Mission Type | Enum | INTAKE / BUILD / STRATEGIC / REHAB / AGENTIC_INSERTION / SPEC / PROPOSAL |
| Title | String | Mission title |
| Platform | Reference | PLT-NNNNNN |
| Status | Enum | ISSUED / IN_PROGRESS / EDP_READY / VERIFIED / RELEASE_READY / COMPLETE / CANCELLED |
| Issued By | String | Founder / Claude / GPT / Copilot |
| Issued Date | Date | ISO 8601 |
| EDP Ref | Reference | EDP-NNNNNN |
| Verification Ref | Reference | VER-NNNNNN |
| Scorecard Ref | Reference | SCR-NNNNNN |
| Completed Date | Date | ISO 8601 |
| Notes | String | Free text |

---

## 5. Mission Types

| Type | Description |
|---|---|
| INTAKE | MISSION-001 — Platform onboarding |
| BUILD | Standard build mission |
| STRATEGIC | Intelligence mission — where to add agentic capability etc |
| REHAB | Codebase rehabilitation — unfuck mission |
| AGENTIC_INSERTION | Add agentic capability to identified location |
| PROPOSAL | Generate build proposal from SDK or requirement |
| SPEC | Generate technical specification from approved proposal |

---

## 6. Lifecycle

```
ISSUED → IN_PROGRESS → EDP_READY → VERIFIED → RELEASE_READY → COMPLETE
                                                              → CANCELLED
```

---

## 7. Entries

| Mission ID | Issue # | Type | Platform | Status | Issued Date |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

*No missions issued yet.*

---

## 8. Relationships

| Relationship | Artefact ID | Artefact Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Updated By | All missions | — |
| Required By | REG-000001 | Readiness Register |
| Produces | Mission audit trail | — |

---

## 9. Quality Rules

- Every GitHub Issue that represents a mission must have a corresponding Mission Register entry
- No mission may enter IN_PROGRESS without a READY platform in REG-000001
- No mission may enter COMPLETE without a closed Verification Report and Scorecard

---

## 10. Review Cycle

Continuous — updated on every mission state change.

---

## 11. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1 Sprint 1.3 | SeierTech EMS |
