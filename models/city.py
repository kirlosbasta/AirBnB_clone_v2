#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if models.HBNB_TYPE_STORAGE == 'db':
        __tablename__ = 'cities'
        name = Column('name', String(128), nullable=False)
        state_id = Column('state_id', String(60), ForeignKey('states.id'))
        state = relationship('State', back_populates='cities')
    else:
        name = ''
        state_id = ''
