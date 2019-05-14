from db_base import Base
from sqlalchemy import Table, Column, String, Integer

class Increment(Base):
    __tablename__ = "increment"

    table = Column(String, primary_key=True)
    value = Column(Integer)