#!/usr/bin/python3
"""Module for State class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """SQLAlchemy-compatible subclass of Base with class attributes id and
    name and link to states table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='states', cascade="all, delete",
        passive_deletes=True)
    state = cities.name
