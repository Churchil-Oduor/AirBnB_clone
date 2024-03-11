#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
""""this module holds the console program"""


class HBNBCommand(cmd.Cmd):
    """ Classs to handle the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ To quit from  the console
        """
        return True

    def do_EOF(self, line):
        """"Exits the Console
        """
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
        storage = FileStorage()
        objects = storage.__objects
        classes = ["BaseModel"]
        if arg:
            if len(arg) == 2:
                if arg[0] == "BaseModel":
                    try:
                        obj_key = "BaseModel."+str(arg[1])
                        obj = objects[obj_key]
                        print(obj)
                    except:
                        print("{}".format("** no instance found **"))
                else:
                    print("{}".format("** class doesn't exist **"))
            else:
                pass

        else:
            print("{}".format("** class name missing **"))



if __name__ == '__main__':
    HBNBCommand().cmdloop()
