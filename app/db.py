# Used to declare async generator return types
from collections.abc import AsyncGenerator
# For generating unique ids
import uuid

# Column tyypes and constraints
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from datetime import datetime
# postgresql specific type uuis, could have used uuid imported before
from sqlalchemy.dialects.postgresql import UUID
# Async database engine and session utilities for non‑blocking DB operations.
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
# used for declaring SQLalchemy orm models in fastapi, improves readability, type safety. Defines relationships between tables.
from sqlalchemy.orm import DeclarativeBase, relationship

# Connection string for SQLite. DB file name will be test.db
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

class Base(DeclarativeBase):
    pass

# ORM   
class Entry(Base):
    __tablename__ = "Entry"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    fname = Column(Text)
    lname = Column(Text)
    dp_url = Column(String, nullable=False)
    created_on = Column(DateTime, default=datetime.utcnow)

# Creates async DB engine bound to SQLite file, core objects that manages connection to database.
engine = create_async_engine(DATABASE_URL)
# Factory for async sessions. Expire_on_commit=False keeps objects usable after commit. 
async_session_maker = async_sessionmaker(engine, expire_on_commit = False)

# Async function to create tables defined by models. Runs create_all on metadata inside a transaction.
async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Async generator that yields a DB session. Common FastAPI pattern: dependency injection for DB access in routes.
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session