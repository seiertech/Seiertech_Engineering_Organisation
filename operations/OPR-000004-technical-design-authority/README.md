# OPR-000004 — TECHNICAL DESIGN AUTHORITY OPERATION

| Field | Value |
|---|---|
| Artefact ID | OPR-000004 |
| Artefact Class | Operation |
| Title | Technical Design Authority Operation |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | Chief Architect |
| Approval Authority | AUTH-003 Mission Governance Authority |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Define the TDA process — the architectural governance gate between an approved Proposal and an Engineering Delivery Package. No EDP is produced without a TDA verdict of APPROVED.

---

## 2. Trigger

Engineering Proposal status APPROVED in REG-000003.

---

## 3. Steps

| Step | Action | Persona | Gate |
|---|---|---|---|
| 1 | Chief Architect reviews Proposal against Architecture Document | Chief Architect | — |
| 2 | Assess architectural coherence — does this fit the existing architecture? | Chief Architect | — |
| 3 | Assess standards compliance — does this meet all relevant standards? | Standards Engineer | — |
| 4 | Assess security implications | Security Architect | — |
| 5 | Assess data model impact | Data Architect | — |
| 6 | Assess integration impact | Integration Engineer | — |
| 7 | Produce TDA verdict: APPROVED / REJECTED / REVISION_REQUIRED | Chief Architect | — |
| 8 | Record architectural decisions in REG-000009 Decision Register | Chief Architect | — |
| 9 | APPROVED → proceed to OPR-000005 Engineering Delivery | — | APPROVED |
| 10 | REVISION_REQUIRED → return to Proposal with specific revision requirements | Chief Architect | — |
| 11 | REJECTED → return to Mission Control Director — mission does not proceed | Chief Architect | — |

---

## 4. Gates

- TDA verdict is mandatory for all BUILD and AGENTIC_INSERTION missions
- Chief Architect has sole TDA verdict authority
- No EDP without TDA APPROVED

---

## 5. Outputs

- TDA verdict (APPROVED / REJECTED / REVISION_REQUIRED)
- Architectural decision records in REG-000009 Decision Register
- Approved design brief for EDP generation

---

## 6. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-003 | Mission Governance Authority |
| Chaired By | PER-000007 | Chief Architect |
| Follows | OPR-000003 | Engineering Proposal Operation |
| Followed By | OPR-000005 | Engineering Delivery Operation |
| Updates | REG-000009 | Decision Register |

---

## 7. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1.5 | SeierTech EMS |
