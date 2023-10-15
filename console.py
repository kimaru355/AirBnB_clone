#!/usr/bin/python3

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
                my_model.save()
                print(my_model.id)
            except NameError:
                print("** class name doesn't exist **")

    def do_show(self, *args):
        'Prints the string representation of an instance'
        args = args[0].split(' ')
        if len(args) == 1 and args[0] == '':
            print("** class name missing **")
        elif len(args) == 1:
            print(args)
            print(len(args))
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
                    break


if __name__ == '__main__':
    HBNBCommand().cmdloop()
