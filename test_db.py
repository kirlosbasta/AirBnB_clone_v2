#!/usr/bin/python3
from models.engine.db_storage import DBStorage
from models.state import State


storage = DBStorage()
storage.reload()
print(storage.all())
