#!/usr/bin/python3
"""Module for City class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """SQLAlchemy-compatible subclass of Base with class attributes id, name,
    and foreign key state_id and link to cities table"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
