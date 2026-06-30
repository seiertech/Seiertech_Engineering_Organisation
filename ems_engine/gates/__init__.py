"""
Deterministic readiness gate checking — RG-001 to RG-010 against real
artefact presence/content on disk, not LLM self-assessment.

See checker.py for check_readiness(), the importable entry point, tested
against both empty and populated platform directory fixtures to confirm
it correctly discriminates pass/fail rather than rubber-stamping.
"""

from ems_engine.gates.checker import check_readiness

__all__ = ["check_readiness"]
