#!/usr/bin/python3

from copy import deepcopy
import cmd
from models.base_model import BaseModel
from models.base_model import storage

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
            try:
                eval(args[0])()
            except NameError:
                print("** class name doesn't exist **")
                return None
            all_objs = storage.all()
            for obj_id in all_objs:
                obj = all_objs[obj_id]
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
                try:
                    eval(args[0])()
                except NameError:
                    print("** class name doesn't exist **")
                    return None
            my_all = []
            all_objs = storage.all()
            temp_objs = deepcopy(all_objs)
            if args[0] == '':
                for obj_id in temp_objs:
                    obj = temp_objs[obj_id]
                    my_model = BaseModel(obj)
                    my_all.append(my_model.__str__())
                print(my_all)
            else:
                for obj_id in temp_objs:
                    my_name = obj_id.split('.')
                    if my_name[0] == args[0]:
                        obj = temp_objs[obj_id]
                        my_model = eval(args[0])(obj)
                        my_all.append(my_model.__str__())
                print(my_all)

    def update(self, *args):
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
            try:
                eval(args[0])()
            except NameError:
                print("** class doesn't exist **")
                return None
            all_objs = storage.all()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
