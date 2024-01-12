#!/usr/bin/python3
"""The console of HBnB project,
to control the models and the storage engine"""
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage


models_map = {
            'BaseModel': BaseModel, 'Amenity': Amenity,
            'City': City, 'Place': Place, 'Review': Review,
            'State': State, 'User': User
        }
error_flag = 'error'

class HBNBCommand(cmd.Cmd):
    """HBNB Console to control the storage engine"""

    def __init__(self, completeKey='tab', stdin=None, stdout=None):
        """HBNBCommand Constructor"""
        super().__init__(completekey=completeKey, stdin=stdin, stdout=stdout)
        self.prompt = '(hbnb) '

    def do_create(self, line):
        """"""
        if self.check_line(line) == error_flag:
            return
        if self.check_name(line) == error_flag:
            return
        my_model = models_map[line]()
        my_model.save()
        print(my_model.id)
        
    def do_s(self, line):
        """"""
        line_list = line.split(' ')
        obj_name = line_list[0]
        obj_id = line_list[1]
        obj_key = obj_name + '.' + obj_id
        if self.check_line(line) == error_flag:
            return
        if self.check_name(obj_name) == error_flag:
            return
        if self.check_id(obj_id) == error_flag:
            return
        if self.check_instance(obj_key) == error_flag:
            return


    def check_line(self, line):
        """"""
        if not line:
            print('** class name missing **')
            return error_flag

    def check_name(self, name):
        """"""
        if name not in models_map:
            print('** class doesn\'t exist **')
            return error_flag
        
    def check_id(self, id):
        """"""
        if id not in FileStorage.__objects.values().id:
            print('** instance id missing **')
            return error_flag
        
    def check_instance(self, key):
        """"""
        if key not in FileStorage.__objects:
            print('** no instance found **')
            return error_flag
        

    def emptyline(self):
        """Do nothing if the line is empty"""
        return

    def do_quit(self, line):
        """Quiting if line == quit"""
        return True

    def do_EOF(self, line):
        """Quiting with ctrl+d"""
        print('')
        return True

    def help_quit(self):
        """The quit command help"""
        print('Quit command to exit the program\n')

    def help_EOF(self):
        """The EOF command help"""
        print('EOF command to exit the program\n')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
