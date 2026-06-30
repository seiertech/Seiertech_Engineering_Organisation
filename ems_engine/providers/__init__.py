"""
Provider adapters — one module per AI provider, all implementing the
common AIProvider interface defined in base.py.

Use router.get_provider() to resolve and instantiate the correct provider
rather than importing a specific adapter directly — this keeps calling
code provider-independent per AUTH-008 AI Governance Authority.
"""

from ems_engine.providers.base import AIProvider, ProviderError, ProviderResponse
from ems_engine.providers.router import get_provider, list_registered_providers, resolve_provider_name

__all__ = [
    "AIProvider",
    "ProviderError",
    "ProviderResponse",
    "get_provider",
    "list_registered_providers",
    "resolve_provider_name",
]
