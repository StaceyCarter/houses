from unittest import TestCase
import unittest
import json
from ..sales import Sales

from pathlib import Path


class Test(TestCase):
    def setUp(self):
        path = Path(__file__).parent / "./test_data.json"
        with path.open() as f:
            d = json.load(f)
            self.test_data = d

    def test_create(self):
        import pprint

        pprint.pprint(self.test_data)
        print("here")


if __name__ == "__main__":
    unittest.main()
