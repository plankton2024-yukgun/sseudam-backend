from pydantic import BaseModel
from datetime import datetime


class CommentCreate(BaseModel):
    content: str


class CommentResponse(BaseModel):
    comment_id: int
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
