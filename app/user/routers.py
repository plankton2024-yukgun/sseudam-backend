from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, services
from ..db import get_db
from typing import List

router = APIRouter()


@router.get("/users/", response_model=List[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return services.get_all_users(db)


@router.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.create_user(db, user)


@router.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return services.get_user(db, user_id)


@router.get("/users/{user_id}/posts/", response_model=List[schemas.PostResponse])
def get_user_posts(user_post: schemas.UserPostsRequest, db: Session = Depends(get_db)):
    return services.get_user_posts(db, user_post) @ router.get(
        "/users/{user_id}/posts/", response_model=List[schemas.PostResponse]
    )


# def get_user_posts(
#     user_id: int, page: int = 1, limit: int = 10, db: Session = Depends(get_db)
# ):
#     return services.get_user_posts(db, user_id, page, limit)
