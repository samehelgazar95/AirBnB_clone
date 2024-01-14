#!/usr/bin/python3
"""Unit tests for file Base Class"""
import unittest
import datetime
import models
from models.place import Place


class TestBase(unittest.TestCase):
    """UnitTest for Base Class Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    def test_does_module_has_doc(self):
        self.assertTrue(len(models.place.__doc__) > 0)

    def test_does_class_has_doc(self):
        self.assertTrue(len(Place.__doc__) > 0)

    def test_is_place_a_class(self):
        obj = Place()
        self.assertTrue(str(obj.__class__), "<class 'models.place.Place'>")

    def test_does_Place_has_id_attr(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'id'))

    def test_does_Place_has_created_at_attr(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'created_at'))

    def test_does_Place_has_updated_at_attr(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_does_Place_has_city_id_attr(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'city_id'))

    def test_does_Place_has_user_id_attr(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'user_id'))

    def test_does_Place_has_name_attr(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'name'))

    def test_does_Place_has_description_attr(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'description'))

    def test_does_Place_has_number_rooms_attr(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'number_rooms'))

    def test_does_Place_has_number_bathrooms_attr(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'number_bathrooms'))

    def test_does_Place_has_max_guest_attr(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'max_guest'))

    def test_does_Place_has_price_by_night_attr(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'price_by_night'))

    def test_does_Place_has_latitude_attr(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'latitude'))

    def test_does_Place_has_longitude_attr(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'longitude'))

    def test_does_Place_has_amenity_ids_attr(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'amenity_ids'))

    def test_instantiation(self):
        """Test object creation and attribute setting."""
        obj = Place(description="delicious", max_guest=0)
        self.assertEqual(obj.description, "delicious")
        self.assertEqual(obj.max_guest, 0)


if __name__ == "__main__":
    unittest.main()
