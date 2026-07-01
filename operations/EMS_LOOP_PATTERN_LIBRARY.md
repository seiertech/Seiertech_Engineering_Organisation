# EMS Loop Pattern Library

| Field | Value |
|---|---|
| Document | EMS Loop Pattern Library |
| Version | 1.0.0 |
| Status | ACTIVE |
| Governing Standard | STD-000005 EMS Loop Engineering Standard |
| Governing Operation | OPR-000013 Loop Engineering Operation |
| Produced By | DAM-000014 |
| Date | 2026-07-01 |

---

## Purpose

This library gives EMS a reusable set of loop patterns without changing the existing operating model. A pattern is not a new mission type; it is a bounded execution shape that can appear inside one or more EMS workflows.

---

## Pattern 1 — Issue Parsing Loop

| Contract Field | Value |
|---|---|
| Trigger | GitHub issue opened or edited. |
| Goal | Determine whether the issue maps to a recognised mission type. |
| Work Unit | Deterministic parsing of title/body. |
| Actor | `issue_parser.py` through `ems-mission-chain.yml`. |
| Verifier | Workflow branch condition and resulting mission-type output. |
| Governor | AUTH-003 Mission Governance Authority; EMS Operating Model Section 1. |
| Stop Condition | AMBIGUOUS_INPUT or recognised mission type. |
| Output Artefact | `parsed_mission.json`, workflow outputs, issue label/comment. |
| Knowledge Update | Ambiguity patterns can become parser or doctrine amendments. |

---

## Pattern 2 — Intake Loop

| Contract Field | Value |
|---|---|
| Trigger | MISSION-001 brownfield intake issue. |
| Goal | Establish platform baseline from an existing repository. |
| Work Unit | Repository scan, grouped persona passes, MTS synthesis, handoff, readiness gates. |
| Actor | Team 1 intake executor and baseline-establishment personas. |
| Verifier | Standards Engineer gates and deterministic readiness gate checker. |
| Governor | AUTH-001, AUTH-003, AUTH-004, AUTH-005, STD-000001, REG-000001. |
| Stop Condition | READY_WITH_KNOWN_CEILING or BLOCKED_BY_GATE. |
| Output Artefact | Platform artefacts, run log, readiness result, issue status label. |
| Knowledge Update | Missing artefact coverage or persona input gaps route to lessons/amendments. |

---

## Pattern 3 — Genesis Loop

| Contract Field | Value |
|---|---|
| Trigger | MISSION-000 greenfield genesis issue. |
| Goal | Establish initial platform baseline from a brief. |
| Work Unit | DESIGN-mode persona passes, MTS synthesis, readiness gates. |
| Actor | Team 2 genesis executor and design personas. |
| Verifier | Standards Engineer gates and deterministic readiness gate checker. |
| Governor | AUTH-001, AUTH-003, AUTH-004, AUTH-005, STD-000001, REG-000001. |
| Stop Condition | READY_WITH_KNOWN_CEILING or BLOCKED_BY_GATE. |
| Output Artefact | Genesis artefacts, run log, readiness result, issue status label. |
| Knowledge Update | Weak briefs, missing founder questions or design gaps route to lessons/amendments. |

---

## Pattern 4 — BUILD Loop

| Contract Field | Value |
|---|---|
| Trigger | BUILD mission issue against a sufficiently READY platform. |
| Goal | Produce a governed Engineering Delivery Package and release decision. |
| Work Unit | Proposal → TDA → EDP → Verification → Release → Knowledge Capture. |
| Actor | Team 2 forward-build personas and `run_build_chain.py`. |
| Verifier | TDA, Standards Engineer gates, Verification and Governance Director, Release Manager. |
| Governor | AUTH-001, AUTH-003, AUTH-008, AUTH-009, AUTH-010, STD-000005, OPR-000003 through OPR-000008. |
| Stop Condition | HALTED_BY_AUTHORITY, VERIFIER_FAILED, RELEASE_HOLD, RELEASE_REJECTED, DELIVERED_TO_TARGET, DELIVERY_FAILED. |
| Output Artefact | Proposal, TDA verdict, EDP, Verification Report, Scorecard, mission memory, issue comment/label, optional target PR. |
| Knowledge Update | Memory entry and lesson marker scan. |

---

## Pattern 5 — TDA Review Loop

