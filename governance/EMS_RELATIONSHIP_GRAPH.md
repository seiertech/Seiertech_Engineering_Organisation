# EMS RELATIONSHIP GRAPH

| Field | Value |
|---|---|
| Artefact ID | GOV-000001 |
| Artefact Class | Governance |
| Title | EMS Relationship Graph |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

This document defines the complete relationship graph of the SeierTech EMS. Every artefact is a node. Every declared relationship is an edge. No orphan nodes are permitted. This graph is the traceability backbone of the entire system — it enables the NIM chain to navigate the EMS, the Standards Engineer to audit completeness, and the Foundation Certification to verify integrity.

---

## 2. Graph Rules

Per STD-000005:
- Every artefact must appear as a node
- Every relationship must be declared in both directions
- No circular dependencies
- No orphan nodes — every artefact has at least one Governed By relationship
- All referenced Artefact IDs must resolve to existing files

---

## 3. Authority Layer

```
AUTH-001 Engineering Constitution
├── Governed By: [NONE — root authority]
├── Governs: ALL artefacts in EMS
├── Produces: Constitutional framework
├── Required By: AUTH-002 through AUTH-010
├── Required By: STD-000001 through STD-000005
├── Required By: All personas, missions, operations, registers

AUTH-002 Platform Governance Authority
├── Governed By: AUTH-001
├── Governs: All platform onboarding, REG-000001, OPR-000002
├── Required By: MSN-000001, All platform missions

AUTH-003 Mission Governance Authority
├── Governed By: AUTH-001
├── Governs: REG-000002, OPR-000001 through OPR-000007
├── Required By: All missions

AUTH-004 Workforce Authority
├── Governed By: AUTH-001
├── Governs: All personas in agents/
├── Required By: All persona definitions

AUTH-005 Standards Authority
├── Governed By: AUTH-001
├── Governs: STD-000001 through STD-000005
├── Required By: Standards Engineer persona

AUTH-006 Data Governance Authority
├── Governed By: AUTH-001
├── Governs: Data Model artefacts, data classification
├── Required By: Data Architect persona, all platform data artefacts

AUTH-007 Security Governance Authority
├── Governed By: AUTH-001
├── Governs: Security Posture artefacts, Risk Register
├── Required By: Security Architect persona

AUTH-008 AI Governance Authority
├── Governed By: AUTH-001
├── Governs: AI Capability Maps, NIM integration
├── Required By: AI Architect persona, integrations/NIM_INTEGRATION_CONFIG.md

AUTH-009 Release Authority
├── Governed By: AUTH-001
├── Governs: OPR-000007, REG-000006, Scorecard artefacts
├── Required By: Release Manager persona

AUTH-010 Knowledge Governance Authority
├── Governed By: AUTH-001
├── Governs: Knowledge Graph artefacts, memory/, OPR-000008
├── Required By: Knowledge Graph Architect, Documentation Curator
```

---

## 4. Standards Layer

```
STD-000001 EMS Foundation Conformance Standard
├── Governed By: AUTH-001, AUTH-005
├── Enforced By: PER-000020 Standards Engineer
├── Required By: ALL artefacts
├── Updates: REG-000005 Foundation Baseline Register

STD-000002 Engineering Artefact Metadata Standard
├── Governed By: AUTH-001, AUTH-005
├── Depends On: STD-000001
├── Required By: ALL artefacts
├── Enforced By: PER-000020 Standards Engineer

STD-000003 Engineering Artefact Structure Standard
├── Governed By: AUTH-001, AUTH-005
├── Depends On: STD-000002
├── Required By: ALL artefacts
├── Defines: 13 artefact subclass structures
├── Enforced By: PER-000020 Standards Engineer

STD-000004 Engineering Vocabulary Standard
├── Governed By: AUTH-001, AUTH-005
├── Required By: ALL artefacts and agent prompts
├── Enforced By: PER-000020 Standards Engineer

STD-000005 Traceability Standard
├── Governed By: AUTH-001, AUTH-005
├── Depends On: STD-000002
├── Required By: ALL artefacts
├── Enforced By: PER-000020 Standards Engineer
├── Defines: This relationship graph structure
```

---

## 5. Register Layer

```
REG-000001 Readiness Register
├── Governed By: AUTH-001, AUTH-002
├── Updated By: MSN-000001, OPR-000002
├── Read By: Mission Control Director, all mission chains
├── Gates: All non-intake missions

REG-000002 Mission Register
├── Governed By: AUTH-001, AUTH-003
├── Updated By: OPR-000001 (all status transitions)
├── Read By: Executive Director, Mission Control Director
├── Contains: All mission records

REG-000003 Proposal Register
├── Governed By: AUTH-001, AUTH-003
├── Updated By: OPR-000003
├── Read By: Chief Architect, Release Manager
├── Gates: EDP generation

REG-000004 Delivery Package Register
├── Governed By: AUTH-001, AUTH-003
├── Updated By: OPR-000005
├── Read By: QA & Governance Director, Release Manager
├── Gates: Verification activation

REG-000005 Foundation Baseline Register
├── Governed By: AUTH-001
├── Updated By: OPR-000009
├── Updated By: STD-000001 conformance results
├── Read By: Executive Director

REG-000006 Release Register
├── Governed By: AUTH-001, AUTH-009
├── Updated By: OPR-000007
├── Read By: Executive Director, Founder
```

