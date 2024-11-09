from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    board_type = Column(String)
    content = Column(String)
    location = Column(String)
    image_url = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="posts")
    likes = relationship("Like", back_populates="post")
    comments = relationship("Comment", back_populates="post")


# class InfoPost(Base):
#     __tablename__ = "info_posts"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     content = Column(String)
#     image_url = Column(String)
#     created_at = Column(DateTime, default=datetime.datetime.utcnow)
#     user_id = Column(Integer, ForeignKey("users.id"))
#
#     user = relationship("User", back_populates="posts")
#
#
# class PartyPost(Base):
#     __tablename__ = "party_posts"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     content = Column(String)
#     location = Column(String)
#     image_url = Column(String)
#     created_at = Column(DateTime, default=datetime.datetime.utcnow)
#     user_id = Column(Integer, ForeignKey("users.id"))
#
#     user = relationship("User", back_populates="posts")
