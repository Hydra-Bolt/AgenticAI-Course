"""Agent module exposing a safe, evaluable demo agent.

Public entrypoints:
 - run_agent(task: str, user_input: str) -> dict
 - get_version() -> str

Design Goals (Week4 principles):
 - Responsible defaults: safety + ethical checks before responding.
 - Evaluation hooks: automatic metrics & JSONL logging for analysis.
 - Transparency: structured response with metrics & flags.
 - Extensibility: clear, small abstraction layers (safety, tools, evaluator).
"""

from .core import run_agent, get_version

__all__ = ["run_agent", "get_version"]
