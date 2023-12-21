from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base

TABLE_NAME = "user"


class User(Base):
    """
    User model

    A user is a person who has access to the Collab environment.
    """

    __tablename__ = TABLE_NAME

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=False, nullable=False)
    email: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f"{self.username} - {self.email}"
