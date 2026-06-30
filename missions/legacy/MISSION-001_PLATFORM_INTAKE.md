# MISSION-001 – Platform Intake

**Mission ID:** MISSION-001  
**Title:** Platform Intake  
**Status:** Draft  
**Mission Type:** Platform Onboarding  
**Parent EMS Concept:** Loop Engineering

## Purpose

Platform Intake is the mandatory onboarding mission that must complete before any engineering mission can be issued against a platform.

A platform is not mission-ready until its platform record, readiness state and mission spine are complete.

## Intake Command Format

```text
Complete intake for [Platform Name] — repo: [repo URL]
```

## Intake Flow

```text
Founder issues intake mission
  ↓
Repo scan
  ↓
Structure and documentation discovery
  ↓
Data model and schema discovery
  ↓
Authority and standards reasoning
  ↓
Platform record populated
  ↓
Persona extraction pass
  ↓
Mission spine generated
  ↓
Founder questions raised if required
  ↓
Readiness register updated
  ↓
Platform missions unlocked only when complete
```

## Required Outputs

- Platform record under `platforms/[platform_name]/`
- Persona spine files under `platforms/[platform_name]/spine/`
- Open founder questions where evidence is incomplete
- Readiness Register update
- Mission Register update

## Locking Rule

No mission may be issued against a platform until Platform Intake is complete and the Readiness Register shows the platform as ready.

## Persona Extraction Rule

Each EMS persona shall extract the platform information it requires to operate effectively.

The combined persona outputs form the Mission Spine.

## Loop Engineering Context

Loop Engineering is the closed-loop operating model where doctrine governs personas, personas execute missions, missions produce builds, builds are verified, verification feeds back into registers and memory, and the loop tightens over time.

Git is the source of truth. The EMS is the governance layer. NIM/Nemotron may power the chain. Kiro executes approved builds.
