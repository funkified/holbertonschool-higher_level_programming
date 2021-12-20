#!/usr/bin/python3
"""
Connecting script with my database
"""
from relationship_city import City
from relationship_state import State, Base
from sys import argv
from sqlalchemy import create_engine, orm
from sqlalchemy.orm import sessionmaker
import sqlalchemy

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
        argv[1], argv[2], 'localhost', argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    new_state = State()
    new_city = City()
    new_state.name = 'California'
    new_city.name = 'San Francisco'
    new_state.cities = [new_city]

    session.add(new_state, new_city)
    session.commit()
    session.close()
