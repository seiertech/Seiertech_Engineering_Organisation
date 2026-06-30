"""
Persona executor — NOT YET BUILT.

This is Step 5 of PYTHON_ENGINE_BUILD_PLAN.md. Deliberately left as a
placeholder rather than built unsupervised, because it depends on
ems_engine.rag (Step 4, also not yet built) and involves real decisions
about the persona dependency graph and concurrency model that should be
confirmed with the founder:

- Which personas can genuinely run concurrently (only those with no
  data dependency on each other's output — get this wrong and outputs
  become incoherent, see PYTHON_ENGINE_BUILD_PLAN.md "Concurrency" section)
- How persona definitions in agents/team-1-baseline/ and
  agents/team-2-forward/ map to executable configuration
- Whether the existing 5 grouped passes in run_intake_chain.py become the
  initial persona registry entries (recommended — regression-safe) or are
  redesigned at the same time (higher risk)

What providers/, scan/, and gates/ give this module once it is built:
provider-independent AI calls (providers/), real repo evidence (scan/),
and real readiness verification (gates/) — all already available and
tested.
"""
