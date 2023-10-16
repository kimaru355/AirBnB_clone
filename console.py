#!/usr/bin/python3

from copy import deepcopy
import cmd
from models.base_model import BaseModel
from models.base_model import storage
from models.__init__ import all_classes

# Command line interpreter


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        'ignore empt line'
        pass

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF to exit the program'
        return True

    def do_create(self, *args):
        'Creates a new instance of a class'
        args = args[0].split(' ')
        if len(args) > 1:
            print("** pass one class name **")
        else:
            if args[0] == '':
                print("** class name missing **")
                return None
            try:
                my_model = eval(args[0])()
                storage.save()
                print(my_model.id)
            except NameError:
                print("** class name doesn't exist **")

    def do_show(self, *args):
        'Prints the string representation of an instance'
        args = args[0].split(' ')
        if len(args) == 1 and args[0] == '':
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) > 2:
            print("** pass class name and id **")
        else:
            if args[0] not in all_classes:
                print("** class name doesn't exist **")
                return None
            all_objs = storage.all()
            if not all_objs:
                print("** no instance found **")
                return None
            # copy to avoid error during iteration
            all_objs_copy = deepcopy(all_objs)
            for obj_id in all_objs_copy:
                obj = all_objs_copy[obj_id]
                if obj['id'] == args[1]:
                    my_model = eval(args[0])(obj)
                    print(my_model.__str__())
                    return None
            print("** no instance found **")

    def do_destroy(self, *args):
        'Deletes an instace of a class'
        args = args[0].split(' ')
        if len(args) == 1 and args[0] == '':
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) > 2:
            print("** pass class name and id **")
        else:
            try:
                eval(args[0])()
            except NameError:
                print("** class name doesn't exist **")
                return None
            all_objs = storage.all()
            all_remain = {}
            for obj_id in all_objs:
                obj = all_objs[obj_id]
                if obj['id'] != args[1]:
                    all_remain[obj_id] = obj

    def do_all(self, *args):
        'Prints all string representation of all instances'
        args = args[0].split(' ')
        if len(args) > 1:
            print("** pass class name or nothing **")
        else:
            if args[0] != '':
                if args[0] not in all_classes:
                    print("** class doesn't exist **")
                    return None
            my_all = []
            # reload to remove new instances not in the file
            storage.reload()
            all_objs = storage.all()
            if not all_objs:
                print("** no instances exist **")
                return None
            all_objs_copy = deepcopy(all_objs)
            if args[0] != '':
                for obj_id in all_objs_copy:
                    obj = all_objs_copy[obj_id]
                    if obj['__class__'] == args[0]:
                        my_model = eval(args[0])(obj)
                        my_all.append(my_model.__str__())
                if my_all:
                    print(my_all)
                else:
                    print("** no instances exist **")
            else:
                for obj_id in all_objs_copy:
                        obj = all_objs[obj_id]
                        my_model = eval(obj['__class__'])(obj)
                        my_all.append(my_model.__str__())
                if my_all:
                    print(my_all)

    def do_update(self, *args):
        'Updates an instance based on class name and id'
        args = args[0].split(' ')
        if args[0] == '':
            print("** class name missing **")
        elif len(args) < 2:
            print("** class instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif len(args) > 4:
            print("** pass class id attribute and value **")
        else:
            if args[0] not in all_classes:
                print("** class doesn't exist **")
                return None
            all_objs = storage.all()
            if not all_objs:
                print("** no instance found **")
                return None
            all_objs_copy = deepcopy(all_objs)
            for obj_id in all_objs_copy:
                obj = all_objs_copy[obj_id]
                if obj['__class__'] == args[0]:
                    if obj['id'] == args[1]:
                        if args[2] != 'id' and args[2] != 'updated_at' and args[2] != 'created_at':
                            my_model = eval(args[0])(obj)
                            attr = args[2]
                            my_model.attr = args[3]
                            my_model.save()
                            print(my_model)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
