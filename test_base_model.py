#!/usr/bin/python3

from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = 'My First Model'
my_model.my_number = 89
print(my_model)
print(my_model.name, my_model.id, my_model.my_number)
my_model.save()
print(my_model)
