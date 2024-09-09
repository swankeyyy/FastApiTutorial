from fastapi import APIRouter
from .schemas import CreateUser
from users import crud

router = APIRouter(tags=["Users"], prefix="/users")


@router.post("/user")
def create_user(user: CreateUser):
    return crud.create_user(user)
