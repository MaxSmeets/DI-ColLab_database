from datetime import datetime
from sqlalchemy import Integer, DateTime, String
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base
from .user import TABLE_NAME as USER_TABLE_NAME, User

TABLE_NAME = "session"


class Session(Base):
    """
    Session model

    A session is created when a user logs in and monitors the user's
    last known activity within the Collab environment.
    """

    __tablename__ = TABLE_NAME

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey=f"{USER_TABLE_NAME}.id")
    creation_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    last_activity: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    last_known_location: Mapped[str] = mapped_column(String(80))

    user: Mapped[User] = mapped_column(User)

    def __repr__(self):
        return f"{self.user.username} - {self.creation_date} - {self.last_activity}"
