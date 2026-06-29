# OPR-000003 — ENGINEERING PROPOSAL OPERATION

| Field | Value |
|---|---|
| Artefact ID | OPR-000003 |
| Artefact Class | Operation |
| Title | Engineering Proposal Operation |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | Mission Control Director |
| Approval Authority | AUTH-003 Mission Governance Authority |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Define the process for producing an Engineering Proposal from a BUILD, AGENTIC_INSERTION, or SPEC mission. Every mission that results in code changes must first produce a Proposal that the Founder approves before an EDP is generated.

---

## 2. Trigger

BUILD, AGENTIC_INSERTION, or SPEC mission classified and routed by Mission Control Director.

---

## 3. Preconditions

- Platform at READY in REG-000001
- Mission record in REG-000002 at IN_PROGRESS
- Master Technical Specification available for context injection

---

## 4. Steps

| Step | Action | Persona | Gate |
|---|---|---|---|
| 1 | Load Master Technical Specification as primary context | NIM Chain | MTS exists |
| 2 | Load relevant spine files for mission scope | NIM Chain | — |
| 3 | Load relevant authorities and standards | NIM Chain | — |
| 4 | Activate relevant personas per mission type | Mission Control Director | — |
| 5 | Produce Proposal — problem statement, approach, SDK refs if applicable, alternatives, dependencies, risks, effort estimate | Lead persona | — |
| 6 | Standards Engineer assesses Proposal conformance | Standards Engineer | PASS |
| 7 | Post Proposal to GitHub Issue for Founder decision | Mission Control Director | — |
| 8 | Await Founder decision: APPROVED / REJECTED / DEFERRED | — | Founder decision |
| 9 | Record decision in REG-000003 Proposal Register | Mission Control Director | — |
| 10 | APPROVED → proceed to OPR-000004 TDA | — | APPROVED |
| 11 | REJECTED → close mission, update registers | Mission Control Director | — |
| 12 | DEFERRED → pause mission, update registers | Mission Control Director | — |

---

## 5. Gates

- Proposal must pass Standards Engineer before Founder sees it
- Founder decision is mandatory — no EDP without APPROVED Proposal
- No gate may be skipped

---

## 6. Outputs

- Engineering Proposal (PRP-NNNNNN) in proposals/
- REG-000003 Proposal Register updated
- Founder decision recorded

---

## 7. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-003 | Mission Governance Authority |
| Updates | REG-000003 | Proposal Register |
| Produces | Engineering Proposal | PRP-NNNNNN |
| Followed By | OPR-000004 | Technical Design Authority |

---

## 8. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1.5 | SeierTech EMS |
