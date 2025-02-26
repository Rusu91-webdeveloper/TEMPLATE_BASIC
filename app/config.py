from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_TYPE: str = "sqlite"
    DB_USERNAME: str | None = None
    DB_PASSWORD: str | None = None
    DB_HOST: str | None = None
    DB_PORT: str | None = None
    DB_NAME: str = "test.db"

    @property
    def SQLALCHEMY_DATABASE_URL(self) -> str:
        if self.DATABASE_TYPE == "sqlite":
            return f"sqlite+aiosqlite:///./{self.DB_NAME}"
        elif self.DATABASE_TYPE == "mysql":
            return f"mysql+aiomysql://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        elif self.DATABASE_TYPE == "postgres":
            return f"postgresql+asyncpg://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        raise ValueError(f"Unsupported DATABASE_TYPE: {self.DATABASE_TYPE}")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()