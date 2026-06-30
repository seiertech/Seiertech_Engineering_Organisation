# OPR-000002 — PLATFORM INTAKE OPERATION

| Field | Value |
|---|---|
| Artefact ID | OPR-000002 |
| Artefact Class | Operation |
| Title | Platform Intake Operation |
| Status | ACTIVE |
| Version | 1.1.0 |
| Classification | FOUNDATIONAL |
| Owner | Mission Control Director |
| Approval Authority | AUTH-002 Platform Governance Authority |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Define every step of the MISSION-001 Platform Intake process — from issue creation to platform READY status. This operation is the most complex in the EMS. It runs 24 personas, produces 20+ artefacts, and gates on Standards Engineer conformance after every persona output.

---

## 2. Trigger

GitHub Issue containing: "Complete intake for [PLATFORM_NAME] — repo: [REPO_URL]"

---

## 3. Preconditions

- EMS at BASELINE-1.0 or above
- NIM API key active
- Target repo accessible to the chain
- Platform NOT already at READY status in REG-000001

---

## 4. Steps

### Phase 1 — Mission Activation
| Step | Action | Persona | Gate |
|---|---|---|---|
| 1.1 | Parse issue — extract platform name and repo URL | Mission Control Director | — |
| 1.2 | Create mission record in REG-000002 | Mission Control Director | — |
| 1.3 | Label GitHub Issue: mission:intake, status:in-progress | Mission Control Director | — |
| 1.4 | Create platform directory: platforms/[PLATFORM_NAME]/ | Mission Control Director | — |
| 1.5 | Create spine directory: platforms/[PLATFORM_NAME]/spine/ | Mission Control Director | — |
| 1.6 | Persist target repo URL to platforms/[PLATFORM_NAME]/PLATFORM_REPO_URL.txt — the only mechanism later forward missions (e.g. BUILD via deliver_to_target_repo.py) have to know where to deliver | Mission Control Director | — |
| 1.7 | Clone/read target repo | NIM Chain | Repo accessible |

### Phase 2 — Repo Scan
| Step | Action | Persona | Gate |
|---|---|---|---|
| 2.1 | Full codebase structure scan | NIM Chain | — |
| 2.2 | Identify: languages, frameworks, file count, LOC | NIM Chain | — |
| 2.3 | Identify: existing documentation | NIM Chain | — |
| 2.4 | Identify: existing tests | NIM Chain | — |
| 2.5 | Identify: infrastructure and deployment config | NIM Chain | — |
| 2.6 | Identify: existing knowledge graph (if any) | NIM Chain | — |

### Phase 3 — Layer 1 Persona Extraction (parallel where possible)

Each step: Persona produces artefact → Standards Engineer assesses → PASS proceeds → FAIL returns to persona

| Step | Persona | Output Artefact |
|---|---|---|
| 3.1 | Use Case Analyst | Use Case Register |
| 3.2 | Data Architect | Data Model |
| 3.3 | Integration Engineer | Integration Map + API Register |
| 3.4 | Platform Engineer | Deployment Architecture |
| 3.5 | Chief Architect | Architecture Document |
| 3.6 | Enterprise Architect | Enterprise Architecture Context |
| 3.7 | Security Architect | Security Posture + Risk Register entries |
| 3.8 | Frontend Engineering Lead | Frontend Engineering Assessment |
| 3.9 | Backend Engineering Lead | Backend Engineering Assessment |
| 3.10 | UI/UX Director | UX Assessment |
| 3.11 | AI Architect | AI Capability Map |
| 3.12 | Knowledge Graph Architect | Knowledge Graph + Domain Vocabulary |
| 3.13 | SME System User | Operational validation of Use Cases |
| 3.14 | Senior Business Analyst | Requirements Register |
| 3.15 | Technical Debt Auditor | Technical Debt Register |
| 3.16 | Verification & Governance Director | Test Strategy |
| 3.17 | Documentation & Knowledge Curator | Documentation Assessment |

**Standards Engineer gate after every artefact — PASS or REVISE**

### Phase 4 — Questions to Founder
| Step | Action | Persona | Gate |
|---|---|---|---|
| 4.1 | Aggregate all unresolved gaps from Layer 1 | Mission Control Director | — |
| 4.2 | Post Questions to Founder as GitHub Issue comment | Mission Control Director | — |
| 4.3 | Wait for Founder responses | — | Founder response received |
| 4.4 | Update relevant artefacts with Founder responses | Relevant personas | — |
| 4.5 | Re-run Standards Engineer on updated artefacts | Standards Engineer | PASS |

