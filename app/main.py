from contextlib import asynccontextmanager
from datetime import datetime
import time
from typing import AsyncIterator

from fastapi import Depends, FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


from app.users.router import router as router_users
from app.posts.router import router as router_posts
from app.images.router import router as router_images
from app.config import settings
from app.database import engine

app = FastAPI()

app.include_router(router_users)
app.include_router(router_posts)
app.include_router(router_images)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)
