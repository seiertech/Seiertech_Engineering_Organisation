# NIM_INTEGRATION_CONFIG.md

| Field | Value |
|---|---|
| Artefact ID | INT-000001 |
| Artefact Class | Integration Configuration |
| Title | NVIDIA NIM Integration Configuration |
| Status | ACTIVE |
| Version | 1.0.0 |
| Classification | OPERATIONAL |
| Owner | SeierTech Engineering Organisation |
| Baseline | BASELINE-1.0 |

---

## 1. Purpose

Defines the NVIDIA NIM model configuration for the SeierTech EMS mission chain. This is the single source of truth for which model handles which tier of reasoning in the Loop Engineering system.

---

## 2. API Configuration

| Parameter | Value |
|---|---|
| Base URL | `https://integrate.api.nvidia.com/v1` |
| Chat Endpoint | `/chat/completions` |
| Auth Header | `Authorization: Bearer ${NIM_API_KEY}` |
| API Key Secret | `NIM_API_KEY` (GitHub Actions secret) |
| Content Type | `application/json` |

---

## 3. Model Tier Assignment

| Tier | Model | Use Cases |
|---|---|---|
| ORCHESTRATION | `nvidia/nemotron-3-super` | Mission planning, doctrine injection, EDP generation, proposal creation, spec generation, cross-workstream reasoning |
| SUB-AGENT | `nvidia/nemotron-3-nano` | Discrete tasks — metadata extraction, vocabulary checks, register updates, simple summarisation |
| CODE-SPECIALIST | `qwen/qwen3-coder-480b` | Code analysis during intake, agentic insertion identification, EDP build instruction generation |
| FUNCTION-CALLING | `mistral/mistral-nemotron` | Structured output generation, register updates, JSON payloads, tool calling within the chain |

---

## 4. Mission Type to Model Routing

| Mission Type | Primary Model | Secondary Model |
|---|---|---|
| INTAKE | nemotron-3-super | qwen3-coder-480b (for code scan) |
| BUILD | nemotron-3-super | qwen3-coder-480b (for EDP build instructions) |
| STRATEGIC | nemotron-3-super | — |
| REHAB | nemotron-3-super | qwen3-coder-480b |
| AGENTIC_INSERTION | nemotron-3-super | qwen3-coder-480b |
| PROPOSAL | nemotron-3-super | — |
| SPEC | nemotron-3-super | mistral-nemotron (structured output) |
| PARSE | nemotron-3-nano | — |
| REGISTER_UPDATE | mistral-nemotron | — |

---

## 5. Doctrine Injection Pattern

Every NIM call follows this system prompt structure:

```
[ENGINEERING CONSTITUTION — AUTH-001]
[VOCABULARY STANDARD — STD-000004]
[RELEVANT STANDARDS for this mission type]
[PLATFORM RECORD — for platform-specific missions]
[MISSION SPINE — persona-specific extractions]
[MISSION SPECIFICATION — the specific operation being executed]
```

This ensures every model call is fully doctrine-governed and platform-aware before any reasoning begins.

---

## 6. Context Window Management

| Model | Context Window | Strategy |
|---|---|---|
| nemotron-3-super | 1M tokens | Full doctrine + spine injection |
| nemotron-3-nano | 128K tokens | Targeted injection — relevant sections only |
| qwen3-coder-480b | 256K tokens | Code context + relevant standards |
| mistral-nemotron | 128K tokens | Structured output schema + minimal context |

---

## 7. Model Upgrade Path

When NVIDIA releases Nemotron 3 Ultra or a superior model, update the ORCHESTRATION tier model string in this file only. The entire chain upgrades automatically. No other changes required.

```
Current: nvidia/nemotron-3-super
Next:    nvidia/nemotron-3-ultra (when available)
```

---

## 8. Getting Started

1. Go to `build.nvidia.com`
2. Sign up — free, no credit card required
3. Generate API key
4. Add to GitHub repo: Settings → Secrets → Actions → New secret → `NIM_API_KEY`
5. The mission chain GitHub Action reads it automatically

---

## 9. Relationships

| Relationship | Artefact ID | Artefact Title |
|---|---|---|
| Governed By | AUTH-001 | Engineering Constitution |
| Required By | .github/workflows/ems-mission-chain.yml | Mission Chain Workflow |
| Consumes | All missions | Mission chain execution |

---

## 10. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Initial creation | SeierTech EMS |
