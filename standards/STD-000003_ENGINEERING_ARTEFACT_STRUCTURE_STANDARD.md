# STD-000003 — ENGINEERING ARTEFACT STRUCTURE STANDARD

| Field | Value |
|---|---|
| Artefact ID | STD-000003 |
| Artefact Class | Standard |
| Title | Engineering Artefact Structure Standard |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

This standard defines the canonical structure for every artefact class in the EMS. Every file is an instance of the EngineeringArtefact base class with a specialised subclass structure. This makes the entire repository internally consistent and machine-readable by NVIDIA NIM, Kiro, Claude, and any future execution engine.

---

## 2. The EngineeringArtefact Base Class

All artefacts inherit:

```
EngineeringArtefact
├── metadata_block        (per STD-000002)
├── purpose
├── scope
├── body                  (subclass-specific)
├── dependencies
├── relationships
├── verification_method
└── change_history
```

---

## 3. Canonical Subclass Structures

### 3.1 Authority

```
Authority
├── metadata_block
├── purpose
├── scope
├── principles            (numbered list)
├── requirements          (numbered, SHALL statements)
├── responsibilities      (by role)
├── governance            (how this authority is enforced)
├── dependencies
├── produces
├── consumes
├── updates
├── related_authorities
├── related_standards
├── related_registers
├── related_operations
├── review_cycle
├── verification
└── change_history
```

### 3.2 Standard

```
Standard
├── metadata_block
├── purpose
├── scope
├── requirements          (numbered, SHALL statements)
├── quality_gates         (if applicable)
├── acceptance_criteria
├── verification_method
├── dependencies
├── relationships
└── change_history
```

### 3.3 Register

```
Register
├── metadata_block
├── purpose
├── owner
├── update_trigger
├── relationships
├── quality_rules
├── review_cycle
├── schema                (field definitions)
├── lifecycle             (entry states)
├── mandatory_fields
└── entries               (table of records)
```

### 3.4 Mission

```
Mission
├── metadata_block
├── mission_statement
├── platform              (target platform reference)
├── trigger               (what initiated this mission)
├── objectives            (numbered)
├── scope_in
├── scope_out
├── persona_assignments   (which agents are activated)
├── spine_references      (platform spine files consumed)
├── authority_references  (authorities governing this mission)
├── standard_references   (standards to be enforced)
├── acceptance_criteria
├── engineering_delivery_package_ref
├── verification_ref
├── questions_to_founder  (gaps chain cannot resolve)
├── status
└── change_history
```

### 3.5 Proposal

```
Proposal
├── metadata_block
├── mission_ref
├── problem_statement
├── proposed_approach
├── sdk_references        (if applicable)
├── alternatives_considered
├── dependencies
├── risks
├── effort_estimate
├── acceptance_criteria
├── founder_decision      (APPROVED / REJECTED / DEFERRED)
├── decision_rationale
└── change_history
```

### 3.6 Engineering Delivery Package (EDP)

```
EngineeringDeliveryPackage
├── metadata_block
├── mission_ref
├── proposal_ref
├── platform_ref
├── deliverables          (list of files/components)
├── build_instructions    (for Kiro / builder agents)
├── standards_applied
├── test_assertions       (for test agents)
├── verification_ref
├── scorecard_ref
└── change_history
```

### 3.7 Verification Report

```
VerificationReport
├── metadata_block
├── edp_ref
├── mission_ref
├── verification_method
├── gates_checked         (table: gate / result / evidence)
├── overall_result        (PASS / FAIL / CONDITIONAL)
├── findings              (list)
├── recommendations
└── change_history
```

### 3.8 Scorecard

```
Scorecard
├── metadata_block
├── mission_ref
├── verification_ref
├── dimensions            (table: dimension / score / weight / weighted_score)
├── overall_score
├── release_recommendation (RELEASE / HOLD / REJECT)
└── change_history
```

### 3.9 Decision

```
Decision
├── metadata_block
├── context
├── options_considered
├── decision
├── rationale
├── consequences
├── decision_maker
├── date
└── change_history
```

### 3.10 Platform Record

```
PlatformRecord
├── metadata_block
├── platform_name
├── repo_url
├── intake_mission_ref
├── data_model            (entities, relationships, schema)
├── tech_stack
├── use_case_register_ref
├── knowledge_graph_ref
├── current_state         (what is built, partial, missing)
├── readiness_status      (BLOCKED / IN_PROGRESS / READY)
├── readiness_gate_results (table)
├── spine/                (per-persona extraction files)
├── questions_to_founder  (unresolved gaps)
└── change_history
```

### 3.11 Persona

```
Persona
├── metadata_block
├── mission               (why this persona exists)
├── purpose
├── authority             (what this persona is authorised to do)
├── decision_rights
├── inputs
├── outputs
├── required_evidence
├── registers_read
├── registers_updated
├── authorities_governed
├── standards_governed
├── operations_participated
├── deliverables
├── success_measures
├── kpis
├── ai_reasoning_profile  (how NIM should instantiate this persona)
├── escalation_rules
├── committee_membership
└── change_history
```

### 3.12 Operation

```
Operation
├── metadata_block
├── trigger
├── preconditions
├── steps                 (numbered, each with responsible persona)
├── gates                 (decision points within the operation)
├── outputs
├── postconditions
├── escalation_path
└── change_history
```

### 3.13 Template

```
Template
├── metadata_block
├── target_class          (which artefact class this templates)
├── instructions          (for human or agent completing the template)
├── body                  (the template itself with placeholders)
└── change_history
```

---

## 4. The Full Lifecycle (from GPT EF-1 output)

```
Mission
↓
Platform Readiness
↓
Engineering Proposal
↓
Specialist Review
↓
TDA (Technical Design Authority)
↓
Approved Design
↓
Engineering Delivery Package
↓
GitHub Branch
↓
Builder (Kiro / Builder Agents)
↓
Pull Request
↓
Verification
↓
Engineering Scorecard
↓
Release Authority
↓
Merge
↓
Knowledge Capture
↓
Registers
↓
Baseline
```

---

## 5. Dependencies

- STD-000002 — Engineering Artefact Metadata Standard
- AUTH-001 — Engineering Constitution

---

## 6. Relationships

| Relationship | Artefact |
|---|---|
| Governed By | AUTH-001 |
| Required By | All EMS artefacts |
| Produces | Structural consistency across EMS |
| Enables | NIM agent reasoning, Kiro execution, automated conformance |

---

## 7. Verification Method

Structural conformance check by EMS Foundation Audit agent. Every section in the canonical subclass structure must be present in the artefact instance.

---

## 8. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1 Sprint 1.1 | SeierTech EMS |
