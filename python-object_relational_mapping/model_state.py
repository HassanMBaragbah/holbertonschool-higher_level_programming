#!/usr/bin/python3
"""
This module defines the State class and an instance Base
using SQLAlchemy for Object Relational Mapping (ORM).
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table 'states'.
    Attributes:
        id (int): An auto-generated, unique integer, primary key.
        name (str): A string of maximum 128 characters, cannot be null.
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
