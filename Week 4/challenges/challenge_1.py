class CostTracker:
    def __init__(self):
        self.total_tokens = 0
    def record(self, prompt_tokens, completion_tokens):
        self.total_tokens += (prompt_tokens + completion_tokens)

KB_DOCS = load_all_documents()  # Returns thousands of long docs

def build_context(question):
    # BAD: concatenates EVERYTHING each time
    return "\n\n".join(doc.text for doc in KB_DOCS) + f"\nUserQuestion: {question}" 

def answer(question, llm, cost: CostTracker):
    context = build_context(question)
    # Simulated token counts; real impl would parse model usage metadata
    prompt_tokens = len(context.split())
    completion = llm.generate(context)  # No system prompt, no grounding
    completion_tokens = len(completion.split())
    cost.record(prompt_tokens, completion_tokens)
    return completion

def batch_answer(questions, llm):
    cost = CostTracker()
    answers = [answer(q, llm, cost) for q in questions]
    print("TOTAL TOKENS:", cost.total_tokens)  # No per-Q breakdown, no cap
    return answers