from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, Integer, MetaData
from db_base import Base
from sqlalchemy.orm.session import sessionmaker
from url_tbl import Url

class PhishDB:
    def __init__(self):
        self.db_engine = create_engine("sqlite:///phish.sqlite")
        self.base = Base
        self.base.metadata.create_all(self.db_engine)
        self.sessionmaker = sessionmaker(bind=self.db_engine)
        print("Database Created")
    
    def get_url_rating(self, url):
        session = self.sessionmaker()
        our_url = session.query(Url).filter(Url.link == url).first()
        if our_url is None:
            return -1
        else:
            return our_url.rating
    
    def insert_url_rating(self, new_id, new_url, new_rating):
        session = self.sessionmaker()
        new_url = Url(id=new_id, link=new_url, rating=new_rating)
        session.add(new_url)
        try:
            session.commit()
        except Exception as ex:
            print("Exception occured inserting url rating.\n")
            print(ex)
            return ex
        return new_url
    
    def set_url_rating(self, url, new_rating):
        session = self.sessionmaker()
        our_url = session.query(Url).filter(Url.link == url).first()
        if our_url is None:
            return -1
        our_url.rating += 1
        try:
            session.commit()
        except Exception as ex:
            print("Exception occured setting url rating.\n")
            print(ex)
            return ex
        return our_url         

phish_db = PhishDB()
        
