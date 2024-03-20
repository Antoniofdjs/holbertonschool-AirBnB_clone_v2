#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        @property
        def cities(self):
            """
            Getter for cities related to a state using a FIlEStorage engine
            """
            from models import storage
            city_list = []

            cities_from_storage = storage.all(City)

            for city in cities_from_storage.values():
                # Match our current state id witt all cities.state_id
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
