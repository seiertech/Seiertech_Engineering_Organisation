"""
Anthropic Claude provider adapter.

Same interface as NIMProvider — persona/orchestration code calls .call()
identically regardless of which provider is selected. Uses the official
anthropic Python SDK if installed; raises a clear ProviderError with
install instructions if it is not, rather than failing with an
unhelpful ImportError deep in a persona pass.
"""

from __future__ import annotations

import os

from ems_engine.providers.base import AIProvider, ProviderError, ProviderResponse

DEFAULT_MODEL = "claude-sonnet-4-6"


class ClaudeProvider(AIProvider):
    name = "claude"
    default_model = DEFAULT_MODEL

    def __init__(self, api_key_env: str = "ANTHROPIC_API_KEY"):
        self.api_key_env = api_key_env
        self._client = None

    def is_configured(self) -> bool:
        return bool(os.environ.get(self.api_key_env))

    def _get_client(self):
        if self._client is not None:
            return self._client
        try:
            import anthropic
        except ImportError as e:
            raise ProviderError(
                self.name,
                "The 'anthropic' package is not installed. Add it to requirements "
                "(pip install anthropic) before selecting this provider.",
            ) from e

        api_key = os.environ.get(self.api_key_env)
        if not api_key:
            raise ProviderError(self.name, f"Missing API key in env var {self.api_key_env}")

        self._client = anthropic.Anthropic(api_key=api_key)
        return self._client

    def call(
        self,
        system_content: str,
        user_content: str,
        max_tokens: int = 4000,
        model: str | None = None,
    ) -> ProviderResponse:
        client = self._get_client()
        use_model = model or self.default_model

        try:
            response = client.messages.create(
                model=use_model,
                max_tokens=max_tokens,
                system=system_content,
                messages=[{"role": "user", "content": user_content}],
            )
            content = "".join(
                block.text for block in response.content if getattr(block, "type", None) == "text"
            )
            return ProviderResponse(
                content=content,
                provider_name=self.name,
                model=use_model,
                raw=response.model_dump() if hasattr(response, "model_dump") else None,
            )
        except Exception as e:
            raise ProviderError(self.name, str(e))
