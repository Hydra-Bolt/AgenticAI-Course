TOOLS = {
  "llm": lambda prompt: call_llm(prompt),
  # Missing: dedicated calculator, date_diff, currency fx, etc.
}

def solve(user_query):
    # BAD heuristic: always call LLM, even for numeric-only tasks
    prompt = f"Answer precisely: {user_query}" 
    result = TOOLS["llm"](prompt)
    log_cost(prompt, result)  # Only raw token count, no classification
    return result

queries = ["2+2", "What is 17*41?", "Days between 2024-11-01 and 2025-03-01?", "Summarize quantum computing news"]
for q in queries:
    print(q, '=>', solve(q))