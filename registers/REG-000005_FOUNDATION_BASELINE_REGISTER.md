# REG-000005 — FOUNDATION BASELINE REGISTER

| Field | Value |
|---|---|
| Artefact ID | REG-000005 |
| Artefact Class | Register |
| Title | Foundation Baseline Register |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Records all certified EMS baselines. A baseline is a formally tagged, audited state of the EMS repository. BASELINE-1.0 is the EMS Foundation Certification milestone.

---

## 2. Schema

| Field | Type | Description |
|---|---|---|
| Baseline ID | String | e.g. BASELINE-1.0 |
| Git Tag | String | GitHub tag reference |
| Status | Enum | PLANNED / IN_PROGRESS / CERTIFIED / SUPERSEDED |
| Certification Ref | String | EMS_FOUNDATION_CERTIFICATION.md path |
| Sprints Completed | List | List of sprint IDs included |
| Certification Date | Date | ISO 8601 |
| Certifying Persona | String | Persona that performed audit |
| Score | String | Overall conformance score |
| Notes | String | Free text |

---

## 3. Entries

| Baseline ID | Status | Git Tag | Certification Date | Score |
|---|---|---|---|---|
| BASELINE-1.0 | IN_PROGRESS | — | — | — |

---

## 4. Relationships

| Relationship | Artefact ID | Artefact Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Updated By | EMS Foundation Audit | Sprint EF-1.8 |
| Depends On | STD-000001 | EMS Foundation Conformance Standard |

---

## 5. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1 Sprint 1.3 | SeierTech EMS |
