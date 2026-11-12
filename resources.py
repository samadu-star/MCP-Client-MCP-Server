from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Resources")

@mcp.resource()
def get_inventory_overview() -> str:
    """
    Returns overview of inventory
    """

    overview = """
    Inventory overview:
    - Coffee
    - Tea
    - Cookies
    """
    return overview.strip()

if __name__ == "__main__":
    mcp.run()