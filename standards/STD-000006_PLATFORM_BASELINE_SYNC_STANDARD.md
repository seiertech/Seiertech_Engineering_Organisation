# STD-000006 — PLATFORM BASELINE SYNC STANDARD

| Field | Value |
|---|---|
| Artefact ID | STD-000006 |
| Artefact Class | Standard |
| Title | Platform Baseline Sync Standard |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

This standard defines the `.ems/` folder structure that the EMS establishes in every governed platform repository. The `.ems/` folder is the physical EMS footprint in the platform — it makes EMS doctrine, spine, and governance directly accessible to builders, agents, and Kiro without requiring them to read the EMS repo. It is the bridge between the EMS and the platform it governs.

---

## 2. Scope

Applies to every platform reaching READY status — both brownfield platforms completing MISSION-001 intake and greenfield platforms completing MISSION-000 genesis. Every governed platform has a `.ems/` folder. No exceptions.

---

## 3. The Two Platform Origins

This standard serves two distinct platform origin types:

| Origin | Mission | How .ems/ is created |
|---|---|---|
| BROWNFIELD | MISSION-001 Platform Intake | OPR-000010 Platform Baseline Sync creates .ems/ after intake |
| GREENFIELD | MISSION-000 Platform Genesis | OPR-000011 Platform Genesis creates .ems/ before any application code |

Regardless of origin, the `.ems/` folder structure is identical. After READY status, the platform is governed identically.

---

## 4. The .ems/ Folder Structure

Every governed platform repository SHALL contain the following structure:

```
.ems/
├── PLATFORM_BASELINE.md
├── MASTER_TECHNICAL_SPECIFICATION.md
├── BASELINE_MANIFEST.md
├── spine/
│   ├── ARCHITECTURE_ENGINEER_SPINE.md
│   ├── DATA_ARCHITECT_SPINE.md
│   ├── INTEGRATION_ENGINEER_SPINE.md
│   ├── PLATFORM_ENGINEER_SPINE.md
│   ├── CHIEF_ARCHITECT_SPINE.md
│   ├── ENTERPRISE_ARCHITECT_SPINE.md
│   ├── SECURITY_ARCHITECT_SPINE.md
│   ├── FRONTEND_ENGINEERING_LEAD_SPINE.md
│   ├── BACKEND_ENGINEERING_LEAD_SPINE.md
│   ├── UI_UX_DIRECTOR_SPINE.md
│   ├── AI_ARCHITECT_SPINE.md
│   ├── KNOWLEDGE_GRAPH_ARCHITECT_SPINE.md
│   ├── SME_SYSTEM_USER_SPINE.md
│   ├── SENIOR_BUSINESS_ANALYST_SPINE.md
│   ├── TECHNICAL_DEBT_AUDITOR_SPINE.md
│   ├── QA_GOVERNANCE_DIRECTOR_SPINE.md
│   └── DOCUMENTATION_CURATOR_SPINE.md
├── governance/
│   ├── BUILD_GOVERNANCE_REGISTER.md
│   ├── ACTIVE_STANDARDS.md
│   └── DEPRECATED_GOVERNANCE.md
└── kiro-sync/
    ├── MEMORY.md
    ├── RULES.md
    └── STANDARDS.md
```

---

## 5. File Definitions

### PLATFORM_BASELINE.md
The current EMS baseline version this platform is synced to. Updated every time a new EMS baseline is tagged and synced to this platform.

```markdown
# Platform Baseline

Platform: [PLATFORM_NAME]
EMS Baseline: BASELINE-1.0
Sync Date: [DATE]
Sync Mission: [MSN-NNNNNN]
Status: SYNCED
Next Sync Trigger: On EMS BASELINE-2.0 tag
```

### MASTER_TECHNICAL_SPECIFICATION.md
Copy or symlink of the platform MTS from the EMS repo. This is the primary reference document for all builders and agents operating on this platform. Updated after every mission that changes platform state.

### BASELINE_MANIFEST.md
Complete inventory of every EMS artefact produced for this platform, their versions, and their locations in the EMS repo. Enables any agent to locate any artefact without searching.

