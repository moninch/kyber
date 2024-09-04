from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from datetime import datetime
from app.database import Base
from sqlalchemy.orm import relationship

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)  
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship('Users', back_populates='posts')