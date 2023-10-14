#!/usr/bin/python3

import uuid
from datetime import datetime
from models.__init__ import storage

# the base model
date_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "updated_at":
                    setattr(self, key, datetime.strptime(value, date_format))
                elif key == "created_at":
                    setattr(self, key, datetime.strptime(value, date_format))
                else:
                    setattr(self, key, value)
        else:
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            #storage.new()

    def save(self):
        self.updated_at = datetime.now()
        #storage.save()


    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        my_dict = {}
        my_dict['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == "updated_at":
                my_dict[key] = self.updated_at.strftime(date_format)
            elif key == "created_at":
                my_dict[key] = self.created_at.strftime(date_format)
            else:
                my_dict[key] = value
        return my_dict
