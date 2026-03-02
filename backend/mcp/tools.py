# mcp/tools.py

def mock_web_search(query: str) -> str:
    """
    MCP Tool: Mock Web Search
    This simulates an external tool exposed via MCP.
    """

    query = query.lower()

    if "capital" in query and "india" in query:
        return "The capital of India is New Delhi."

    if "capital" in query and "france" in query:
        return "The capital of France is Paris."

    if "capital" in query and "germany" in query:
        return "The capital of Germany is Berlin."

    return "No results found (mock MCP search)."
    #Fallback response for unrecognized queries