# mcp/mock_search.py

def mock_web_search(query: str) -> str:
    """
    Fake web search tool.
    Returns hardcoded answers for learning purposes.
    """
    fake_results = {
        "capital of france": "The capital of France is Paris.",
        "capital of germany": "The capital of Germany is Berlin."
    }

    return fake_results.get(
        query.lower(),
        "No results found (mock search)."
    )