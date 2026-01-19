from sqlalchemy import create_engine  #creates connection to database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "postgresql://postgres:psql@localhost:5432/library_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine) #to open temporary DB connection

# Base class for models
Base = declarative_base()

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()