# MSN-000001 — MISSION-001: PLATFORM INTAKE

| Field | Value |
|---|---|
| Artefact ID | MSN-000001 |
| Artefact Class | Mission |
| Title | Platform Intake |
| Status | ACTIVE |
| Version | 3.0.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Mission Statement

Complete the full intake of a named platform into the SeierTech EMS. Read the platform repository autonomously. Find what exists. Derive what is implied. Create what is missing. Produce 20+ conformant EMS artefacts across 4 layers. Every artefact must pass the Standards Engineer before it is committed. No mission may be issued against the platform until this mission completes with all readiness gates PASSED, all founder questions resolved, and the Master Technical Specification approved.

---

## 2. The Mandatory Creation Rule

The intake chain does not ask "does this exist?" It asks "do I have this?" If not — it builds it.

| Artefact | If Found in Repo | If Not Found |
|---|---|---|
| Knowledge Graph | Ingest, validate, enrich | CREATE from Data Model, Use Cases, Architecture Document |
| Use Case Register | Harvest and normalise | DERIVE from routes, features, README, user stories |
| Data Model | Extract and formalise | GENERATE from schemas, migrations, ORM models, DB configs |
| Architecture Document | Ingest | GENERATE from folder structure, dependencies, service boundaries |
| API Register | Parse existing docs | GENERATE from routes, controllers, endpoints in code |
| Test Strategy | Assess coverage, identify gaps | SCAFFOLD — create strategy, document coverage gap as debt |
| Security Posture | Extract from auth model | GENERATE from auth patterns, dependency scan, API exposure |
| Knowledge Graph | Ingest | CREATE — this is mandatory, not optional |
| All other artefacts | Same pattern | Same pattern — create from evidence |

No platform exits intake with a missing artefact. Every platform reaches the same baseline quality regardless of prior state.

---

## 3. How to Issue This Mission

The Founder issues this mission by creating a GitHub Issue in any format:

```
Complete intake for [PLATFORM_NAME] — repo: [REPO_URL]
```

Or free text — the Mission Control Director and NIM chain normalise any instruction into a structured intake mission.

Example:
```
Complete intake for COMMANDER_C2 — repo: github.com/seiertech/commander-c2
```

The chain detects the issue, parses intent, and begins execution automatically via the GitHub Actions workflow.

---

## 4. Trigger

GitHub Issue created. Webhook fires. NIM chain activates via `.github/workflows/ems-mission-chain.yml`.

---

## 5. Execution — Full Intake Sequence

See OPR-000002 Platform Intake Operation for the complete step-by-step execution sequence.

---

## 6. Mandatory Output Set

### Layer 1 — Discovery & Creation (17 artefacts)

Every artefact is produced by its designated persona, assessed by the Standards Engineer, and committed only on PASS.

| # | Artefact | Producing Persona | Location |
|---|---|---|---|
| 1 | Use Case Register | Use Case Analyst | platforms/[NAME]/USE_CASE_REGISTER.md |
| 2 | Data Model | Data Architect | platforms/[NAME]/DATA_MODEL.md |
| 3 | Integration Map | Integration Engineer | platforms/[NAME]/INTEGRATION_MAP.md |
| 4 | API Register | Integration Engineer | platforms/[NAME]/API_REGISTER.md |
| 5 | Deployment Architecture | Platform Engineer | platforms/[NAME]/DEPLOYMENT_ARCHITECTURE.md |
| 6 | Architecture Document | Chief Architect | platforms/[NAME]/ARCHITECTURE_DOCUMENT.md |
| 7 | Enterprise Architecture Context | Enterprise Architect | platforms/[NAME]/ENTERPRISE_ARCHITECTURE_CONTEXT.md |
| 8 | Security Posture Document | Security Architect | platforms/[NAME]/SECURITY_POSTURE.md |
| 9 | Risk Register entries | Security Architect | registers/RISK_REGISTER.md |
| 10 | Frontend Engineering Assessment | Frontend Engineering Lead | platforms/[NAME]/FRONTEND_ASSESSMENT.md |
| 11 | Backend Engineering Assessment | Backend Engineering Lead | platforms/[NAME]/BACKEND_ASSESSMENT.md |
| 12 | UX Assessment | UI/UX Director | platforms/[NAME]/UX_ASSESSMENT.md |
| 13 | AI Capability Map | AI Architect | platforms/[NAME]/AI_CAPABILITY_MAP.md |
| 14 | Knowledge Graph | Knowledge Graph Architect | platforms/[NAME]/KNOWLEDGE_GRAPH.md |
| 15 | Domain Vocabulary | Knowledge Graph Architect | platforms/[NAME]/DOMAIN_VOCABULARY.md |
| 16 | Requirements Register | Senior Business Analyst | platforms/[NAME]/REQUIREMENTS_REGISTER.md |
| 17 | Technical Debt Register | Technical Debt Auditor | platforms/[NAME]/TECHNICAL_DEBT_REGISTER.md |
| 18 | Test Strategy | QA & Governance Director | platforms/[NAME]/TEST_STRATEGY.md |
| 19 | Documentation Assessment | Documentation & Knowledge Curator | platforms/[NAME]/DOCUMENTATION_ASSESSMENT.md |

### Layer 2 — Engineering Documentation

| # | Artefact | Producing Persona | Location |
|---|---|---|---|
| 20 | Spine files (one per persona) | All Layer 1 personas | platforms/[NAME]/spine/ |

### Layer 3 — Commercial & Strategic Synthesis

Activates only after ALL Layer 1 artefacts have passed the Standards Engineer.

