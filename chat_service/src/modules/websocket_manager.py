from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Dict
from dbcontext.redis_manager import publish_event
import src.modules.crud as bl
import json

CHANEL = 'SUB_EVENTS'

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, user_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    def disconnect(self, user_id: str):
        del self.active_connections[user_id]

    async def send_personal_message(self, message: str, from_user: str, to_user_id: int):
        websocket = self.active_connections.get(to_user_id)
        if websocket:
            # send message to user if online
            await websocket.send_text(message)
        else:
            # send push notify if user offline
            await publish_event(CHANEL, json.dumps({"type": "2", "name": "message", "send_to": to_user_id}))

        # save to db
        await bl.save_message(from_user, to_user_id, message)