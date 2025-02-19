from api.routes import posts, integration
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(posts.router)
api_router.include_router(integration.router)
