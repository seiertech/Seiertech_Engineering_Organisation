# HAR-000001 — PLATFORM HANDOFF ARTEFACT

| Field | Value |
|---|---|
| Artefact ID | HAR-[PLATFORM]-001 |
| Artefact Class | Handoff Artefact |
| Title | [PLATFORM_NAME] — Team 1 to Team 2 Handoff |
| Status | DRAFT |
| Version | 1.0.0 |
| Classification | OPERATIONAL |
| Owner | Executive Director |
| Approval Authority | AUTH-001 Engineering Constitution |
| Platform | [PLATFORM_NAME] |
| Team 1 Mission Ref | MSN-000001 |
| Handoff Date | [DATE] |

---

## 1. Purpose

This artefact is the formal baton between Team 1 and Team 2. It declares that the baseline has been established, summarises what Team 1 found and produced, communicates what Team 2 inherits, and formally authorises Team 2 to begin forward build operations.

Team 2 reads this document before their first mission. It is their briefing.

---

## 2. Handoff Declaration

> Team 1 Baseline Establishment Force has completed its mission against [PLATFORM_NAME].
> The baseline is established. The Master Technical Specification is approved.
> The .ems/ folder is in place. Kiro is synced to EMS doctrine.
> Team 1 stands down.
> Team 2 Forward Build Force is hereby authorised to begin forward operations.

**Executive Director Sign-off:** [DATE]

---

## 3. What Team 1 Found

### 3.1 Platform State at Intake

| Dimension | Finding |
|---|---|
| Codebase size | [LOC count] |
| Languages | [list] |
| Build state | [GREENFIELD / EARLY / PARTIAL / MATURE / LEGACY] |
| Documentation state | [NONE / POOR / PARTIAL / GOOD] |
| Test coverage | [%] |
| CI/CD state | [NONE / BASIC / MATURE] |
| Security posture | [CRITICAL / HIGH RISK / MEDIUM / LOW] |
| Technical debt level | [CRITICAL / HIGH / MEDIUM / LOW] |

### 3.2 What Existed (FOUND)

[List of artefacts that existed in the repo before intake — documentation, tests, architecture docs, etc]

### 3.3 What Team 1 Created (CREATED)

[List of artefacts that did not exist and were created by Team 1 during intake]

### 3.4 What Team 1 Derived (DERIVED)

