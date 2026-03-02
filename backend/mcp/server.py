# mcp/server.py

from mcp.tools import mock_web_search

class MCPServer:
    """
    MCP Server mock.
    In production, this could be a remote service.
    """

    def call_tool(self, tool_name: str, input_data: str) -> str:    #Returns the result of specified tool with the input data.
        if tool_name == "web_search":   #One tool only
            return mock_web_search(input_data)

        raise ValueError(f"Unknown tool: {tool_name}")