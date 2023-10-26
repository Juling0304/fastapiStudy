from models import BoardPosts, BoardPostsReply
from domain.board.board_posts_reply_schema import BoardPostsReplyCreate
from domain.board.board_posts_schema import BoardPostsCreate
from sqlalchemy.orm import Session
from datetime import datetime


def get_posts_list(db: Session, skip: int = 0, limit: int = 10):
    posts_list = db.query(BoardPosts)\
        .order_by(BoardPosts.id.desc())
    total = posts_list.count()
    posts_list = posts_list.offset(skip).limit(limit).all()

    return total, posts_list

def get_posts(db: Session, posts_id: int):
    posts = db.query(BoardPosts).get(posts_id)
    return posts

def create_posts_reply(db: Session, posts: BoardPosts, reply_create: BoardPostsReplyCreate):
    db_reply = BoardPostsReply(posts = posts,
                                content = reply_create.content,
                                create_date = datetime.now())
    db.add(db_reply)
    db.commit()
    
def create_posts(db: Session, posts_create: BoardPostsCreate):
    db_posts = BoardPosts(subject= posts_create.subject, content = posts_create.content, create_date = datetime.now())
    db.add(db_posts)
    db.commit()

def dummy_create_posts(db:Session):
    for i in range(100):
        p = BoardPosts(subject='테스트 게시물 :[%03d]' % i, content='내용 없음', create_date=datetime.now())
        db.add(p)
    db.commit()