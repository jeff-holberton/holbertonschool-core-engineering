#!/usr/bin/env python3
"""Broadcast server"""
import asyncio
from websockets.asyncio.server import serve, broadcast

connected_clients = set()


async def connection_handler(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            broadcast(connected_clients, f"B:{message}")
    finally:
        connected_clients.discard(websocket)


async def main():
    async with serve(connection_handler, "127.0.0.1", 8765) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
