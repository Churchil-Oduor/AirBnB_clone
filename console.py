#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
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
        classes = ["BaseModel", "User"]
        storage = FileStorage()
        storage.reload()
        reloaded_objs = storage.all()
        # creating keys of the class
        if len(arg):
            # checking if no variable has been passed
            print("{}".format("** class name missing **"))
        elif len(arg) == 2:
            if arg[0] in classes:
                obj_key = f"{arg[0]}.{arg[1]}"
                if obj_key in reloaded_objs:
                    obj = reloaded_obj[obj_key]
                    print("{}".format(obj))
                else:
                    print("{}".format("** no instance found **"))
            else:
                print("{}".format("** class doesn't exist **"))
        else:
            print("{}".format("** instance id missing **"))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
