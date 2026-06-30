# REG-000010 — LESSON REGISTER

| Field | Value |
|---|---|
| Artefact ID | REG-000010 |
| Artefact Class | Register |
| Title | Lesson Register |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | OPERATIONAL |
| Owner | Documentation and Knowledge Curator (PER-000018 / T2-PER-000018) |
| Approval Authority | AUTH-001 Engineering Constitution |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Captures every genuine lesson learned across the EMS — bugs found, gaps discovered, assumptions that proved wrong, patterns that worked — and links each one to whatever doctrine change it produced. A lesson that doesn't change anything is not a lesson, it's an anecdote. This register exists to close that gap: `OPR-000008` Knowledge Capture has always instructed personas to "extract lessons learned from mission execution," but until now there was nowhere conformant to put them, and no required link from lesson to doctrine amendment. Every prior lesson lived only in commit messages and session-specific audit documents — readable once, not load-bearing, not preventing recurrence.

---

## 2. Owner

Documentation and Knowledge Curator persona, both teams. Team 1 captures lessons surfaced during intake/genesis. Team 2 captures lessons surfaced during forward missions. Any persona may propose a lesson entry; the Curator is responsible for ensuring it's properly recorded and routed.

---

## 3. Update Trigger

- Any bug found in EMS doctrine, scripts, or generated artefacts during a mission, an audit, or manual testing
- Any gap discovered between what doctrine claims exists and what actually exists (e.g. a register referenced but never built)
- Any assumption that proved wrong once exercised against real evidence (e.g. "Flask and FastAPI share decorator syntax" — they don't)
- Any pattern that worked well enough to be worth deliberately repeating
- `OPR-000008` Knowledge Capture, on every mission completion — the Curator checks whether this mission surfaced anything lesson-worthy

---

## 4. Schema

| Field | Type | Description |
|---|---|---|
| Lesson ID | Reference | LES-NNNNNN |
| Title | String | Short, specific description — not vague |
| Category | Enum | STRUCTURAL_BUG / DOCTRINE_GAP / WRONG_ASSUMPTION / GOOD_PATTERN / VOCABULARY_DRIFT |
| Source | String | What surfaced this — a mission, an audit, manual testing, founder review |
| Date | Date | ISO 8601 |
| Finding | String | What was actually found — specific, not generic |
| Impact | String | What this affected or would have affected if unfixed |
| Doctrine Amendment | Reference | DAM-NNNNNN — every CAPTURED lesson must link to one, or explicitly state why no amendment was needed |
| Status | Enum | CAPTURED / AMENDED / SUPERSEDED |
| Reuse Guidance | String | How a future persona or session should act differently because of this |

---

## 5. Quality Rules

- **No lesson may sit at CAPTURED with no Doctrine Amendment reference for more than one session** — either it produces a DAM-NNNNNN, or the entry is updated to explicitly record "no amendment needed because X," with rationale. A dangling lesson with no resolution is itself a doctrine gap.
- Findings must be specific. "Personas were sometimes thin" is not a valid Finding. "8 of Team 1's 25 personas were built via a batch script and ended up missing 11 of the 19 standard sections, averaging 68 lines vs siblings' 109-265" is.
- Reuse Guidance must be actionable by a future session with no other context — not "be more careful," but "when batch-writing multiple personas, immediately run the structural completeness check before considering the batch complete."

---

## 6. Lifecycle

```
CAPTURED → AMENDED (a Doctrine Amendment was produced and applied)
CAPTURED → SUPERSEDED (a later, more complete lesson replaces this one)
```

---

## 7. Entries

| Lesson ID | Title | Category | Doctrine Amendment | Status |
|---|---|---|---|---|
| LES-000001 | Flask route decorator syntax never matched by scan_repo.py | STRUCTURAL_BUG | DAM-000001 | AMENDED |
| LES-000002 | Gate checker structurally could never pass a greenfield platform | STRUCTURAL_BUG | DAM-000001 | AMENDED |
| LES-000003 | Genesis brief never reached GITHUB_OUTPUT | STRUCTURAL_BUG | DAM-000001 | AMENDED |
| LES-000004 | Risk Register and Decision Register referenced as live artefacts across multiple authorities but never formally built | DOCTRINE_GAP | DAM-000002 | AMENDED |
| LES-000005 | Persona title "QA and Governance Director" violated STD-000004's own prohibited vocabulary list | VOCABULARY_DRIFT | DAM-000002 | AMENDED |
| LES-000006 | Batch-written personas silently end up thin unless structural completeness is checked immediately, not at next audit | DOCTRINE_GAP | DAM-000003 | AMENDED |
| LES-000007 | Lessons captured in commit messages and session audit docs are not load-bearing — no register existed to make them reusable doctrine | DOCTRINE_GAP | DAM-000003 | AMENDED |

See full detail for each in `memory/lessons/LES-NNNNNN.md` (one file per lesson, created as part of this same change).

---

## 8. Relationships

| Relationship | Artefact ID | Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Governed By | AUTH-010 | Knowledge Governance Authority |
| Owned By | PER-000018 | Documentation and Knowledge Curator (Team 1) |
| Owned By | T2-PER-000018 | Documentation and Knowledge Curator (Team 2) |
| Produces | DAM-NNNNNN | Doctrine Amendments |
| Updated By | OPR-000008 | Knowledge Capture Operation |
| Updated By | OPR-000012 | Doctrine Amendment Operation |

---

## 9. Review Cycle

Continuous — updated as lessons are found. Audited at the start of every significant work session: any lesson still at CAPTURED with no amendment after one prior session is a hard stop requiring resolution before new work proceeds.

---

## 10. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — closes the doctrine gap where OPR-000008 instructed lesson capture but no conformant register existed to receive it. Backfilled 7 lessons from this session's actual findings | SeierTech EMS |
