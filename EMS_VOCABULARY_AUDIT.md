# EMS VOCABULARY AUDIT

| Field | Value |
|---|---|
| Document | EMS Vocabulary Audit |
| Status | ACTIVE — findings recorded, fixes NOT yet applied (see recommendation) |
| Audit Date | 2026-06-29 |
| Audited Against | STD-000004 Engineering Vocabulary Standard, Section 4 (Prohibited Terms) |
| Method | Programmatic word-boundary scan of every `.md` file in the repo (excluding `ems_engine/` code and this audit doc itself), not a manual spot-check |

---

## Method Note

This was run as an actual scan, not eyeballed — `re.findall(r'\bTERM\b', content)` against every prohibited term in STD-000004 Section 4, across every markdown file in the repo. 23 files flagged. Full list below, nothing summarised away.

---

## Finding 1 — "QA" Was a Persona's Actual Title — ✅ RESOLVED 2026-06-29

**21 of the 23 originally flagged instances were "QA."** This was not scattered casual usage — it was the formal title of **PER-000016 / T2-PER-000016**, used as:

- The persona title itself: "QA and Governance Director" (Team 1) / "QA & Governance Director" (Team 2)
- The folder name: `agents/team-1-baseline/15-qa-governance-director/`, `agents/team-2-forward/15-qa-and-governance-director/`
- Referenced by name in: `TEAM_1_REGISTRY.md`, `TEAM_2_REGISTRY.md`, `AUTH-003`, `AUTH-007`, `AUTH-009`, `EMS_RELATIONSHIP_GRAPH.md`, `MSN-000000`, `MSN-000001`, `OPR-000001`, `OPR-000002`, `OPR-000006` (9 instances alone), `OPR-000011`, `registers/PERSONA_REGISTER.md` (legacy file)

**This was a real STD-000004 violation, not a false positive.** STD-000004 explicitly says "QA (use: Verification)" — the persona that chairs Verification was named after the very term the standard prohibits.

**Fix applied:** Renamed to **"Verification and Governance Director"** (Team 1) / **"Verification & Governance Director"** (Team 2) — the cleanest direct application of the standard's own suggested replacement. Both persona folders renamed via `git mv` (history preserved): `15-qa-governance-director` → `15-verification-governance-director`, `15-qa-and-governance-director` → `15-verification-and-governance-director`. All ~21 cross-references updated individually after confirming exact context in each file — not a blind global find-replace. Re-scanned afterward: zero remaining "QA" instances outside the legacy `PERSONA_REGISTER.md` (which was itself archived to `registers/legacy/` in the same session — see `EMS_DOCTRINE_INVENTORY.md`).

---

## Finding 2 — "Build Pack" — 3 instances, genuinely missed in earlier cleanup

| File | Context |
|---|---|
| `EMS_ARCHITECTURE.md` | 1 instance |
| `memory/decisions/DEC-000003.md` | 1 instance |
| `templates/engineering-proposal-template.md` | 1 instance (this is a **legacy** template, see `EMS_DOCTRINE_INVENTORY.md` — superseded by `TPL-000003`, so this finding is lower priority) |
| `templates/scorecard-template.md` | 1 instance (also **legacy**, superseded by `TPL-000006`) |

An earlier session already did a "Build Pack → Engineering Delivery Package" global fix before BASELINE-1.0 certification — these 3 instances (4 if counting the legacy templates) were evidently missed at that time, or added afterward. Two of the four are in files already flagged as legacy/superseded in the doctrine inventory, so the live-priority count is really just `EMS_ARCHITECTURE.md` and `DEC-000003.md`.

---

## Finding 3 — "Checklist" — 3 instances, one resolved on inspection

| File | Context | Verdict |
|---|---|---|
| `COMMANDER_ONBOARDING_CHECKLIST.md` | The document's own title/filename | Acceptable — ordinary English usage for a practical "before you start" doc, different register from EMS formal nouns |
| `agents/team-1-baseline/19-standards-engineer/README.md` | `"Reasoning style: Checklist-rigorous — systematically verify every gate for every artefact"` | **Real violation** — directly adjacent to "every gate," describing the Quality Gates concept STD-000004 explicitly says to name that way |
| `agents/team-2-forward/19-standards-engineer/README.md` | Same phrasing, Team 2 equivalent | **Real violation** — same fix needed |

**Confirmed by reading the actual context, not assumed.** Both Standards Engineer persona files use "Checklist-rigorous" to describe gate-by-gate verification — should be "Gate-rigorous" or "Quality-Gates-rigorous" per the standard's own replacement guidance.

---

## What Was NOT Found (the encouraging part)

- **Zero** instances of "Task," "Ticket," "Bot," "Policy," "Guideline," or "Snapshot" anywhere in the corpus. The newer doctrine (everything from EF-1.1 onward) has been genuinely vocabulary-disciplined on these six terms.
- The "Build Pack" cleanup that was done earlier in this build session was largely effective — only 4 instances slipped through out of what would have originally been a much larger count across dozens of files.

---

## Summary Table

| Prohibited Term | Instances Found | Files Affected | Severity |
|---|---|---|---|
| QA | 21 | 16 files | **HIGH — formal persona title, needs deliberate rename** |
| Build Pack | 4 | 4 files (2 of which are already-legacy) | LOW — small mechanical fix |
| Checklist | 3 | 3 files | LOW-MEDIUM — needs a quick read to confirm if violation or acceptable plain English |
| Task / Ticket / Bot / Policy / Guideline / Snapshot | 0 | 0 | None — clean |

---

## Recommendation

**The QA → Verification & Governance Director rename was NOT auto-fixed.** It's the right call per the standard, but it touches folder names and ~21 references across both team structures, multiple authorities, operations, and missions — a deliberate confirmed rename, not a quiet sed script. Awaiting a decision.

**The other two findings WERE fixed during this audit**, since both were unambiguous on inspection and low blast-radius:

- ✅ **Build Pack** — fixed in `EMS_ARCHITECTURE.md` and `memory/decisions/DEC-000003.md` (the 2 live, non-legacy instances). The 2 instances in already-legacy templates were left as-is since those files are superseded and flagged for archival/deletion in `EMS_DOCTRINE_INVENTORY.md` anyway.
- ✅ **Checklist** — fixed in both Standards Engineer persona files (`Checklist-rigorous` → `Gate-rigorous`), confirmed on inspection to be a real violation describing the Quality Gates concept directly. The onboarding checklist document title was left as-is — confirmed acceptable plain-English usage, different register from EMS formal nouns.

**Net result of this audit:** 4 of 6 findings resolved in-session. 1 finding (legacy template instances) deliberately left, tracked elsewhere. 1 finding (the QA persona rename) requires a confirmed decision before touching — flagged, not actioned.

---

## Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial audit — programmatic scan of full corpus, found QA persona title violation (21 instances, not previously caught) and residual Build Pack instances missed by earlier cleanup | SeierTech EMS |
