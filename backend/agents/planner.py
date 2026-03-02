# agents/planner.py
def planner_agent(state):   #The shared state
    question = state["question"]

    # Simple, explicit plan for the research agent
    plan = f"SEARCH: {question}"

    #Writes plan to the shared state for the research agent to read
    state["plan"] = plan
    return state