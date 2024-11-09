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


@router.post("/upload-image", tags=["Post"])
async def upload_image(image: UploadFile = File(...)):
    image_path = services.save_image_locally(image)
    return {"image_url": image_path}


@router.get("/", tags=["Post"], response_model=schemas.PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = services.get_post(db=db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.get("/calendar", response_model=schemas.CalendarResponse, tags=["Post"])
def get_calendar(calendar: schemas.CalendarRequest, db: Session = Depends(get_db)):
    days_with_posts = services.get_posts_by_month(
        calendar.user_id, calendar.year, calendar.month, db
    )

    return schemas.CalendarResponse(
        month=calendar.month, year=calendar.year, days_with_posts=days_with_posts
    )


# @router.get("/calendar", response_model=schemas.CalendarResponse, tags=["Post"])
# def get_calendar(user_id: int, year: int, month: int, db: Session = Depends(get_db)):
#     days_with_posts = services.get_posts_by_month(user_id, month, year, db)
#
#     return schemas.CalendarResponse(
#         month=month, year=year, days_with_posts=days_with_posts
#     )


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
