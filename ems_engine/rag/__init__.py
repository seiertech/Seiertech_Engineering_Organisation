"""
RAG (Chroma) layer — NOT YET BUILT.

This is Step 4 of PYTHON_ENGINE_BUILD_PLAN.md. Deliberately left as a
placeholder rather than built unsupervised, because it involves real
architectural decisions that should be confirmed with the founder first:

- Collection structure (shared doctrine collection vs per-platform
  namespacing — the plan recommends per-platform namespacing to prevent
  context bleed between platforms, but this should be confirmed)
- Chunking strategy for doctrine documents (whole-file vs section-level)
- Embedding model choice
- Whether to index spine/scan-evidence automatically on every intake run,
  or as a separate explicit step

Per the build plan: prove standalone retrieval against the 16 doctrine
files BEFORE coupling this into the persona executor (Step 5). Do not
build Step 5's dependency on this module until that proof exists.
"""
