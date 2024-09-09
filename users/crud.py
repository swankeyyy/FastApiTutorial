from .schemas import CreateUser


def create_user(user: CreateUser) -> dict:
    user = user.model_dump()
    return {
        "ready": True,
        "user": user
    }
