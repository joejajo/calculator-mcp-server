import os
import calculator_server

if __name__ == "__main__":
    # Render will pass the port in the PORT env variable
    port = int(os.environ.get("PORT", "8000"))

    # Expose the MCP server over Streamable HTTP
    # This will serve MCP at: http://0.0.0.0:<port>/mcp
    calculator_server.mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port,
    )
