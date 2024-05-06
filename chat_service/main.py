from fastapi import FastAPI, Request,  WebSocket, WebSocketDisconnect
from src.endpoints.v1 import main as ws_v1
from fastapi.middleware.cors import CORSMiddleware
import time
import uvicorn
from typing import Dict

def create_application() -> FastAPI:
    application = FastAPI(
        title="SN platform",
        description="SN Chat Service.",
        version="1.0.0",
        openapi_url="/chat/openapi.json",
        docs_url="/chat/docs")
    application.include_router(ws_v1.router, prefix='/chat')
    return application


app = create_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def index():
    return {"title":"platform API",
    "description":"This API was built with FastAPI.",
    "version":"1.0.0"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8003)