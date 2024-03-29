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

    def help_quit(self):
        """The quit command help"""
        print('Quit command to exit the program\n')

    def help_EOF(self):
        """The EOF command help"""
        print('EOF command to exit the program\n')

    def default(self, line):
        """Handling User.count(), User.all(), User.create()
            User.show(id), User.destroy(id),
            User.update(id, attr, val)
            Arguments:
                quotes: Using for stripping
                methods: methods map
                obj: Getting the instance
                method: Getting the method to execute
                all_params: The params to pass to method
            """
        if '.' in line:
            quotes = ' \'"'
            methods = {
                'create': self.do_create,
                'all': self.do_all,
                'count': self.do_count,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update
                }
            obj, rest = line.split('.', 1)
            method, params = rest.split('(', 1)

            if params == ')':
                # Handling no args, ex: args = ''
                all_params = obj
            else:
                if ',' not in params:
                    # Handling just id arg, ex: args = id
                    all_params = obj + ' ' + params.strip(quotes+')')
                elif ',' in params:
                    # Handling args for update(), id - key - val
                    id, items = params.split(',', 1)
                    id = id.strip(quotes)
                    items = items.strip(' )(')

                    if items.startswith('{') and items.endswith('}'):
                        all_params = obj + ' ' + id + ' ' + items
                    else:
                        # Handling just one item (key, val) passing to update()
                        k_and_v = [x.strip(quotes) for x in items.split(',')]
                        all_params = [obj, id] + k_and_v
                        all_params = ' '.join(all_params).strip(' ')
            # Invoking the proper method for each all_params
            if method in methods.keys():
                methods[method](all_params)
        else:
            cmd.Cmd.default(self, line)

    def do_create(self, line):
        """Creating a new instance and save it"""
        if self.check_line(line) == HBNBCommand.flag:
            return
        if self.check_name(line) == HBNBCommand.flag:
            return
        my_model = FileStorage.models_map[line]()
        my_model.save()
        print(my_model.id)

    def do_show(self, line):
        """Printing the string representation"""
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
        """Resetting everything"""
        keys = list(self.all_objects().keys())
        if line:
            if self.check_name(line) == HBNBCommand.flag:
                return
            for key in keys:
                obj_name, obj_id = key.split('.')
                if obj_name == line:
                    del self.all_objects()[key]
        else:
            for key in keys:
                del self.all_objects()[key]
        self.store_save()
        self.store_reload()

    def do_all(self, line):
        """Printing all string representation of all instances"""
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
        """Updating the instance by adding new attributes"""
        if self.check_line(line) == HBNBCommand.flag:
            return
        args = line.split(' ')
        quotes = ' "\''
        length = len(args)
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
            # Handling adding one attribute
            if self.attr_valid(args[2]) == HBNBCommand.flag:
                return
            setattr(self.all_objects()[obj_key],
                    args[2].strip(quotes), self.cast_attr(args[3]))
        elif length > 4:
            # Handling if there is a dictionary with valid items
            if args[2].startswith('{') and args[-1].endswith('}'):
                expected_dict = eval(' '.join(args[2:]))
                print(args)
                if type(expected_dict) == dict:
                    for k, v in expected_dict.items():
                        if self.attr_valid(args[2]) == HBNBCommand.flag:
                            return
                        setattr(self.all_objects()[obj_key],
                                k.strip(quotes), self.cast_attr(v))
            else:
                # Handling more than attr and no dictionary
                setattr(self.all_objects()[obj_key],
                        args[2].strip(quotes), self.cast_attr(args[3]))
                print(args)
        self.store_save()
        self.store_reload()

    def attr_valid(self, attr):
        if attr in ['id', 'created_at', 'updated_at']:
            return HBNBCommand.flag

    def do_count(self, line):
        """Counting How many instance are there"""
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
        try:
            return int(var)
        except ValueError:
            try:
                return float(var)
            except ValueError:
                var = var.strip(' \'"')
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
