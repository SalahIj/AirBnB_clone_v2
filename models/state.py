#!/usr/bin/python3
""" Imported necessery modules """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ The class definition
    Aargs:
        BaseModel
        Base
    """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ __init__ definition
        Args:
            args:
            kwargs
        """
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """ Getting a list of city instances """
            list_city = []
            cities_all = models.storage.all(City)
            for city in cities_all.values():
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
