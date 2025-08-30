"""Configuration for the demo agent.

Central place to adjust safety thresholds, logging paths, and cost factors.
"""
from __future__ import annotations
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AgentConfig:
    model_name: str = "demo-local-echo"
    log_dir: str = "logs"
    log_file: str = "agent_runs.jsonl"
    # naive token cost estimate factors
    input_token_cost: float = 0.000_001  # pretend $ per token
    output_token_cost: float = 0.000_002
    max_input_chars: int = 4000
    enable_bias_mitigation: bool = True
    enable_basic_pii_scan: bool = True
    enable_profanity_filter: bool = True

    @property
    def log_path(self) -> str:
        return os.path.join(self.log_dir, self.log_file)


CONFIG = AgentConfig()
