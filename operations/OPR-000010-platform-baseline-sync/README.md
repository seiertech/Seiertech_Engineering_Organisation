# OPR-000010 — PLATFORM BASELINE SYNC OPERATION

| Field | Value |
|---|---|
| Artefact ID | OPR-000010 |
| Artefact Class | Operation |
| Title | Platform Baseline Sync Operation |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | Mission Control Director |
| Approval Authority | AUTH-002 Platform Governance Authority |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Establish the EMS footprint in a brownfield platform repository after intake completes. Reconcile all existing governance against EMS doctrine. Sync Kiro to EMS-derived instructions. Create the `.ems/` folder. Eliminate governance drift permanently. After this operation completes, EMS is the single source of truth for the platform — not just in the EMS repo but embedded in the platform itself.

---

## 2. Trigger

MISSION-001 Platform Intake completes — all 10 readiness gates PASS, Master Technical Specification approved, platform status set to READY. OPR-000010 fires immediately as Phase 7 of MISSION-001.

---

## 3. Preconditions

- Platform at READY status in REG-000001
- All intake artefacts (24+) produced and Standards Engineer approved
- Master Technical Specification complete and approved
- Build Governance Register (REG-000007) populated by Build Governance Auditor
- All CONFLICTING governance items resolved

---

## 4. Steps

### Phase 1 — Create .ems/ Structure

| Step | Action | Persona | Gate |
|---|---|---|---|
| 1.1 | Create .ems/ folder in platform repo | Mission Control Director | Platform at READY |
| 1.2 | Create .ems/spine/ directory | Mission Control Director | — |
| 1.3 | Create .ems/governance/ directory | Mission Control Director | — |
| 1.4 | Create .ems/kiro-sync/ directory | Mission Control Director | — |
| 1.5 | Write PLATFORM_BASELINE.md | Mission Control Director | — |
| 1.6 | Write BASELINE_MANIFEST.md | Mission Control Director | — |

### Phase 2 — Populate Spine

| Step | Action | Persona | Gate |
|---|---|---|---|
| 2.1 | Copy all persona spine files from EMS to .ems/spine/ | Mission Control Director | All spine files exist |
| 2.2 | Standards Engineer validates spine files are current | Standards Engineer | PASS |

### Phase 3 — Populate MTS

| Step | Action | Persona | Gate |
|---|---|---|---|
| 3.1 | Copy Master Technical Specification to .ems/MASTER_TECHNICAL_SPECIFICATION.md | Master Spec Author | MTS approved |
| 3.2 | Standards Engineer validates MTS copy | Standards Engineer | PASS |

### Phase 4 — Governance Reconciliation

| Step | Action | Persona | Gate |
|---|---|---|---|
| 4.1 | Build Governance Auditor produces final governance disposition for all items | Build Governance Auditor | All items classified |
| 4.2 | Write .ems/governance/BUILD_GOVERNANCE_REGISTER.md | Build Governance Auditor | — |
| 4.3 | Write .ems/governance/DEPRECATED_GOVERNANCE.md | Build Governance Auditor | — |
| 4.4 | Write .ems/governance/ACTIVE_STANDARDS.md | Build Governance Auditor | — |
| 4.5 | Mark all ABSORBED/SUPERSEDED files as deprecated in platform repo | Build Governance Auditor | — |
| 4.6 | Archive ORPHANED files to legacy/ folder in platform repo | Build Governance Auditor | Founder approval |
| 4.7 | Standards Engineer validates governance folder | Standards Engineer | PASS |

### Phase 5 — Kiro Sync

| Step | Action | Persona | Gate |
|---|---|---|---|
| 5.1 | Build Governance Auditor synthesises kiro-sync content from: surviving COMPATIBLE governance + EMS standards + MTS constraints + architectural decisions + known debt | Build Governance Auditor | — |
| 5.2 | Write .ems/kiro-sync/MEMORY.md | Build Governance Auditor | — |
| 5.3 | Write .ems/kiro-sync/RULES.md | Build Governance Auditor | — |
| 5.4 | Write .ems/kiro-sync/STANDARDS.md | Build Governance Auditor | — |
| 5.5 | Standards Engineer validates kiro-sync files | Standards Engineer | PASS |
| 5.6 | Documentation Curator verifies kiro-sync files are readable and complete | Documentation Curator | PASS |

### Phase 6 — Continuous Sync Hook

| Step | Action | Persona | Gate |
|---|---|---|---|
| 6.1 | Create GitHub Action in platform repo: .github/workflows/ems-sync.yml | Mission Control Director | — |
| 6.2 | Action watches EMS repo for new baseline tags | Mission Control Director | — |
| 6.3 | On new EMS baseline: action fires sync mission automatically | Mission Control Director | — |
| 6.4 | Test sync hook by triggering manually | Mission Control Director | Fires successfully |

### Phase 7 — Verification and Completion

| Step | Action | Persona | Gate |
|---|---|---|---|
| 7.1 | Verify .ems/ folder complete per STD-000006 | Standards Engineer | All files present |
| 7.2 | Verify kiro-sync/ non-contradictory | Build Governance Auditor | No contradictions |
| 7.3 | Update REG-000001 — platform sync status: SYNCED | Mission Control Director | — |
| 7.4 | Update REG-000007 — all items dispositioned | Build Governance Auditor | — |
| 7.5 | Comment on GitHub Issue: sync complete | Mission Control Director | — |
| 7.6 | Platform is now fully operational | — | — |

---

## 5. Gates

| Gate | Description |
|---|---|
| G-001 | All CONFLICTING governance resolved before Phase 4 completes |
| G-002 | .ems/ folder complete per STD-000006 before Kiro sync |
| G-003 | kiro-sync/ files non-contradictory before platform operational |
| G-004 | Continuous sync hook functional before operation closes |

---

## 6. Outputs

- .ems/ folder in platform repo (complete per STD-000006)
- Build Governance Register fully populated
- All stale governance deprecated or archived
- Kiro reading EMS-derived instructions only
- Continuous sync hook active
- Platform fully operational

---

## 7. The Governance Drift Problem — Solved

After this operation:

- Kiro reads `.ems/kiro-sync/` at session start — not its own stale files
- No competing governance documents in the repo
- Every governance artefact tracked in REG-000007
- EMS is the single source of truth embedded in the platform
- New governance created by future missions is registered automatically via OPR-000008
- EMS baseline updates propagate automatically via the sync hook
- Manual governance sweeps are permanently eliminated

---

## 8. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-002 | Platform Governance Authority |
| Governed By | STD-000006 | Platform Baseline Sync Standard |
| Follows | OPR-000002 | Platform Intake Operation |
| Triggered By | MSN-000001 | MISSION-001 Platform Intake (Phase 7) |
| Uses | PER-000025 | Build Governance Auditor |
| Produces | .ems/ folder | Per platform |
| Updates | REG-000001 | Readiness Register |
| Updates | REG-000007 | Build Governance Register |

---

## 9. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — post BASELINE-1.0 | SeierTech EMS |
