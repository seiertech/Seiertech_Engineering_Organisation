# AUTH-008 — AI GOVERNANCE AUTHORITY

| Field | Value |
|---|---|
| Artefact ID | AUTH-008 |
| Artefact Class | Authority |
| Title | AI Governance Authority |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

This authority governs all AI capability within the SeierTech EMS — including NVIDIA NIM model usage, agent persona orchestration, agentic insertion into platforms, and the Loop Engineering execution model. Every AI capability must be governed, auditable, and doctrine-bound.

---

## 2. Scope

Applies to all NIM model calls, all agent persona activations, all agentic insertions into platforms, and the Loop Engineering system itself.

---

## 3. Principles

- AI-001 — Every NIM call SHALL be doctrine-injected — authorities and standards loaded before any reasoning begins.
- AI-002 — No AI agent SHALL operate outside its defined persona scope.
- AI-003 — The EMS is model-agnostic at the execution layer. Model strings are configuration — not doctrine.
- AI-004 — Every agentic insertion into a platform SHALL be identified, proposed, and TDA-approved before build.
- AI-005 — AI outputs are work products — they must pass Standards Engineer before commitment to the repo.
- AI-006 — The loop must close — every mission writes back to memory.
- AI-007 — When a superior model becomes available, update NIM_INTEGRATION_CONFIG only — doctrine is unchanged.

---

## 4. Requirements

| ID | Requirement |
|---|---|
| AI-REQ-001 | Every NIM call SHALL inject relevant authorities and standards as system prompt context |
| AI-REQ-002 | Every NIM call SHALL inject the platform spine for platform-specific missions |
| AI-REQ-003 | Model tier assignment SHALL follow integrations/NIM_INTEGRATION_CONFIG.md |
| AI-REQ-004 | Agentic insertions SHALL be documented in the platform AI Capability Map |
| AI-REQ-005 | AI Capability Map SHALL be produced for every platform during intake |
| AI-REQ-006 | Builder agents replacing Kiro SHALL be governed by this authority and AUTH-003 |
| AI-REQ-007 | No NIM call SHALL operate without doctrine injection |
| AI-REQ-008 | All AI outputs SHALL be treated as DRAFT until Standards Engineer approval |

---

## 5. Responsibilities

| Role | Responsibility |
|---|---|
| AI Architect | Own AI Capability Map, design agentic insertions, govern model selection |
| Mission Control Director | Ensure doctrine injection in every chain call |
| Standards Engineer | Validate all AI-produced outputs before commitment |
| Executive Director | Govern AI capability expansion and model changes |

---

## 6. Governance

Model changes require update to NIM_INTEGRATION_CONFIG only — no constitutional change required. New AI capability types (beyond current mission types) require Executive Director approval. Agentic insertions into platforms require TDA approval per AUTH-003.

---

## 7. Dependencies

- AUTH-001 Engineering Constitution
- AUTH-003 Mission Governance Authority
- AUTH-004 Workforce Authority

---

## 8. Produces

- AI governance framework
- Model-agnostic execution layer
- Governed agentic insertion process

---

## 9. Consumes

- AUTH-001 Engineering Constitution
- integrations/NIM_INTEGRATION_CONFIG.md

---

## 10. Updates

- integrations/NIM_INTEGRATION_CONFIG.md (on model tier changes)
- Platform AI Capability Maps

---

## 11. Related Authorities

- AUTH-001, AUTH-003, AUTH-004

---

## 12. Related Standards

- STD-000003 (AI Capability Map structure)

---

## 13. Related Registers

- AI Capability Maps per platform

---

## 14. Related Operations

- All operations — AI powers the entire Loop Engineering chain

---

## 15. Review Cycle

Quarterly — AI model landscape changes rapidly.

---

## 16. Verification

Audit: all NIM calls in GitHub Actions workflow inject doctrine. AI Capability Map exists for every READY platform. Zero AI outputs committed without Standards Engineer approval.

---

## 17. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1.2 | SeierTech EMS |
