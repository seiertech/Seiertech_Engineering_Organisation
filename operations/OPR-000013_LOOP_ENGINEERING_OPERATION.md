# OPR-000013 — Loop Engineering Operation

| Field | Value |
|---|---|
| Operation ID | OPR-000013 |
| Title | Loop Engineering Operation |
| Version | 1.0.0 |
| Status | ACTIVE |
| Owner | Verification and Governance Director |
| Governing Standard | STD-000005 EMS Loop Engineering Standard |
| Governing Authorities | AUTH-001, AUTH-003, AUTH-008, AUTH-010 |
| Produced By | DAM-000014 |
| Date | 2026-07-01 |

---

## 1. Purpose

This operation defines how EMS applies loop engineering to real mission workflows without changing the existing Mission → Proposal → TDA → EDP → Verification → Release → Knowledge Capture chain.

It makes loop boundaries, governors, verifiers, stop conditions and output artefacts explicit across doctrine, workflows and Python executors.

---

## 2. Entry Conditions

This operation is active when:

- A new mission workflow is created or amended.
- A Python mission executor is created or amended.
- A mission chain terminal-state model is changed.
- A persona pass is added, grouped, split or retired.
- A review finds that a loop can run without an explicit verifier, governor or stop condition.

---

## 3. Procedure

### Step 1 — Identify Loop Boundary

Determine the bounded loop being executed.

Examples:

- Issue parsing loop.
- Intake chain loop.
- Genesis chain loop.
- BUILD chain loop.
- TDA review loop.
- Verification loop.
- Release loop.
- Knowledge capture loop.
- Cross-repo delivery loop.

### Step 2 — Declare Loop Contract

Record the following fields either in the artefact itself or in an adjacent generated contract file:

```text
Trigger:
Goal:
Work Unit:
Actor:
Verifier:
Governor:
Stop Condition:
Output Artefact:
Knowledge Update:
```

### Step 3 — Confirm Actor / Verifier Separation

Check that the same persona, script or model call is not both the final producer and the final verifier of the same work unit.

Where separation is not possible yet, the loop must stop as `HUMAN_REQUIRED` or be marked as a known implementation gap.

### Step 4 — Apply Governor

Confirm the loop is bounded by at least one of:

- Authority.
- Standard.
- Operation.
- Deterministic gate.
- Release decision rule.
- Repository permission or token constraint.
- Explicit scope limit.

### Step 5 — Select Stop Condition

Use a standard stop condition from STD-000005. Do not invent a new label in workflow or Python code unless STD-000005 has first been amended.

### Step 6 — Produce Output Artefact

Every loop must produce at least one inspectable artefact. This can be a Markdown artefact, JSON contract, run log, register entry, issue comment, branch, pull request, memory entry or decision record.

### Step 7 — Knowledge Capture

If the loop reveals a reusable lesson, doctrine drift, repeated failure, insufficient evidence, weak persona input or workflow ambiguity, route it to the existing Knowledge Capture and doctrine amendment mechanism.

---

## 4. Required Sweep Method

Any implementation of this operation must perform both directions.

### Left-to-right sweep

```text
Constitution
→ Authorities
→ Standards
→ Registers
→ Operations
→ Templates
→ Personas
→ Workflows
→ Python scripts
→ Memory
```

Purpose: confirm the new loop contract is permitted by doctrine and can be followed forward into execution.

### Right-to-left sweep

```text
Python scripts
→ Workflows
→ Personas
→ Templates
→ Operations
→ Registers
→ Standards
→ Authorities
→ Constitution
```

Purpose: confirm real execution artefacts can trace backward to doctrine and are not merely ad hoc code.

---

## 5. Outputs

This operation may produce:

- Loop contract files.
- Loop pattern library updates.
- Workflow comments or terminal-state labels.
- Python validation scripts.
- Doctrine amendment records.
- Mission run log additions.
- Lesson register candidates.

---

## 6. Completion Criteria

This operation completes when:

1. STD-000005 exists and is authoritative.
2. At least one operation describes how to apply loop engineering.
3. A loop pattern library exists.
4. A machine-checkable sweep script exists.
5. The sweep report states which artefact categories are wired, partially wired or not yet wired.
6. No existing EMS structural chain is replaced or bypassed.

---

## 7. Non-Goals

This operation does not:

- Replace the EMS Operating Model.
- Replace Mission Orders.
- Change the current mission type taxonomy.
- Add a new product architecture.
- Authorise direct code changes in target platform repositories.
- Declare any mission COMPLETE before Knowledge Capture has executed.

---

## 8. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-07-01 | Initial operation added to wire loop engineering into EMS process without structural replacement. | SeierTech EMS |
