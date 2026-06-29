# SEIERTECH EMS — AGENT PERSONA REGISTRY

| Field | Value |
|---|---|
| Document | Agent Persona Registry |
| Status | ACTIVE |
| Version | 2.0.0 |
| Baseline | BASELINE-1.0 |
| Last Updated | 2026-06-29 |

---

## Purpose

This registry defines all 24 agent personas active in the SeierTech EMS. Every persona is an AI reasoning role instantiated by NVIDIA NIM during mission execution. Each persona has defined scope, authority, inputs, outputs, and an AI Reasoning Profile that governs how NIM instantiates it.

---

## Intake Sequence

The intake sequence defines the order in which personas activate during MISSION-001 Platform Intake:

### Layer 1 — Discovery & Creation (run in parallel where possible)

| Order | Persona | Primary Intake Output |
|---|---|---|
| 1 | Use Case Analyst | Use Case Register |
| 2 | Data Architect | Data Model |
| 3 | Integration Engineer | Integration Map + API Register |
| 4 | Platform Engineer | Deployment Architecture |
| 5 | Chief Architect | Architecture Document |
| 6 | Enterprise Architect | Enterprise Architecture Context |
| 7 | Security Architect | Security Posture + Risk Register |
| 8 | Frontend Engineering Lead | Frontend Assessment |
| 9 | Backend Engineering Lead | Backend Assessment |
| 10 | UI/UX Director | UX Assessment |
| 11 | AI Architect | AI Capability Map |
| 12 | Knowledge Graph Architect | Knowledge Graph + Domain Vocabulary |
| 13 | SME System User | Operational validation of use cases |
| 14 | Senior Business Analyst | Requirements Register |
| 15 | Technical Debt Auditor | Technical Debt Register |
| 16 | QA & Governance Director | Test Strategy |
| 17 | Documentation & Knowledge Curator | Documentation Assessment |

**Standards Engineer runs after EVERY persona above — conformance gate before proceeding**

### Layer 2 — Engineering Documentation

| Order | Persona | Primary Intake Output |
|---|---|---|
| 18 | Mission Control Director | Mission Register update |

### Layer 3 — Synthesis (run after all Layer 1 complete)

| Order | Persona | Primary Intake Output |
|---|---|---|
| 19 | Proposition Analyst | Proposition Document + Value Assessment + Roadmap Scaffold |
| 20 | Master Spec Author | Master Technical Specification |

**Standards Engineer runs after Layer 3 — final conformance gate**

**Executive Director** — final sign-off on intake package before READY

---

## Governance Personas (not in intake sequence)

| Persona | Role |
|---|---|
| Executive Director | Constitutional authority — escalation terminus |
| Mission Control Director | Mission lifecycle and routing |
| Release Manager | Release readiness and scorecard |
| Product Strategy Director | Strategic mission lead |

---

## Full Persona Register

| ID | Number | Title | Intake Layer | Status |
|---|---|---|---|---|
| PER-000001 | 00 | Executive Director | Governance | ACTIVE |
| PER-000002 | 01 | Mission Control Director | Governance | ACTIVE |
| PER-000003 | 02 | Product Strategy Director | Governance | ACTIVE |
| PER-000004 | 03 | Senior Business Analyst | Layer 1 | ACTIVE |
| PER-000005 | 04 | Business / Use Case Analyst | Layer 1 | ACTIVE |
| PER-000006 | 05 | SME System User | Layer 1 | ACTIVE |
| PER-000007 | 06 | Chief Architect | Layer 1 | ACTIVE |
| PER-000008 | 07 | Enterprise Architect | Layer 1 | ACTIVE |
| PER-000009 | 08 | Data Architect | Layer 1 | ACTIVE |
| PER-000010 | 09 | Knowledge Graph Architect | Layer 1 | ACTIVE |
| PER-000011 | 10 | AI Architect | Layer 1 | ACTIVE |
| PER-000012 | 11 | UI / UX Director | Layer 1 | ACTIVE |
| PER-000013 | 12 | Frontend Engineering Lead | Layer 1 | ACTIVE |
| PER-000014 | 13 | Backend Engineering Lead | Layer 1 | ACTIVE |
| PER-000015 | 14 | Security Architect | Layer 1 | ACTIVE |
| PER-000016 | 15 | QA & Governance Director | Layer 1 | ACTIVE |
| PER-000017 | 16 | Technical Debt Auditor | Layer 1 | ACTIVE |
| PER-000018 | 17 | Documentation & Knowledge Curator | Layer 1 | ACTIVE |
| PER-000019 | 18 | Release Manager | Governance | ACTIVE |
| PER-000020 | 19 | Standards Engineer | Gate (all layers) | ACTIVE |
| PER-000021 | 20 | Integration Engineer | Layer 1 | ACTIVE |
| PER-000022 | 21 | Platform Engineer | Layer 1 | ACTIVE |
| PER-000023 | 22 | Proposition Analyst | Layer 3 | ACTIVE |
| PER-000024 | 23 | Master Spec Author | Layer 3 | ACTIVE |
| PER-000025 | 24 | Build Governance Auditor | Layer 1 (Phase 2b) | ACTIVE |
| PER-000020 | 19 | Standards Engineer | Gate (all layers) | ACTIVE |
| PER-000021 | 20 | Integration Engineer | Layer 1 | ACTIVE |
| PER-000022 | 21 | Platform Engineer | Layer 1 | ACTIVE |
| PER-000023 | 22 | Proposition Analyst | Layer 3 | ACTIVE |
| PER-000024 | 23 | Master Spec Author | Layer 3 | ACTIVE |

---

## Mission Types Served

| Mission | Description | All Personas Mode |
|---|---|---|
| MISSION-000 Platform Genesis | Greenfield — design forward from brief | GENESIS MODE |
| MISSION-001 Platform Intake | Brownfield — extract from existing code | EXTRACT MODE |
| All other missions | Build, Rehab, Strategic, Agentic etc | EXECUTE MODE |

Every persona AI Reasoning Profile contains both EXTRACT and GENESIS mode instructions.


---

## Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Consumed By | MSN-000001 | MISSION-001 Platform Intake |
| Consumed By | All missions | Every mission activates relevant personas |

---

## Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-01 | Initial stub registry | SeierTech EMS |
| 2.0.0 | 2026-06-29 | Full EF-1.4 rewrite — 24 personas, full intake sequence | SeierTech EMS |
| 3.0.0 | 2026-06-29 | Added PER-000025 Build Governance Auditor, genesis mode all personas, MISSION-000 | SeierTech EMS |
