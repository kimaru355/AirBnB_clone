#!/usr/bin/python3

from base_model import BaseModel
from base_model import storage

class User(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
