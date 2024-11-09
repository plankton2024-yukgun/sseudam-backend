from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .core.config import settings


engine = create_engine(settings.DATABASE_URL)
# engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False}) # SQLite
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# 데이터베이스 세션 의존성 제공
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 데이터베이스 테이블을 초기화
def init_database():
    Base.metadata.create_all(bind=engine)


# 개발 환경에서 데이터베이스 초기화
def init_dev_db():
    try:
        init_database()
        print(f"Database initialized")
        return True
    except Exception as e:
        print(f"Database initialization error: {e}")
        return False
