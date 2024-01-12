#!/usr/bin/python3
"""The centeralized storage for the application
almost followed the singleton pattern"""
import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


models_map = {
            'BaseModel': BaseModel, 'Amenity': Amenity,
            'City': City, 'Place': Place, 'Review': Review,
            'State': State, 'User': User
        }

class FileStorage:
    """Manipulate the file that's storing data
        Arguments:
            __file_path: to store the JSON format
            __objects: {ClassName.id: Object, ClassName.id: Object}
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Simple function returns the private __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Writing new obj dict to file.json"""
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def reload(self):
        """Loading the dict from file.json"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                try:
                    data = json.load(file)
                    if not isinstance(data, dict) or not data:
                        return
                    self.new_objects(data)
                except json.decoder.JSONDecodeError:
                    return

    @staticmethod
    def new_objects(data):
        """Create new __objects with every reload()"""
        FileStorage.__objects = {}
        for key, val in data.items():
            cls_name = val.get('__class__')
            if cls_name:
                new_obj = models_map[cls_name](**val)
                FileStorage.__objects[key] = new_obj
