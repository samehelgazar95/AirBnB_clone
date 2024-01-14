#!/usr/bin/python3
"""Unit tests for file Base Class"""
import unittest
import datetime
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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
        b = BaseModel()
        self.assertTrue(str(b.__class__), "<class 'models.base_model.BaseModel'>")

    def test_does_basemodel_has_id_attr(self):
        b = BaseModel()
        self.assertTrue(hasattr(b, 'id'))

    def test_does_basemodel_has_created_at_attr(self):
        b = BaseModel()
        self.assertTrue(hasattr(b, 'created_at'))

    def test_does_basemodel_has_updated_at_attr(self):
        b = BaseModel()
        self.assertTrue(hasattr(b, 'updated_at'))

    def test_str(self):
        b = BaseModel()
        b.created_at = datetime.datetime(2024, 1, 1, 1, 1, 1, 1.123456)
        cls_name = b.to_dict()['__class__']
        excepted_str = f"[{cls_name}] ({b.id}) {b.__dict__}"
        self.assertEqual(str(b), excepted_str)

    def test_to_dict(self):
        b = BaseModel()
        b.created_at = datetime.datetime(2024, 1, 1, 0, 0, 0, int(0.123456*1000000))
        expected_dict = {
            'id': b.id,
            'created_at': '2024-01-01T00:00:00.123456',
            'updated_at': b.updated_at.isoformat(),
            '__class__': b.to_dict()['__class__']
        }
        self.assertEqual(b.to_dict(), expected_dict)

    def test_to_dict(self):
        b = BaseModel()
        b.created_at = datetime.datetime(2024, 1, 1, 0, 0, 0, int(0.123456*1000000))
        expected_dict = {
            'id': b.id,
            'created_at': '2024-01-01T00:00:00.123456',
            'updated_at': b.updated_at.isoformat(),
            '__class__': b.to_dict()['__class__']
        }
        self.assertEqual(b.to_dict(), expected_dict)

if __name__ == "__main__":
    unittest.main()
