# REG-000003 — PROPOSAL REGISTER

| Field | Value |
|---|---|
| Artefact ID | REG-000003 |
| Artefact Class | Register |
| Title | Proposal Register |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | OPERATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Indexes all Engineering Proposals produced by the mission chain. Tracks founder decisions — approved, rejected, or deferred.

---

## 2. Schema

| Field | Type | Description |
|---|---|---|
| Proposal ID | Reference | PRP-NNNNNN |
| Mission Ref | Reference | MSN-NNNNNN |
| Platform | Reference | PLT-NNNNNN |
| Title | String | Proposal title |
| Status | Enum | DRAFT / PENDING_DECISION / APPROVED / REJECTED / DEFERRED |
| Founder Decision | Enum | APPROVED / REJECTED / DEFERRED / PENDING |
| Decision Date | Date | ISO 8601 |
| EDP Ref | Reference | EDP-NNNNNN (if approved and built) |

---

## 3. Entries

| Proposal ID | Mission Ref | Platform | Title | Status | Decision |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

---

## 4. Relationships

| Relationship | Artefact ID | Artefact Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Updated By | PROPOSAL missions | — |
| Required By | REG-000004 | Delivery Package Register |

---

## 5. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1 Sprint 1.3 | SeierTech EMS |
