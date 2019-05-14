from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, Integer, MetaData
from db_base import Base
from sqlalchemy.orm.session import sessionmaker
from url_tbl import Url
from increment_tbl import Increment

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
    
    def insert_url_rating(self, new_url, new_rating):
        session = self.sessionmaker()
        current_index = self.get_increment("url")
        if(current_index is None):
            current_index = self.create_increment("url")
        new_url = Url(id=current_index, link=new_url, rating=new_rating)
        session.add(new_url)
        try:
            session.commit()
        except Exception as ex:
            session.rollback()
            print("Exception occured inserting url rating.\n")
            print(ex)
            return ex
        self.increment_table_index("url")
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
            session.rollback()
            print("Exception occured setting url rating.\n")
            print(ex)
            return ex
        return our_url
    
    def increment_table_index(self, table_name):
        session = self.sessionmaker()
        increment_row = session.query(Increment).filter(Increment.table == table_name).first()

        #create increment if it doesnt exist
        if(increment_row is None):
            increment_row = Increment(id=table_name, value=0)
            session.add(increment_row)
            try:
                session.commit()
            except Exception as ex:
                session.rollback()
                print("Error creating table increment {0}\n".format(table_name))
                print(ex)
                return ex
        #increment the increment?
        increment_row.value += 1
        
        try:
            session.commit()
        except Exception as ex:
            session.rollback()
            print("Error incrementing table increment {0}\n".format(table_name))
            print(ex)
            return ex
        
        return increment_row
    
    def create_increment(self, tablename):
        session = self.sessionmaker()
        increment_row = Increment(table=tablename, value=0)
        session.add(increment_row)
        try:
            session.commit()
        except Exception as ex:
            session.rollback()
            print("Error creating table increment {0}\n".format(tablename))
            print(ex)
            return ex
        return increment_row.value
    
    def get_increment(self, table_name):
        session = self.sessionmaker()
        increment_row = session.query(Increment).filter(Increment.table == table_name).first()
        if(increment_row is None):
            return None
        return increment_row.value
    
    def get_all_increments(self):
        session = self.sessionmaker()
        return session.query(Increment).all()

phish_db = PhishDB()
        
