# REG-000008 — RISK REGISTER

| Field | Value |
|---|---|
| Artefact ID | REG-000008 |
| Artefact Class | Register |
| Title | Risk Register |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | OPERATIONAL |
| Owner | Security Architect (PER-000015 / T2-PER-000015) |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Tracks every identified risk across every platform governed by the EMS — security vulnerabilities, dependency CVEs, architectural risks, data exposure risks, and operational risks. This register was referenced as a real, load-bearing artefact across multiple authorities and personas (AUTH-006, AUTH-007, both Security Architect persona definitions in Team 1 and Team 2) before it formally existed as a `REG-NNNNNN` artefact — this fills that gap.

---

## 2. Owner

Security Architect persona. Both Team 1 (during intake — initial risk identification) and Team 2 (during forward missions — ongoing risk tracking) write to this register; Security Architect is the consistent owner across both teams.

---

## 3. Update Trigger

- Platform intake (MISSION-001) identifies dependency CVEs or security posture risks
- Platform genesis (MISSION-000) identifies design-time security risks
- Any forward mission (BUILD/REHAB/AGENTIC_INSERTION) introduces a new dependency, integration, or data handling change
- PII identification during data classification (per AUTH-006 Data Governance Authority)
- A CRITICAL or HIGH severity CVE is found in any dependency manifest

---

## 4. Schema

| Field | Type | Description |
|---|---|---|
| Risk ID | Reference | RSK-[PLATFORM]-NNNNNN |
| Platform | Reference | PLT-NNNNNN |
| Title | String | Short risk description |
| Category | Enum | SECURITY / DEPENDENCY_CVE / ARCHITECTURAL / DATA_EXPOSURE / OPERATIONAL |
| Severity | Enum | CRITICAL / HIGH / MEDIUM / LOW |
| Source | Enum | INTAKE / GENESIS / BUILD_MISSION / MANUAL |
| Identified By | String | Persona or Founder |
| Identified Date | Date | ISO 8601 |
| Description | String | What the risk is and why it matters |
| Affected Component | String | What part of the platform this affects |
| Mitigation | String | Planned or applied mitigation |
| Status | Enum | OPEN / MITIGATED / ACCEPTED / FALSE_POSITIVE |
| Blocks Release | Boolean | True for CRITICAL findings per AUTH-007 — automatic REJECT |
| Resolved Date | Date | ISO 8601, if applicable |

---

## 5. Quality Rules

- Per AUTH-007 SEC-REQ-004: every CRITICAL or HIGH CVE identified during intake or a mission SHALL be added to this register immediately, not deferred
- A risk with Severity CRITICAL and Status OPEN automatically sets Blocks Release to TRUE — this is enforced by the Release Manager during OPR-000007 and cannot be overridden, per AUTH-007's absolute CRITICAL-finding veto
- No risk may move to status MITIGATED or ACCEPTED without the Security Architect recording the mitigation/rationale
- Every entry must reference the platform it belongs to — this register tracks risks across ALL platforms, not one

---

## 6. Lifecycle

```
OPEN → MITIGATED (fix applied, verified)
OPEN → ACCEPTED (Founder/Security Architect accepts the risk explicitly, with rationale)
OPEN → FALSE_POSITIVE (on review, not a genuine risk)
```

---

## 7. Entries

| Risk ID | Platform | Title | Category | Severity | Status | Blocks Release |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

*Populated during MISSION-001/MISSION-000 and ongoing forward missions. No entries yet — no platform has completed a live intake run.*

---

## 8. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Governed By | AUTH-007 | Security Governance Authority |
| Governed By | AUTH-006 | Data Governance Authority (PII-sourced risks) |
| Owned By | PER-000015 | Security Architect (Team 1) |
| Owned By | T2-PER-000015 | Security Architect (Team 2) |
| Updated By | MSN-000001 | MISSION-001 Platform Intake |
| Updated By | MSN-000000 | MISSION-000 Platform Genesis |
| Required By | OPR-000007 | Release Operation (CRITICAL finding gate) |

---

## 9. Review Cycle

Continuous — updated on every risk identification event. Reviewed in full during every OPR-000007 Release Operation for any platform with OPEN CRITICAL/HIGH entries.

---

## 10. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — closes the doctrine gap identified in EMS_DOCTRINE_INVENTORY.md (Risk Register was referenced across AUTH-006, AUTH-007, and both Security Architect personas but did not formally exist as a REG-NNNNNN artefact until now) | SeierTech EMS |
