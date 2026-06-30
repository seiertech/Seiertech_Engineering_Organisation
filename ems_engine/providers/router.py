"""
Provider router — selects which AI provider to use for a given call.

Selection precedence (highest to lowest priority):
  1. Explicit `provider` argument passed to get_provider()
  2. Per-platform override (platforms/[NAME]/PROVIDER_CONFIG.json, if present)
  3. EMS_DEFAULT_PROVIDER environment variable
  4. Fallback default: "nim" (the only provider validated end-to-end so far)

This keeps provider selection out of persona/orchestration code entirely —
that code just calls get_provider(...).call(...) and never needs to know
which concrete provider answered.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

from ems_engine.providers.base import AIProvider, ProviderError
from ems_engine.providers.claude import ClaudeProvider
from ems_engine.providers.nim import NIMProvider
from ems_engine.providers.openai import OpenAIProvider

_REGISTRY: dict[str, type[AIProvider]] = {
    "nim": NIMProvider,
    "claude": ClaudeProvider,
    "openai": OpenAIProvider,
}

FALLBACK_PROVIDER = "nim"


def _read_platform_override(platform_name: str | None) -> str | None:
    if not platform_name:
        return None
    config_path = Path(f"platforms/{platform_name.upper()}/PROVIDER_CONFIG.json")
    if not config_path.exists():
        return None
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config.get("provider")
    except Exception:
        # Malformed config should not crash provider selection — fall through
        # to the next precedence level rather than blocking a mission.
        return None


def resolve_provider_name(
    explicit: str | None = None,
    platform_name: str | None = None,
) -> str:
    if explicit:
        return explicit

    platform_override = _read_platform_override(platform_name)
    if platform_override:
        return platform_override

    env_default = os.environ.get("EMS_DEFAULT_PROVIDER")
    if env_default:
        return env_default

    return FALLBACK_PROVIDER


def get_provider(
    explicit: str | None = None,
    platform_name: str | None = None,
) -> AIProvider:
    """
    Resolve and instantiate the correct provider per the precedence rules
    above. Raises ProviderError if the resolved provider is not registered
    or is registered but not configured (e.g. missing API key) — fails
    loudly with a clear message rather than silently falling back, since
    a silent fallback to the wrong model is worse than a clear error.
    """
    name = resolve_provider_name(explicit, platform_name)

    if name not in _REGISTRY:
        raise ProviderError(
            name,
            f"Unknown provider '{name}'. Registered providers: {list(_REGISTRY.keys())}",
        )

    provider = _REGISTRY[name]()

    if not provider.is_configured():
        raise ProviderError(
            name,
            f"Provider '{name}' is registered but not configured "
            f"(missing API key or required setup). Check env vars.",
        )

    return provider


def list_registered_providers() -> list[str]:
    return list(_REGISTRY.keys())
