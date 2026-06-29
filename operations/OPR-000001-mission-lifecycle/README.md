# OPR-000001 — MISSION LIFECYCLE OPERATION

| Field | Value |
|---|---|
| Artefact ID | OPR-000001 |
| Artefact Class | Operation |
| Title | Mission Lifecycle Operation |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | Mission Control Director |
| Approval Authority | AUTH-003 Mission Governance Authority |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Define the end-to-end lifecycle of every mission from GitHub Issue creation to baseline update. This is the master operation that all other operations operate within.

---

## 2. Trigger

GitHub Issue created containing a mission instruction in any format — free text, structured, or template-based.

---

## 3. Preconditions

- EMS repository at BASELINE-1.0 or above
- NIM API key configured in GitHub Actions secrets
- For non-intake missions: platform must be READY in REG-000001

---

## 4. Full Lifecycle

```
GitHub Issue Created (any interface — Claude, GPT, Copilot, mobile, free text)
↓
OPR-000001: Mission Control Director classifies and routes
↓
REG-000002: Mission Register updated — status: IN_PROGRESS
↓
[INTAKE missions] → OPR-000002: Platform Intake Operation
[BUILD missions] → OPR-000003: Engineering Proposal Operation
[STRATEGIC missions] → AI Architect leads chain
[REHAB missions] → Technical Debt Auditor leads chain
[AGENTIC_INSERTION] → AI Architect leads chain
[SPEC missions] → Master Spec Author leads chain
↓
OPR-000004: Technical Design Authority (BUILD missions)
↓
OPR-000005: Engineering Delivery Operation
↓
GitHub Branch created
↓
Builder (Kiro / Builder Agent) executes EDP
↓
Pull Request opened
↓
OPR-000006: Verification Operation
↓
Engineering Scorecard produced
↓
OPR-000007: Release Operation
↓
Merge to main
↓
OPR-000008: Knowledge Capture Operation
↓
Registers updated
↓
OPR-000009: Baseline Operation (if baseline trigger met)
↓
GitHub Issue closed
↓
REG-000002: Mission Register updated — status: COMPLETE
```

---

## 5. Gates

| Gate | Description | Responsible Persona |
|---|---|---|
| G-001 | Platform READY before non-intake mission activates | Mission Control Director |
| G-002 | EDP produced and Standards Engineer approved | Standards Engineer |
| G-003 | TDA approved before builder activates | Chief Architect |
| G-004 | Verification PASS before Scorecard | QA & Governance Director |
| G-005 | Scorecard RELEASE decision before merge | Release Manager |
| G-006 | Knowledge captured before issue closes | Documentation & Knowledge Curator |

---

## 6. No Skipped Gates

Every gate is mandatory. No gate may be bypassed for any reason including delivery speed, Founder instruction, or emergency. Gates exist because the loop requires them to tighten. A skipped gate breaks the loop.

---

## 7. Outputs

- Complete mission audit trail in REG-000002
- EDP in work-products/
- Verification Report (VER-NNNNNN)
- Scorecard (SCR-NNNNNN)
- Merged code on main branch
- Knowledge capture artefact
- Updated registers
- Baseline tag (if triggered)

---

## 8. Escalation Path

Mission stalled at any gate → Mission Control Director → Executive Director → Founder

---

## 9. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-003 | Mission Governance Authority |
| Updates | REG-000002 | Mission Register |
| Produces | Complete mission audit trail | — |
| Contains | OPR-000002 through OPR-000009 | All sub-operations |

---

## 10. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1.5 | SeierTech EMS |
