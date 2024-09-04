from fastapi import HTTPException
from sqlalchemy import delete
from app.dao.base import BaseDAO

from app.exceptions import PostNotFound
from app.posts.models import Posts

from app.database import async_session_maker

class PostsDAO(BaseDAO):

    model = Posts

    @classmethod
    async def delete_by_id(cls, post_id: int) -> None:

        async with async_session_maker() as session:
            query = delete(cls.model).where(cls.model.id == post_id)

            result = await session.execute(query)
            await session.commit()

            if result.rowcount == 0:
                raise PostNotFound
