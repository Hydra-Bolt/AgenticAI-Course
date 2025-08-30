# Responsible Demo Agent

Educational example agent module + Flask API + simple frontend illustrating Week 4 concepts: evaluation, safety, ethics, cost & transparency.

## Features
* Safety checks: profanity, rudimentary PII & bias term scan.
* Tool selection: picks calculator or knowledge retrieval when appropriate.
* Evaluation metrics: latency, token estimates, cost estimate, hallucination heuristic, success flag.
* JSONL logging for offline analysis in `logs/agent_runs.jsonl`.
* Frontend to interact & visualize metrics.

## Structure
```
agent/            # Reusable module
  config.py
  core.py
  safety.py
  evaluator.py
  tools.py
server.py         # Flask API (port 8000)
frontend/         # Static demo client
  index.html
  script.js
  style.css
requirements.txt
```

## Quick Start
Install deps (prefer venv):
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python server.py
```
Open `frontend/index.html` in a browser (or serve it) and interact.

## API
POST http://localhost:8000/api/agent
```json
{ "task": "general", "input": "2+2*10" }
```
Response (abridged):
```json
{
  "task": "general",
  "output": "ToolsUsed -> calculator: 22",
  "safety": { "safe": true, ... },
  "metrics": { "latency_ms": 3, ... }
}
```

## Logging & Evaluation
Each call appends a JSON line to `logs/agent_runs.jsonl`. You can later parse to compute aggregate success rate, average latency, etc.

## Ethical Notes / Limitations
This is a minimalist demo; safety heuristics are intentionally simple and MUST NOT be relied on in production. Replace with robust moderation, red-teaming, and human review for real deployments.

## Next Ideas
* Add proper LLM integration (OpenAI, Azure) with guarded prompt templates.
* Expand safety to include model-based classifiers.
* Add unit tests for evaluator & safety modules.
* Build analytics dashboard summarizing logs.

---
Educational use only.
