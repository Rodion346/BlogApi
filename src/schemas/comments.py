from uuid import UUID

from pydantic import BaseModel


class CommentIn(BaseModel):
    author_id: UUID
    text: str
    post_id: UUID

    class Config:
        orm_mode: bool = True


class CommentOut(BaseModel):
    id: UUID
    author_id: UUID
    text: str
    post_id: UUID

    class Config:
        orm_mode: bool = True