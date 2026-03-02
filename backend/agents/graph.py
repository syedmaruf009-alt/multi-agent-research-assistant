# agents/graph.py

#Langgraph library for multi-step flow, data schema, nodes
from langgraph.graph import StateGraph
from agents.state import AgentState
from agents.planner import planner_agent
from agents.researcher import research_agent

def build_graph():
    #All nodes will pass around a shared state structured like AgentState
    graph = StateGraph(AgentState)

    #Name and functions for each node
    graph.add_node("planner", planner_agent)
    graph.add_node("researcher", research_agent)

    #Defines start and connection between nodes
    graph.set_entry_point("planner")
    graph.add_edge("planner", "researcher")

    #Converts the graph definition into an executable workflow object.
    return graph.compile()