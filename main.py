import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model import create_tables
from sales import Sales
from datetime import datetime, timedelta
import time
import click

import logging

logging.basicConfig(
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.DEBUG,
)

# This date works: "https://www.domain.com.au/auction-results/api/city-summary/melbourne/2020-11-21"


def get_city_data(city, date):
    base_path = "https://www.domain.com.au/auction-results/api/city-summary"
    res = requests.get(f"{base_path}/{city}/{date}")
    if res.status_code != 200:
        logging.info(f"No data for {city} on {date}")
        return None
    return res.json()


def get_data(date):
    cities = ["melbourne", "sydney", "brisbane"]
    responses = []
    for city in cities:
        response = get_city_data(city, date)
        if response:
            responses.append(response)
        time.sleep(5)
    return responses


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


def get_default_date():
    date_format = "%Y-%m-%d"
    yesterday = datetime.now() - timedelta(days=1)
    return yesterday.strftime(date_format)


@click.command()
@click.option(
    "--date",
    default=get_default_date(),
    help="Date you want to collect data for in the format yyyy-mm-dd eg.2020-11-21. Default date is yesterday.",
)
def main(date):
    logging.info("Starting script...")
    db = get_db()
    Session = sessionmaker(db)
    session = Session()
    create_tables(db)
    city_data_list = get_data(date)
    if not city_data_list:
        return

    for city_data in city_data_list:
        sales = get_sales(city_data)
        dump_sales(session, sales)

    logging.info("Finished dumping data...")


if __name__ == "__main__":
    main()
