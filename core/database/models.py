from typing import List, Optional
from sqlalchemy import Text, String, DateTime, func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    date_created: Mapped[DateTime] = mapped_column(DateTime,
                                                   default=func.now())  # func.now() - подтягивает текущее время
    date_updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Instructions(Base):
    __tablename__ = 'instructions'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    is_published: Mapped[int] = mapped_column(default=1)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    photo_1: Mapped[Optional[str]] = mapped_column(String(150))
    photo_2: Mapped[Optional[str]] = mapped_column(String(150))
    photo_3: Mapped[Optional[str]] = mapped_column(String(150))
    photo_4: Mapped[Optional[str]] = mapped_column(String(150))
    photo_5: Mapped[Optional[str]] = mapped_column(String(150))
    photo_6: Mapped[Optional[str]] = mapped_column(String(150))
    photo_7: Mapped[Optional[str]] = mapped_column(String(150))
    photo_8: Mapped[Optional[str]] = mapped_column(String(150))
    photo_9: Mapped[Optional[str]] = mapped_column(String(150))
    photo_10: Mapped[Optional[str]] = mapped_column(String(150))


class Problems(Base):
    __tablename__ = 'problems'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    is_published: Mapped[int] = mapped_column(default=1)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    decision: Mapped[str] = mapped_column(Text, nullable=False)
    photo_1: Mapped[Optional[str]] = mapped_column(String(150))
    photo_2: Mapped[Optional[str]] = mapped_column(String(150))
    photo_3: Mapped[Optional[str]] = mapped_column(String(150))
    photo_4: Mapped[Optional[str]] = mapped_column(String(150))
    photo_5: Mapped[Optional[str]] = mapped_column(String(150))
    photo_6: Mapped[Optional[str]] = mapped_column(String(150))
    photo_7: Mapped[Optional[str]] = mapped_column(String(150))
    photo_8: Mapped[Optional[str]] = mapped_column(String(150))
    photo_9: Mapped[Optional[str]] = mapped_column(String(150))
    photo_10: Mapped[Optional[str]] = mapped_column(String(150))


class user(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(300), nullable=False)
