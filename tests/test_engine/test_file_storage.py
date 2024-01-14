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
        self.assertTrue(str(b.__class__), "<class 'models.engine.FileStorage'>")


if __name__ == "__main__":
    unittest.main()
