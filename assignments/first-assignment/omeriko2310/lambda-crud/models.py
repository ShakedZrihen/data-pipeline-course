from sqlalchemy import Column, Integer, String, JSON, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Environment variables
db_name = os.getenv("POSTGRES_DB").strip()
db_user = os.getenv("POSTGRES_USER").strip()
db_password = os.getenv("POSTGRES_PASSWORD").strip()
db_host = os.getenv("POSTGRES_HOST").strip()

# Construct the DATABASE_URL dynamically
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON)


Base.metadata.create_all(bind=engine)
