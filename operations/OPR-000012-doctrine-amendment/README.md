# OPR-000012 — DOCTRINE AMENDMENT OPERATION

| Field | Value |
|---|---|
| Artefact ID | OPR-000012 |
| Artefact Class | Operation |
| Title | Doctrine Amendment Operation |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | Executive Director |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Define the mandatory process by which a lesson becomes a permanent, verified change to EMS doctrine. This operation exists because, prior to it, every lesson learned in this EMS's build sessions lived only in commit messages and one-off audit documents — readable, but not load-bearing. Nothing required a finding to actually change a standard, persona, or operation, and nothing prevented the same bug class from being silently rediscovered in a future session. This operation closes that gap.

---

## 2. Trigger

- Any bug found in EMS doctrine, scripts, or generated artefacts
- Any gap discovered between what doctrine claims exists and what is actually built
- Any wrong assumption discovered once exercised against real evidence
- The start of any new significant work session — see Step 0 below
- `OPR-000008` Knowledge Capture flags a mission-surfaced lesson

---

## 3. Preconditions

None — this operation has no platform readiness dependency. It governs the EMS itself, not a specific platform.

---

## 4. Steps

### Step 0 — Session Start Gate

Before any new significant work begins, the Documentation and Knowledge Curator (or the founder, or whichever agent/session is starting work) checks `REG-000010` Lesson Register for any entry at status `CAPTURED` with no `Doctrine Amendment` reference. **This is a hard stop.** A dangling lesson from a prior session must be resolved — either amended now, or explicitly marked with documented rationale for why no amendment is needed — before new work proceeds. This is what prevents lessons from being captured once and then quietly forgotten.

### Step 1 — Capture

| Step | Action | Responsible |
|---|---|---|
| 1.1 | Lesson identified during a mission, audit, or manual work | Any persona or the founder |
| 1.2 | Lesson recorded in `REG-000010` with a specific Finding (not vague) | Documentation and Knowledge Curator |
| 1.3 | Lesson assigned a Category (STRUCTURAL_BUG / DOCTRINE_GAP / WRONG_ASSUMPTION / GOOD_PATTERN / VOCABULARY_DRIFT) | Documentation and Knowledge Curator |

### Step 2 — Amend

| Step | Action | Responsible |
|---|---|---|
| 2.1 | Determine which artefact(s) the lesson requires changes to | Relevant domain persona (e.g. Standards Engineer for vocabulary, Chief Architect for architecture doctrine) |
| 2.2 | Draft the Doctrine Amendment per `TPL-000011`, including explicit Before/After | Relevant domain persona |
| 2.3 | Apply the amendment to the actual artefact(s) | Relevant domain persona |
| 2.4 | Standards Engineer assesses the amended artefact(s) for conformance | Standards Engineer |

### Step 3 — Verify

| Step | Action | Responsible |
|---|---|---|
| 3.1 | Re-run whatever test, scan, or check originally surfaced the lesson, confirm it no longer fails | Originating persona or Standards Engineer |
| 3.2 | If the lesson came from a STRUCTURAL_BUG, add a permanent regression test if one does not already exist | Relevant engineering persona |
| 3.3 | Record verification method and result in the Doctrine Amendment's Verification section | Relevant domain persona |

### Step 4 — Close

| Step | Action | Responsible |
|---|---|---|
| 4.1 | Doctrine Amendment status set to APPLIED | Executive Director |
| 4.2 | `REG-000010` lesson entry status updated to AMENDED, with the DAM reference | Documentation and Knowledge Curator |
| 4.3 | If the amendment changes a foundational standard or authority, version incremented per `STD-000002` rules | Standards Engineer |

---

## 5. Gates

| Gate | Description |
|---|---|
| G-001 | No lesson may remain CAPTURED with no amendment beyond one session — Step 0 enforces this |
| G-002 | No Doctrine Amendment closes without a recorded verification method and result |
| G-003 | A STRUCTURAL_BUG-category lesson must produce a permanent regression test, not just a one-time fix |

---

## 6. Why This Is Not Bureaucracy

This operation is deliberately lightweight — a markdown register entry and a markdown amendment file, not a review board. The discipline it enforces is narrow and specific: every real finding either changes something permanently and verifiably, or someone has to explicitly say why it doesn't, in writing, where the next session can see it. The alternative — what existed before this operation — is what actually happened across this build: real findings, real fixes, but nothing forcing them to compound. This is the difference between an EMS that gets audited occasionally and one that genuinely tightens its own loop over time, which is the entire premise of Loop Engineering.

---

## 7. Outputs

- `REG-000010` Lesson Register entries, kept current
- `DAM-NNNNNN` Doctrine Amendment artefacts, one per resolved lesson
- Amended doctrine artefacts (standards, authorities, personas, operations, etc.)
- Permanent regression tests for structural bugs

---

## 8. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Governed By | AUTH-010 | Knowledge Governance Authority |
| Updates | REG-000010 | Lesson Register |
| Produces | TPL-000011 instances | Doctrine Amendments |
| Triggered By | OPR-000008 | Knowledge Capture Operation |

---

## 9. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — closes the gap where lessons were found but never structurally required to change doctrine | SeierTech EMS |
