from model import SalesModel
import pprint


class Sales:
    def __init__(self, sales_dict):
        self.sales_model = self.create_entry(sales_dict)

    def create_entry(self, sales_dict):
        sales_model = SalesModel(
            auctionDate=sales_dict.get("auctionDate"),
            suburb=sales_dict.get("suburb"),
            street_number=sales_dict.get("streetNumber"),
            street_name=sales_dict.get("streetName"),
            street_type=sales_dict.get("streetType"),
            postcode=sales_dict.get("postcode"),
            state=sales_dict.get("state"),
            property_type=sales_dict.get("propertyType"),
            bedrooms=sales_dict.get("bedrooms"),
            car_spaces=sales_dict.get("carspaces"),
            bathrooms=sales_dict.get("bathrooms"),
            property_details_url=sales_dict.get("domainPropertyDetailsUrl"),
            agent=sales_dict.get("agent"),
            agency_name=sales_dict.get("agencyName"),
            geom=self.get_geometry_string(sales_dict.get("geoLocation")),
        )
        return sales_model

    def get_geometry_string(self, lat_long_dict):
        pass

    def get_sales_model(self):
        return self.sales_model

    def __str__(self):
        return f"{pprint.pformat(vars(self.get_sales_model()))}"
