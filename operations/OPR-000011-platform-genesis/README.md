# OPR-000011 — PLATFORM GENESIS OPERATION

| Field | Value |
|---|---|
| Artefact ID | OPR-000011 |
| Artefact Class | Operation |
| Title | Platform Genesis Operation |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | Mission Control Director |
| Approval Authority | AUTH-002 Platform Governance Authority |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Define the greenfield platform creation process — building a new platform from nothing but a brief. Unlike intake which reads backward from existing code, genesis designs forward from intent. The .ems/ folder is created first, before any application code. Every artefact is designed not extracted. The builder is assigned to a clean, governed, doctrine-bound repo from day one.

---

## 2. Trigger

GitHub Issue containing: `Genesis: [PLATFORM_NAME] — [brief]`

Example: `Genesis: COMPASS — personal growth operating system for consumer mobile`

---

## 3. Preconditions

- EMS at BASELINE-1.0 or above
- NIM API key active
- GitHub token available for repo creation
- Platform name not already in REG-000001

---

## 4. Steps

### Phase 1 — Mission Activation

| Step | Action | Persona | Gate |
|---|---|---|---|
| 1.1 | Parse issue — extract platform name and brief | Mission Control Director | — |
| 1.2 | Create mission record in REG-000002 | Mission Control Director | — |
| 1.3 | Label GitHub Issue: mission:genesis, status:in-progress | Mission Control Director | — |
| 1.4 | Create platform entry in REG-000001 — status: IN_PROGRESS | Mission Control Director | — |

### Phase 2 — Brief Expansion

| Step | Action | Persona | Gate |
|---|---|---|---|
| 2.1 | Executive Director reviews brief for constitutional alignment | Executive Director | Brief valid |
| 2.2 | Product Strategy Director expands brief into platform proposition | Product Strategy Director | — |
| 2.3 | Business/Use Case Analyst derives initial use cases from brief | Use Case Analyst | — |
| 2.4 | SME System User validates use cases from operational perspective | SME System User | — |
| 2.5 | Senior Business Analyst formalises requirements from use cases | Senior Business Analyst | — |
| 2.6 | Standards Engineer assesses all Phase 2 outputs | Standards Engineer | PASS |
| 2.7 | Questions to Founder posted if brief insufficient for full expansion | Mission Control Director | — |

### Phase 3 — Architecture Design

| Step | Action | Persona | Gate |
|---|---|---|---|
| 3.1 | Chief Architect designs system architecture from brief and use cases | Chief Architect | — |
| 3.2 | Data Architect designs data model from use cases and requirements | Data Architect | — |
| 3.3 | Integration Engineer designs integration map from use cases | Integration Engineer | — |
| 3.4 | Platform Engineer designs deployment architecture | Platform Engineer | — |
| 3.5 | Enterprise Architect defines portfolio context | Enterprise Architect | — |
| 3.6 | Security Architect designs security architecture | Security Architect | — |
| 3.7 | Frontend Engineering Lead designs frontend architecture | Frontend Engineering Lead | — |
| 3.8 | Backend Engineering Lead designs backend architecture | Backend Engineering Lead | — |
| 3.9 | UI/UX Director designs UX framework | UI/UX Director | — |
| 3.10 | AI Architect designs AI capability map from use cases | AI Architect | — |
| 3.11 | Knowledge Graph Architect designs knowledge graph from data model + use cases | Knowledge Graph Architect | — |
| 3.12 | QA Governance Director designs test strategy | QA Governance Director | — |
| 3.13 | Technical Debt Auditor creates empty Technical Debt Register | Technical Debt Auditor | — |
| 3.14 | Documentation Curator creates documentation framework | Documentation Curator | — |
| 3.15 | Standards Engineer assesses ALL Phase 3 outputs | Standards Engineer | ALL PASS |

### Phase 4 — Repo Creation

| Step | Action | Persona | Gate |
|---|---|---|---|
| 4.1 | Create GitHub repository: [PLATFORM_NAME] | Mission Control Director | All Phase 3 PASS |
| 4.2 | Create .ems/ folder structure per STD-000006 | Mission Control Director | Repo created |
| 4.3 | Write .ems/PLATFORM_BASELINE.md | Mission Control Director | — |
| 4.4 | Write .ems/BASELINE_MANIFEST.md | Mission Control Director | — |
| 4.5 | Write all spine files to .ems/spine/ | All Layer 1 personas | — |
| 4.6 | Create empty .ems/governance/BUILD_GOVERNANCE_REGISTER.md | Build Governance Auditor | — |
| 4.7 | Write .ems/governance/ACTIVE_STANDARDS.md | Build Governance Auditor | — |
| 4.8 | Write .ems/kiro-sync/MEMORY.md from EMS doctrine + designed artefacts | Build Governance Auditor | — |
| 4.9 | Write .ems/kiro-sync/RULES.md from EMS standards | Build Governance Auditor | — |
| 4.10 | Write .ems/kiro-sync/STANDARDS.md from EMS standards | Build Governance Auditor | — |
| 4.11 | Create repo folder structure per architecture design | Chief Architect | — |
| 4.12 | Add GitHub Actions: ems-mission-chain.yml + ems-sync.yml | Mission Control Director | — |
| 4.13 | Standards Engineer validates .ems/ folder per STD-000006 | Standards Engineer | PASS |

