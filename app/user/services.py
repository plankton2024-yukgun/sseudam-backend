from sqlalchemy.orm import Session
from . import models, schemas
from ..post import models as post_models
from fastapi import HTTPException
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_all_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_user_posts(db: Session, user_post: schemas.UserPostsRequest):
    posts = (
        db.query(post_models.Post)
        .filter(post_models.Post.user_id == user_post.user_id)
        .filter(post_models.Post.board_type == user_post.board_type)
        .all()
    )
    return posts


# def get_user_posts(db: Session, user_id: int, page: int, limit: int):
#     skip = (page - 1) * limit
#     posts = (
#         db.query(post_models.Post)
#         .filter(post_models.Post.user_id == user_id)
#         .offset(skip)
#         .limit(limit)
#         .all()
#     )
#     return posts
