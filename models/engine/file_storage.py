#!/usr/bin/env python3
from json import dump, load
#from models.user import User

class FileStorage:
    """ Class for serializing and deserializing objects
    for persistent data storage"""
    # Creating private attributs
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ To return the dictionary __objects"""
        return FileStorage.__objects

    def new(self,obj):
        """sets in __objects dict the obj with key <obj class name>.id
        and object as value"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ Method serializes objects to JSON file"""
        temp_dict = {}
        for i, j in FileStorage.__objects.items():
            temp_dict[i] = j.to_dict()
            # Open JSON file for writing
            with open(FileStorage.__file_path, "a", encoding="utf-8") as file_json:
                dump(temp_dict, file_json)
                
    def reload(self):
        """ Deserializes JSON file to objects"""
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as str_json:
                deserial_jsonfile = load(str_json)
                for obj_val in deserial_jsonfile.values():
                    class_name = obj_val["__class__"]
                    # Valicate input to our dict for security & avoid unwanted values
                    if isinstance(class_name, str) and type(eval(class_name) == type):
                        # Process inputs using eval to get the class name
                        self.new(eval(class_name)(**obj_val))
        except FileNotFoundError:
            pass
