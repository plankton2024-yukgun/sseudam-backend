from pydantic import BaseModel
from datetime import datetime


class PostCreate(BaseModel):
    board_type: str
    content: str
    location: str = None
    image_url: str = None


class PostResponse(BaseModel):
    id: int
    board_type: str
    content: str
    location: str
    image_url: str
    created_at: datetime

    class Config:
        from_attributes = True
