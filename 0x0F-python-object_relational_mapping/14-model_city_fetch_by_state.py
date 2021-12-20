#!/usr/bin/python3
"""
Connecting script with my database
"""


from model_state import State, Base
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from model_city import City

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
        argv[1], argv[2], 'localhost', argv[3]), pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    query = session.query(State, City).join(City)

    for state, city in query.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
