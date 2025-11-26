from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Database URL - replace with actual database path as needed
DATABASE_URL = "sqlite:///./question_storage.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create all tables (for simple use; in production use migrations)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Yield a new database session.
    Usage:
        with get_db() as db:
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
