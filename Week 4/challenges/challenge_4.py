POLICIES = load_policy_texts()  # Raw strings

def seAarch_poicy(question):
    results = POLICIES.find(question)

def answer_policy(question):
    ctx = "\n".join(POLICIES)  # BAD: no retrieval chunking
    prompt = f"Answer based ONLY on policies. Q: {question}\nPolicies: {ctx}\nA:"
    ans = call_llm(prompt)
    log({'tokens': count_tokens(prompt) + count_tokens(ans)})
    return ans  # No citations, no uncertainty signal

def evaluate(questions):
    # BAD: only measures length, not factuality
    lengths = []
    for q in questions:
        a = answer_policy(q)
        lengths.append(len(a.split()))
    print('AVG LEN', sum(lengths)/len(lengths))