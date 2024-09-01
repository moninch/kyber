
from typing import Literal
from fastapi import APIRouter, Depends, HTTPException,status
from pydantic import TypeAdapter

from app.exceptions import PostNotCreatedException, UserAlreadyExistsException
from app.posts.dao import PostsDAO
from app.posts.schemas import SPost
from app.users.auth import password_get_hash
from app.users.dependencies import get_current_user
from app.users.models import Users


router = APIRouter(
    prefix='/posts',
    tags = ["Публикации"]
)

#Добавление публикации
@router.post("/add_post")
async def create_post( 
    title: str,
    content: str,
    category: Literal["rome", "garrysmod"],
    user: Users = Depends(get_current_user)):
    await PostsDAO.add(title = title, content=content,author_id = user.id,category = category)
    

#Чтобы чел мог посмотреть посты пользователя
@router.get('/user/{author_id}')
async def get_posts_by_user(author_id: int):
    return await PostsDAO.find_all(author_id = author_id)

@router.get('/all')
async def get_all_posts():
    return await PostsDAO.find_all()

@router.get('/category/{category}')
async def get_all_posts_by_category(category: Literal["rome", "garrysmod"]):
    return await PostsDAO.find_all(category = category)

@router.delete("/{post_id}")
async def delete_bookings(post_id: int, user: Users = Depends(get_current_user)):
    post = await PostsDAO.find_by_id(post_id)

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    # Проверяем, является ли текущий пользователь владельцем поста
    if post.author_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this post")
    
    await PostsDAO.delete_model(post_id)

