#!/usr/bin/python3
from models.engine.db_storage import DBStorage
from models.state import State

<<<<<<< HEAD
create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297
all Place
=======

storage = DBStorage()
storage.reload()
print(storage.all())
>>>>>>> parent of 155732b (stash)
