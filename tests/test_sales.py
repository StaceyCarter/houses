if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))

    __package__ = "houses"

from unittest import TestCase
import unittest
import json
from sales import Sales

from pathlib import Path


def get_test_listing():
    return {
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
    }


class TestSales(TestCase):
    def setUp(self):
        path = Path(__file__).parent / "./test_data.json"
        with path.open() as f:
            d = json.load(f)
            self.test_data = d

    def test_create(self):
        print("\n\n here")

        sales_data = Sales(get_test_listing())
        print("print S: ", sales_data)


if __name__ == "__main__":
    unittest.main()
