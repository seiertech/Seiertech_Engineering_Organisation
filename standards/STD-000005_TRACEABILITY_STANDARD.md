# STD-000005 — TRACEABILITY STANDARD

| Field | Value |
|---|---|
| Artefact ID | STD-000005 |
| Artefact Class | Standard |
| Title | Traceability Standard |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

This standard ensures every artefact in the EMS declares its relationships to all other artefacts it depends on, produces, consumes, updates, is governed by, or is required by. No orphan artefacts. No undeclared dependencies. Complete traceability from mission to baseline.

---

## 2. Scope

Applies to every artefact in every EMS domain. Every file is a node in the EMS relationship graph. Every relationship is a declared edge.

---

## 3. Mandatory Relationship Declarations

Every artefact must declare all applicable relationships in its Relationships table:

| Relationship Type | Direction | Meaning |
|---|---|---|
| Depends On | Inbound | This artefact cannot exist or function without the referenced artefact |
| Produces | Outbound | This artefact creates or generates the referenced artefact |
| Consumes | Inbound | This artefact reads or uses the referenced artefact as input |
| Updates | Outbound | This artefact writes to or modifies the referenced artefact |
| Governed By | Inbound | The referenced authority or standard controls this artefact |
| Required By | Outbound | The referenced artefact depends on this artefact |

---

## 4. Relationships Table Format

Every artefact includes a Relationships section formatted as:

```markdown
## Relationships

| Relationship | Artefact ID | Artefact Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Depends On | STD-000002 | Engineering Artefact Metadata Standard |
| Produces | REG-000001 | Mission Register |
| Consumes | PLT-000001 | Commander C2 Platform Record |
| Updates | REG-000003 | Readiness Register |
| Required By | MSN-000001 | MISSION-001 Platform Intake |
```

---

## 5. Orphan Rule

An artefact is considered orphaned if:

- It declares no Governed By relationship
- It declares no Depends On relationships when dependencies clearly exist
- No other artefact declares it as Required By or Produces

Orphaned artefacts MUST NOT be set to ACTIVE status. The EMS Foundation Audit agent will flag all orphans during Sprint EF-1.8 certification.

---

## 6. Relationship Graph Integrity Rules

| Rule | Requirement |
|---|---|
| TR-001 | Every artefact must declare at least one Governed By relationship |
| TR-002 | Every artefact must declare all upstream dependencies in Depends On |
| TR-003 | When an artefact produces another artefact, both must declare the relationship |
| TR-004 | When an artefact updates a register, the register must list the artefact as a source |
| TR-005 | No circular dependencies — an artefact cannot depend on something that depends on it |
| TR-006 | All referenced Artefact IDs must exist in the repository |

---

## 7. Traceability Across the Mission Lifecycle

The following relationships must be traceable end-to-end for every completed mission:

```
GitHub Issue (Mission trigger)
→ Mission (MSN)
→ Platform Record (PLT) [consumed]
→ Platform Spine (consumed)
→ Proposal (PRP) [produced]
→ Engineering Delivery Package (EDP) [produced]
→ Verification Report (VER) [produced]
→ Scorecard (SCR) [produced]
→ Registers updated
→ Baseline tagged
```

Every node in this chain must carry the Mission ID as a reference. A mission is not complete until this chain is unbroken.

---

## 8. Automated Traceability Check

The EMS Foundation Audit agent performs the following checks:

1. Every artefact has a Relationships table
2. All declared Artefact ID references resolve to existing files
3. No orphan artefacts exist
4. Every mission has an unbroken traceability chain from issue to baseline
5. No circular dependencies

---

## 9. Dependencies

- AUTH-001 — Engineering Constitution
- STD-000002 — Engineering Artefact Metadata Standard

---

## 10. Relationships

| Relationship | Artefact ID | Artefact Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Depends On | STD-000002 | Engineering Artefact Metadata Standard |
| Required By | All EMS artefacts | — |
| Produces | Relationship graph integrity | — |
| Updates | FOUNDATION_BASELINE_REGISTER | Foundation Baseline Register |

---

## 11. Verification Method

Automated graph traversal by EMS Foundation Audit agent. All six integrity rules checked. Orphan report produced.

---

## 12. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1 Sprint 1.1 | SeierTech EMS |
