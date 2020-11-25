import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model import create_tables
from sales import Sales

import logging

logging.basicConfig(
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.DEBUG,
)


def get_data():
    res = requests.get(
        "https://www.domain.com.au/auction-results/api/city-summary/melbourne/2020-11-21"
    )
    return res.json()


def get_db():
    db_string = "postgres:///houses"
    return create_engine(db_string, echo=True)


def get_sales(json_data):
    auction_date = json_data.get("auctionDate")
    sales_listings = json_data.get("salesListings")
    sales = []
    for suburb_data in sales_listings:
        listings = suburb_data.get("listings", [])
        if not listings:
            continue
        for listing in listings:
            sales.append(Sales(listing, auction_date))
    return sales


def dump_sales(session, sales):
    logging.info("Dumping sales data...")
    for sale in sales:
        entry = sale.get_sales_model()
        session.add(entry)
    session.commit()


def main():
    logging.info("Starting script")
    db = get_db()
    Session = sessionmaker(db)
    session = Session()
    create_tables(db)
    json_data = get_data()
    sales = get_sales(json_data)
    dump_sales(session, sales)


if __name__ == "__main__":
    main()
