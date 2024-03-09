#!/usr/bin/env python3
import cmd


""""this module holds the console program"""


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True

    def do_EOF(self, line):
        """"Exits the Console"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