| # | Artefact | Producing Persona | Location |
|---|---|---|---|
| 21 | Proposition Document | Proposition Analyst | platforms/[NAME]/PROPOSITION_DOCUMENT.md |
| 22 | Platform Value Assessment | Proposition Analyst | platforms/[NAME]/PLATFORM_VALUE_ASSESSMENT.md |
| 23 | Product Roadmap Scaffold | Proposition Analyst | platforms/[NAME]/PRODUCT_ROADMAP_SCAFFOLD.md |

### Layer 4 — Master Synthesis

Activates only after ALL Layer 3 artefacts have passed the Standards Engineer. The final intake output.

| # | Artefact | Producing Persona | Location |
|---|---|---|---|
| 24 | Master Technical Specification | Master Spec Author | platforms/[NAME]/MASTER_TECHNICAL_SPECIFICATION.md |

---

## 7. Master Technical Specification — 15 Required Sections

The MTS is the crown jewel of the intake. Every subsequent mission reads it first. It must contain all 15 sections:

1. Executive Summary
2. Architecture Specification
3. Data Model Specification
4. API Specification
5. Integration Specification
6. Frontend Specification
7. Backend Specification
8. Security Specification
9. Deployment Specification
10. AI Capability Specification
11. Test Specification
12. Knowledge Architecture
13. Technical Debt Schedule
14. Proposition Summary
15. Mission Readiness Declaration

Every section must cite its source persona output. No invented content.

---

## 8. Standards Engineer Gate

The Standards Engineer runs after EVERY persona output — not just at end of intake. No artefact proceeds to the next step until it passes:

- STD-000001 — all 10 quality gates
- STD-000002 — complete metadata block
- STD-000003 — correct subclass structure
- STD-000004 — no prohibited vocabulary
- STD-000005 — all relationships declared and resolvable

FAIL → persona revises → re-assessed. No exceptions. No waivers.

---

## 9. Questions to Founder

When the chain cannot determine information from the repo alone, it posts a structured Questions to Founder comment on the GitHub Issue:

```markdown
## Questions to Founder

The following information could not be determined from the repository:

1. [QUESTION] — Context: [why the chain needs this] — Blocking: [which artefact]
2. [QUESTION] — Context: [why the chain needs this] — Blocking: [which artefact]
```

The Founder responds by commenting on the issue. The chain reads the response, updates the relevant artefact, re-runs Standards Engineer, and continues.

No question may remain unresolved when the platform reaches READY.

---

## 10. Readiness Gates

All 10 must pass before platform status is set to READY:

| Gate | Description |
|---|---|
| RG-001 | Platform Record created and metadata complete |
| RG-002 | Repo scan completed |
| RG-003 | Data model extracted or created |
| RG-004 | Tech stack identified |
| RG-005 | Use case register populated or created |
| RG-006 | Knowledge graph created or enriched |
| RG-007 | All persona spine files present |
| RG-008 | All founder questions resolved |
| RG-009 | Master Technical Specification reviewed and approved |
| RG-010 | Platform registered in Readiness Register at READY |

---


---

## 11. Phase 7 — Platform Baseline Sync

After all 10 readiness gates pass and the Master Technical Specification is approved, MISSION-001 does not close. It triggers OPR-000010 Platform Baseline Sync immediately.

OPR-000010 runs as Phase 7 of every brownfield intake. It:

- Creates the `.ems/` folder in the platform repo per STD-000006
- Populates `.ems/spine/` with all persona spine files
- Copies the MTS to `.ems/MASTER_TECHNICAL_SPECIFICATION.md`
- Runs the Build Governance Auditor (PER-000025) — archaeology, classification, reconciliation
- Produces `.ems/governance/` — Build Governance Register, Active Standards, Deprecated Governance
- Produces `.ems/kiro-sync/` — MEMORY.md, RULES.md, STANDARDS.md for Kiro
- Deprecates all superseded governance in the platform repo
- Installs the continuous sync GitHub Action in the platform repo
- Verifies `.ems/` completeness per STD-000006

Only when OPR-000010 completes does the platform reach fully operational status and MISSION-001 close.

See OPR-000010 for the complete step-by-step sequence.

## 12. Persona Sequence

**Team 1 — Baseline Establishment Force** activates for this mission.

All 25 Team 1 personas activate in the defined intake sequence. See `agents/team-1-baseline/TEAM_1_REGISTRY.md` for the complete sequence.

After intake completes, Team 1 produces the Handoff Artefact (HAR) and stands down. Team 2 takes over all forward operations.

The Standards Engineer is the only persona that runs after every other persona — it is the continuous quality gate throughout intake.

---

## 13. Authority References

- AUTH-001 — Engineering Constitution
- AUTH-002 — Platform Governance Authority
- AUTH-003 — Mission Governance Authority
- AUTH-006 — Data Governance Authority
- AUTH-007 — Security Governance Authority
- AUTH-008 — AI Governance Authority
- AUTH-010 — Knowledge Governance Authority

---

## 14. Standard References

- STD-000001 through STD-000005 — all applied to every artefact produced

---

## 15. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Implements | OPR-000002 | Platform Intake Operation |
| Produces | 24+ artefacts | platforms/[NAME]/ |
| Updates | REG-000001 | Readiness Register |
| Updates | REG-000002 | Mission Register |
| Required By | All platform missions | No mission fires without intake complete |

---

## 16. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation | SeierTech EMS |
| 2.0.0 | 2026-06-29 | Full rebuild — 4-layer output mandate, mandatory creation rule, 24 personas, 15-section MTS | SeierTech EMS |
| 3.0.0 | 2026-06-29 | Added Phase 7 Platform Baseline Sync, Build Governance Auditor persona, .ems/ footprint | SeierTech EMS |
