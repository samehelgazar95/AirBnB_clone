#!/usr/bin/python3
"""Unit tests for file Base Class"""
import sys
from io import StringIO
from contextlib import redirect_stdout
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review


class TestBase(unittest.TestCase):
    """UnitTest for Base Class Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass
    
    
if __name__ == "__main__":
    unittest.main()
