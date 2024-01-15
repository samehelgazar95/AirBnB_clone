#!/usr/bin/python3
"""Unit tests for file Base Class"""
import unittest
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
        instance = User()
        self.assertTrue(str(instance.__class__), "<class 'models.user.User'>")

    def test_does_user_has_id_attr(self):
        instance = User()
        self.assertTrue(hasattr(instance, 'id'))

    def test_does_user_has_created_at_attr(self):
        instance = User()
        self.assertTrue(hasattr(instance, 'created_at'))

    def test_does_user_has_updated_at_attr(self):
        instance = User()
        self.assertTrue(hasattr(instance, 'updated_at'))

    def test_does_user_has_email_attr(self):
        instance = User()
        self.assertIsInstance(instance.email, str)

    def test_does_user_has_password_attr(self):
        instance = User()
        self.assertTrue(hasattr(instance, 'password'))

    def test_does_user_has_first_name_attr(self):
        instance = User()
        self.assertTrue(hasattr(instance, 'first_name'))

    def test_does_user_has_last_name_attr(self):
        instance = User()
        self.assertTrue(hasattr(instance, 'last_name'))

    def test_instantiation(self):
        """Test object creation and attribute setting."""
        instance = User(name="Sameh")
        self.assertEqual(instance.name, "Sameh")


if __name__ == "__main__":
    unittest.main()
