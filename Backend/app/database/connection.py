from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

# 1. اكتب باسووردك الحقيقي هنا داخل علامات التنصيص (حتى لو فيه @ أو #)
password = quote_plus("0090Mirqah0090@") 

# 2. الرابط الآن سيتم تكوينه بشكل صحيح ومحمي
DATABASE_URL = f"postgresql://postgres:{password}@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()