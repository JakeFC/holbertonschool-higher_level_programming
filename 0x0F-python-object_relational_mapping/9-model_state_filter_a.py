#!/usr/bin/python3
"""Script which takes MySQL login and database info from argv to list
every State object with the letter 'a' in its name by id and name
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State):
        if 'a' in instance.name:
            print("{}: {}".format(instance.id, instance.name))
