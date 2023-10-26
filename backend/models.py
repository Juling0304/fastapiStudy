from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class BoardPosts(Base):
    __tablename__ = "BOARD_POSTS"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)

class BoardPostsReply(Base):
    __tablename__ = "BOARD_POSTS_REPLY"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    posts_id = Column(Integer, ForeignKey("BOARD_POSTS.id"))
    posts = relationship("BoardPosts", backref="replys")

class User(Base):
    __tablename__ = "USER"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)