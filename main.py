import uuid

from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from src.auth.auth import auth_backend
from src.auth.manage import get_user_manager
from src.auth.schemas import UserRead, UserCreate
from src.models.models import User
from src.pages.router import router


app: FastAPI = FastAPI()

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    tags=["auth"],
)




app.include_router(router)
