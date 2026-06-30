"""
SeierTech EMS Engine — Python orchestration layer for the EMS operating model.

This package executes the EMS doctrine (constitution, authorities, standards,
missions, operations, personas, registers). It does not define or replace
that doctrine — the doctrine in standards/, authorities/, agents/, missions/,
operations/ remains authoritative.

Git remains the system of record. The AI providers (NIM, Claude, OpenAI, ...)
provide reasoning only, behind a common provider interface so the EMS is not
locked to any single model vendor.

See PYTHON_ENGINE_BUILD_PLAN.md in the repo root for the build plan and
sequencing decisions behind this package's structure.
"""

__version__ = "0.1.0"
