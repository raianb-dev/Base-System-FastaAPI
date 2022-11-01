import sqlalchemy
from sqlalchemy import create_engine 

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://jhbiockfkomjxn:6ddbedefceb3f216b159a483d8f88429ecaeae03a4078785bec471209ee12f66@ec2-52-70-45-163.compute-1.amazonaws.com:5432/daund6m8qjmt1p"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
metadata = sqlalchemy.MetaData()
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
