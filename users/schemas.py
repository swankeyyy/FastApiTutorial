from typing import Annotated

from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    name: Annotated[str, MinLen(3), MaxLen(30)]
    email: EmailStr
