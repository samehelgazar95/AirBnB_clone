#!/usr/bin/python3
"""Unit tests for file Base Class"""
import unittest
import datetime
import models
from models.city import City


class TestBase(unittest.TestCase):
    """UnitTest for Base Class Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    def test_does_module_has_doc(self):
        self.assertTrue(len(models.city.__doc__) > 0)

    def test_does_class_has_doc(self):
        self.assertTrue(len(City.__doc__) > 0)

    def test_is_City_a_class(self):
        obj = City()
        self.assertTrue(str(obj.__class__), "<class 'models.city.City'>")

    def test_does_City_has_id_attr(self):
        obj = City()
        self.assertTrue(hasattr(obj, 'id'))

    def test_does_City_has_created_at_attr(self):
        obj = City()
        self.assertTrue(hasattr(obj, 'created_at'))

    def test_does_City_has_updated_at_attr(self):
        obj = City()
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_does_City_has_state_id_attr(self):
        obj = City()
        self.assertTrue(hasattr(obj, 'state_id'))

    def test_does_City_has_name_attr(self):
        obj = City()
        self.assertTrue(hasattr(obj, 'name'))

    def test_instantiation(self):
        """Test object creation and attribute setting."""
        obj = City(state_id="123", name="Shebin El-Koum")
        self.assertEqual(obj.state_id, "123")
        self.assertEqual(obj.name, "Shebin El-Koum")

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        obj = City(state_id="123", name="Shebin El-Koum")
        self.assertIsNotNone(obj.state_id)


if __name__ == "__main__":
    unittest.main()
