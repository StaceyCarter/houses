from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, MetaData, Table, String, DateTime
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import Geometry

base = declarative_base()
metadata = MetaData()

class Queries(base):  
    __tablename__ = 'queries'

    query_id = Column(Integer, autoincrement=True, primary_key=True)
    date_executed = Column(DateTime)
    auction_date_retrieved = Column(DateTime)
    number_listed_for_auction = Column(Integer)
    number_withdrawn = Column(Integer)
    number_unreported = Column(Integer)
    number_auctioned = Column(Integer)
    number_sold = Column(Integer)


class Sales(base):
    __tablename__ = "sales"

    sales_id = Column(Integer, autoincrement=True, primary_key=True)
    auctionDate = Column(DateTime)
    suburb = Column(String(200))
    street_number = Column(String(200))
    street_name = Column(String(200))
    street_type = Column(String(200))
    postcode = Column(String(200))
    state = Column(String(200))
    property_type = Column(String(200))
    bedrooms = Column(Integer)
    car_spaces = Column(Integer)
    bathrooms = Column(Integer)
    property_details_url = Column(String(400))
    agent = Column(String(400))
    agency_name = Column(String(400))
    geom = Column(Geometry(geometry_type='POINT', srid='4362')) #4362 is lat long

def create_tables(db):
    base.metadata.create_all(db)