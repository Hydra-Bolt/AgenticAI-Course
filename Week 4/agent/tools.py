"""Simple internal tools the agent can choose from.

Demonstrates cost-conscious tool selection (Week4 principle).
"""
from __future__ import annotations
from typing import Dict
import math


def calculator(expression: str) -> str:
    try:
        # Restricted eval environment
        allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
        allowed_names.update({"__builtins__": {}})
        result = eval(expression, allowed_names, {})  # noqa: S307 (demo only, restricted)
        return str(result)
    except Exception as e:  # pragma: no cover - demo simplicity
        return f"CalculatorError: {e}"


KNOWLEDGE_BASE: Dict[str, str] = {
    "evaluation": "Evaluation improves reliability and trust via systematic metrics.",
    "safety": "Safety involves filtering harmful content, protecting privacy, and mitigating bias.",
    "ethics": "Ethical agent design centers user values, transparency, and accountability.",
}


def retrieve(keyword: str) -> str:
    return KNOWLEDGE_BASE.get(keyword.lower(), "KnowledgeNotFound")


def select_tools(user_input: str):
    # Very small heuristic: if input looks arithmetic -> calculator; if single word -> retrieval.
    import re
    if re.fullmatch(r"[0-9+\-*/(). ^]+", user_input.strip()):
        return ["calculator"]
    words = user_input.strip().split()
    if len(words) == 1:
        return ["retrieve"]
    return []


def execute_tools(tool_names, user_input: str):
    outputs = {}
    for name in tool_names:
        if name == "calculator":
            outputs[name] = calculator(user_input)
        elif name == "retrieve":
            outputs[name] = retrieve(user_input)
    return outputs
