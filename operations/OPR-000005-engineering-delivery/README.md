# OPR-000005 — ENGINEERING DELIVERY OPERATION

| Field | Value |
|---|---|
| Artefact ID | OPR-000005 |
| Artefact Class | Operation |
| Title | Engineering Delivery Operation |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | Mission Control Director |
| Approval Authority | AUTH-003 Mission Governance Authority |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Define the process for producing an Engineering Delivery Package from a TDA-approved design and executing the build via Kiro or builder agents.

---

## 2. Trigger

TDA verdict APPROVED in OPR-000004.

---

## 3. Steps

| Step | Action | Persona | Gate |
|---|---|---|---|
| 1 | Generate EDP from approved design + MTS + spine context | NIM Chain | TDA APPROVED |
| 2 | EDP includes: build instructions, standards applied, test assertions | Lead persona | — |
| 3 | Standards Engineer assesses EDP conformance | Standards Engineer | PASS |
| 4 | EDP committed to work-products/ | Mission Control Director | — |
| 5 | REG-000004 Delivery Package Register updated — status: PRODUCED | Mission Control Director | — |
| 6 | GitHub branch created: mission/[MSN-ID] | NIM Chain | — |
| 7 | Builder (Kiro / Builder Agent) picks up EDP and executes | Builder | — |
| 8 | REG-000004 updated — status: BUILDING | Mission Control Director | — |
| 9 | Builder completes — Pull Request opened | Builder | — |
| 10 | REG-000004 updated — status: BUILT | Mission Control Director | — |
| 11 | Proceed to OPR-000006 Verification | Mission Control Director | — |

---

## 4. Gates

- EDP must pass Standards Engineer before builder activation
- No build without a conformant EDP in work-products/
- PR must exist before Verification activates

---

## 5. Outputs

- Engineering Delivery Package (EDP-NNNNNN) in work-products/
- GitHub branch with built code
- Pull Request ready for Verification

---

## 6. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-003 | Mission Governance Authority |
| Follows | OPR-000004 | Technical Design Authority |
| Followed By | OPR-000006 | Verification Operation |
| Updates | REG-000004 | Delivery Package Register |

---

## 7. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1.5 | SeierTech EMS |
