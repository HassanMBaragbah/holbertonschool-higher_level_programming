#!/usr/bin/python3
"""
This module defines the City class linked to the MySQL table 'cities'
and referencing State using SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    City class that links to the MySQL table 'cities'.

    Attributes:
        id (int): An auto-generated, unique integer, primary key.
        name (str): A string of 128 characters, cannot be null.
        state_id (int): Integer, foreign key to states.id, cannot be null.
        state (State): Reference to the State object.
    """
    __tablename__ = 'cities'

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True,
        unique=True
    )
    name = Column(
        String(128),
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
