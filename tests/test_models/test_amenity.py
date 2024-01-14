#!/usr/bin/python3
"""Unit tests for file Amenity Class"""
import unittest
import datetime
import models
from models.amenity import Amenity


class TestBase(unittest.TestCase):
    """UnitTest for Base Class Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass
    
    def test_does_module_has_doc(self):
        self.assertTrue(len(models.amenity.__doc__) > 0)

    def test_does_class_has_doc(self):
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_is_Amenity_a_class(self):
        obj = Amenity()
        self.assertTrue(str(obj.__class__), "<class 'models.amenity.Amenity'>")

    def test_does_Amenity_has_id_attr(self):
        obj = Amenity()
        self.assertTrue(hasattr(obj, 'id'))

    def test_does_Amenity_has_created_at_attr(self):
        obj = Amenity()
        self.assertTrue(hasattr(obj, 'created_at'))

    def test_does_Amenity_has_updated_at_attr(self):
        obj = Amenity()
        self.assertTrue(hasattr(obj, 'updated_at'))
    
    def test_does_amenity_has_name_attr(self):
        obj = Amenity()
        self.assertTrue(hasattr(obj, 'name'))

    def test_instantiation(self):
        """Test object creation and attribute setting."""
        obj = Amenity(name="Share3 El Mdares")
        self.assertEqual(obj.name, "Share3 El Mdares")


if __name__ == "__main__":
    unittest.main()
