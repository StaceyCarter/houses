from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, MetaData, Table, String, DateTime, Float
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import Geometry
import datetime

base = declarative_base()
metadata = MetaData()


class SalesModel(base):
    __tablename__ = "sales"

    sales_id = Column(Integer, autoincrement=True, primary_key=True)
    entry_created = Column(DateTime, default=datetime.datetime.now())
    auction_date = Column(DateTime)
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
    price = Column(Float)
    result = Column(String(50))
    # TODO: Postgis stuff.. was hard to install on ec2. maybs come back to this in future.
    # geom = Column(Geometry(geometry_type="POINT", srid="4326"))  # 4326 is lat long
    longitude = Column(Float)  # 4326 is lat long
    latitude = Column(Float)  # 4326 is lat long


def create_tables(db):
    base.metadata.create_all(db)