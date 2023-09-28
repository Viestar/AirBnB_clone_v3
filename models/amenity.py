#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_switch
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """
    The Amenity model

    Argument:
        name (str): Amenity name.
    """
    __tablename__ = 'amenities'
    if storage_switch == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
