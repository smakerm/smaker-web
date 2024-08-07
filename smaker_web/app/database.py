from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from fastapi import Depends

from ..core import setting
from typing import Annotated


async def get_db():
    async_engine = create_async_engine(str(setting.db_url), echo=True)
    Session = async_sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)
    try:
        session = Session()
        yield session
    finally:
        session.close()

SessionDep = Annotated[AsyncSession, Depends(get_db)]
