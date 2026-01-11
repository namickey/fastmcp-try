import asyncio
from fastmcp import Client
import json

async def call():
    async with Client("http://localhost:8000/mcp") as client:

        # ツールリスト取得        
        result = await client.list_tools()
        print("Available tools:")
        print(result)
        print(result[0].name)

        # ツール呼び出し
        result = await client.call_tool("getAllTaskList", {"user_id": "user123"})
        print("Retrieved tasks:", result)
        
        # ツール呼び出し
        result = await client.call_tool("getCompleteTaskList", {"user_id": "user123"})
        print("Retrieved tasks:", result)
        
        # ツール呼び出し
        result = await client.call_tool("getUnCompleteTaskList", {"user_id": "user123"})
        print("Retrieved tasks:", result)

if __name__ == "__main__":
    asyncio.run(call())
