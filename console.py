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
    """HBNBConsole to control the storage engine
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
        """Quitting if line == quit"""
        return True

    def do_EOF(self, line):
        """Quitting with ctrl+d"""
        print('')
        return True

    def default(self, line):
        """Handling User.count(), User.all(),
            User.show(id), User.destroy(id),
            User.update(id, attr, val)
            Arguments:
                method: Getting the method to execute
                obj: Getting the instance
                beg_params: char's index beginning of the params
                end_params: char's index ending of the params
                all_params: The params to pass to method

                =======================================
                = ALTERNITAVE CODE THAT I LIKED:
                = if '.' in line:
                =     obj, rest = line.split('.', 1)
                =     method, params = rest.split('(', 1)
                =     params = params.rstrip(')')
                =     params = [p.strip(' "\'') for p in params.split(',')]
                =     all_params = [obj] + params
                =     all_params = ' '.join(all_params)
                =     methods = {
                =         'all': self.do_all,
                =         'count': self.do_count,
                =         'show': self.do_show,
                =         'destroy': self.do_destroy,
                =         'update': self.do_update
                =     }
                =
                =     if method in methods:
                =        methods[method](all_params)
                =======================================
            """
        if '.' in line:
            args = line.split('.')
            if len(args) == 2:
                method = args[1][:args[1].find('(')]
                obj = args[0]
                beg_params = args[1].find('(') + 1
                end_params = args[1].find(')')
                all_params = args[1][beg_params:end_params].split(',')
                all_params.insert(0, obj)
                all_params = [x.strip(' "\'') for x in all_params]
                all_params = ' '.join(all_params).strip(' ')
                methods = {
                    'all': self.do_all,
                    'count': self.do_count,
                    'show': self.do_show,
                    'destroy': self.do_destroy,
                    'update': self.do_update
                    }
                if method in methods.keys():
                    methods[method](all_params)
        else:
            cmd.Cmd.default(self, line)

    def help_quit(self):
        """The quit command help"""
        print('Quit command to exit the program\n')

    def help_EOF(self):
        """The EOF command help"""
        print('EOF command to exit the program\n')

    def do_create(self, line):
        """Creating a new instance of BaseModel,
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
        else:
            if self.check_name(line) == HBNBCommand.flag:
                return
            for key, val in self.all_objects().items():
                if key.split('.')[0] == line:
                    objects_list.append(val.__str__())
        print(objects_list)

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

    def do_count(self, line):
        """Printing all string representation of all instances based,
            or not on the class name"""
        counter = 0
        if line:
            if self.check_name(line) == HBNBCommand.flag:
                return
            for key in self.all_objects().keys():
                if key.split('.')[0] == line:
                    counter += 1
        elif not line:
            return
        print(counter)

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
        if name not in FileStorage.models_map.keys():
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
