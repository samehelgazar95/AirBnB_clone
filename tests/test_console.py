#!/usr/bin/python3
"""Unit tests for file Console Class"""
import sys
from io import StringIO
from contextlib import redirect_stdout
import unittest
from unittest.mock import patch
from ..console import HBNBCommand
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

    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            HBNBCommand().onecmd("help show")

        # Now you can assert the output captured by mock_stdout
        expected_output = "Expected help message for the show command"
        self.assertIn(expected_output, mock_stdout.getvalue())

    
    
if __name__ == "__main__":
    unittest.main()
