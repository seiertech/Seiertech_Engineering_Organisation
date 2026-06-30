# AUTH-003 — MISSION GOVERNANCE AUTHORITY

| Field | Value |
|---|---|
| Artefact ID | AUTH-003 |
| Artefact Class | Authority |
| Title | Mission Governance Authority |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

This authority governs the complete mission lifecycle within the SeierTech EMS — from issue creation to baseline. It defines how missions are classified, routed, executed, verified, released, and closed. No mission may operate outside this authority.

---

## 2. Scope

Applies to every mission of every type issued within the EMS.

---

## 3. Principles

- **MSN-001** — Every mission begins with a GitHub Issue. No issue, no mission.
- **MSN-002** — No mission fires against a platform not at READY status.
- **MSN-003** — No gate may be skipped for any reason including delivery speed.
- **MSN-004** — Every mission produces a complete, unbroken audit trail.
- **MSN-005** — The Engineering Delivery Package is the only permissible build instruction format. Engineering Delivery Package is a prohibited term.
- **MSN-006** — Knowledge Capture is mandatory after every mission — the loop must close.
- **MSN-007** — Free text mission instructions are valid. The chain normalises them.

---

## 4. Requirements

| ID | Requirement |
|---|---|
| MSN-REQ-001 | Every mission SHALL originate from a GitHub Issue |
| MSN-REQ-002 | Every mission SHALL be classified and registered in REG-000002 before chain activation |
| MSN-REQ-003 | Platform SHALL be at READY status before any non-intake mission activates |
| MSN-REQ-004 | Every BUILD mission SHALL produce a Proposal before an EDP is generated |
| MSN-REQ-005 | Every Proposal SHALL receive a Founder decision before proceeding |
| MSN-REQ-006 | Every BUILD mission SHALL pass Technical Design Authority before builder activates |
| MSN-REQ-007 | Every EDP SHALL pass Standards Engineer conformance before builder activation |
| MSN-REQ-008 | Every completed build SHALL pass Verification before Scorecard |
| MSN-REQ-009 | Every mission SHALL produce a Scorecard before merge to main |
| MSN-REQ-010 | Knowledge Capture SHALL execute after every mission regardless of release decision |
| MSN-REQ-011 | Every mission SHALL close its GitHub Issue with a completion summary |
| MSN-REQ-012 | No gate defined in OPR-000001 SHALL be bypassed |

---

## 5. Mission Types

| Type | Description | Requires Proposal | Requires TDA |
|---|---|---|---|
| INTAKE | Platform onboarding via MISSION-001 | No | No |
| BUILD | Standard build mission | Yes | Yes |
| STRATEGIC | Intelligence — where to add agentic capability | No | No |
| REHAB | Codebase rehabilitation | Yes | Yes |
| AGENTIC_INSERTION | Add agentic capability | Yes | Yes |
| PROPOSAL | Generate build proposal | No | No |
| SPEC | Generate technical specification | No | No |

---

## 6. Responsibilities

| Role | Responsibility |
|---|---|
| Mission Control Director | Classify, route, and track all missions |
| Chief Architect | Chair TDA for all BUILD missions |
| Verification & Governance Director | Own Verification for all missions |
| Release Manager | Own Scorecard and release decision |
| Documentation Curator | Execute Knowledge Capture after every mission |
| Executive Director | Escalation authority for all mission conflicts |

---

## 7. Dependencies

- AUTH-001 Engineering Constitution
- AUTH-002 Platform Governance Authority
- REG-000001 Readiness Register
- REG-000002 Mission Register

---

## 8. Produces

- Mission governance framework
- Complete mission audit trails

---

## 9. Related Authorities

- AUTH-001, AUTH-002, AUTH-009

---

## 10. Related Registers

- REG-000002 Mission Register
- REG-000003 Proposal Register
- REG-000004 Delivery Package Register
- REG-000006 Release Register

---

## 11. Related Operations

- OPR-000001 through OPR-000009

---

## 12. Review Cycle

On any change to the mission lifecycle or addition of new mission types.

---

## 13. Verification

Audit REG-000002: every COMPLETE mission has an unbroken audit trail from GitHub Issue to baseline. Zero missions closed without Verification Report and Scorecard.

---

## 14. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1.2 | SeierTech EMS |
