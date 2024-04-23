from sqlalchemy.types import Integer, String, Text
from sqlalchemy import Column,ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import List
from sqlalchemy.orm import relationship
from core.database.config import DATABASE_URL_asyncpg
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from datetime import datetime

engine = create_async_engine(
    url=DATABASE_URL_asyncpg,
    echo=True
)

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass

class DeleteDataHistory(Base):
    __tablename__="delete_data_history"

    id:Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column()
    delete_time: Mapped[datetime] = mapped_column()

class User(Base):
    __tablename__="users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(unique=True)

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    passwords:Mapped[list["Password"]] = relationship("Password", back_populates="user", lazy="selectin", cascade="all, delete-orphan")


class Password(Base):
    __tablename__="passwords"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    login: Mapped[str]
    password: Mapped[str]
    
    user_id = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="passwords")


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