### Phase 5 — Layer 3 Synthesis
| Step | Action | Persona | Gate |
|---|---|---|---|
| 5.1 | Proposition Analyst activates — all Layer 1 outputs confirmed PASS | Proposition Analyst | All Layer 1 PASS |
| 5.2 | Produce Proposition Document | Proposition Analyst | — |
| 5.3 | Produce Platform Value Assessment | Proposition Analyst | — |
| 5.4 | Produce Product Roadmap Scaffold | Proposition Analyst | — |
| 5.5 | Standards Engineer assesses Layer 3 outputs | Standards Engineer | PASS |
| 5.6 | Master Spec Author activates | Master Spec Author | Layer 3 PASS |
| 5.7 | Produce Master Technical Specification (15 sections) | Master Spec Author | — |
| 5.8 | Standards Engineer assesses MTS | Standards Engineer | PASS |

### Phase 6 — Readiness Certification
| Step | Action | Persona | Gate |
|---|---|---|---|
| 6.1 | Check all 10 readiness gates in REG-000001 | Mission Control Director | All gates PASS |
| 6.2 | Executive Director reviews intake package | Executive Director | Sign-off |
| 6.3 | Set platform status to READY in REG-000001 | Mission Control Director | — |
| 6.4 | Close GitHub Issue with READY confirmation | Mission Control Director | — |
| 6.5 | Post completion comment on GitHub Issue | Mission Control Director | — |
| 6.6 | Update REG-000002 — mission status: COMPLETE | Mission Control Director | — |

---

## 5. Mandatory Intake Outputs

Every platform must exit intake with ALL of the following:

**Layer 1 Artefacts:**
- Use Case Register
- Data Model
- Integration Map
- API Register
- Deployment Architecture
- Architecture Document
- Enterprise Architecture Context
- Security Posture Document
- Frontend Engineering Assessment
- Backend Engineering Assessment
- UX Assessment
- AI Capability Map
- Knowledge Graph
- Domain Vocabulary
- Requirements Register
- Technical Debt Register
- Test Strategy
- Documentation Assessment

**Layer 3 Artefacts:**
- Proposition Document
- Platform Value Assessment
- Product Roadmap Scaffold
- Master Technical Specification

**Register Updates:**
- REG-000001 Readiness Register — platform at READY
- REG-000002 Mission Register — mission COMPLETE

---

## 6. The Mandatory Creation Rule

If any Layer 1 artefact does not exist in the platform repo, the chain MUST create it. No artefact may be left absent. Every platform exits intake with a complete set regardless of prior state.

| Artefact | If Found | If Not Found |
|---|---|---|
| Knowledge Graph | Ingest and enrich | CREATE from Data Model, Use Cases, Architecture |
| Use Case Register | Harvest and normalise | DERIVE from routes, features, README |
| Data Model | Extract and formalise | GENERATE from schemas, migrations, ORM |
| Test Strategy | Assess coverage | SCAFFOLD — create strategy, flag coverage gap |
| Architecture Document | Ingest | GENERATE from codebase structure |
| All others | Same pattern | Same pattern |

---

## 7. Outputs

- 20+ conformant EMS artefacts in platforms/[PLATFORM_NAME]/
- Platform spine in platforms/[PLATFORM_NAME]/spine/
- Platform at READY in REG-000001
- Complete mission audit trail in REG-000002

---

## 8. Escalation Path

- Repo inaccessible → notify Founder, halt intake
- Standards Engineer repeated FAIL → escalate to Executive Director
- Questions to Founder unanswered > 48 hours → escalate to Founder, pause intake

---

## 9. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-002 | Platform Governance Authority |
| Governed By | AUTH-003 | Mission Governance Authority |
| Implements | MSN-000001 | MISSION-001 Platform Intake |
| Updates | REG-000001 | Readiness Register |
| Updates | REG-000002 | Mission Register |
| Activates | All 24 personas | Intake sequence |

---

## 10. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1.5 | SeierTech EMS |
| 1.1.0 | 2026-06-30 | Added Phase 1 Step 1.6 — persist target repo URL to PLATFORM_REPO_URL.txt (renumbered the clone step to 1.7) — full-repo sweep found run_intake_chain.py's DAM-000006 fix had never been reflected back into this operation's own step table | SeierTech EMS |
