from pydantic import BaseModel
from datetime import datetime
from typing import List
from ..post.schemas import PostResponse


class UserCreate(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    created_at: datetime

    class Config:
        from_attributes = True


class UserPostsResponse(BaseModel):
    user: UserResponse
    posts: List[PostResponse]

    class Config:
        from_attributes = True


class UserPostsRequest(BaseModel):
    user_id: str
    board_type: str
