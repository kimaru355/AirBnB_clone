#!/usr/bin/python3

import json


class FileStorage():
    def __init__(self):
        self.__file_path = "my_file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj['__class__']}.{obj['id']}"
        print(self.__objects)
        self.__objects[key] = obj
        print(self.__objects)

    def save(self):
        with open(self.__file_path, 'a') as file:
            json.dump(self.__objects, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.loads(file.read())
        except FileNotFoundError:
            pass
