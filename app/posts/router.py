
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import TypeAdapter

from app.exceptions import (
    PostNotCreated,
    PostNotFound,
    UserAlreadyExists,
    TokenAbsent,
)
from app.posts.dao import PostsDAO
from app.posts.schemas import SPost
from app.users.auth import password_get_hash
from app.users.dependencies import get_current_user
from app.users.models import Users
from fastapi_cache.decorator import cache


router = APIRouter(
    prefix="/posts",
    tags=["Публикации"],
)


@router.post("/add_post")
async def create_post(
    title: str,
    content: str,
    category: Literal["rome", "garrysmod"],
    user: Users = Depends(get_current_user),
):
    await PostsDAO.add(
        title=title, content=content, author_id=user.id, category=category
    )


# Просмотр всех постов пользователя
@router.get("/user/{author_id}")
async def get_posts_by_user(author_id: int):
    return await PostsDAO.find_all(author_id=author_id)


# Просмотр вообще всех постов
@router.get("/all")
@cache(expire=30)
async def get_all_posts():
    return await PostsDAO.find_all()


# Просмотр постов по категории
@router.get("/category/{category}")
async def get_all_posts_by_category(category: Literal["rome", "garrysmod"]):
    return await PostsDAO.find_all(category=category)


# Удаление поста по его айди
@router.delete("/{post_id}")
async def delete_bookings(post_id: int, user: Users = Depends(get_current_user)):
    post = await PostsDAO.find_by_id(post_id)

    if post is None:
        raise PostNotFound

    # Проверяем, является ли текущий пользователь владельцем поста
    if post.author_id != user.id:
        raise TokenAbsent

    await PostsDAO.delete_model(post_id)

