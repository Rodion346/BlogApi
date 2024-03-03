from uuid import UUID

from pydantic import BaseModel



class UsersIn(BaseModel):
    email: str
    username: str
    password: str

    class Config:
        orm_mode: bool = True

class UsersOut(BaseModel):
    id: UUID
    email: str
    username: str

    class Config:
        orm_mode: bool = True