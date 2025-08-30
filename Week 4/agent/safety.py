"""Safety utilities: profanity, PII, bias heuristics.

Lightweight, dependency-free heuristics for demo purposes.
Real systems should leverage robust libraries & human review.
"""

from __future__ import annotations
import re
from typing import Dict, List

PROFANITY = {"badword", "dummy"}  # demo placeholder list

PII_PATTERNS = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "phone": re.compile(r"(?:\+?\d{1,3}[ -]?)?(?:\d{3}[ -]?){2}\d{4}"),
}


def scan_profanity(text: str) -> List[str]:
    lowered = re.findall(r"\b\w+\b", text.lower())
    return sorted({w for w in lowered if w in PROFANITY})


def scan_pii(text: str) -> Dict[str, List[str]]:
    findings: Dict[str, List[str]] = {}
    for label, pattern in PII_PATTERNS.items():
        matches = pattern.findall(text)
        if matches:
            findings[label] = matches[:3]  # limit for brevity
    return findings


def basic_bias_terms(text: str) -> List[str]:
    # Extremely naive: flag gendered pronouns for manual audit demonstration.
    bias_tokens = {
        "punjabi",
        "sindhi",
        "pathan",
        "balochi",
        "muhajir",
        "shia",
        "ahmadi",
        "hindu",
        "christian",
        "burger",
        "paindo",
    }
    lowered = re.findall(r"\b\w+\b", text.lower())
    found = sorted({w for w in lowered if w in bias_tokens})
    return found


def safety_check(text: str) -> Dict:
    profanity = scan_profanity(text)
    pii = scan_pii(text)
    bias = basic_bias_terms(text)
    safe = not profanity and not pii
    return {
        "safe": safe,
        "profanity": profanity,
        "pii": pii,
        "bias_terms": bias,
    }
