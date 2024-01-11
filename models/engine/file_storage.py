#!/usr/bin/python3
"""The centeralized storage for the application
almost followed the singleton pattern"""
import json


class FileStorage:
    """Manipulate the file that's storing data"""
    __file_path = 'file.json'
    __objects = {}
    
    def __init__(self, **kwargs):
        if kwargs:
            FileStorage.__objects.update(kwargs)

    def all(self):
        """Returns __objects"""
        return self.__objects

    def new(self, obj):
        """"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        value = obj.__dict__
        FileStorage.__objects[key] = value

    def save(self):
        """Parsing the dict to file.json"""
        with open(self.__file_path, 'w') as file:
            data = json.dumps(self.__objects)
            file.write(data)
            print("Save_Test")

    def reload(self):
        """Loading the dict from file.json"""
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.loads(file.read())
                print("Reload_Test")
        except FileNotFoundError:
            print("No File")
            pass


if __name__ == '_main__':
    test = FileStorage({'name': 'Sameh', 'age': 28})
    test.save()
    test.reload()
    print(test.all())