| Contract Field | Value |
|---|---|
| Trigger | Engineering Proposal produced. |
| Goal | Approve, reject or require revision before delivery packaging. |
| Work Unit | Architectural review against available architecture evidence. |
| Actor | Chief Architect. |
| Verifier | TDA output is later consumed by workflow halt/release path and can be independently audited. |
| Governor | AUTH-001, OPR-000004, architecture artefacts. |
| Stop Condition | HALTED_BY_AUTHORITY or approval to continue. |
| Output Artefact | TDA verdict file and run log entry. |
| Knowledge Update | Architectural drift or missing evidence can become a lesson. |

---

## Pattern 6 — Verification Loop

| Contract Field | Value |
|---|---|
| Trigger | Engineering Delivery Package produced. |
| Goal | Determine whether acceptance criteria are genuinely addressed. |
| Work Unit | Criteria-by-criteria verification. |
| Actor | Verification and Governance Director. |
| Verifier | Release Manager must consume verification status and cannot release on FAIL. |
| Governor | OPR-000006, STD-000005, release safety rule. |
| Stop Condition | VERIFIER_FAILED, RELEASE_HOLD or continuation to release decision. |
| Output Artefact | Verification report and run log entry. |
| Knowledge Update | False criteria, missing tests or evidence gaps become lesson candidates. |

---

## Pattern 7 — Release Loop

| Contract Field | Value |
|---|---|
| Trigger | Verification report produced. |
| Goal | Decide RELEASE, HOLD or REJECT. |
| Work Unit | Release scorecard against quality, architecture, standards, operational fit and test coverage. |
| Actor | Release Manager. |
| Verifier | Workflow terminal-state labelling and optional cross-repo delivery result. |
| Governor | AUTH-009, OPR-000007, verification hard-stop rule. |
| Stop Condition | RELEASE_HOLD, RELEASE_REJECTED, DELIVERED_TO_TARGET or DELIVERY_FAILED. |
| Output Artefact | Release scorecard, issue label/comment, optional target PR. |
| Knowledge Update | Release rationale preserved; repeated HOLD/REJECT causes can become lessons. |

---

## Pattern 8 — Knowledge Capture Loop

| Contract Field | Value |
|---|---|
| Trigger | Mission reaches a terminal decision or halt. |
| Goal | Preserve what was learned and decide whether doctrine change is warranted. |
| Work Unit | Memory entry, lesson marker scan, REG-000010 review, OPR-000012 trigger if warranted. |
| Actor | Knowledge Capture operation and/or mission executor. |
| Verifier | Human/founder or domain persona judgement for doctrine amendment. |
| Governor | AUTH-010, OPR-000008, OPR-000012. |
| Stop Condition | COMPLETE, HUMAN_REQUIRED or doctrine amendment created. |
| Output Artefact | Memory entry, lesson register candidate, DAM amendment if required. |
| Knowledge Update | This pattern is itself the knowledge update mechanism. |

---

## Pattern 9 — Doctrine Drift Loop

| Contract Field | Value |
|---|---|
| Trigger | Sweep, review, failed reference, inconsistent status or founder challenge. |
| Goal | Align doctrine, scripts, workflows and registers. |
| Work Unit | Left-to-right and right-to-left trace check. |
| Actor | Verification and Governance Director / doctrine sweep script. |
| Verifier | Resolved references and amendment record. |
| Governor | AUTH-010, OPR-000012, STD-000005. |
| Stop Condition | COMPLETE, HUMAN_REQUIRED or BLOCKED_BY_GATE. |
| Output Artefact | Sweep report, DAM amendment, updated doctrine. |
| Knowledge Update | Lessons and amendment history. |

---

## Pattern 10 — Workflow Repair Loop

| Contract Field | Value |
|---|---|
| Trigger | Workflow ambiguity, bad label, failed branch condition or terminal-state defect. |
| Goal | Produce deterministic workflow behaviour for each distinct outcome. |
| Work Unit | Reproduce, simulate, fix, label, document. |
| Actor | Workflow maintainer / EMS script repair pass. |
| Verifier | Port-and-simulate or deterministic fixture test. |
| Governor | STD-000005, EMS terminal-state model, AUTH-010. |
| Stop Condition | COMPLETE, NO_PROGRESS or HUMAN_REQUIRED. |
| Output Artefact | Workflow patch, test evidence, amendment record. |
| Knowledge Update | Reusable failure mode captured as lesson. |
