from os import getenv



DB_USER: str = getenv("PG_USER")
DB_PASS: str = getenv("PG_PASS")
DB_HOST: str = getenv("PG_HOST")
DB_PORT: int = getenv("PG_PORT")
DB_NAME: str = getenv("PG_NAME")

DATABASE_URL_asyncpg = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
