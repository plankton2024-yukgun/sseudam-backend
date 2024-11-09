import os
from sqlalchemy.orm import Session
from fastapi import UploadFile
from typing import List, Dict
from sqlalchemy import extract
import boto3
from .models import Post
from .schemas import PostCreate
from ..core.config import settings

# UPLOAD_DIR = os.getenv("UPLOAD_DIR")

# AWS S3 설정
S3_BASE_URL = f"https://{settings.S3_BUCKET}.s3.{settings.S3_REGION}.amazonaws.com/"

# S3 클라이언트 생성
s3_client = boto3.client(
    "s3",
    region_name=settings.S3_REGION,
)


def create_post(db: Session, post: PostCreate):
    db_post = Post(
        user_id=post.user_id,
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
    return db.query(Post).filter(Post.id == post_id).first()


# def save_image_locally(image: UploadFile):
#     # 저장할 파일 경로 생성
#     if not os.path.exists(UPLOAD_DIR):  # 경로가 존재하지 않으면
#         os.makedirs(UPLOAD_DIR)  # 디렉토리 생성
#
#     file_path = os.path.join(UPLOAD_DIR, image.filename)
#
#     # 파일을 지정한 경로에 저장
#     with open(file_path, "wb") as buffer:
#         buffer.write(image.file.read())
#
#     return file_path


def save_image_to_s3(image: UploadFile):
    # S3에 저장할 파일 경로
    file_path = f"images/{image.filename}"

    # S3에 파일 업로드
    s3_client.upload_fileobj(
        image.file, settings.S3_BUCKET, file_path, ExtraArgs={"ACL": "public-read"}
    )

    # 업로드된 파일의 URL 반환
    return S3_BASE_URL + file_path


def get_posts_by_month(
    user_id: int, year: int, month: int, db: Session
) -> Dict[int, List[int]]:
    # 해당 월의 게시물 조회
    posts = (
        db.query(Post)
        .filter(Post.user_id == user_id)
        .filter(extract("year", Post.created_at) == year)
        .filter(extract("month", Post.created_at) == month)
        .all()
    )

    # 각 날짜별로 업로드된 게시물들의 post_id를 모은 딕셔너리
    days_with_posts = {}
    for post in posts:
        day = post.created_at.day
        if day not in days_with_posts:
            days_with_posts[day] = []
        days_with_posts[day].append(post.id)

    return days_with_posts


# def get_posts(db: Session, board_type: str, skip: int = 0, limit: int = 10):
#     return (
#         db.query(Post)
#         .filter(Post.board_type == board_type)
#         .offset(skip)
#         .limit(limit)
#         .all()
#     )
