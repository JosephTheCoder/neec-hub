import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()
db.UUID = UUID(as_uuid=True)

Base = declarative_base()


def create_tables():
    from app.models import  Note
    db.create_all()


def drop_tables():
    db.reflect()
    db.drop_all()


def create_testing_db():
    conn = db.engine.connect()
    conn.execute('commit')  # stop open transaction
    conn.execute('create database test_' + os.environ['APP_DB'])
    conn.close()