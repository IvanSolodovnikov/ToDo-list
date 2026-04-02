from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker,  AsyncSession
from collections.abc import AsyncGenerator

from os import getenv
from dotenv import load_dotenv

load_dotenv()

DB_URL = getenv("DB_URL", "sqlite+aiosqlite:///./app.db")
DB_POOL = int(getenv("DB_POOL", "5"))
DB_MAX_OVERFLOW = int(getenv("DB_MAX_OVERFLOW", "10"))

engine = create_async_engine(
    url=DB_URL,
    pool_size=DB_POOL,
    max_overflow=DB_MAX_OVERFLOW,
)

async_session_maker = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()