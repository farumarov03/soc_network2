from fastapi import FastAPI
import threading
import uvicorn
from src.modules.listener_manager import redis_listener


def create_application() -> FastAPI:
    application = FastAPI(
        title="SN platform",
        description="SN Notify Service.",
        version="1.0.0",
        openapi_url="/notify/openapi.json",
        docs_url="/notify/docs")
    return application

app = create_application()



@app.on_event("startup")
def start_redis_listener():
    thread = threading.Thread(target=redis_listener, daemon=True)
    thread.start()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)
