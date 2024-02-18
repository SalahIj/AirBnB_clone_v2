#!/usr/bin/python
""" The imported modules """
import models
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv


class City(BaseModel, Base):
    """ Class representation
    Args:
        BaseModel:
        Base:
    """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """ The __init__ method
        Args:
            args:
            kwargs:
        """
        super().__init__(*args, **kwargs)
