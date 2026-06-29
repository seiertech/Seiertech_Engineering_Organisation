# STD-000004 — ENGINEERING VOCABULARY STANDARD

| Field | Value |
|---|---|
| Artefact ID | STD-000004 |
| Artefact Class | Standard |
| Title | Engineering Vocabulary Standard |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

This standard is the single source of truth for all engineering terminology used within the SeierTech EMS. No synonyms are permitted. Every agent, persona, mission, and artefact uses these terms exclusively. This enables unambiguous machine reasoning across the entire loop.

---

## 2. Scope

Applies to all written artefacts, agent prompts, mission instructions, NIM chain calls, and human communications within the EMS.

---

## 3. Core Vocabulary

| Term | Definition | Do Not Use |
|---|---|---|
| Engineering Delivery Package (EDP) | The structured build instruction set produced by the mission chain and consumed by the builder agent or Kiro | Build Pack, Build File, Build Bundle |
| Mission | A formally issued instruction to the EMS chain to perform a defined engineering objective | Task, Ticket, Job, Request |
| Mission Chain | The sequence of agent calls, NIM reasoning steps, and outputs that execute a mission from instruction to EDP | Pipeline, Workflow, Process |
| Platform | A software product or system onboarded to the EMS and governed by its authorities and standards | App, Application, Service, System (unless referring to a specific layer) |
| Platform Record | The complete structured knowledge object describing a platform's state, data model, tech stack, spine, and readiness | Platform Profile, Platform Doc |
| Platform Spine | The per-persona extracted knowledge base built during platform intake, enabling all subsequent missions | Context, Knowledge Base, Platform Context |
| Agent Persona | A specialised AI reasoning role with defined scope, inputs, outputs, and authorities, instantiated by NIM during mission execution | Agent, Bot, AI, Role |
| Authority | A constitutional doctrine document that defines controlling rules and principles for a domain of engineering | Policy, Rule, Guideline, Principle Document |
| Standard | A detailed engineering expectation derived from an authority, against which artefacts and work products are verified | Rule, Requirement, Spec (unless referring to a specification artefact) |
| Register | An indexed, structured record of engineering objects of a given type, maintained as a live source of truth | List, Log, Tracker, Database |
| Operation | A defined engineering process with steps, gates, responsible personas, and outcomes | Process, Procedure, Workflow, Method |
| Verification | The act of checking an artefact or work product against defined criteria and producing a formal result | Testing, Review, QA, Check (informal) |
| Verification Report | The formal output of a verification activity | Test Report, QA Report, Review Output |
| Scorecard | The structured quality assessment of a mission's outputs used by Release Authority to make a release decision | Report Card, Assessment, Evaluation |
| Baseline | A formally tagged state of the EMS repository representing a certified milestone | Release, Version, Snapshot |
| Readiness Gate | A pass/fail criterion that must be satisfied before a platform can receive missions | Gate, Checkpoint, Threshold |
| Mission Spine | The pre-loaded, persona-specific knowledge base extracted during intake that every mission draws from | Context Package, Knowledge Load |
| Loop Engineering | The SeierTech engineering methodology — a closed-loop autonomous engineering system where doctrine governs agents, agents execute missions, missions produce builds, builds get tested, and the loop tightens over time | Agentic Engineering, AI Engineering, Automated Engineering |
| Founder | The principal human authority of the SeierTech EMS who issues missions, approves proposals, and resolves questions the chain cannot determine autonomously | User, Owner, Admin |
| NIM | NVIDIA Inference Microservices — the model execution layer powering the EMS mission chain | AI, Model, LLM (in operational context) |
| Kiro | The current build executor that receives EDPs and produces code | Builder, Executor (when Kiro is specifically meant) |
| Builder Agent | An autonomous agent that executes EDPs to produce code, replacing or supplementing Kiro as the agent army matures | Kiro (when referring to future agent-native execution) |
| TDA | Technical Design Authority — the governance gate where proposed designs are reviewed and approved before an EDP is produced | Design Review, Architecture Review |
| Knowledge Graph | The structured semantic model of a platform's domain, entities, relationships, and concepts built during intake | Data Model (when referring to semantics beyond schema), Ontology |
| Intake | The MISSION-001 process that onboards a platform to the EMS by reading its repo, building the platform record, extracting the spine, and satisfying readiness gates | Onboarding, Setup, Initialisation |

---

## 4. Prohibited Terms

The following terms are prohibited within the EMS because they are ambiguous, overloaded, or introduce synonyms that break machine reasoning:

- Build Pack (use: Engineering Delivery Package)
- Build File (use: Engineering Delivery Package)
- Task (use: Mission)
- Ticket (use: Mission or GitHub Issue)
- Bot (use: Agent Persona)
- Policy (use: Authority)
- Guideline (use: Standard or Authority)
- Snapshot (use: Baseline)
- QA (use: Verification)
- Checklist (use: Quality Gates or Verification criteria)

---

## 5. Naming Conventions

| Object | Convention | Example |
|---|---|---|
| File names | UPPER_SNAKE_CASE with prefix | STD-000001_EMS_FOUNDATION_CONFORMANCE_STANDARD.md |
| Artefact IDs | PREFIX-NNNNNN | MSN-000001 |
| Folder names | lowercase-kebab | work-products |
| Platform names | UPPER_SNAKE_CASE | COMMANDER_C2 |
| Persona names | Title Case with role suffix | Architecture Engineer Persona |

---

## 6. Dependencies

- AUTH-001 — Engineering Constitution

---

## 7. Relationships

| Relationship | Artefact |
|---|---|
| Governed By | AUTH-001 |
| Required By | All EMS artefacts and agent prompts |
| Produces | Unambiguous language across the EMS |
| Enables | Precise NIM reasoning, consistent agent outputs |

---

## 8. Verification Method

Vocabulary audit by Standards Engineer persona. Scan all artefacts for prohibited terms. Flag synonyms for correction.

---

## 9. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1 Sprint 1.1 | SeierTech EMS |
