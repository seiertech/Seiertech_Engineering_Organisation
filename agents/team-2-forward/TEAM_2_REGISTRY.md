# TEAM 2 — FORWARD BUILD FORCE

| Field | Value |
|---|---|
| Team | Team 2 |
| Designation | Forward Build Force |
| Status | ACTIVE |
| Activation | After Team 1 handoff (brownfield) or from day one (greenfield) |
| Operates | All forward missions — BUILD, REHAB, STRATEGIC, AGENTIC_INSERTION, SPEC, PROPOSAL |
| Baseline | BASELINE-1.0 |

---

## Purpose

Team 2 builds the platform forward. They activate after Team 1 delivers the handoff artefact and the clean EMS baseline is established. They reason exclusively against the MTS, spine, and clean EMS artefacts — never against the old platform state.

Team 2 is the permanent operational force. They never stand down.

---

## The Foundational Rule

**Team 2 never looks backward. The Handoff Artefact and MTS are the starting point. Always.**

Every Team 2 persona reads the MTS before activating. Every Team 2 persona references the clean EMS baseline artefacts. The old platform codebase is archaeology — Team 1 dealt with it. Team 2 builds forward from the clean baseline.

---

## Activation Triggers

| Trigger | Description |
|---|---|
| Brownfield | Team 1 handoff complete — HAR produced and signed off |
| Greenfield | MISSION-000 genesis complete — Team 2 built the baseline themselves |
| Mission types | BUILD, REHAB, STRATEGIC, AGENTIC_INSERTION, SPEC, PROPOSAL |

---

## Team 2 Persona Register

| # | ID | Persona | Primary Forward Role |
|---|---|---|---|
| 00 | T2-PER-000001 | Executive Director | Forward constitutional authority |
| 01 | T2-PER-000002 | Mission Control Director | Forward mission orchestration |
| 02 | T2-PER-000003 | Product Strategy Director | Strategic direction and STRATEGIC missions |
| 03 | T2-PER-000004 | Senior Business Analyst | Forward requirements and acceptance criteria |
| 04 | T2-PER-000005 | Business / Use Case Analyst | Use case register maintenance |
| 05 | T2-PER-000006 | SME System User | Operational validation of outputs |
| 06 | T2-PER-000007 | Chief Architect | TDA chair and architectural integrity |
| 07 | T2-PER-000008 | Enterprise Architect | Portfolio coherence |
| 08 | T2-PER-000009 | Data Architect | Forward data model evolution |
| 09 | T2-PER-000010 | Knowledge Graph Architect | Knowledge graph maintenance |
| 10 | T2-PER-000011 | AI Architect | AGENTIC_INSERTION missions lead |
| 11 | T2-PER-000012 | UI / UX Director | Forward UX design |
| 12 | T2-PER-000013 | Frontend Engineering Lead | Frontend build quality |
| 13 | T2-PER-000014 | Backend Engineering Lead | Backend build quality |
| 14 | T2-PER-000015 | Security Architect | Forward security governance |
| 15 | T2-PER-000016 | Verification and Governance Director | Verification chair |
| 16 | T2-PER-000017 | Technical Debt Auditor | Debt reduction — REHAB missions |
| 17 | T2-PER-000018 | Documentation and Knowledge Curator | Knowledge Capture — every mission |
| 18 | T2-PER-000019 | Release Manager | Release gate — every mission |
| 19 | T2-PER-000020 | Standards Engineer | Conformance gate — every output |
| 20 | T2-PER-000021 | Integration Engineer | Forward integration design |
| 21 | T2-PER-000022 | Platform Engineer | Forward infrastructure design |
| 22 | T2-PER-000023 | Proposition Analyst | Proposition evolution tracking |
| 23 | T2-PER-000024 | Master Spec Author | MTS currency maintenance |
| 24 | T2-PER-000025 | Build Governance Auditor | Governance hygiene — prevent drift returning |

---

## Forward Mission Routing

| Mission Type | Lead Persona | Supporting Personas |
|---|---|---|
| BUILD | Chief Architect (TDA) | Relevant engineering leads, Security, Verification, Release |
| REHAB | Technical Debt Auditor | Chief Architect, Engineering Leads, Verification |
| STRATEGIC | Product Strategy Director | AI Architect, Use Case Analyst, Proposition Analyst |
| AGENTIC_INSERTION | AI Architect | Chief Architect, Backend Lead, Security, Verification |
| SPEC | Master Spec Author | Chief Architect, Data Architect, Integration Engineer |
| PROPOSAL | Product Strategy Director | Chief Architect, AI Architect, Senior Business Analyst |

Standards Engineer and Release Manager activate on every mission.
Documentation Curator executes Knowledge Capture on every mission.
Build Governance Auditor runs hygiene check on every mission.

---

## What Team 2 Reads

Before every mission, the chain injects:

1. AUTH-001 Engineering Constitution
2. STD-000004 Vocabulary Standard
3. Relevant Team 2 persona definition
4. Platform MTS (full or summary)
5. Relevant spine files for this persona
6. Handoff Artefact (confidence levels and open items)
7. Mission instruction

---

## Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Governed By | AUTH-004 | Workforce Authority |
| Receives From | HAR-[PLATFORM]-001 | Platform Handoff Artefact |
| Counterpart | agents/team-1-baseline/ | Team 1 Baseline Establishment Force |
| Operates Against | platforms/[NAME]/MASTER_TECHNICAL_SPECIFICATION.md | Primary reference |

---

## Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — Team 2 Forward Build Force | SeierTech EMS |
