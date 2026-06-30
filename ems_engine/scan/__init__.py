"""
Real repository scanning — shallow clone + file walk, not just metadata.

See scanner.py for scan_repository(), the importable entry point used by
the persona executor, and the original CLI behaviour preserved for the
existing GitHub Actions workflow.
"""

from ems_engine.scan.scanner import scan_repository

__all__ = ["scan_repository"]
