# OPR-000008 — KNOWLEDGE CAPTURE OPERATION

| Field | Value |
|---|---|
| Artefact ID | OPR-000008 |
| Artefact Class | Operation |
| Title | Knowledge Capture Operation |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | Documentation & Knowledge Curator |
| Approval Authority | AUTH-010 Knowledge Governance Authority |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Define the Knowledge Capture process — the closing operation of every mission that ensures the loop learns. Every mission completion writes back to memory, updates registers, and enriches the platform spine so subsequent missions are smarter.

---

## 2. Trigger

Release decision issued in OPR-000007 (RELEASE, HOLD, or REJECT — all trigger knowledge capture).

---

## 3. Steps

| Step | Action | Persona | Gate |
|---|---|---|---|
| 1 | Documentation & Knowledge Curator reviews all mission outputs | Documentation & Knowledge Curator | — |
| 2 | Extract lessons learned from mission execution | Documentation & Knowledge Curator | — |
| 3 | Update platform Knowledge Graph with any new entities or relationships introduced | Knowledge Graph Architect | — |
| 4 | Update platform Data Model if schema changed | Data Architect | — |
| 5 | Update platform Architecture Document if architecture changed | Chief Architect | — |
| 6 | Update Technical Debt Register — new debt introduced or resolved | Technical Debt Auditor | — |
| 7 | Update Master Technical Specification with mission changes | Master Spec Author | — |
| 8 | Write mission summary to memory/[PLATFORM_NAME]/ | Documentation & Knowledge Curator | — |
| 9 | Update all relevant registers | Mission Control Director | — |
| 10 | Standards Engineer assesses all updated artefacts | Standards Engineer | PASS |
| 11 | Close GitHub Issue with mission summary comment | Mission Control Director | — |
| 12 | REG-000002 updated — status: COMPLETE | Mission Control Director | — |
| 13 | Assess if baseline trigger conditions are met | Mission Control Director | — |
| 14 | If baseline triggered → proceed to OPR-000009 | Mission Control Director | — |

---

## 4. The Loop Closes Here

Knowledge Capture is what separates Loop Engineering from one-shot agentic tools. Every mission makes the system smarter. The spine gets richer. The MTS stays current. The memory layer accumulates. The next mission starts from a higher baseline than the last.

---

## 5. Outputs

- Updated Knowledge Graph
- Updated Data Model (if changed)
- Updated Architecture Document (if changed)
- Updated Technical Debt Register
- Updated Master Technical Specification
- Mission memory entry in memory/[PLATFORM_NAME]/
- All registers current
- GitHub Issue closed

---

## 6. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-010 | Knowledge Governance Authority |
| Owned By | PER-000018 | Documentation & Knowledge Curator |
| Follows | OPR-000007 | Release Operation |
| Followed By | OPR-000009 | Baseline Operation (if triggered) |
| Updates | memory/ | Platform memory layer |

---

## 7. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1.5 | SeierTech EMS |
