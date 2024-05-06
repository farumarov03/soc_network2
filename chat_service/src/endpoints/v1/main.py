# Chat main 
from fastapi import APIRouter, Depends,  WebSocket, WebSocketDisconnect
from typing import Dict
from src.models import models
from src.modules.websocket_manager import ConnectionManager
import lib.acl as ACL
from src.modules import crud

router = APIRouter(prefix='/v1')

manager = ConnectionManager()


@router.get('/contacts')
async def get_user_contacts(payload: dict = Depends(ACL.JWTpayload)):
    return await crud.get_user_contacts()

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await manager.connect(user_id, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            receiver_id = data['receiver_id']
            message = data['message']
            await manager.send_personal_message(f"{message}", user_id, receiver_id)
    except WebSocketDisconnect:
        manager.disconnect(user_id)