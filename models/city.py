#!/usr/bin/python3
<<<<<<< HEAD
""" City Module for HBNB project """
=======
"""BACKUP VERSION"""
>>>>>>> master
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
<<<<<<< HEAD
=======

>>>>>>> master
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
