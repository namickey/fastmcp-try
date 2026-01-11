from fastmcp import FastMCP

# Create a server instance
mcp = FastMCP(name="MyTeamTaskManagementServer", instructions="This is a my team's task management server.")

@mcp.tool()
async def getUserIdList() -> list:
    """
    Get the list of users ids
    arguments: None
    returns: list of user ids
    """
    # ダミーデータを返す
    return ["suzuki", "tanaka", "yamada"]

@mcp.tool()
async def getAllTaskList(user_id: str) -> list:
    """
    Get the list of all tasks for a user
    arguments:
        user_id: str - The ID of the user
    returns: list of tasks
    """
    # ダミーデータを返す
    return ["Task 1", "Task 2", "Task 3"]

@mcp.tool()
async def getCompleteTaskList(user_id: str) -> list:
    """
    Get the list of completed tasks for a user
    arguments:
        user_id: str - The ID of the user
    returns: list of completed tasks"""
    # ダミーデータを返す
    return ["Task 1", "Task 2", "Task 3"]

@mcp.tool()
async def getUnCompleteTaskList(user_id: str) -> list:
    """
    Get the list of uncompleted tasks for a user
    arguments:
        user_id: str - The ID of the user
    returns: list of uncompleted tasks"""
    # ダミーデータを返す
    return []

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)
