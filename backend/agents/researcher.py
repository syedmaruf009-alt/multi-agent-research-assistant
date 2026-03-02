# agents/researcher.py
#This agent depends on external tools, MCP is the GW
from mcp.server import MCPServer

def research_agent(state):
    # Extract the plan from the state
    plan = state["plan"]

    # Extract query cleanly
    query = plan.replace("SEARCH:", "").strip()
    mcp = MCPServer()
    # Call the web search tool with the query
    result = mcp.call_tool("web_search", query)
    state["research_result"] = result
    state["final_answer"] = result
    return state