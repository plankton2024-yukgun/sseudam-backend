import os
from sqlalchemy.orm import Session
from fastapi import UploadFile
from .models import Post
from .schemas import PostCreate

UPLOAD_DIR = "uploaded_images/"


def create_post(db: Session, post: PostCreate):
    db_post = Post(
        board_type=post.board_type,
        content=post.content,
        location=post.location,
        image_url=post.image_url,
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_posts(db: Session, board_type: str):
    return db.query(Post).filter(Post.board_type == board_type).all()


def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.post_id == post_id).first()


def save_image_locally(image: UploadFile):
    file_path = os.path.join(UPLOAD_DIR, image.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(image.file.read())
    return file_path


# def get_posts(db: Session, board_type: str, skip: int = 0, limit: int = 10):
#     return (
#         db.query(Post)
#         .filter(Post.board_type == board_type)
#         .offset(skip)
#         .limit(limit)
#         .all()
#     )
