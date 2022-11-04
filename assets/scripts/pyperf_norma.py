#!/usr/bin/env python3
import pyperf

setup_s = """
from norma2.__main__ import entrypoint
"""

runner = pyperf.Runner()
runner.timeit(
    name="norma2 playground",
    stmt="entrypoint(['playground', '--only-exit-code'])",
    setup=setup_s,
)
