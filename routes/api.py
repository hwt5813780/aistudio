from fastapi import APIRouter
from app.http.api import demo
from app.http.api import auth
from app.http.api import users
from app.http.api import gpt
from app.http.api import ocr

api_router = APIRouter()

api_router.include_router(demo.router, tags=["demo"])

api_router.include_router(auth.router, tags=["auth"])

api_router.include_router(users.router, tags=["users"])

api_router.include_router(gpt.router, tags=["gpt"])

api_router.include_router(ocr.router, tags=["ocr"])