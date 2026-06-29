# TPL-000002 — MISSION TEMPLATE

| Field | Value |
|---|---|
| Artefact ID | TPL-000002 |
| Artefact Class | Template |
| Title | Mission Template |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | FOUNDATIONAL |
| Owner | SeierTech Engineering Organisation |
| Approval Authority | AUTH-001 Engineering Constitution |
| Purpose | Provides the canonical template for Mission artefacts. |
| Scope | Covers Mission artefact creation and excludes Proposal, Engineering Delivery Package, Verification Report, Scorecard, Decision, Persona, Authority, and Register artefacts. |
| Inputs | STD-000002; STD-000003; STD-000004 |
| Outputs | Mission artefact instance |
| Produces | MSN-000000 Mission artefact |
| Consumes | AUTH-001; STD-000002; STD-000003; STD-000004 |
| Dependencies | AUTH-001; STD-000002; STD-000003; STD-000004 |
| Relationships | Produces: Mission artefact; Consumes: Standards; Depends On: AUTH-001; Governed By: AUTH-001; Required By: EMS Mission Chain |
| Review Cycle | On Change |
| Verification Method | Metadata completeness, canonical structure conformance, and vocabulary audit. |
| Baseline | BASELINE-1.0 |
| Change History | 1.0.0 / 2026-06-29 / Initial creation — EF-1.6 / SeierTech EMS |

---

## 1. Target Class

Mission.

---

## 2. Instructions

### 2.1 Human Completion Instructions

Use this template when issuing a formal Mission to the EMS Mission Chain. Replace every placeholder with verified information. Keep all section headings. Use only STD-000004 vocabulary. Record questions the Mission Chain cannot resolve in `questions_to_founder`.

### 2.2 Agent Persona Completion Instructions

Complete this template from Founder instruction, Platform Record, Platform Spine, Authority artefacts, Standards, Registers, and prior Decisions. Do not infer approval. Do not remove placeholders unless verified replacement content is available. Produce a Mission artefact suitable for Proposal creation and Mission Chain execution.

---

## 3. Body

```markdown
# MSN-000000 — <MISSION_TITLE>

| Field | Value |
|---|---|
| Artefact ID | MSN-000000 |
| Artefact Class | Mission |
| Title | <MISSION_TITLE> |
| Status | DRAFT |
| Version | 0.1.0 |
| Classification | <FOUNDATIONAL / OPERATIONAL / PLATFORM-SPECIFIC / EXPERIMENTAL> |
| Owner | <RESPONSIBLE_PERSONA_OR_TEAM> |
| Approval Authority | <AUTHORITY_ARTEFACT_ID> |
| Purpose | <ONE_SENTENCE_PURPOSE> |
| Scope | <MISSION_SCOPE_AND_EXCLUSIONS> |
| Inputs | <INPUT_ARTEFACT_IDS_OR_DESCRIPTIONS> |
| Outputs | <OUTPUT_ARTEFACT_IDS_OR_DESCRIPTIONS> |
| Produces | <DOWNSTREAM_ARTEFACTS> |
| Consumes | <UPSTREAM_ARTEFACTS> |
| Dependencies | <ACTIVE_DEPENDENCY_ARTEFACT_IDS> |
| Relationships | Produces: <ITEMS>; Consumes: <ITEMS>; Depends On: <ITEMS>; Updates: <ITEMS>; Governed By: <ITEMS>; Required By: <ITEMS> |
| Review Cycle | <REVIEW_CYCLE> |
| Verification Method | <VERIFICATION_METHOD> |
| Baseline | <BASELINE_ID> |
| Change History | <VERSION> / <DATE> / <CHANGE> / <AUTHOR> |

---

## 1. Mission Statement

<MISSION_STATEMENT>

---

## 2. Platform

<PLATFORM_REFERENCE>

---

## 3. Trigger

<WHAT_INITIATED_THIS_MISSION>

---

## 4. Objectives

1. <OBJECTIVE_1>
2. <OBJECTIVE_2>
3. <OBJECTIVE_3>

---

## 5. Scope In

- <IN_SCOPE_ITEM_1>
- <IN_SCOPE_ITEM_2>

---

## 6. Scope Out

- <OUT_OF_SCOPE_ITEM_1>
- <OUT_OF_SCOPE_ITEM_2>

---

## 7. Persona Assignments

| Agent Persona | Responsibility | Expected Output |
|---|---|---|
| <AGENT_PERSONA> | <RESPONSIBILITY> | <EXPECTED_OUTPUT> |

---

## 8. Spine References

- <PLATFORM_SPINE_REFERENCE_1>
- <PLATFORM_SPINE_REFERENCE_2>

---

## 9. Authority References

- <AUTHORITY_REFERENCE_1>
- <AUTHORITY_REFERENCE_2>

---

## 10. Standard References

- <STANDARD_REFERENCE_1>
- <STANDARD_REFERENCE_2>

---

## 11. Acceptance Criteria

1. <ACCEPTANCE_CRITERION_1>
2. <ACCEPTANCE_CRITERION_2>
3. <ACCEPTANCE_CRITERION_3>

---

## 12. Engineering Delivery Package Ref

<EDP_REFERENCE_OR_PENDING>

---

## 13. Verification Ref

<VERIFICATION_REPORT_REFERENCE_OR_PENDING>

---

## 14. Questions To Founder

| Question | Reason | Required By |
|---|---|---|
| <QUESTION> | <REASON> | <DATE_OR_GATE> |

---

## 15. Status

<STATUS_SUMMARY>

---

## 16. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 0.1.0 | <DATE> | Initial draft | <AUTHOR> |
```

---

## 4. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation — EF-1.6 | SeierTech EMS |
