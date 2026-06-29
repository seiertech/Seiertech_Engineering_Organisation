# REG-000007 — BUILD GOVERNANCE REGISTER

| Field | Value |
|---|---|
| Artefact ID | REG-000007 |
| Artefact Class | Register |
| Title | Build Governance Register |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | OPERATIONAL |
| Owner | Build Governance Auditor (PER-000025) |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Tracks every build governance artefact found during platform intake — MEMORY.md files, ERRORS.md files, Kiro rules, skill packages, hook configurations, prompt files, performance doctrine, conformance assertions, workflow definitions, and any file that tells a builder or agent how to behave. Every item is classified, reconciled against EMS doctrine, and mapped to its EMS replacement or disposition.

This register eliminates the manual governance sweep problem permanently. After intake, no governance document is untracked.

---

## 2. Owner

PER-000025 Build Governance Auditor

---

## 3. Update Trigger

- MISSION-001 Platform Intake — Build Governance Discovery Pass
- MISSION-000 Platform Genesis — created empty, updated as governance is created
- Any mission that produces new build governance artefacts
- OPR-000010 Platform Baseline Sync — reconciliation updates
- OPR-000008 Knowledge Capture — post-mission governance additions

---

## 4. Schema

| Field | Type | Description |
|---|---|---|
| Item ID | String | BGV-[PLATFORM]-[NNNNNN] |
| Platform | Reference | PLT-NNNNNN |
| File Path | String | Path in platform repo |
| File Type | Enum | MEMORY / ERRORS / RULES / SKILL_PACKAGE / HOOK / PROMPT / DOCTRINE / CONFORMANCE / WORKFLOW / OTHER |
| Description | String | What this file does / did |
| Discovery Source | Enum | FOUND / CREATED |
| Classification | Enum | ABSORBED / CONFLICTING / COMPATIBLE / ORPHANED / SUPERSEDED |
| EMS Mapping | Reference | Artefact ID of EMS replacement (if ABSORBED/SUPERSEDED) |
| Disposition | Enum | ARCHIVED / DEPRECATED / DELETED / ACTIVE / MIGRATED_TO_EMS |
| Conflicts With | String | Description of conflict if CONFLICTING |
| Resolution | String | How conflict was resolved |
| Resolved By | String | Persona or founder who resolved |
| kiro-sync Mapped | Boolean | Whether this governance is reflected in .ems/kiro-sync/ |
| Last Reviewed | Date | ISO 8601 |
| Notes | String | Free text |

---

## 5. Classification Definitions

| Classification | Meaning | Disposition |
|---|---|---|
| ABSORBED | Content fully superseded by an EMS artefact. EMS version is authoritative. | ARCHIVED or DELETED |
| CONFLICTING | Contradicts EMS doctrine or another governance file. Requires resolution. | DEPRECATED after resolution |
| COMPATIBLE | Does not conflict with EMS. Can coexist or be migrated. | ACTIVE or MIGRATED_TO_EMS |
| ORPHANED | Nothing in the repo references this file. No clear owner. | ARCHIVED pending founder decision |
| SUPERSEDED | A newer version of this same governance exists. | DEPRECATED |

---

## 6. The Commander Expected Findings

Based on known Commander build history, intake is expected to find and classify:

| File | Expected Classification | Expected EMS Mapping |
|---|---|---|
| MEMORY.md | ABSORBED | Platform spine |
| ERRORS.md | ABSORBED | Technical Debt Register |
| Performance Doctrine PD-1.0 | COMPATIBLE → MIGRATED_TO_EMS | Platform-specific standard |
| Conformance lattice ARCH-005 to ARCH-009 | ABSORBED | Architecture Document + Standards |
| 50-unit readiness state machine | ABSORBED | REG-000001 Readiness Register |
| Kiro skill packages | COMPATIBLE → kiro-sync | .ems/kiro-sync/RULES.md |
| GitHub Actions workflows | COMPATIBLE | Integration Map |
| Scattered .md governance files | CLASSIFIED per content | Various |

---

## 7. Lifecycle

```
FOUND (during intake) → CLASSIFIED → RESOLVED → DISPOSITION SET → kiro-sync UPDATED
CREATED (during mission) → REGISTERED → CLASSIFIED → EMS MAPPED
```

---

## 8. Quality Rules

- Every governance file found during intake must have an entry in this register
- No item may remain CONFLICTING after OPR-000010 completes
- Every ABSORBED item must have an EMS Mapping reference
- kiro-sync Mapped must be true for all ACTIVE governance affecting builder behaviour
- No builder may read files marked DEPRECATED or ARCHIVED

---

## 9. Entries

| Item ID | Platform | File Path | Type | Classification | Disposition | EMS Mapping |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

*Populated during MISSION-001 intake Build Governance Discovery Pass or MISSION-000 genesis.*

---

## 10. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Owned By | PER-000025 | Build Governance Auditor |
| Updated By | MSN-000001 | MISSION-001 Platform Intake |
| Updated By | MSN-000000 | MISSION-000 Platform Genesis |
| Updated By | OPR-000010 | Platform Baseline Sync |
| Updated By | OPR-000008 | Knowledge Capture |
| Required By | STD-000006 | Platform Baseline Sync Standard |
| Stored In | .ems/governance/ | Per platform |

---

## 11. Review Cycle

After every mission that touches build governance. After every EMS baseline sync.

---

## 12. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — post BASELINE-1.0 | SeierTech EMS |
