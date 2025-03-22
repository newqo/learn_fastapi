from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Create SQLAlchemy engine
SQLALCHEMY_DARABASE_URL = os.getenv("DARABASE_URL")

engine = create_engine(
    SQLALCHEMY_DARABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base =declarative_base()

# Dependency - Define DB Session
def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()