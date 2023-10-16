#!/usr/bin/python3

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
all_classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']
