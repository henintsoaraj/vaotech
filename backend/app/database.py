from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:user_password@postgres:5432/vaotech"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)