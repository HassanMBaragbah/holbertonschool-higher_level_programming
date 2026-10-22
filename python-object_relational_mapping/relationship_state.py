#!/usr/bin/python3
"""
This module defines the State class with a relationship to City
using SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class linked to the MySQL table 'states' with a cities relationship.

    Attributes:
        id (int): An auto-generated, unique integer, primary key.
        name (str): A string of maximum 128 characters, cannot be null.
        cities (list): Relationship with City class, cascade delete.
    """
    __tablename__ = 'states'

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
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete, delete-orphan"
    )
