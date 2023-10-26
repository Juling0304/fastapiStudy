import datetime

from pydantic import BaseModel, validator
from domain.board.board_posts_reply_schema import BoardPostsReplyResponse


class BoardPostsCreate(BaseModel):
    subject: str
    content: str
    @validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

class BoardPostsResponse(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    replys: list[BoardPostsReplyResponse]

    class Config:
        orm_mode = True

class BoardPostsListResponse(BaseModel):
    total: int = 0
    posts_list: list[BoardPostsResponse] = []