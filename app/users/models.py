from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True,nullable= False)
    login = Column(String,nullable= False)
    hashed_password = Column(String,nullable= False)

    posts = relationship('Posts', back_populates='author')

    def __str__(self) -> str:
        return f"Пользователь {self.login}"