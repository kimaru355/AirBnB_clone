#!/usr/bin/python3

from base_model import BaseModel

class Review(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.place_id = ''
        self.user_id = ''
        self.text = ''
