#!/usr/bin/python3
"""
Creating City class
"""


import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    City class
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, auto_increment=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
