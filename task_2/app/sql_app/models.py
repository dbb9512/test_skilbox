"""В этом файле будут описаны все модели таблиц"""
from sqlalchemy import MetaData
from .database import engine
from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Text,
)

meta = MetaData()

cats = Table(
    "cats", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), server_default="None"),
    Column("breed", String(100), server_default="None"),
    Column("age", Integer),
    Column("description", Text, server_default="None"),
    Column("picture", String(100), server_default="None")
)

meta.create_all(engine)