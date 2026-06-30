"""
Provider abstraction — the common interface every AI provider adapter implements.

The EMS Engine must remain provider-independent (AUTH-008 AI Governance
Authority: "The EMS is model-agnostic at the execution layer"). Persona
execution code should depend on this interface, never on a specific
provider's SDK or API shape directly.

Adding a new provider means implementing this interface — it should never
require changes to persona or orchestration code.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ProviderResponse:
    """Normalised response shape, regardless of which provider produced it."""
    content: str
    provider_name: str
    model: str
    raw: dict | None = None  # original provider response, for debugging only


class ProviderError(Exception):
    """Raised when a provider call fails. Callers should catch this, not
    provider-specific exceptions, to stay provider-independent."""

    def __init__(self, provider_name: str, message: str, status_code: int | None = None):
        self.provider_name = provider_name
        self.status_code = status_code
        super().__init__(f"[{provider_name}] {message}")


class AIProvider(ABC):
    """
    Every provider adapter (NIM, Claude, OpenAI, ...) must implement this
    interface. Persona executor code calls `.call()` and never needs to
    know which concrete provider it is talking to.
    """

    name: str = "unnamed-provider"
    default_model: str = ""

    @abstractmethod
    def call(
        self,
        system_content: str,
        user_content: str,
        max_tokens: int = 4000,
        model: str | None = None,
    ) -> ProviderResponse:
        """
        Make a single-turn system+user call and return a normalised response.

        Must raise ProviderError (not a provider-specific exception) on
        failure, so calling code can handle errors uniformly.
        """
        raise NotImplementedError

    def is_configured(self) -> bool:
        """Return True if this provider has the credentials/config it needs
        to be called (e.g. API key present in environment). Used by the
        router to skip providers that aren't set up rather than failing
        loudly when a provider simply isn't configured for this environment."""
        return True
