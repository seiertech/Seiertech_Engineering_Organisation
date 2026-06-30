"""
OpenAI provider adapter.

STATUS: STUB — same interface shape as NIMProvider/ClaudeProvider, written
to the documented OpenAI chat completions API shape, but NOT validated
against a live call (no API key available in this environment). Treat as
unverified until a real call has been made and confirmed working.
"""

from __future__ import annotations

import os

from ems_engine.providers.base import AIProvider, ProviderError, ProviderResponse

DEFAULT_MODEL = "gpt-4o"


class OpenAIProvider(AIProvider):
    name = "openai"
    default_model = DEFAULT_MODEL

    def __init__(self, api_key_env: str = "OPENAI_API_KEY"):
        self.api_key_env = api_key_env
        self._client = None

    def is_configured(self) -> bool:
        return bool(os.environ.get(self.api_key_env))

    def _get_client(self):
        if self._client is not None:
            return self._client
        try:
            import openai
        except ImportError as e:
            raise ProviderError(
                self.name,
                "The 'openai' package is not installed. Add it to requirements "
                "(pip install openai) before selecting this provider.",
            ) from e

        api_key = os.environ.get(self.api_key_env)
        if not api_key:
            raise ProviderError(self.name, f"Missing API key in env var {self.api_key_env}")

        self._client = openai.OpenAI(api_key=api_key)
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
            response = client.chat.completions.create(
                model=use_model,
                max_tokens=max_tokens,
                messages=[
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": user_content},
                ],
            )
            content = response.choices[0].message.content or ""
            return ProviderResponse(
                content=content,
                provider_name=self.name,
                model=use_model,
                raw=response.model_dump() if hasattr(response, "model_dump") else None,
            )
        except Exception as e:
            raise ProviderError(self.name, str(e))
