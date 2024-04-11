#!/usr/bin/python3
"""
THis module contains City class mapper that inherits the\
        Base class for it to be able to be mapped to the cities\
        table in the database.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import ForeignKey

import sys
"""
Contains the class defination of a City which has foreign key\
        states_id that references states.id
"""

Base = declarative_base()


class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True,
                nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
