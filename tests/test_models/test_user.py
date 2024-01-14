#!/usr/bin/python3
"""Unit tests for file Base Class"""
import unittest
import datetime
import models
from models.user import User


class TestBase(unittest.TestCase):
    """UnitTest for Base Class Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    def test_does_module_has_doc(self):
        self.assertTrue(len(models.user.__doc__) > 0)

    def test_does_class_has_doc(self):
        self.assertTrue(len(User.__doc__) > 0)

    def test_is_user_a_class(self):
        b = User()
        self.assertTrue(str(b.__class__), "<class 'models.user.User'>")

    def test_does_user_has_id_attr(self):
        b = User()
        self.assertTrue(hasattr(b, 'id'))

    def test_does_user_has_created_at_attr(self):
        b = User()
        self.assertTrue(hasattr(b, 'created_at'))

    def test_does_user_has_updated_at_attr(self):
        b = User()
        self.assertTrue(hasattr(b, 'updated_at'))

    def test_does_user_has_email_attr(self):
        b = User()
        self.assertTrue(hasattr(b, 'email'))

    def test_does_user_has_password_attr(self):
        b = User()
        self.assertTrue(hasattr(b, 'password'))
        
    def test_does_user_has_first_name_attr(self):
        b = User()
        self.assertTrue(hasattr(b, 'first_name'))
        
    def test_does_user_has_last_name_attr(self):
        b = User()
        self.assertTrue(hasattr(b, 'last_name'))
        
        
if __name__ == "__main__":
    unittest.main()
