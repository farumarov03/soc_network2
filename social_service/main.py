from fastapi import FastAPI, Request
from src.endpoints.v1 import main as social_v1
from fastapi.middleware.cors import CORSMiddleware
import time
import uvicorn

def create_application() -> FastAPI:
    application = FastAPI(
        title="SN platform",
        description="SN Social Service.",
        version="1.0.0",
        openapi_url="/social/openapi.json",
        docs_url="/social/docs")
    application.include_router(social_v1.router, prefix='/social')
    return application

app = create_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    response.headers["X-Process-App"] = "Time took to process the request and return response is {} sec".format(time.time() - start_time)
    return response


@app.get('/')
def index():
    return {"title":"platform API",
    "description":"This API was built with FastAPI.",
    "version":"1.0.0"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)