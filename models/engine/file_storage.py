#!/usr/bin/env python3
from json import dump, load

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
        data = []
        temp_dict = {}
        for key, value in FileStorage.__objects.items():
            temp_dict[key] = value.to_dict()
            data.append(temp_dict)

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file_json:
            dump(data, file_json, indent=4)


    def reload(self):
        """ Deserializes JSON file to objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as str_json:
                loaded_list = load(str_json)
                
            from models.base_model import BaseModel
            for item in loaded_list:
                for obj in item.values():
                    class_name = obj["__class__"]

                    if isinstance(class_name, str) and type(eval(class_name) == type):
                        self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            pass
