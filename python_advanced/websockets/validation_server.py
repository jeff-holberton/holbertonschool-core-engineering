#!/usr/bin/env python3
"""Echo server"""
import asyncio
from websockets.asyncio.server import serve


async def connection_handler(websocket):
    async for message in websocket:
        if len(message.strip()) == 0:
            await websocket.send("ERR:EMPTY")
        else:
            await websocket.send(f"OK:{message}")


async def main():
    async with serve(connection_handler, "127.0.0.1", 8765) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
