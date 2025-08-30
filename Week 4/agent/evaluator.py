"""Evaluation helpers implementing Week4 metrics.

Metrics:
 - latency_ms
 - input_tokens / output_tokens (rough estimate)
 - cost_estimate (simulated)
 - hallucination_suspected (heuristic)
 - success (heuristic based on non-empty output & safety)
"""
from __future__ import annotations
import json, os, time
from typing import Dict, Any
from .config import CONFIG


def estimate_tokens(text: str) -> int:
    # naive approximation 1 token ≈ 4 chars
    return max(1, len(text) // 4)


def estimate_cost(input_tokens: int, output_tokens: int) -> float:
    return round(
        input_tokens * CONFIG.input_token_cost
        + output_tokens * CONFIG.output_token_cost,
        6,
    )


def hallucination_heuristic(output_text: str) -> bool:
    # Demo rule: flag if contains disclaimers like "as an AI" (pretend model self-talk) or numbers >10k.
    if "as an ai" in output_text.lower():
        return True
    digits = [int(d) for d in __import__("re").findall(r"\b(\d{5,})\b", output_text)]
    return bool(digits)


def evaluate(start_ts: float, user_input: str, output_text: str, safety: Dict[str, Any]) -> Dict[str, Any]:
    end_ts = time.time()
    latency_ms = int((end_ts - start_ts) * 1000)
    in_tokens = estimate_tokens(user_input)
    out_tokens = estimate_tokens(output_text)
    cost = estimate_cost(in_tokens, out_tokens)
    hallucination = hallucination_heuristic(output_text)
    success = bool(output_text.strip()) and safety.get("safe", False)
    return {
        "latency_ms": latency_ms,
        "input_tokens": in_tokens,
        "output_tokens": out_tokens,
        "cost_estimate": cost,
        "hallucination_suspected": hallucination,
        "success": success,
    }


def append_log(record: Dict[str, Any]):
    os.makedirs(CONFIG.log_dir, exist_ok=True)
    with open(CONFIG.log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
