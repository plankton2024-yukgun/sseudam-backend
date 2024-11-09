from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict


class PostCreate(BaseModel):
    user_id: int
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


class CalendarRequest(BaseModel):
    user_id: int
    year: int
    month: int


class CalendarResponse(BaseModel):
    year: int
    month: int
    days_with_posts: Dict[int, List[int]]
