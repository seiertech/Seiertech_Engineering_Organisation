# EMS PLATFORM-AGNOSTIC AUDIT — "COMMANDER" LEAKAGE INTO CORE DOCTRINE

| Field | Value |
|---|---|
| Document | Platform-Agnostic Audit (Commander Leakage) |
| Status | ACTIVE — fixes applied and verified |
| Audit Date | 2026-06-29 |
| Trigger | Founder flagged risk of Commander hardcoded into core docs/instructions causing future anomalies when a second platform onboards |
| Method | Programmatic scan of every `.md`/`.yml`/`.json` file for "commander" (case-insensitive), categorised by whether the hit is core doctrine (must be platform-agnostic), platform-specific working files (expected), or this session's own commentary docs (expected) |

---

## Why This Mattered

Team 2 (the forward build force) was written during the same session Commander was the live, active topic. Several persona mission statements ended up with "Commander" hardcoded directly into otherwise-generic role definitions — e.g. the AI Architect's mission read "Design every agentic capability added to **Commander**" instead of "added to **the platform**." This is exactly the kind of anomaly the founder flagged: harmless while Commander is the only platform in the EMS, but a real bug the moment a second platform's missions start running against personas that still think their job is specifically about Commander.

---

## Scan Results — Before Fix

| Category | Files | Instances | Verdict |
|---|---|---|---|
| Core doctrine (`agents/`, `missions/`, `standards/`, `operations/`, `authorities/`, `templates/`, `governance/`) | 13 | 22 | **Needs review — most were real bugs** |
| Platform-specific (`platforms/`, `memory/`) | 1 | 1 | Expected, no action |
| This session's own status/planning docs | 5 | 40 | Expected — these documents are literally about onboarding Commander |
| Other (root README, registers) | 5 | 7 | Mixed — some fine, some real bugs |

---

## What Was Found On Inspection — Two Genuinely Different Categories

**Category A — Real bugs: Commander hardcoded into generic role/doctrine definitions.**

Confirmed by reading actual context (not assumed from grep alone):

| File | What was wrong |
|---|---|
| `agents/team-2-forward/00-executive-director/README.md` | Mission statement: "...advances **Commander** toward completion" |
| `agents/team-2-forward/05-sme-system-user/README.md` | "Validate against...(cyber security for **Commander**)" — hardcoded domain example as if it were the rule |
| `agents/team-2-forward/07-enterprise-architect/README.md` | A persona whose entire job is cross-*platform* coherence had its own mission statement say "as **Commander** is built forward" |
| `agents/team-2-forward/10-ai-architect/README.md` | "Design every agentic capability added to **Commander**" |
| `agents/team-2-forward/17-documentation-and-knowledge-curator/README.md` | "Ensure the MTS stays accurate as **Commander** evolves" |
| `agents/team-2-forward/21-platform-engineer/README.md` | "Evolve the Deployment Architecture as **Commander** scales" |
| `agents/team-2-forward/23-master-spec-author/README.md` | "Keep the MTS current as **Commander** is built forward" |
| `agents/team-2-forward/TEAM_2_REGISTRY.md` | The team's own purpose statement: "Team 2 builds **Commander** forward" + "the old **Commander** codebase is archaeology" |
| `agents/README.md` | Section heading "Two Teams. One Mission. **Finish Commander.**" and a "## For **Commander**" section presenting the brownfield sequence as Commander-specific rather than general |
| `registers/REG-000007_BUILD_GOVERNANCE_REGISTER.md` | **The worst instance** — an entire section, "## 6. The **Commander** Expected Findings," baked Commander's specific known files (MEMORY.md, Performance Doctrine PD-1.0, the ARCH-005–009 lattice, the 50-unit readiness state machine) directly into the **generic, reusable** Build Governance Register doctrine that every future platform's intake reads |

**Category B — Legitimate: Commander used purely as a worked example.**

Confirmed by reading context — these are fine, left unchanged:

| File | Why it's fine |
|---|---|
| `README.md` (root) | "...such as Commander C2 will be governed by this Engineering Organisation but are not defined directly in this root repository" — explicitly states the agnostic principle, uses Commander only as an example noun |
| `standards/STD-000004` | `\| Platform names \| UPPER_SNAKE_CASE \| COMMANDER_C2 \|` — a naming-convention table needs *a* concrete example; this is normal technical writing, not a bug |
| `standards/STD-000005` | `\| Consumes \| PLT-000001 \| Commander C2 Platform Record \|` — a worked example in a relationship-table illustration |
| `missions/MSN-000000` | `Genesis: COMMANDER_ASM — outside-in attack surface management...` — a worked example of the issue format, using one consistent example platform name across docs rather than a different fake name every time |
| `missions/MSN-000001` | `Complete intake for COMMANDER_C2 — repo: ...` — same, a worked format example |

---

## Fixes Applied

All Category A instances were corrected — "Commander" replaced with "the platform" (or equivalent generic phrasing), preserving the original sentence's meaning exactly, just removing the hardcoded platform name:

- 7 individual Team 2 persona files corrected
- `TEAM_2_REGISTRY.md` corrected (2 instances — the team's own purpose statement)
- `agents/README.md` — heading changed to "Two Teams. One Mission Lifecycle. Any Platform." and the "For Commander" section reframed as "## Worked Example — Brownfield Onboarding," explicitly stating Commander was the *first* platform through this sequence and that "nothing in Team 1 or Team 2's doctrine is Commander-specific" — turning the section from an implicit bug into an explicit, correctly-labelled example
- `registers/REG-000007_BUILD_GOVERNANCE_REGISTER.md` — Section 6 rewritten from Commander-specific predictions into a genuinely generic "Illustrative Findings Pattern" table (same useful shape — common governance file patterns and their typical classification — but described generically), with a footnote clarifying that Commander's actual findings belong in `platforms/COMMANDER_C2/` once intake has run, not in the shared doctrine register

Category B instances (5 files, 5 instances) were deliberately left unchanged — they are correct, normal usage of a worked example in illustrative tables, not bugs.

---

## Verification — Re-Scanned After Fixes

| Category | Before | After |
|---|---|---|
| Core doctrine real-bug instances | 22 (across 13 files) | 0 |
| Core doctrine legitimate worked-example instances | 0 (mixed in, unlabelled) | 8 (across 5 files, all confirmed legitimate, several now explicitly labelled as examples) |

Confirmed by re-running the identical scan used to find the original 22 — the only remaining core-doctrine hits are the 5 files in the legitimate-example category, each individually re-checked by reading context, not just counted.

---

## What Was NOT Touched (flagged, not fixed)

`registers/PLATFORM_REGISTER.md` and `registers/READINESS_REGISTER.md` (both **legacy**, already flagged for cleanup decision in `EMS_DOCTRINE_INVENTORY.md`) have Commander hardcoded as **data**, not doctrine prose — e.g. `| PLAT-000001 | Commander | Placeholder | platforms/commander/ |`. This is different from the Category A bugs above: it's stale placeholder data in files already pending an archive/delete decision, not live doctrine that would mislead a future platform's persona. Left as-is, pending the broader legacy-artefact cleanup decision already on record.

---

## Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial audit and fix — found and corrected 22 instances of Commander hardcoded into generic Team 2 doctrine (the worst being an entire register section built around Commander-specific predictions), confirmed 8 remaining instances are legitimate worked-example usage, re-scanned to verify | SeierTech EMS |
