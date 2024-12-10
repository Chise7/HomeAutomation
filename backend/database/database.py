from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'postgresql://<user>:<password>@localhost:<port>/homeautomation'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflash=False,bind=engine)

Base = declarative_base()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
