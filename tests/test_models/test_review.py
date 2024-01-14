#!/usr/bin/python3
"""Unit tests for file Base Class"""
import unittest
import datetime
import models
from models.review import Review


class TestBase(unittest.TestCase):
    """UnitTest for Base Class Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    def test_does_module_has_doc(self):
        self.assertTrue(len(models.review.__doc__) > 0)

    def test_does_class_has_doc(self):
        self.assertTrue(len(Review.__doc__) > 0)

    def test_is_review_a_class(self):
        b = Review()
        self.assertTrue(str(b.__class__), "<class 'models.review.Review'>")

    def test_does_review_has_id_attr(self):
        b = Review()
        self.assertTrue(hasattr(b, 'id'))

    def test_does_review_has_created_at_attr(self):
        b = Review()
        self.assertTrue(hasattr(b, 'created_at'))

    def test_does_review_has_updated_at_attr(self):
        b = Review()
        self.assertTrue(hasattr(b, 'updated_at'))


if __name__ == "__main__":
    unittest.main()
