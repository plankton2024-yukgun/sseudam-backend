from pydantic import BaseModel
from datetime import datetime


class CommentCreate(BaseModel):
    post_id: int
    user_id: int
    content: str


class CommentResponse(BaseModel):
    id: int
    post_id: int
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class LikeResponse(BaseModel):
    post_id: int
    like_count: int

    class Config:
        from_attributes = True
