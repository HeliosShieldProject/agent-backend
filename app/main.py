from fastapi import FastAPI

from app.routers import config_router

app = FastAPI()

app.include_router(config_router)
