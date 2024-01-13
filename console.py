#!/usr/bin/python3
"""The console of HBnB project,
to control the models and the storage engine"""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNB Console to control the storage engine
        Arguments:
            flag: Error flag
    """

    flag = 'error'
    

    def __init__(self, completeKey='tab', stdin=None, stdout=None):
        """HBNBCommand Constructor"""
        super().__init__(completekey=completeKey, stdin=stdin, stdout=stdout)
        self.prompt = '(hbnb) '

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

    def default(self, line):
        """"""
        if '.' in line:
            args = line.split('.')  
            if len(args) == 2:
                cls_name, cls_method = args # [User, all()]
                if cls_name in FileStorage.models_map:
                    methods_map = {
                        'create': self.do_create, 'show': self.do_show, 
                        'all': self.do_all, 'destroy': self.do_destroy,
                        'destroyall': self.do_destroyall, 'update': self.do_update
                    }
                if cls_method in methods_map:
                    methods_map[cls_method](cls_name)
                    return


    def help_quit(self):
        """The quit command help"""
        print('Quit command to exit the program\n')

    def help_EOF(self):
        """The EOF command help"""
        print('EOF command to exit the program\n')

    def do_create(self, line):
        """Createing a new instance of BaseModel,
            saves it (to the JSON file) and prints the id"""
        if self.check_line(line) == HBNBCommand.flag:
            return
        if self.check_name(line) == HBNBCommand.flag:
            return
        my_model = FileStorage.models_map[line]()
        my_model.save()
        print(my_model.id)

    def do_show(self, line):
        """Printing the string representation of an instance
            based on the class name """
        if self.check_line(line) == HBNBCommand.flag:
            return
        args = line.split(' ')
        length = len(args)
        if self.check_name(args[0]) == HBNBCommand.flag:
            return
        elif length == 1:
            print('** instance id missing **')
            return
        elif length == 2:
            obj_key = '.'.join([args[0], args[1]])
            if self.check_instance(obj_key) == HBNBCommand.flag:
                return
            print(self.all_objects()[obj_key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if self.check_line(line) == HBNBCommand.flag:
            return
        args = line.split(' ')
        length = len(args)
        if self.check_name(args[0]) == HBNBCommand.flag:
            return
        elif length == 1:
            print('** instance id missing **')
            return
        if length == 2:
            obj_key = '.'.join([args[0], args[1]])
            if self.check_instance(obj_key) == HBNBCommand.flag:
                return
            del self.all_objects()[obj_key]
            self.store_save()
            self.store_reload()

    def do_destroyall(self, line):
        """Deletes all instances from __object
            and from the file.json"""
        if line:
            print("** destroyall don't take any arguments **")
            return
        keys = list(self.all_objects().keys())
        for key in keys:
            del self.all_objects()[key]
        self.store_save()
        self.store_reload()

    def do_all(self, line):
        """Printing all string representation of all instances based,
            or not on the class name"""
        objects_list = []
        if not line:
            for val in self.all_objects().values():
                objects_list.append(val.__str__())
                print(objects_list)
        else:
            if self.check_name(line) == HBNBCommand.flag:
                return
            for key, val in self.all_objects().items():
                if key.split('.')[0] == line:
                    objects_list.append(val.__str__())
                    print(objects_list)
                else:
                    return

    def do_update(self, line):
        """Updating the instance by adding new attribute or,
            by updating the exising attribute"""
        if self.check_line(line) == HBNBCommand.flag:
            return
        args = line.split(' ')
        length = len(args)
        if length > 4:
            length = 4
        if length >= 2:
            obj_key = '.'.join([args[0], args[1]])
        if self.check_name(args[0]) == HBNBCommand.flag:
            return
        elif length == 1:
            print('** instance id missing **')
            return
        elif self.check_instance(obj_key) == HBNBCommand.flag:
            return
        elif length == 2:
            print('** attribute name missing **')
            return
        elif length == 3:
            print('** value missing **')
            return
        elif length == 4:
            if args[2] in ['id', 'created_at', 'updated_at']:
                return
            setattr(self.all_objects()[obj_key],
                    args[2], self.cast_attr(args[3]))
            self.store_save()
            self.store_reload()

    def cast_attr(self, var):
        """Editing the attr value before saving to the file.json"""
        var = var.strip('\'"')
        try:
            return int(var)
        except ValueError:
            try:
                return float(var)
            except ValueError:
                return str(var)

    def check_line(self, line):
        """Checking if the use didnot with the class name"""
        if not line:
            print('** class name missing **')
            return HBNBCommand.flag

    def check_name(self, name):
        """Checking if the use is writing the class name wrongly"""
        if name not in FileStorage.models_map:
            print('** class doesn\'t exist **')
            return HBNBCommand.flag

    def check_instance(self, key):
        """Checking if instance not found, by checking the obj_key"""
        if key not in FileStorage.all(self).keys():
            print('** no instance found **')
            return HBNBCommand.flag

    def all_objects(self):
        """returns __objects dict variable from file_storage"""
        return FileStorage.all(FileStorage)

    def store_save(self):
        """invokes save() func from file_storage"""
        FileStorage.save(FileStorage)

    def store_reload(self):
        """invokes reload() func from file_storage"""
        FileStorage.reload(FileStorage)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
