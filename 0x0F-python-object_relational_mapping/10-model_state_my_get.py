#!/usr/bin/python3
"""Script which takes MySQL login and database info from argv to list
the State id belonging to the name given in argv[4], or "Not found"
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
    for instance in session.query(State).filter(State.name == sys.argv[4]):
        if instance:
            print(instance.id)
            break
    else:
        print("Not found")
