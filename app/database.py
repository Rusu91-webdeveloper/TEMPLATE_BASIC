from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Create async database engine
engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URL, echo=True)

# Create session factory
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Dependency to get a database session
async def get_db():
    async with AsyncSessionLocal() as db:
        yield db