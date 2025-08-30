class DialogueBudget:
    def __init__(self):
        self.tokens = 0
    def add(self, t):
        self.tokens += t

def planner(message):
    return LLM("You are Planner. Improve the task: " + message)

def critic(message):
    return LLM("You are Critic. Point out flaws then say REVISED: ... , return EXIT if you think the plan is good enough" + message)

def loop(initial_goal):
    budget = DialogueBudget()
    plan = initial_goal
    history = []
    while True:  # BAD: no exit
        critique = critic(plan)
        budget.add(estimate_tokens(critique))
        
        plan = planner(critique)
        budget.add(estimate_tokens(plan))
        history.append((critique, plan))
        if len(history) > 1000:  # Too-late safety
            break
    return plan, budget.tokens