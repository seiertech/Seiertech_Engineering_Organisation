# TPL-000001 — PLATFORM INTAKE TEMPLATE

| Field | Value |
|---|---|
| Artefact ID | TPL-000001 |
| Artefact Class | Template |
| Title | Platform Intake Template |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | OPERATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 |
| Baseline | BASELINE-1.0 |
| Target Class | Platform Record |

---

## Instructions

This template is completed by the NIM mission chain during MISSION-001 Platform Intake. The chain reads the platform repo and populates every section. Sections that cannot be determined from the repo are left with `[UNKNOWN — QUESTION FOR FOUNDER]` and added to the Questions to Founder section.

Do not manually complete this template. Issue MISSION-001 and let the chain do it.

---

## PLATFORM RECORD

```markdown
# PLT-[NNNNNN] — [PLATFORM_NAME] PLATFORM RECORD

| Field | Value |
|---|---|
| Artefact ID | PLT-[NNNNNN] |
| Artefact Class | Platform Record |
| Title | [PLATFORM_NAME] Platform Record |
| Status | DRAFT |
| Version | 1.0.0 |
| Classification | PLATFORM-SPECIFIC |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 |
| Intake Mission Ref | MSN-000001 |
| Repo URL | [REPO_URL] |
| Baseline | BASELINE-1.0 |

---

## 1. Platform Overview

**Name:** [PLATFORM_NAME]
**Description:** [Chain extracted from repo README and docs]
**Primary Purpose:** [Chain extracted]
**Current Status:** [GREENFIELD / ACTIVE / LEGACY / PARTIAL]

---

## 2. Data Model

### 2.1 Core Entities

[Chain extracted from codebase — list of primary entities with descriptions]

### 2.2 Entity Relationships

[Chain extracted — relationship diagram in text form]

### 2.3 Schema

[Chain extracted — key tables/collections/models with fields]

---

## 3. Tech Stack

| Layer | Technology | Version | Notes |
|---|---|---|---|
| Frontend | [extracted] | [extracted] | |
| Backend | [extracted] | [extracted] | |
| Database | [extracted] | [extracted] | |
| Infrastructure | [extracted] | [extracted] | |
| AI/ML | [extracted] | [extracted] | |
| Integrations | [extracted] | [extracted] | |

---

## 4. Current Build State

### 4.1 Built and Stable
[Chain extracted — list of complete, stable components]

### 4.2 Partially Built
[Chain extracted — list of in-progress or incomplete components]

### 4.3 Missing / Not Started
[Chain extracted — list of planned but unbuilt components]

### 4.4 Technical Debt Identified
[Chain extracted — known issues, drift, duplication, violations]

---

## 5. Use Case Register

| ID | Use Case | Status | Priority |
|---|---|---|---|
| UC-001 | [extracted] | [BUILT/PARTIAL/MISSING] | |

---

## 6. Knowledge Graph

**Status:** [EXISTS / DOES_NOT_EXIST / PARTIAL]
**Location:** [path if exists]
**Coverage:** [Chain assessment]

---

## 7. Existing Documentation

| Document | Location | Quality | Notes |
|---|---|---|---|
| [extracted] | [path] | [GOOD/PARTIAL/POOR] | |

---

## 8. Integration Points

| Integration | Type | Status | Notes |
|---|---|---|---|
| [extracted] | [API/MCP/WEBHOOK/DB] | [ACTIVE/PLANNED/BROKEN] | |

---

## 9. Readiness Gate Results

| Gate | ID | Result | Evidence |
|---|---|---|---|
| Platform Record created | RG-001 | [PASS/FAIL] | |
| Repo scan completed | RG-002 | [PASS/FAIL] | |
| Data model extracted | RG-003 | [PASS/FAIL] | |
| Tech stack identified | RG-004 | [PASS/FAIL] | |
| Use case register populated | RG-005 | [PASS/FAIL] | |
| Knowledge graph addressed | RG-006 | [PASS/FAIL] | |
| All persona spines complete | RG-007 | [PASS/FAIL] | |
| All founder questions resolved | RG-008 | [PASS/FAIL] | |
| Platform Record reviewed | RG-009 | [PASS/FAIL] | |
| Platform registered | RG-010 | [PASS/FAIL] | |

**Overall Readiness Status:** [BLOCKED / IN_PROGRESS / READY]

---

## 10. Questions to Founder

The following could not be determined from the repository:

1. [QUESTION] — Context: [why needed]
2. [QUESTION] — Context: [why needed]

*Respond by commenting on GitHub Issue #[ISSUE_NUMBER]. The chain will update this record and re-check readiness gates.*

---

## 11. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Produced By | MSN-000001 | MISSION-001 Platform Intake |
| Updates | REG-000001 | Readiness Register |
| Required By | All platform missions | — |

---

## 12. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | [DATE] | Created by MISSION-001 intake chain | SeierTech EMS |
```
