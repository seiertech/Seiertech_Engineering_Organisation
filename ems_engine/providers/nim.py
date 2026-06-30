"""
NVIDIA NIM provider adapter.

Wraps the same call logic validated earlier in .github/scripts/call_nim.py
and run_intake_chain.py behind the common AIProvider interface. Behaviour
is unchanged from the validated version — this is a relocation + interface
wrap, not a rewrite of the working logic.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request

from ems_engine.providers.base import AIProvider, ProviderError, ProviderResponse

NIM_API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
DEFAULT_MODEL = "nvidia/nemotron-3-super"


class NIMProvider(AIProvider):
    name = "nim"
    default_model = DEFAULT_MODEL

    def __init__(self, api_key_env: str = "NIM_API_KEY"):
        self.api_key_env = api_key_env

    def is_configured(self) -> bool:
        return bool(os.environ.get(self.api_key_env))

    def call(
        self,
        system_content: str,
        user_content: str,
        max_tokens: int = 4000,
        model: str | None = None,
    ) -> ProviderResponse:
        api_key = os.environ.get(self.api_key_env)
        if not api_key:
            raise ProviderError(self.name, f"Missing API key in env var {self.api_key_env}")

        use_model = model or self.default_model

        payload = {
            "model": use_model,
            "max_tokens": max_tokens,
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
        }
        data = json.dumps(payload).encode("utf-8")

        req = urllib.request.Request(
            NIM_API_URL,
            data=data,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                body = resp.read().decode("utf-8")
                result = json.loads(body)
                content = result["choices"][0]["message"]["content"]
                return ProviderResponse(
                    content=content,
                    provider_name=self.name,
                    model=use_model,
                    raw=result,
                )
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")
            raise ProviderError(self.name, f"HTTP {e.code}: {err_body}", status_code=e.code)
        except Exception as e:
            raise ProviderError(self.name, str(e))
