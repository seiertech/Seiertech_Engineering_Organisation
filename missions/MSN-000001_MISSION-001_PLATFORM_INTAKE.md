# MSN-000001 — MISSION-001: PLATFORM INTAKE

| Field | Value |
|---|---|
| Artefact ID | MSN-000001 |
| Artefact Class | Mission |
| Title | Platform Intake |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Mission Statement

Complete the intake of a named platform into the SeierTech EMS. Read the platform repository autonomously. Build the Platform Record. Extract the Mission Spine. Satisfy all Readiness Gates. No mission may be issued against the platform until this mission completes with all gates PASSED and all founder questions resolved.

---

## 2. How to Issue This Mission

The Founder issues this mission by creating a GitHub Issue with the following free text format:

```
Complete intake for [PLATFORM_NAME] — repo: [REPO_URL]
```

Example:
```
Complete intake for COMMANDER_C2 — repo: github.com/seiertech/commander-c2
```

The mission chain detects the issue, parses the platform name and repo URL, and begins execution automatically.

---

## 3. Trigger

GitHub Issue created containing platform name and repo URL. Webhook fires. Chain activates.

---

## 4. Objectives

1. Create Platform Record at `platforms/[PLATFORM_NAME]/PLATFORM_RECORD.md`
2. Scan the repository and extract: data model, schema, tech stack, existing documentation, current build state
3. Populate use case register for the platform
4. Build knowledge graph (or confirm it does not yet exist)
5. Execute persona extraction pass — each active persona extracts what it requires from the platform
6. Populate `platforms/[PLATFORM_NAME]/spine/` with one file per persona
7. Identify all gaps the chain cannot resolve autonomously
8. Output Questions to Founder for all unresolved gaps
9. Update REG-000001 Readiness Register
10. When all founder questions resolved — flip platform to READY status

---

## 5. Scope In

- Repository structure analysis
- Data model and schema extraction
- Tech stack identification
- Existing documentation ingestion
- Current build state assessment (what is built, partial, missing)
- Use case extraction
- Knowledge graph creation
- All persona spine extractions
- Readiness gate assessment
- Founder question generation

---

## 6. Scope Out

- No code changes to the platform during intake
- No missions against the platform until READY
- No assumptions substituted for missing information — all gaps go to Questions to Founder

---

## 7. Persona Assignments

All active personas in `agents/` are activated during intake. Each performs its spine extraction pass.

| Persona | Spine Extraction Responsibility |
|---|---|
| Architecture Engineer | Data model, entity relationships, system boundaries, integration points |
| Standards Engineer | Tech stack, standards compliance posture, deviation identification |
| Security Engineer | Security posture, authentication model, data classification, risk surface |
| Data Engineer | Schema, data flows, storage patterns, data quality |
| Integration Engineer | Connectors, APIs, external dependencies, MCP hooks |
| Test Engineer | Existing test coverage, acceptance criteria, test strategy gaps |
| Platform Engineer | Infrastructure, deployment model, environments, CI/CD state |
| Knowledge Engineer | Documentation quality, knowledge gaps, vocabulary alignment |

---

## 8. Mission Spine Output

Each persona writes its extraction to:

```
platforms/[PLATFORM_NAME]/spine/[PERSONA_NAME]_SPINE.md
```

The combined spine is the Mission Spine — the pre-loaded context for all subsequent missions against this platform.

---

## 9. Authority References

- AUTH-001 — Engineering Constitution
- AUTH-002 — Platform Governance Authority (when created)

---

## 10. Standard References

- STD-000001 — EMS Foundation Conformance Standard
- STD-000002 — Engineering Artefact Metadata Standard
- STD-000003 — Engineering Artefact Structure Standard
- STD-000004 — Engineering Vocabulary Standard
- STD-000005 — Traceability Standard

---

## 11. Acceptance Criteria

| Criterion | Gate |
|---|---|
| Platform Record created and conformant | RG-001 |
| Repo scan completed | RG-002 |
| Data model extracted | RG-003 |
| Tech stack identified | RG-004 |
| Use case register populated | RG-005 |
| Knowledge graph created or absence confirmed | RG-006 |
| All persona spine files present | RG-007 |
| All founder questions resolved | RG-008 |
| Platform Record reviewed | RG-009 |
| Platform registered in Platform Register | RG-010 |

---

## 12. Questions to Founder

The chain outputs this section when it cannot determine information from the repo alone. Format:

```markdown
## Questions to Founder

The following information could not be determined from the repository and requires your input before platform readiness can be confirmed:

1. [QUESTION] — Context: [why the chain needs this]
2. [QUESTION] — Context: [why the chain needs this]
```

The Founder responds by commenting on the GitHub Issue. The chain reads the response, updates the Platform Record, and re-checks readiness gates.

---

## 13. Status

| State | Description |
|---|---|
| ISSUED | GitHub Issue created |
| IN_PROGRESS | Chain activated, repo scan underway |
| QUESTIONS_PENDING | Scan complete, awaiting founder responses |
| COMPLETE | All gates passed, platform at READY |
| CANCELLED | Intake abandoned |

---

## 14. Relationships

| Relationship | Artefact ID | Artefact Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Produces | Platform Record | platforms/[PLATFORM_NAME]/PLATFORM_RECORD.md |
| Produces | Mission Spine | platforms/[PLATFORM_NAME]/spine/ |
| Updates | REG-000001 | Readiness Register |
| Updates | REG-000002 | Mission Register |
| Depends On | STD-000001 | EMS Foundation Conformance Standard |
| Required By | All platform missions | — |

---

## 15. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1 Sprint 1.5 | SeierTech EMS |
