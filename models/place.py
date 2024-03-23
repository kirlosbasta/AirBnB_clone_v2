#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', ForeignKey('places.id'), primary_key=True),
                          Column('amenity_id', ForeignKey('amenities.id'), primary_key=True))
    amenities = relationship('Amenity', secondary='place_amenity', viewonly=False)
    

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        amenity_ids = []
        @property
        def amenities(self):
            '''returns the list of Amenity instances'''
            amenity = []
            for obj in models.storage.all(Amenity).values():
                if obj.id in amenity_ids:
                    amenity.append(obj)
            return amenity
        @amenities.setter
        def amenities(self, obj):
            '''setter'''
            if type(obj) == 'Amenity':
                amenity_ids.append(obj.id)
