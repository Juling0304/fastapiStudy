from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.board import board_posts_schema, board_posts_reply_schema, board_crud
from domain.user.user_router import get_current_user
from models import User

router = APIRouter(
    prefix="/api/board",
)


@router.get("/posts/list", response_model=board_posts_schema.BoardPostsListResponse)
def posts_list(db: Session = Depends(get_db), page: int = 0, limit: int = 10):
    page = page - 1
    total, _posts_list = board_crud.get_posts_list(db, skip=page*limit, limit=limit)
    return { 'total': total, 'posts_list': _posts_list }

@router.get("/posts/detail/{posts_id}", response_model=board_posts_schema.BoardPostsResponse)
def posts_detail(posts_id: int, db: Session = Depends(get_db)):
    posts = board_crud.get_posts(db, posts_id=posts_id)
    return posts

@router.post("/reply/create", status_code=status.HTTP_204_NO_CONTENT)
def answer_create(reply_create: board_posts_reply_schema.BoardPostsReplyCreate,
                  db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    # create reply
    posts = board_crud.get_posts(db, posts_id=reply_create.posts_id)
    if not posts:
        raise HTTPException(status_code=404, detail="Posts not found")
    board_crud.create_posts_reply(db, posts=posts, reply_create=reply_create)

@router.post("/posts/create", status_code=status.HTTP_204_NO_CONTENT)
def posts_create(posts_create: board_posts_schema.BoardPostsCreate, db: Session = Depends(get_db)):
    board_crud.create_posts(db=db, posts_create=posts_create)

@router.get("dummy/posts/create", status_code=status.HTTP_204_NO_CONTENT)
def dummy_create(db: Session = Depends(get_db)):
    board_crud.dummy_create_posts(db)