### Phase 5 — Synthesis

| Step | Action | Persona | Gate |
|---|---|---|---|
| 5.1 | Proposition Analyst produces Proposition Document from designed artefacts | Proposition Analyst | All Phase 3 PASS |
| 5.2 | Proposition Analyst produces Platform Value Assessment (projected) | Proposition Analyst | — |
| 5.3 | Proposition Analyst produces Product Roadmap (full — greenfield has no PARTIAL/MISSING) | Proposition Analyst | — |
| 5.4 | Master Spec Author produces Master Technical Specification | Master Spec Author | All outputs ready |
| 5.5 | Write MTS to .ems/MASTER_TECHNICAL_SPECIFICATION.md | Master Spec Author | — |
| 5.6 | Standards Engineer assesses MTS | Standards Engineer | PASS |

### Phase 6 — Builder Assignment

| Step | Action | Persona | Gate |
|---|---|---|---|
| 6.1 | Produce first Engineering Delivery Package — initial scaffold build | Chief Architect + NIM Chain | MTS approved |
| 6.2 | EDP defines: repo structure, initial files, foundational components | Chief Architect | — |
| 6.3 | Standards Engineer assesses EDP | Standards Engineer | PASS |
| 6.4 | Register EDP in REG-000004 | Mission Control Director | — |
| 6.5 | Assign builder: Kiro or builder agent | Mission Control Director | Founder approval |
| 6.6 | Builder reads .ems/kiro-sync/ and executes first EDP | Builder | — |
| 6.7 | Initial scaffold committed to platform repo | Builder | — |

### Phase 7 — Readiness Certification

| Step | Action | Persona | Gate |
|---|---|---|---|
| 7.1 | Check all 10 readiness gates | Mission Control Director | All PASS |
| 7.2 | Executive Director reviews genesis package | Executive Director | Sign-off |
| 7.3 | Set platform to READY in REG-000001 | Mission Control Director | — |
| 7.4 | Update REG-000002 — mission COMPLETE | Mission Control Director | — |
| 7.5 | Close GitHub Issue with genesis summary | Mission Control Director | — |
| 7.6 | Platform is operational — missions may now fire | — | — |

---

## 5. Key Differences from Brownfield Intake

| Aspect | Brownfield (MISSION-001) | Greenfield (MISSION-000) |
|---|---|---|
| Repo exists | Yes | No — created by this operation |
| Code exists | Yes | No |
| Governance exists | Yes — archaeology needed | No — clean slate |
| .ems/ creation timing | After intake (OPR-000010) | During genesis (this operation) |
| Persona mode | EXTRACT from code | DESIGN from brief |
| Data Model source | Extracted from schema | Designed from use cases |
| Architecture source | Reverse engineered | Forward designed |
| Technical Debt Register | Populated from findings | Empty — clean start |
| kiro-sync/ content | Reconciled existing + EMS | EMS doctrine only |
| First builder action | Builds against existing code | Builds initial scaffold |

---

## 6. The .ems/ First Principle

In greenfield genesis, `.ems/` is created before any application code. This is non-negotiable. The builder's first action is to read `.ems/kiro-sync/` — not to make architectural decisions, not to choose a framework, not to write a README. EMS doctrine comes first. Always.

---

## 7. Outputs

- New GitHub repository
- .ems/ folder (complete per STD-000006)
- Full artefact set (same as brownfield intake)
- First EDP produced and executed — initial scaffold in repo
- Platform at READY
- Builder assigned and synced to EMS doctrine

---

## 8. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-002 | Platform Governance Authority |
| Governed By | AUTH-003 | Mission Governance Authority |
| Governed By | STD-000006 | Platform Baseline Sync Standard |
| Implements | MSN-000000 | MISSION-000 Platform Genesis |
| Activates | All 25 personas | Genesis sequence |
| Produces | New governed platform | — |
| Updates | REG-000001 | Readiness Register |
| Updates | REG-000002 | Mission Register |

---

## 9. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — post BASELINE-1.0 | SeierTech EMS |
