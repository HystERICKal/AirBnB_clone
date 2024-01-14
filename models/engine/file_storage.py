#!/usr/bin/python3
"""The Module Filestorage"""
import json
import models


class FileStorage:
    """File storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """dict return"""
        return FileStorage.__objects

    def new(self, obj):
        """obj with key set here"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serialization"""
        the_dict = {}
        for i, j in FileStorage.__objects.items():
            the_dict[i] = j.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8")\
                as the_file:
            json.dump(the_dict, the_file)

    def reload(self):
        """deserialisation"""

        try:
            with open(self.__file_path, encoding="UTF8") as the_file:
                self.__objects = json.load(the_file)
            for i, j in self.__objects.items():
                holder = FileStorage.classes[j["__class__"]](**j)
                FileStorage.__objects[i] = holder
        except FileNotFoundError:
            pass
