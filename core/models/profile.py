from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from .mixins import UserRelationMixin
from .base import Base


class Profile(UserRelationMixin, Base):
    _user_back_populates = "profile"
    _user_id_unique = True
    firstname: Mapped[str | None] = mapped_column(String(40), unique=False)
    lastname: Mapped[str | None] = mapped_column(String(40), unique=False)
    bio: Mapped[str | None]
