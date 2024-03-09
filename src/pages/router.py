import uuid

from fastapi_users import FastAPIUsers
from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from src.auth.auth import auth_backend
from src.auth.manage import get_user_manager
from src.models.models import User

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

router = APIRouter(tags=["Pages"])

temp = Jinja2Templates(directory="src/templates")

@router.get("/")
def get_base(request: Request):
    return temp.TemplateResponse("base_non.html", {"request": request})

@router.get("/registration")
def get_reg(request: Request):
    return temp.TemplateResponse("newuser.html", {"request": request})

@router.get("/loging")
def get_reg(request: Request):
    return temp.TemplateResponse("login.html", {"request": request})


current_user = fastapi_users.current_user()

@router.get("/protected-route")
def protected_route(request: Request, user: User = Depends(current_user)):
    if user.email:
        return temp.TemplateResponse("user.html", {"request": request})