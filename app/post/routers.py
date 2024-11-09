from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from . import services, schemas
from app.db import get_db

router = APIRouter()


@router.get("/", response_model=list[schemas.PostResponse])
def get_posts(
    board_type: str = "post",
    db: Session = Depends(get_db),
):
    posts = services.get_posts(db=db, board_type=board_type)
    return posts


# @router.get("/", response_model=list[schemas.PostResponse])
# def get_posts(
#     board_type: str = "post",
#     page: int = 1,
#     limit: int = 10,
#     db: Session = Depends(get_db),
# ):
#     skip = (page - 1) * limit
#     posts = services.get_posts(db=db, board_type=board_type, skip=skip, limit=limit)
#     return posts


@router.post("/", response_model=schemas.PostResponse)
async def upload_post(
    board_type: str,
    content: str,
    location: str,
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    image_path = services.save_image_locally(image)
    post = schemas.PostCreate(
        board_type=board_type, content=content, location=location, image_url=image_path
    )
    return services.create_post(db=db, post=post)


@router.get("/{post_id}", response_model=schemas.PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = services.get_post(db=db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
