#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    if models.HBNB_TYPE_STORAGE == 'db':
        __tablename__ = 'states'
        id = Column('id', String(60), primary_key=True)
        name = Column('name', String(128), nullable=False)
        cities = relationship('City', back_populates='state')
    else:
        name = ''
