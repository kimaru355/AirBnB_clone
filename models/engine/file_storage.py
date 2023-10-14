#!/usr/bin/python3

import json


class FileStorage():
    def __init__(self):
        self.__file_path = "my_file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        for key, value in obj.items():
            setattr(self, self.__objects[key], value)

    def save(self):
        with open(self.__file_path, 'a') as file:
            json.dump(self.__object, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                setattr(self, self.__objects, json.loads(file.read()))
        except FileNotFoundError:
            pass
