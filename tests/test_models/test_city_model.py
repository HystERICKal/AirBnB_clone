#!/usr/bin/python3

"""Testing city model"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """The test cityclass"""

    def test_City_inheritance(self):
        """testing inheritance"""
        city_test = City()
        self.assertIsInstance(city_test, BaseModel)

    def test_User_attributes(self):
        city_test = City()
        self.assertTrue("state_id" in city_test.__dir__())
        self.assertTrue("name" in city_test.__dir__())

    def test_type_name(self):
        city_test = City()
        name = getattr(city_test, "name")
        self.assertIsInstance(name, str)
