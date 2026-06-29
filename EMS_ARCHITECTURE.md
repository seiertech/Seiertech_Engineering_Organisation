# SeierTech Engineering Management System Architecture

**Version:** 0.3.0  
**Status:** Draft  
**Classification:** EMS Architecture

## Purpose

This document defines the architectural pivot from a document repository to the SeierTech Engineering Management System.

The Engineering Management System is the controlled operating system for engineering work across SeierTech products and platforms.

## EMS Domains

The EMS is organised into the following domains:

1. Authorities
2. Registers
3. Libraries
4. Operations
5. Workforce
6. Platforms
7. Standards
8. Verification
9. Work Products

## Principle

Every durable engineering object shall be identifiable, traceable and reviewable.

No mission shall directly authorise implementation.

No build pack shall be created until an engineering proposal has passed the EMS review chain.

No build shall be considered deployable until it has passed Engineering Verification and Release Assurance.

## Authorities

Authorities define doctrine and controlling rules.

## Registers

Registers provide indexed truth for decisions, missions, proposals, platforms, roles, standards, risks, changes, releases and requirements.

## Libraries

Libraries contain reusable knowledge, patterns, evidence, vocabulary, lessons and reference material.

## Operations

Operations contain live engineering activity including missions, proposals, reviews, approvals, builds, verification, release assurance, releases and audits.

## Workforce

Workforce contains engineering roles and professional personas used to perform reviews and produce work products.

## Platforms

Platforms contain onboarded SeierTech products and their operating context.

## Standards

Standards define detailed engineering expectations derived from authorities.

## Verification

Verification is a first-class EMS domain.

It governs post-build engineering assurance, including code quality review, architecture conformance, security review, debt review, documentation review, standards compliance, performance review, regression review and release readiness.

Implementation systems do not self-certify. The EMS certifies release readiness through evidence-based verification.

## Work Products

Work Products are outputs produced during engineering missions, proposals, reviews, verification activities, release assurance and outcomes.

## EMS Lifecycle

```text
Mission
  ↓
Platform readiness check
  ↓
Engineering Proposal
  ↓
Specialist Persona Review
  ↓
Technical Design Authority
  ↓
Approved Design Package
  ↓
Build Pack
  ↓
Builder Branch
  ↓
Implementation
  ↓
Engineering Verification
  ↓
Scorecard
  ↓
Release Authority
  ↓
Final Merge or Commit Instruction
  ↓
Knowledge Capture
  ↓
Registers Updated
  ↓
Baseline Updated
```

## Operating Gates

Mission does not authorise build.

Mission authorises proposal generation.

Proposal does not authorise build.

Approved proposal authorises build pack generation.

Build does not authorise release.

Verification and scoring support the final merge or commit instruction.

## Status

This architecture supersedes the earlier folder-first repository design and establishes the EMS capability model.

Version 0.3.0 adds the mandatory proposal gate, scorecard gate and final merge or commit instruction.
