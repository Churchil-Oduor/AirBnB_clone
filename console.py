#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel

""""this module holds the console program"""


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True

    def do_EOF(self, line):
        """"Exits the Console"""
        return True

    def do_create(self, arg):
        """
        creates a new instance of basemodel, saves
        it json file and prints the id.
        """
        if arg == "BaseModel":
            obj = BaseModel()
            obj.save()
            print("{}".format(obj.id))
        elif not arg:
            print("{}".format("** class name missing **"))
        else:
            print("{}".format("** class doesn't exist **"))

    def do_show(self, *arg):
        """
        Prints the string representation of an instance based
        on the class name and id.
        """
        print(*arg)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
