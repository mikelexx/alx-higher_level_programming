#!/usr/bin/python3
"""
This module maps classes to database tables/records.
Classes mapped using the Declarative system are defined in terms \
        of a base class(Base) which maintains a catalog of classes and tables \
        relative to that base - this is known as the declarative base class.
"""
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City
import sys


class State(Base):
    """
    This State class constructed via the Declarative system defines\
            information about our table "states", known as table\
            metadata.the metadat can then be used to emit actual\
            sql queries to the database via the enginthe metadat
            can then be used to emit actual sql queries to the \
            database via engine.
    """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True,
                nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete")
