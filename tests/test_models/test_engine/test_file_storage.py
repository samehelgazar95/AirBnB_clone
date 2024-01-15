#!/usr/bin/python3
import unittest
import datetime
import models
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestBase(unittest.TestCase):

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    def test_does_module_has_doc(self):
        doc = models.engine.file_storage.__doc__
        self.assertTrue(len(doc) > 0)

    def test_does_class_has_doc(self):
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_is_FileStorage_a_class(self):
        b = FileStorage()
        cls_name = "<class 'models.engine.FileStorage'>"
        self.assertTrue(str(b.__class__), cls_name)

    def test_does_FileStorage_has_private_file_path(self):
        obj = FileStorage()
        self.assertEqual(str, type(obj._FileStorage__file_path))

    def test_does_FileStorage_has_private_objects(self):
        obj = FileStorage()
        self.assertEqual(dict, type(obj._FileStorage__objects))

    def test_FileStorage_all(self):
        obj = FileStorage()
        self.assertEqual(dict, type(obj.all()))


if __name__ == "__main__":
    unittest.main()
