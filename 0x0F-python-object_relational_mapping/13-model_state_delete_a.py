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

    for state in query:
        if 'a' in state.name:
            session.delete(state)
    session.commit()
    session.close()
