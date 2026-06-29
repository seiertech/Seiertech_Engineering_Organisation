# Platform Intake Mission Template

**Mission ID:**  
**Title:** Complete intake for [Platform Name]  
**Platform Name:**  
**Repository URL:**  
**Status:** Draft  
**Originator:** Founder  
**Mission Type:** Platform Intake

## Intake Command

```text
Complete intake for [Platform Name] — repo: [repo URL]
```

## Objective

Complete EMS onboarding for the named platform so that future missions can be safely issued against it.

## Required Discovery

- repository structure
- application architecture
- technology stack
- data model
- schema and persistence model
- existing documentation
- build and test setup
- known standards or governance artefacts
- open questions

## Persona Extraction Pass

Each EMS persona shall extract the platform information required for that persona to operate.

## Mission Spine Output

Create one file per persona under:

```text
platforms/[platform_name]/spine/
```

## Founder Questions

Where facts cannot be determined from repository evidence, record questions under:

```text
platforms/[platform_name]/questions/
```

## Completion Criteria

- Platform record complete
- Mission spine complete
- Open questions resolved
- Readiness Register updated
- Platform status set to Ready
