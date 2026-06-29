# REG-000004 — DELIVERY PACKAGE REGISTER

| Field | Value |
|---|---|
| Artefact ID | REG-000004 |
| Artefact Class | Register |
| Title | Engineering Delivery Package Register |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | OPERATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Indexes all Engineering Delivery Packages produced by the mission chain. Every EDP dropped to work-products/ for builder execution is registered here.

---

## 2. Schema

| Field | Type | Description |
|---|---|---|
| EDP ID | Reference | EDP-NNNNNN |
| Mission Ref | Reference | MSN-NNNNNN |
| Proposal Ref | Reference | PRP-NNNNNN |
| Platform | Reference | PLT-NNNNNN |
| Title | String | EDP title |
| Status | Enum | PRODUCED / PICKED_UP / BUILDING / BUILT / VERIFIED / RELEASED |
| Builder | String | Kiro / Builder Agent name |
| Verification Ref | Reference | VER-NNNNNN |
| Scorecard Ref | Reference | SCR-NNNNNN |
| PR Ref | String | GitHub PR number |
| Released Date | Date | ISO 8601 |

---

## 3. Entries

| EDP ID | Mission Ref | Platform | Title | Status | Builder |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

---

## 4. Relationships

| Relationship | Artefact ID | Artefact Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Depends On | REG-000003 | Proposal Register |
| Updated By | All build missions | — |
| Required By | REG-000005 | Foundation Baseline Register |

---

## 5. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1 Sprint 1.3 | SeierTech EMS |
