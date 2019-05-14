from db_base import Base
from sqlalchemy import Table, Column, Integer, String

class Url(Base):
    __tablename__ = "url"
    id = Column(Integer, primary_key=True)
    link = Column(String)
    rating = Column(Integer)