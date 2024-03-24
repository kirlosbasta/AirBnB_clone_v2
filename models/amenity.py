#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', ForeignKey('places.id'),
                             primary_key=True),
                      Column('amenity_id', ForeignKey('amenities.id'),
                             primary_key=True))


class Amenity(BaseModel, Base):
    '''class that define amenities'''
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
