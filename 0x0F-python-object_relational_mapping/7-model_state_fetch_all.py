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
# Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    session_query = session.query(State).order_by(State.id)
    for state in session_query:
        print("{}: {}".format(state.id, state.name))
    session.close()
