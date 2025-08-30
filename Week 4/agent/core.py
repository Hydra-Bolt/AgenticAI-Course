"""Core agent orchestration."""
from __future__ import annotations
import time
from typing import Dict, Any
from .config import CONFIG
from . import safety
from . import tools
from .evaluator import evaluate, append_log

VERSION = "0.1.0"


def get_version() -> str:
    return VERSION


def truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 20] + "... [TRUNCATED]"


def generate_response(user_input: str, tool_results: Dict[str, str]) -> str:
    if tool_results:
        parts = [f"{k}: {v}" for k, v in tool_results.items()]
        tool_section = " | ".join(parts)
        return f"ToolsUsed -> {tool_section}"
    # Fallback reflective echo style
    return f"Echo: {user_input.strip()}"


def run_agent(task: str, user_input: str) -> Dict[str, Any]:
    start = time.time()
    original_input = user_input or ""
    user_input = truncate(original_input, CONFIG.max_input_chars)

    safety_result = safety.safety_check(user_input)
    selected_tools = [] if not safety_result.get("safe", True) else tools.select_tools(user_input)
    tool_outputs = tools.execute_tools(selected_tools, user_input) if selected_tools else {}
    output_text = generate_response(user_input, tool_outputs)
    metrics = evaluate(start, user_input, output_text, safety_result)

    record = {
        "task": task,
        "input": user_input,
        "output": output_text,
        "safety": safety_result,
        "metrics": metrics,
        "version": VERSION,
    }
    append_log(record)
    return record
