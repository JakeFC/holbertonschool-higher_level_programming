#!/usr/bin/python3
"""Script which takes MySQL login and database info from argv to remove
States from the states table
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_obj = State(name='California')
    city_obj = City(name='San Francisco', state=state_obj)
    state_obj.cities.append(city_obj)
    session.add(state_obj)
    session.add(city_obj)
    session.commit()
