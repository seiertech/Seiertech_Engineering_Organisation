# AUTH-010 — KNOWLEDGE GOVERNANCE AUTHORITY

| Field | Value |
|---|---|
| Artefact ID | AUTH-010 |
| Artefact Class | Authority |
| Title | Knowledge Governance Authority |
| Status | ACTIVE |
| Version | 1.1.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

This authority governs all knowledge artefacts within the SeierTech EMS — knowledge graphs, domain vocabularies, memory layers, documentation, and organisational learning. Knowledge is infrastructure. Every mission must leave the system more knowledgeable than it found it.

---

## 2. Scope

Applies to all knowledge artefacts across all platforms and the EMS memory layer.

---

## 3. Principles

- KNW-001 — Every platform SHALL have a Knowledge Graph — created if not found.
- KNW-002 — The loop closes through knowledge capture. No mission is complete until knowledge is written back.
- KNW-003 — Domain vocabulary SHALL be aligned to STD-000004 for every platform.
- KNW-004 — Memory is persistent — mission learnings accumulate across all loop cycles.
- KNW-005 — The Master Technical Specification is the living knowledge record of every platform — it must be kept current.
- KNW-006 — A lesson that does not change doctrine is not a lesson, it is an anecdote. Every genuine finding SHALL be recorded in REG-000010 and SHALL produce a Doctrine Amendment (DAM-NNNNNN) or an explicit, recorded reason why none is needed.
- KNW-007 — No significant work session SHALL begin while REG-000010 contains a lesson at status CAPTURED with no amendment from a prior session. This is a hard stop, not a recommendation.

---

## 4. Requirements

| ID | Requirement |
|---|---|
| KNW-REQ-001 | Every platform SHALL have a Knowledge Graph before READY status |
| KNW-REQ-002 | Knowledge Graph SHALL be updated after any mission introducing new entities or relationships |
| KNW-REQ-003 | Domain Vocabulary SHALL be produced for every platform during intake |
| KNW-REQ-004 | OPR-000008 Knowledge Capture SHALL execute after every mission without exception |
| KNW-REQ-005 | Master Technical Specification SHALL be updated after every mission that changes platform state |
| KNW-REQ-006 | memory/ SHALL accumulate mission learnings across all loop cycles |
| KNW-REQ-007 | Knowledge Graph SHALL be created from codebase evidence if it does not exist |
| KNW-REQ-008 | Every lesson recorded in REG-000010 SHALL have a specific, non-vague Finding and actionable Reuse Guidance, per the quality rules in REG-000010 itself |
| KNW-REQ-009 | OPR-000012 Doctrine Amendment SHALL be the only governed path by which a lesson changes EMS doctrine — ad hoc undocumented fixes to standards, authorities, or operations are not permitted regardless of how small the change appears |

---

## 5. Responsibilities

| Role | Responsibility |
|---|---|
| Knowledge Graph Architect | Own Knowledge Graph creation and maintenance |
| Documentation Curator | Own memory layer, execute Knowledge Capture, maintain MTS currency |
| Master Spec Author | Produce and maintain Master Technical Specification |
| Mission Control Director | Trigger Knowledge Capture after every mission |

---

## 6. Governance

Knowledge Capture is mandatory — it cannot be skipped. MTS must be updated after every platform-state-changing mission. Knowledge Graph ownership rests with Knowledge Graph Architect — no other persona may modify it without their involvement.

---

## 7. Dependencies

- AUTH-001 Engineering Constitution
- AUTH-006 Data Governance Authority (Knowledge Graph connects to Data Model)

---

## 8. Produces

- Knowledge governance framework
- Persistent organisational memory model

---

## 9. Consumes

- AUTH-001 Engineering Constitution
- Data Model artefacts from AUTH-006

---

## 10. Updates

- Knowledge Graphs per platform
- Domain Vocabularies per platform
- memory/ layer
- Master Technical Specifications

---

## 11. Related Authorities

- AUTH-001, AUTH-006

---

## 12. Related Standards

- STD-000003 (Knowledge Graph and Domain Vocabulary structures)
- STD-000004 (Vocabulary alignment)

---

## 13. Related Registers

- Knowledge Graphs per platform
- Domain Vocabularies per platform
- REG-000010 Lesson Register

---

## 14. Related Operations

- OPR-000008 Knowledge Capture Operation
- OPR-000002 Platform Intake Operation
- OPR-000012 Doctrine Amendment Operation

---

## 15. Review Cycle

Annually or on significant change to knowledge architecture.

---

## 16. Verification

Audit: every READY platform has a Knowledge Graph and Domain Vocabulary. Every COMPLETE mission has a memory entry. MTS updated within 24 hours of mission completion. No lesson in REG-000010 sits at CAPTURED for more than one work session without an amendment or documented rationale.

---

## 17. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1.2 | SeierTech EMS |
| 1.1.0 | 2026-06-29 | Added KNW-006/007 principles and KNW-REQ-008/009 requirements establishing REG-000010 Lesson Register and OPR-000012 Doctrine Amendment as the governed mechanism by which findings become permanent doctrine — see DAM-000003 | SeierTech EMS |
