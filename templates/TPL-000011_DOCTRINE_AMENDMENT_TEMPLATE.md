# TPL-000011 — DOCTRINE AMENDMENT TEMPLATE

| Field | Value |
|---|---|
| Artefact ID | TPL-000011 |
| Artefact Class | Template |
| Title | Doctrine Amendment Template |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 |
| Target Class | Doctrine Amendment |
| Baseline | BASELINE-1.0 |

---

## Instructions

A Doctrine Amendment (DAM) is the artefact that makes a lesson real. A lesson on its own is just an observation; a Doctrine Amendment is the specific, auditable change made to EMS doctrine because of it. Every `REG-000010` Lesson Register entry with status AMENDED must reference one of these.

Use this template whenever a lesson, audit finding, or bug requires a change to a standard, authority, persona, operation, mission, or register. Do not skip this for "small" fixes — the smallness of a fix is not a reason to leave it untracked; small undocumented fixes are exactly how doctrine drifts silently.

---

## DOCTRINE AMENDMENT BODY

```markdown
# DAM-[NNNNNN] — [TITLE]

| Field | Value |
|---|---|
| Artefact ID | DAM-[NNNNNN] |
| Artefact Class | Doctrine Amendment |
| Title | [Short title] |
| Status | PROPOSED |
| Date | [DATE] |
| Source Lesson | LES-[NNNNNN] |
| Approval Authority | AUTH-001 Engineering Constitution |

---

## 1. Source Lesson

[Reference and one-sentence restatement of the lesson this amendment resolves]

---

## 2. Artefacts Amended

| Artefact ID | Title | Nature of Change |
|---|---|---|
| [e.g. STD-000004] | [title] | [e.g. Added "Checklist" to prohibited terms] |

---

## 3. Before / After

**Before:**
[The specific doctrine text, behaviour, or structure that was wrong or missing]

**After:**
[The specific doctrine text, behaviour, or structure now in place]

---

## 4. Why This Amendment Resolves The Lesson

[Plain statement of how the change prevents recurrence — not just "fixed it" but specifically what mechanism now catches this class of problem]

---

## 5. Verification

[How it was confirmed the amendment actually works — re-run test, re-run audit scan, regression test added. A Doctrine Amendment without verification is not complete.]

---

## 6. Regression Prevention

[If applicable: what permanent check (test, audit script rule, structural requirement) now exists so this exact class of issue cannot silently return undetected]

---

## 7. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Resolves | LES-[NNNNNN] | [Lesson title] |
| Amends | [artefact IDs] | [titles] |

---

## 8. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | [DATE] | Amendment proposed and applied | [Author] |
```
