#!/usr/bin/python3
"""Unit tests for file Base Class"""
import unittest
import datetime
import models
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """UnitTest for Base Class Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    def test_does_module_has_doc(self):
        self.assertTrue(len(models.base_model.__doc__) > 0)

    def test_does_class_has_doc(self):
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_is_basemodel_a_class(self):
        obj = BaseModel()
        cls_str = "<class 'models.base_model.BaseModel'>"
        self.assertTrue(str(obj.__class__), cls_str)

    def test_does_basemodel_has_id_attr(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))

    def test_does_basemodel_has_created_at_attr(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'created_at'))

    def test_does_basemodel_has_updated_at_attr(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)

    def test_str(self):
        obj = BaseModel()
        date = 2024, 1, 1, 1, 1, 1, int(0.123456*1000000)
        obj.created_at = datetime.datetime(date)
        cls_name = obj.to_dict()['__class__']
        excepted_str = f"[{cls_name}] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), excepted_str)

    def test_to_dict(self):
        obj = BaseModel()
        date = 2024, 1, 1, 0, 0, 0, int(0.123456*1000000)
        obj.created_at = datetime.datetime(date)
        expected_dict = {
            'id': obj.id,
            'created_at': '2024-01-01T00:00:00.123456',
            'updated_at': obj.updated_at.isoformat(),
            '__class__': obj.to_dict()['__class__']
        }
        self.assertEqual(obj.to_dict(), expected_dict)

    def test_save(self):
        obj = BaseModel()
        date = 2024, 1, 1, 0, 0, 0, int(0.123456*1000000)
        obj.created_at = datetime.datetime(date)
        expected_dict = {
            'id': obj.id,
            'created_at': '2024-01-01T00:00:00.123456',
            'updated_at': obj.updated_at.isoformat(),
            '__class__': obj.to_dict()['__class__']
        }
        self.assertEqual(obj.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
