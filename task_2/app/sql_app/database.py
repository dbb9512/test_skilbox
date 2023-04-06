"""Тут описываем все соединения с базой данных."""

from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_ADDRESS = os.environ.get('DB_ADDRESS')
OS = os.environ.get('OS')
DB_PORT = os.environ.get('DB_PORT')


SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///postgres/data.db")


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, poolclass=NullPool
)
