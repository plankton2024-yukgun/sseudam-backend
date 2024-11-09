from app.db import SessionLocal


# TODO: 필요?
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
