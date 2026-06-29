# OPR-000006 — VERIFICATION OPERATION

| Field | Value |
|---|---|
| Artefact ID | OPR-000006 |
| Artefact Class | Operation |
| Title | Verification Operation |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | QA & Governance Director |
| Approval Authority | AUTH-003 Mission Governance Authority |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Define the Verification process — the quality gate between a completed build and release. Every EDP must pass Verification before a Scorecard is produced and release is considered.

---

## 2. Trigger

Pull Request opened following builder completion in OPR-000005.

---

## 3. Steps

| Step | Action | Persona | Gate |
|---|---|---|---|
| 1 | QA & Governance Director activates Verification | QA & Governance Director | PR exists |
| 2 | Assert every EDP acceptance criterion has a test | QA & Governance Director | — |
| 3 | Execute test assertions defined in EDP | Test agents / QA persona | — |
| 4 | Standards Engineer assesses built output against all relevant standards | Standards Engineer | — |
| 5 | Security Architect reviews for security regression | Security Architect | — |
| 6 | Chief Architect reviews for architectural drift | Chief Architect | — |
| 7 | SME System User validates operational acceptability | SME System User | — |
| 8 | Produce Verification Report (VER-NNNNNN) | QA & Governance Director | — |
| 9 | Overall result: PASS / FAIL / CONDITIONAL | QA & Governance Director | — |
| 10 | PASS → proceed to OPR-000007 Release | — | PASS |
| 11 | FAIL → return to builder with specific findings | QA & Governance Director | — |
| 12 | CONDITIONAL → proceed with conditions recorded in Scorecard | — | Conditions documented |

---

## 4. Gates

- Every acceptance criterion must be tested — no exceptions
- CRITICAL security findings block release regardless of other results
- Verification Report mandatory before Scorecard

---

## 5. Outputs

- Verification Report (VER-NNNNNN)
- Test execution evidence
- Overall PASS / FAIL / CONDITIONAL verdict

---

## 6. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-003 | Mission Governance Authority |
| Owned By | PER-000016 | QA & Governance Director |
| Follows | OPR-000005 | Engineering Delivery Operation |
| Followed By | OPR-000007 | Release Operation |
| Produces | Verification Report | VER-NNNNNN |

---

## 7. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1.5 | SeierTech EMS |
