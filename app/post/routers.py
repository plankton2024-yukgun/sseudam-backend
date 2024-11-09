from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from . import services, schemas
from app.db import get_db

router = APIRouter()


@router.get("/", tags=["Post"], response_model=list[schemas.PostResponse])
def get_posts(
    board_type: str = "post",
    db: Session = Depends(get_db),
):
    posts = services.get_posts(db=db, board_type=board_type)
    return posts


@router.post("/", tags=["Post"], response_model=schemas.PostResponse)
async def upload_post(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
):
    return services.create_post(db=db, post=post)


# TODO: 구현 필요
@router.post("/upload-image", tags=["Post"])
async def upload_image(image: UploadFile = File(...)):
    image_path = services.save_image_locally(image)
    return {"image_url": image_path}


@router.get("/{post_id}", tags=["Post"], response_model=schemas.PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = services.get_post(db=db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


# @router.get("/", tags=["Post"], response_model=list[schemas.PostResponse])
# def get_posts(
#     board_type: str = "post",
#     page: int = 1,
#     limit: int = 10,
#     db: Session = Depends(get_db),
# ):
#     skip = (page - 1) * limit
#     posts = services.get_posts(db=db, board_type=board_type, skip=skip, limit=limit)
#     return posts
