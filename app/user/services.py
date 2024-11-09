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

    post_count = (
        db.query(post_models.Post).filter(post_models.Post.user_id == user_id).count()
    )
    level = calculate_level(post_count)

    return schemas.UserDetailResponse(
        id=user.id,
        username=user.username,
        level=level,
        created_at=user.created_at,
    )

    return user


def get_user_posts(db: Session, user_post: schemas.UserPostsRequest):
    posts = (
        db.query(post_models.Post)
        .filter(post_models.Post.user_id == user_post.user_id)
        .filter(post_models.Post.board_type == user_post.board_type)
        .all()
    )
    return posts


# 플로깅 횟수별 계급 기준 리스트
level_thresholds = [
    0,  # 소위: 가입 시
    5,  # 중위: 누적 플로깅 5회 이상
    10,  # 대위: 누적 플로깅 10회 이상
    30,  # 소령: 누적 플로깅 30회 이상
    60,  # 중령: 누적 플로깅 60회 이상
    100,  # 대령: 누적 플로깅 100회 이상
    150,  # 준장: 누적 플로깅 150회 이상
    250,  # 소장: 누적 플로깅 250회 이상
    400,  # 중장: 누적 플로깅 400회 이상
    1000,  # 대장: 누적 플로깅 1,000회 이상
]


def calculate_level(plogging_count):
    # 각 횟수 기준에 맞는 계급을 순서대로 확인
    for level, threshold in enumerate(level_thresholds):
        if plogging_count < threshold:
            return level - 1
    # 최상위 계급은 모든 기준을 초과하는 경우
    return len(level_thresholds) - 1


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
