# AUTH-006 — DATA GOVERNANCE AUTHORITY

| Field | Value |
|---|---|
| Artefact ID | AUTH-006 |
| Artefact Class | Authority |
| Title | Data Governance Authority |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

This authority governs all data artefacts within the SeierTech EMS — data models, schemas, data classification, data lineage, and data quality. Every platform's data layer must be formally documented and classified before missions may operate against it.

---

## 2. Scope

Applies to all data artefacts across all platforms governed by the EMS.

---

## 3. Principles

- DAT-001 — Every platform SHALL have a formal Data Model before READY status.
- DAT-002 — Every data entity SHALL be classified by sensitivity: PII / SENSITIVE / INTERNAL / PUBLIC.
- DAT-003 — Data models are derived from codebase evidence — not invented.
- DAT-004 — Data lineage SHALL be traceable from source to consumption.
- DAT-005 — The Data Architect is the authoritative owner of all data artefacts.

---

## 4. Requirements

| ID | Requirement |
|---|---|
| DAT-REQ-001 | Every platform SHALL have a Data Model created or extracted during intake |
| DAT-REQ-002 | Every data entity SHALL carry a sensitivity classification |
| DAT-REQ-003 | Data models SHALL be updated after any mission that changes the schema |
| DAT-REQ-004 | PII data SHALL be identified and flagged to Security Architect during intake |
| DAT-REQ-005 | Knowledge Graph SHALL connect to Data Model entities |
| DAT-REQ-006 | Data Model SHALL be generated from code evidence if no documentation exists |

---

## 5. Responsibilities

| Role | Responsibility |
|---|---|
| Data Architect | Own all data artefacts, produce Data Model during intake |
| Security Architect | Receive and act on PII classification flags |
| Knowledge Graph Architect | Connect Knowledge Graph to Data Model entities |

---

## 6. Governance

Data Model changes require Data Architect sign-off. PII classification disputes escalate to Security Architect then Executive Director.

---

## 7. Dependencies

- AUTH-001 Engineering Constitution
- AUTH-007 Security Governance Authority (for PII handling)

---

## 8. Produces

- Data governance framework for all platforms

---

## 9. Consumes

- AUTH-001 Engineering Constitution

---

## 10. Updates

- Platform Data Model artefacts
- Risk Register (on PII identification)

---

## 11. Related Authorities

- AUTH-001, AUTH-007 Security Governance Authority

---

## 12. Related Standards

- STD-000003 (Data Model subclass structure)
- STD-000005 (Traceability — data lineage)

---

## 13. Related Registers

- Platform Data Classification Registers

---

## 14. Related Operations

- OPR-000002 Platform Intake Operation

---

## 15. Review Cycle

Annually or on regulatory change affecting data classification.

---

## 16. Verification

Audit: every READY platform has a Data Model with all entities classified. Zero unclassified PII entities.

---

## 17. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1.2 | SeierTech EMS |