---

## 6. Persona Layer

```
PER-000001 Executive Director
├── Governed By: AUTH-001, AUTH-004
├── Governs: AUTH-001 (custodian)
├── Updates: REG-000005
├── Final escalation for: All personas

PER-000002 Mission Control Director
├── Governed By: AUTH-001, AUTH-003, AUTH-004
├── Updates: REG-000002
├── Reads: REG-000001, REG-000002, REG-000004
├── Activates: All personas in intake sequence
├── Owns: OPR-000001, OPR-000002

PER-000003 Product Strategy Director
├── Governed By: AUTH-001, AUTH-004
├── Consumes: All Layer 1 persona outputs
├── Produces: Proposition Document, Value Assessment, Roadmap Scaffold
├── Leads: STRATEGIC mission type

PER-000004 Senior Business Analyst
├── Governed By: AUTH-001, AUTH-004
├── Consumes: Use Case Register
├── Produces: Requirements Register
├── Depends On: PER-000005

PER-000005 Business / Use Case Analyst
├── Governed By: AUTH-001, AUTH-004
├── Produces: Use Case Register
├── Required By: PER-000004, PER-000003, PER-000010

PER-000006 SME System User
├── Governed By: AUTH-001, AUTH-004
├── Consumes: Use Case Register
├── Produces: Operational validation verdicts
├── Enriches: Use Case Register with domain context

PER-000007 Chief Architect
├── Governed By: AUTH-001, AUTH-004
├── Produces: Architecture Document
├── Chairs: OPR-000004 TDA
├── Required By: PER-000008, PER-000024

PER-000008 Enterprise Architect
├── Governed By: AUTH-001, AUTH-004
├── Consumes: Architecture Document (from PER-000007)
├── Produces: Enterprise Architecture Context
├── Depends On: PER-000007

PER-000009 Data Architect
├── Governed By: AUTH-001, AUTH-004, AUTH-006
├── Produces: Data Model
├── Required By: PER-000010, PER-000015, PER-000024

PER-000010 Knowledge Graph Architect
├── Governed By: AUTH-001, AUTH-004, AUTH-010
├── Consumes: Data Model, Use Case Register, Architecture Document
├── Produces: Knowledge Graph, Domain Vocabulary
├── Required By: PER-000024
├── Depends On: PER-000009, PER-000005, PER-000007

PER-000011 AI Architect
├── Governed By: AUTH-001, AUTH-004, AUTH-008
├── Consumes: Architecture Document, Knowledge Graph
├── Produces: AI Capability Map
├── Leads: AGENTIC_INSERTION missions
├── Depends On: PER-000007, PER-000010

PER-000012 UI/UX Director
├── Governed By: AUTH-001, AUTH-004
├── Produces: UX Assessment
├── Reads: Use Case Register

PER-000013 Frontend Engineering Lead
├── Governed By: AUTH-001, AUTH-004
├── Produces: Frontend Engineering Assessment
├── Required By: PER-000017, PER-000024

PER-000014 Backend Engineering Lead
├── Governed By: AUTH-001, AUTH-004
├── Produces: Backend Engineering Assessment
├── Required By: PER-000021, PER-000017, PER-000024

PER-000015 Security Architect
├── Governed By: AUTH-001, AUTH-004, AUTH-007
├── Consumes: Data Model, Deployment Architecture
├── Produces: Security Posture Document
├── Updates: Risk Register
├── Depends On: PER-000009, PER-000022

PER-000016 QA & Governance Director
├── Governed By: AUTH-001, AUTH-004
├── Produces: Test Strategy, Verification Report
├── Owns: OPR-000006
├── Gates: Release (VER must exist)

PER-000017 Technical Debt Auditor
├── Governed By: AUTH-001, AUTH-004
├── Consumes: All Layer 1 outputs
├── Produces: Technical Debt Register
├── Required By: PER-000024

PER-000018 Documentation & Knowledge Curator
├── Governed By: AUTH-001, AUTH-004, AUTH-010
├── Produces: Documentation Assessment
├── Updates: memory/ after every mission
├── Owns: OPR-000008

PER-000019 Release Manager
├── Governed By: AUTH-001, AUTH-004, AUTH-009
├── Produces: Scorecard
├── Updates: REG-000006
├── Owns: OPR-000007
├── Gates: Merge to main

PER-000020 Standards Engineer
├── Governed By: AUTH-001, AUTH-004, AUTH-005
├── Enforces: STD-000001 through STD-000005
├── Gates: Every artefact in intake and every EDP
├── Updates: REG-000001 (gate results), REG-000005
├── Required By: ALL artefacts

PER-000021 Integration Engineer
├── Governed By: AUTH-001, AUTH-004
├── Produces: Integration Map, API Register
├── Required By: PER-000007, PER-000015, PER-000011

PER-000022 Platform Engineer
├── Governed By: AUTH-001, AUTH-004
├── Produces: Deployment Architecture
├── Required By: PER-000015, PER-000024

PER-000023 Proposition Analyst
├── Governed By: AUTH-001, AUTH-004
├── Consumes: ALL Layer 1 outputs
├── Produces: Proposition Document, Value Assessment, Roadmap Scaffold
├── Required By: PER-000024
├── Depends On: ALL Layer 1 personas

PER-000024 Master Spec Author
├── Governed By: AUTH-001, AUTH-004
├── Consumes: ALL intake outputs (Layers 1, 2, 3)
├── Produces: Master Technical Specification
├── Updates: REG-000001 (final READY trigger)
├── Required By: ALL platform missions (MTS is primary reference)
├── Depends On: ALL preceding personas
```

