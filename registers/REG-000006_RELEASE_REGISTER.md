# REG-000006 — RELEASE REGISTER

| Field | Value |
|---|---|
| Artefact ID | REG-000006 |
| Artefact Class | Register |
| Title | Release Register |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | OPERATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Records all releases approved by Release Authority across all platforms governed by the EMS. A release is a scored, verified, approved merge of an Engineering Delivery Package into a platform's main branch.

---

## 2. Schema

| Field | Type | Description |
|---|---|---|
| Release ID | String | REL-NNNNNN |
| Platform | Reference | PLT-NNNNNN |
| Mission Ref | Reference | MSN-NNNNNN |
| EDP Ref | Reference | EDP-NNNNNN |
| Scorecard Ref | Reference | SCR-NNNNNN |
| Scorecard Score | String | Overall score |
| Release Decision | Enum | RELEASE / HOLD / REJECT |
| Release Authority | String | Persona or founder |
| PR Number | String | GitHub PR |
| Merged Date | Date | ISO 8601 |
| Knowledge Capture Ref | String | Path to knowledge capture artefact |
| Baseline Updated | String | Baseline ID if this release triggered a baseline |

---

## 3. Entries

| Release ID | Platform | Mission Ref | Decision | Merged Date |
|---|---|---|---|---|
| — | — | — | — | — |

---

## 4. Relationships

| Relationship | Artefact ID | Artefact Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Depends On | REG-000004 | Delivery Package Register |
| Updated By | Release Authority | Per release decision |
| Updates | REG-000005 | Foundation Baseline Register (on baseline trigger) |

---

## 5. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1 Sprint 1.3 | SeierTech EMS |
