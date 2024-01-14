#!/usr/bin/python3
"""Testing amenity model"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenity(unittest.TestCase):
    """The testamenity class"""

    def testing_inheritence(self):
        """testing inheritance"""        
        amenity_test = Amenity()
        self.assertIsInstance(amenity_test, BaseModel)

    def testing_attributes(self):
        """testing the attributes"""
        amenity_test = Amenity()
        self.assertTrue("name" in amenity_test.__dir__())

    def testing_the_attribute_types(self):
        """testing attribute types"""
        amenity_test = Amenity()
        name_value = getattr(amenity_test, "name")
        self.assertIsInstance(name_value, str)
