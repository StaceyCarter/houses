from model import SalesModel
import pprint
from datetime import datetime


class Sales:
    def __init__(self, sales_dict, auction_date):
        sales_data = self.create_data(sales_dict, auction_date)
        self.sales_model = self.create_entry(**sales_data)

    def create_entry(self, **kwargs):
        sales_model = SalesModel(**kwargs)
        return sales_model

    def create_data(self, sales_dict, auction_date):
        sales_data = {
            "auctionDate": self.get_date(auction_date),
            "suburb": sales_dict.get("suburb"),
            "street_number": sales_dict.get("streetNumber"),
            "street_name": sales_dict.get("streetName"),
            "street_type": sales_dict.get("streetType"),
            "postcode": sales_dict.get("postcode"),
            "state": sales_dict.get("state"),
            "property_type": sales_dict.get("propertyType"),
            "bedrooms": sales_dict.get("bedrooms"),
            "car_spaces": sales_dict.get("carspaces"),
            "bathrooms": sales_dict.get("bathrooms"),
            "property_details_url": sales_dict.get("domainPropertyDetailsUrl"),
            "agent": sales_dict.get("agent"),
            "agency_name": sales_dict.get("agencyName"),
            "geom": self.get_geometry_string(sales_dict.get("geoLocation")),
            "price": sales_dict.get("price"),
            "result": sales_dict.get("result"),
        }
        self.sales_data = sales_data
        return sales_data

    def get_geometry_string(self, lat_long_dict):
        if not lat_long_dict:
            return None
        lat = lat_long_dict.get("latitude")
        lon = lat_long_dict.get("longitude")
        return f"SRID=4326;POINT({lat} {lon})"

    def get_date(self, date_time_string):
        date_string = date_time_string.split("T")[
            0
        ]  # Get date only w/o timezone and time info
        date_format = "%Y-%m-%d"
        return datetime.strptime(date_string, date_format)

    def get_sales_model(self):
        return self.sales_model

    def __str__(self):
        return f"{pprint.pformat(self.sales_data)}"
