from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from .base import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .user import (
        User,
    )  # Чтобы не было циклического импорта, т.к. пост будет импортироваться в юзера


class Post(UserRelationMixin, Base):
    _user_back_populates = "posts"
    title: Mapped[str] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(
        Text,
        default="",  # когда новый экземпляр в алхимии
        server_default="",  # значение по умолчанию в БД
    )
