from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, services
from ..db import get_db
from typing import List

router = APIRouter()


@router.get("/", tags=["User"], response_model=List[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return services.get_all_users(db)


@router.post("/", tags=["User"], response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.create_user(db, user)


@router.get("/{user_id}", tags=["User"], response_model=schemas.UserDetailResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return services.get_user(db, user_id)
