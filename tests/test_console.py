#!/usr/bin/python3
"""Unit tests for file Base Class"""
import os
from io import StringIO
import unittest
from unittest.mock import patch
from datetime import datetime
from models.engine.file_storage import FileStorage
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """UnitTest for Console Class Class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_console_methods(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('\n')
            self.assertEqual(f.getvalue(), '')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help')
            self.assertIsInstance(f.getvalue(), str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('quit')
            self.assertEqual(f.getvalue(), '')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('EOF')
            self.assertEqual(f.getvalue(), '\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help quit')
            msg = 'Quit command to exit the program'
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help quit')
            msg = 'Quit command to exit the program'
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help EOF')
            msg = 'EOF command to exit the program'
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('? EOF')
            msg = 'EOF command to exit the program'
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('? create')
            msg = "Creating a new instance and save it"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help create')
            msg = "Creating a new instance and save it"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('? show')
            msg = "Printing the string representation"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help show')
            msg = "Printing the string representation"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help destroy')
            msg = "Deletes an instance based on the class name and id"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('? destroy')
            msg = "Deletes an instance based on the class name and id"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('? all')
            msg = "Printing all string representation of all instances"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help all')
            msg = "Printing all string representation of all instances"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('? update')
            msg = "Updating the instance by adding new attributes"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help update')
            msg = "Updating the instance by adding new attributes"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help count')
            msg = "Counting How many instance are there"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('? count')
            msg = "Counting How many instance are there"
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), msg)


if __name__ == "__main__":
    unittest.main()
