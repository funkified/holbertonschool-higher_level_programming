#!/usr/bin/python3
"""
Connecting script with my database
"""
from model_state import State, Base
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
        argv[1], argv[2], 'localhost', argv[3]))

    Session = sessionmaker(engine)
    session = Session()
    query = session.query(State).order_by(State.id)

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)
    session.close()
