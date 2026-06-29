# AUTH-004 — WORKFORCE AUTHORITY

| Field | Value |
|---|---|
| Artefact ID | AUTH-004 |
| Artefact Class | Authority |
| Title | Workforce Authority |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

This authority governs the definition, activation, and governance of all agent personas within the SeierTech EMS. Every persona is an AI reasoning role instantiated by NVIDIA NIM. This authority defines what personas may do, how they are structured, and how they are governed.

---

## 2. Scope

Applies to all 24 agent personas defined in agents/ and any future personas added to the EMS.

---

## 3. Principles

- WRK-001 — Every persona operates within defined scope. No persona may exceed its authority.
- WRK-002 — Every persona has a defined AI Reasoning Profile that governs NIM instantiation.
- WRK-003 — Personas are not interchangeable. Each has a unique role and cannot substitute for another.
- WRK-004 — The Standards Engineer is the quality gate for all persona outputs — it cannot be bypassed.
- WRK-005 — Persona definitions are living artefacts — updated as the EMS matures.

---

## 4. Requirements

| ID | Requirement |
|---|---|
| WRK-REQ-001 | Every persona SHALL conform to the Persona subclass structure per STD-000003 |
| WRK-REQ-002 | Every persona SHALL declare an AI Reasoning Profile for NIM instantiation |
| WRK-REQ-003 | Every persona SHALL declare its intake role |
| WRK-REQ-004 | New personas SHALL be approved by Executive Director before activation |
| WRK-REQ-005 | Every persona SHALL declare escalation rules |
| WRK-REQ-006 | The Standards Engineer persona SHALL run after every other persona output |

---

## 5. Responsibilities

| Role | Responsibility |
|---|---|
| Executive Director | Approve new persona creation, resolve persona conflicts |
| Mission Control Director | Activate correct persona set per mission type |
| Standards Engineer | Validate all persona outputs before commitment |

---

## 6. Governance

New persona proposals require Executive Director approval. Persona scope disputes escalate to Executive Director. No persona may self-expand its scope.

---

## 7. Dependencies

- AUTH-001 Engineering Constitution
- STD-000002 Engineering Artefact Metadata Standard
- STD-000003 Engineering Artefact Structure Standard

---

## 8. Produces

- Governed workforce of 24 AI agent personas
- Defined intake execution sequence

---

## 9. Consumes

- AUTH-001 Engineering Constitution

---

## 10. Updates

- agents/README.md (Persona Registry)

---

## 11. Related Authorities

- AUTH-001 Engineering Constitution
- AUTH-003 Mission Governance Authority
- AUTH-008 AI Governance Authority

---

## 12. Related Standards

- STD-000003 Engineering Artefact Structure Standard (Persona subclass)

---

## 13. Related Registers

- agents/README.md Persona Registry

---

## 14. Related Operations

- OPR-000002 Platform Intake Operation (activates all personas)

---

## 15. Review Cycle

On addition of new personas or significant change to persona scope.

---

## 16. Verification

Audit: every persona in agents/ has an AI Reasoning Profile, intake role, and escalation rules defined. Count: 24 active personas.

---

## 17. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1.2 | SeierTech EMS |