---

## 7. Mission Layer

```
MSN-000001 MISSION-001 Platform Intake
├── Governed By: AUTH-001, AUTH-002, AUTH-003
├── Implements: OPR-000002
├── Activates: All 24 personas in sequence
├── Produces: 24+ artefacts in platforms/[NAME]/
├── Updates: REG-000001, REG-000002
├── Required By: All platform missions (must complete first)
├── Gated By: Standards Engineer (after every artefact)
```

---

## 8. Operation Layer

```
OPR-000001 Mission Lifecycle Operation
├── Governed By: AUTH-003
├── Owned By: PER-000002 Mission Control Director
├── Contains: OPR-000002 through OPR-000009
├── Updates: REG-000002

OPR-000002 Platform Intake Operation
├── Governed By: AUTH-002, AUTH-003
├── Implements: MSN-000001
├── Updates: REG-000001, REG-000002
├── Activates: All 24 personas

OPR-000003 Engineering Proposal Operation
├── Governed By: AUTH-003
├── Updates: REG-000003
├── Produces: Engineering Proposal (PRP-NNNNNN)
├── Followed By: OPR-000004

OPR-000004 Technical Design Authority
├── Governed By: AUTH-003
├── Chaired By: PER-000007 Chief Architect
├── Follows: OPR-000003
├── Followed By: OPR-000005

OPR-000005 Engineering Delivery Operation
├── Governed By: AUTH-003
├── Produces: EDP in work-products/
├── Updates: REG-000004
├── Followed By: OPR-000006

OPR-000006 Verification Operation
├── Governed By: AUTH-003
├── Owned By: PER-000016 QA & Governance Director
├── Produces: Verification Report (VER-NNNNNN)
├── Followed By: OPR-000007

OPR-000007 Release Operation
├── Governed By: AUTH-003, AUTH-009
├── Owned By: PER-000019 Release Manager
├── Produces: Scorecard (SCR-NNNNNN)
├── Updates: REG-000006
├── Followed By: OPR-000008

OPR-000008 Knowledge Capture Operation
├── Governed By: AUTH-010
├── Owned By: PER-000018 Documentation Curator
├── Updates: memory/, Knowledge Graph, MTS, Technical Debt Register
├── Closes: GitHub Issue
├── Followed By: OPR-000009 (if baseline triggered)

OPR-000009 Baseline Operation
├── Governed By: AUTH-001
├── Owned By: PER-000001 Executive Director
├── Updates: REG-000005
├── Produces: Git baseline tag
```

---

## 9. Integration Layer

```
integrations/NIM_INTEGRATION_CONFIG.md
├── Governed By: AUTH-001, AUTH-008
├── Required By: .github/workflows/ems-mission-chain.yml
├── Consumes: All mission chains

.github/workflows/ems-mission-chain.yml
├── Governed By: AUTH-001, AUTH-003
├── Triggered By: GitHub Issues
├── Implements: Mission detection and routing
├── Calls: NIM API per NIM_INTEGRATION_CONFIG
├── Produces: Mission chain execution
```

---

## 10. Template Layer

