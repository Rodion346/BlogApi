from uuid import UUID

from pydantic import BaseModel


class PostIn(BaseModel):
    title: str
    text: str
    id_user: UUID

    class Config:
        orm_mode: bool = True

class PostOut(BaseModel):
    id: UUID
    title: str
    text: str
    id_user: UUID

    class Config:
        orm_mode: bool = True