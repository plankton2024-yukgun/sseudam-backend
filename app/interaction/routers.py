from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, services
from ..db import get_db

router = APIRouter()


@router.post(
    "/{post_id}/like", tags=["Interaction"], response_model=schemas.LikeResponse
)
def add_like(post_id: int, user_id: int, db: Session = Depends(get_db)):
    return services.add_like(db, post_id, user_id)


@router.delete(
    "/{post_id}/like", tags=["Interaction"], response_model=schemas.LikeResponse
)
def remove_like(post_id: int, user_id: int, db: Session = Depends(get_db)):
    return services.remove_like(db, post_id, user_id)


@router.post(
    "/{post_id}/comments/", tags=["Interaction"], response_model=schemas.CommentResponse
)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return services.create_comment(db, comment)


@router.delete(
    "/comments/{comment_id}",
    tags=["Interaction"],
)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    return services.delete_comment(db, comment_id)
