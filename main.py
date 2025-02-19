from fastapi import FastAPI, Request
from api.routes import api_router
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router)