```
TPL-000001 Platform Intake Template → Target: Platform Record
TPL-000002 Mission Template → Target: Mission artefacts
TPL-000003 Proposal Template → Target: Engineering Proposals
TPL-000004 Engineering Delivery Package Template → Target: EDPs
TPL-000005 Verification Report Template → Target: Verification Reports
TPL-000006 Scorecard Template → Target: Scorecards
TPL-000007 Decision Template → Target: Decisions
TPL-000008 Persona Template → Target: Persona definitions
TPL-000009 Authority Template → Target: Authorities
TPL-000010 Register Template → Target: Registers

All templates:
├── Governed By: AUTH-001
├── Conform To: STD-000002, STD-000003, STD-000004, STD-000005
├── Required By: Respective artefact creation processes
```

---

## 11. Orphan Audit

The following artefact groups exist in the repo but require relationship declaration updates as authorities are built in Sprint EF-1.2:

| Group | Status | Blocker |
|---|---|---|
| AUTH-001 through AUTH-010 | PENDING | EF-1.2 sprint in progress (GPT) |
| Templates TPL-000006 through TPL-000010 | PENDING | EF-1.6 sprint in progress (GPT) |
| platforms/ | EMPTY | No platforms onboarded yet — awaiting MISSION-001 |
| memory/ | EMPTY | Populated by OPR-000008 after first mission completes |
| work-products/ | EMPTY | Populated by OPR-000005 after first EDP |
| libraries/ | EMPTY | Populated as reusable patterns emerge from missions |

None of the above constitute orphans — they are pending population. Orphan status applies only to artefacts that exist but have no declared relationships.

---

## 12. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Depends On | STD-000005 | Traceability Standard |
| Maps | All EMS artefacts | Complete relationship graph |
| Required By | REG-000005 | Foundation Baseline Register (certification input) |
| Required By | PER-000020 | Standards Engineer (orphan audit) |

---

## 13. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1.7 | SeierTech EMS |


---

## 14. Post-BASELINE-1.0 Additions

The following artefacts were added after BASELINE-1.0 certification:

### New Standards
```
STD-000006 Platform Baseline Sync Standard
├── Governed By: AUTH-001, AUTH-002
├── Defines: .ems/ folder structure and contents
├── Required By: OPR-000010, OPR-000011
├── Required By: PER-000025 Build Governance Auditor
├── Required By: All builders (kiro-sync/ compliance)
```

### New Registers
```
REG-000007 Build Governance Register
├── Governed By: AUTH-001
├── Owned By: PER-000025 Build Governance Auditor
├── Updated By: MSN-000000, MSN-000001, OPR-000010, OPR-000008
├── Required By: STD-000006
├── Stored In: .ems/governance/ per platform
```

### New Persona
```
PER-000025 Build Governance Auditor
├── Governed By: AUTH-001, AUTH-004, STD-000006
├── Produces: REG-000007 Build Governance Register
├── Produces: .ems/kiro-sync/ (builder instruction set)
├── Produces: .ems/governance/ folder
├── Activates In: MISSION-001 Phase 2b, OPR-000010, OPR-000008
├── Solves: Governance drift problem permanently
```

### New Operations
```
OPR-000010 Platform Baseline Sync Operation
├── Governed By: AUTH-002, STD-000006
├── Triggered By: MSN-000001 Phase 7 (after READY)
├── Uses: PER-000025 Build Governance Auditor
├── Produces: .ems/ folder in platform repo
├── Updates: REG-000001, REG-000007
├── Installs: Continuous sync GitHub Action in platform repo

OPR-000011 Platform Genesis Operation
├── Governed By: AUTH-002, AUTH-003, STD-000006
├── Implements: MSN-000000 MISSION-000
├── Creates: GitHub repository from scratch
├── Creates: .ems/ folder before application code
├── Activates: All 25 personas in GENESIS MODE
├── Produces: Full platform artefact set (designed not extracted)
├── Assigns: Builder to governed platform
```

### New Mission
```
MSN-000000 MISSION-000 Platform Genesis
├── Governed By: AUTH-001, AUTH-002, AUTH-003
├── Implements: OPR-000011
├── Counterpart: MSN-000001 MISSION-001 (brownfield)
├── Trigger: GitHub Issue: "Genesis: [NAME] — [brief]"
├── Mode: GENESIS — all personas design forward from intent
├── Creates: New GitHub repository
├── Produces: Full EMS artefact set (designed)
├── Produces: .ems/ folder (before application code)
├── Updates: REG-000001, REG-000002
```

### Updated Missions
```
MSN-000001 MISSION-001 Platform Intake v3.0
├── Added: Phase 7 — triggers OPR-000010 after readiness gates pass
├── Added: PER-000025 Build Governance Auditor in Phase 2b
├── .ems/ folder now established as part of every brownfield intake
```

### The Two-Origin Model
```
BROWNFIELD → MSN-000001 → OPR-000002 (extract) → OPR-000010 (sync) → .ems/ → READY
GREENFIELD → MSN-000000 → OPR-000011 (design) → .ems/ first → builder assigned → READY
Both → identical READY state → all subsequent missions identical
```
