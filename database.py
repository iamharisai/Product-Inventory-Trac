from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import settings

DATABASE_URL = (
    f"postgresql://{settings.DB_USER}:{settings.DB_PASS}@"
    f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

engine = create_engine(url= DATABASE_URL)
session = sessionmaker(autocommit= False, autoflush=False, bind=engine)