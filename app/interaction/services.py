from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException


def add_like(db: Session, post_id: int, user_id: int):
    user_id = user_id
    like = models.Like(user_id=user_id, post_id=post_id)
    db.add(like)
    db.commit()
    db.refresh(like)
    like_count = db.query(models.Like).filter(models.Like.post_id == post_id).count()
    return {"post_id": post_id, "like_count": like_count}


def remove_like(db: Session, post_id: int, user_id: int):
    like = (
        db.query(models.Like)
        .filter(models.Like.user_id == user_id, models.Like.post_id == post_id)
        .first()
    )
    if not like:
        raise HTTPException(status_code=404, detail="Like not found")
    db.delete(like)
    db.commit()
    like_count = db.query(models.Like).filter(models.Like.post_id == post_id).count()
    return {"post_id": post_id, "like_count": like_count}


def create_comment(db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comment(
        content=comment.content, user_id=comment.user_id, post_id=comment.post_id
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def delete_comment(db: Session, comment_id: int):
    comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    db.delete(comment)
    db.commit()
    return {"status": "success", "message": "Comment deleted successfully"}
