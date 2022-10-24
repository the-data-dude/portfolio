from enum import unique
from sqlalchemy import create_engine, Column, Float, String, Integer, Date
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def db_engine():
    return create_engine('sqlite:///quotes.db', echo = True)


def db_session():
    Session = sessionmaker(bind = db_engine())
    return Session()


class Quote(Base):
    __tablename__ = 'daily_quotes'

    id = Column(String, primary_key=True, unique = True)
    date = Column(String)
    currency = Column(String)
    value = Column(Float)

    def __repr__(self):
        return f"({self.date}, {self.currency}, {self.value})"


if __name__ == '__main__':
    
    engine = db_engine()
    Base.metadata.create_all(engine)