[List of artefacts derived from evidence that existed but wasn't formalised]

### 3.5 Confidence Assessment

| Artefact | Confidence | Basis |
|---|---|---|
| Data Model | HIGH / MEDIUM / LOW | [FOUND/DERIVED/CREATED] |
| Architecture Document | HIGH / MEDIUM / LOW | [FOUND/DERIVED/CREATED] |
| Knowledge Graph | HIGH / MEDIUM / LOW | [FOUND/DERIVED/CREATED] |
| Use Case Register | HIGH / MEDIUM / LOW | [FOUND/DERIVED/CREATED] |
| Security Posture | HIGH / MEDIUM / LOW | [FOUND/DERIVED/CREATED] |

---

## 4. What Team 2 Inherits

### 4.1 Clean Baseline Artefacts

Team 2 operates exclusively against these EMS-governed artefacts. Never against the old platform state.

| Artefact | Location | Version | Confidence |
|---|---|---|---|
| Master Technical Specification | platforms/[NAME]/MASTER_TECHNICAL_SPECIFICATION.md | 1.0.0 | [H/M/L] |
| Knowledge Graph | platforms/[NAME]/KNOWLEDGE_GRAPH.md | 1.0.0 | [H/M/L] |
| Data Model | platforms/[NAME]/DATA_MODEL.md | 1.0.0 | [H/M/L] |
| Architecture Document | platforms/[NAME]/ARCHITECTURE_DOCUMENT.md | 1.0.0 | [H/M/L] |
| Use Case Register | platforms/[NAME]/USE_CASE_REGISTER.md | 1.0.0 | [H/M/L] |
| AI Capability Map | platforms/[NAME]/AI_CAPABILITY_MAP.md | 1.0.0 | [H/M/L] |
| Technical Debt Register | platforms/[NAME]/TECHNICAL_DEBT_REGISTER.md | 1.0.0 | [H/M/L] |
| Security Posture | platforms/[NAME]/SECURITY_POSTURE.md | 1.0.0 | [H/M/L] |
| Requirements Register | platforms/[NAME]/REQUIREMENTS_REGISTER.md | 1.0.0 | [H/M/L] |
| Proposition Document | platforms/[NAME]/PROPOSITION_DOCUMENT.md | 1.0.0 | [H/M/L] |

### 4.2 Platform .ems/ Footprint

| File | Status |
|---|---|
| .ems/MASTER_TECHNICAL_SPECIFICATION.md | [PRESENT / MISSING] |
| .ems/PLATFORM_BASELINE.md | [PRESENT / MISSING] |
| .ems/BASELINE_MANIFEST.md | [PRESENT / MISSING] |
| .ems/spine/ (all 17 files) | [COMPLETE / PARTIAL] |
| .ems/governance/BUILD_GOVERNANCE_REGISTER.md | [PRESENT / MISSING] |
| .ems/kiro-sync/MEMORY.md | [PRESENT / MISSING] |
| .ems/kiro-sync/RULES.md | [PRESENT / MISSING] |
| .ems/kiro-sync/STANDARDS.md | [PRESENT / MISSING] |

### 4.3 Builder Sync Status

| Builder | Sync Status | Notes |
|---|---|---|
| Kiro | SYNCED / PENDING | [notes] |

---

## 5. Known Debt Inherited

Team 2 inherits this debt from the brownfield state. It is documented in the Technical Debt Register. Team 2 does not ignore it — they address it through REHAB missions as prioritised by the Founder.

| Severity | Count | Top Items |
|---|---|---|
| CRITICAL | [n] | [top 3] |
| HIGH | [n] | [top 3] |
| MEDIUM | [n] | [summary] |
| LOW | [n] | [summary] |

---

## 6. Open Items Requiring Team 2 Attention

[Items that Team 1 could not resolve — questions outstanding, low confidence artefacts, gaps the Founder has not yet answered]

| Item | Type | Priority | Notes |
|---|---|---|---|
| [item] | [QUESTION / LOW_CONFIDENCE / GAP] | [HIGH/MED/LOW] | [notes] |

---

## 7. Recommended First Missions for Team 2

Based on the baseline assessment, Team 1 recommends Team 2 prioritise these mission types first:

| Priority | Mission Type | Rationale |
|---|---|---|
| 1 | [REHAB / BUILD / AGENTIC_INSERTION / STRATEGIC] | [why this first] |
| 2 | [type] | [rationale] |
| 3 | [type] | [rationale] |

---

## 8. Governance Archaeology Summary

| Item | Count | Disposition |
|---|---|---|
| Governance files found | [n] | — |
| ABSORBED into EMS | [n] | Archived |
| COMPATIBLE / Active | [n] | In .ems/governance/ |
| ORPHANED | [n] | Quarantined |
| CONFLICTING / Resolved | [n] | Deprecated |

---

## 9. Formal Handoff

| Role | Confirmation | Date |
|---|---|---|
| Team 1 Mission Control Director | Baseline complete — handing off | [DATE] |
| Standards Engineer | All artefacts conformant | [DATE] |
| Executive Director | Handoff approved | [DATE] |
| Team 2 Mission Control Director | Handoff received — forward operations authorised | [DATE] |

---

## 10. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Produced By | MSN-000001 | MISSION-001 Platform Intake |
| Produced By | Team 1 | Baseline Establishment Force |
| Consumed By | Team 2 | Forward Build Force |
| References | platforms/[NAME]/MASTER_TECHNICAL_SPECIFICATION.md | Primary baseline document |
| Updates | REG-000001 | Readiness Register — handoff complete |
| Updates | REG-000002 | Mission Register — MISSION-001 COMPLETE |

---

## 11. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | [DATE] | Produced by Team 1 on intake completion | SeierTech EMS |
