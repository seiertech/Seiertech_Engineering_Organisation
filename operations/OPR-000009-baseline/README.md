# OPR-000009 — BASELINE OPERATION

| Field | Value |
|---|---|
| Artefact ID | OPR-000009 |
| Artefact Class | Operation |
| Title | Baseline Operation |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | Executive Director |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Define the Baseline process — the formal certification of the EMS repository at a defined milestone. A baseline is a tagged, audited, certified state of the entire EMS. BASELINE-1.0 is EMS Foundation Certified. Subsequent baselines mark platform milestones and major EMS capability additions.

---

## 2. Trigger

Baseline trigger conditions met — either Sprint EF-1.8 completion (BASELINE-1.0) or defined milestone achievement for subsequent baselines.

---

## 3. Steps

| Step | Action | Persona | Gate |
|---|---|---|---|
| 1 | EMS Foundation Audit agent runs full conformance audit | Standards Engineer | All sprints complete |
| 2 | Audit: all artefacts against STD-000001 quality gates | Standards Engineer | — |
| 3 | Audit: metadata completeness per STD-000002 | Standards Engineer | — |
| 4 | Audit: structural conformance per STD-000003 | Standards Engineer | — |
| 5 | Audit: vocabulary compliance per STD-000004 | Standards Engineer | — |
| 6 | Audit: traceability completeness per STD-000005 | Standards Engineer | — |
| 7 | Audit: zero orphan artefacts | Standards Engineer | — |
| 8 | Produce EMS_FOUNDATION_CERTIFICATION.md with scores | Standards Engineer | — |
| 9 | Executive Director reviews certification | Executive Director | — |
| 10 | Executive Director approves baseline | Executive Director | Approved |
| 11 | REG-000005 updated with baseline record | Mission Control Director | — |
| 12 | Git tag created: BASELINE-[version] | Mission Control Director | — |
| 13 | All platforms notified of new baseline | Mission Control Director | — |

---

## 4. Baseline Trigger Conditions

| Baseline | Trigger |
|---|---|
| BASELINE-1.0 | Sprint EF-1.8 complete, all sprints EF-1.1 to EF-1.7 certified |
| BASELINE-1.x | Major EMS capability addition or first platform reaching READY |
| BASELINE-2.0 | First complete mission loop executed end-to-end |

---

## 5. Outputs

- EMS_FOUNDATION_CERTIFICATION.md (updated with scores)
- Git tag: BASELINE-[version]
- REG-000005 Foundation Baseline Register updated

---

## 6. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Owned By | PER-000001 | Executive Director |
| Follows | OPR-000008 | Knowledge Capture Operation |
| Updates | REG-000005 | Foundation Baseline Register |
| Produces | Git baseline tag | — |

---

## 7. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1.5 | SeierTech EMS |
