from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import environ

SQLALCHEMY_DATABASE_URL = environ.get('DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)