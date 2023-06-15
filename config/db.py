from sqlalchemy import create_engine , MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("mysql+pymysql://root:0000@localhost:3306/tehwissav2")

"""engine = create_engine("mysql+pymysql://root:0000@localhost:3306/tehwissa")"""
"meta = MetaData()"
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"conn = engine.connect()"