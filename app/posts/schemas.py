from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class SPost(BaseModel):
    id : int
    title : str
    content : str
    author : str
    category : Literal["rome", "garrysmod"]
    created_at : datetime
    updated_at : datetime

    class Config:
        arbitrary_types_allowed = True