### spine/
One file per Layer 1 persona. Contains the persona's extracted knowledge about this platform. This is what gets injected into NIM calls for this persona when executing missions against this platform. Updated by OPR-000008 Knowledge Capture after every relevant mission.

### governance/
**BUILD_GOVERNANCE_REGISTER.md** — Registry of every build governance artefact found during intake, its classification, and its EMS mapping. See REG-000007.

**ACTIVE_STANDARDS.md** — Consolidated list of all EMS standards active for this platform, plus any platform-specific standards derived during intake.

**DEPRECATED_GOVERNANCE.md** — Archive of all governance documents found during intake that have been superseded by EMS artefacts. Kept for audit trail. Builders and agents must not read these.

### kiro-sync/
The EMS-derived instruction set for Kiro (or any builder agent). Replaces Kiro's own accumulated governance files. Kiro reads these on every session start.

**MEMORY.md** — EMS-derived memory for Kiro. Contains: platform summary, key architectural decisions, known constraints, critical standards to enforce, active missions context.

**RULES.md** — EMS-derived rules for Kiro. Derived from active standards and authorities. Written in Kiro's instruction format. Supersedes any previous Kiro rules files.

**STANDARDS.md** — Subset of EMS standards directly relevant to Kiro build execution. What Kiro must enforce on every file it touches.

---

## 6. Continuous Sync

A GitHub Action in the platform repository watches the EMS repository for new baseline tags. When a new EMS baseline is tagged:

1. Sync Action fires in platform repo
2. MTS updated from EMS
3. Spine files updated from EMS
4. kiro-sync/ files regenerated from new baseline standards
5. PLATFORM_BASELINE.md updated
6. BASELINE_MANIFEST.md updated
7. Sync recorded in Build Governance Register

This ensures every platform stays in sync with EMS doctrine automatically. No manual governance sweeps required.

---

## 7. Builder Behaviour Requirements

| Requirement | Description |
|---|---|
| BSY-REQ-001 | Kiro SHALL read .ems/kiro-sync/MEMORY.md at session start |
| BSY-REQ-002 | Kiro SHALL read .ems/kiro-sync/RULES.md at session start |
| BSY-REQ-003 | Kiro SHALL read .ems/kiro-sync/STANDARDS.md at session start |
| BSY-REQ-004 | Kiro SHALL NOT read deprecated governance files |
| BSY-REQ-005 | Kiro SHALL reference .ems/MASTER_TECHNICAL_SPECIFICATION.md as primary platform reference |
| BSY-REQ-006 | Builder agents SHALL read .ems/ before any build activity |
| BSY-REQ-007 | No builder SHALL modify .ems/ directly — only EMS sync operations may update it |

---

## 8. Greenfield vs Brownfield Behaviour

| Aspect | Brownfield | Greenfield |
|---|---|---|
| .ems/ creation timing | After intake completes (OPR-000010) | Before application code (OPR-000011) |
| kiro-sync/ content | Derived from reconciled existing governance + EMS doctrine | Derived purely from EMS doctrine |
| governance/ content | Contains BUILD_GOVERNANCE_REGISTER with archaeology findings | Contains empty BUILD_GOVERNANCE_REGISTER |
| spine/ content | Extracted from existing codebase | Designed from genesis brief |
| MTS | Generated from codebase analysis | Generated from designed artefacts |

---

## 9. Dependencies

- AUTH-001 Engineering Constitution
- AUTH-002 Platform Governance Authority
- STD-000001 through STD-000005
- MSN-000001 MISSION-001 Platform Intake
- MSN-000000 MISSION-000 Platform Genesis

---

## 10. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Depends On | STD-000001 | EMS Foundation Conformance Standard |
| Produced By | OPR-000010 | Platform Baseline Sync Operation |
| Produced By | OPR-000011 | Platform Genesis Operation |
| Required By | All platform missions | .ems/ must exist before missions fire |
| Required By | PER-000025 | Build Governance Auditor |

---

## 11. Verification Method

Audit: every READY platform has a .ems/ folder with all required files. Every kiro-sync/ file is current with latest EMS baseline. No builder reading deprecated governance files.

---

## 12. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — post BASELINE-1.0 | SeierTech EMS |
