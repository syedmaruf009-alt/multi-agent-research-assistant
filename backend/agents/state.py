# agents/state.py
"""This file defines the shared state that
 all agents read from and write to collaborate."""
from typing import TypedDict

class AgentState(TypedDict):    #Fixed structured dict
    question: str
    plan: str
    research_result: str
    final_answer: str