#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import storage_switch


class Review(BaseModel, Base):
    """
    The Review model

    Arguments:
        __tablename__: Database table
        place_id (str): Unique Place id.
        user_id (str): Unique user id.
        text (str): Review.
    """
    __tablename__ = 'reviews'
    if storage_switch == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
