if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))

    __package__ = "houses"

from unittest import TestCase
import unittest
import json
import datetime
from sales import Sales
from model import SalesModel
from main import extract_data

from pathlib import Path


def get_test_listing():
    return {
        "test_listing": {
            "streetNumber": "4",
            "streetName": "Alma",
            "streetType": "St",
            "suburb": "Aberfeldie",
            "postcode": "3040",
            "state": "Vic",
            "geoLocation": {"latitude": -37.757401, "longitude": 144.9034335},
            "propertyType": "House",
            "bedrooms": 4,
            "bathrooms": 2,
            "carspaces": 4,
            "price": 1700000,
            "result": "AUVB",
            "agent": "Nelson Alexander Essendon",
            "domainId": "2016543328",
            "domainAgencyId": "4722",
            "agencyName": "Nelson Alexander Essendon",
            "agencyProfilePageUrl": "http://www.domain.com.au/real-estate-agencies/nelsonalexanderessendon-4722",
            "domainPropertyDetailsUrl": "https://www.domain.com.au/4-alma-street-aberfeldie-vic-3040-2016543328",
        },
        "expected_result": {
            "agency_name": "Nelson Alexander Essendon",
            "agent": "Nelson Alexander Essendon",
            "auctionDate": datetime.datetime(2020, 11, 21, 0, 0),
            "bathrooms": 2,
            "bedrooms": 4,
            "car_spaces": 4,
            "geom": "SRID=4326;POINT(-37.757401 144.9034335)",
            "postcode": "3040",
            "property_details_url": "https://www.domain.com.au/4-alma-street-aberfeldie-vic-3040-2016543328",
            "property_type": "House",
            "state": "Vic",
            "street_name": "Alma",
            "street_number": "4",
            "street_type": "St",
            "suburb": "Aberfeldie",
        },
    }


class TestSales(TestCase):
    def test_create_sales_entry(self):
        listing = get_test_listing()
        test_listing = listing["test_listing"]
        expected_sales_data = listing["expected_result"]
        entry = Sales(test_listing, "2020-11-21T00:00:00")
        self.assertIsInstance(entry.get_sales_model(), SalesModel)
        self.assertDictEqual(entry.sales_data, expected_sales_data)


class TestExtractData(TestCase):
    def setUp(self):
        path = Path(__file__).parent / "./test_data.json"
        with path.open() as f:
            d = json.load(f)
            self.test_data = d

    def test_extract_data(self):
        pass


if __name__ == "__main__":
    unittest.main()
