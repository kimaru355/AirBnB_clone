#!/usr/bin/python3

import cmd
from models.base_model import BaseModel

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

    def show(self, *args):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
