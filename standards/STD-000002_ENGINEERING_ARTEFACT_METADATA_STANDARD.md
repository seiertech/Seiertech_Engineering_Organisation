# STD-000002 — ENGINEERING ARTEFACT METADATA STANDARD

| Field | Value |
|---|---|
| Artefact ID | STD-000002 |
| Artefact Class | Standard |
| Title | Engineering Artefact Metadata Standard |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

This standard defines the universal metadata block that every EMS artefact must carry. The metadata block is the identity, lineage, and governance record of the artefact. It enables automated indexing, traceability, register population, and agent reasoning across the entire EMS.

---

## 2. Scope

Applies universally to every artefact in every EMS domain without exception.

---

## 3. Universal Metadata Block

Every artefact must open with the following metadata table. All fields are mandatory unless marked OPTIONAL.

| Field | Type | Description |
|---|---|---|
| Artefact ID | String | Unique identifier. Format: `[CLASS-PREFIX]-[NNNNNN]` e.g. STD-000002, AUTH-001, MSN-000001 |
| Artefact Class | Enum | One of: Authority, Standard, Register, Mission, Proposal, Engineering Delivery Package, Verification Report, Scorecard, Decision, Platform Record, Persona, Operation, Template, Work Product |
| Title | String | Full human-readable title |
| Status | Enum | One of: DRAFT, REVIEW, ACTIVE, DEPRECATED, SUPERSEDED |
| Version | SemVer | Major.Minor.Patch — e.g. 1.0.0 |
| Classification | Enum | One of: FOUNDATIONAL, OPERATIONAL, PLATFORM-SPECIFIC, EXPERIMENTAL |
| Owner | String | Responsible person or team |
| Approval Authority | Reference | Artefact ID of the authority that governs approval |
| Purpose | String | One sentence — why this artefact exists |
| Scope | String | What this artefact covers and what it explicitly excludes |
| Inputs | List | Artefact IDs or descriptions of what this artefact consumes |
| Outputs | List | Artefact IDs or descriptions of what this artefact produces |
| Produces | List | Downstream artefacts created as a result of this artefact |
| Consumes | List | Upstream artefacts this artefact depends on |
| Dependencies | List | Artefact IDs that must exist and be ACTIVE for this artefact to be valid |
| Relationships | Table | Produces / Consumes / Depends On / Updates / Governed By / Required By |
| Review Cycle | String | e.g. Quarterly, On Change, Annual |
| Verification Method | String | How conformance of this artefact is verified |
| Baseline | String | Baseline version this artefact belongs to e.g. BASELINE-1.0 |
| Change History | Table | Version / Date / Change / Author |

---

## 4. Artefact Class Prefix Registry

| Class | Prefix | Example |
|---|---|---|
| Authority | AUTH | AUTH-001 |
| Standard | STD | STD-000001 |
| Register | REG | REG-000001 |
| Mission | MSN | MSN-000001 |
| Proposal | PRP | PRP-000001 |
| Engineering Delivery Package | EDP | EDP-000001 |
| Verification Report | VER | VER-000001 |
| Scorecard | SCR | SCR-000001 |
| Decision | DEC | DEC-000001 |
| Platform Record | PLT | PLT-000001 |
| Persona | PER | PER-000001 |
| Operation | OPR | OPR-000001 |
| Template | TPL | TPL-000001 |
| Work Product | WPR | WPR-000001 |

---

## 5. Status Lifecycle

```
DRAFT → REVIEW → ACTIVE → DEPRECATED
                        → SUPERSEDED (replaced by newer version)
```

No artefact may be consumed by another artefact or referenced in a mission unless status is ACTIVE.

---

## 6. Versioning Rules

- Major version increment: breaking change to artefact structure or purpose
- Minor version increment: additive change, new sections, expanded scope
- Patch version increment: corrections, clarifications, metadata updates

---

## 7. Dependencies

- AUTH-001 — Engineering Constitution
- STD-000001 — EMS Foundation Conformance Standard

---

## 8. Relationships

| Relationship | Artefact |
|---|---|
| Governed By | AUTH-001 |
| Required By | All EMS artefacts |
| Produces | Consistent metadata across EMS |
| Updates | All domain registers on artefact creation |

---

## 9. Verification Method

Automated metadata completeness check. All mandatory fields present and non-empty. Artefact Class value from permitted enum. Status value from permitted enum.

---

## 10. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1 Sprint 1.1 | SeierTech EMS |
