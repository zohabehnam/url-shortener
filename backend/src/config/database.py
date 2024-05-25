import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DB_URL = "postgresql://dev:dev@db:5432/dev"
DB_URL = f"""postgresql://{os.getenv("DB_USER", "dev")}:{
    os.getenv("DB_PASSWORD", "dev")}@{os.getenv("DB_HOST", "db")
                                      }:{os.getenv("DB_PORT", "5432")}/{
                                          os.getenv("DB_NAME", "dev")}"""

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
