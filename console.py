#!/usr/bin/python3

import cmd

# Command line interpreter


class MyConsole(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        'ignore empt line'
        pass

    def do_quit(self, arg):
        'Exit the terminal'
        return True

    def do_EOF(self, arg):
        'End of file'
        return True


if __name__ == '__main__':
    MyConsole().cmdloop()
