from sqlalchemy.types import Integer, String, Text
from sqlalchemy import Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import List
from sqlalchemy.orm import relationship
from config import Settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine(
    Settings.DATABASE_URL_asyncpg
)

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__="user"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(unique=True)
    is_deleted: Mapped[bool]
    passwords: Mapped[List["Password"]] = relationship(
         back_populates="user", cascade="all, delete-orphan"
     )


class Password(Base):
    __tablename__="password"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    login: Mapped[str]
    password: Mapped[str]
    user: Mapped["User"] = relationship(back_populates="passwords")

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)