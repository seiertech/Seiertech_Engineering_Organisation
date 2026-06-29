# OPR-000007 — RELEASE OPERATION

| Field | Value |
|---|---|
| Artefact ID | OPR-000007 |
| Artefact Class | Operation |
| Title | Release Operation |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | Release Manager |
| Approval Authority | AUTH-009 Release Authority |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Define the Release process — the final governance gate before code merges to main. The Release Manager scores the mission output and issues a RELEASE, HOLD, or REJECT decision.

---

## 2. Trigger

Verification Report status PASS or CONDITIONAL in OPR-000006.

---

## 3. Steps

| Step | Action | Persona | Gate |
|---|---|---|---|
| 1 | Release Manager reviews Verification Report | Release Manager | VER exists |
| 2 | Produce Scorecard (SCR-NNNNNN) — score all dimensions | Release Manager | — |
| 3 | Score dimensions: quality, security, architecture, standards, operational fit, test coverage | Release Manager | — |
| 4 | Issue release decision: RELEASE / HOLD / REJECT | Release Manager | — |
| 5 | RELEASE → approve PR merge | Release Manager | — |
| 6 | Merge PR to main | Builder / NIM Chain | RELEASE |
| 7 | REG-000004 updated — status: RELEASED | Release Manager | — |
| 8 | REG-000006 Release Register updated | Release Manager | — |
| 9 | Proceed to OPR-000008 Knowledge Capture | Mission Control Director | — |
| 10 | HOLD → document hold reasons, return to Verification | Release Manager | — |
| 11 | REJECT → close mission without merge, update all registers | Release Manager | — |

---

## 4. Gates

- Scorecard mandatory before release decision
- CRITICAL security findings = automatic REJECT
- No merge without RELEASE decision

---

## 5. Outputs

- Scorecard (SCR-NNNNNN)
- Release decision (RELEASE / HOLD / REJECT)
- Merged code on main (if RELEASE)
- REG-000006 updated

---

## 6. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-009 | Release Authority |
| Owned By | PER-000019 | Release Manager |
| Follows | OPR-000006 | Verification Operation |
| Followed By | OPR-000008 | Knowledge Capture Operation |
| Updates | REG-000006 | Release Register |

---

## 7. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1.5 | SeierTech EMS |
