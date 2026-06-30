# MSN-000000 — MISSION-000: PLATFORM GENESIS

| Field | Value |
|---|---|
| Artefact ID | MSN-000000 |
| Artefact Class | Mission |
| Title | Platform Genesis |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Mission Statement

Create a new platform from nothing but a brief. Design every artefact forward from intent. Create the GitHub repository. Establish the `.ems/` folder before any application code. Assign a builder to a clean, governed, doctrine-bound repo. Produce the same READY state as a brownfield platform completing MISSION-001 — so that all subsequent missions operate identically regardless of platform origin.

---

## 2. How to Issue This Mission

```
Genesis: [PLATFORM_NAME] — [one line brief]
```

Examples:
```
Genesis: COMPASS — personal growth operating system for consumer mobile
Genesis: COMMANDER_ASM — outside-in attack surface management for enterprise security
Genesis: PULSE — real-time financial analytics dashboard for SME founders
```

Free text is also valid — Mission Control Director normalises any instruction into a structured genesis mission.

---

## 3. Trigger

GitHub Issue containing genesis instruction. Webhook fires. NIM chain activates via `.github/workflows/ems-mission-chain.yml`.

---

## 4. The Core Principle

**Design forward, not backward.**

Every persona operates in DESIGN mode not EXTRACT mode:
- Chief Architect designs the architecture from the brief
- Data Architect designs the data model from use cases
- Knowledge Graph Architect designs the graph from designed entities
- Security Architect designs the security posture from requirements

Nothing is extracted from code because no code exists yet. Everything is reasoned from the brief, the use cases, and EMS doctrine.

---

## 5. The .ems/ First Rule

The `.ems/` folder is created before any application code. This is the defining characteristic of greenfield genesis. The builder's first action is to read `.ems/kiro-sync/` — doctrine comes before code, always.

---

## 6. Execution

See OPR-000011 Platform Genesis Operation for the complete 7-phase execution sequence.

**Team 2 — Forward Build Force** activates for this mission. In greenfield genesis, Team 2 both establishes the baseline AND operates as the permanent forward force. No handoff needed — they hold the baseline from the start.

---

## 7. Mandatory Output Set

### Designed Artefacts (same set as MISSION-001 but designed not extracted)

| Artefact | Producing Persona | Location |
|---|---|---|
| Use Case Register | Use Case Analyst | platforms/[NAME]/USE_CASE_REGISTER.md |
| Data Model | Data Architect | platforms/[NAME]/DATA_MODEL.md |
| Integration Map | Integration Engineer | platforms/[NAME]/INTEGRATION_MAP.md |
| API Register | Integration Engineer | platforms/[NAME]/API_REGISTER.md |
| Deployment Architecture | Platform Engineer | platforms/[NAME]/DEPLOYMENT_ARCHITECTURE.md |
| Architecture Document | Chief Architect | platforms/[NAME]/ARCHITECTURE_DOCUMENT.md |
| Enterprise Architecture Context | Enterprise Architect | platforms/[NAME]/ENTERPRISE_ARCHITECTURE_CONTEXT.md |
| Security Architecture | Security Architect | platforms/[NAME]/SECURITY_POSTURE.md |
| Frontend Architecture | Frontend Engineering Lead | platforms/[NAME]/FRONTEND_ASSESSMENT.md |
| Backend Architecture | Backend Engineering Lead | platforms/[NAME]/BACKEND_ASSESSMENT.md |
| UX Framework | UI/UX Director | platforms/[NAME]/UX_ASSESSMENT.md |
| AI Capability Map | AI Architect | platforms/[NAME]/AI_CAPABILITY_MAP.md |
| Knowledge Graph | Knowledge Graph Architect | platforms/[NAME]/KNOWLEDGE_GRAPH.md |
| Domain Vocabulary | Knowledge Graph Architect | platforms/[NAME]/DOMAIN_VOCABULARY.md |
| Requirements Register | Senior Business Analyst | platforms/[NAME]/REQUIREMENTS_REGISTER.md |
| Technical Debt Register | Technical Debt Auditor | platforms/[NAME]/TECHNICAL_DEBT_REGISTER.md |
| Test Strategy | Verification Governance Director | platforms/[NAME]/TEST_STRATEGY.md |
| Documentation Framework | Documentation Curator | platforms/[NAME]/DOCUMENTATION_ASSESSMENT.md |

### Synthesis Artefacts

| Artefact | Producing Persona | Location |
|---|---|---|
| Proposition Document | Proposition Analyst | platforms/[NAME]/PROPOSITION_DOCUMENT.md |
| Platform Value Assessment | Proposition Analyst | platforms/[NAME]/PLATFORM_VALUE_ASSESSMENT.md |
| Product Roadmap | Proposition Analyst | platforms/[NAME]/PRODUCT_ROADMAP_SCAFFOLD.md |
| Master Technical Specification | Master Spec Author | platforms/[NAME]/MASTER_TECHNICAL_SPECIFICATION.md |

### .ems/ Artefacts (created in platform repo)

| Artefact | Location in Platform Repo |
|---|---|
| PLATFORM_BASELINE.md | .ems/ |
| MASTER_TECHNICAL_SPECIFICATION.md | .ems/ |
| BASELINE_MANIFEST.md | .ems/ |
| Spine files (17) | .ems/spine/ |
| BUILD_GOVERNANCE_REGISTER.md | .ems/governance/ |
| ACTIVE_STANDARDS.md | .ems/governance/ |
| MEMORY.md | .ems/kiro-sync/ |
| RULES.md | .ems/kiro-sync/ |
| STANDARDS.md | .ems/kiro-sync/ |

### Platform Deliverables

| Deliverable | Description |
|---|---|
| GitHub Repository | New repo created with EMS-standard folder structure |
| Initial EDP | First Engineering Delivery Package — scaffold build |
| Builder Assignment | Kiro or builder agent assigned and synced to .ems/ |
| GitHub Actions | ems-mission-chain.yml + ems-sync.yml installed |

---

## 8. Differences from MISSION-001

| Aspect | MISSION-000 Genesis | MISSION-001 Intake |
|---|---|---|
| Starting state | Nothing exists | Code exists |
| Persona mode | DESIGN from brief | EXTRACT from code |
| Repo | Created by chain | Already exists |
| .ems/ timing | Created first | Created after intake |
| Build Governance | None to find — clean | Archaeology required |
| Technical Debt | Empty register | Populated from findings |
| First builder action | Build initial scaffold | Build against existing code |

---

## 9. After Genesis — Identical to Brownfield

Once READY status is achieved, the platform is governed identically to any brownfield platform. Every mission type is available. Every operation applies. The origin of the platform is irrelevant to all subsequent EMS activity.

---

## 10. Readiness Gates

Same 10 gates as MISSION-001. All must pass before READY.

---

## 11. Authority References

- AUTH-001 through AUTH-010 — all apply
- STD-000001 through STD-000006 — all apply

---

## 12. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Governed By | AUTH-002 | Platform Governance Authority |
| Implements | OPR-000011 | Platform Genesis Operation |
| Produces | New platform with full EMS artefact set | — |
| Produces | .ems/ folder in new repo | — |
| Updates | REG-000001 | Readiness Register |
| Updates | REG-000002 | Mission Register |
| Counterpart | MSN-000001 | MISSION-001 Platform Intake (brownfield) |

---

## 13. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — post BASELINE-1.0 | SeierTech EMS |
