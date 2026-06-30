# AUTH-009 — RELEASE AUTHORITY

| Field | Value |
|---|---|
| Artefact ID | AUTH-009 |
| Artefact Class | Authority |
| Title | Release Authority |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

This authority governs the release of all engineering outputs to production within the SeierTech EMS. Nothing merges to main without a Scorecard and a RELEASE decision from the Release Manager. This authority is the final quality gate of the mission lifecycle.

---

## 2. Scope

Applies to all code releases across all platforms governed by the EMS.

---

## 3. Principles

- REL-001 — No code merges to main without a RELEASE decision.
- REL-002 — Every release SHALL be scored against defined dimensions.
- REL-003 — CRITICAL security findings SHALL result in automatic REJECT — no override.
- REL-004 — HOLD is a valid decision — it is not a failure.
- REL-005 — Every release decision is recorded in REG-000006 regardless of outcome.
- REL-006 — Knowledge Capture executes after every mission regardless of release decision.

---

## 4. Requirements

| ID | Requirement |
|---|---|
| REL-REQ-001 | Every mission output SHALL produce a Scorecard before release decision |
| REL-REQ-002 | Scorecard SHALL score: quality, security, architecture, standards compliance, operational fit, test coverage |
| REL-REQ-003 | Release Manager SHALL have sole release decision authority |
| REL-REQ-004 | CRITICAL security findings SHALL automatically set decision to REJECT |
| REL-REQ-005 | Every release decision SHALL be recorded in REG-000006 |
| REL-REQ-006 | Merged code SHALL trigger OPR-000008 Knowledge Capture immediately |
| REL-REQ-007 | No pull request SHALL merge without RELEASE decision in Scorecard |

---

## 5. Responsibilities

| Role | Responsibility |
|---|---|
| Release Manager | Produce Scorecard, issue release decision, update REG-000006 |
| Verification Governance Director | Produce Verification Report as input to Scorecard |
| Security Architect | Provide CRITICAL finding flags to Release Manager |
| Executive Director | Escalation authority for release disputes |

---

## 6. Governance

Release Manager decision is final within this authority. CRITICAL security overrides are absolute — even Executive Director cannot override a CRITICAL security REJECT. Release disputes escalate to Executive Director.

---

## 7. Dependencies

- AUTH-001 Engineering Constitution
- AUTH-003 Mission Governance Authority
- AUTH-007 Security Governance Authority

---

## 8. Produces

- Release governance framework
- Scorecard format authority
- Release audit trail

---

## 9. Consumes

- AUTH-001, AUTH-007

---

## 10. Updates

- REG-000006 Release Register

---

## 11. Related Authorities

- AUTH-001, AUTH-003, AUTH-007

---

## 12. Related Standards

- STD-000003 (Scorecard subclass structure)

---

## 13. Related Registers

- REG-000006 Release Register

---

## 14. Related Operations

- OPR-000007 Release Operation

---

## 15. Review Cycle

Annually or on significant change to release risk profile.

---

## 16. Verification

Audit: every entry in REG-000006 has a Scorecard reference. Zero merges without RELEASE decision. Zero CRITICAL findings released.

---

## 17. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1.2 | SeierTech EMS |
